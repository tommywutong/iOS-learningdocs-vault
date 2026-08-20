---
title: GNU Compiler Collection (GCC) 4.2 Internals
apple_id: TP40007093
resource_type: Guide
platform: Xcode Developer Tools
topic: null
technology: null
published: '2012-07-23'
source_url: https://developer.apple.com/library/archive/documentation/DeveloperTools/gcc-4.2.1/gccint/Machine-Constraints.html
archived_at: '2026-07-15T07:31:02.275478Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [GNU Compiler Collection (GCC) 4.2 Internals](index.md)



Next: [Define Constraints](Define-Constraints.md#apple-irswm2lomuwug33oon2heyljnz2hg),
Previous: [Modifiers](Modifiers.md#apple-jvxwi2lgnfsxe4y),
Up: [Constraints](Constraints.md#apple-inxw443uojqws3tuom)

---

#### 14.8.5 Constraints for Particular Machines

Whenever possible, you should use the general-purpose constraint letters
in `asm` arguments, since they will convey meaning more readily to
people reading your code. Failing that, use the constraint letters
that usually have very similar meanings across architectures. The most
commonly used constraints are ``m`' and ``r`' (for memory and
general-purpose registers respectively; see [Simple Constraints](Simple-Constraints.md#apple-knuw24dmmuwug33oon2heyljnz2hg)), and
``I`', usually the letter indicating the most common
immediate-constant format.

Each architecture defines additional constraints. These constraints
are used by the compiler itself for instruction generation, as well as
for `asm` statements; therefore, some of the constraints are not
particularly useful for `asm`. Here is a summary of some of the
machine-dependent constraints available on some particular machines;
it includes both constraints that are useful for `asm` and
constraints that aren't. The compiler source file mentioned in the
table heading for each architecture is the definitive reference for
the meanings of that architecture's constraints.

**_ARM family—_config/arm/arm.h**
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

**`Uv`**
: A memory reference suitable for VFP load/store insns (reg+constant offset)

**`Uy`**
: A memory reference suitable for iWMMXt load/store instructions.

**`Uq`**
: A memory reference suitable for the ARMv4 ldrsb instruction.

**_AVR family—_config/avr/constraints.md**
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

**_CRX Architecture—_config/crx/crx.h**
: **`b`**
: Registers from r0 to r14 (registers without stack pointer)

**`l`**
: Register r16 (64-bit accumulator lo register)

**`h`**
: Register r17 (64-bit accumulator hi register)

**`k`**
: Register pair r16-r17. (64-bit accumulator lo-hi pair)

**`I`**
: Constant that fits in 3 bits

**`J`**
: Constant that fits in 4 bits

**`K`**
: Constant that fits in 5 bits

**`L`**
: Constant that is one of -1, 4, -4, 7, 8, 12, 16, 20, 32, 48

**`G`**
: Floating point constant that is legal for store immediate

**_PowerPC and IBM RS6000—_config/rs6000/rs6000.h**
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

**_MorphoTech family—_config/mt/mt.h**
: **`I`**
: Constant for an arithmetic insn (16-bit signed integer).

**`J`**
: The constant 0.

**`K`**
: Constant for a logical insn (16-bit zero-extended integer).

**`L`**
: A constant that can be loaded with `lui` (i.e. the bottom 16
bits are zero).

**`M`**
: A constant that takes two words to load (i.e. not matched by
`I`, `K`, or `L`).

**`N`**
: Negative 16-bit constants other than -65536.

**`O`**
: A 15-bit signed integer constant.

**`P`**
: A positive 16-bit constant.

**_Intel 386—_config/i386/constraints.md**
: **`R`**
: Legacy register—the eight integer registers available on all
i386 processors (`a`, `b`, `c`, `d`,
`si`, `di`, `bp`, `sp`).

**`q`**
: Any register accessible as r`l`. In 32-bit mode, `a`,
`b`, `c`, and `d`; in 64-bit mode, any integer register.

**`Q`**
: Any register accessible as r`h`: `a`, `b`,
`c`, and `d`.

**`l`**
: Any register that can be used as the index in a base+index memory
access: that is, any general register except the stack pointer.

**`a`**
: The `a` register.

**`b`**
: The `b` register.

**`c`**
: The `c` register.

**`d`**
: The `d` register.

**`S`**
: The `si` register.

**`D`**
: The `di` register.

**`A`**
: The `a` and `d` registers, as a pair (for instructions that
return half the result in one and half in the other).

**`f`**
: Any 80387 floating-point (stack) register.

**`t`**
: Top of 80387 floating-point stack (`%st(0)`).

**`u`**
: Second from top of 80387 floating-point stack (`%st(1)`).

**`y`**
: Any MMX register.

**`x`**
: Any SSE register.

**`Y`**
: Any SSE2 register.

**`I`**
: Integer constant in the range 0 ... 31, for 32-bit shifts.

**`J`**
: Integer constant in the range 0 ... 63, for 64-bit shifts.

**`K`**
: Signed 8-bit integer constant.

**`L`**
: `0xFF` or `0xFFFF`, for andsi as a zero-extending move.

**`M`**
: 0, 1, 2, or 3 (shifts for the `lea` instruction).

**`N`**
: Unsigned 8-bit integer constant (for `in` and `out`
instructions).

**`O`**
: Integer constant in the range 0 ... 127, for 128-bit shifts.

**`G`**
: Standard 80387 floating point constant.

**`C`**
: Standard SSE floating point constant.

**`e`**
: 32-bit signed integer constant, or a symbolic reference known
to fit that range (for immediate operands in sign-extending x86-64
instructions).

**`Z`**
: 32-bit unsigned integer constant, or a symbolic reference known
to fit that range (for immediate operands in zero-extending x86-64
instructions).

**_Intel IA-64—_config/ia64/ia64.h**
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

**_FRV—_config/frv/frv.h**
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

**_Blackfin family—_config/bfin/bfin.h**
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

**`v`**
: B register

**`f`**
: M register

**`c`**
: Registers used for circular buffering, i.e. I, B, or L registers.

**`C`**
: The CC register.

**`t`**
: LT0 or LT1.

**`k`**
: LC0 or LC1.

**`u`**
: LB0 or LB1.

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

**_M32C—_config/m32c/m32c.c**
: **`Rsp`

**`Rfb`

**`Rsb`******
: ``$sp`', ``$fb`', ``$sb`'.

**`Rcr`**
: Any control register, when they're 16 bits wide (nothing if control
registers are 24 bits wide)

**`Rcl`**
: Any control register, when they're 24 bits wide.

**`R0w`

**`R1w`

**`R2w`

**`R3w`********
: $r0, $r1, $r2, $r3.

**`R02`**
: $r0 or $r2, or $r2r0 for 32 bit values.

**`R13`**
: $r1 or $r3, or $r3r1 for 32 bit values.

**`Rdi`**
: A register that can hold a 64 bit value.

**`Rhl`**
: $r0 or $r1 (registers with addressable high/low bytes)

**`R23`**
: $r2 or $r3

**`Raa`**
: Address registers

**`Raw`**
: Address registers when they're 16 bits wide.

**`Ral`**
: Address registers when they're 24 bits wide.

**`Rqi`**
: Registers that can hold QI values.

**`Rad`**
: Registers that can be used with displacements ($a0, $a1, $sb).

**`Rsi`**
: Registers that can hold 32 bit values.

**`Rhi`**
: Registers that can hold 16 bit values.

**`Rhc`**
: Registers chat can hold 16 bit values, including all control
registers.

**`Rra`**
: $r0 through R1, plus $a0 and $a1.

**`Rfl`**
: The flags register.

**`Rmm`**
: The memory-based pseudo-registers $mem0 through $mem15.

**`Rpi`**
: Registers that can hold pointers (16 bit registers for r8c, m16c; 24
bit registers for m32cm, m32c).

**`Rpa`**
: Matches multiple registers in a PARALLEL to form a larger register.
Used to match function return values.

**`Is3`**
: -8 ... 7

**`IS1`**
: -128 ... 127

**`IS2`**
: -32768 ... 32767

**`IU2`**
: 0 ... 65535

**`In4`**
: -8 ... -1 or 1 ... 8

**`In5`**
: -16 ... -1 or 1 ... 16

**`In6`**
: -32 ... -1 or 1 ... 32

**`IM2`**
: -65536 ... -1

**`Ilb`**
: An 8 bit value with exactly one bit set.

**`Ilw`**
: A 16 bit value with exactly one bit set.

**`Sd`**
: The common src/dest memory addressing modes.

**`Sa`**
: Memory addressed using $a0 or $a1.

**`Si`**
: Memory addressed with immediate addresses.

**`Ss`**
: Memory addressed using the stack pointer ($sp).

**`Sf`**
: Memory addressed using the frame base register ($fb).

**`Ss`**
: Memory addressed using the small base register ($sb).

**`S1`**
: $r1h

**_MIPS—_config/mips/constraints.md**
: **`d`**
: An address register. This is equivalent to `r` unless
generating MIPS16 code.

**`f`**
: A floating-point register (if available).

**`h`**
: The `hi` register.

**`l`**
: The `lo` register.

**`x`**
: The `hi` and `lo` registers.

**`c`**
: A register suitable for use in an indirect jump. This will always be
`$25` for `-mabicalls`.

**`y`**
: Equivalent to `r`; retained for backwards compatibility.

**`z`**
: A floating-point condition code register.

**`I`**
: A signed 16-bit constant (for arithmetic instructions).

**`J`**
: Integer zero.

**`K`**
: An unsigned 16-bit constant (for logic instructions).

**`L`**
: A signed 32-bit constant in which the lower 16 bits are zero.
Such constants can be loaded using `lui`.

**`M`**
: A constant that cannot be loaded using `lui`, `addiu`
or `ori`.

**`N`**
: A constant in the range -65535 to -1 (inclusive).

**`O`**
: A signed 15-bit constant.

**`P`**
: A constant in the range 1 to 65535 (inclusive).

**`G`**
: Floating-point zero.

**`R`**
: An address that can be used in a non-macro load or store.

**_Motorola 680x0—_config/m68k/m68k.h**
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

**_Motorola 68HC11 & 68HC12 families—_config/m68hc11/m68hc11.h**
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

**_SPARC—_config/sparc/sparc.h**
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

**_TMS320C3x/C4x—_config/c4x/c4x.h**
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

**_S/390 and zSeries—_config/s390/s390.h**
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

**_Score family—_config/score/score.h**
: **`d`**
: Registers from r0 to r32.

**`e`**
: Registers from r0 to r16.

**`t`**
: r8—r11 or r22—r27 registers.

**`h`**
: hi register.

**`l`**
: lo register.

**`x`**
: hi + lo register.

**`q`**
: cnt register.

**`y`**
: lcb register.

**`z`**
: scb register.

**`a`**
: cnt + lcb + scb register.

**`c`**
: cr0—cr15 register.

**`b`**
: cp1 registers.

**`f`**
: cp2 registers.

**`i`**
: cp3 registers.

**`j`**
: cp1 + cp2 + cp3 registers.

**`I`**
: High 16-bit constant (32-bit constant with 16 LSBs zero).

**`J`**
: Unsigned 5 bit integer (in the range 0 to 31).

**`K`**
: Unsigned 16 bit integer (in the range 0 to 65535).

**`L`**
: Signed 16 bit integer (in the range −32768 to 32767).

**`M`**
: Unsigned 14 bit integer (in the range 0 to 16383).

**`N`**
: Signed 14 bit integer (in the range −8192 to 8191).

**`Z`**
: Any SYMBOL_REF.

**_Xstormy16—_config/stormy16/stormy16.h**
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

**_Xtensa—_config/xtensa/xtensa.h**
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
