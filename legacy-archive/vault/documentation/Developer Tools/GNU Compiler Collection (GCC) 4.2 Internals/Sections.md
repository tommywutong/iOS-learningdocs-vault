---
title: GNU Compiler Collection (GCC) 4.2 Internals
apple_id: TP40007093
resource_type: Guide
platform: Xcode Developer Tools
topic: null
technology: null
published: '2012-07-23'
source_url: https://developer.apple.com/library/archive/documentation/DeveloperTools/gcc-4.2.1/gccint/Sections.html
archived_at: '2026-07-15T07:31:02.768781Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [GNU Compiler Collection (GCC) 4.2 Internals](index.md)



Next: [PIC](PIC.md#apple-kbeug),
Previous: [Scheduling](Scheduling.md#apple-knrwqzleovwgs3th),
Up: [Target Macros](Target-Macros.md#apple-krqxez3foqwu2yldojxxg)

---

### 15.19 Dividing the Output into Sections (Texts, Data, ...)

An object file is divided into sections containing different types of
data. In the most common case, there are three sections: the text
section, which holds instructions and read-only data; the data
section, which holds initialized writable data; and the bss
section, which holds uninitialized data. Some systems have other kinds
of sections.

`varasm.c` provides several well-known sections, such as
`text_section`, `data_section` and `bss_section`.
The normal way of controlling a foo`_section` variable
is to define the associated FOO`_SECTION_ASM_OP` macro,
as described below. The macros are only read once, when `varasm.c`
initializes itself, so their values must be run-time constants.
They may however depend on command-line flags.

_Note:_ Some run-time files, such `crtstuff.c`, also make
use of the FOO`_SECTION_ASM_OP` macros, and expect them
to be string literals.

Some assemblers require a different string to be written every time a
section is selected. If your assembler falls into this category, you
should define the `TARGET_ASM_INIT_SECTIONS` hook and use
`get_unnamed_section` to set up the sections.

You must always create a `text_section`, either by defining
`TEXT_SECTION_ASM_OP` or by initializing `text_section`
in `TARGET_ASM_INIT_SECTIONS`. The same is true of
`data_section` and `DATA_SECTION_ASM_OP`. If you do not
create a distinct `readonly_data_section`, the default is to
reuse `text_section`.

All the other `varasm.c` sections are optional, and are null
if the target does not provide them.

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

— Macro: __SDATA_SECTION_ASM_OP__
> If defined, a C expression whose value is a string, including spacing,
> containing the assembler operation to identify the following data as
> initialized, writable small data.

— Macro: __READONLY_DATA_SECTION_ASM_OP__
> A C expression whose value is a string, including spacing, containing the
> assembler operation to identify the following data as read-only initialized
> data.

— Macro: __BSS_SECTION_ASM_OP__
> If defined, a C expression whose value is a string, including spacing,
> containing the assembler operation to identify the following data as
> uninitialized global data. If not defined, and neither
> `ASM_OUTPUT_BSS` nor `ASM_OUTPUT_ALIGNED_BSS` are defined,
> uninitialized global data will be output in the data section if
> `-fno-common` is passed, otherwise `ASM_OUTPUT_COMMON` will be
> used.

— Macro: __SBSS_SECTION_ASM_OP__
> If defined, a C expression whose value is a string, including spacing,
> containing the assembler operation to identify the following data as
> uninitialized, writable small data.

— Macro: __INIT_SECTION_ASM_OP__
> If defined, a C expression whose value is a string, including spacing,
> containing the assembler operation to identify the following data as
> initialization code. If not defined, GCC will assume such a section does
> not exist. This section has no corresponding `init_section`
> variable; it is used entirely in runtime code.

— Macro: __FINI_SECTION_ASM_OP__
> If defined, a C expression whose value is a string, including spacing,
> containing the assembler operation to identify the following data as
> finalization code. If not defined, GCC will assume such a section does
> not exist. This section has no corresponding `fini_section`
> variable; it is used entirely in runtime code.

— Macro: __INIT_ARRAY_SECTION_ASM_OP__
> If defined, a C expression whose value is a string, including spacing,
> containing the assembler operation to identify the following data as
> part of the `.init_array` (or equivalent) section. If not
> defined, GCC will assume such a section does not exist. Do not define
> both this macro and `INIT_SECTION_ASM_OP`.

— Macro: __FINI_ARRAY_SECTION_ASM_OP__
> If defined, a C expression whose value is a string, including spacing,
> containing the assembler operation to identify the following data as
> part of the `.fini_array` (or equivalent) section. If not
> defined, GCC will assume such a section does not exist. Do not define
> both this macro and `FINI_SECTION_ASM_OP`.

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

— Macro: __TARGET_LIBGCC_SDATA_SECTION__
> If defined, a string which names the section into which small
> variables defined in crtstuff and libgcc should go. This is useful
> when the target has options for optimizing access to small data, and
> you want the crtstuff and libgcc routines to be conservative in what
> they expect of your application yet liberal in what your application
> expects. For example, for targets with a `.sdata` section (like
> MIPS), you could compile crtstuff with `-G 0` so that it doesn't
> require small data support from your application, but use this macro
> to put small data into `.sdata` so that your application can
> access these variables whether it uses small data or not.

— Macro: __FORCE_CODE_SECTION_ALIGN__
> If defined, an ASM statement that aligns a code section to some
> arbitrary boundary. This is used to force all fragments of the
> `.init` and `.fini` sections to have to same alignment
> and thus prevent the linker from having to add any padding.

— Macro: __JUMP_TABLES_IN_TEXT_SECTION__
> Define this macro to be an expression with a nonzero value if jump
> tables (for `tablejump` insns) should be output in the text
> section, along with the assembler instructions. Otherwise, the
> readonly data section is used.
>
> This macro is irrelevant if there is no separate readonly data section.

— Target Hook: void __TARGET_ASM_INIT_SECTIONS__ (void)
> Define this hook if you need to do something special to set up the
> `varasm.c` sections, or if your target has some special sections
> of its own that you need to create.
>
> GCC calls this hook after processing the command line, but before writing
> any assembly code, and before calling any of the section-returning hooks
> described below.

— Target Hook: TARGET_ASM_RELOC_RW_MASK __(__void)
> Return a mask describing how relocations should be treated when
> selecting sections. Bit 1 should be set if global relocations
> should be placed in a read-write section; bit 0 should be set if
> local relocations should be placed in a read-write section.
>
> The default version of this function returns 3 when `-fpic`
> is in effect, and 0 otherwise. The hook is typically redefined
> when the target cannot support (some kinds of) dynamic relocations
> in read-only sections even in executables.

— Target Hook: section \* __TARGET_ASM_SELECT_SECTION__ (tree exp, int reloc, unsigned HOST_WIDE_INT align)
> Return the section into which exp should be placed. You can
> assume that exp is either a `VAR_DECL` node or a constant of
> some sort. reloc indicates whether the initial value of exp
> requires link-time relocations. Bit 0 is set when variable contains
> local relocations only, while bit 1 is set for global relocations.
> align is the constant alignment in bits.
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

— Target Hook: section \* __TARGET_ASM_FUNCTION_RODATA_SECTION__ (tree decl)
> Return the readonly data section associated with
> ``DECL_SECTION_NAME (decl)`'.
> The default version of this function selects `.gnu.linkonce.r.name` if
> the function's section is `.gnu.linkonce.t.name`, `.rodata.name`
> if function is in `.text.name`, and the normal readonly-data section
> otherwise.

— Target Hook: section \* __TARGET_ASM_SELECT_RTX_SECTION__ (enum machine_mode mode, rtx x, unsigned HOST_WIDE_INT align)
> Return the section into which a constant x, of mode mode,
> should be placed. You can assume that x is some kind of
> constant in RTL. The argument mode is redundant except in the
> case of a `const_int` rtx. align is the constant alignment
> in bits.
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
