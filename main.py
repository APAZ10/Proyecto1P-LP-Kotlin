from tkinter import *
import ply.lex as lex
import ply.yacc as yacc
import analizadorLex
import analizadorSint

class TextLineNumbers(Canvas):
    def __init__(self, *args, **kwargs):
        Canvas.__init__(self, *args, **kwargs)
        self.textwidget = None

    def attach(self, text_widget):
        self.textwidget = text_widget
        
    def redraw(self, *args):
        self.delete("all")

        i = self.textwidget.index("@0,0")
        while True :
            dline= self.textwidget.dlineinfo(i)
            if dline is None: break
            y = dline[1]
            linenum = str(i).split(".")[0]
            self.create_text(2,y,anchor="nw", text=linenum, font=("Courier",12))
            i = self.textwidget.index("%s+1line" % i)

class CustomText(Text):
    def __init__(self, *args, **kwargs):
        Text.__init__(self, *args, **kwargs)

        self._orig = self._w + "_orig"
        self.tk.call("rename", self._w, self._orig)
        self.tk.createcommand(self._w, self._proxy)

    def _proxy(self, *args):

        try:
            cmd = (self._orig,) + args
            result = self.tk.call(cmd)


            if (args[0] in ("insert", "replace", "delete") or 
                args[0:3] == ("mark", "set", "insert") or
                args[0:2] == ("xview", "moveto") or
                args[0:2] == ("xview", "scroll") or
                args[0:2] == ("yview", "moveto") or
                args[0:2] == ("yview", "scroll")
            ):
                self.event_generate("<<Change>>", when="tail")

            return result
        except:
            pass

class Analizador():

    def _on_change(self, event):
        self.linenumbers.redraw()

    def showErrors(self, errors, defaultMssg = "Ingrese lo que desea probar en el bloque Code"):
        self.txterrors.config(state="normal")
        self.txterrors.delete('1.0', "end")

        if len(errors) == 0:
            self.txterrors.insert("1.0", defaultMssg)
        else:
            for i in range(0, len(errors)):
                self.txterrors.insert("1.0", errors[len(errors) - 1- i] + "\n")
        errors.clear()
        self.txterrors.config(state="disabled")

    def datosPruebas(self):

        archivo = open("testFile.txt")
        data = archivo.read()

        self.code.config(state="normal")
        self.code.delete('1.0', "end")

        self.code.insert("1.0", data)

        archivo.close()

    def lexer(self, data):
        datos = {}
        lexer = lex.lex(module=analizadorLex)
            
        lexer.input(data)
        while True:
            tok = lexer.token()
            if not tok:
                break
            if tok.lineno in datos:
                datos[tok.lineno].append(tok)
            else:
                datos[tok.lineno] = [tok]
        return datos

    def boton_lexer(self):
        data = self.code.get("1.0", 'end-1c')
        analizadorLex.errors.clear()
        if len(data) == 0:
            self.showErrors(analizadorLex.errors)
        else:
            datos = self.lexer(data)
            self.populate(datos)
            self.showErrors(analizadorLex.errors, "No hay errores léxicos")

    def parser(self):
        data = self.code.get("1.0", 'end-1c')

        if len(data) == 0:
            self.showErrors(analizadorLex.errors)
        else:
            datos = self.lexer(data)
            self.populate(datos)
            
            parser = yacc.yacc(module=analizadorSint)
            data = self.code.get("1.0", 'end-1c')
            parser.parse(data)
            self.showErrors(analizadorSint.errors, "No hay errores sintácticos")

    def populate(self, data):
        
        self.txttokens.config(state="normal")
        self.txttokens.delete('1.0', "end")
        for i in list(data.keys())[::-1]:
            for y in list(data[i])[::-1]:
                self.txttokens.insert("1.0", y.type+" ")
            self.txttokens.insert("1.0", str(i)+" ")

            self.txttokens.insert("1.0", "\n")
            
        
    def clear_frame(self,frame):
        for widgets in frame.winfo_children():
            widgets.destroy()

    def __init__(self, window):
        self.window = window
        window.title("Lexer y Parser básico para Kotlin")
        window.geometry("1000x670")

        # Contenedor code
        contenedor_texto = Frame(window, width=60, height=15, bg="#F9C005")
        Label(contenedor_texto, text="Code").pack()
        self.code = CustomText(contenedor_texto, width=45, height=15, font=("Courier",12)) 
        self.sb = Scrollbar(contenedor_texto, orient="vertical", command=self.code.yview)
        self.code.configure(yscrollcommand=self.sb.set)
        self.linenumbers = TextLineNumbers(contenedor_texto, width=30)
        self.linenumbers.attach(self.code)

        self.sb.pack(side="right", fill="y")
        self.linenumbers.pack(side="left", fill="y")
        self.code.pack(side="right", fill="both", expand=True)

        self.code.bind("<<Change>>", self._on_change)
        self.code.bind("<Configure>", self._on_change)

        # contenedor consola
        contenedor_consola = Frame(window, width=60, height=15, bg="#F90505")
        Label(contenedor_consola, text="Errores").pack()
        self.txterrors = Text(contenedor_consola, width=45, height=15, font=("Courier",12))
        self.txterrors.config(state="disabled")
        self.txterrors.pack()

        # contenedor tokens
        self.contenedor_token = Frame(window, width=120, height=15, bg="#052CF9")
        Label(self.contenedor_token, text="Tokens").pack()
        self.txttokens = CustomText(self.contenedor_token, width=90, height=15, font=("Courier",12))

        self.sbTokens = Scrollbar(self.contenedor_token, orient="vertical", command=self.txttokens.yview)
        self.txttokens.configure(yscrollcommand=self.sbTokens.set)
        self.sbTokens.pack(side="right", fill="y")

        self.txttokens.config(state="disabled")
        self.txttokens.pack()

        # contenedor botones
        contenedor_botones = Frame(window, width=120, bg="#ababab")
        
        btn = Button(contenedor_botones,text="Léxico", command=self.boton_lexer)
        btn2 = Button(contenedor_botones,text="Sintáctico", command=self.parser)
        btn3 = Button(contenedor_botones,text="Prueba", command=self.datosPruebas)
        btn.pack(side=LEFT)
        btn2.pack(side=LEFT)
        btn3.pack(side=LEFT)

        contenedor_texto.grid(row=0, column=0, sticky="ew")
        contenedor_consola.grid(row=0, column=1, sticky="ew")
        self.contenedor_token.grid(row=1, column=0, columnspan=2, sticky="ew")
        contenedor_botones.grid(row=2, column=0, columnspan=2, sticky="n")

        self.code.focus()


window = Tk()
interfaz = Analizador(window)
window.mainloop()
