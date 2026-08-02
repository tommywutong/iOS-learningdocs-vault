---
title: GNU Compiler Collection (GCC) Internals
apple_id: TP40006804
resource_type: Guide
platform: Xcode Developer Tools
topic: null
technology: null
published: '2012-07-23'
source_url: https://developer.apple.com/library/archive/documentation/DeveloperTools/gcc-4.0.1/gccint/Sections.html
archived_at: '2026-07-15T07:31:00.698494Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [GNU Compiler Collection (GCC) Internals](index.md)



Next: [PIC](PIC.md#apple-kbeug),
Previous: [Scheduling](Scheduling.md#apple-knrwqzleovwgs3th),
Up: [Target Macros](Target-Macros.md#apple-krqxez3foqwu2yldojxxg)

---

### 13.17 Dividing the Output into Sections (Texts, Data, ...)

An object file is divided into sections containing different types of
data. In the most common case, there are three sections: the text
section, which holds instructions and read-only data; the data
section, which holds initialized writable data; and the bss
section, which holds uninitialized data. Some systems have other kinds
of sections.

The compiler must tell the assembler when to switch sections. These
macros control what commands to output to tell the assembler this. You
can also define additional sections.

— Macro: __TEXT_SECTION_ASM_OP__
> A C expression whose value is a string, including spacing, containing the
> assembler operation that should precede instructions and read-only data.
> Normally `"\t.text"` is right.

— Macro: __HOT_TEXT_SECTION_NAME__
> If defined, a C string constant for the name of the section containing most
> frequently executed functions of the program. If not defined, GCC will provide
> a default definition if the target supports named sections.

— Macro: __UNLIKELY_EXECUTED_TEXT_SECTION_NAME__
> If defined, a C string constant for the name of the section containing unlikely
> executed functions in the program.

— Macro: __DATA_SECTION_ASM_OP__
> A C expression whose value is a string, including spacing, containing the
> assembler operation to identify the following data as writable initialized
> data. Normally `"\t.data"` is right.

— Macro: __READONLY_DATA_SECTION_ASM_OP__
> A C expression whose value is a string, including spacing, containing the
> assembler operation to identify the following data as read-only initialized
> data.

— Macro: __READONLY_DATA_SECTION__
> A macro naming a function to call to switch to the proper section for
> read-only data. The default is to use `READONLY_DATA_SECTION_ASM_OP`
> if defined, else fall back to `text_section`.
>
> The most common definition will be `data_section`, if the target
> does not have a special read-only data section, and does not put data
> in the text section.

— Macro: __BSS_SECTION_ASM_OP__
> If defined, a C expression whose value is a string, including spacing,
> containing the assembler operation to identify the following data as
> uninitialized global data. If not defined, and neither
> `ASM_OUTPUT_BSS` nor `ASM_OUTPUT_ALIGNED_BSS` are defined,
> uninitialized global data will be output in the data section if
> `-fno-common` is passed, otherwise `ASM_OUTPUT_COMMON` will be
> used.

— Macro: __INIT_SECTION_ASM_OP__
> If defined, a C expression whose value is a string, including spacing,
> containing the assembler operation to identify the following data as
> initialization code. If not defined, GCC will assume such a section does
> not exist.

— Macro: __FINI_SECTION_ASM_OP__
> If defined, a C expression whose value is a string, including spacing,
> containing the assembler operation to identify the following data as
> finalization code. If not defined, GCC will assume such a section does
> not exist.

— Macro: __CRT_CALL_STATIC_FUNCTION__ (section_op, function)
> If defined, an ASM statement that switches to a different section
> via section_op, calls function, and switches back to
> the text section. This is used in `crtstuff.c` if
> `INIT_SECTION_ASM_OP` or `FINI_SECTION_ASM_OP` to calls
> to initialization and finalization functions from the init and fini
> sections. By default, this macro uses a simple function call. Some
> ports need hand-crafted assembly code to avoid dependencies on
> registers initialized in the function prologue or to ensure that
> constant pools don't end up too far way in the text section.

— Macro: __FORCE_CODE_SECTION_ALIGN__
> If defined, an ASM statement that aligns a code section to some
> arbitrary boundary. This is used to force all fragments of the
> `.init` and `.fini` sections to have to same alignment
> and thus prevent the linker from having to add any padding.

— Macro: __EXTRA_SECTIONS__
> A list of names for sections other than the standard two, which are
> `in_text` and `in_data`. You need not define this macro
> on a system with no other sections (that GCC needs to use).

— Macro: __EXTRA_SECTION_FUNCTIONS__
> One or more functions to be defined in `varasm.c`. These
> functions should do jobs analogous to those of `text_section` and
> `data_section`, for your additional sections. Do not define this
> macro if you do not define `EXTRA_SECTIONS`.

— Macro: __JUMP_TABLES_IN_TEXT_SECTION__
> Define this macro to be an expression with a nonzero value if jump
> tables (for `tablejump` insns) should be output in the text
> section, along with the assembler instructions. Otherwise, the
> readonly data section is used.
>
> This macro is irrelevant if there is no separate readonly data section.

— Target Hook: void __TARGET_ASM_SELECT_SECTION__ (tree exp, int reloc, unsigned HOST_WIDE_INT align)
> Switches to the appropriate section for output of exp. You can
> assume that exp is either a `VAR_DECL` node or a constant of
> some sort. reloc indicates whether the initial value of exp
> requires link-time relocations. Bit 0 is set when variable contains
> local relocations only, while bit 1 is set for global relocations.
> Select the section by calling `data_section` or one of the
> alternatives for other sections. align is the constant alignment
> in bits.
>
> The default version of this function takes care of putting read-only
> variables in `readonly_data_section`.
>
> See also USE_SELECT_SECTION_FOR_FUNCTIONS.

— Macro: __USE_SELECT_SECTION_FOR_FUNCTIONS__
> Define this macro if you wish TARGET_ASM_SELECT_SECTION to be called
> for `FUNCTION_DECL`s as well as for variables and constants.
>
> In the case of a `FUNCTION_DECL`, reloc will be zero if the
> function has been determined to be likely to be called, and nonzero if
> it is unlikely to be called.

— Target Hook: void __TARGET_ASM_UNIQUE_SECTION__ (tree decl, int reloc)
> Build up a unique section name, expressed as a `STRING_CST` node,
> and assign it to ``DECL_SECTION_NAME (decl)`'.
> As with `TARGET_ASM_SELECT_SECTION`, reloc indicates whether
> the initial value of exp requires link-time relocations.
>
> The default version of this function appends the symbol name to the
> ELF section name that would normally be used for the symbol. For
> example, the function `foo` would be placed in `.text.foo`.
> Whatever the actual target object format, this is often good enough.

— Target Hook: void __TARGET_ASM_FUNCTION_RODATA_SECTION__ (tree decl)
> Switches to a readonly data section associated with
> ``DECL_SECTION_NAME (decl)`'.
> The default version of this function switches to `.gnu.linkonce.r.name`
> section if function's section is `.gnu.linkonce.t.name`, to
> `.rodata.name` if function is in `.text.name` section
> and otherwise switches to the normal readonly data section.

— Target Hook: void __TARGET_ASM_SELECT_RTX_SECTION__ (enum machine_mode mode, rtx x, unsigned HOST_WIDE_INT align)
> Switches to the appropriate section for output of constant pool entry
> x in mode. You can assume that x is some kind of
> constant in RTL. The argument mode is redundant except in the
> case of a `const_int` rtx. Select the section by calling
> `readonly_data_section` or one of the alternatives for other
> sections. align is the constant alignment in bits.
>
> The default version of this function takes care of putting symbolic
> constants in `flag_pic` mode in `data_section` and everything
> else in `readonly_data_section`.

— Target Hook: void __TARGET_ENCODE_SECTION_INFO__ (tree decl, rtx rtl, int new_decl_p)
> Define this hook if references to a symbol or a constant must be
> treated differently depending on something about the variable or
> function named by the symbol (such as what section it is in).
>
> The hook is executed immediately after rtl has been created for
> decl, which may be a variable or function declaration or
> an entry in the constant pool. In either case, rtl is the
> rtl in question. Do _not_ use `DECL_RTL (`decl`)`
> in this hook; that field may not have been initialized yet.
>
> In the case of a constant, it is safe to assume that the rtl is
> a `mem` whose address is a `symbol_ref`. Most decls
> will also have this form, but that is not guaranteed. Global
> register variables, for instance, will have a `reg` for their
> rtl. (Normally the right thing to do with such unusual rtl is
> leave it alone.)
>
> The new_decl_p argument will be true if this is the first time
> that `TARGET_ENCODE_SECTION_INFO` has been invoked on this decl. It will
> be false for subsequent invocations, which will happen for duplicate
> declarations. Whether or not anything must be done for the duplicate
> declaration depends on whether the hook examines `DECL_ATTRIBUTES`.
> new_decl_p is always true when the hook is called for a constant.
>
> The usual thing for this hook to do is to record flags in the
> `symbol_ref`, using `SYMBOL_REF_FLAG` or `SYMBOL_REF_FLAGS`.
> Historically, the name string was modified if it was necessary to
> encode more than one bit of information, but this practice is now
> discouraged; use `SYMBOL_REF_FLAGS`.
>
> The default definition of this hook, `default_encode_section_info`
> in `varasm.c`, sets a number of commonly-useful bits in
> `SYMBOL_REF_FLAGS`. Check whether the default does what you need
> before overriding it.

— Target Hook: const __char__ \*TARGET_STRIP_NAME_ENCODING (const char \*name)
> Decode name and return the real name part, sans
> the characters that `TARGET_ENCODE_SECTION_INFO`
> may have added.

— Target Hook: bool __TARGET_IN_SMALL_DATA_P__ (tree exp)
> Returns true if exp should be placed into a “small data” section.
> The default version of this hook always returns false.

— Variable: Target Hook __bool__ TARGET_HAVE_SRODATA_SECTION
> Contains the value true if the target places read-only
> “small data” into a separate section. The default value is false.

— Target Hook: bool __TARGET_BINDS_LOCAL_P__ (tree exp)
> Returns true if exp names an object for which name resolution
> rules must resolve to the current “module” (dynamic shared library
> or executable image).
>
> The default version of this hook implements the name resolution rules
> for ELF, which has a looser model of global name binding than other
> currently supported object file formats.

— Variable: Target Hook __bool__ TARGET_HAVE_TLS
> Contains the value true if the target supports thread-local storage.
> The default value is false.
