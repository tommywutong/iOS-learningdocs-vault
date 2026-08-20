---
title: GDB Internals
apple_id: TP40001009
resource_type: Guide
platform: Xcode Developer Tools
topic: Xcode
technology: null
published: '2013-04-23'
source_url: https://developer.apple.com/library/archive/documentation/DeveloperTools/gdb/gdbint/gdbint_7.html
archived_at: '2026-07-15T07:31:03.878533Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [GDB Internals](GDB%20Internals.md)


Go to the [first](Requirements.md), [previous](Symbol%20Handling.md), [next](Host%20Definition.md), [last](Index.md) section, [table of contents](GDB%20Internals.md).

---

# [Language Support](GDB%20Internals.md#apple-krhugnjy)

GDB's language support is mainly driven by the symbol reader,
although it is possible for the user to set the source language
manually.

GDB chooses the source language by looking at the extension
of the file recorded in the debug info; `.c' means C, `.f'
means Fortran, etc. It may also use a special-purpose language
identifier if the debug format supports it, like with DWARF.

## [Adding a Source Language to GDB](GDB%20Internals.md#apple-krhugnjz)

To add other languages to GDB's expression parser, follow the
following steps:

**_Create the expression parser._**
: 
This should reside in a file `lang-exp.y'. Routines for
building parsed expressions into a `union exp_element` list are in
`parse.c'.

Since we can't depend upon everyone having Bison, and YACC produces
parsers that define a bunch of global names, the following lines
__must__ be included at the top of the YACC parser, to prevent the
various parsers from defining the same global names:

```
#define yyparse         lang_parse
#define yylex           lang_lex
#define yyerror         lang_error
#define yylval          lang_lval
#define yychar          lang_char
#define yydebug         lang_debug
#define yypact          lang_pact
#define yyr1            lang_r1
#define yyr2            lang_r2
#define yydef           lang_def
#define yychk           lang_chk
#define yypgo           lang_pgo
#define yyact           lang_act
#define yyexca          lang_exca
#define yyerrflag       lang_errflag
#define yynerrs         lang_nerrs
```

At the bottom of your parser, define a `struct language_defn` and
initialize it with the right values for your language. Define an
`initialize_lang` routine and have it call
`` `add_language(lang_language_defn)' `` to tell the rest of GDB
that your language exists. You'll need some other supporting variables
and functions, which will be used via pointers from your
`lang_language_defn`. See the declaration of `struct
language_defn` in `language.h', and the other `\*-exp.y' files,
for more information.

**_Add any evaluation routines, if necessary_**
: 

If you need new opcodes (that represent the operations of the language),
add them to the enumerated type in `expression.h'. Add support
code for these operations in the `evaluate_subexp` function
defined in the file `eval.c'. Add cases
for new opcodes in two functions from `parse.c':
`prefixify_subexp` and `length_of_subexp`. These compute
the number of `exp_element`s that a given operation takes up.

**_Update some existing code_**
: Add an enumerated identifier for your language to the enumerated type
`enum language` in `defs.h'.
Update the routines in `language.c' so your language is included.
These routines include type predicates and such, which (in some cases)
are language dependent. If your language does not appear in the switch
statement, an error is reported.

Also included in `language.c' is the code that updates the variable
`current_language`, and the routines that translate the
`language_lang` enumerated identifier into a printable
string.

Update the function `_initialize_language` to include your
language. This function picks the default language upon startup, so is
dependent upon which languages that GDB is built for.

Update `allocate_symtab` in `symfile.c' and/or symbol-reading
code so that the language of each symtab (source file) is set properly.
This is used to determine the language to use at each stack frame level.
Currently, the language is set based upon the extension of the source
file. If the language can be better inferred from the symbol
information, please set the language of the symtab in the symbol-reading
code.

Add helper code to `print_subexp` (in `expprint.c') to handle any new
expression opcodes you have added to `expression.h'. Also, add the
printed representations of your operators to `op_print_tab`.

**_Add a place of call_**
: 
Add a call to `lang_parse()` and `lang_error` in
`parse_exp_1` (defined in `parse.c').

**_Use macros to trim code_**
: 
The user has the option of building GDB for some or all of the
languages. If the user decides to build GDB for the language
lang, then every file dependent on `language.h' will have the
macro `_LANG_lang` defined in it. Use `#ifdef`s to
leave out large routines that the user won't need if he or she is not
using your language.
Note that you do not need to do this in your YACC parser, since if GDB
is not build for lang, then `lang-exp.tab.o' (the
compiled form of your parser) is not linked into GDB at all.
See the file `configure.in' for how GDB is configured
for different languages.

**_Edit `Makefile.in'_**
: Add dependencies in `Makefile.in'. Make sure you update the macro
variables such as `HFILES` and `OBJS`, otherwise your code may
not get linked in, or, worse yet, it may not get `tar`red into the
distribution!

---

Go to the [first](Requirements.md), [previous](Symbol%20Handling.md), [next](Host%20Definition.md), [last](Index.md) section, [table of contents](GDB%20Internals.md).
