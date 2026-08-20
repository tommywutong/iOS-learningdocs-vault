---
title: RISC-V 链接器松弛的阴暗面
source: MaskRay (宋方睿)
source_key: maskray
source_url: 'https://maskray.me/blog/2021-03-14-the-dark-side-of-riscv-linker-relaxation'
original_language: en
published: 2021-03-14
status: active
license: 未声明 → 仅私有归档
archived_at: 2026-07-27
content_hash: 'sha256:f4ffdc94ab1f524f'
translated: true
---

> 原文：[的阴暗面 RISC-V 链接器松弛](https://maskray.me/blog/2021-03-14-the-dark-side-of-riscv-linker-relaxation)　·　MaskRay (宋方睿)

[2021-03-14](https://maskray.me/blog/2021-03-14-the-dark-side-of-riscv-linker-relaxation)

# 的阴暗面 RISC-V 链接器松弛

更新于 2025-07。

本文介绍 RISC-V 链接器松弛并描述其缺点。

## 链接器优化/松弛

由于链接器拥有全局视图和布局信息，它可以执行一些在编译器端难以或无法做到的窥孔优化。通用的链接时代码序列转换是有风险的，因为语义信息会丢失，链接器看到的只是字节流。但是，如果候选代码序列中的每条指令都关联一个或多个重定位，那么 ABI 和实现可以赋予重定位类型（额外的）语义，使这种转换变得安全。这种技术通常被称为链接器优化或链接器松弛。术语「链接器优化」通常用于字节数不变的情况，而「链接器松弛」则用于字节数减少的情况。link-time 代码序列转换 ABI

GNU ld、gold 和 ld.lld 的 i386、x86-64 与 ppc64 移植都实现了多种链接器优化。下面是 x86-64 GOTPCRELX 优化的示例（GNU ld 自 2015 年起支持）。

```plaintext
# Load the address via GOT indirection.
movq x@GOTPCREL(%rip), %rax  # R_X86_64_REX_GOTPCRELX
# =>
# Add an offset to PC.
leaq x(%rip), %rax
```

详情请参阅[全局偏移表完全指南#GOT 优化](https://maskray.me/blog/2021-08-29-all-about-global-offset-table#got-optimization)。更多端口实现了 TLS 代码序列优化。详情请参阅 TLS 线程局部存储完全指南[线程局部 thread-local 存储](https://maskray.me/blog/2021-02-14-all-about-thread-local-storage)。

由于术语「链接时优化」与链接器松弛相似，但通常用在含义非常不同的狭义上（将符号解析传达给编译器，合并多个翻译单元的信息，并执行 IR 级别的优化），我和其他一些人使用「链接器松弛」来指代不改变代码序列长度的转换。link-time 优化

现在让我们将焦点转向链接器松弛。

RISC 架构通常需要多条指令来生成符号地址。通常有两条指令，第一条生成高位，第二条生成低位。在许多情况下，如果符号距离程序计数器足够近，则可以使用一条指令。这要求链接器能够从节中删除一条指令。

另一种情况是分支指令的设计。在某些 RISC 架构（例如 AVR）上，长指令可以被替换为短指令。RISCe.g. AVRe.g. AVR

```plaintext
jmp dest    # 4 bytes, R_AVR_CALL
# =>
rjmp dest   # 2 bytes
```

分支指令的跳转范围通常远小于 32 位地址空间。在极少数情况下，跳转目标可能超出范围。大多数 RISC 架构使用范围扩展桩（thunk）：让链接器将分支指令重定向到一个桩，该桩生成目标地址并跳转过去。RISC

## RISC-V 链接器松弛

设计者没有给诸如 `R_RISCV_HI20、R_RISCV_LO12、R_RISCV_PCREL_LO12_I、R_RISCV_PCREL_LO12_S、R_RISCV_CALL` 之类的重定位类型赋予额外的语义，而是引入了一种新的重定位类型 `R_RISCV_RELAX`。你会看到在同一个位置有两个重定位。ELF 规范指出：`R_RISCV_HI20, R_RISCV_LO12, R_RISCV_PCREL_LO12_I, R_RISCV_PCREL_LO12_S, R_RISCV_CALL``R_RISCV_RELAX`。你会看到在同一个位置有两个重定位。ELF

> 如果对同一个重定位位置（`r_offset`）应用了多个连续的重定位记录，则这些记录将被组合，而不是像上述那样独立应用。所谓「连续」，是指重定位记录在单个重定位节内是连续的。所谓「组合」，是指对上述标准应用方式进行如下修改：__`r_offset`____
>  
> - 在组合序列中除最后一次重定位操作外的所有操作中，重定位表达式的结果会被保留，而不是提取一部分并放入重定位字段。结果以适用的 ABI 处理器补充说明的完整指针精度保留。ABI
> - 在组合序列中除第一次重定位操作外的所有操作中，所使用的加数是前一次重定位操作保留的结果，而不是由重定位类型隐含的结果。
>  
> 请注意，上述规则的一个结果是：重定位类型指定的位置仅与组合序列的第一个元素相关（并且仅适用于不包含显式加数字段的重定位记录），以及与最后一个元素相关，其中该位置决定了重定位值将被放置的位置。对于组合序列中的所有其他重定位操作数，指定的位置将被忽略。
>  
> ABI 处理器补充说明可以指定某些重定位类型始终终止组合序列，或始终开始一个新的组合序列。ABI

在组合序列中，`R_RISCV_RELAX` 要求链接器可能删除字节。`R_RISCV_RELAX`

对于可能具有长距离的分支，RISC-V 使用 2 条指令。这很好地避免了范围扩展 thunk。如果分支结果是短距离的，GNU ld 可以删除一条指令，甚至压缩剩余的那条。RISC-VGNU

```plaintext
call fun                       # auipc ra, ..; jalr ra, ..(ra)
# =>
jal fun  # or c.jal fun
```

### 示例

```c
void ext(void);
void foo(void) {
  ext();
  ext();
  ext();
  ext();
}
```

```plaintext
0000000000000000 <.text>:
# sh_addralign=4, insert NOP of sh_addrline-2 bytes
       0: 01 00         nop
                0000000000000000:  R_RISCV_ALIGN        *ABS*+0x2

0000000000000002 <foo>:
       2: 41 11         addi    sp, sp, -16
       4: 06 e4         sd      ra, 8(sp)
       6: 97 00 00 00   auipc   ra, 0
                0000000000000006:  R_RISCV_CALL ext
                0000000000000006:  R_RISCV_RELAX        *ABS*
       a: e7 80 00 00   jalr    ra
       e: 97 00 00 00   auipc   ra, 0
                000000000000000e:  R_RISCV_CALL ext
                000000000000000e:  R_RISCV_RELAX        *ABS*
      12: e7 80 00 00   jalr    ra
      16: 97 00 00 00   auipc   ra, 0
                0000000000000016:  R_RISCV_CALL ext
                0000000000000016:  R_RISCV_RELAX        *ABS*
      1a: e7 80 00 00   jalr    ra
      ...
```

使用两条指令来生成调用。如果调用结果证明是短距离的，则可以删除第一条指令。

```plaintext
000000000000244 <foo>:
     244: 41 11         addi    sp, sp, -16
     246: 06 e4         sd      ra, 8(sp)
     248: ef 00 80 01   jal     24 <ext>
     24c: ef 00 40 01   jal     20 <ext>
     250: ef 00 00 01   jal     16 <ext>
     254: ef 00 c0 00   jal     12 <ext>
     258: a2 60         ld      ra, 8(sp)
     25a: 41 01         addi    sp, sp, 16
     25c: 11 a0         j       4 <ext>
     25e: 00 00         unimp
```

### 全局指针松弛

在 `-no-pie` 模式下，GNU ld 执行全局指针松弛。`-no-pie`GNU

生成可执行文件时，链接器把 `__global_pointer$` 定义在 `.sdata` 起始位置加 0x800 处。运行时会将 gp（x3）初始化为 `__global_pointer$` 的值。当要生成 `__global_pointer$` 前后 2KiB 范围内的地址时，可以用一条 `addi` 替换 `lui+addi`。

```plaintext
lui a0, %hi(sym)               # R_RISCV_HI20, R_RISCV_RELAX
addi a0, a0, %lo(sym)          # R_RISCV_LO12, R_RISCV_RELAX
# =>
addi a0, offset(gp)

.L0: auipc a0, %pcrel_hi(sym)  # R_RISCV_PCREL_HI20, R_RISCV_RELAX
addi a0, a0, %pcrel_lo(.L0)    # R_RISCV_PCREL_LO12_I, R_RISCV_RELAX
# =>
addi a0, offset(gp)
```

从 binutils 2.41 开始，GNU ld 支持 `--no-relax-gp` 来禁用全局指针松弛。GNU[`--no-relax-gp`](https://sourceware.org/git/?p=binutils-gdb.git;a=commit;h=50980ba351856dff75bb0743bfca62f4c3ab19ff)

截至 2023 年 4 月，psABI 已[提及](https://github.com/riscv-non-isa/riscv-elf-psabi-doc/pull/371) gp (x3) 可用于 platform-specific 目的。此类用途与全局指针松弛不兼容。

ld.lld [got](https://reviews.llvm.org/D143673) global pointer relaxation in April 2023. We made a deliberate choice to make `--no-relax-gp` the default.

[Haiku](https://github.com/riscv-non-isa/riscv-elf-psabi-doc/issues/298#issuecomment-1344724796)、Android 和 Fuchsia 已提及希望将 gp 用于 non-relaxation 目的。

## 汇编器影响

### 对齐指令

对齐指令的填充大小取决于其节偏移，而该偏移可能在链接器松弛期间因前一条指令大小变化而改变。为使链接器能够调整此对齐，汇编器会插入填充字节（NOP 指令）并生成一个指向其起始位置的 `R_RISCV_ALIGN` 重定位。NOP 的起始位置由 `R_RISCV_ALIGN` 偏移指定，而需要对哪条指令对齐则位于 `R_RISCV_ALIGN` 偏移加上其加数的位置。

```plaintext
call fun      # 8 bytes
.balign 16    # NOPs with an R_RISCV_ALIGN relocation
mv a1, a0
```

汇编器行为：

- 不开启链接器松弛时，不会生成 R_RISCV_ALIGN 重定位。
- 启用链接器松弛时：

    - If the alignment is larger than the minimum instruction size (2 bytes if `LLVM>=22 || enabled(RVC)`), generate `$alignment-$min_instruction_size` bytes of NOPS. These NOPs are associated with an `R_RISCV_ALIGN` relocation, using `$alignment - minimum_instruction_size` as the addend.
    - Otherwise (if the alignment is less than or equal to the minimum instruction size), no `R_RISCV_ALIGN` relocation is generated.

链接器负责删除字节，以在松弛前一条指令后维持正确的对齐。链接器只需删除字节，无需添加新字节。

在 non-RVC 代码中，最小指令大小为 4。自 LLVM 22 ([https://github.com/llvm/llvm-project/pull/150816](https://github.com/llvm/llvm-project/pull/150816)起，当对齐超过 2 时，汇编器会插入 `$alignment-2` 字节的 NOP，即使在 non-RVC 代码中也是如此。这使得 non-RVC 代码之后的 RVC 代码能够处理 2 字节调整：

```plaintext
.globl _start
_start:
// GNU ld can relax this to  6505          lui     a0, 0x1
// LLD hasn't implemented this transformation.
  lui a0, %hi(foo)

.option push
.option norelax
.option norvc
// Now we generate R_RISCV_ALIGN with addend 2, even if this is a norvc region.
.balign 4
b0:
  .word 0x3a393837
.option pop
foo:
```

**使用 `R_RISCV_ALIGN` 的可重定位链接挑战 `R_RISCV_ALIGN`**

在可重定位链接中会出现一个特定问题：当一个_没有_使用链接器松弛的节前面有一个_使用_.

对于未为特定可重定位文件或节启用链接器松弛的情况（例 e.g 如使用 `.option norelax`），汇编器不会为对齐指令生成 `R_RISCV_ALIGN` 重定位。这在 two-stage 链接过程中会引发问题：

```sh
cat > a.s <<e
.globl _start
_start:
  call foo

.section .text1,"ax"
.globl foo
foo:
e
cat > b.s <<e
.option push
.option norelax
# Assembler will not generate R_RISCV_ALIGN here
.balign 8
b0:
  .word 0x3a393837
.option pop
e
clang --target=riscv64 -mrelax -c a.s b.s

# Single-stage linking
ld.lld a.o b.o -o ab

# Two-stage linking
ld.lld -r a.o b.o -o ab.o
ld.lld ab.o -o ab.r
```

当 `ab.o` 被链接到可执行文件时，前面经过松弛的节（`a.o` 的内容）可能会缩小。由于 `R_RISCV_ALIGN` 中不存在供链接器处理的 `b.o` 重定位，因此 `.word 0x3a393837` 中的数据最终可能无法在最终可执行文件中对齐。这会产生与直接 `b.o` 链接 single-stage 不同的输出，后者会正确地对齐数据。`ld.lld a.o b.o -o ab` 的输出，后者会正确地对齐数据。

此问题在实践中可能不会导致重大问题，主要由于以下因素：

- 很少使用可重定位链接（`ld -r`).
- 文本节中的数据很少见。此类数据位于节开头或节中非常靠前（以至于前面没有任何 linker-relaxable 指令）的情况甚至更少。

为了解决此问题，我正在修改 LLD，使其在具有显式对齐要求的文本节开头合成一个 `R_RISCV_ALIGN` 重定位。这将为链接器提供必要的手段，用于调整该节的起始地址，并可能插入或删除填充以维持所需的对齐。

GNU ld 问题：[https://sourceware.org/bugzilla/show_bug.cgi?id=33236](https://sourceware.org/bugzilla/show_bug.cgi?id=33236)

**对链接器不友好**

当链接器松弛被禁用时（`ld --no-relax`). `$align-2` 或 `$align-4` 个字节并不一定能对齐后续指令。因此，即使忽略 `R_RISCV_ALIGN` 重定位并删除部分字节，链接器仍需处理 `R_RISCV_RELAX` 重定位。

ld.lld prior to 15.0 did not implement linker relaxation, and conservatively bailed out with an error like `error: relocation R_RISCV_ALIGN requires unimplemented linker relaxation`.

### 保守的汇编器行为

汇编器可能通过生成过多的重定位来表现出保守行为。例如，第一条 ALIGN 指令之前的 linker-relaxable 重定位就是冗余的。我正通过一项待定的更改来解决此问题，以移除它们：[https://github.com/llvm/llvm-project/pull/150816](https://github.com/llvm/llvm-project/pull/150816).

### 对链接器友好的 `R_RISCV_ALIGN`

在 ELF 中，许多支持链接器优化的重定位类型纯属可选功能：`R_AVR_CALL, R_PPC64_PCREL_OPT, R_X86_64_GOTPCRELX, R_X86_64_REX_GOTPCRELX`，以及支持 GD-\>LE、GD-\>IE、LD-\>LE 等优化的 TLS 重定位类型。

当前 `R_RISCV_ALIGN` 仅编码了预期的对齐值。它能否在预期的对齐值之外也编码实际 NOP 的字节？这样不支持链接器松弛的链接器就可以愉快地接受带 `-mrelax` 的目标文件。

有几种方案：

- 将实际 NOP 字段的符号部分中编码。关联的符号可以是绝对符号（`r_info` 字段的符号部分中编码。关联的符号可以是绝对符号（`st_shndx==SHN_ABS`).
- 编码 NOP 的实际字节在 NOP 位于 `r_addend` 字段的高位中。
- 引入一种新的重定位类型，与 `R_RISCV_ALIGN`.

第三种方案最不受欢迎。第一种方案应与现有实现兼容。

就此问题，我已提交[https://github.com/riscv-non-isa/riscv-elf-psabi-doc/issues/183](https://github.com/riscv-non-isa/riscv-elf-psabi-doc/issues/183)，但在为 ld.lld 实现链接器松弛后关闭了它。ld.lld.

### `.align [abs-expr[, abs-expr[, abs-expr]]]`

在 GNU 汇编器中，`.align` 的第三个参数指定了此对齐指令应跳过的最大字节数。不幸的是，这在 `R_RISCV_ALIGN` 方案中无法表示。第二个参数也同样无法表示。

### `R_RISCV_RELAX` 松弛并不使用本地 RVC 状态

`R_RISCV_RELAX` 松弛使用 `e_eflags & EF_RISCV_RVC`ELF 头部中的 `.option norvc` 区域。在以下示例中（改编自[https://github.com/riscv-collab/riscv-gnu-toolchain/issues/445](https://github.com/riscv-collab/riscv-gnu-toolchain/issues/445)), `tail foo`，tail foo`c.j foo` 将被松弛为压缩指令 `.option norvc`.

```plaintext
.option rvc
  add a0, a0, a1
  add a1, a1, a2
  .balign 4        # 2 bytes padding, R_RISCV_ALIGN

.option norvc
  add a0, a1, a2
  tail foo         # R_RISCV_CALL_PLT+R_RISCV_RELAX
  .balign 8        # 4 bytes padding, R_RISCV_ALIGN
foo:
```

更糟糕的是，这 4 个填充字节无法满足 `.bliang 8`. GNU 的要求。GNU ld 将报告错误 `6 bytes required for alignment to 8-byte boundary, but only 4 present`. 1  
2  
3  
4  
5  
0: add a0，a0，a1
2: add a1，a1，a2
4: add a0，a1，a2
8: c.j foo
10: // 需要 6 个字节来满足 .balign 8，但只有 4 个填充字节

### 针对局部符号的重定位

对于同一节内对局部符号的引用（例如，分支目标），传统上不需要重定位，因为重定位在汇编时已解析。但使用链接器松弛时，我们需要保留重定位，因为偏移量可能在链接时发生变化。e.g 对于同一节内对局部符号的引用（例如，分支目标），传统上不需要重定位，因为重定位在汇编时已解析。但使用链接器松弛时，我们需要保留重定位，因为偏移量可能在链接时发生变化。

```plaintext
.globl fun
fun:
  jmp .L0     # No relocation
.L0:
  call local0 # No relocation

local0:
```

对于汇编中的标签差值 `A-B`，如果 A 与 B 之间隔着一条可由链接器松弛的指令，就应生成一对 ADD/SUB 重定位（例如 `R_RISCV_ADD32`/`R_RISCV_SUB32`、`R_RISCV_ADD64`/`R_RISCV_SUB64`）。`R_RISCV_32_PCREL` 可用于某些 32 位重定位，但 GNU 汇编器只会为 `.eh_frame` 生成 `R_RISCV_32_PCREL`。（AVR 的 [`R_AVR_DIFF{8,16,32}` 重定位](https://sourceware.org/pipermail/binutils/2014-April/084624.html)与此类似。）

汇编器的行为没有很好的文档记录[https://github.com/riscv-non-isa/riscv-asm-manual/issues/80](https://github.com/riscv-non-isa/riscv-asm-manual/issues/80)。无论如何，我们来看一个示例。

```plaintext
.text
w:
.long extern - w   # extern remains undefined
.long w1 - w       # w1 is defined after parsing this expression
.long .L.str - w   # .L.str will be defined (in LLVM MC, .L.str is considered temporary while it isn't in GNU assembler)

w1:
```

`w1 - w` 可以被折叠为常量。`extern - w` 需要 ADD/SUB 重定位，而 `w1 - w` 可以被折叠为常量（LLVM 集成汇编器的行为）。然而，GNU 汇编器对 ADD/SUB 生成 `w1 - w` 重定位，因为 `gas/config/tc-riscv.c` 保守地定义 `TC_FORCE_RELOCATION_SUB_SAME(seg)` 以禁用代码节的折叠。

在 LLVM 17.0 之前，是否生成 LLVMADD/SUB 的决策在解析阶段就基于不充分的启发式规则提前做出（`requiresFixup`）。因此，较旧版本的 LLVM 集成汇编器会错误地抑制以下代码的 `R_RISCV_ADD32/R_RISCV_SUB32`：

```plaintext
# Both end and begin are not defined yet. We decide ADD/SUB relocations upfront and don't know they will be needed.
.4byte end-begin

begin:
  call foo
end:
```

Android[riscv64 mterp：修复 "oat" 代码大小计算。](https://android-review.googlesource.com/c/platform/art/+/2619609)是一个通过在一个符号定义在 `.4byte` 指令之前来解决此问题的实例。

我提交的 [[RISCV] 让链接器可松弛指令终止 MCDataFragment](https://reviews.llvm.org/D153097) 和 [[RISCV] 允许延迟决定 ADD/SUB 重定位](https://reviews.llvm.org/D155357) 修复了这个问题。对于汇编中的标签差值 `A-B`，如果 `A` 与 `B` 位于同一节，且二者之间没有对齐指令、汇编器可松弛指令或链接器可松弛指令，就可以把 `A-B` 折叠为常量。

来看一个示例，其中一条 assembler-relaxable 指令导致 `A-B` 不可折叠。
2  
3  
4  
.L1：
 .dword .L2-.L1 # R_RISCV_ADD32/R_RISCV_SUB32  
 beq s1, s1, .L1
.L2:

因此，对于 DWARF 中接下来的 32 位标签差值 DWARF，通常会在 `R_RISCV_ADD32`/`R_RISCV_SUB32` 模式下存在一对 `-mrelax`。
2  
3  
.section .debug_info,"",@progbits
...  
.word .Lfunc_end0-.Lfunc_begin0

GNU 汇编器通常会在更多情况下生成 `R_RISCV_ADD32`/`R_RISCV_SUB32` 对。它甚至会在使用 `R_RISCV_ADD32`/`R_RISCV_SUB32` 时，为 `.word .Lfunc_end0-.Lfunc_begin0` 生成一对 `-mno-relax`.

TODOgas 注释
2  
3  
4  
5  
6  
read.c:emit_expr_with_reloc
write.c:2322 resolve_symbol_value
write.c:2339 adjust_reloc_syms
write.c:2348 bfd_map_over_sections (stdoutput, fix_segment, (char *) 0);  
 config/tc-riscv.c:4156 If we are deleting this reloc entry, we must fill in the  
write.c:2505 bfd_map_over_sections (stdoutput, write_relocs, (char *) 0);

## DWARF

DWARF 是一种广泛使用的调试信息格式。

### 代码地址

在 DWARF 中，描述具有机器代码地址范围之实体的调试信息条目（DIE），可以使用 `DW_AT_low_pc/DW_AT_high_pc/DW_AT_ranges` 属性描述这些地址。
在其他架构上，典型实现会以这种方式使用汇编指令，并需要一个引用函数起始位置的重定位。


```plaintext
.quad   .Lfunc_begin0              # DW_AT_low_pc
.long   .Lfunc_end0-.Lfunc_begin0  # DW_AT_high_pc
```

由于链接器松弛，长度不是常量，因此标签差值实际上会产生两个重定位，即一对 `R_RISCV_ADD32` 和 `R_RISCV_SUB32`。所以 RISC-V 给了我们两个重定位，它们在目标文件中占用一些空间。RISC-V

```text
0x0000002a:   DW_TAG_subprogram [2]
                DW_AT_low_pc [DW_FORM_addr]     (0x0000000000000002 ".text")
                  # R_RISCV_64
                DW_AT_high_pc [DW_FORM_data4]   (0x00000040)
                  # Constant on other architectures
                  # Two relocations: R_RISCV_ADD32 and R_RISCV_SUB32
                  # Neither GCC nor Clang uses DW_FORM_addr (DWARF v3)
                DW_AT_frame_base [DW_FORM_exprloc]      (DW_OP_reg8 X8)
                DW_AT_name [DW_FORM_strp]       ( .debug_str[0x00000020] = "foo")
                DW_AT_decl_file [DW_FORM_data1] ("/tmp/c/a.c")
                DW_AT_decl_line [DW_FORM_data1] (2)
                DW_AT_external [DW_FORM_flag_present]   (true)
```

另一种设计是让 `DW_AT_high_pc` 属性的值为地址类，具体来说是 `DW_FORM_addr`。它在 ELFCLASS64 上占用 8 个字节，但可以去掉一个重定位。ELFCLASS64

```plaintext
.quad   .Lfunc_begin0              # DW_AT_low_pc
.quad   .Lfunc_end0                # DW_AT_high_pc
```

### 行号信息

行号信息提供从源代码文件位置到机器指令地址的关联。它从概念上讲是一个矩阵，每行对应一条指令。该矩阵有以下列：

- 源代码文件名
- 源代码行号
- 源代码列号
- 等等

DWARF 使用一种字节编码（byte-coded）语言来编码该矩阵。规范说明：byte-coded 语言来编码该矩阵。规范说：

> 行号程序中的大多数指令都是特殊操作码。

对于上述例子（连续的 `ext()` 调用），在大多数架构上，一次调用占用一个特殊操作码的一个字节。`llvm-dwarfdump --debug-line` 可以转储该矩阵：

```plaintext
# x86-64
            Address            Line   Column File   ISA Flags
            ------------------ ------ ------ ------ --- -------------
0x00000025: 00 DW_LNE_set_address (0x0000000000000000)
0x00000030: 13 address += 0,  line += 1
            0x0000000000000000      2      0      1   0  is_stmt
0x00000031: 05 DW_LNS_set_column (3)
0x00000033: 0a DW_LNS_set_prologue_end
0x00000034: 4b address += 4,  line += 1
            0x0000000000000004      3      3      1   0  is_stmt prologue_end
0x00000035: 75 address += 7,  line += 1
            0x000000000000000b      4      3      1   0  is_stmt
0x00000036: 75 address += 7,  line += 1
            0x0000000000000012      5      3      1   0  is_stmt
0x00000037: 75 address += 7,  line += 1
            0x0000000000000019      6      3      1   0  is_stmt
0x00000038: 75 address += 7,  line += 1
            0x0000000000000020      7      3      1   0  is_stmt
0x00000039: 75 address += 7,  line += 1
            0x0000000000000027      8      3      1   0  is_stmt
```

然而，在 RISC-V 上，一行会附带两个重定位，显得臃肿不堪！RISC-V`DW_LNS_advance_line+DW_LNS_fixed_advance_pc+DW_LNS_copy` 占用 6 个字节。两个 `Elf64_Rela` 重定位占用 48 个字节。

```plaintext
# RISC-V
            Address            Line   Column File   ISA Flags
            ------------------ ------ ------ ------ --- -------------
0x00000025: 00 DW_LNE_set_address (0x0000000000000002)
0x00000030: 13 address += 0,  line += 1
            0x0000000000000002      2      0      1   0  is_stmt
0x00000031: 05 DW_LNS_set_column (3)
0x00000033: 0a DW_LNS_set_prologue_end
0x00000034: 03 DW_LNS_advance_line (3)
0x00000036: 09 DW_LNS_fixed_advance_pc (0x0002)
0x00000039: 01 DW_LNS_copy
            0x0000000000000004      3      3      1   0  is_stmt prologue_end
0x0000003a: 03 DW_LNS_advance_line (4)
0x0000003c: 09 DW_LNS_fixed_advance_pc (0x000e)
0x0000003f: 01 DW_LNS_copy
            0x0000000000000012      4      3      1   0  is_stmt
0x00000040: 03 DW_LNS_advance_line (5)
0x00000042: 09 DW_LNS_fixed_advance_pc (0x0008)
0x00000045: 01 DW_LNS_copy
            0x000000000000001a      5      3      1   0  is_stmt
...

Relocation section ''.rela.debug_line' at offset 0x7e0 contains 17 entries:
    Offset             Info             Type      Symbol's Value  Symbol's Name + Addend
0000000000000028  0000000400000002 R_RISCV_64    0000000000000002 <null> + 0
0000000000000037  0000000600000022 R_RISCV_ADD16 0000000000000004 <null> + 0
0000000000000037  0000000400000026 R_RISCV_SUB16 0000000000000002 <null> + 0
000000000000003d  0000000a00000022 R_RISCV_ADD16 0000000000000012 <null> + 0
000000000000003d  0000000600000026 R_RISCV_SUB16 0000000000000004 <null> + 0
0000000000000043  0000000b00000022 R_RISCV_ADD16 000000000000001a <null> + 0
0000000000000043  0000000a00000026 R_RISCV_SUB16 0000000000000012 <null> + 0
...
```

54 倍的浪费！那么，问题出在哪里？

嗯，由于链接器松弛，两次调用之间的地址增量不是编译期常量。一个特殊操作码用以下公式编码：compile-time

```text
# DWARF v4 introduced maximum_operations_per_instruction for VLIW architectures.
# maximum_operations_per_instruction is 1 and operation_increment is address_advance on non-VLIW architectures.
opcode = line_increment - line_base + (line_range * operation_increment) + opcode_base
```

除 operation_increment 以外的变量都是编译期常量，但我们没有表示乘法的重定位类型。如果存在这样的重定位类型，并且编译器能确保最大 compile-time`address_advance` 不会导致 ubyte`opcode` 溢出（这并不简单），我们就可以使链接后的输出更小。也就是说，重定位仍然是目标文件的主要开销。

在几种主要二进制格式中，Mach-O 重定位为 8 字节，PE-COFF 为 10 字节，而 ELF 的 `Elf64_Rela` 为 24 字节，开销十分显著。我不知道 RISC-V 社区未来是否愿意让 64 位 RISC-V 改用 ELFCLASS32。目前 Linux 内核把 ELFCLASS32 与 ILP32 ABI 变体关联起来，但并没有什么能阻止小代码模型的目标文件使用 ELFCLASS32。

#### 生成的汇编文件的行号信息

GNU 汇编器和 LLVM 集成汇编器都会为含有 `.file` 和 `.loc` 指令的汇编文件创建 `.debug_line` 节。对不含这些指令的汇编文件指定 `-g` 时，则会合成包括行号信息在内的调试信息。

不过，LLVM 集成汇编器存在一个缺陷：无论 `.loc` 指令是显式提供还是合成生成，`.debug_line` 与 `-mrelax` 结合使用都会出问题。原因是 `MCDwarfLineTable::emitOne` 会调用 `MCObjectStreamer::emitDwarfAdvanceLineAddr`，为一个节生成行表操作码。

对于汇编文件，`createRISCVELFStreamer` 用于创建一个带有 `MCAssembler` 对象的 `MCObjectStreamer` 实例。对于 C/C++ 文件，`createRISCVObjectTargetStreamer` 用于创建一个不带 `MCAssembler` 对象的 `MCObjectStreamer` 实例。

使用 `MCAssembler` 对象时，行号信息中的标签差值会被错误地视为可以折叠。LLVM 集成汇编器会生成将指令偏移硬编码进去的特殊操作码；一旦链接器松弛改变了指令偏移，这些操作码就可能出错。

```sh
#!/bin/sh -e
cat > x.c <<eof
void f();
void _start() {
  f();
  f();
  f();
}
eof
# C to object file: correct DW_LNS_fixed_advance_pc
clang --target=riscv64 -g -c x.c
llvm-dwarfdump --debug-line -v x.o | grep \ DW_LNS_fixed_advance_pc

# Assembly to object file with synthesized line number information: incorrect special opcodes
clang --target=riscv64 -S x.c && clang --target=riscv64 -g -c x.s
llvm-dwarfdump --debug-line -v x.o | grep \ DW_LNS_fixed_advance_pc; test $? -eq 1

# Assembly with .loc to object file: incorrect special opcodes
clang --target=riscv64 -S -g x.c && clang --target=riscv64 -c x.s
llvm-dwarfdump --debug-line -v x.o | grep \ DW_LNS_fixed_advance_pc; test $? -eq 1
```

项目构建通常不会对同一个源文件先使用 `-S` 再使用 `-c`，但 `clang --target=riscv64 -g -c x.s` 相当常见。我建议目前先去掉 `-g`，反正合成的调试信息本身也没有多大用处。

我已经为 Clang 17.0 [修复了这个问题](https://reviews.llvm.org/D150004)。

### 调用帧信息

调用帧信息（`.debug_frame/.eh_frame`）中的帧描述条目（FDE）会编码实体的长度，因此需要一对重定位。

与行号信息类似，调用帧指令也使用字节码语言编码。`DW_CFA_advance_loc` 指令带有一个 6 位操作数（与操作码一起编码），表示位置增量为 `operand * code_alignment_factor`。可以用一对 `R_RISCV_SET6` 和 `R_RISCV_SUB6` 对该指令进行重定位。

### 拆分 DWARF

`-gsplit-dwarf` 会生成一个不由链接器处理的 `.dwo` 文件。如果 `.dwo` 文件含有重定位，这些重定位就无法解析。因此惯例是让 `.dwo` 文件不包含重定位。

目前 Clang 和 GCC 使用 `DW_AT_high_pc` 或 `DW_AT_ranges` 描述地址范围，其中的范围大小或端点通过重定位表示。这类实现与链接器松弛不兼容。为了配合链接器松弛，`DW_AT_high_pc` 和 `DW_AT_ranges` 需要使用 `.debug_addr` 中的索引（例如 `DW_RLE_startx_endx`）。

[https://github.com/llvm/llvm-project/issues/56642](https://github.com/llvm/llvm-project/issues/56642)

### 范围列表与位置列表

很长一段时间里，由于不支持 `.uleb128` 标签差值，无法使用紧凑的 `DW_LLE_offset_pair` 描述。GCC 使用 `DW_LLE_startx_endx` 描述（[PR99090](https://gcc.gnu.org/bugzilla/show_bug.cgi?id=99090)），其操作数是 `.debug_addr` 节中的索引。`.debug_addr` 中的两个值通过 `R_RISCV_64` 重定位。

2023 年定义了 `R_RISCV_SET_ULEB128` 和 `R_RISCV_SUB_ULEB128` 两种重定位。对于涉及可松弛文本节的 `.uleb128` 标签差值，GNU 汇编器会[生成一对 `R_RISCV_SET_ULEB128` 和 `R_RISCV_SUB_ULEB128`](https://sourceware.org/git/?p=binutils-gdb.git;a=commit;h=f1cd8b94e7c941c2a9107c1112ab2339916b8efd)。当时存在一个缺陷，可能让 `R_RISCV_SUB_ULEB128` 重定位[得到错误的非零加数](https://sourceware.org/bugzilla/show_bug.cgi?id=31179)。修复时还为 GNU ld 增加了 `--check-uleb128` 选项，用于检查这类缺陷。

我为 [LLVM 集成汇编器实现了 `R_RISCV_SET_ULEB128`/`R_RISCV_SUB_ULEB128` 的汇编器支持](https://reviews.llvm.org/D157657)，并为 lld [实现了对不带 `SHF_ALLOC` 标志之节的支持](https://github.com/llvm/llvm-project/pull/72610)。

## 语言特定数据区

在 Itanium C++ ABI 中，处理异常所需的信息称为语言特定数据区（LSDA）。在 ELF 目标上，它通常存放在 `.gcc_except_table` 节中。详见 [C++ 异常处理 ABI](https://maskray.me/blog/2020-12-12-c++-exception-handling-abi)。

```cpp
int comdat() {
  try { throw 1; }
  catch (int) { return 1; }
  return 0;
}
```

调用点记录描述了着陆垫的偏移/长度。在没有链接器松弛的情况下，这些值是汇编时常量，实际上 `.gcc_except_table` 没有引用文本段的重定位。

```plaintext
  .section .gcc_except_table,"a",@progbits
  .p2align 2
GCC_except_table0:
.Lexception0:
  .byte    255                         # @LPStart Encoding = omit
  .byte    3                           # @TType Encoding = udata4
  .uleb128 .Lttbase0-.Lttbaseref0
.Lttbaseref0:
  .byte    1                           # Call site Encoding = uleb128
  .uleb128 .Lcst_end0-.Lcst_begin0
.Lcst_begin0:
  .uleb128 .Lfunc_begin0-.Lfunc_begin0 # >> Call Site 1 <<
  .uleb128 .Ltmp0-.Lfunc_begin0        #   Call between .Lfunc_begin0 and .Ltmp0
  .byte    0                           #     has no landing pad
  .byte    0                           #   On action: cleanup
  .uleb128 .Ltmp0-.Lfunc_begin0        # >> Call Site 2 <<
  .uleb128 .Ltmp1-.Ltmp0               #   Call between .Ltmp0 and .Ltmp1
  .uleb128 .Ltmp2-.Lfunc_begin0        #     jumps to .Ltmp2
  .byte    1                           #   On action: 1
  .uleb128 .Ltmp1-.Lfunc_begin0        # >> Call Site 3 <<
  .uleb128 .Lfunc_end0-.Ltmp1          #   Call between .Ltmp1 and .Lfunc_end0
  .byte    0                           #     has no landing pad
  .byte    0                           #   On action: cleanup
.Lcst_end0:
  .byte    1                           # >> Action Record 1 <<
                                       #   Catch TypeInfo 1
  .byte   0                            #   No further actions
  .p2align 2
                                       # >> Catch TypeInfos <<
  .long _ZTIi                          # TypeInfo 1
.Lttbase0:
```

启用链接器松弛后，一般需要用一对重定位（[R_RISCV_SET_ULEB128 和 R_RISCV_SUB_ULEB128](https://github.com/riscv-non-isa/riscv-elf-psabi-doc/commit/96d6e190e9fc04a8517f9ff7fb9aed3e9876cbd6)）表示标签差值。

较旧的 GCC 和 Clang 使用 `DW_EH_PE_udata4`（`.word`）编码调用点记录。1  
2  
3  
4  
5  
6  
7  
8  
9  
10  
11  
12  
13  
14  
15  
16  
17  
18  
19  
20  
21  
22  
23  
24  
25  
26  
 except_table,"a",@progbits_
 .p2align 2
GCC_except_table1:
.Lexception0:
 .byte 255 # @LPStart Encoding = omit
 .byte 155 # @TType Encoding = indirect pcrel sdata4
 .uleb128 .Lttbase0-.Lttbaseref0  
.Lttbaseref0:
 .byte 3 # Call site Encoding = udata4
 .uleb128 .Lcst_end0-.Lcst_begin0  
.Lcst_begin0:
 .word .Lfunc_begin1-.Lfunc_begin1 # \>\>调用点 1\<\<  
 .word .Ltmp2-.Lfunc_begin1 # 在 .Lfunc_begin1 与 .Ltmp2 之间调用
 .word 0 # 没有着陆垫
 .byte 0 # 操作：清理
 .word .Ltmp2-.Lfunc_begin1 # \>\>调用点 2\<\<  
 .word .Ltmp3-.Ltmp2 # 在 .Ltmp2 与 .Ltmp3 之间调用
 .word .Ltmp4-.Lfunc_begin1 # 跳转到 .Ltmp4
 .byte 1 # 操作：1
 .word .Ltmp3-.Lfunc_begin1 # \>\>调用点 3\<\<  
 .word .Lfunc_end1-.Ltmp3 # 在 .Ltmp3 与 .Lfunc_end1 之间调用
 .word 0 # 没有着陆垫
 .byte 0 # 操作：清理
.Lcst_end0:
 .byte 1 # \>\>操作记录 1\<\<  
 ...

另一个问题是，从 `.gcc_except_table` 到文本段的重定位可能会导致一些链接器垃圾回收困难。这需要分段的 `.gcc_except_table` 段。详情请参见[C++ 异常处理 ABI](https://maskray.me/blog/2020-12-12-c++-exception-handling-abi)。

头部中的调用点表长度字段使用 uleb128 编码。更有趣的是，该值以及其他 uleb128 偏移量/长度可能会导致振荡，并需要在汇编器中进行迭代。请参见 GNUas ([PR4029](https://sourceware.org/bugzilla/show_bug.cgi?id=4029)).

## `ld --emit-relocs`

在存在链接器松弛的情况下，需要做相当多的工作来保持 `--emit-relocs` 输出的更新。与收缩指令相关的重定位可能看起来很奇怪，一些重定位可能会感觉位置不对。

对于 GNUld 的 AArch64 和 x86-64 端口，`--emit-relocs` 代码即使在应用了链接器优化后仍保留原始重定位类型。这在一定程度上是为了向用户传达更多信息，部分原因是该转换可能无法用任何现有的重定位类型来描述。ppc64 端口会转换某些重定位类型。

```sh
cat > aarch64.s <<'eof'
.global _start; _start:
  adrp    x1, :got:x
  ldr     x1, [x1, #:got_lo12:x]
.data; .globl x; .hidden x; x: .word 0
eof
cat > ppc64.s <<'eof'
.globl _start; _start:
  addis 3, 2, .Lhidden@toc@ha // R_PPC64_TOC16_HA(.toc) => R_PPC64_TOC16_HA(hidden)
  ld    3, .Lhidden@toc@l(3)  // R_PPC64_TOC16_LO_DS(.toc) => R_PPC64_TOC16_LO(hidden)
  lwa   3, 0(3)
.data; .globl hidden; .hidden hidden; hidden: .long 0
.section .toc,"aw",@progbits
.Lhidden: .tc hidden[TC], hidden
eof
cat > x86-64.s <<'eof'
.globl _start; _start:
  movq foo@gotpcrel(%rip), %rax
foo: nop
eof

aarch64-linux-gnu-gcc -fuse-ld=lld -B/tmp/Rel/bin -nostdlib aarch64.s -Wl,--emit-relocs -o aarch64 && aarch64-linux-gnu-objdump -dr aarch64
powerpc64le-linux-gnu-gcc -nostdlib ppc64.s -Wl,--emit-relocs -o ppc64 && powerpc64le-linux-gnu-objdump -dr ppc64
gcc -nostdlib x86-64.s -Wl,--emit-relocs -o x86-64 && objdump -dr x86-64
```

```sh
cat > riscv64.s <<'eof'
.global _start; _start:
  call f@plt
  call f@plt
  .balign 8
f: ret
eof

riscv64-linux-gnu-gcc -nostdlib riscv64.s -Wl,--emit-relocs -o riscv64
```

不过，RISC-V 端口会修改重定位类型，包括可松弛指令的重定位类型（e.g. `R_RISCV_CALL_PLT`）和标记（`R_RISCV_ALIGN` 和 `R_RISCV_RELAX`). `R_RISCV_CALL_PLT` 被修改为 `R_RISCV_JAL`，它可以描述松弛后的指令。`R_RISCV_ALIGN` 和 `R_RISCV_RELAX` 多少会被修改为 `R_RISCV_NONE`，从而丢失了原始信息。

我认为这种行为并非有意为之，因为在 `--emit-relocs` 中根本没有 `ld/testsuite/ld-riscv-elf/` 测试。到目前为止，这种无意的改动似乎还可以，但某些松弛（例如 TLSDESC）可能没有与松弛指令相关联的重定位类型。

```plaintext
Disassembly of section .text:

00000000000002a0 <_start>:
 2a0:   008000ef                jal     2a8 <f>
                        2a0: R_RISCV_JAL        f
 2a4:   004000ef                jal     2a8 <f>
                        2a4: R_RISCV_NONE       *ABS*+0x4
                        2a4: R_RISCV_JAL        f

00000000000002a8 <f>:
 2a8:   8082                    ret
                        2a8: R_RISCV_NONE       *ABS*+0x4
                        2a8: R_RISCV_NONE       *ABS*+0x6
```

我非常担心 RISC-V `--emit-relocs` 得到更多使用。我认为应该先理清预期的行为。

[https://sourceware.org/bugzilla/show_bug.cgi?id=30844](https://sourceware.org/bugzilla/show_bug.cgi?id=30844)

## 链接器的实现

GNU ld 执行以下步骤：1  
2  
3  
4  
5  
6  
7  
8  
9  
10  
11  
12  
13  
lang_check_relocs ();  
  
ldemul_after_allocation ();  
 ldelf_map_segments  
 lang_relax_sections  
 lang_size_sections (&relax_again, false);  
 bfd_relax_section  
 _bfd_riscv_relax_delete  
 _bfd_riscv_relax_align  
  
ldwrite ();  
 bfd_final_link  
 riscv_elf_relocate_section

有关[RISC-V 中的 RISC-V 链接器松弛](https://maskray.me/blog/2022-07-10-riscv-linker-relaxation-in-lld)，请参阅 ld.lld 的实现。

## 链接时优化或后 link-time 链接时 link-time 优化是否有帮助？

几乎没有。这是一个阶段排序问题。IR 级别（以及未来的机器 IR 级别）的 link-time 链接时优化在非常早的阶段执行，就在符号解析之后。它必须提前完成，因为后面的步骤需要访问它发出的输入段。LTO 库没有布局信息来指导其分支指令的选择。例如，对于从 .data 到 .text 的引用，LTO 库不知道距离有多远。

## 松弛振荡

- 两个前向调用场景：[https://github.com/llvm/llvm-project/pull/142899](https://github.com/llvm/llvm-project/pull/142899)。解决方案在几次迭代后阻止字节移除。
- 三个前向调用场景：[https://github.com/llvm/llvm-project/pull/73624](https://github.com/llvm/llvm-project/pull/73624)。尽管该场景是可行的，但该测试突出了重叠的段。

## 结语

我有时将链接器松弛称为具有良好人体工学的穷人的 link-time 链接时优化。我承认它有用，可能对嵌入式系统更有用，但似乎会带来巨大的可重定位目标文件大小成本。某些工具链组件具有很高的复杂性，但现在它们大多已经稳定下来了。

LoongArch 社区似乎很热心，想要添加链接器松弛（https://github.com/loongson/LoongArch-Documentation/pull/77）。我已在 GitHub PR 以及[https://sourceware.org/pipermail/binutils/2022-December/125322.html](https://sourceware.org/pipermail/binutils/2022-December/125322.html)上表达了我的担忧，即在没有解决所有问题之前添加支持。
