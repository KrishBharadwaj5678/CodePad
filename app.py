import streamlit as st
from streamlit_ace import st_ace

st.set_page_config(
    page_title="Your Code Creation Hub",
    page_icon="icon.png",
    menu_items={
        "About":"Dive into Code Pad, the perfect digital workspace for coding enthusiasts. Effortlessly select your favorite programming language and write your code in a sleek, user-friendly environment. Get creative with your coding ideas and keep your code neat and accessible with Code Pad!"
    }
)

tab1,tab2,tab3=st.tabs(["Code Editor","Settings",'Getting Started'])

with tab2:
   themes = {"Ambiance": "ambiance", "Chaos": "chaos", "Chrome": "chrome", "Clouds": "clouds", "Clouds Midnight": "clouds_midnight", "Cobalt": "cobalt", "Crimson Editor": "crimson_editor", "Dawn": "dawn", "Dracula": "dracula", "Dream Weaver": "dreamweaver", "Eclipse": "eclipse", "Github": "github", "Gob": "gob", "Gruvbox": "gruvbox", "Idle Fingers": "idle_fingers", "Iplastic": "iplastic", "Katzenmilch": "katzenmilch", "Kuroir": "kuroir", "Merbivore": "merbivore", "Merbivore Soft": "merbivore_soft", "Mono Industrial": "mono_industrial", "Monokai": "monokai", "Nord Dark": "nord_dark", "One Dark": "one_dark", "Pastel on dark": "pastel_on_dark", "Solarized Dark": "solarized_dark", "Solarized Light": "solarized_light", "Sql Server": "sqlserver", "Terminal": "terminal", "Textmate": "textmate", "Tomorrow": "tomorrow", "Tomorrow Night": "tomorrow_night", "Tomorrow Night Blue": "tomorrow_night_blue", "Tomorrow Night Bright": "tomorrow_night_bright", "Tomorrow Night Eighties": "tomorrow_night_eighties", "Twilight": "twilight", "Vibrant Ink": "vibrant_ink", "Xcode": "xcode"}

   languages = {
    "ABAP": ["abap", ".abap", "WRITE 'Hello, World!'. "],
    "ActionScript": ["actionscript", ".as", "trace('Hello, World!');"],
    "Ada": ["ada", ".ada", "with Ada.Text_IO; use Ada.Text_IO;\nbegin\n   Put_Line ('Hello, World!');\nend;"],
    "Apex": ["apex", ".apex", "System.debug('Hello, World!');"],
    "Arduino": ["arduino", ".ino", "void setup() {\n  Serial.begin(9600);\n  Serial.println('Hello, World!');\n}\nvoid loop() {}"],
    "Bash": ["bash", ".sh", "echo 'Hello, World!'"],
    "C": ["c", ".c", "#include <stdio.h>\nint main() {\n   printf('Hello, World!');\n   return 0;\n}"],
    "C++": ["cpp", ".cpp", "#include <iostream>\nint main() {\n   std::cout << 'Hello, World!';\n   return 0;\n}"],
    "C#": ["csharp", ".cs", "using System;\nclass Program {\n    static void Main() {\n        Console.WriteLine('Hello, World!');\n    }\n}"],
    "Clojure": ["clojure", ".clj", "(println 'Hello, World!')"],
    "CoffeeScript": ["coffeescript", ".coffee", "console.log 'Hello, World!'"],
    "ColdFusion": ["coldfusion", ".cfm", "<cfoutput>Hello, World!</cfoutput>"],
    "Crystal": ["crystal", ".cr", "puts 'Hello, World!'"],
    "ClojureScript": ["clojurescript", ".cljs", "(println 'Hello, World!')"],
    "D": ["d", ".d", "import std.stdio;\nvoid main() {\n   writeln('Hello, World!');\n}"],
    "Dart": ["dart", ".dart", "void main() {\n   print('Hello, World!');\n}"],
    "Eiffel": ["eiffel", ".eiffel", "class\n   HELLO_WORLD\ncreate\n   make\nfeature\n   make\n      do\n         print ('Hello, World!%N')\n      end\nend"],
    "Elixir": ["elixir", ".ex", "IO.puts 'Hello, World!'"],
    "Elm": ["elm", ".elm", "main = text 'Hello, World!'"],
    "Erlang": ["erlang", ".erl", "io:format('Hello, World!~n')."],
    "F#": ["fsharp", ".fs", "printfn 'Hello, World!'"],
    "Forth": ["forth", ".fs", ".\" Hello, World!\""],
    "Fortran": ["fortran", ".f90", "program Hello\n   print *, 'Hello, World!'\nend program Hello"],
    "Go": ["go", ".go", "package main\nimport 'fmt'\nfunc main() {\n   fmt.Println('Hello, World!')\n}"],
    "Groovy": ["groovy", ".groovy", "println 'Hello, World!'"],
    "HAML": ["haml", ".haml", "%p= 'Hello, World!'"],
    "Haskell": ["haskell", ".hs", "main = putStrLn 'Hello, World!'"],
    "HTML": ["html", ".html", "<!DOCTYPE html>\n<html>\n   <body>\n      <p>Hello, World!</p>\n   </body>\n</html>"],
    "JSON": ["json", ".json", '{ "message": "Hello, World!" }'],
    "Java": ["java", ".java", "public class HelloWorld {\n   public static void main(String[] args) {\n      System.out.println('Hello, World!');\n   }\n}"],
    "JavaScript": ["javascript", ".js", "console.log('Hello, World!');"],
    "Jinja2": ["jinja2", ".jinja", "{{ 'Hello, World!' }}"],
    "Julia": ["julia", ".jl", "println('Hello, World!')"],
    "Kotlin": ["kotlin", ".kt", "fun main() {\n   println('Hello, World!')\n}"],
    "Lisp": ["lisp", ".lisp", "(print 'Hello, World!')"],
    "LiveScript": ["livescript", ".ls", "console.log 'Hello, World!'"],
    "Lua": ["lua", ".lua", "print('Hello, World!')"],
    "MATLAB": ["matlab", ".m", "disp('Hello, World!')"],
    "Nim": ["nim", ".nim", "echo 'Hello, World!'"],
    "Objective-C": ["objectivec", ".m", "#import <Foundation/Foundation.h>\nint main() {\n   @autoreleasepool {\n      NSLog(@'Hello, World!');\n   }\n   return 0;\n}"],
    "OCaml": ["ocaml", ".ml", "print_endline 'Hello, World!'"],
    "Pascal": ["pascal", ".pas", "program HelloWorld;\nbegin\n   writeln('Hello, World!');\nend."],
    "Perl": ["perl", ".pl", "print 'Hello, World!\\n';"],
    "PHP": ["php", ".php", "<?php\n   echo 'Hello, World!';\n?>"],
    "Prolog": ["prolog", ".pl", ":- initialization(main).\nmain :- write('Hello, World!'), nl."],
    "Puppet": ["puppet", ".pp", "notify { 'Hello, World!': }"],
    "Python": ["python", ".py", "print('Hello, World!')"],
    "R": ["r", ".r", "cat('Hello, World!\\n')"],
    "Ruby": ["ruby", ".rb", "puts 'Hello, World!'"],
    "Rust": ["rust", ".rs", "fn main() {\n   println!('Hello, World!');\n}"],
    "SAS": ["sas", ".sas", "data _null_;\n   put 'Hello, World!';\nrun;"],
    "Scala": ["scala", ".scala", "object HelloWorld {\n   def main(args: Array[String]): Unit = {\n      println('Hello, World!')\n   }\n}"],
    "Scheme": ["scheme", ".scm", "(display 'Hello, World!')"],
    "Shell": ["shell", ".sh", "echo 'Hello, World!'"],
    "Smalltalk": ["smalltalk", ".st", "'Hello, World!' printNl"],
    "SQL": ["sql", ".sql", "CREATE TABLE HelloWorld (\n   message VARCHAR(50)\n);\nINSERT INTO HelloWorld (message) VALUES ('Hello, World!');"],
    "Squirrel": ["squirrel", ".nut", "print('Hello, World!');"],
    "Tcl": ["tcl", ".tcl", "puts 'Hello, World!'"],
    "TypeScript": ["typescript", ".ts", "console.log('Hello, World!');"],
    "VimScript": ["vim", ".vim", "echo 'Hello, World!'"],
    "XQuery": ["xquery", ".xqy", "xquery version '1.0';\n<message>Hello, World!</message>"],
    "XML": ["xml", ".xml", "<message>Hello, World!</message>"],
    "YAML": ["yaml", ".yaml", "message: 'Hello, World!'"]
  }


   language=st.selectbox("Select Language",languages,index=46)

   code=languages[language][2]
   extension=languages[language][1]
   language=languages[language][0]

   theme=st.selectbox("Select Editor Theme",themes.keys(),index=31)
   theme=themes[theme]

   font_size = st.number_input("Editor Font Size",value=17)

with tab1:

    download_btn=st.empty()

    code=st_ace(
        value=code,
        language=language,
        theme=theme,
        keybinding='vscode',
        min_lines=21,
        font_size=font_size,
        auto_update=True
    )

    download_btn.download_button("Download File",code,f"code{extension}")

with tab3:
    st.write("<h3 style='color:#00BFFF;'>Getting Started with CodePad</h3>", unsafe_allow_html=True)
    
    st.write("**Welcome to Code Pad!** Here’s how you can make the most out of our code editor:")
    
    st.write("1. **Select a Programming Language:**")
    st.write("   - Use the **Settings** tab to choose your preferred programming language for syntax highlighting.")
    
    st.write("2. **Write Your Code:**")
    st.write("   - In the **Code Editor** tab, type or paste your code into the editor.")
    
    st.write("3. **Customize Your Editor:**")
    st.write("   - Adjust the editor theme and font size in the **Settings** tab to match your preferences for a better coding experience.")
    
    st.write("4. **Explore Themes:**")
    st.write("   - Select different themes to change the appearance of the editor. This helps reduce eye strain and improves focus.")
    
    st.write("5. **Download and Organize:**")
    st.write("   - While you cannot execute code in CodePad, you can still download and organize your code for future reference.")