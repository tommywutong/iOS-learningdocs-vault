---
title: GNU Compiler Collection (GCC) 4.2 Internals
apple_id: TP40007093
resource_type: Guide
platform: Xcode Developer Tools
topic: null
technology: null
published: '2012-07-23'
source_url: https://developer.apple.com/library/archive/documentation/DeveloperTools/gcc-4.2.1/gccint/Label-Output.html
archived_at: '2026-07-15T07:31:02.180062Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [GNU Compiler Collection (GCC) 4.2 Internals](index.md)



Next: [Initialization](Initialization.md#apple-jfxgs5djmfwgs6tboruw63q),
Previous: [Uninitialized Data](Uninitialized-Data.md#apple-kvxgs3tjoruwc3djpjswilkemf2gc),
Up: [Assembler Format](Assembler-Format.md#apple-ifzxgzlnmjwgk4rnizxxe3lboq)

---

#### 15.21.4 Output and Generation of Labels

This is about outputting labels.

— Macro: __ASM_OUTPUT_LABEL__ (stream, name)
> A C statement (sans semicolon) to output to the stdio stream
> stream the assembler definition of a label named name.
> Use the expression `assemble_name (`stream`,` name`)` to
> output the name itself; before and after that, output the additional
> assembler syntax for defining the name, and a newline. A default
> definition of this macro is provided which is correct for most systems.

— Macro: __ASM_OUTPUT_INTERNAL_LABEL__ (stream, name)
> Identical to `ASM_OUTPUT_LABEL`, except that name is known
> to refer to a compiler-generated label. The default definition uses
> `assemble_name_raw`, which is like `assemble_name` except
> that it is more efficient.

— Macro: __SIZE_ASM_OP__
> A C string containing the appropriate assembler directive to specify the
> size of a symbol, without any arguments. On systems that use ELF, the
> default (in `config/elfos.h`) is ``"\t.size\t"`'; on other
> systems, the default is not to define this macro.
>
> Define this macro only if it is correct to use the default definitions
> of `ASM_OUTPUT_SIZE_DIRECTIVE` and `ASM_OUTPUT_MEASURED_SIZE`
> for your system. If you need your own custom definitions of those
> macros, or if you do not need explicit symbol sizes at all, do not
> define this macro.

— Macro: __ASM_OUTPUT_SIZE_DIRECTIVE__ (stream, name, size)
> A C statement (sans semicolon) to output to the stdio stream
> stream a directive telling the assembler that the size of the
> symbol name is size. size is a `HOST_WIDE_INT`.
> If you define `SIZE_ASM_OP`, a default definition of this macro is
> provided.

— Macro: __ASM_OUTPUT_MEASURED_SIZE__ (stream, name)
> A C statement (sans semicolon) to output to the stdio stream
> stream a directive telling the assembler to calculate the size of
> the symbol name by subtracting its address from the current
> address.
>
> If you define `SIZE_ASM_OP`, a default definition of this macro is
> provided. The default assumes that the assembler recognizes a special
> ``.`' symbol as referring to the current address, and can calculate
> the difference between this and another symbol. If your assembler does
> not recognize ``.`' or cannot do calculations with it, you will need
> to redefine `ASM_OUTPUT_MEASURED_SIZE` to use some other technique.

— Macro: __TYPE_ASM_OP__
> A C string containing the appropriate assembler directive to specify the
> type of a symbol, without any arguments. On systems that use ELF, the
> default (in `config/elfos.h`) is ``"\t.type\t"`'; on other
> systems, the default is not to define this macro.
>
> Define this macro only if it is correct to use the default definition of
> `ASM_OUTPUT_TYPE_DIRECTIVE` for your system. If you need your own
> custom definition of this macro, or if you do not need explicit symbol
> types at all, do not define this macro.

— Macro: __TYPE_OPERAND_FMT__
> A C string which specifies (using `printf` syntax) the format of
> the second operand to `TYPE_ASM_OP`. On systems that use ELF, the
> default (in `config/elfos.h`) is ``"@%s"`'; on other systems,
> the default is not to define this macro.
>
> Define this macro only if it is correct to use the default definition of
> `ASM_OUTPUT_TYPE_DIRECTIVE` for your system. If you need your own
> custom definition of this macro, or if you do not need explicit symbol
> types at all, do not define this macro.

— Macro: __ASM_OUTPUT_TYPE_DIRECTIVE__ (stream, type)
> A C statement (sans semicolon) to output to the stdio stream
> stream a directive telling the assembler that the type of the
> symbol name is type. type is a C string; currently,
> that string is always either ``"function"`' or ``"object"`', but
> you should not count on this.
>
> If you define `TYPE_ASM_OP` and `TYPE_OPERAND_FMT`, a default
> definition of this macro is provided.

— Macro: __ASM_DECLARE_FUNCTION_NAME__ (stream, name, decl)
> A C statement (sans semicolon) to output to the stdio stream
> stream any text necessary for declaring the name name of a
> function which is being defined. This macro is responsible for
> outputting the label definition (perhaps using
> `ASM_OUTPUT_LABEL`). The argument decl is the
> `FUNCTION_DECL` tree node representing the function.
>
> If this macro is not defined, then the function name is defined in the
> usual manner as a label (by means of `ASM_OUTPUT_LABEL`).
>
> You may wish to use `ASM_OUTPUT_TYPE_DIRECTIVE` in the definition
> of this macro.

— Macro: __ASM_DECLARE_FUNCTION_SIZE__ (stream, name, decl)
> A C statement (sans semicolon) to output to the stdio stream
> stream any text necessary for declaring the size of a function
> which is being defined. The argument name is the name of the
> function. The argument decl is the `FUNCTION_DECL` tree node
> representing the function.
>
> If this macro is not defined, then the function size is not defined.
>
> You may wish to use `ASM_OUTPUT_MEASURED_SIZE` in the definition
> of this macro.

— Macro: __ASM_DECLARE_OBJECT_NAME__ (stream, name, decl)
> A C statement (sans semicolon) to output to the stdio stream
> stream any text necessary for declaring the name name of an
> initialized variable which is being defined. This macro must output the
> label definition (perhaps using `ASM_OUTPUT_LABEL`). The argument
> decl is the `VAR_DECL` tree node representing the variable.
>
> If this macro is not defined, then the variable name is defined in the
> usual manner as a label (by means of `ASM_OUTPUT_LABEL`).
>
> You may wish to use `ASM_OUTPUT_TYPE_DIRECTIVE` and/or
> `ASM_OUTPUT_SIZE_DIRECTIVE` in the definition of this macro.

— Macro: __ASM_DECLARE_CONSTANT_NAME__ (stream, name, exp, size)
> A C statement (sans semicolon) to output to the stdio stream
> stream any text necessary for declaring the name name of a
> constant which is being defined. This macro is responsible for
> outputting the label definition (perhaps using
> `ASM_OUTPUT_LABEL`). The argument exp is the
> value of the constant, and size is the size of the constant
> in bytes. name will be an internal label.
>
> If this macro is not defined, then the name is defined in the
> usual manner as a label (by means of `ASM_OUTPUT_LABEL`).
>
> You may wish to use `ASM_OUTPUT_TYPE_DIRECTIVE` in the definition
> of this macro.

— Macro: __ASM_DECLARE_REGISTER_GLOBAL__ (stream, decl, regno, name)
> A C statement (sans semicolon) to output to the stdio stream
> stream any text necessary for claiming a register regno
> for a global variable decl with name name.
>
> If you don't define this macro, that is equivalent to defining it to do
> nothing.

— Macro: __ASM_FINISH_DECLARE_OBJECT__ (stream, decl, toplevel, atend)
> A C statement (sans semicolon) to finish up declaring a variable name
> once the compiler has processed its initializer fully and thus has had a
> chance to determine the size of an array when controlled by an
> initializer. This is used on systems where it's necessary to declare
> something about the size of the object.
>
> If you don't define this macro, that is equivalent to defining it to do
> nothing.
>
> You may wish to use `ASM_OUTPUT_SIZE_DIRECTIVE` and/or
> `ASM_OUTPUT_MEASURED_SIZE` in the definition of this macro.

— Target Hook: void __TARGET_ASM_GLOBALIZE_LABEL__ (FILE \*stream, const char \*name)
> This target hook is a function to output to the stdio stream
> stream some commands that will make the label name global;
> that is, available for reference from other files.
>
> The default implementation relies on a proper definition of
> `GLOBAL_ASM_OP`.

— Macro: __ASM_WEAKEN_LABEL__ (stream, name)
> A C statement (sans semicolon) to output to the stdio stream
> stream some commands that will make the label name weak;
> that is, available for reference from other files but only used if
> no other definition is available. Use the expression
> `assemble_name (`stream`,` name`)` to output the name
> itself; before and after that, output the additional assembler syntax
> for making that name weak, and a newline.
>
> If you don't define this macro or `ASM_WEAKEN_DECL`, GCC will not
> support weak symbols and you should not define the `SUPPORTS_WEAK`
> macro.

— Macro: __ASM_WEAKEN_DECL__ (stream, decl, name, value)
> Combines (and replaces) the function of `ASM_WEAKEN_LABEL` and
> `ASM_OUTPUT_WEAK_ALIAS`, allowing access to the associated function
> or variable decl. If value is not `NULL`, this C statement
> should output to the stdio stream stream assembler code which
> defines (equates) the weak symbol name to have the value
> value. If value is `NULL`, it should output commands
> to make name weak.

— Macro: __ASM_OUTPUT_WEAKREF__ (stream, decl, name, value)
> Outputs a directive that enables name to be used to refer to
> symbol value with weak-symbol semantics. `decl` is the
> declaration of `name`.

— Macro: __SUPPORTS_WEAK__
> A C expression which evaluates to true if the target supports weak symbols.
>
> If you don't define this macro, `defaults.h` provides a default
> definition. If either `ASM_WEAKEN_LABEL` or `ASM_WEAKEN_DECL`
> is defined, the default definition is ``1`'; otherwise, it is
> ``0`'. Define this macro if you want to control weak symbol support
> with a compiler flag such as `-melf`.

— Macro: __MAKE_DECL_ONE_ONLY__ (decl)
> A C statement (sans semicolon) to mark decl to be emitted as a
> public symbol such that extra copies in multiple translation units will
> be discarded by the linker. Define this macro if your object file
> format provides support for this concept, such as the ``COMDAT`'
> section flags in the Microsoft Windows PE/COFF format, and this support
> requires changes to decl, such as putting it in a separate section.

— Macro: __SUPPORTS_ONE_ONLY__
> A C expression which evaluates to true if the target supports one-only
> semantics.
>
> If you don't define this macro, `varasm.c` provides a default
> definition. If `MAKE_DECL_ONE_ONLY` is defined, the default
> definition is ``1`'; otherwise, it is ``0`'. Define this macro if
> you want to control one-only symbol support with a compiler flag, or if
> setting the `DECL_ONE_ONLY` flag is enough to mark a declaration to
> be emitted as one-only.

— Target Hook: void __TARGET_ASM_ASSEMBLE_VISIBILITY__ (tree decl, const char \*visibility)
> This target hook is a function to output to asm_out_file some
> commands that will make the symbol(s) associated with decl have
> hidden, protected or internal visibility as specified by visibility.

— Macro: __TARGET_WEAK_NOT_IN_ARCHIVE_TOC__
> A C expression that evaluates to true if the target's linker expects
> that weak symbols do not appear in a static archive's table of contents.
> The default is `0`.
>
> Leaving weak symbols out of an archive's table of contents means that,
> if a symbol will only have a definition in one translation unit and
> will have undefined references from other translation units, that
> symbol should not be weak. Defining this macro to be nonzero will
> thus have the effect that certain symbols that would normally be weak
> (explicit template instantiations, and vtables for polymorphic classes
> with noninline key methods) will instead be nonweak.
>
> The C++ ABI requires this macro to be zero. Define this macro for
> targets where full C++ ABI compliance is impossible and where linker
> restrictions require weak symbols to be left out of a static archive's
> table of contents.

— Macro: __ASM_OUTPUT_EXTERNAL__ (stream, decl, name)
> A C statement (sans semicolon) to output to the stdio stream
> stream any text necessary for declaring the name of an external
> symbol named name which is referenced in this compilation but
> not defined. The value of decl is the tree node for the
> declaration.
>
> This macro need not be defined if it does not need to output anything.
> The GNU assembler and most Unix assemblers don't require anything.

— Target Hook: void __TARGET_ASM_EXTERNAL_LIBCALL__ (rtx symref)
> This target hook is a function to output to asm_out_file an assembler
> pseudo-op to declare a library function name external. The name of the
> library function is given by symref, which is a `symbol_ref`.

— Target Hook: void __TARGET_ASM_MARK_DECL_PRESERVED__ (tree decl)
> This target hook is a function to output to asm_out_file an assembler
> directive to annotate used symbol. Darwin target use .no_dead_code_strip
> directive.

— Macro: __ASM_OUTPUT_LABELREF__ (stream, name)
> A C statement (sans semicolon) to output to the stdio stream
> stream a reference in assembler syntax to a label named
> name. This should add ``_`' to the front of the name, if that
> is customary on your operating system, as it is in most Berkeley Unix
> systems. This macro is used in `assemble_name`.

— Macro: __ASM_OUTPUT_SYMBOL_REF__ (stream, sym)
> A C statement (sans semicolon) to output a reference to
> `SYMBOL_REF` sym. If not defined, `assemble_name`
> will be used to output the name of the symbol. This macro may be used
> to modify the way a symbol is referenced depending on information
> encoded by `TARGET_ENCODE_SECTION_INFO`.

— Macro: __ASM_OUTPUT_LABEL_REF__ (stream, buf)
> A C statement (sans semicolon) to output a reference to buf, the
> result of `ASM_GENERATE_INTERNAL_LABEL`. If not defined,
> `assemble_name` will be used to output the name of the symbol.
> This macro is not used by `output_asm_label`, or the `%l`
> specifier that calls it; the intention is that this macro should be set
> when it is necessary to output a label differently when its address is
> being taken.

— Target Hook: void __TARGET_ASM_INTERNAL_LABEL__ (FILE \*stream, const char \*prefix, unsigned long labelno)
> A function to output to the stdio stream stream a label whose
> name is made from the string prefix and the number labelno.
>
> It is absolutely essential that these labels be distinct from the labels
> used for user-level functions and variables. Otherwise, certain programs
> will have name conflicts with internal labels.
>
> It is desirable to exclude internal labels from the symbol table of the
> object file. Most assemblers have a naming convention for labels that
> should be excluded; on many systems, the letter ``L`' at the
> beginning of a label has this effect. You should find out what
> convention your system uses, and follow it.
>
> The default version of this function utilizes `ASM_GENERATE_INTERNAL_LABEL`.

— Macro: __ASM_OUTPUT_DEBUG_LABEL__ (stream, prefix, num)
> A C statement to output to the stdio stream stream a debug info
> label whose name is made from the string prefix and the number
> num. This is useful for VLIW targets, where debug info labels
> may need to be treated differently than branch target labels. On some
> systems, branch target labels must be at the beginning of instruction
> bundles, but debug info labels can occur in the middle of instruction
> bundles.
>
> If this macro is not defined, then `(*targetm.asm_out.internal_label)` will be
> used.

— Macro: __ASM_GENERATE_INTERNAL_LABEL__ (string, prefix, num)
> A C statement to store into the string string a label whose name
> is made from the string prefix and the number num.
>
> This string, when output subsequently by `assemble_name`, should
> produce the output that `(*targetm.asm_out.internal_label)` would produce
> with the same prefix and num.
>
> If the string begins with ``*`', then `assemble_name` will
> output the rest of the string unchanged. It is often convenient for
> `ASM_GENERATE_INTERNAL_LABEL` to use ``*`' in this way. If the
> string doesn't start with ``*`', then `ASM_OUTPUT_LABELREF` gets
> to output the string, and may change it. (Of course,
> `ASM_OUTPUT_LABELREF` is also part of your machine description, so
> you should know what it does on your machine.)

— Macro: __ASM_FORMAT_PRIVATE_NAME__ (outvar, name, number)
> A C expression to assign to outvar (which is a variable of type
> `char *`) a newly allocated string made from the string
> name and the number number, with some suitable punctuation
> added. Use `alloca` to get space for the string.
>
> The string will be used as an argument to `ASM_OUTPUT_LABELREF` to
> produce an assembler label for an internal static variable whose name is
> name. Therefore, the string must be such as to result in valid
> assembler code. The argument number is different each time this
> macro is executed; it prevents conflicts between similarly-named
> internal static variables in different scopes.
>
> Ideally this string should not be a valid C identifier, to prevent any
> conflict with the user's own symbols. Most assemblers allow periods
> or percent signs in assembler symbols; putting at least one of these
> between the name and the number will suffice.
>
> If this macro is not defined, a default definition will be provided
> which is correct for most systems.

— Macro: __ASM_OUTPUT_DEF__ (stream, name, value)
> A C statement to output to the stdio stream stream assembler code
> which defines (equates) the symbol name to have the value value.
>
> If `SET_ASM_OP` is defined, a default definition is provided which is
> correct for most systems.

— Macro: __ASM_OUTPUT_DEF_FROM_DECLS__ (stream, decl_of_name, decl_of_value)
> A C statement to output to the stdio stream stream assembler code
> which defines (equates) the symbol whose tree node is decl_of_name
> to have the value of the tree node decl_of_value. This macro will
> be used in preference to ``ASM_OUTPUT_DEF`' if it is defined and if
> the tree nodes are available.
>
> If `SET_ASM_OP` is defined, a default definition is provided which is
> correct for most systems.

— Macro: __TARGET_DEFERRED_OUTPUT_DEFS__ (decl_of_name, decl_of_value)
> A C statement that evaluates to true if the assembler code which defines
> (equates) the symbol whose tree node is decl_of_name to have the value
> of the tree node decl_of_value should be emitted near the end of the
> current compilation unit. The default is to not defer output of defines.
> This macro affects defines output by ``ASM_OUTPUT_DEF`' and
> ``ASM_OUTPUT_DEF_FROM_DECLS`'.

— Macro: __ASM_OUTPUT_WEAK_ALIAS__ (stream, name, value)
> A C statement to output to the stdio stream stream assembler code
> which defines (equates) the weak symbol name to have the value
> value. If value is `NULL`, it defines name as
> an undefined weak symbol.
>
> Define this macro if the target only supports weak aliases; define
> `ASM_OUTPUT_DEF` instead if possible.

— Macro: __OBJC_GEN_METHOD_LABEL__ (buf, is_inst, class_name, cat_name, sel_name)
> Define this macro to override the default assembler names used for
> Objective-C methods.
>
> The default name is a unique method number followed by the name of the
> class (e.g. ``_1_Foo`'). For methods in categories, the name of
> the category is also included in the assembler name (e.g.
> ``_1_Foo_Bar`').
>
> These names are safe on most systems, but make debugging difficult since
> the method's selector is not present in the name. Therefore, particular
> systems define other ways of computing names.
>
> buf is an expression of type `char *` which gives you a
> buffer in which to store the name; its length is as long as
> class_name, cat_name and sel_name put together, plus
> 50 characters extra.
>
> The argument is_inst specifies whether the method is an instance
> method or a class method; class_name is the name of the class;
> cat_name is the name of the category (or `NULL` if the method is not
> in a category); and sel_name is the name of the selector.
>
> On systems where the assembler can handle quoted names, you can use this
> macro to provide more human-readable names.

— Macro: __ASM_DECLARE_CLASS_REFERENCE__ (stream, name)
> A C statement (sans semicolon) to output to the stdio stream
> stream commands to declare that the label name is an
> Objective-C class reference. This is only needed for targets whose
> linkers have special support for NeXT-style runtimes.

— Macro: __ASM_DECLARE_UNRESOLVED_REFERENCE__ (stream, name)
> A C statement (sans semicolon) to output to the stdio stream
> stream commands to declare that the label name is an
> unresolved Objective-C class reference. This is only needed for targets
> whose linkers have special support for NeXT-style runtimes.
