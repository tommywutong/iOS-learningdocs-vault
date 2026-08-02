---
title: GNU Compiler Collection (GCC) Internals
apple_id: TP40006804
resource_type: Guide
platform: Xcode Developer Tools
topic: null
technology: null
published: '2012-07-23'
source_url: https://developer.apple.com/library/archive/documentation/DeveloperTools/gcc-4.0.1/gccint/Register-Classes.html
archived_at: '2026-07-15T07:31:00.626895Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [GNU Compiler Collection (GCC) Internals](index.md)



Next: [Stack and Calling](Stack-and-Calling.md#apple-kn2gcy3lfvqw4zbninqwy3djnztq),
Previous: [Registers](Registers.md#apple-kjswo2ltorsxe4y),
Up: [Target Macros](Target-Macros.md#apple-krqxez3foqwu2yldojxxg)

---

### 13.8 Register Classes

On many machines, the numbered registers are not all equivalent.
For example, certain registers may not be allowed for indexed addressing;
certain registers may not be allowed in some instructions. These machine
restrictions are described to the compiler using register classes.

You define a number of register classes, giving each one a name and saying
which of the registers belong to it. Then you can specify register classes
that are allowed as operands to particular instruction patterns.

In general, each register will belong to several classes. In fact, one
class must be named `ALL_REGS` and contain all the registers. Another
class must be named `NO_REGS` and contain no registers. Often the
union of two classes will be another class; however, this is not required.

One of the classes must be named `GENERAL_REGS`. There is nothing
terribly special about the name, but the operand constraint letters
``r`' and ``g`' specify this class. If `GENERAL_REGS` is
the same as `ALL_REGS`, just define it as a macro which expands
to `ALL_REGS`.

Order the classes so that if class x is contained in class y
then x has a lower class number than y.

The way classes other than `GENERAL_REGS` are specified in operand
constraints is through machine-dependent operand constraint letters.
You can define such letters to correspond to various classes, then use
them in operand constraints.

You should define a class for the union of two classes whenever some
instruction allows both classes. For example, if an instruction allows
either a floating point (coprocessor) register or a general register for a
certain operand, you should define a class `FLOAT_OR_GENERAL_REGS`
which includes both of them. Otherwise you will get suboptimal code.

You must also specify certain redundant information about the register
classes: for each class, which classes contain it and which ones are
contained in it; for each pair of classes, the largest class contained
in their union.

When a value occupying several consecutive registers is expected in a
certain class, all the registers used must belong to that class.
Therefore, register classes cannot be used to enforce a requirement for
a register pair to start with an even-numbered register. The way to
specify this requirement is with `HARD_REGNO_MODE_OK`.

Register classes used for input-operands of bitwise-and or shift
instructions have a special requirement: each such class must have, for
each fixed-point machine mode, a subclass whose registers can transfer that
mode to or from memory. For example, on some machines, the operations for
single-byte values (`QImode`) are limited to certain registers. When
this is so, each register class that is used in a bitwise-and or shift
instruction must have a subclass consisting of registers from which
single-byte values can be loaded or stored. This is so that
`PREFERRED_RELOAD_CLASS` can always have a possible value to return.

— Data type: __enum reg_class__
> An enumerated type that must be defined with all the register class names
> as enumerated values. `NO_REGS` must be first. `ALL_REGS`
> must be the last register class, followed by one more enumerated value,
> `LIM_REG_CLASSES`, which is not a register class but rather
> tells how many classes there are.
>
> Each register class has a number, which is the value of casting
> the class name to type `int`. The number serves as an index
> in many of the tables described below.

— Macro: __N_REG_CLASSES__
> The number of distinct register classes, defined as follows:
>
> ```
>           #define N_REG_CLASSES (int) LIM_REG_CLASSES
>
> ```

— Macro: __REG_CLASS_NAMES__
> An initializer containing the names of the register classes as C string
> constants. These names are used in writing some of the debugging dumps.

— Macro: __REG_CLASS_CONTENTS__
> An initializer containing the contents of the register classes, as integers
> which are bit masks. The nth integer specifies the contents of class
> n. The way the integer mask is interpreted is that
> register r is in the class if mask `& (1 <<` r`)` is 1.
>
> When the machine has more than 32 registers, an integer does not suffice.
> Then the integers are replaced by sub-initializers, braced groupings containing
> several integers. Each sub-initializer must be suitable as an initializer
> for the type `HARD_REG_SET` which is defined in `hard-reg-set.h`.
> In this situation, the first integer in each sub-initializer corresponds to
> registers 0 through 31, the second integer to registers 32 through 63, and
> so on.

— Macro: __REGNO_REG_CLASS__ (regno)
> A C expression whose value is a register class containing hard register
> regno. In general there is more than one such class; choose a class
> which is minimal, meaning that no smaller class also contains the
> register.

— Macro: __BASE_REG_CLASS__
> A macro whose definition is the name of the class to which a valid
> base register must belong. A base register is one used in an address
> which is the register value plus a displacement.

— Macro: __MODE_BASE_REG_CLASS__ (mode)
> This is a variation of the `BASE_REG_CLASS` macro which allows
> the selection of a base register in a mode dependent manner. If
> mode is VOIDmode then it should return the same value as
> `BASE_REG_CLASS`.

— Macro: __MODE_BASE_REG_REG_CLASS__ (mode)
> A C expression whose value is the register class to which a valid
> base register must belong in order to be used in a base plus index
> register address. You should define this macro if base plus index
> addresses have different requirements than other base register uses.

— Macro: __INDEX_REG_CLASS__
> A macro whose definition is the name of the class to which a valid
> index register must belong. An index register is one used in an
> address where its value is either multiplied by a scale factor or
> added to another register (as well as added to a displacement).

— Macro: __CONSTRAINT_LEN__ (char, str)
> For the constraint at the start of str, which starts with the letter
> c, return the length. This allows you to have register class /
> constant / extra constraints that are longer than a single letter;
> you don't need to define this macro if you can do with single-letter
> constraints only. The definition of this macro should use
> DEFAULT_CONSTRAINT_LEN for all the characters that you don't want
> to handle specially.
> There are some sanity checks in genoutput.c that check the constraint lengths
> for the md file, so you can also use this macro to help you while you are
> transitioning from a byzantine single-letter-constraint scheme: when you
> return a negative length for a constraint you want to re-use, genoutput
> will complain about every instance where it is used in the md file.

— Macro: __REG_CLASS_FROM_LETTER__ (char)
> A C expression which defines the machine-dependent operand constraint
> letters for register classes. If char is such a letter, the
> value should be the register class corresponding to it. Otherwise,
> the value should be `NO_REGS`. The register letter ``r`',
> corresponding to class `GENERAL_REGS`, will not be passed
> to this macro; you do not need to handle it.

— Macro: __REG_CLASS_FROM_CONSTRAINT__ (char, str)
> Like `REG_CLASS_FROM_LETTER`, but you also get the constraint string
> passed in str, so that you can use suffixes to distinguish between
> different variants.

— Macro: __REGNO_OK_FOR_BASE_P__ (num)
> A C expression which is nonzero if register number num is
> suitable for use as a base register in operand addresses. It may be
> either a suitable hard register or a pseudo register that has been
> allocated such a hard register.

— Macro: __REGNO_MODE_OK_FOR_BASE_P__ (num, mode)
> A C expression that is just like `REGNO_OK_FOR_BASE_P`, except that
> that expression may examine the mode of the memory reference in
> mode. You should define this macro if the mode of the memory
> reference affects whether a register may be used as a base register. If
> you define this macro, the compiler will use it instead of
> `REGNO_OK_FOR_BASE_P`.

— Macro: __REGNO_MODE_OK_FOR_REG_BASE_P__ (num, mode)
> A C expression which is nonzero if register number num is suitable for
> use as a base register in base plus index operand addresses, accessing
> memory in mode mode. It may be either a suitable hard register or a
> pseudo register that has been allocated such a hard register. You should
> define this macro if base plus index addresses have different requirements
> than other base register uses.

— Macro: __REGNO_OK_FOR_INDEX_P__ (num)
> A C expression which is nonzero if register number num is
> suitable for use as an index register in operand addresses. It may be
> either a suitable hard register or a pseudo register that has been
> allocated such a hard register.
>
> The difference between an index register and a base register is that
> the index register may be scaled. If an address involves the sum of
> two registers, neither one of them scaled, then either one may be
> labeled the “base” and the other the “index”; but whichever
> labeling is used must fit the machine's constraints of which registers
> may serve in each capacity. The compiler will try both labelings,
> looking for one that is valid, and will reload one or both registers
> only if neither labeling works.

— Macro: __PREFERRED_RELOAD_CLASS__ (x, class)
> A C expression that places additional restrictions on the register class
> to use when it is necessary to copy value x into a register in class
> class. The value is a register class; perhaps class, or perhaps
> another, smaller class. On many machines, the following definition is
> safe:
>
> ```
>           #define PREFERRED_RELOAD_CLASS(X,CLASS) CLASS
>
> ```
>
> Sometimes returning a more restrictive class makes better code. For
> example, on the 68000, when x is an integer constant that is in range
> for a ``moveq`' instruction, the value of this macro is always
> `DATA_REGS` as long as class includes the data registers.
> Requiring a data register guarantees that a ``moveq`' will be used.
>
> One case where `PREFERRED_RELOAD_CLASS` must not return
> class is if x is a legitimate constant which cannot be
> loaded into some register class. By returning `NO_REGS` you can
> force x into a memory location. For example, rs6000 can load
> immediate values into general-purpose registers, but does not have an
> instruction for loading an immediate value into a floating-point
> register, so `PREFERRED_RELOAD_CLASS` returns `NO_REGS` when
> x is a floating-point constant. If the constant can't be loaded
> into any kind of register, code generation will be better if
> `LEGITIMATE_CONSTANT_P` makes the constant illegitimate instead
> of using `PREFERRED_RELOAD_CLASS`.

— Macro: __PREFERRED_OUTPUT_RELOAD_CLASS__ (x, class)
> Like `PREFERRED_RELOAD_CLASS`, but for output reloads instead of
> input reloads. If you don't define this macro, the default is to use
> class, unchanged.

— Macro: __LIMIT_RELOAD_CLASS__ (mode, class)
> A C expression that places additional restrictions on the register class
> to use when it is necessary to be able to hold a value of mode
> mode in a reload register for which class class would
> ordinarily be used.
>
> Unlike `PREFERRED_RELOAD_CLASS`, this macro should be used when
> there are certain modes that simply can't go in certain reload classes.
>
> The value is a register class; perhaps class, or perhaps another,
> smaller class.
>
> Don't define this macro unless the target machine has limitations which
> require the macro to do something nontrivial.

— Macro: __SECONDARY_RELOAD_CLASS__ (class, mode, x)
— Macro: __SECONDARY_INPUT_RELOAD_CLASS__ (class, mode, x)
— Macro: __SECONDARY_OUTPUT_RELOAD_CLASS__ (class, mode, x)
> Many machines have some registers that cannot be copied directly to or
> from memory or even from other types of registers. An example is the
> ``MQ`' register, which on most machines, can only be copied to or
> from general registers, but not memory. Some machines allow copying all
> registers to and from memory, but require a scratch register for stores
> to some memory locations (e.g., those with symbolic address on the RT,
> and those with certain symbolic address on the SPARC when compiling
> PIC). In some cases, both an intermediate and a scratch register are
> required.
>
> You should define these macros to indicate to the reload phase that it may
> need to allocate at least one register for a reload in addition to the
> register to contain the data. Specifically, if copying x to a
> register class in mode requires an intermediate register,
> you should define `SECONDARY_INPUT_RELOAD_CLASS` to return the
> largest register class all of whose registers can be used as
> intermediate registers or scratch registers.
>
> If copying a register class in mode to x requires an
> intermediate or scratch register, `SECONDARY_OUTPUT_RELOAD_CLASS`
> should be defined to return the largest register class required. If the
> requirements for input and output reloads are the same, the macro
> `SECONDARY_RELOAD_CLASS` should be used instead of defining both
> macros identically.
>
> The values returned by these macros are often `GENERAL_REGS`.
> Return `NO_REGS` if no spare register is needed; i.e., if x
> can be directly copied to or from a register of class in
> mode without requiring a scratch register. Do not define this
> macro if it would always return `NO_REGS`.
>
> If a scratch register is required (either with or without an
> intermediate register), you should define patterns for
> ``reload_inm`' or ``reload_outm`', as required
> (see [Standard Names](Standard-Names.md#apple-kn2gc3temfzgilkomfwwk4y). These patterns, which will normally be
> implemented with a `define_expand`, should be similar to the
> ``movm`' patterns, except that operand 2 is the scratch
> register.
>
> Define constraints for the reload register and scratch register that
> contain a single register class. If the original reload register (whose
> class is class) can meet the constraint given in the pattern, the
> value returned by these macros is used for the class of the scratch
> register. Otherwise, two additional reload registers are required.
> Their classes are obtained from the constraints in the insn pattern.
>
> x might be a pseudo-register or a `subreg` of a
> pseudo-register, which could either be in a hard register or in memory.
> Use `true_regnum` to find out; it will return −1 if the pseudo is
> in memory and the hard register number if it is in a register.
>
> These macros should not be used in the case where a particular class of
> registers can only be copied to memory and not to another class of
> registers. In that case, secondary reload registers are not needed and
> would not be helpful. Instead, a stack location must be used to perform
> the copy and the `mov`m pattern should use memory as an
> intermediate storage. This case often occurs between floating-point and
> general registers.

— Macro: __SECONDARY_MEMORY_NEEDED__ (class1, class2, m)
> Certain machines have the property that some registers cannot be copied
> to some other registers without using memory. Define this macro on
> those machines to be a C expression that is nonzero if objects of mode
> m in registers of class1 can only be copied to registers of
> class class2 by storing a register of class1 into memory
> and loading that memory location into a register of class2.
>
> Do not define this macro if its value would always be zero.

— Macro: __SECONDARY_MEMORY_NEEDED_RTX__ (mode)
> Normally when `SECONDARY_MEMORY_NEEDED` is defined, the compiler
> allocates a stack slot for a memory location needed for register copies.
> If this macro is defined, the compiler instead uses the memory location
> defined by this macro.
>
> Do not define this macro if you do not define
> `SECONDARY_MEMORY_NEEDED`.

— Macro: __SECONDARY_MEMORY_NEEDED_MODE__ (mode)
> When the compiler needs a secondary memory location to copy between two
> registers of mode mode, it normally allocates sufficient memory to
> hold a quantity of `BITS_PER_WORD` bits and performs the store and
> load operations in a mode that many bits wide and whose class is the
> same as that of mode.
>
> This is right thing to do on most machines because it ensures that all
> bits of the register are copied and prevents accesses to the registers
> in a narrower mode, which some machines prohibit for floating-point
> registers.
>
> However, this default behavior is not correct on some machines, such as
> the DEC Alpha, that store short integers in floating-point registers
> differently than in integer registers. On those machines, the default
> widening will not work correctly and you must define this macro to
> suppress that widening in some cases. See the file `alpha.h` for
> details.
>
> Do not define this macro if you do not define
> `SECONDARY_MEMORY_NEEDED` or if widening mode to a mode that
> is `BITS_PER_WORD` bits wide is correct for your machine.

— Macro: __SMALL_REGISTER_CLASSES__
> On some machines, it is risky to let hard registers live across arbitrary
> insns. Typically, these machines have instructions that require values
> to be in specific registers (like an accumulator), and reload will fail
> if the required hard register is used for another purpose across such an
> insn.
>
> Define `SMALL_REGISTER_CLASSES` to be an expression with a nonzero
> value on these machines. When this macro has a nonzero value, the
> compiler will try to minimize the lifetime of hard registers.
>
> It is always safe to define this macro with a nonzero value, but if you
> unnecessarily define it, you will reduce the amount of optimizations
> that can be performed in some cases. If you do not define this macro
> with a nonzero value when it is required, the compiler will run out of
> spill registers and print a fatal error message. For most machines, you
> should not define this macro at all.

— Macro: __CLASS_LIKELY_SPILLED_P__ (class)
> A C expression whose value is nonzero if pseudos that have been assigned
> to registers of class class would likely be spilled because
> registers of class are needed for spill registers.
>
> The default value of this macro returns 1 if class has exactly one
> register and zero otherwise. On most machines, this default should be
> used. Only define this macro to some other expression if pseudos
> allocated by `local-alloc.c` end up in memory because their hard
> registers were needed for spill registers. If this macro returns nonzero
> for those classes, those pseudos will only be allocated by
> `global.c`, which knows how to reallocate the pseudo to another
> register. If there would not be another register available for
> reallocation, you should not change the definition of this macro since
> the only effect of such a definition would be to slow down register
> allocation.

— Macro: __CLASS_MAX_NREGS__ (class, mode)
> A C expression for the maximum number of consecutive registers
> of class class needed to hold a value of mode mode.
>
> This is closely related to the macro `HARD_REGNO_NREGS`. In fact,
> the value of the macro `CLASS_MAX_NREGS (`class`,` mode`)`
> should be the maximum value of `HARD_REGNO_NREGS (`regno`,`mode`)` for all regno values in the class class.
>
> This macro helps control the handling of multiple-word values
> in the reload pass.

— Macro: __CANNOT_CHANGE_MODE_CLASS__ (from, to, class)
> If defined, a C expression that returns nonzero for a class for which
> a change from mode from to mode to is invalid.
>
> For the example, loading 32-bit integer or floating-point objects into
> floating-point registers on the Alpha extends them to 64 bits.
> Therefore loading a 64-bit object and then storing it as a 32-bit object
> does not store the low-order 32 bits, as would be the case for a normal
> register. Therefore, `alpha.h` defines `CANNOT_CHANGE_MODE_CLASS`
> as below:
>
> ```
>           #define CANNOT_CHANGE_MODE_CLASS(FROM, TO, CLASS) \
>             (GET_MODE_SIZE (FROM) != GET_MODE_SIZE (TO) \
>              ? reg_classes_intersect_p (FLOAT_REGS, (CLASS)) : 0)
>
> ```

Three other special macros describe which operands fit which constraint
letters.

— Macro: __CONST_OK_FOR_LETTER_P__ (value, c)
> A C expression that defines the machine-dependent operand constraint
> letters (``I`', ``J`', ``K`', ... ``P`') that specify
> particular ranges of integer values. If c is one of those
> letters, the expression should check that value, an integer, is in
> the appropriate range and return 1 if so, 0 otherwise. If c is
> not one of those letters, the value should be 0 regardless of
> value.

— Macro: __CONST_OK_FOR_CONSTRAINT_P__ (value, c, str)
> Like `CONST_OK_FOR_LETTER_P`, but you also get the constraint
> string passed in str, so that you can use suffixes to distinguish
> between different variants.

— Macro: __CONST_DOUBLE_OK_FOR_LETTER_P__ (value, c)
> A C expression that defines the machine-dependent operand constraint
> letters that specify particular ranges of `const_double` values
> (``G`' or ``H`').
>
> If c is one of those letters, the expression should check that
> value, an RTX of code `const_double`, is in the appropriate
> range and return 1 if so, 0 otherwise. If c is not one of those
> letters, the value should be 0 regardless of value.
>
> `const_double` is used for all floating-point constants and for
> `DImode` fixed-point constants. A given letter can accept either
> or both kinds of values. It can use `GET_MODE` to distinguish
> between these kinds.

— Macro: __CONST_DOUBLE_OK_FOR_CONSTRAINT_P__ (value, c, str)
> Like `CONST_DOUBLE_OK_FOR_LETTER_P`, but you also get the constraint
> string passed in str, so that you can use suffixes to distinguish
> between different variants.

— Macro: __EXTRA_CONSTRAINT__ (value, c)
> A C expression that defines the optional machine-dependent constraint
> letters that can be used to segregate specific types of operands, usually
> memory references, for the target machine. Any letter that is not
> elsewhere defined and not matched by `REG_CLASS_FROM_LETTER` /
> `REG_CLASS_FROM_CONSTRAINT`
> may be used. Normally this macro will not be defined.
>
> If it is required for a particular target machine, it should return 1
> if value corresponds to the operand type represented by the
> constraint letter c. If c is not defined as an extra
> constraint, the value returned should be 0 regardless of value.
>
> For example, on the ROMP, load instructions cannot have their output
> in r0 if the memory reference contains a symbolic address. Constraint
> letter ``Q`' is defined as representing a memory address that does
> _not_ contain a symbolic address. An alternative is specified with
> a ``Q`' constraint on the input and ``r`' on the output. The next
> alternative specifies ``m`' on the input and a register class that
> does not include r0 on the output.

— Macro: __EXTRA_CONSTRAINT_STR__ (value, c, str)
> Like `EXTRA_CONSTRAINT`, but you also get the constraint string passed
> in str, so that you can use suffixes to distinguish between different
> variants.

— Macro: __EXTRA_MEMORY_CONSTRAINT__ (c, str)
> A C expression that defines the optional machine-dependent constraint
> letters, amongst those accepted by `EXTRA_CONSTRAINT`, that should
> be treated like memory constraints by the reload pass.
>
> It should return 1 if the operand type represented by the constraint
> at the start of str, the first letter of which is the letter c,
> comprises a subset of all memory references including
> all those whose address is simply a base register. This allows the reload
> pass to reload an operand, if it does not directly correspond to the operand
> type of c, by copying its address into a base register.
>
> For example, on the S/390, some instructions do not accept arbitrary
> memory references, but only those that do not make use of an index
> register. The constraint letter ``Q`' is defined via
> `EXTRA_CONSTRAINT` as representing a memory address of this type.
> If the letter ``Q`' is marked as `EXTRA_MEMORY_CONSTRAINT`,
> a ``Q`' constraint can handle any memory operand, because the
> reload pass knows it can be reloaded by copying the memory address
> into a base register if required. This is analogous to the way
> a ``o`' constraint can handle any memory operand.

— Macro: __EXTRA_ADDRESS_CONSTRAINT__ (c, str)
> A C expression that defines the optional machine-dependent constraint
> letters, amongst those accepted by `EXTRA_CONSTRAINT` /
> `EXTRA_CONSTRAINT_STR`, that should
> be treated like address constraints by the reload pass.
>
> It should return 1 if the operand type represented by the constraint
> at the start of str, which starts with the letter c, comprises
> a subset of all memory addresses including
> all those that consist of just a base register. This allows the reload
> pass to reload an operand, if it does not directly correspond to the operand
> type of str, by copying it into a base register.
>
> Any constraint marked as `EXTRA_ADDRESS_CONSTRAINT` can only
> be used with the `address_operand` predicate. It is treated
> analogously to the ``p`' constraint.
