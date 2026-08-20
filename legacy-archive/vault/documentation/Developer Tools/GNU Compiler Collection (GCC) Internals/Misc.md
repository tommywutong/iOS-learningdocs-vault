---
title: GNU Compiler Collection (GCC) Internals
apple_id: TP40006804
resource_type: Guide
platform: Xcode Developer Tools
topic: null
technology: null
published: '2012-07-23'
source_url: https://developer.apple.com/library/archive/documentation/DeveloperTools/gcc-4.0.1/gccint/Misc.html
archived_at: '2026-07-15T07:31:00.366875Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [GNU Compiler Collection (GCC) Internals](index.md)



Previous: [C++ ABI](C_002b_002b-ABI.md#apple-inptambsmjptambsmiwucqsj),
Up: [Target Macros](Target-Macros.md#apple-krqxez3foqwu2yldojxxg)

---

### 13.27 Miscellaneous Parameters

Here are several miscellaneous parameters.

— Macro: __PREDICATE_CODES__
> Define this if you have defined special-purpose predicates in the file
> `machine.c`. This macro is called within an initializer of an
> array of structures. The first field in the structure is the name of a
> predicate and the second field is an array of rtl codes. For each
> predicate, list all rtl codes that can be in expressions matched by the
> predicate. The list should have a trailing comma. Here is an example
> of two entries in the list for a typical RISC machine:
>
> ```
>           #define PREDICATE_CODES \
>             {"gen_reg_rtx_operand", {SUBREG, REG}},  \
>             {"reg_or_short_cint_operand", {SUBREG, REG, CONST_INT}},
>
> ```
>
> Defining this macro does not affect the generated code (however,
> incorrect definitions that omit an rtl code that may be matched by the
> predicate can cause the compiler to malfunction). Instead, it allows
> the table built by `genrecog` to be more compact and efficient,
> thus speeding up the compiler. The most important predicates to include
> in the list specified by this macro are those used in the most insn
> patterns.
>
> For each predicate function named in `PREDICATE_CODES`, a
> declaration will be generated in `insn-codes.h`.
>
> Use of this macro is deprecated; use `define_predicate` instead.
> See [Defining Predicates](Defining-Predicates.md#apple-irswm2lonfxgolkqojswi2ldmf2gk4y).

— Macro: __SPECIAL_MODE_PREDICATES__
> Define this if you have special predicates that know special things
> about modes. Genrecog will warn about certain forms of
> `match_operand` without a mode; if the operand predicate is
> listed in `SPECIAL_MODE_PREDICATES`, the warning will be
> suppressed.
>
> Here is an example from the IA-32 port (`ext_register_operand`
> specially checks for `HImode` or `SImode` in preparation
> for a byte extraction from `%ah` etc.).
>
> ```
>           #define SPECIAL_MODE_PREDICATES \
>             "ext_register_operand",
>
> ```
>
> Use of this macro is deprecated; use `define_special_predicate`
> instead. See [Defining Predicates](Defining-Predicates.md#apple-irswm2lonfxgolkqojswi2ldmf2gk4y).

— Macro: __HAS_LONG_COND_BRANCH__
> Define this boolean macro to indicate whether or not your architecture
> has conditional branches that can span all of memory. It is used in
> conjunction with an optimization that partitions hot and cold basic
> blocks into separate sections of the executable. If this macro is
> set to false, gcc will convert any conditional branches that attempt
> to cross between sections into unconditional branches or indirect jumps.

— Macro: __HAS_LONG_UNCOND_BRANCH__
> Define this boolean macro to indicate whether or not your architecture
> has unconditional branches that can span all of memory. It is used in
> conjunction with an optimization that partitions hot and cold basic
> blocks into separate sections of the executable. If this macro is
> set to false, gcc will convert any unconditional branches that attempt
> to cross between sections into indirect jumps.

— Macro: __CASE_VECTOR_MODE__
> An alias for a machine mode name. This is the machine mode that
> elements of a jump-table should have.

— Macro: __CASE_VECTOR_SHORTEN_MODE__ (min_offset, max_offset, body)
> Optional: return the preferred mode for an `addr_diff_vec`
> when the minimum and maximum offset are known. If you define this,
> it enables extra code in branch shortening to deal with `addr_diff_vec`.
> To make this work, you also have to define `INSN_ALIGN` and
> make the alignment for `addr_diff_vec` explicit.
> The body argument is provided so that the offset_unsigned and scale
> flags can be updated.

— Macro: __CASE_VECTOR_PC_RELATIVE__
> Define this macro to be a C expression to indicate when jump-tables
> should contain relative addresses. You need not define this macro if
> jump-tables never contain relative addresses, or jump-tables should
> contain relative addresses only when `-fPIC` or `-fPIC`
> is in effect.

— Macro: __CASE_VALUES_THRESHOLD__
> Define this to be the smallest number of different values for which it
> is best to use a jump-table instead of a tree of conditional branches.
> The default is four for machines with a `casesi` instruction and
> five otherwise. This is best for most machines.

— Macro: __CASE_USE_BIT_TESTS__
> Define this macro to be a C expression to indicate whether C switch
> statements may be implemented by a sequence of bit tests. This is
> advantageous on processors that can efficiently implement left shift
> of 1 by the number of bits held in a register, but inappropriate on
> targets that would require a loop. By default, this macro returns
> `true` if the target defines an `ashlsi3` pattern, and
> `false` otherwise.

— Macro: __WORD_REGISTER_OPERATIONS__
> Define this macro if operations between registers with integral mode
> smaller than a word are always performed on the entire register.
> Most RISC machines have this property and most CISC machines do not.

— Macro: __LOAD_EXTEND_OP__ (mem_mode)
> Define this macro to be a C expression indicating when insns that read
> memory in mem_mode, an integral mode narrower than a word, set the
> bits outside of mem_mode to be either the sign-extension or the
> zero-extension of the data read. Return `SIGN_EXTEND` for values
> of mem_mode for which the
> insn sign-extends, `ZERO_EXTEND` for which it zero-extends, and
> `UNKNOWN` for other modes.
>
> This macro is not called with mem_mode non-integral or with a width
> greater than or equal to `BITS_PER_WORD`, so you may return any
> value in this case. Do not define this macro if it would always return
> `UNKNOWN`. On machines where this macro is defined, you will normally
> define it as the constant `SIGN_EXTEND` or `ZERO_EXTEND`.
>
> You may return a non-`UNKNOWN` value even if for some hard registers
> the sign extension is not performed, if for the `REGNO_REG_CLASS`
> of these hard registers `CANNOT_CHANGE_MODE_CLASS` returns nonzero
> when the from mode is mem_mode and the to mode is any
> integral mode larger than this but not larger than `word_mode`.
>
> You must return `UNKNOWN` if for some hard registers that allow this
> mode, `CANNOT_CHANGE_MODE_CLASS` says that they cannot change to
> `word_mode`, but that they can change to another integral mode that
> is larger then mem_mode but still smaller than `word_mode`.

— Macro: __SHORT_IMMEDIATES_SIGN_EXTEND__
> Define this macro if loading short immediate values into registers sign
> extends.

— Macro: __FIXUNS_TRUNC_LIKE_FIX_TRUNC__
> Define this macro if the same instructions that convert a floating
> point number to a signed fixed point number also convert validly to an
> unsigned one.

— Macro: __MOVE_MAX__
> The maximum number of bytes that a single instruction can move quickly
> between memory and registers or between two memory locations.

— Macro: __MAX_MOVE_MAX__
> The maximum number of bytes that a single instruction can move quickly
> between memory and registers or between two memory locations. If this
> is undefined, the default is `MOVE_MAX`. Otherwise, it is the
> constant value that is the largest value that `MOVE_MAX` can have
> at run-time.

— Macro: __SHIFT_COUNT_TRUNCATED__
> A C expression that is nonzero if on this machine the number of bits
> actually used for the count of a shift operation is equal to the number
> of bits needed to represent the size of the object being shifted. When
> this macro is nonzero, the compiler will assume that it is safe to omit
> a sign-extend, zero-extend, and certain bitwise `and' instructions that
> truncates the count of a shift operation. On machines that have
> instructions that act on bit-fields at variable positions, which may
> include `bit test' instructions, a nonzero `SHIFT_COUNT_TRUNCATED`
> also enables deletion of truncations of the values that serve as
> arguments to bit-field instructions.
>
> If both types of instructions truncate the count (for shifts) and
> position (for bit-field operations), or if no variable-position bit-field
> instructions exist, you should define this macro.
>
> However, on some machines, such as the 80386 and the 680x0, truncation
> only applies to shift operations and not the (real or pretended)
> bit-field operations. Define `SHIFT_COUNT_TRUNCATED` to be zero on
> such machines. Instead, add patterns to the `md` file that include
> the implied truncation of the shift instructions.
>
> You need not define this macro if it would always have the value of zero.

— Target Hook: int __TARGET_SHIFT_TRUNCATION_MASK__ (enum machine_mode mode)
> This function describes how the standard shift patterns for mode
> deal with shifts by negative amounts or by more than the width of the mode.
> See [shift patterns](https://developer.apple.com/library/archive/documentation/DeveloperTools/gcc-4.0.1/gccint/shift-patterns.html#shift-patterns).
>
> On many machines, the shift patterns will apply a mask m to the
> shift count, meaning that a fixed-width shift of x by y is
> equivalent to an arbitrary-width shift of x by y & m. If
> this is true for mode mode, the function should return m,
> otherwise it should return 0. A return value of 0 indicates that no
> particular behavior is guaranteed.
>
> Note that, unlike `SHIFT_COUNT_TRUNCATED`, this function does
> _not_ apply to general shift rtxes; it applies only to instructions
> that are generated by the named shift patterns.
>
> The default implementation of this function returns
> `GET_MODE_BITSIZE (`mode`) - 1` if `SHIFT_COUNT_TRUNCATED`
> and 0 otherwise. This definition is always safe, but if
> `SHIFT_COUNT_TRUNCATED` is false, and some shift patterns
> nevertheless truncate the shift count, you may get better code
> by overriding it.

— Macro: __TRULY_NOOP_TRUNCATION__ (outprec, inprec)
> A C expression which is nonzero if on this machine it is safe to
> “convert” an integer of inprec bits to one of outprec
> bits (where outprec is smaller than inprec) by merely
> operating on it as if it had only outprec bits.
>
> On many machines, this expression can be 1.
>
> When `TRULY_NOOP_TRUNCATION` returns 1 for a pair of sizes for
> modes for which `MODES_TIEABLE_P` is 0, suboptimal code can result.
> If this is the case, making `TRULY_NOOP_TRUNCATION` return 0 in
> such cases may improve things.

— Macro: __STORE_FLAG_VALUE__
> A C expression describing the value returned by a comparison operator
> with an integral mode and stored by a store-flag instruction
> (``scond`') when the condition is true. This description must
> apply to _all_ the ``scond`' patterns and all the
> comparison operators whose results have a `MODE_INT` mode.
>
> A value of 1 or −1 means that the instruction implementing the
> comparison operator returns exactly 1 or −1 when the comparison is true
> and 0 when the comparison is false. Otherwise, the value indicates
> which bits of the result are guaranteed to be 1 when the comparison is
> true. This value is interpreted in the mode of the comparison
> operation, which is given by the mode of the first operand in the
> ``scond`' pattern. Either the low bit or the sign bit of
> `STORE_FLAG_VALUE` be on. Presently, only those bits are used by
> the compiler.
>
> If `STORE_FLAG_VALUE` is neither 1 or −1, the compiler will
> generate code that depends only on the specified bits. It can also
> replace comparison operators with equivalent operations if they cause
> the required bits to be set, even if the remaining bits are undefined.
> For example, on a machine whose comparison operators return an
> `SImode` value and where `STORE_FLAG_VALUE` is defined as
> ``0x80000000`', saying that just the sign bit is relevant, the
> expression
>
> ```
>           (ne:SI (and:SI x (const_int power-of-2)) (const_int 0))
>
> ```
>
> can be converted to
>
> ```
>           (ashift:SI x (const_int n))
>
> ```
>
> where n is the appropriate shift count to move the bit being
> tested into the sign bit.
>
> There is no way to describe a machine that always sets the low-order bit
> for a true value, but does not guarantee the value of any other bits,
> but we do not know of any machine that has such an instruction. If you
> are trying to port GCC to such a machine, include an instruction to
> perform a logical-and of the result with 1 in the pattern for the
> comparison operators and let us know at [gcc@gcc.gnu.org](mailto:gcc@gcc.gnu.org).
>
> Often, a machine will have multiple instructions that obtain a value
> from a comparison (or the condition codes). Here are rules to guide the
> choice of value for `STORE_FLAG_VALUE`, and hence the instructions
> to be used:
>
> - Use the shortest sequence that yields a valid definition for
>   `STORE_FLAG_VALUE`. It is more efficient for the compiler to
>   “normalize” the value (convert it to, e.g., 1 or 0) than for the
>   comparison operators to do so because there may be opportunities to
>   combine the normalization with other operations.
> - For equal-length sequences, use a value of 1 or −1, with −1 being
>   slightly preferred on machines with expensive jumps and 1 preferred on
>   other machines.
> - As a second choice, choose a value of ``0x80000001`' if instructions
>   exist that set both the sign and low-order bits but do not define the
>   others.
> - Otherwise, use a value of ``0x80000000`'.
>
> Many machines can produce both the value chosen for
> `STORE_FLAG_VALUE` and its negation in the same number of
> instructions. On those machines, you should also define a pattern for
> those cases, e.g., one matching
>
> ```
>           (set A (neg:m (ne:m B C)))
>
> ```
>
> Some machines can also perform `and` or `plus` operations on
> condition code values with less instructions than the corresponding
> ``scond`' insn followed by `and` or `plus`. On those
> machines, define the appropriate patterns. Use the names `incscc`
> and `decscc`, respectively, for the patterns which perform
> `plus` or `minus` operations on condition code values. See
> `rs6000.md` for some examples. The GNU Superoptizer can be used to
> find such instruction sequences on other machines.
>
> If this macro is not defined, the default value, 1, is used. You need
> not define `STORE_FLAG_VALUE` if the machine has no store-flag
> instructions, or if the value generated by these instructions is 1.

— Macro: __FLOAT_STORE_FLAG_VALUE__ (mode)
> A C expression that gives a nonzero `REAL_VALUE_TYPE` value that is
> returned when comparison operators with floating-point results are true.
> Define this macro on machines that have comparison operations that return
> floating-point values. If there are no such operations, do not define
> this macro.

— Macro: __VECTOR_STORE_FLAG_VALUE__ (mode)
> A C expression that gives a rtx representing the non-zero true element
> for vector comparisons. The returned rtx should be valid for the inner
> mode of mode which is guaranteed to be a vector mode. Define
> this macro on machines that have vector comparison operations that
> return a vector result. If there are no such operations, do not define
> this macro. Typically, this macro is defined as `const1_rtx` or
> `constm1_rtx`. This macro may return `NULL_RTX` to prevent
> the compiler optimizing such vector comparison operations for the
> given mode.

— Macro: __CLZ_DEFINED_VALUE_AT_ZERO__ (mode, value)
— Macro: __CTZ_DEFINED_VALUE_AT_ZERO__ (mode, value)
> A C expression that evaluates to true if the architecture defines a value
> for `clz` or `ctz` with a zero operand. If so, value
> should be set to this value. If this macro is not defined, the value of
> `clz` or `ctz` is assumed to be undefined.
>
> This macro must be defined if the target's expansion for `ffs`
> relies on a particular value to get correct results. Otherwise it
> is not necessary, though it may be used to optimize some corner cases.
>
> Note that regardless of this macro the “definedness” of `clz`
> and `ctz` at zero do _not_ extend to the builtin functions
> visible to the user. Thus one may be free to adjust the value at will
> to match the target expansion of these operations without fear of
> breaking the API.

— Macro: __Pmode__
> An alias for the machine mode for pointers. On most machines, define
> this to be the integer mode corresponding to the width of a hardware
> pointer; `SImode` on 32-bit machine or `DImode` on 64-bit machines.
> On some machines you must define this to be one of the partial integer
> modes, such as `PSImode`.
>
> The width of `Pmode` must be at least as large as the value of
> `POINTER_SIZE`. If it is not equal, you must define the macro
> `POINTERS_EXTEND_UNSIGNED` to specify how pointers are extended
> to `Pmode`.

— Macro: __FUNCTION_MODE__
> An alias for the machine mode used for memory references to functions
> being called, in `call` RTL expressions. On most machines this
> should be `QImode`.

— Macro: __STDC_0_IN_SYSTEM_HEADERS__
> In normal operation, the preprocessor expands `__STDC__` to the
> constant 1, to signify that GCC conforms to ISO Standard C. On some
> hosts, like Solaris, the system compiler uses a different convention,
> where `__STDC__` is normally 0, but is 1 if the user specifies
> strict conformance to the C Standard.
>
> Defining `STDC_0_IN_SYSTEM_HEADERS` makes GNU CPP follows the host
> convention when processing system header files, but when processing user
> files `__STDC__` will always expand to 1.

— Macro: __NO_IMPLICIT_EXTERN_C__
> Define this macro if the system header files support C++ as well as C.
> This macro inhibits the usual method of using system header files in
> C++, which is to pretend that the file's contents are enclosed in
> ``extern "C" {...}`'.

— Macro: __REGISTER_TARGET_PRAGMAS__ ()
> Define this macro if you want to implement any target-specific pragmas.
> If defined, it is a C expression which makes a series of calls to
> `c_register_pragma` or `c_register_pragma_with_expansion`
> for each pragma. The macro may also do any
> setup required for the pragmas.
>
> The primary reason to define this macro is to provide compatibility with
> other compilers for the same target. In general, we discourage
> definition of target-specific pragmas for GCC.
>
> If the pragma can be implemented by attributes then you should consider
> defining the target hook ``TARGET_INSERT_ATTRIBUTES`' as well.
>
> Preprocessor macros that appear on pragma lines are not expanded. All
> ``#pragma`' directives that do not match any registered pragma are
> silently ignored, unless the user specifies `-Wunknown-pragmas`.

— Function: void __c_register_pragma__ (const char \*space, const char \*name, void (\*callback) (struct cpp_reader \*))
— Function: void __c_register_pragma_with_expansion__ (const char \*space, const char \*name, void (\*callback) (struct cpp_reader \*))
> Each call to `c_register_pragma` or
> `c_register_pragma_with_expansion` establishes one pragma. The
> callback routine will be called when the preprocessor encounters a
> pragma of the form
>
> ```
>           #pragma [space] name ...
>
> ```
>
> space is the case-sensitive namespace of the pragma, or
> `NULL` to put the pragma in the global namespace. The callback
> routine receives pfile as its first argument, which can be passed
> on to cpplib's functions if necessary. You can lex tokens after the
> name by calling `c_lex`. Tokens that are not read by the
> callback will be silently ignored. The end of the line is indicated by
> a token of type `CPP_EOF`. Macro expansion occurs on the
> arguments of pragmas registered with
> `c_register_pragma_with_expansion` but not on the arguments of
> pragmas registered with `c_register_pragma`.
>
> For an example use of this routine, see `c4x.h` and the callback
> routines defined in `c4x-c.c`.
>
> Note that the use of `c_lex` is specific to the C and C++
> compilers. It will not work in the Java or Fortran compilers, or any
> other language compilers for that matter. Thus if `c_lex` is going
> to be called from target-specific code, it must only be done so when
> building the C and C++ compilers. This can be done by defining the
> variables `c_target_objs` and `cxx_target_objs` in the
> target entry in the `config.gcc` file. These variables should name
> the target-specific, language-specific object file which contains the
> code that uses `c_lex`. Note it will also be necessary to add a
> rule to the makefile fragment pointed to by `tmake_file` that shows
> how to build this object file.

— Macro: __HANDLE_SYSV_PRAGMA__
> Define this macro (to a value of 1) if you want the System V style
> pragmas ``#pragma pack(<n>)`' and ``#pragma weak <name>
> [=<value>]`' to be supported by gcc.
>
> The pack pragma specifies the maximum alignment (in bytes) of fields
> within a structure, in much the same way as the ``__aligned__`' and
> ``__packed__`' `__attribute__`s do. A pack value of zero resets
> the behavior to the default.
>
> A subtlety for Microsoft Visual C/C++ style bit-field packing
> (e.g. -mms-bitfields) for targets that support it:
> When a bit-field is inserted into a packed record, the whole size
> of the underlying type is used by one or more same-size adjacent
> bit-fields (that is, if its long:3, 32 bits is used in the record,
> and any additional adjacent long bit-fields are packed into the same
> chunk of 32 bits. However, if the size changes, a new field of that
> size is allocated).
>
> If both MS bit-fields and ``__attribute__((packed))`' are used,
> the latter will take precedence. If ``__attribute__((packed))`' is
> used on a single field when MS bit-fields are in use, it will take
> precedence for that field, but the alignment of the rest of the structure
> may affect its placement.
>
> The weak pragma only works if `SUPPORTS_WEAK` and
> `ASM_WEAKEN_LABEL` are defined. If enabled it allows the creation
> of specifically named weak labels, optionally with a value.

— Macro: __HANDLE_PRAGMA_PACK_PUSH_POP__
> Define this macro (to a value of 1) if you want to support the Win32
> style pragmas ``#pragma pack(push[,n])`' and ``#pragma
> pack(pop)`'. The ``pack(push,[n])`' pragma specifies the maximum
> alignment (in bytes) of fields within a structure, in much the same way as
> the ``__aligned__`' and ``__packed__`' `__attribute__`s do. A
> pack value of zero resets the behavior to the default. Successive
> invocations of this pragma cause the previous values to be stacked, so
> that invocations of ``#pragma pack(pop)`' will return to the previous
> value.

— Macro: __HANDLE_PRAGMA_PACK_WITH_EXPANSION__
> Define this macro, as well as
> `HANDLE_SYSV_PRAGMA`, if macros should be expanded in the
> arguments of ``#pragma pack`'.

— Macro: __TARGET_DEFAULT_PACK_STRUCT__
> If your target requires a structure packing default other than 0 (meaning
> the machine default), define this macro to the necessary value (in bytes).
> This must be a value that would also valid to be used with
> ``#pragma pack()`' (that is, a small power of two).

— Macro: __DOLLARS_IN_IDENTIFIERS__
> Define this macro to control use of the character ``$`' in
> identifier names for the C family of languages. 0 means ``$`' is
> not allowed by default; 1 means it is allowed. 1 is the default;
> there is no need to define this macro in that case.

— Macro: __NO_DOLLAR_IN_LABEL__
> Define this macro if the assembler does not accept the character
> ``$`' in label names. By default constructors and destructors in
> G++ have ``$`' in the identifiers. If this macro is defined,
> ``.`' is used instead.

— Macro: __NO_DOT_IN_LABEL__
> Define this macro if the assembler does not accept the character
> ``.`' in label names. By default constructors and destructors in G++
> have names that use ``.`'. If this macro is defined, these names
> are rewritten to avoid ``.`'.

— Macro: __INSN_SETS_ARE_DELAYED__ (insn)
> Define this macro as a C expression that is nonzero if it is safe for the
> delay slot scheduler to place instructions in the delay slot of insn,
> even if they appear to use a resource set or clobbered in insn.
> insn is always a `jump_insn` or an `insn`; GCC knows that
> every `call_insn` has this behavior. On machines where some `insn`
> or `jump_insn` is really a function call and hence has this behavior,
> you should define this macro.
>
> You need not define this macro if it would always return zero.

— Macro: __INSN_REFERENCES_ARE_DELAYED__ (insn)
> Define this macro as a C expression that is nonzero if it is safe for the
> delay slot scheduler to place instructions in the delay slot of insn,
> even if they appear to set or clobber a resource referenced in insn.
> insn is always a `jump_insn` or an `insn`. On machines where
> some `insn` or `jump_insn` is really a function call and its operands
> are registers whose use is actually in the subroutine it calls, you should
> define this macro. Doing so allows the delay slot scheduler to move
> instructions which copy arguments into the argument registers into the delay
> slot of insn.
>
> You need not define this macro if it would always return zero.

— Macro: __MULTIPLE_SYMBOL_SPACES__
> Define this macro as a C expression that is nonzero if, in some cases,
> global symbols from one translation unit may not be bound to undefined
> symbols in another translation unit without user intervention. For
> instance, under Microsoft Windows symbols must be explicitly imported
> from shared libraries (DLLs).
>
> You need not define this macro if it would always evaluate to zero.

— Target Hook: tree __TARGET_MD_ASM_CLOBBERS__ (tree clobbers)
> This target hook should add to clobbers `STRING_CST` trees for
> any hard regs the port wishes to automatically clobber for all asms.
> It should return the result of the last `tree_cons` used to add a
> clobber.

— Macro: __MATH_LIBRARY__
> Define this macro as a C string constant for the linker argument to link
> in the system math library, or ``""`' if the target does not have a
> separate math library.
>
> You need only define this macro if the default of ``"-lm"`' is wrong.

— Macro: __LIBRARY_PATH_ENV__
> Define this macro as a C string constant for the environment variable that
> specifies where the linker should look for libraries.
>
> You need only define this macro if the default of ``"LIBRARY_PATH"`'
> is wrong.

— Macro: __TARGET_HAS_F_SETLKW__
> Define this macro if the target supports file locking with fcntl / F_SETLKW.
> Note that this functionality is part of POSIX.
> Defining `TARGET_HAS_F_SETLKW` will enable the test coverage code
> to use file locking when exiting a program, which avoids race conditions
> if the program has forked.

— Macro: __MAX_CONDITIONAL_EXECUTE__
> A C expression for the maximum number of instructions to execute via
> conditional execution instructions instead of a branch. A value of
> `BRANCH_COST`+1 is the default if the machine does not use cc0, and
> 1 if it does use cc0.

— Macro: __IFCVT_MODIFY_TESTS__ (ce_info, true_expr, false_expr)
> Used if the target needs to perform machine-dependent modifications on the
> conditionals used for turning basic blocks into conditionally executed code.
> ce_info points to a data structure, `struct ce_if_block`, which
> contains information about the currently processed blocks. true_expr
> and false_expr are the tests that are used for converting the
> then-block and the else-block, respectively. Set either true_expr or
> false_expr to a null pointer if the tests cannot be converted.

— Macro: __IFCVT_MODIFY_MULTIPLE_TESTS__ (ce_info, bb, true_expr, false_expr)
> Like `IFCVT_MODIFY_TESTS`, but used when converting more complicated
> if-statements into conditions combined by `and` and `or` operations.
> bb contains the basic block that contains the test that is currently
> being processed and about to be turned into a condition.

— Macro: __IFCVT_MODIFY_INSN__ (ce_info, pattern, insn)
> A C expression to modify the PATTERN of an INSN that is to
> be converted to conditional execution format. ce_info points to
> a data structure, `struct ce_if_block`, which contains information
> about the currently processed blocks.

— Macro: __IFCVT_MODIFY_FINAL__ (ce_info)
> A C expression to perform any final machine dependent modifications in
> converting code to conditional execution. The involved basic blocks
> can be found in the `struct ce_if_block` structure that is pointed
> to by ce_info.

— Macro: __IFCVT_MODIFY_CANCEL__ (ce_info)
> A C expression to cancel any machine dependent modifications in
> converting code to conditional execution. The involved basic blocks
> can be found in the `struct ce_if_block` structure that is pointed
> to by ce_info.

— Macro: __IFCVT_INIT_EXTRA_FIELDS__ (ce_info)
> A C expression to initialize any extra fields in a `struct ce_if_block`
> structure, which are defined by the `IFCVT_EXTRA_FIELDS` macro.

— Macro: __IFCVT_EXTRA_FIELDS__
> If defined, it should expand to a set of field declarations that will be
> added to the `struct ce_if_block` structure. These should be initialized
> by the `IFCVT_INIT_EXTRA_FIELDS` macro.

— Target Hook: void __TARGET_MACHINE_DEPENDENT_REORG__ ()
> If non-null, this hook performs a target-specific pass over the
> instruction stream. The compiler will run it at all optimization levels,
> just before the point at which it normally does delayed-branch scheduling.
>
> The exact purpose of the hook varies from target to target. Some use
> it to do transformations that are necessary for correctness, such as
> laying out in-function constant pools or avoiding hardware hazards.
> Others use it as an opportunity to do some machine-dependent optimizations.
>
> You need not implement the hook if it has nothing to do. The default
> definition is null.

— Target Hook: void __TARGET_INIT_BUILTINS__ ()
> Define this hook if you have any machine-specific built-in functions
> that need to be defined. It should be a function that performs the
> necessary setup.
>
> Machine specific built-in functions can be useful to expand special machine
> instructions that would otherwise not normally be generated because
> they have no equivalent in the source language (for example, SIMD vector
> instructions or prefetch instructions).
>
> To create a built-in function, call the function
> `lang_hooks.builtin_function`
> which is defined by the language front end. You can use any type nodes set
> up by `build_common_tree_nodes` and `build_common_tree_nodes_2`;
> only language front ends that use those two functions will call
> ``TARGET_INIT_BUILTINS`'.

— Target Hook: rtx __TARGET_EXPAND_BUILTIN__ (tree exp, rtx target, rtx subtarget, enum machine_mode mode, int ignore)
> Expand a call to a machine specific built-in function that was set up by
> ``TARGET_INIT_BUILTINS`'. exp is the expression for the
> function call; the result should go to target if that is
> convenient, and have mode mode if that is convenient.
> subtarget may be used as the target for computing one of
> exp's operands. ignore is nonzero if the value is to be
> ignored. This function should return the result of the call to the
> built-in function.

— Target Hook: tree __TARGET_FOLD_BUILTIN__ (tree exp, bool ignore)
> Expand a call to a machine specific built-in function that was set up by
> ``TARGET_INIT_BUILTINS`'. exp is the expression for the
> function call; the result is another tree containing a simplified
> expression for the call's result. If ignore is true the
> value will be ignored.

— Macro: __MD_CAN_REDIRECT_BRANCH__ (branch1, branch2)
> Take a branch insn in branch1 and another in branch2.
> Return true if redirecting branch1 to the destination of
> branch2 is possible.
>
> On some targets, branches may have a limited range. Optimizing the
> filling of delay slots can result in branches being redirected, and this
> may in turn cause a branch offset to overflow.

— Macro: __ALLOCATE_INITIAL_VALUE__ (hard_reg)
> When the initial value of a hard register has been copied in a pseudo
> register, it is often not necessary to actually allocate another register
> to this pseudo register, because the original hard register or a stack slot
> it has been saved into can be used. `ALLOCATE_INITIAL_VALUE`, if
> defined, is called at the start of register allocation once for each
> hard register that had its initial value copied by using
> `get_func_hard_reg_initial_val` or `get_hard_reg_initial_val`.
> Possible values are `NULL_RTX`, if you don't want
> to do any special allocation, a `REG` rtx—that would typically be
> the hard register itself, if it is known not to be clobbered—or a
> `MEM`.
> If you are returning a `MEM`, this is only a hint for the allocator;
> it might decide to use another register anyways.
> You may use `current_function_leaf_function` in the definition of the
> macro, functions that use `REG_N_SETS`, to determine if the hard
> register in question will not be clobbered.

— Macro: __TARGET_OBJECT_SUFFIX__
> Define this macro to be a C string representing the suffix for object
> files on your target machine. If you do not define this macro, GCC will
> use ``.o`' as the suffix for object files.

— Macro: __TARGET_EXECUTABLE_SUFFIX__
> Define this macro to be a C string representing the suffix to be
> automatically added to executable files on your target machine. If you
> do not define this macro, GCC will use the null string as the suffix for
> executable files.

— Macro: __COLLECT_EXPORT_LIST__
> If defined, `collect2` will scan the individual object files
> specified on its command line and create an export list for the linker.
> Define this macro for systems like AIX, where the linker discards
> object files that are not referenced from `main` and uses export
> lists.

— Macro: __MODIFY_JNI_METHOD_CALL__ (mdecl)
> Define this macro to a C expression representing a variant of the
> method call mdecl, if Java Native Interface (JNI) methods
> must be invoked differently from other methods on your target.
> For example, on 32-bit Microsoft Windows, JNI methods must be invoked using
> the `stdcall` calling convention and this macro is then
> defined as this expression:
>
> ```
>           build_type_attribute_variant (mdecl,
>                                         build_tree_list
>                                         (get_identifier ("stdcall"),
>                                          NULL))
>
> ```

— Target Hook: bool __TARGET_CANNOT_MODIFY_JUMPS_P__ (void)
> This target hook returns `true` past the point in which new jump
> instructions could be created. On machines that require a register for
> every jump such as the SHmedia ISA of SH5, this point would typically be
> reload, so this target hook should be defined to a function such as:
>
> ```
>           static bool
>           cannot_modify_jumps_past_reload_p ()
>           {
>             return (reload_completed || reload_in_progress);
>           }
>
> ```

— Target Hook: int __TARGET_BRANCH_TARGET_REGISTER_CLASS__ (void)
> This target hook returns a register class for which branch target register
> optimizations should be applied. All registers in this class should be
> usable interchangeably. After reload, registers in this class will be
> re-allocated and loads will be hoisted out of loops and be subjected
> to inter-block scheduling.

— Target Hook: bool __TARGET_BRANCH_TARGET_REGISTER_CALLEE_SAVED__ (bool after_prologue_epilogue_gen)
> Branch target register optimization will by default exclude callee-saved
> registers
> that are not already live during the current function; if this target hook
> returns true, they will be included. The target code must than make sure
> that all target registers in the class returned by
> ``TARGET_BRANCH_TARGET_REGISTER_CLASS`' that might need saving are
> saved. after_prologue_epilogue_gen indicates if prologues and
> epilogues have already been generated. Note, even if you only return
> true when after_prologue_epilogue_gen is false, you still are likely
> to have to make special provisions in `INITIAL_ELIMINATION_OFFSET`
> to reserve space for caller-saved target registers.

— Macro: __POWI_MAX_MULTS__
> If defined, this macro is interpreted as a signed integer C expression
> that specifies the maximum number of floating point multiplications
> that should be emitted when expanding exponentiation by an integer
> constant inline. When this value is defined, exponentiation requiring
> more than this number of multiplications is implemented by calling the
> system library's `pow`, `powf` or `powl` routines.
> The default value places no upper bound on the multiplication count.

— Macro: void __TARGET_EXTRA_INCLUDES__ (const char \*sysroot, const char \*iprefix, int stdinc)
> This target hook should register any extra include files for the
> target. The parameter stdinc indicates if normal include files
> are present. The parameter sysroot is the system root directory.
> The parameter iprefix is the prefix for the gcc directory.

— Macro: void __TARGET_EXTRA_PRE_INCLUDES__ (const char \*sysroot, const char \*iprefix, int stdinc)
> This target hook should register any extra include files for the
> target before any standard headers. The parameter stdinc
> indicates if normal include files are present. The parameter
> sysroot is the system root directory. The parameter
> iprefix is the prefix for the gcc directory.

— Macro: void __TARGET_OPTF__ (char \*path)
> This target hook should register special include paths for the target.
> The parameter path is the include to register. On Darwin
> systems, this is used for Framework includes, which have semantics
> that are different from `-I`.

— Target Hook: bool __TARGET_USE_LOCAL_THUNK_ALIAS_P__ (tree fndecl)
> This target hook returns `true` if it is safe to use a local alias
> for a virtual function fndecl when constructing thunks,
> `false` otherwise. By default, the hook returns `true` for all
> functions, if a target supports aliases (i.e. defines
> `ASM_OUTPUT_DEF`), `false` otherwise,

— Macro: __TARGET_FORMAT_TYPES__
> If defined, this macro is the name of a global variable containing
> target-specific format checking information for the `-Wformat`
> option. The default is to have no target-specific format checks.

— Macro: __TARGET_N_FORMAT_TYPES__
> If defined, this macro is the number of entries in
> `TARGET_FORMAT_TYPES`.

— Target Hook: bool __TARGET_RELAXED_ORDERING__
> If set to `true`, means that the target's memory model does not
> guarantee that loads which do not depend on one another will access
> main memory in the order of the instruction stream; if ordering is
> important, an explicit memory barrier must be used. This is true of
> many recent processors which implement a policy of “relaxed,”
> “weak,” or “release” memory consistency, such as Alpha, PowerPC,
> and ia64. The default is `false`.

— Target Hook: const __char__ \*TARGET_INVALID_ARG_FOR_UNPROTOTYPED_FN (tree typelist, tree funcdecl, tree val)
> If defined, this macro returns the diagnostic message when it is
> illegal to pass argument val to function funcdecl
> with prototype typelist.

— Macro: __TARGET_USE_JCR_SECTION__
> This macro determines whether to use the JCR section to register Java
> classes. By default, TARGET_USE_JCR_SECTION is defined to 1 if both
> SUPPORTS_WEAK and TARGET_HAVE_NAMED_SECTIONS are true, else 0.
