---
title: GNU Compiler Collection (GCC) Internals
apple_id: TP40006804
resource_type: Guide
platform: Xcode Developer Tools
topic: null
technology: null
published: '2012-07-23'
source_url: https://developer.apple.com/library/archive/documentation/DeveloperTools/gcc-4.0.1/gccint/Machine-Constraints.html
archived_at: '2026-07-15T07:31:00.240108Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [GNU Compiler Collection (GCC) Internals](index.md)



Previous: [Modifiers](Modifiers.md#apple-jvxwi2lgnfsxe4y),
Up: [Constraints](Constraints.md#apple-inxw443uojqws3tuom)

---

#### 12.8.5 Constraints for Particular Machines

Whenever possible, you should use the general-purpose constraint letters
in `asm` arguments, since they will convey meaning more readily to
people reading your code. Failing that, use the constraint letters
that usually have very similar meanings across architectures. The most
commonly used constraints are ``m`' and ``r`' (for memory and
general-purpose registers respectively; see [Simple Constraints](Simple-Constraints.md#apple-knuw24dmmuwug33oon2heyljnz2hg)), and
``I`', usually the letter indicating the most common
immediate-constant format.

For each machine architecture, the
`config/machine/machine.h` file defines additional
constraints. These constraints are used by the compiler itself for
instruction generation, as well as for `asm` statements; therefore,
some of the constraints are not particularly interesting for `asm`.
The constraints are defined through these macros:

**`REG_CLASS_FROM_LETTER`**
: Register class constraints (usually lowercase).

**`CONST_OK_FOR_LETTER_P`**
: Immediate constant constraints, for non-floating point constants of
word size or smaller precision (usually uppercase).

**`CONST_DOUBLE_OK_FOR_LETTER_P`**
: Immediate constant constraints, for all floating point constants and for
constants of greater than word size precision (usually uppercase).

**`EXTRA_CONSTRAINT`**
: Special cases of registers or memory. This macro is not required, and
is only defined for some machines.

Inspecting these macro definitions in the compiler source for your
machine is the best way to be certain you have the right constraints.
However, here is a summary of the machine-dependent constraints
available on some particular machines.

**_ARM family—_arm.h**
: **`f`**
: Floating-point register

**`w`**
: VFP floating-point register

**`F`**
: One of the floating-point constants 0.0, 0.5, 1.0, 2.0, 3.0, 4.0, 5.0
or 10.0

**`G`**
: Floating-point constant that would satisfy the constraint ``F`' if it
were negated

**`I`**
: Integer that is valid as an immediate operand in a data processing
instruction. That is, an integer in the range 0 to 255 rotated by a
multiple of 2

**`J`**
: Integer in the range −4095 to 4095

**`K`**
: Integer that satisfies constraint ``I`' when inverted (ones complement)

**`L`**
: Integer that satisfies constraint ``I`' when negated (twos complement)

**`M`**
: Integer in the range 0 to 32

**`Q`**
: A memory reference where the exact address is in a single register
(```m`'' is preferable for `asm` statements)

**`R`**
: An item in the constant pool

**`S`**
: A symbol in the text segment of the current file

**_Uv_**
: A memory reference suitable for VFP load/store insns (reg+constant offset)

**_Uy_**
: A memory reference suitable for iWMMXt load/store instructions.

**_Uq_**
: A memory reference suitable for the ARMv4 ldrsb instruction.

**_AVR family—_avr.h**
: **`l`**
: Registers from r0 to r15

**`a`**
: Registers from r16 to r23

**`d`**
: Registers from r16 to r31

**`w`**
: Registers from r24 to r31. These registers can be used in ``adiw`' command

**`e`**
: Pointer register (r26–r31)

**`b`**
: Base pointer register (r28–r31)

**`q`**
: Stack pointer register (SPH:SPL)

**`t`**
: Temporary register r0

**`x`**
: Register pair X (r27:r26)

**`y`**
: Register pair Y (r29:r28)

**`z`**
: Register pair Z (r31:r30)

**`I`**
: Constant greater than −1, less than 64

**`J`**
: Constant greater than −64, less than 1

**`K`**
: Constant integer 2

**`L`**
: Constant integer 0

**`M`**
: Constant that fits in 8 bits

**`N`**
: Constant integer −1

**`O`**
: Constant integer 8, 16, or 24

**`P`**
: Constant integer 1

**`G`**
: A floating point constant 0.0

**_PowerPC and IBM RS6000—_rs6000.h**
: **`b`**
: Address base register

**`f`**
: Floating point register

**`v`**
: Vector register

**`h`**
: ``MQ`', ``CTR`', or ``LINK`' register

**`q`**
: ``MQ`' register

**`c`**
: ``CTR`' register

**`l`**
: ``LINK`' register

**`x`**
: ``CR`' register (condition register) number 0

**`y`**
: ``CR`' register (condition register)

**`z`**
: ``FPMEM`' stack memory for FPR-GPR transfers

**`I`**
: Signed 16-bit constant

**`J`**
: Unsigned 16-bit constant shifted left 16 bits (use ``L`' instead for
`SImode` constants)

**`K`**
: Unsigned 16-bit constant

**`L`**
: Signed 16-bit constant shifted left 16 bits

**`M`**
: Constant larger than 31

**`N`**
: Exact power of 2

**`O`**
: Zero

**`P`**
: Constant whose negation is a signed 16-bit constant

**`G`**
: Floating point constant that can be loaded into a register with one
instruction per word

**`Q`**
: Memory operand that is an offset from a register (``m`' is preferable
for `asm` statements)

**`R`**
: AIX TOC entry

**`S`**
: Constant suitable as a 64-bit mask operand

**`T`**
: Constant suitable as a 32-bit mask operand

**`U`**
: System V Release 4 small data area reference

**_Intel 386—_i386.h**
: **`q`**
: ``a`', `b`, `c`, or `d` register for the i386.
For x86-64 it is equivalent to ``r`' class (for 8-bit instructions that
do not use upper halves).

**`Q`**
: ``a`', `b`, `c`, or `d` register (for 8-bit instructions,
that do use upper halves).

**`R`**
: Legacy register—equivalent to `r` class in i386 mode.
(for non-8-bit registers used together with 8-bit upper halves in a single
instruction)

**`A`**
: Specifies the ``a`' or ``d`' registers. This is primarily useful
for 64-bit integer values (when in 32-bit mode) intended to be returned
with the ``d`' register holding the most significant bits and the
``a`' register holding the least significant bits.

**`f`**
: Floating point register

**`t`**
: First (top of stack) floating point register

**`u`**
: Second floating point register

**`a`**
: ``a`' register

**`b`**
: ``b`' register

**`c`**
: ``c`' register

**`C`**
: Specifies constant that can be easily constructed in SSE register without
loading it from memory.

**`d`**
: ``d`' register

**`D`**
: ``di`' register

**`S`**
: ``si`' register

**`x`**
: ``xmm`' SSE register

**`y`**
: MMX register

**`I`**
: Constant in range 0 to 31 (for 32-bit shifts)

**`J`**
: Constant in range 0 to 63 (for 64-bit shifts)

**`K`**
: ``0xff`'

**`L`**
: ``0xffff`'

**`M`**
: 0, 1, 2, or 3 (shifts for `lea` instruction)

**`N`**
: Constant in range 0 to 255 (for `out` instruction)

**`Z`**
: Constant in range 0 to `0xffffffff` or symbolic reference known to fit specified range.
(for using immediates in zero extending 32-bit to 64-bit x86-64 instructions)

**`e`**
: Constant in range −2147483648 to 2147483647 or symbolic reference known to fit specified range.
(for using immediates in 64-bit x86-64 instructions)

**`G`**
: Standard 80387 floating point constant

**_Intel IA-64—_ia64.h**
: **`a`**
: General register `r0` to `r3` for `addl` instruction

**`b`**
: Branch register

**`c`**
: Predicate register (``c`' as in “conditional”)

**`d`**
: Application register residing in M-unit

**`e`**
: Application register residing in I-unit

**`f`**
: Floating-point register

**`m`**
: Memory operand.
Remember that ``m`' allows postincrement and postdecrement which
require printing with ``%Pn`' on IA-64.
Use ``S`' to disallow postincrement and postdecrement.

**`G`**
: Floating-point constant 0.0 or 1.0

**`I`**
: 14-bit signed integer constant

**`J`**
: 22-bit signed integer constant

**`K`**
: 8-bit signed integer constant for logical instructions

**`L`**
: 8-bit adjusted signed integer constant for compare pseudo-ops

**`M`**
: 6-bit unsigned integer constant for shift counts

**`N`**
: 9-bit signed integer constant for load and store postincrements

**`O`**
: The constant zero

**`P`**
: 0 or −1 for `dep` instruction

**`Q`**
: Non-volatile memory for floating-point loads and stores

**`R`**
: Integer constant in the range 1 to 4 for `shladd` instruction

**`S`**
: Memory operand except postincrement and postdecrement

**_FRV—_frv.h**
: **`a`**
: Register in the class `ACC_REGS` (`acc0` to `acc7`).

**`b`**
: Register in the class `EVEN_ACC_REGS` (`acc0` to `acc7`).

**`c`**
: Register in the class `CC_REGS` (`fcc0` to `fcc3` and
`icc0` to `icc3`).

**`d`**
: Register in the class `GPR_REGS` (`gr0` to `gr63`).

**`e`**
: Register in the class `EVEN_REGS` (`gr0` to `gr63`).
Odd registers are excluded not in the class but through the use of a machine
mode larger than 4 bytes.

**`f`**
: Register in the class `FPR_REGS` (`fr0` to `fr63`).

**`h`**
: Register in the class `FEVEN_REGS` (`fr0` to `fr63`).
Odd registers are excluded not in the class but through the use of a machine
mode larger than 4 bytes.

**`l`**
: Register in the class `LR_REG` (the `lr` register).

**`q`**
: Register in the class `QUAD_REGS` (`gr2` to `gr63`).
Register numbers not divisible by 4 are excluded not in the class but through
the use of a machine mode larger than 8 bytes.

**`t`**
: Register in the class `ICC_REGS` (`icc0` to `icc3`).

**`u`**
: Register in the class `FCC_REGS` (`fcc0` to `fcc3`).

**`v`**
: Register in the class `ICR_REGS` (`cc4` to `cc7`).

**`w`**
: Register in the class `FCR_REGS` (`cc0` to `cc3`).

**`x`**
: Register in the class `QUAD_FPR_REGS` (`fr0` to `fr63`).
Register numbers not divisible by 4 are excluded not in the class but through
the use of a machine mode larger than 8 bytes.

**`z`**
: Register in the class `SPR_REGS` (`lcr` and `lr`).

**`A`**
: Register in the class `QUAD_ACC_REGS` (`acc0` to `acc7`).

**`B`**
: Register in the class `ACCG_REGS` (`accg0` to `accg7`).

**`C`**
: Register in the class `CR_REGS` (`cc0` to `cc7`).

**`G`**
: Floating point constant zero

**`I`**
: 6-bit signed integer constant

**`J`**
: 10-bit signed integer constant

**`L`**
: 16-bit signed integer constant

**`M`**
: 16-bit unsigned integer constant

**`N`**
: 12-bit signed integer constant that is negative—i.e. in the
range of −2048 to −1

**`O`**
: Constant zero

**`P`**
: 12-bit signed integer constant that is greater than zero—i.e. in the
range of 1 to 2047.

**_Blackfin family—_bfin.h**
: **`a`**
: P register

**`d`**
: D register

**`z`**
: A call clobbered P register.

**`D`**
: Even-numbered D register

**`W`**
: Odd-numbered D register

**`e`**
: Accumulator register.

**`A`**
: Even-numbered accumulator register.

**`B`**
: Odd-numbered accumulator register.

**`b`**
: I register

**`B`**
: B register

**`f`**
: M register

**`c`**
: Registers used for circular buffering, i.e. I, B, or L registers.

**`C`**
: The CC register.

**`x`**
: Any D, P, B, M, I or L register.

**`y`**
: Additional registers typically used only in prologues and epilogues: RETS,
RETN, RETI, RETX, RETE, ASTAT, SEQSTAT and USP.

**`w`**
: Any register except accumulators or CC.

**`Ksh`**
: Signed 16 bit integer (in the range -32768 to 32767)

**`Kuh`**
: Unsigned 16 bit integer (in the range 0 to 65535)

**`Ks7`**
: Signed 7 bit integer (in the range -64 to 63)

**`Ku7`**
: Unsigned 7 bit integer (in the range 0 to 127)

**`Ku5`**
: Unsigned 5 bit integer (in the range 0 to 31)

**`Ks4`**
: Signed 4 bit integer (in the range -8 to 7)

**`Ks3`**
: Signed 3 bit integer (in the range -3 to 4)

**`Ku3`**
: Unsigned 3 bit integer (in the range 0 to 7)

**`P`n**
: Constant n, where n is a single-digit constant in the range 0 to 4.

**`M1`**
: Constant 255.

**`M2`**
: Constant 65535.

**`J`**
: An integer constant with exactly a single bit set.

**`L`**
: An integer constant with all bits set except exactly one.

**`H`

**`Q`****
: Any SYMBOL_REF.

**_IP2K—_ip2k.h**
: **`a`**
: ``DP`' or ``IP`' registers (general address)

**`f`**
: ``IP`' register

**`j`**
: ``IPL`' register

**`k`**
: ``IPH`' register

**`b`**
: ``DP`' register

**`y`**
: ``DPH`' register

**`z`**
: ``DPL`' register

**`q`**
: ``SP`' register

**`c`**
: ``DP`' or ``SP`' registers (offsettable address)

**`d`**
: Non-pointer registers (not ``SP`', ``DP`', ``IP`')

**`u`**
: Non-SP registers (everything except ``SP`')

**`R`**
: Indirect through ``IP`'—Avoid this except for `QImode`, since we
can't access extra bytes

**`S`**
: Indirect through ``SP`' or ``DP`' with short displacement (0..127)

**`T`**
: Data-section immediate value

**`I`**
: Integers from −255 to −1

**`J`**
: Integers from 0 to 7—valid bit number in a register

**`K`**
: Integers from 0 to 127—valid displacement for addressing mode

**`L`**
: Integers from 1 to 127

**`M`**
: Integer −1

**`N`**
: Integer 1

**`O`**
: Zero

**`P`**
: Integers from 0 to 255

**_MIPS—_mips.h**
: **`d`**
: General-purpose integer register

**`f`**
: Floating-point register (if available)

**`h`**
: ``Hi`' register

**`l`**
: ``Lo`' register

**`x`**
: ``Hi`' or ``Lo`' register

**`y`**
: General-purpose integer register

**`z`**
: Floating-point status register

**`I`**
: Signed 16-bit constant (for arithmetic instructions)

**`J`**
: Zero

**`K`**
: Zero-extended 16-bit constant (for logic instructions)

**`L`**
: Constant with low 16 bits zero (can be loaded with `lui`)

**`M`**
: 32-bit constant which requires two instructions to load (a constant
which is not ``I`', ``K`', or ``L`')

**`N`**
: Negative 16-bit constant

**`O`**
: Exact power of two

**`P`**
: Positive 16-bit constant

**`G`**
: Floating point zero

**`Q`**
: Memory reference that can be loaded with more than one instruction
(``m`' is preferable for `asm` statements)

**`R`**
: Memory reference that can be loaded with one instruction
(``m`' is preferable for `asm` statements)

**`S`**
: Memory reference in external OSF/rose PIC format
(``m`' is preferable for `asm` statements)

**_Motorola 680x0—_m68k.h**
: **`a`**
: Address register

**`d`**
: Data register

**`f`**
: 68881 floating-point register, if available

**`I`**
: Integer in the range 1 to 8

**`J`**
: 16-bit signed number

**`K`**
: Signed number whose magnitude is greater than 0x80

**`L`**
: Integer in the range −8 to −1

**`M`**
: Signed number whose magnitude is greater than 0x100

**`G`**
: Floating point constant that is not a 68881 constant

**_Motorola 68HC11 & 68HC12 families—_m68hc11.h**
: **`a`**
: Register `a'

**`b`**
: Register `b'

**`d`**
: Register `d'

**`q`**
: An 8-bit register

**`t`**
: Temporary soft register _.tmp

**`u`**
: A soft register _.d1 to _.d31

**`w`**
: Stack pointer register

**`x`**
: Register `x'

**`y`**
: Register `y'

**`z`**
: Pseudo register `z' (replaced by `x' or `y' at the end)

**`A`**
: An address register: x, y or z

**`B`**
: An address register: x or y

**`D`**
: Register pair (x:d) to form a 32-bit value

**`L`**
: Constants in the range −65536 to 65535

**`M`**
: Constants whose 16-bit low part is zero

**`N`**
: Constant integer 1 or −1

**`O`**
: Constant integer 16

**`P`**
: Constants in the range −8 to 2

**_SPARC—_sparc.h**
: **`f`**
: Floating-point register on the SPARC-V8 architecture and
lower floating-point register on the SPARC-V9 architecture.

**`e`**
: Floating-point register. It is equivalent to ``f`' on the
SPARC-V8 architecture and contains both lower and upper
floating-point registers on the SPARC-V9 architecture.

**`c`**
: Floating-point condition code register.

**`d`**
: Lower floating-point register. It is only valid on the SPARC-V9
architecture when the Visual Instruction Set is available.

**`b`**
: Floating-point register. It is only valid on the SPARC-V9 architecture
when the Visual Instruction Set is available.

**`h`**
: 64-bit global or out register for the SPARC-V8+ architecture.

**`I`**
: Signed 13-bit constant

**`J`**
: Zero

**`K`**
: 32-bit constant with the low 12 bits clear (a constant that can be
loaded with the `sethi` instruction)

**`L`**
: A constant in the range supported by `movcc` instructions

**`M`**
: A constant in the range supported by `movrcc` instructions

**`N`**
: Same as ``K`', except that it verifies that bits that are not in the
lower 32-bit range are all zero. Must be used instead of ``K`' for
modes wider than `SImode`

**`O`**
: The constant 4096

**`G`**
: Floating-point zero

**`H`**
: Signed 13-bit constant, sign-extended to 32 or 64 bits

**`Q`**
: Floating-point constant whose integral representation can
be moved into an integer register using a single sethi
instruction

**`R`**
: Floating-point constant whose integral representation can
be moved into an integer register using a single mov
instruction

**`S`**
: Floating-point constant whose integral representation can
be moved into an integer register using a high/lo_sum
instruction sequence

**`T`**
: Memory address aligned to an 8-byte boundary

**`U`**
: Even register

**`W`**
: Memory address for ``e`' constraint registers

**`Y`**
: Vector zero

**_TMS320C3x/C4x—_c4x.h**
: **`a`**
: Auxiliary (address) register (ar0-ar7)

**`b`**
: Stack pointer register (sp)

**`c`**
: Standard (32-bit) precision integer register

**`f`**
: Extended (40-bit) precision register (r0-r11)

**`k`**
: Block count register (bk)

**`q`**
: Extended (40-bit) precision low register (r0-r7)

**`t`**
: Extended (40-bit) precision register (r0-r1)

**`u`**
: Extended (40-bit) precision register (r2-r3)

**`v`**
: Repeat count register (rc)

**`x`**
: Index register (ir0-ir1)

**`y`**
: Status (condition code) register (st)

**`z`**
: Data page register (dp)

**`G`**
: Floating-point zero

**`H`**
: Immediate 16-bit floating-point constant

**`I`**
: Signed 16-bit constant

**`J`**
: Signed 8-bit constant

**`K`**
: Signed 5-bit constant

**`L`**
: Unsigned 16-bit constant

**`M`**
: Unsigned 8-bit constant

**`N`**
: Ones complement of unsigned 16-bit constant

**`O`**
: High 16-bit constant (32-bit constant with 16 LSBs zero)

**`Q`**
: Indirect memory reference with signed 8-bit or index register displacement

**`R`**
: Indirect memory reference with unsigned 5-bit displacement

**`S`**
: Indirect memory reference with 1 bit or index register displacement

**`T`**
: Direct memory reference

**`U`**
: Symbolic address

**_S/390 and zSeries—_s390.h**
: **`a`**
: Address register (general purpose register except r0)

**`c`**
: Condition code register

**`d`**
: Data register (arbitrary general purpose register)

**`f`**
: Floating-point register

**`I`**
: Unsigned 8-bit constant (0–255)

**`J`**
: Unsigned 12-bit constant (0–4095)

**`K`**
: Signed 16-bit constant (−32768–32767)

**`L`**
: Value appropriate as displacement.

**`(0..4095)`**
: for short displacement

**`(-524288..524287)`**
: for long displacement

**`M`**
: Constant integer with a value of 0x7fffffff.

**`N`**
: Multiple letter constraint followed by 4 parameter letters.

**`0..9:`**
: number of the part counting from most to least significant

**`H,Q:`**
: mode of the part

**`D,S,H:`**
: mode of the containing operand

**`0,F:`**
: value of the other parts (F—all bits set)

The constraint matches if the specified part of a constant
has a value different from it's other parts.

**`Q`**
: Memory reference without index register and with short displacement.

**`R`**
: Memory reference with index register and short displacement.

**`S`**
: Memory reference without index register but with long displacement.

**`T`**
: Memory reference with index register and long displacement.

**`U`**
: Pointer with short displacement.

**`W`**
: Pointer with long displacement.

**`Y`**
: Shift count operand.

**_Xstormy16—_stormy16.h**
: **`a`**
: Register r0.

**`b`**
: Register r1.

**`c`**
: Register r2.

**`d`**
: Register r8.

**`e`**
: Registers r0 through r7.

**`t`**
: Registers r0 and r1.

**`y`**
: The carry register.

**`z`**
: Registers r8 and r9.

**`I`**
: A constant between 0 and 3 inclusive.

**`J`**
: A constant that has exactly one bit set.

**`K`**
: A constant that has exactly one bit clear.

**`L`**
: A constant between 0 and 255 inclusive.

**`M`**
: A constant between −255 and 0 inclusive.

**`N`**
: A constant between −3 and 0 inclusive.

**`O`**
: A constant between 1 and 4 inclusive.

**`P`**
: A constant between −4 and −1 inclusive.

**`Q`**
: A memory reference that is a stack push.

**`R`**
: A memory reference that is a stack pop.

**`S`**
: A memory reference that refers to a constant address of known value.

**`T`**
: The register indicated by Rx (not implemented yet).

**`U`**
: A constant that is not between 2 and 15 inclusive.

**`Z`**
: The constant 0.

**_Xtensa—_xtensa.h**
: **`a`**
: General-purpose 32-bit register

**`b`**
: One-bit boolean register

**`A`**
: MAC16 40-bit accumulator register

**`I`**
: Signed 12-bit integer constant, for use in MOVI instructions

**`J`**
: Signed 8-bit integer constant, for use in ADDI instructions

**`K`**
: Integer constant valid for BccI instructions

**`L`**
: Unsigned constant valid for BccUI instructions
