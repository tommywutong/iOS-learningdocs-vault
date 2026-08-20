---
title: AArch32 链接器笔记
source: MaskRay (宋方睿)
source_key: maskray
source_url: 'https://maskray.me/blog/2023-04-23-linker-notes-on-aarch32'
original_language: en
published: 2023-04-23
status: active
license: 未声明 → 仅私有归档
archived_at: 2026-07-27
content_hash: 'sha256:3b3cd5fac93af45c'
translated: true
---

> 原文：[Linker notes on AArch32](https://maskray.me/blog/2023-04-23-linker-notes-on-aarch32)　·　MaskRay (宋方睿)

[2023-04-23](https://maskray.me/blog/2023-04-23-linker-notes-on-aarch32)

# AArch32 链接器笔记

施工中

本文介绍 ELF 链接器中 AArch32 的特有细节。我已在[上一篇文章](https://maskray.me/blog/2023-03-05-linker-notes-on-aarch64)中介绍了 AArch64。

AArch32 是 Arm 架构的 32 位执行状态，运行 A32 和 T32 指令集。A32 指旧的固定宽度 32 位 ISA，而 T32 指混合 16 位和 32 位的 Thumb2 指令。

"AArch32"、"A32" 和 "T32" 是新名称。许多项目使用 "ARM"、"Arm" 或 "arm" 作为其移植名称。

## ABI 文档

- [ELF for the Arm® Architecture](https://github.com/ARM-software/abi-aa/blob/main/aaelf32/aaelf32.rst)
- [Procedure Call Standard for the Arm® Architecture](https://github.com/ARM-software/abi-aa/blob/main/aapcs32/aapcs32.rst)
- [C++ ABI for the Arm® Architecture](https://github.com/ARM-software/abi-aa/blob/main/cppabi32/cppabi32.rst)
- [Exception Handling ABI for the Arm® Architecture](https://github.com/ARM-software/abi-aa/blob/main/ehabi32/ehabi32.rst)

## 全局偏移表（Global Offset Table）

全局偏移表由两个节组成：

- `.got.plt` 存放 PLT 的代码地址。
- `.got` 存放其他地址和偏移量。

符号 `_GLOBAL_OFFSET_TABLE_` 定义在 `.got` 节的开头。GNU ld 为 `.got` 保留了一个条目，`.got[0]` 存放 `_DYNAMIC` 的链接时地址，这是出于历史原因：2.35 之前的 glibc 版本有 `_DYNAMIC` 的要求。参见[关于全局偏移表的一切](https://maskray.me/blog/2021-08-29-all-about-global-offset-table#global_offset_table_0)。

## 程序链接表（Procedure Linkage Table）

PLT 头部如下所示：

```plaintext
L1: str lr, [sp, #-4]!
    add lr, pc,  #0x0NN00000 &(.got.plt - L1 - 4)
    add lr, lr,  #0x000NN000 &(.got.plt - L1 - 4)
    ldr pc, [lr, #0x00000NNN] &(.got.plt -L1 - 4)
```

如果 `.git.plt-.plt-4` 超过 +-128MiB 范围，则需要长格式的 PLT 头部。

在 binutils 中，`bfd/elf32-arm.c:elf32_thumb2_plt_entry` 为 Thumb2 支持一种 PLT 方案（[https://sourceware.org/PR16017](https://sourceware.org/PR16017)）。对于仅支持 Thumb 指令的无 MMU 微控制器处理器，由于不支持 System V 风格的动态链接，其使用场景尚不明确。此时需要使用 FDPIC。

## Cortex-M 安全扩展

### `--cmse-implib`

此选项用于链接器对 [Cortex-M 安全扩展（CMSE）](https://arm-software.github.io/acle/cmse/cmse.html)的支持。它完成两项工作：

- 合成安全网关（secure gateway）veneer
- 在指定 `--out-implib=` 时写入 CMSE 导入库

如果存在非局部符号 `__acle_se_$sym`，而 `$sym` 未定义，则报告错误。否则 `$sym` 被视为安全网关 veneer。`__acle_se_$sym` 和 `$sym` 都必须是非绝对函数，且 `st_value` 为奇数。

如果 `__acle_se_$sym` 和 `$sym` 的地址不相等，链接器认为存在内联安全网关，不执行特殊操作；否则，链接器在特殊节 `.gnu.sgstubs` 中按以下逻辑合成一个安全网关 veneer。

链接器在 `.gnu.sgstubs` 中分配一个输入节，并定义相对于该节的 `$sym`。在输出文件中，`$sym` 被移动到 `.gnu.sgstubs`，这是一个不同的文本节。  
1  
2  
3  
4  
5  
\<.gnu.sgstubs\>:  
 ...  
$sym:  
 sg  
 b.w __acle_se_$sym

如果指定了 `--in-implib` 且该库定义了 `$sym`（假设地址为 `$addr`），则在输出中 `$sym` 具有固定地址 `$addr`。否则，链接器分配一个地址（大于所有具有固定地址的已合成安全网关 veneer）。

### `--out-implib=out.lib`

与 `--cmse-implib` 一起使用。将 CMSE 导入库写入 `out.lib`。

`out.lib` 将有 3 个节：`.symtab, .strtab, .shstrtab`。对于每个已合成的安全网关 veneer，写入一个 `SHN_ABS` 符号，其地址为 `$addr`（如果由 `--in-implib` 库指定）或链接器分配的地址。（CMSE 导入库不包含文本节，因此定义的符号必须使用 `SHN_ABS`。）

## 线程本地存储（Thread Local Storage）

AArch32 使用 TLS Variant I 的一种变体：静态 TLS 块位于线程指针之上。线程指针指向线程控制块的末尾。

链接器不执行 TLS 优化。

默认使用传统的通用动态（general dynamic）和局部动态（local dynamic）TLS 模型。存在一个 [TLSDESC ABI](https://www.fsfla.org/~lxoliva/writeups/TLS/RFC-TLSDESC-ARM.txt)。

参见[关于线程本地存储的一切](https://maskray.me/blog/2021-02-14-all-about-thread-local-storage)。

## Thunk

分支指令无法到达的目标需要范围扩展 thunk。ARM 和 Thumb 状态切换也需要 thunk。

### v4, v4T

ARMv4T 引入了 16 位 Thumb 指令集。这些处理器不支持 BLX。ARM/Thumb 状态切换必须使用 BX 完成。

在 ARM 状态下，重定位类型 `R_ARM_PC24/R_ARM_PLT32/R_ARM_JUMP24/R_ARM_CALL` 可能需要范围扩展或状态切换。lld 16.0.0 已为 Thumb 添加了 thunk 支持。我们可以使用 ld.lld 和 Thumb 代码构建 Game Boy Advance 或 Nintendo DS rom。

```plaintext
// ARM 到 ARM，绝对寻址
ldr pc, [pc, #-4]
L1: .word S

// ARM 到 Thumb，绝对寻址
ldr r12, [pc] ; L1
bx r12
L1: .word S

// ARM 到 ARM，位置无关
ldr ip, [pc]
L1: add pc, pc, ip
.word S - (L1 + 8)

// ARM 到 Thumb，位置无关
ldr ip, [pc]
L1: add ip, pc, ip
bx ip
.word S - (L1 + 8)
```

`R_ARM_THM_CALL` 1  
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
27  
// Thumb 到 ARM，绝对寻址  
bx  
b #-6  
ldr pc, [pc, #-4]  
L1: .word S  
  
// Thumb 到 Thumb，绝对寻址  
bx  
b #-6  
ldr ip, [pc]  
bx ip  
L1: .word S  
  
// Thumb 到 ARM，位置无关  
bx  
b #-6  
ldr ip, [pc, #]  
L1: add ip, pc, ip  
L2: .word S - (L1 + 8)  
  
// Thumb 到 Thumb，位置无关  
bx  
b #-6  
ldr ip, [pc, #-4]  
L1: add ip, pc, ip  
bx ip  
L2: .word S - (L1 + 8)

### v5, v6, v6-K, v6-KZ

这些是支持 BLX 但不支持 Thumb 分支范围扩展或 MOVT/MOVW 的前 Cortex 处理器。

ARMv5 中没有支持 thunk 的 Thumb 分支指令。LDR 可以切换处理器状态。

```plaintext
// 绝对寻址（LDR 可以切换处理器状态）
ldr pc, [pc, #-4]
.word S

// 位置无关
ldr ip, [pc, #4]
L1: add ip, pc, ip
bx ip
.word S - (L1 + 8)
```

### v6-M

仅支持 Thumb 指令。这些处理器支持 BLX 和 J1 J2 编码（分支范围扩展），但不支持 MOVT/MOVW。

```plaintext
// 近程
b.w S

// 远程，绝对寻址
push {r0, r1}
ldr r0, [pc, #4]
str r0, [sp, #4]
pop {r0, pc}
.word S

// 远程，位置无关
push {r0}
ldr r0, [pc, #8]; L2
mov ip, r0
pop {r0}
L1: add pc, ip
nop
L2: .word S - (L1 + 4)
```

### v6T2, v7 (v7-A, v7-R, v7-M, v7E-M) 及更新版本

ARMv6T2 引入了 Thumb-2。这些处理器支持 BLX/MOVT/MOVW 和 Thumb 分支范围扩展。（除 v6-M 和 v6S-M 外，所有 Cortex 处理器中使用的架构都具备 MOVT/MOVW 指令。）

一对 MOVT/MOVT 指令可以生成：

- 一个 32 位立即数（例如绝对地址），使用 `R_ARM_MOVT_ABS`/`R_ARM_MOVW_ABS_NC` 重定位，
- 一个 PC 相对地址，使用 `R_ARM_MOVT_PREL`/`R_ARM_MOVW_PREL_NC` 重定位，
- 或一个静态基址相对地址，使用 `R_ARM_MOVT_BREL`/`R_ARM_MOVW_BREL_NC` 重定位。

在 ELF 中，`R_ARM_MOVT_PREL`/`R_ARM_MOVW_PREL_NC` 在生成局部符号地址时未被利用。[https://bugs.llvm.org/show_bug.cgi?id=28229](https://bugs.llvm.org/show_bug.cgi?id=28229) 然而，由于 `R_ARM_MOVT_BREL`/`R_ARM_MOVW_BREL_NC` 被 ROPI/RWPI 使用，这应该引起注意。

在 ARM 状态下，这些重定位类型 `R_ARM_PC24, R_ARM_PLT32, R_ARM_JUMP24, R_ARM_CALL` 可能需要 thunk 用于范围扩展或状态切换。

```plaintext
// 近程，且目标处于 ARM 状态
b S

// 绝对寻址
movw ip, :lower16:S
movt ip, :upper16:S
bx ip

// 位置无关
movw ip, :lower16:S-(L1+8)
movt ip, :upper16:S-(L1+8)
L1: add ip, ip, pc
bx ip
```

在 Thumb 状态下，这些重定位类型 `R_ARM_THM_JUMP19, R_ARM_THM_JUMP24, R_ARM_THM_CALL` 可能需要 thunk 用于范围扩展或状态切换。

```plaintext
// 近程，且目标处于 Thumb 状态
b.w S

// 绝对寻址
movw ip, :lower16:S
movt ip, :upper16:S
bx ip

// 位置无关
movw ip, :lower16:S-(L1+4)
movt ip, :upper16:S-(L1+4)
L1: add ip, ip, pc
bx ip
```

MOVT 提取一个值的高位，并在 ELF 和 Mach-O 格式中都需要特殊处理，因为它们都使用隐式加数（implicit addend）。在 ELF 中，它使用 REL 重定位格式。当汇编器处理 MOVT 修复时，会产生两种可能的结果（`ARMAsmBackend::adjustFixupValue`）：

- 已解析的修复：汇编器使用 `value >> 16` 更新相关位。
- 未解析的修复：汇编器基于原始值创建重定位。

## `--fix-cortex-a8`

此选项启用针对 Arm Cortex-A8 勘误 657417 的链接器变通方法。链接器会扫描跨两个 4KiB 页面的 4 字节 Thumb-2 分支指令（Bcc.w、B.w、BLX.w、BL.w），且分支的目标地址落在第一个区域内。分支指令后跟一条 4 字节非分支指令。这可能导致不正确的指令获取或处理器死锁。

一旦检测到勘误条件，链接器会尝试将其重写为替代的代码序列。有关详细信息，请参见实现中的注释。

## `SHT_ARM_ATTRIBUTES`

通常命名为 `.ARM.attributes`。

## `SHT_ARM_EXIDX` (`.ARM.exidx`) 和 `.ARM.extab`

参见[栈展开](https://maskray.me/blog/2020-11-08-stack-unwinding)

## `--be8`

在链接大端序映像时，存在已废弃的 BE-32 模式（字不变寻址大端序模式）和新的 BE-8 模式（字节不变寻址大端序模式）。

BE-32 用于较旧的架构，如 arm7tdmi 和 arm926ej-s。

对于 ARMv6-M、ARMv7 及更高版本架构，默认为 BE8。可重定位目标文件具有大端序代码和数据。编译器驱动程序将 `--be8` 传递给链接器，以将大端序代码转换为小端序。

链接器查找 `$a`/`$d`/`$t` 映射符号以定位 ARM 和 Thumb 代码并执行字节交换。ARM 代码按 4 字节单位反转，Thumb 代码按 2 字节单位反转，而数据保持不变。链接器在 ELF 头部设置 `EF_ARM_BE8` 标志。

```sh
cat > a.s <<e
.syntax unified
.cpu    arm1176jzf-s

.text
.globl _start
.type _start,%function
_start:
  bl thumbfunc
  bx lr
  .word   0x12345678

.thumb
.section .text.2, "ax", %progbits
.globl thumbfunc
.type thumbfunc,%function
thumbfunc:
  bx lr
e
clang --target=armeb-none-linux-gnueabi -c a.s
arm-linux-gnueabihf-ld -EB --be8 a.o -o a
```

`a.o` 和 `a` 的数据（`.word`）具有相同的字节序，但 `a` 的指令是小端序的。

```plaintext
% llvm-objdump -s -d -j .text -j .text.2 a.o

a.o:    file format elf32-bigarm
Contents of section .text:
 0000 ebfffffe e12fff1e 12345678           ...../...4Vx
Contents of section .text.2:
 0000 4770                                 Gp

Disassembly of section .text:

00000000 <_start>:
       0: ebfffffe      bl      0x0 <_start>            @ imm = #-0x8
       4: e12fff1e      bx      lr

00000008 <$d.1>:
       8: 12 34 56 78   .word   0x12345678

Disassembly of section .text.2:

00000000 <thumbfunc>:
       0: 4770          bx      lr
% llvm-objdump -s -d -j .text a

a:      file format elf32-bigarm
Contents of section .text:
 10058 020000eb 1eff2fe1 12345678 70470000  ....../..4VxpG..
 10068 00c09fe5 1cff2fe1 00010065 00000000  ....../....e....

Disassembly of section .text:

00010058 <_start>:
   10058: eb000002      bl      0x10068 <__thumbfunc_from_arm> @ imm = #0x8
   1005c: e12fff1e      bx      lr

00010060 <$d.1>:
   10060: 12 34 56 78   .word   0x12345678

00010064 <thumbfunc>:
   10064: 4770          bx      lr
   10066: 0000          movs    r0, r0

00010068 <__thumbfunc_from_arm>:
   10068: e59fc000      ldr     r12, [pc]               @ 0x10070 <__thumbfunc_from_arm+0x8>
   1006c: e12fff1c      bx      r12

00010070 <$d>:
   10070: 00 01 00 65   .word   0x00010065
   10074: 00 00 00 00   .word   0x00000000
% readelf -h a
...
 Flags:                             0x5800200, Version5 EABI, soft-float ABI, BE8
```

## 静态基址（Static base）

几种重定位类型编码了静态基址的相对偏移量，例如 `R_ARM_GOT_BREL`。

## FDPIC ABI

[https://github.com/mickael-guene/fdpic_doc/blob/master/abi.txt](https://github.com/mickael-guene/fdpic_doc/blob/master/abi.txt)
