---
title: GNU Compiler Collection (GCC) Internals
apple_id: TP40006804
resource_type: Guide
platform: Xcode Developer Tools
topic: null
technology: null
published: '2012-07-23'
source_url: https://developer.apple.com/library/archive/documentation/DeveloperTools/gcc-4.0.1/gccint/Addressing-Modes.html
archived_at: '2026-07-15T07:30:59.218252Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [GNU Compiler Collection (GCC) Internals](index.md)



Next: [Condition Code](Condition-Code.md#apple-inxw4zdjoruw63rninxwizi),
Previous: [Library Calls](Library-Calls.md#apple-jruwe4tboj4s2q3bnrwhg),
Up: [Target Macros](Target-Macros.md#apple-krqxez3foqwu2yldojxxg)

---

### 13.13 Addressing Modes

This is about addressing modes.

— Macro: __HAVE_PRE_INCREMENT__
— Macro: __HAVE_PRE_DECREMENT__
— Macro: __HAVE_POST_INCREMENT__
— Macro: __HAVE_POST_DECREMENT__
> A C expression that is nonzero if the machine supports pre-increment,
> pre-decrement, post-increment, or post-decrement addressing respectively.

— Macro: __HAVE_PRE_MODIFY_DISP__
— Macro: __HAVE_POST_MODIFY_DISP__
> A C expression that is nonzero if the machine supports pre- or
> post-address side-effect generation involving constants other than
> the size of the memory operand.

— Macro: __HAVE_PRE_MODIFY_REG__
— Macro: __HAVE_POST_MODIFY_REG__
> A C expression that is nonzero if the machine supports pre- or
> post-address side-effect generation involving a register displacement.

— Macro: __CONSTANT_ADDRESS_P__ (x)
> A C expression that is 1 if the RTX x is a constant which
> is a valid address. On most machines, this can be defined as
> `CONSTANT_P (`x`)`, but a few machines are more restrictive
> in which constant addresses are supported.

— Macro: __CONSTANT_P__ (x)
> `CONSTANT_P`, which is defined by target-independent code,
> accepts integer-values expressions whose values are not explicitly
> known, such as `symbol_ref`, `label_ref`, and `high`
> expressions and `const` arithmetic expressions, in addition to
> `const_int` and `const_double` expressions.

— Macro: __MAX_REGS_PER_ADDRESS__
> A number, the maximum number of registers that can appear in a valid
> memory address. Note that it is up to you to specify a value equal to
> the maximum number that `GO_IF_LEGITIMATE_ADDRESS` would ever
> accept.

— Macro: __GO_IF_LEGITIMATE_ADDRESS__ (mode, x, label)
> A C compound statement with a conditional `goto` label`;`
> executed if x (an RTX) is a legitimate memory address on the
> target machine for a memory operand of mode mode.
>
> It usually pays to define several simpler macros to serve as
> subroutines for this one. Otherwise it may be too complicated to
> understand.
>
> This macro must exist in two variants: a strict variant and a
> non-strict one. The strict variant is used in the reload pass. It
> must be defined so that any pseudo-register that has not been
> allocated a hard register is considered a memory reference. In
> contexts where some kind of register is required, a pseudo-register
> with no hard register must be rejected.
>
> The non-strict variant is used in other passes. It must be defined to
> accept all pseudo-registers in every context where some kind of
> register is required.
>
> Compiler source files that want to use the strict variant of this
> macro define the macro `REG_OK_STRICT`. You should use an
> `#ifdef REG_OK_STRICT` conditional to define the strict variant
> in that case and the non-strict variant otherwise.
>
> Subroutines to check for acceptable registers for various purposes (one
> for base registers, one for index registers, and so on) are typically
> among the subroutines used to define `GO_IF_LEGITIMATE_ADDRESS`.
> Then only these subroutine macros need have two variants; the higher
> levels of macros may be the same whether strict or not.
>
> Normally, constant addresses which are the sum of a `symbol_ref`
> and an integer are stored inside a `const` RTX to mark them as
> constant. Therefore, there is no need to recognize such sums
> specifically as legitimate addresses. Normally you would simply
> recognize any `const` as legitimate.
>
> Usually `PRINT_OPERAND_ADDRESS` is not prepared to handle constant
> sums that are not marked with `const`. It assumes that a naked
> `plus` indicates indexing. If so, then you _must_ reject such
> naked constant sums as illegitimate addresses, so that none of them will
> be given to `PRINT_OPERAND_ADDRESS`.
>
> On some machines, whether a symbolic address is legitimate depends on
> the section that the address refers to. On these machines, define the
> target hook `TARGET_ENCODE_SECTION_INFO` to store the information
> into the `symbol_ref`, and then check for it here. When you see a
> `const`, you will have to look inside it to find the
> `symbol_ref` in order to determine the section. See [Assembler Format](Assembler-Format.md#apple-ifzxgzlnmjwgk4rnizxxe3lboq).

— Macro: __REG_OK_FOR_BASE_P__ (x)
> A C expression that is nonzero if x (assumed to be a `reg`
> RTX) is valid for use as a base register. For hard registers, it
> should always accept those which the hardware permits and reject the
> others. Whether the macro accepts or rejects pseudo registers must be
> controlled by `REG_OK_STRICT` as described above. This usually
> requires two variant definitions, of which `REG_OK_STRICT`
> controls the one actually used.

— Macro: __REG_MODE_OK_FOR_BASE_P__ (x, mode)
> A C expression that is just like `REG_OK_FOR_BASE_P`, except that
> that expression may examine the mode of the memory reference in
> mode. You should define this macro if the mode of the memory
> reference affects whether a register may be used as a base register. If
> you define this macro, the compiler will use it instead of
> `REG_OK_FOR_BASE_P`.

— Macro: __REG_MODE_OK_FOR_REG_BASE_P__ (x, mode)
> A C expression which is nonzero if x (assumed to be a `reg` RTX)
> is suitable for use as a base register in base plus index operand addresses,
> accessing memory in mode mode. It may be either a suitable hard
> register or a pseudo register that has been allocated such a hard register.
> You should define this macro if base plus index addresses have different
> requirements than other base register uses.

— Macro: __REG_OK_FOR_INDEX_P__ (x)
> A C expression that is nonzero if x (assumed to be a `reg`
> RTX) is valid for use as an index register.
>
> The difference between an index register and a base register is that
> the index register may be scaled. If an address involves the sum of
> two registers, neither one of them scaled, then either one may be
> labeled the “base” and the other the “index”; but whichever
> labeling is used must fit the machine's constraints of which registers
> may serve in each capacity. The compiler will try both labelings,
> looking for one that is valid, and will reload one or both registers
> only if neither labeling works.

— Macro: __FIND_BASE_TERM__ (x)
> A C expression to determine the base term of address x.
> This macro is used in only one place: `find_base_term' in alias.c.
>
> It is always safe for this macro to not be defined. It exists so
> that alias analysis can understand machine-dependent addresses.
>
> The typical use of this macro is to handle addresses containing
> a label_ref or symbol_ref within an UNSPEC.

— Macro: __LEGITIMIZE_ADDRESS__ (x, oldx, mode, win)
> A C compound statement that attempts to replace x with a valid
> memory address for an operand of mode mode. win will be a
> C statement label elsewhere in the code; the macro definition may use
>
> ```
>           GO_IF_LEGITIMATE_ADDRESS (mode, x, win);
>
> ```
>
> to avoid further processing if the address has become legitimate.
>
> x will always be the result of a call to `break_out_memory_refs`,
> and oldx will be the operand that was given to that function to produce
> x.
>
> The code generated by this macro should not alter the substructure of
> x. If it transforms x into a more legitimate form, it
> should assign x (which will always be a C variable) a new value.
>
> It is not necessary for this macro to come up with a legitimate
> address. The compiler has standard ways of doing so in all cases. In
> fact, it is safe to omit this macro. But often a
> machine-dependent strategy can generate better code.

— Macro: __LEGITIMIZE_RELOAD_ADDRESS__ (x, mode, opnum, type, ind_levels, win)
> A C compound statement that attempts to replace x, which is an address
> that needs reloading, with a valid memory address for an operand of mode
> mode. win will be a C statement label elsewhere in the code.
> It is not necessary to define this macro, but it might be useful for
> performance reasons.
>
> For example, on the i386, it is sometimes possible to use a single
> reload register instead of two by reloading a sum of two pseudo
> registers into a register. On the other hand, for number of RISC
> processors offsets are limited so that often an intermediate address
> needs to be generated in order to address a stack slot. By defining
> `LEGITIMIZE_RELOAD_ADDRESS` appropriately, the intermediate addresses
> generated for adjacent some stack slots can be made identical, and thus
> be shared.
>
> _Note_: This macro should be used with caution. It is necessary
> to know something of how reload works in order to effectively use this,
> and it is quite easy to produce macros that build in too much knowledge
> of reload internals.
>
> _Note_: This macro must be able to reload an address created by a
> previous invocation of this macro. If it fails to handle such addresses
> then the compiler may generate incorrect code or abort.
>
> The macro definition should use `push_reload` to indicate parts that
> need reloading; opnum, type and ind_levels are usually
> suitable to be passed unaltered to `push_reload`.
>
> The code generated by this macro must not alter the substructure of
> x. If it transforms x into a more legitimate form, it
> should assign x (which will always be a C variable) a new value.
> This also applies to parts that you change indirectly by calling
> `push_reload`.
>
> The macro definition may use `strict_memory_address_p` to test if
> the address has become legitimate.
>
> If you want to change only a part of x, one standard way of doing
> this is to use `copy_rtx`. Note, however, that is unshares only a
> single level of rtl. Thus, if the part to be changed is not at the
> top level, you'll need to replace first the top level.
> It is not necessary for this macro to come up with a legitimate
> address; but often a machine-dependent strategy can generate better code.

— Macro: __GO_IF_MODE_DEPENDENT_ADDRESS__ (addr, label)
> A C statement or compound statement with a conditional `goto`label`;` executed if memory address x (an RTX) can have
> different meanings depending on the machine mode of the memory
> reference it is used for or if the address is valid for some modes
> but not others.
>
> Autoincrement and autodecrement addresses typically have mode-dependent
> effects because the amount of the increment or decrement is the size
> of the operand being addressed. Some machines have other mode-dependent
> addresses. Many RISC machines have no mode-dependent addresses.
>
> You may assume that addr is a valid address for the machine.

— Macro: __LEGITIMATE_CONSTANT_P__ (x)
> A C expression that is nonzero if x is a legitimate constant for
> an immediate operand on the target machine. You can assume that
> x satisfies `CONSTANT_P`, so you need not check this. In fact,
> ``1`' is a suitable definition for this macro on machines where
> anything `CONSTANT_P` is valid.

— Target Hook: rtx __TARGET_DELEGITIMIZE_ADDRESS__ (rtx x)
> This hook is used to undo the possibly obfuscating effects of the
> `LEGITIMIZE_ADDRESS` and `LEGITIMIZE_RELOAD_ADDRESS` target
> macros. Some backend implementations of these macros wrap symbol
> references inside an `UNSPEC` rtx to represent PIC or similar
> addressing modes. This target hook allows GCC's optimizers to understand
> the semantics of these opaque `UNSPEC`s by converting them back
> into their original form.

— Target Hook: bool __TARGET_CANNOT_FORCE_CONST_MEM__ (rtx x)
> This hook should return true if x is of a form that cannot (or
> should not) be spilled to the constant pool. The default version of
> this hook returns false.
>
> The primary reason to define this hook is to prevent reload from
> deciding that a non-legitimate constant would be better reloaded
> from the constant pool instead of spilling and reloading a register
> holding the constant. This restriction is often true of addresses
> of TLS symbols for various targets.

— Target Hook: tree __TARGET_VECTORIZE_BUILTIN_MASK_FOR_LOAD__ (void)
> This hook should return the DECL of a function f that given an
> address addr as an argument returns a mask m that can be
> used to extract from two vectors the relevant data that resides in
> addr in case addr is not properly aligned.
>
> The autovectrizer, when vectorizing a load operation from an address
> addr that may be unaligned, will generate two vector loads from
> the two aligned addresses around addr. It then generates a
> `REALIGN_LOAD` operation to extract the relevant data from the
> two loaded vectors. The first two arguments to `REALIGN_LOAD`,
> v1 and v2, are the two vectors, each of size VS, and
> the third argument, OFF, defines how the data will be extracted
> from these two vectors: if OFF is 0, then the returned vector is
> v2; otherwise, the returned vector is composed from the last
> VS-OFF elements of v1 concatenated to the first
> OFF elements of v2.
>
> If this hook is defined, the autovectorizer will generate a call
> to f (using the DECL tree that this hook returns) and will
> use the return value of f as the argument OFF to
> `REALIGN_LOAD`. Therefore, the mask m returned by f
> should comply with the semantics expected by `REALIGN_LOAD`
> described above.
> If this hook is not defined, then addr will be used as
> the argument OFF to `REALIGN_LOAD`, in which case the low
> log2(VS)-1 bits of addr will be considered.
