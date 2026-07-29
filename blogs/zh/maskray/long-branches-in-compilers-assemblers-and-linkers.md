---
title: 编译器、汇编器和链接器中的长分支
source: MaskRay (宋方睿)
source_key: maskray
source_url: 'https://maskray.me/blog/2026-01-25-long-branches-in-compilers-assemblers-and-linkers'
original_language: en
published: 2026-01-25
status: active
license: 未声明 → 仅私有归档
archived_at: 2026-07-27
content_hash: 'sha256:64e4985122b5bd2b'
translated: true
---

> 原文：[Long branches in compilers, assemblers, and linkers](https://maskray.me/blog/2026-01-25-long-branches-in-compilers-assemblers-and-linkers)　·　MaskRay (宋方睿)

[2026-01-25](https://maskray.me/blog/2026-01-25-long-branches-in-compilers-assemblers-and-linkers)

# 编译器、汇编器和链接器中的长分支

大多数架构上的分支指令使用 PC 相对寻址，且范围有限。当目标过远时，分支会“超出范围”，需要特殊处理。

考虑一个大型二进制文件，其中 `main()` 位于地址 0x10000，它调用位于地址 0x8010000——相距超过 128MiB——的 `foo()`。在 AArch64 上，`bl` 指令只能覆盖 ±128MiB 的范围，因此无法直接编码这个调用。如果没有适当的处理，链接器会报错“重定位超出范围”。工具链必须透明地处理此问题，以生成正确的可执行文件。

本文探讨编译器、汇编器和链接器如何协同解决长分支问题。

- 编译器（IR 到汇编）：处理函数内部超出条件分支指令范围的分支
- 汇编器（汇编到可重定位文件）：处理同一节（section）内、汇编时已知距离的分支
- 链接器：处理在最终布局期间发现的跨节和跨目标文件分支

## 分支范围限制

不同架构有不同的分支范围限制。以下是无条件/有条件分支范围的快速比较：

| 架构 | 条件分支 | 无条件分支 | 调用 | 备注 |
|---|---|---|---|---|
| AArch64 | ±1MiB | ±128MiB | ±128MiB | 桩（Thunk） |
| AArch32 (A32) | ±32MiB | ±32MiB | ±32MiB | 桩、交互工作 |
| AArch32 (T32) | ±1MiB | ±16MiB | ±16MiB | 桩、交互工作 |
| LoongArch | ±128KiB | ±128MiB | ±128MiB | 链接器松弛 |
| M68k (68020+) | ±2GiB | ±2GiB | ±2GiB | 汇编器选择尺寸 |
| MIPS (pre-R6) | ±128KiB | ±128KiB (`b offset`) | ±128KiB (`bal offset`) | 在 `-fno-pic` 代码中，伪绝对 `j`/`jal` 可用于 256MiB 区域。 |
| MIPS R6 | ±128KiB | ±128MiB | ±128MiB |  |
| PowerPC64 | ±32KiB | ±32MiB | ±32MiB | 桩 |
| RISC-V | ±4KiB | ±1MiB | ±1MiB | 链接器松弛 |
| SPARC | ±1MiB | ±8MiB | ±2GiB | 不需要桩 |
| SuperH | ±256B | ±4KiB | ±4KiB | 必要时使用寄存器间接 |
| x86-64 | ±2GiB | ±2GiB | ±2GiB | 大型代码模型更改调用序列 |
| Xtensa | ±2KiB | ±128KiB | ±512KiB | 链接器松弛 |
| z/Architecture | ±64KiB | ±4GiB | ±4GiB | 不需要桩 |

以下各小节提供每个架构的详细信息，包括与链接器实现相关的重定位类型。

### AArch32

在 A32 状态下：

- 分支（`b`/`b<cond>`）、条件分支和链接（`bl<cond>`）(`R_ARM_JUMP24`)：±32MiB
- 无条件分支和链接（`bl`/`blx`、`R_ARM_CALL`）：±32MiB

注意：`R_ARM_CALL` 用于无条件的 `bl`/`blx`，可以被松弛为内联 BLX；`R_ARM_JUMP24` 用于需要 veneer 进行交互工作的分支。

在 T32 状态下（ARMv8 之前的 Thumb 状态）：

- 条件分支（`b<cond>`、`R_ARM_THM_JUMP8`）：±256 字节
- 短无条件分支（`b`、`R_ARM_THM_JUMP11`）：±2KiB
- ARMv5T 分支和链接（`bl`/`blx`、`R_ARM_THM_CALL`）：±4MiB
- ARMv6T2 宽条件分支（`b<cond>.w`、`R_ARM_THM_JUMP19`）：±1MiB
- ARMv6T2 宽分支（`b.w`、`R_ARM_THM_JUMP24`）：±16MiB
- ARMv6T2 宽分支和链接（`bl`/`blx`、`R_ARM_THM_CALL`）：±16MiB。`R_ARM_THM_CALL` 可以被松弛为 BLX。

### AArch64

- 测试位和分支（`tbz`/`tbnz`、`R_AARCH64_TSTBR14`）：±32KiB
- 比较和分支（`cbz`/`cbnz`、`R_AARCH64_CONDBR19`）：±1MiB
- 条件分支（`b.<cond>`、`R_AARCH64_CONDBR19`）：±1MiB
- 无条件分支（`b`/`bl`、`R_AARCH64_JUMP26`/`R_AARCH64_CALL26`）：±128MiB

编译器的 `BranchRelaxation` 过程通过反转条件并插入无条件分支来处理超出范围的条件分支。AArch64 汇编器不执行分支松弛；如果编译器未处理，超出范围的分支会产生链接器错误。

### LoongArch

- 条件分支（`beq`/`bne`/`blt`/`bge`/`bltu`/`bgeu`、`R_LARCH_B16`）：±128KiB（18 位有符号）
- 比较为零分支（`beqz`/`bnez`、`R_LARCH_B21`）：±4MiB（23 位有符号）
- 无条件分支/调用（`b`/`bl`、`R_LARCH_B26`）：±128MiB（28 位有符号）
- 中程调用（`pcaddu12i`+`jirl`、`R_LARCH_CALL30`）：±2GiB
- 远程调用（`pcaddu18i`+`jirl`、`R_LARCH_CALL36`）：±128GiB

### M68k

- 短分支（`Bcc.B`/`BRA.B`/`BSR.B`）：±128 字节（8 位位移）
- 字分支（`Bcc.W`/`BRA.W`/`BSR.W`）：±32KiB（16 位位移）
- 长分支（`Bcc.L`/`BRA.L`/`BSR.L`、68020+）：±2GiB（32 位位移）

GNU Assembler 提供了[伪操作码](https://sourceware.org/binutils/docs/as/M68K_002dBranch.html)（`jbsr`、`jra`、`jXX`），可以“自动扩展到能够到达目标的最短指令”。例如，`jeq .L0` 会根据位移发出 `beq.b`、`beq.w` 或 `beq.l` 之一。

由于 68020 及更高版本提供了长格式，M68k 不需要链接器范围扩展桩。

### MIPS

- 条件分支（`beq`/`bne`/`bgez`/`bltz`/等、`R_MIPS_PC16`）：±128KiB
- PC 相对跳转（`b offset` (`bgez $zero, offset`)）：±128KiB
- PC 相对调用（`bal offset` (`bgezal $zero, offset`)）：±128KiB
- 伪绝对跳转/调用（`j`/`jal`、`R_MIPS_26`）：在当前 256MiB 区域内分支，仅适用于 `-fno-pic` 代码。在 R6 中已废弃，改为 `bc`/`balc`

Release 6 中移除的 16 位指令：

- 条件分支（`beqz16`、`R_MICROMIPS_PC7_S1`）：±128 字节
- 无条件分支（`b16`、`R_MICROMIPS_PC10_S1`）：±1KiB

MIPS Release 6：

- 无条件分支，紧凑型（`bc16`，工具链实现不明确）：±1KiB
- 比较和分支，紧凑型（`beqc`/`bnec`/`bltc`/`bgec`/等、`R_MIPS_PC16`）：±128KiB
- 寄存器与零比较并分支，紧凑型（`beqzc`/`bnezc`/等、`R_MIPS_PC21_S2`）：±4MiB
- 分支（和链接），紧凑型（`bc`/`balc`、`R_MIPS_PC26_S2`）：±128MiB

编译器长分支处理：GCC（`mips_output_conditional_branch`）和 LLVM（`MipsBranchExpansion`）都通过反转条件并插入无条件跳转来处理超出范围的条件分支：

LLVM 的 `MipsBranchExpansion` 过程处理超出范围的分支。

lld 为 MIPS PIC/非 PIC 交互工作实现了 LA25 桩，但没有范围扩展桩。GNU ld 也没有为 MIPS 实现范围扩展桩。

GCC 的 mips 移植在 1993 年 3 月[添加了 `-mlong-calls`](https://gcc.gnu.org/git/?p=gcc.git;a=commit;h=d1399bd0ff3893bb9ebea7b977c7f3ec91b728b0)。在 `-mno-abicalls` 模式下，GCC 的 `-mlong-calls` 选项（[于 1993 年添加](https://gcc.gnu.org/git/?p=gcc.git;a=commit;h=d1399bd0ff3893bb9ebea7b977c7f3ec91b728b0)）生成可以到达任何地址的间接调用序列。

### PowerPC

- 条件分支（`bc`/`bcl`、`R_PPC64_REL14`）：±32KiB
- 无条件分支（`b`/`bl`、`R_PPC64_REL24`/`R_PPC64_REL24_NOTOC`）：±32MiB

GCC 生成的代码依赖于链接器桩。但是，可以使用传统的 `-mlongcall` 来生成长代码序列。

### RISC-V

- 压缩 `c.beqz`：±256 字节
- 压缩 `c.jal`：±2KiB
- `jalr`（I 型立即数）：±2KiB
- 条件分支（`beq`/`bne`/`blt`/`bge`/`bltu`/`bgeu`、B 型立即数）：±4KiB
- `jal`（J 型立即数、`PseudoBR`）：±1MiB（明显小于其他 RISC 架构：AArch64 ±128MiB、PowerPC64 ±32MiB、LoongArch ±128MiB）
- `PseudoJump`（使用 `auipc` + `jalr`）：±2GiB
- `beqi`/`bnei`（Zibi 扩展、5 位比较立即数（1 到 31 和 -1））：±4KiB

高通 uC Branch Immediate 扩展（Xqcibi）：

- `qc.beqi`/`qc.bnei`/`qc.blti`/`qc.bgei`/`qc.bltui`/`qc.bgeui`（32 位、5 位比较立即数）：±4KiB
- `qc.e.beqi`/`qc.e.bnei`/`qc.e.blti`/`qc.e.bgei`/`qc.e.bltui`/`qc.e.bgeui`（48 位、16 位比较立即数）：±4KiB

高通 uC Long Branch 扩展（Xqcilb）：

- `qc.e.j`/`qc.e.jal`（48 位、`R_RISCV_VENDOR(QUALCOMM)+R_RISCV_QC_E_CALL_PLT`）：±2GiB

对于函数调用：

- [Go 编译器](https://go-review.googlesource.com/c/go/+/345051) 为调用发出单个 `jal`，并依赖其链接器在目标超出范围时生成 trampoline。
- 相比之下，GCC 和 Clang 发出 `auipc`+`jalr`，并依赖链接器松弛来在可能时缩小序列。

`jal` 范围（±1MiB）明显小于其他 RISC 架构（AArch64 ±128MiB、PowerPC64 ±32MiB、LoongArch ±128MiB）。这限制了链接器松弛（“从大开始并缩小”）的有效性，并导致当编译器乐观地发出 `jal`（“从小开始并增长”）时频繁出现 trampoline。

### SPARC

- 比较和分支（`cxbe`、`R_SPARC_5`）：±64 字节
- 条件分支（`bcc`、`R_SPARC_WDISP19`）：±1MiB
- 无条件分支（`b`、`R_SPARC_WDISP22`）：±8MiB
- `call`（`R_SPARC_WDISP30`/`R_SPARC_WPLT30`）：±2GiB

由于 `call` 具有 ±2GiB 的范围，SPARC 在实践中不需要范围扩展桩。

### SuperH

SuperH 使用固定宽度的 16 位指令，这限制了分支范围。

- 条件分支（`bf`/`bt`）：±256 字节（8 位位移）
- 无条件分支（`bra`）：±4KiB（12 位位移）
- 转到子程序（`bsr`）：±4KiB（12 位位移）

对于更长的距离，使用寄存器间接分支（`braf`/`bsrf`）。编译器会反转条件，并在目标超出短范围时发出这些指令。

SuperH 由 GCC 和 binutils 支持，但不受 LLVM 支持。

### Xtensa

Xtensa 使用可变长度指令：16 位（窄，`.n` 后缀）和 24 位（标准）。

- 窄条件分支（`beqz.n`/`bnez.n`、16 位）：-28 到 +35 字节（6 位有符号 + 4）
- 条件分支（比较两个寄存器）（`beq`/`bne`/`blt`/`bge`/等、24 位）：±256 字节
- 条件分支（与零比较）（`beqz`/`bnez`/`bltz`/`bgez`、24 位）：±2KiB
- 无条件跳转（`j`、24 位）：±128KiB
- 调用（`call0`/`call4`/`call8`/`call12`、24 位）：±512KiB

汇编器执行分支松弛：当条件分支目标过远时，它会反转条件并插入 `j` 指令。

根据 [https://www.sourceware.org/binutils/docs/as/Xtensa-Call-Relaxation.html](https://www.sourceware.org/binutils/docs/as/Xtensa-Call-Relaxation.html)，对于调用，GNU Assembler 在目标距离未知时悲观地生成间接序列（`l32r`+`callx8`）。然后 GNU ld 执行链接器松弛。

### x86-64

- 短条件跳转（`Jcc rel8`）：-128 到 +127 字节
- 短无条件跳转（`JMP rel8`）：-128 到 +127 字节
- 近条件跳转（`Jcc rel32`）：±2GiB
- 近无条件跳转（`JMP rel32`）：±2GiB

由于近跳转具有 ±2GiB 的范围，x86-64 在实践中很少遇到超出范围的分支。也就是说，Google 和 Meta Platforms 在 x86-64 生产服务器上主要部署静态链接的可执行文件，并遇到了某些配置下的大型可执行文件问题。

### z/Architecture

- 短条件分支（`BRC`、`R_390_PC16DBL`）：±64KiB（16 位半字位移）
- 长条件分支（`BRCL`、`R_390_PC32DBL`）：±4GiB（32 位半字位移）
- 短调用（`BRAS`、`R_390_PC16DBL`）：±64KiB
- 长调用（`BRASL`、`R_390_PC32DBL`）：±4GiB

由于长格式具有 ±4GiB 的范围，z/Architecture 不需要链接器范围扩展桩。LLVM 的 `SystemZLongBranch` 过程将短分支（`BRC`/`BRAS`）松弛为长格式（`BRCL`/`BRASL`），当目标超出范围时。

## 编译器：分支范围处理

条件分支指令的范围通常比无条件分支指令小，这使得它们不太适合链接器桩（我们稍后将探讨）。编译器通常将条件分支目标保持在同一节内，从而允许编译器通过分支松弛来处理超出范围的情况。

在一个函数内，条件分支仍然可能超出范围。编译器会测量分支距离，并通过反转条件并插入无条件分支来对超出范围的分支进行松弛：

```plaintext
# 松弛前（超出范围）
beq .Lfar_target       # ±4KiB range on RISC-V

# 松弛后
bne .Lskip             # Inverted condition, short range
j .Lfar_target         # Unconditional jump, ±1MiB range
.Lskip:
```

某些架构的条件分支指令会与立即数比较，由于编码额外的立即数，范围更短。例如，AArch64 的 `cbz`/`cbnz`（比较并分支如果为零/非零）和 `tbz`/`tbnz`（测试位并分支）只有 ±32KiB 的范围。RISC-V Zibi 的 `beqi`/`bnei` 具有 ±4KiB 的范围。编译器以类似方式处理这些：

```plaintext
// 松弛前（cbz 具有 ±32KiB 范围）
  cbz w0, far

// 松弛后
  cbnz w0, .Lskip       // Inverted condition
  b far                 // Unconditional branch, ±128MiB range
.Lskip:
```

一名 Intel 员工在 2017 年贡献了 [https://reviews.llvm.org/D41634](https://reviews.llvm.org/D41634)，用于当无法反转分支条件时。这适用于一个外部后端。截至 2026 年 1 月，此代码路径没有内部测试。

在 LLVM 中，这由 `BranchRelaxation` 过程处理，该过程在 `AsmPrinter` 之前运行。不同的后端有自己的实现：

- `BranchRelaxation`：AArch64、AMDGPU、AVR、RISC-V
- `HexagonBranchRelaxation`：Hexagon
- `PPCBranchSelector`：PowerPC
- `SystemZLongBranch`：SystemZ
- `MipsBranchExpansion`：MIPS
- `MSP430BSel`：MSP430

通用的 `BranchRelaxation` 过程计算块大小和偏移量，然后迭代直到所有分支都在范围内。对于条件分支，它尝试反转条件并插入无条件分支。对于仍然超出范围的无条件分支，它调用 `TargetInstrInfo::insertIndirectBranch` 来发出间接跳转序列（例如，AArch64 上的 `adrp`+`add`+`br`）或长跳转序列（例如，RISC-V 上的伪 `jump`）。

注意：由于内联汇编，大小估计可能不准确。LLVM 使用启发式方法来估计内联汇编大小，但对于某些汇编构造，大小在编译时并不精确已知。

无条件分支和调用可以针对不同节，因为它们有更大的范围。如果目标超出范围，链接器可以插入桩来扩展范围。

对于 x86-64，大型代码模型使用多条指令进行调用和跳转，以支持大于 2GiB 的文本节（请参阅[重定位溢出和代码模型：x86-64 大型代码模型](https://maskray.me/blog/2023-05-14-relocation-overflow-and-code-models#x86-64-large-code-model)）。如果被调用者最终在范围内，这将是一种悲观处理。Google 和 Meta Platforms 有兴趣允许使用范围扩展桩来替代多条指令。

## 汇编器：指令松弛

汇编器将汇编转换为机器码。当分支的目标在同一节内且距离在汇编时已知时，汇编器可以选择适当的编码。这与链接器桩不同，后者处理跨节或跨目标文件的引用，其距离直到链接时才知晓。

汇编器指令松弛处理两种情况（有关示例，请参阅[Clang -O0 输出：分支位移和大小增加](https://maskray.me/blog/2024-04-27-clang-o0-output-branch-displacement-and-size-increase)）：

- **跨度相关指令（Span-dependent instructions）**：根据位移选择适当的编码。

    - 在 x86 上，短跳转（`jmp rel8`）可以在目标较远时松弛为近跳转（`jmp rel32`）。
    - 在 RISC-V 上，当位移适合 ±256 字节时，`beqz` 可以汇编为 2 字节的 `c.beqz`。
- **条件分支转换**：反转条件并插入无条件分支。在 RISC-V 上，`blt` 可能被松弛为 `bge` 加上无条件分支。

汇编器使用迭代布局算法，该算法在片段偏移分配和松弛之间交替，直到所有片段合法化。有关实现细节，请参阅[LLVM 19 中集成汇编器的改进](https://maskray.me/blog/2024-06-30-integrated-assembler-improvements-in-llvm-19)。

## 链接器：范围扩展桩

当链接器解析重定位时，它可能发现分支目标超出范围。此时，指令编码已固定，因此链接器不能简单地更改指令。相反，它会生成**范围扩展桩（range extension thunks）**（也称为 veneer、分支桩或 trampoline）。

桩是一小段链接器生成的代码，它可以使用更长的指令序列到达实际目标。原始分支被重定向到桩，然后桩跳转到真正的目的地。

范围扩展桩是链接器生成的桩的一种。其他类型包括：

- **ARM 交互工作 veneer**：在 ARM 和 Thumb 指令集之间切换（请参阅[关于 AArch32 的链接器笔记](https://maskray.me/blog/2023-04-23-linker-notes-on-aarch32)）
- **MIPS LA25 桩**：启用 PIC 和非 PIC 代码的交互工作（请参阅[关于 MIPS 的工具链笔记](https://maskray.me/blog/2023-09-04-toolchain-notes-on-mips)）
- **PowerPC64 TOC/NOTOC 桩**：处理使用不同 TOC 指针约定的函数之间的调用（请参阅[关于 Power ISA 的链接器笔记](https://maskray.me/blog/2023-02-26-linker-notes-on-power-isa)）

### 短范围桩与长范围桩

一个**短范围桩**（请参阅[lld/ELF 的 AArch64 实现](https://reviews.llvm.org/D148701)）只包含一条分支指令。由于它使用分支，它的覆盖范围也受分支范围限制——它只能扩展一个分支距离。对于更远的目标，可以链接多个短范围桩，或者必须使用带有地址计算的长范围桩。

长范围桩使用间接跳转，可以跳转到（实际上）任意位置。

```plaintext
// 短范围桩：单分支，4 字节
__AArch64AbsLongThunk_dst:
  b dst                         // ±128MiB range

// 长范围桩：地址计算，12 字节
__AArch64ADRPThunk_dst:
  adrp x16, dst                 // Load page address (±4GiB range)
  add x16, x16, :lo12:dst       // Add page offset
  br x16                        // Indirect branch
```

### 桩示例

**AArch32 (PIC)**（请参阅[关于 AArch32 的链接器笔记](https://maskray.me/blog/2023-04-23-linker-notes-on-aarch32)）：1  
2  
3  
4  
5  
__ARMV7PILongThunk_dst:  
 movw ip, :lower16:(dst - .) ; ip = 过程内调用暂存寄存器  
 movt ip, :upper16:(dst - .)  
 add ip, ip, pc  
 bx ip

**PowerPC64 ELFv2**（请参阅[关于 Power ISA 的链接器笔记](https://maskray.me/blog/2023-02-26-linker-notes-on-power-isa)）：1  
2  
3  
4  
5  
__long_branch_dst:  
 addis 12, 2, .branch_lt@ha # 从分支查找表加载高位  
 ld 12, .branch_lt@l(12) # 加载目标地址  
 mtctr 12 # 移动到计数寄存器  
 bctr # 分支到计数寄存器

### 桩对调试和分析的影响

桩在源代码级别是透明的，但在底层工具中可见：

- **堆栈回溯**：可能显示调用者和被调用者之间的桩符号（例如，`__AArch64ADRPThunk_foo`）
- **分析器**：样本可能将时间归因于桩代码；某些分析器会将桩时间与被调用函数聚合
- **反汇编**：`objdump` 或 `llvm-objdump` 会显示与常规代码交错的桩节
- **代码大小**：每个桩增加字节；大型二进制文件可能有成千上万个桩

### lld/ELF 的桩创建算法

lld/ELF 在 `finalizeAddressDependentContent` 中使用多遍算法：

```cpp
assignAddresses();
for (pass = 0; pass < 30; ++pass) {
  // 预创建空的 ThunkSections，步长约为 2 * thunkSectionSpacing。
  // 这确保对于最常见的需要桩的重定位类型，重定位可以在
  // thunkSectionSpacing 字节内找到一个 ThunkSection。
  if (pass == 0)
    createInitialThunkSections();

  bool changed = false;
  for (relocation : all_relocations) {
    // 如果此重定位需要桩且桩仍在范围内，则跳过。
    // 否则，恢复原始重定位。
    if (pass > 0 && normalizeExistingThunk(rel))
      continue;

    if (!needsThunk(rel)) continue;
    Thunk *t = getOrCreateThunk(rel);
    ts = findOrCreateThunkSection(rel, src);
    ts->addThunk(t);
    rel.sym = t->getThunkTargetSym();  // redirect
    changed = true;
  }
  // 将 ThunkSections 与常规输入节交错放置。
  mergeThunks();
  if (!changed) break;
  assignAddresses();  // recalculate with new thunks
}
```

关键细节：

- **多遍**：迭代直到收敛（最多 30 遍）。添加桩会更改地址，可能使之前处于范围内的调用超出范围。
- **预分配的 ThunkSections**：在第 0 遍，`createInitialThunkSections` 以规则间隔（`thunkSectionSpacing`）放置空 `ThunkSection`。对于 AArch64：128 MiB - 0x30000 ≈ 127.8 MiB。
- **桩重用**：如果存在针对同一目标的现有桩，`getThunk` 会返回它；`normalizeExistingThunk` 检查之前创建的桩是否仍在范围内。
- **ThunkSection 放置**：`getISDThunkSec` 在调用点的分支范围内找到一个 ThunkSection，或者在与调用 InputSection 相邻的位置创建一个。

### lld/MachO 的桩创建算法

lld/MachO 在 `TextOutputSection::finalize` 中使用单遍算法：

```cpp
for (callIdx = 0; callIdx < inputs.size(); ++callIdx) {
  // 最终确定正向分支范围内的节（减去 slack 余量）
  while (finalIdx < endIdx && fits_in_range(inputs[finalIdx]))
    finalizeOne(inputs[finalIdx++]);

  // 处理此节中的分支重定位
  for (Relocation &r : reverse(isec->relocs)) {
    if (!isBranchReloc(r)) continue;
    if (targetInRange(r)) continue;
    if (existingThunkInRange(r)) { reuse it; continue; }
    // 创建新桩并最终确定它
    createThunk(r);
  }
}
```

与 lld/ELF 的主要区别：

- **单遍**：地址单调分配，从不重新访问
- **Slack 预留**：保留 `slopScale * thunkSize` 字节（ARM64 上默认：256 × 12 = 3072 字节），为未来的桩留出空间
- **桩命名**：`<function>.thunk.<sequence>`，其中 sequence 每个目标递增

[桩饥饿问题](https://github.com/llvm/llvm-project/issues/50920)：如果许多连续分支需要桩，每个桩（12 字节）消耗 slack 的速度快于调用点（相距 4 字节）前进的速度。测试 `lld/test/MachO/arm64-thunk-starvation.s` 演示了此边缘情况。缓解措施是增加 `--slop-scale`，但包含数百个连续超出范围被调用者的病理情况仍然可能失败。

### mold 的桩创建算法

mold 使用两遍方法：

- 悲观地过度分配桩。跨节重定位和引用尚未分配地址的节的重定位悲观地需要桩。（当 `first_pass=true` 时，`requires_thunk(ctx, isec, rel, first_pass)`）
- 然后删除不必要的桩。

链接器遍顺序：

- `compute_section_sizes()` 调用 `create_range_extension_thunks()`——最终节地址**尚未**知晓
- `set_osec_offsets()` 分配节地址
- 在地址知晓**后**调用 `remove_redundant_thunks()`——检查由于跨节重定位而导致的非必需桩
- 重新运行 `set_osec_offsets()`

**第 1 遍**（`create_range_extension_thunks`）：使用滑动窗口批量处理节。窗口跟踪四个位置：

```plaintext
Sections:   [0] [1] [2] [3] [4] [5] [6] [7] [8] [9] ...
             ^       ^       ^           ^
             A       B       C           D
             |       |_______|           |
             |         batch             |
             |                           |
             earliest                    thunk
             reachable                   placement
             from C
```

- **[B, C)** = 要处理的当前批次节（大小 ≤ branch_distance/5）
- **A** = 从 C 仍可达的最早节（用于桩过期）
- **D** = 放置桩的位置（从 B 可到达的最远点）

```cpp
// 简化自 OutputSection<E>::create_range_extension_thunks
while (b < sections.size()) {
  // 推进 D：找到从 B 可达桩的最远点
  while (d < size && thunk_at_d_reachable_from_b)
    assign_address(sections[d++]);

  // 计算批次 [B, C)
  c = b + 1;
  while (c < d && sections[c] < sections[b] + batch_size) c++;

  // 推进 A：使不再可达的桩过期
  while (a < b && sections[a] + branch_distance < sections[c]) a++;
  // 使 A 之前的桩组过期：清除符号标志。
  for (; t < thunks.size() && thunks[t].offset < sections[a]; t++)
    for (sym in thunks[t].symbols) sym->flags = 0;

  // 扫描 [B,C) 的重定位。如果符号尚未分配到桩组，
  // 则将其分配到 D 处的新桩组。
  auto &thunk = thunks.emplace_back(new Thunk(offset));
  parallel_for(b, c, [&](i64 i) {
    for (rel in sections[i].relocs) {
      if (requires_thunk(rel)) {
        Symbol &sym = rel.symbol;
        if (!sym.flags.test_and_set()) {  // atomic: skip if already set
          lock_guard lock(mu);
          thunk.symbols.push_back(&sym);
        }
      }
    }
  });
  offset += thunk.size();
  b = c;  // Move to next batch
}
```

**第 2 遍**（`remove_redundant_thunks`）：在最终地址知晓后，删除实际在范围内的符号的桩条目。

关键特征：

- **悲观过度分配**：假设所有跨节调用都需要桩；稍后安全地收缩
- **批次大小**：branch_distance/5（AArch64 为 25.6 MiB，AArch32 为 3.2 MiB）
- **并行性**：在每个批次内使用 TBB 进行并行重定位扫描
- **单个分支范围**：每个架构使用一个保守的 `branch_distance`。对于 AArch32，为所有分支使用 ±16 MiB（Thumb 限制），而 lld/ELF 为 A32 分支使用 ±32 MiB。
- **桩大小不计入 D 推进**：当推进 D 时，实际桩组大小未知，因此大型桩组的末尾可能无法从批次的开头到达。
- **无收敛循环**：地址分配的单向前向传递，没有不收敛的风险

### GNU ld 的桩创建算法

每个移植都自行实现算法。没有代码共享。

GNU ld 的 AArch64 移植（`bfd/elfnn-aarch64.c`）使用迭代算法，但只有一种 stub 类型且没有查找表。

**主迭代循环**（`elfNN_aarch64_size_stubs()`）：

```c
group_sections(htab, stub_group_size, ...);  // Default: 127 MiB
layout_sections_again();

for (;;) {
  stub_changed = false;
  _bfd_aarch64_add_call_stub_entries(&stub_changed, ...);
  if (!stub_changed)
    return true;
  _bfd_aarch64_resize_stubs(htab);
  layout_sections_again();
}
```

GNU ld 的 ppc64 移植（`bfd/elf64-ppc.c`）使用迭代多遍算法，带有一个用于远程桩的分支查找表（`.branch_lt`）。

**节分组**：节按 `stub_group_size`（默认约 28-30 MiB）分组；每组获得一个 stub 节。对于 14 位条件分支（`R_PPC64_REL14`，±32KiB 范围），组大小减少 1024 倍。

**主迭代循环**（`ppc64_elf_size_stubs()`）：

```c
while (1) {
  // 扫描所有输入节中的所有重定位
  for (input_bfd; section; irela) {
    // 仅处理分支重定位（R_PPC64_REL24、R_PPC64_REL14 等）
    stub_type = ppc_type_of_stub(section, irela, ...);
    if (stub_type == ppc_stub_none)
      continue;
    // 创建或合并 stub 条目
    stub_entry = ppc_add_stub(...);
  }

  // 为所有 stub 确定大小，可能会将 long_branch 升级为 plt_branch
  bfd_hash_traverse(&stub_hash_table, ppc_size_one_stub, ...);

  // 检查收敛
  if (!stub_changed && all_sizes_stable)
    break;

  // 重新布局节
  layout_sections_again();
}
```

**收敛控制**：

- `STUB_SHRINK_ITER = 20`（[PR28827](https://sourceware.org/PR28827)）：20 次迭代后，stub 节只增长（防止振荡）
- 收敛条件：`!stub_changed && all section sizes stable`

**Stub 类型升级**：`ppc_type_of_stub()` 最初为超出范围的分支返回 `ppc_stub_long_branch`。之后 `ppc_size_one_stub()` 检查 stub 的分支是否可达；如果不可达，则升级为 `ppc_stub_plt_branch` 并在 `.branch_lt` 中分配一个 8 字节条目。

### 比较链接器桩算法

| 方面 | lld/ELF | lld/MachO | mold | GNU ld ppc64 |
|---|---|---|---|---|
| 遍数 | 多（最多 30） | 单 | 两 | 多（20 次后收缩） |
| 策略 | 迭代细化 | 滑动窗口 | 滑动窗口 | 迭代细化 |
| 桩放置 | 预分配间隔 | 内联加 slack | 批次间隔 | 每 stub 组 |

## 链接器松弛

某些架构采用不同的方法：链接器不仅可以扩展分支，还可以在目标足够近时**收缩**指令序列。RISC-V 和 LoongArch 都使用这种技术。请参阅[RISC-V 链接器松弛的阴暗面](https://maskray.me/blog/2021-03-14-the-dark-side-of-riscv-linker-relaxation)以更深入地了解其复杂性和权衡。

考虑一个使用 `call` 伪指令的函数调用，它扩展为 `auipc` + `jalr`：1  
2  
3  
4  
5  
# 链接前（8 字节）  
call ext  
# 扩展为：  
# auipc ra, %pcrel_hi(ext)  
# jalr ra, ra, %pcrel_lo(ext)

如果 `ext` 在 ±1MiB 范围内，链接器可以将其松弛为：1  
2  
# 松弛后（4 字节）  
jal ext

这是通过伴随 `R_RISCV_CALL_PLT` 重定位的 `R_RISCV_RELAX` 重定位实现的。`R_RISCV_RELAX` 重定位向链接器发出信号，表明此指令序列是可以收缩的候选对象。

链接前示例目标代码：1  
2  
3  
4  
5  
6  
7  
8  
9  
0000000000000006 \<foo\>:  
 6: 97 00 00 00 auipc ra, 0  
 R_RISCV_CALL_PLT ext  
 R_RISCV_RELAX *ABS*  
 a: e7 80 00 00 jalr ra  
 e: 97 00 00 00 auipc ra, 0  
 R_RISCV_CALL_PLT ext  
 R_RISCV_RELAX *ABS*  
 12: e7 80 00 00 jalr ra

启用松弛后链接，8 字节的 `auipc`+`jalr` 对成为 4 字节的 `jal` 指令：1  
2  
3  
4  
5  
6  
0000000000000244 \<foo\>:  
 244: 41 11 addi sp, sp, -16  
 246: 06 e4 sd ra, 8(sp)  
 248: ef 00 80 01 jal ext  
 24c: ef 00 40 01 jal ext  
 250: ef 00 00 01 jal ext

当链接器删除指令时，它还必须调整：

- 节内后续指令的偏移量
- 符号地址
- 引用受影响位置的其他重定位
- 对齐指令（`R_RISCV_ALIGN`）

这使得 RISC-V 链接器松弛比桩插入更复杂，但它提供了其他架构在链接时无法实现的代码大小优势。

LoongArch 使用类似的方法。一个 `pcaddu12i`+`jirl` 序列（`R_LARCH_CALL36`，±128GiB 范围）可以在目标足够近时松弛为单个 `bl` 指令（`R_LARCH_B26`，±128MiB 范围）。

## 诊断超出范围错误

当你遇到“重定位超出范围”错误时，检查链接器的诊断信息并定位可重定位文件和函数。确定函数调用在汇编中是如何生成的。

## 总结

处理长分支需要整个工具链的协调：

| 阶段 | 技术 | 示例 |
|---|---|---|
| 编译器 | 分支松弛过程 | 反转条件 + 添加无条件跳转 |
| 汇编器 | 指令松弛 | 反转条件 + 添加无条件跳转 |
| 链接器 | 范围扩展桩 | 生成 trampoline |
| 链接器 | 链接器松弛 | 将 `auipc`+`jalr` 收缩为 `jal`（RISC-V） |

链接器的桩生成对于大型程序尤其重要，因为函数调用可能超出分支范围。不同的链接器使用不同的算法，在复杂性、最优性和健壮性之间做出各种权衡。

RISC-V 和 LoongArch 采用的链接器松弛方法是一种替代方案，它避免了范围扩展桩，但引入了其他复杂性。

- [重定位溢出和代码模型](https://maskray.me/blog/2023-05-14-relocation-overflow-and-code-models)
- [关于 AArch32 的链接器笔记](https://maskray.me/blog/2023-04-23-linker-notes-on-aarch32)
- [关于 AArch64 的链接器笔记](https://maskray.me/blog/2023-03-05-linker-notes-on-aarch64)
- [关于 Power ISA 的链接器笔记](https://maskray.me/blog/2023-02-26-linker-notes-on-power-isa)
- [关于 x86 的链接器笔记](https://maskray.me/blog/2023-02-19-linker-notes-on-x86)
- [关于 MIPS 的工具链笔记](https://maskray.me/blog/2023-09-04-toolchain-notes-on-mips)
- [关于 z/Architecture 的工具链笔记](https://maskray.me/blog/2024-02-11-toolchain-notes-on-z-architecture)
