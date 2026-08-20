---
title: 线程局部存储详解
source: MaskRay (宋方睿)
source_key: maskray
source_url: 'https://maskray.me/blog/2021-02-14-all-about-thread-local-storage'
original_language: en
published: 2021-02-14
status: active
license: 未声明 → 仅私有归档
archived_at: 2026-07-27
content_hash: 'sha256:77e6b8c1ef444515'
translated: true
---

> 原文：[All about thread-local storage](https://maskray.me/blog/2021-02-14-all-about-thread-local-storage)　·　MaskRay (宋方睿)

[2021-02-14](https://maskray.me/blog/2021-02-14-all-about-thread-local-storage)

# 线程局部存储详解

2026 年 1 月更新。

线程局部存储（TLS）提供一种为不同线程分配不同对象的机制。它通常用于实现 GCC 扩展 `__thread`、C11 的 `_Thread_local` 与 C++11 的 `thread_local`；这些特性允许使用声明的名称来引用当前线程关联的实体。本文将详细介绍 ELF 平台上的线程局部存储，并简要讨论线程专有数据键以及 Windows/macOS 的 TLS 等相关主题。

线程局部存储的一个用例是 POSIX 的 `errno`：

> 每个线程都有自己的线程 ID、调度优先级和策略、errno 值、浮点环境、线程专有键/值绑定，以及支持控制流所需的系统资源。

不同线程拥有不同的 `errno` 副本。`errno` 通常被定义为返回线程局部变量的函数（例如 `__errno_location`）。

对于每种架构，权威的 ELF ABI 文档是 System V ABI（通用 ABI）的处理器补充（psABI）。这些文档通常引用 Ulrich Drepper 的《_The ELF Handling for Thread-Local Storage_》。然而，该文档将通用规范与 glibc 内部实现混为一谈。

## 表示

### 汇编器行为

编译器通常将线程局部变量定义在 `.tdata` 和 `.tbss` 节中（它们带有节标志 `SHF_TLS`）。表示线程局部变量的符号类型为 `STT_TLS`（表示线程局部存储实体）。在 GNU as 语法中，可用 `.type a, @tls_object` 将 `a` 的类型设为 `STT_TLS`。TLS 符号的 `st_value` 是相对于定义节的偏移量。

```plaintext
.section .tbss,"awT",@nobits
.globl a, b
.type a, @tls_object
.type b, @tls_object
a:
  .zero 4
  .size a, .-a
b:
  .zero 4
  .size b, .-b
```

在此示例中，`st_value(a)=0`，而 `st_value(b)=4`。

在 Clang 和 GCC 生成的汇编中，线程局部变量会标注为 `.type a, @object`（`STT_OBJECT`）。当汇编器发现这类符号定义在 `SHF_TLS` 节中或被 TLS 重定位引用时，便会将 `STT_NOTYPE`/`STT_OBJECT` 升级为 `STT_TLS`。

GNU as 支持 `.tls_common` 指令，用来定义 `STT_TLS SHN_COMMON` 符号。这是个较少使用的特性；目前尚不清楚 GCC 是否仍有生成 `.tls_common` 指令的代码路径。LLVM 集成汇编器不支持 `.tls_common`。

### 链接器行为

链接器将 `.tdata` 输入段合并为一个 `.tdata` 输出段。`.tbss` 输入段被合并为一个 `.tbss` 输出段。这两个 `SHF_TLS` 输出段被放置到一个 `PT_TLS` 程序头中。

- `p_offset`：TLS 初始化映像的文件偏移量
- `p_vaddr`：TLS 初始化映像的虚拟地址
- `p_filesz`：TLS 初始化映像的大小
- `p_memsz`：线程局部存储的总大小；末尾 `p_memsz-p_filesz` 字节由动态加载器置零
- `p_align`：对齐

`PT_TLS` 程序头包含在 `PT_LOAD` 程序头中。如果使用了 `PT_GNU_RELRO`，那么 `PT_TLS` 包含在 `PT_GNU_RELRO` 中，而 `PT_GNU_RELRO` 包含在 `PT_LOAD` 中。从概念上讲，`PT_TLS` 和 `STT_TLS` 符号就像位于一个独立的地址空间中。动态链接器应将 `[p_vaddr,p_vaddr+p_filesz)` 的 TLS 初始化映像复制到相应的静态 TLS 块中。

在可执行文件和共享对象中，`st_value` 通常保存虚拟地址；对于 `STT_TLS` 符号，`st_value` 保存相对于 `PT_TLS` 程序头虚拟地址的偏移量。`PT_TLS` 的第一个字节由 `st_value==0` 的 TLS 符号引用。

GNU ld 将 `STT_TLS SHN_COMMON` 符号视为定义在 `.tcommon` 节中；其内部链接器脚本会把这些节放入输出节 `.tdata`。ld.lld 不支持 `STT_TLS SHN_COMMON` 符号。

### 动态链接器行为

动态加载器从主可执行文件和立即加载的共享对象（经由传递性 `DT_NEEDED`）收集 `PT_TLS` 程序头，并为每个 `PT_TLS` 分配一个静态 TLS 块。对于每个 `PT_TLS`，动态加载器将 TLS 初始化映像中的 `p_filesz` 字节复制到 TLS 块，并把末尾 `p_memsz-p_filesz` 字节置零。

对于主可执行文件的静态 TLS 块，模块 ID 为 1，TLS 符号的 TP 偏移量是链接时常量；链接器与动态加载器使用相同的公式。

对于程序启动时加载的共享对象，从线程指针到其静态 TLS 块的偏移量在启动时固定，尽管它不是链接时常量。初始执行 TLS 模型可通过 GOT 动态重定位引用这个偏移量。

_The ELF Handling for Thread-Local Storage_ 描述并规定了两种 TLS 变体的数据结构。不过，只有主可执行文件静态 TLS 块的 TP 偏移量是硬性要求。尽管如此，libc 实现通常会将静态 TLS 块放在一起，并为线程控制块和静态 TLS 块共同分配空间。

对于由 `pthread_create` 创建的新线程，静态 TLS 块通常作为线程栈的一部分分配。如果在栈的最大地址和线程控制块之间没有保护页，这可能会被认为存在安全风险，因为栈溢出可能会覆盖线程控制块。

## 模型

### Local exec TLS 模型（可执行文件和不可抢占）

这是最高效的 TLS 模型。它适用于 TLS 符号在可执行文件中定义的情况。

在 `-fno-pic/-fpie` 模式下，如果变量符合以下条件，编译器会选择此模型：

- 是一个定义
- 或者一个具有非默认可见性的声明。

第一个条件显而易见。第二个条件是因为非默认可见性意味着该变量必须由可执行文件中的另一个翻译单元定义。

```c
_Thread_local int def;
__attribute__((visibility("hidden"))) extern thread_local int ref;
int foo() { return def + ref; }
```

```plaintext
# x86-64
# The segment register %fs holds the thread pointer. The instruction loads an offset relative to the thread pointer.
movl %fs:def@TPOFF, %eax
```

对于主可执行文件的静态 TLS 块，TLS 符号的 TP 偏移量是链接时常量。以下是常见的重定位类型列表：

- arm：`R_ARM_TLS_LE32`
- aarch64：

    - `-mtls-size=12`: `R_AARCH64_TLSLE_ADD_TPREL_LO12`
    - [-65536,65536) (unavailable in GCC/Clang): `R_AARCH64_TLSLE_MOVW_TPREL_G0`
    - `-mtls-size=24` (default): `R_AARCH64_TLSLE_ADD_TPREL_HI12`, `R_AARCH64_TLSLE_ADD_TPREL_LO12_NC`
    - `-mtls-size=32`: `R_AARCH64_TLSLE_MOVW_TPREL_G1`, `R_AARCH64_TLSLE_MOVW_TPREL_G0_NC`
    - `-mtls-size=48`: `R_AARCH64_TLSLE_MOVW_TPREL_G2`, `R_AARCH64_TLSLE_MOVW_TPREL_G1_NC`, `R_AARCH64_TLSLE_MOVW_TPREL_G0_NC`
- i386：`R_386_TLS_LE`
- x86-64: `R_X86_64_TPOFF32`
- mips：`R_MIPS_TPREL_HI16`, `R_MIPS_TPREL_LO16`
- ppc32：`R_PPC_TPREL_HA`, `R_PPC_TPREL_LO`
- ppc64：`R_PPC64_TPREL_HA`, `R_PPC64_TPREL_LO`
- riscv：`R_RISCV_TPREL_HI20`, `R_RISCV_TPREL_LO12_I`, `R_RISCV_TPREL_LO12_S`

对于 RISC 架构而言，由于一条指令通常为 4 字节，无法编码 32 位偏移量，因此通常需要两条指令来具体化一个 TP 偏移量。

在 [https://reviews.llvm.org/D93331](https://reviews.llvm.org/D93331) 中，我修改 ld.lld，使它在 `-shared` 模式下拒绝 local-exec TLS 重定位。GNU ld 的 arm、riscv 和 x86 端口至少已有类似诊断，但 aarch64 和 ppc64 不会报错。

### 初始执行 TLS 模型（可执行文件与可抢占模块）

此模型的效率低于 local-exec。它适用于 TLS 符号定义在可执行文件或程序启动时已可用的共享对象中的情况；该共享对象可以由 `DT_NEEDED` 或 `LD_PRELOAD` 引入。

当变量是具有默认可见性的声明时，编译器会在 `-fno-pic/-fpie` 模式下选择此模型。其依据是：可执行文件引用的符号必须由立即加载的共享对象定义，而非由 `dlopen` 加载的共享对象定义。链接器也会强制这一点：对 `-no-pie/-pie` 链接默认启用 `-z defs`。

```c
extern thread_local int ref;
int foo() { return ref; }
```

```plaintext
# x86-64
movq ref@GOTTPOFF(%rip), %rax
movl %fs:(%rax), %eax
```

由于线程指针到静态块起始位置的偏移量在程序启动时是固定的，因此这样的偏移量可以通过 GOT 重定位来编码。此类重定位类型的名称中通常包含 `GOT` 和 `TPREL/TPOFF`。以下是常见的重定位类型列表：

- arm：`R_ARM_TLS_IE32`
- aarch64：`R_AARCH64_TLSIE_ADR_GOTTPREL_PAGE21`, `R_AARCH64_TLSIE_LD64_GOTTPREL_LO12_NC` (`adrp x0, :gottprel:tls; ldr x0, [x0, #:gottprel_lo12:tls]`)
- i386：`R_386_TLS_IE`
- x86-64: `R_X86_64_GOTTPOFF`
- ppc32：`R_PPC_GOT_TPREL16`
- ppc64：`R_PPC64_GOT_TPREL16_HA`, `R_PPC64_GOT_TPREL16_LO_DS`
- riscv：`R_RISCV_TLS_GOT_HI20`, `R_RISCV_PCREL_LO12_I`

如果 TLS 符号不满足 initial-exec 优化为 local-exec 的条件，链接器将分配一个 GOT 条目并生成一个动态重定位。以下是动态重定位类型列表：

- arm：`R_ARM_TLS_TPOFF32`
- aarch64：`R_AARCH64_TLS_TPREL64`
- mips32：`R_MIPS_TLS_TPREL32`
- mips64：`R_MIPS_TLS_TPREL64`
- i386：`R_386_TPOFF`
- x86-64: `R_X86_64_TPOFF64`
- ppc32：`R_PPC_TPREL32`
- ppc64：`R_PPC64_TPREL64`
- riscv：`R_RISCV_TLS_TPREL64`

虽然它们的名称中包含 `TPREL` 或 `TPOFF`，但这些动态重定位的位宽与字长相同。这是将它们与目标文件中使用的 local-exec 重定位类型区分开来的好方法。

如果添加 `__attribute((tls_model("initial-exec")))` 属性，线程局部变量就可以在 `-fpic` 模式下使用此模型。如果目标文件链接进可执行文件，一切正常；如果链接进共享对象，该共享对象通常必须在程序启动时立即加载。链接器会设置 `DF_STATIC_TLS` 标志，标记含有 initial-exec TLS 重定位的共享对象。

glibc 的 ld.so 会在静态 TLS 块中预留一些空间，因此只要共享对象的 TLS 较小，就允许通过 dlopen 加载它。使用这一属性的一个少见理由是：glibc 的 general-dynamic 和 local-dynamic TLS 模型不具备异步信号安全性。然而，其他 libc 实现不一定会为通过 dlopen 加载的 initial-exec 共享对象预留额外 TLS 空间，例如 musl 会直接报错。

### 通用动态和局部动态 TLS 模型（DSO）

这两种模型通常与 `-fpic/-fPIC` 一起使用，适用于 TLS 符号可能由共享对象定义的情况。它们不假定 TLS 符号由静态 TLS 块支持，而是假定模块的线程局部存储可以动态分配，因此适合 dlopen 场景。动态分配的 TLS 存储通常称为动态 TLS。

每个 TLS 符号都分配一个（模块 ID，从 dtv[m] 到该符号的偏移量）对，通常称为 `tls_index` 对象。模块 ID m 由动态加载器在加载模块（可执行文件或共享对象）时分配，因此链接时并不知道。dtv 表示动态线程向量。每个线程都有自己的动态线程向量，用于把模块 ID 映射到线程局部存储；dtv[m] 指向为模块 m 分配的存储。

在最简单的形式中，一旦我们有了指向（模块 ID，从 dtv[m] 到该符号的偏移量）对的指针，就可以通过以下 C 程序获取该符号的地址：

```c
// v is a pointer to the first element of the pair.
void *__tls_get_addr(size_t *v) {
  pthread_t self = __pthread_self();
  return (void *)(self->dtv[v[0]] + v[1]);
}
```

代码序列效率较低。如果生成的可重定位文件不会被链接到通过 dlopen 加载的共享对象中，可以考虑使用 `-ftls-model=initial-exec` 切换到 initial-exec TLS 模型。

#### 通用动态 TLS 模型（DSO）

通用动态 TLS 模型是最灵活的模型。它假定链接时既不知道模块 ID，也不知道从 dtv[m] 到符号的偏移量。当局部动态 TLS 模型不适用时，`-fpic` 模式会使用该模型。编译器生成代码，设置指向符号 TLSGD 条目的指针，然后安排调用 `__tls_get_addr`；返回值是当前线程中 TLS 符号的运行时地址。在 x86-64 上，leaq 指令带有一个 data16 前缀，而 call 指令带有两个 data16（0x66）前缀和一个 rex64 前缀。这是有意的设计，使 leaq+call 总长为 16 字节，便于链接时优化。

```plaintext
data16 leaq def@tlsgd(%rip), %rdi  # R_X86_64_TLSGD
# GNU as does not allow duplicate data16 prefixes, so .value is used here.
.value 0x6666
rex64 call __tls_get_addr@PLT
movl (%rax), %eax
```

（LLVM 反汇编器不显示 data16 和 rex64 前缀，这是一个尚未解决的问题。）

以下是一些常见的重定位类型。它们在《The ELF Handling for Thread-Local Storage》中称为“initial relocations”。

- arm：`R_ARM_TLS_GD32`
- aarch64：`R_AARCH64_TLSGD_ADR_PREL21`, `R_AARCH64_TLSGD_ADR_PAGE21`, `R_AARCH64_TLSGD_ADD_LO12_NC`, `R_AARCH64_TLSGD_MOVW_G1`, `R_AARCH64_TLSGD_MOVW_G0_NC`（很少使用，因为默认使用 TLS 描述符）
- i386：`R_386_TLS_GD`
- x86-64: `R_X86_64_TLSGD`
- mips：`R_MIPS_TLS_GD`, `R_MICROMIPS_TLS_GD`
- ppc32：`R_PPC_GOT_TLSGD16`
- ppc64：`R_PPC64_GOT_TLSGD16_HA`, `R_PPC64_GOT_TLSGD16_LO`
- riscv：`R_RISCV_TLS_GD_HI20`

当链接器扫描此类重定位时，会检查所引用的 TLS 符号是否满足优化要求。如果不满足，链接器就在 `.got` 节中分配两个连续的字（如果尚未分配）。这两个条目由两个动态重定位修正。动态加载器把模块 ID 写入第一个字，把从 dtv[m] 到符号的偏移量写入第二个字。动态重定位类型如下：

- arm：`R_ARM_TLS_DTPMOD32` 和 `R_ARM_TLS_DTPOFF32`
- aarch64：`R_AARCH64_TLS_DTPMOD` 和 `R_AARCH64_TLS_DTPREL`（很少使用，因为默认使用 TLS 描述符）
- x86-32: `R_386_TLS_DTPMOD32` 和 `R_386_TLS_DTPOFF32`
- x86-64: `R_X86_64_DTPMOD64` 和 `R_X86_64_DTPOFF64`
- mips32：`R_MIPS_TLS_DTPMOD32` 和 `R_MIPS_TLS_DTPOFF32`
- mips64：`R_MIPS_TLS_DTPMOD64` 和 `R_MIPS_TLS_DTPOFF64`
- ppc32：`R_PPC_DTPMOD32` 和 `R_X86_64_DTPREL32`
- ppc64：`R_PPC64_DTPMOD64` 和 `R_X86_64_DTPREL64`
- riscv32：`R_RISCV_TLS_DTPMOD32` 和 `R_X86_64_TLS_DTPREL32`
- riscv64：`R_RISCV_TLS_DTPMOD64` 和 `R_X86_64_TLS_DTPREL64`
- s390/s390x：`R_390_TLS_DTPMOD` 和 `R_390_TLS_DTPOFF`

它们在《The ELF Handling for Thread-Local Storage》中称为“outstanding relocations”。

在 x86-64 上，`-fno-plt` 使用 `call *__tls_get_addr@GOTPCREL(%rip)`，而非 `call __tls_get_addr`。若用 GNU ld 链接，则需要 [2016-06 的提交](https://sourceware.org/git/?p=binutils-gdb.git;a=commit;h=e2cbcd9156d1606a9f2153aecd93a89fe6e29180)。对于以 `-fpic -fno-plt -Wa,-mrelax-relocations=no` 编译的可重定位目标文件，不能使用 GNU ld（[该问题](https://sourceware.org/bugzilla/show_bug.cgi?id=24784) 被标为 wontfix）。

#### 局部动态 TLS 模型（DSO 且不可抢占）

局部动态 TLS 模型假定从 `dtv[m]` 到符号的偏移量是链接时常量；TLS 符号不可抢占时便是这种情况。编译器生成代码设置指向模块 TLSLD 条目的指针，随后调用 `__tls_get_addr`，再把链接时常量加到返回值上取得地址。

```c
static _Thread_local int def, def1;
int f0() { return ++def; }
int f1() { return ++def1 + def; }
```

若 `def` 使用局部动态 TLS 模型访问，其代码可能如下：1  
2  
3  
leaq def@tlsld(%rip), %rdi  
call __tls_get_addr@PLT  
movl def@dtpoff(%rax), %edx

我说“模块的 TLSLD 条目”，是因为在 x86-64 上，`def@tlsld` 虽然看起来像不可抢占 TLS 符号的 TLSLD 条目，实际上也可由其他不可抢占 TLS 符号共享。因此一个模块只需一个这类条目。从技术上讲，也可直接用通用动态重定位类型表示局部动态 TLS 模型；例如 GCC 的 RISC-V 就如此实现：

```plaintext
la.tls.gd a0, .LANCHOR0
call __tls_get_addr@@plt

.section .tbss,"awT",@nobits
.align 2
.set .LANCHOR0, .+0
.type a, @object
.size a, 4
a:
  .zero 4
```

这很巧妙。不过，我更偏好专用的局部动态重定位类型。若把多个可重定位文件链接在一起，局部符号 `.LANCHOR0` 彼此独立，GOT 条目无法共享；采用专用局部动态重定位类型的架构则可以共享 GOT 条目。

请注意，虽然代码序列不再包含 `data16` 和 `rex64` 前缀，但它并不比通用动态 TLS 模型更短。实际上，在 RISC 架构上，由于增加了 DTPREL，代码序列通常更长。若一个函数需要访问两个或更多不可抢占 TLS 符号，局部动态模型可共享 `__tls_get_addr` 调用。

```plaintext
leaq def0@tlsld(%rip), %rdi
call __tls_get_addr@PLT
movl def0@dtpoff(%rax), %edx
movl def1@dtpoff(%rax), %eax
```

以下是常用的重定位类型列表。

- arm：`R_ARM_TLS_LDM32`
- i386：`R_386_TLS_LDM`
- x86-64: `R_X86_64_TLSLD`
- mips：`R_MIPS_TLS_LDM`, `R_MICROMIPS_TLS_LDM`
- ppc32：`R_PPC_GOT_TLSLD16`
- ppc64：`R_PPC64_GOT_TLSLD16_HA`, `R_PPC64_GOT_TLSLD16_LO`, `R_PPC64_GOT_TLSLD_PCREL34`

在链接阶段，如果 TLS 符号不满足从 local-dynamic 到 local-exec 优化要求，链接器将会在 `.got` 段中为 TLSLD 重定位分配两个连续的字。动态加载器会将模块 ID 写入第一个字，并将从 dtv[m] 到该符号的偏移量写入第二个字。

如果架构未定义 TLS 优化，链接器仍然可以进行一项优化：在 `-no-pie/-pie` 模式下，将第一个字设置为 1（主可执行文件），并省略模块 ID 的动态重定位。

### TLS 描述符

一些架构（arm、aarch64、i386、x86-64）采用 TLS 描述符，作为传统通用动态和局部动态 TLS 模型更高效的替代方案。这类 ABI 将“模块 ID、从 `dtv[m]` 到符号的偏移量”这一对值的第一个字复用为函数指针：静态 TLS 时指向极简单的函数，动态 TLS 时指向类似 `__tls_get_addr` 的函数。调用方改为执行间接函数调用，而非直接调用 `__tls_get_addr`。主要有两点：

- 对 `__tls_get_addr` 的函数调用使用常规调用约定：编译器必须保守地假定所有易失性寄存器都可能被 `__tls_get_addr` 改写。
- 在 glibc（它执行惰性 TLS 分配）中，`__tls_get_addr` 非常复杂。若模块的 TLS 由静态 TLS 块支持，动态加载器只需将 TP 偏移量放入第二个字，并让函数指针指向一个直接返回第二个字的函数。

TLS 描述符通常更高效，主要就是因为第一点。也可以说，传统的通用动态和局部动态 TLS 模型同样可以设计一种机制，为 `__tls_get_addr` 使用自定义调用约定。

对于下列程序，使用 TLS 描述符（`-fpic -mtls-dialect=desc`；arm 和 x86 使用 `gnu2`）时，可以看到保存参数的寄存器不会溢出到栈上。 1  
2  
3  
4  
5  
6  
7  
__thread int x;  
void ext(int a, int b, int c, int d, int e, int f);  
int foo(int a, int b, int c, int d, int e, int f) {  
 int ret = ++x;  
 ext(a, b, c, d, e, f);  
 return ret;  
}

GCC 的 x86-64 移植版假定 `FLAGS_REG` 和 `RAX` 会被修改，而其他所有寄存器都会被保留。2024 年，glibc 的 x86-64 移植版修复了[未在 `_dl_tlsdesc_dynamic`](https://sourceware.org/bugzilla/show_bug.cgi?id=31372)中保留向量寄存器的问题（慢速代码路径）。

在 musl 中，对于静态 TLS 情况，TLS 描述符的两个字会被设置为 `((size_t)__tlsdesc_static, tpoff)`，其中 `__tlsdesc_static` 是一个返回第二个字的函数。glibc 的静态 TLS 情况类似。

```plaintext
.globl __tlsdesc_static
.hidden __tlsdesc_static
__tlsdesc_static:
  # The second word stores the TP offset of the TLS symbol.
  movq 8(%rax), %rax
  ret
```

这种方案优化了静态 TLS 的情况，但对需要动态 TLS 的情况则不利。请记住，我们在 GOT 中只有两个字，通过将第一个字改为函数指针，我们丢失了关于模块 ID 的信息。为了保留该信息，动态加载器必须将第二个字设置为指向一个由 malloc 分配的（模块 ID，偏移量）对的指针。

aarch64 默认使用 TLS 描述符。在 arm、i386 和 x86-64 上，可以通过 GCC `-mtls-dialect=gnu2` 选择 TLS 描述符。RISC-V psABI 于 2023 年 9 月[规定了](https://github.com/riscv-non-isa/riscv-elf-psabi-doc/pull/373) TLS 描述符。https://github.com/riscv-non-isa/riscv-elf-psabi-doc/issues/94

（我在 TLS 的 ld.lld、[IA-32](https://reviews.llvm.org/D112582), x86-64 和 [RISC-V](https://github.com/llvm/llvm-project/pull/79239) 端口中实现了 TLS 描述符及优化。）

我们来看一个例子。使用 `int32_t` 加载 x86-64 TLSDESC 的代码序列如下所示：1  
2  
3  
leaq x@TLSDESC(%rip), %rax  
call *x@TLSCALL(%rax)  
movl %fs:(%rax), %eax

假设我们正在构建共享对象，因此链接器不会把这个序列优化成 initial-exec 或 local-exec 模型。运行时，musl rtld 解析间接调用，使它加载 `__tlsdesc_static` 的 GOT 条目。代码执行时，call 指令调用 `__tlsdesc_static` 函数，从第二个字加载线程指针偏移量。第三条指令 `movl    %fs:(%rax), %eax` 再执行一次相对于 %fs 的内存加载。

在 GNU ld 的 aarch64、arm 和 x86-64 移植中，`R_*_TLSDESC` 重定位会放在 `.rela.plt`。glibc ld.so 必须处理这类延迟绑定重定位。然而，延迟绑定会引入数据竞争，因此 glibc 现在会立即解析 `R_*_TLSDESC` 重定位。我提交了 [`ld: Move R_*_TLSDESC to .rela.dyn`](https://sourceware.org/bugzilla/show_bug.cgi?id=28387)。

对于动态情况，rtld 通过 `dlopen` 分配一个对象，其中保存模块 ID 以及从 `dtv[m]` 到符号的偏移量。第二个 GOT 条目被改写为引用该对象。RISC-V TLS 描述符曾[探索用静态条目取代运行时 `dlopen`](https://github.com/riscv-non-isa/riscv-elf-psabi-doc/pull/373)，但这一想法被否决了。

### PowerPC `__tls_get_addr_opt`

Alan Modra 在 2015 年为 PowerPC 实现了一个简易的 TLSDESC 方案。[https://sourceware.org/legacy-ml/libc-alpha/2015-03/msg00626.html](https://sourceware.org/legacy-ml/libc-alpha/2015-03/msg00626.html)

如果 glibc ld.so 看到 `DT_PPC64_OPT`，它会在 `tls_index` 对象中将模块 ID 设置为零，并设置线程指针偏移量（而非相对于 dtv[m] 的偏移量）。glibc 导出符号 `__tls_get_addr_opt`.

如果 GNU ld 看到已定义的 `__tls_get_addr_opt`，就会把对 `__tls_get_addr` 的调用转换成对 `__tls_get_addr_opt` 的调用。PLT 代码序列检查模块 ID 是否为零：如果为零，就直接把 TP 偏移量加到 TP 并返回；否则调用 ld.so 中定义的 `__tls_get_addr_opt`。

在立即加载的共享对象的常见情况下，这可以省去一次函数调用。然而，此方案没有获得 TLSDESC 的自定义调用约定的好处。

### s390x `__tls_get_offset`

s390 和 s390x 使用 `__tls_get_offset` 而不是 `__tls_get_addr`。详情请参阅 [z/Architecture 工具链笔记](https://maskray.me/blog/2024-02-11-toolchain-notes-on-z-architecture)。

### 编译器选择哪种模型？

```c
if (executable) { // -fno-pic or -fpie
  if (preemptible)
    initial-exec;
  else
    local-exec;
} else { // -fpic
  if (preemptible || local-dynamic is not profitable)
    general-dynamic;
  else
    local-dynamic;
}
```

链接器使用类似的标准来检查是否应用 TLS 优化。

## 链接时 TLS 优化

一些 psABI 定义了 TLS 优化。其思路是代码序列具有固定形式，并带有适当的重定位进行标注。因此，链接器理解编译器的意图，并可以执行 4 种代码序列修改作为优化。共有 4 种优化方案。我已用各自的条件对其进行了标注。

- general-dynamic/TLSDESC 优化为 local-exec：`-no-pie/-pie` && non-preemptible
- general-dynamic/TLSDESC 优化为 initial-exec：`-no-pie/-pie` && 可抢占
- local-dynamic 优化为 local-exec：`-no-pie/-pie`（符号必须不可抢占，否则使用 local-dynamic 会出错）
- initial-exec 优化为 local-exec：`-no-pie/-pie` && non-preemptible

我有时把这些方案称为“易用的穷人版链接时优化”。直观地说，general-dynamic/TLSDESC 到 initial-exec 的优化很少见，因为很少会引用定义在其他模块中的 TLS 符号。

为了实现 TLS 优化，编译器需要向链接器传递足够的信息。因此，你可能会发现一些不重定位值的标记重定位。以下是 ppc64 的 general-dynamic 代码序列：

```plaintext
addis r3, r2, x@got@tlsgd@ha # R_PPC64_GOT_TLSGD16_HA
addi r3, r3, x@got@tlsgd@l   # R_PPC64_GOT_TLSGD16_LO
bl __tls_get_addr(x@tlsgd)   # R_PPC64_TLSGD followed by R_PPC64_REL24
```

`R_PPC64_TLSGD` 不重定位该位置。它用于指示这是代码序列中的 `__tls_get_addr` 函数调用。

据 Stefan Pintilie 称：“从大端 PowerPC Linux 发行版使用的 ELFv1 ABI 过渡到小端 PowerPC Linux 发行版使用的 ELFv2 ABI 之初，TLS 重定位规范存在一些歧义。”`bl __tls_get_addr` 指令不会被 `R_PPC64_TLSGD` 重定位。盲目转换 addis/addi 指令可能破坏代码序列。因此，GNU ld 在 2009-03-03 检测到缺少 `R_PPC64_TLSGD/R_PPC64_TLSLD` 时禁用了优化。

我并不喜欢我们到 2020 年还需要这样的 hack，但由于需求非常强烈，我还是在 ld.lld 中实现了一个方案。[https://reviews.llvm.org/D92959](https://reviews.llvm.org/D92959)

以下示例测试了几种优化方案。`a.c` 测试 general-dynamic 到 initial-exec 优化。`b.c:f1` 测试 local-dynamic 到 local-exec 优化。如果 `f0` 使用了 general-dynamic TLS 模型，那么也会测试 general-dynamic 到 local-exec 优化。

```c
cat > b.c <<e
__attribute__((visibility("protected"))) _Thread_local int x, y;
int f0() { return ++x; }
int f1() { return ++y + x; }
e
cat > a.c <<e
#include <stdio.h>
extern _Thread_local int x, y;
int f0(); int f1();
int main() {
  f0();
  printf("%d\n", f1());
  printf("%d\n", x + y);
}
e
clang -fpic -O1 -shared b.c -o b.so
clang -fpic -O1 a.c ./b.so -o a
```

可以使用 `clang -fpic -O1 a.c b.c -o a` 测试从通用动态模型到 local-exec 的优化。

## TLS 变体

共有两种变体。

在变体 I 中，静态 TLS 块位于线程指针之上（之后）。线程指针指向线程控制块（TCB）的末尾；TCB 是由 libc 实现定义、描述线程各种属性的每线程数据结构。arm、aarch64、alpha、ia64、m68k、mips、ppc 和 riscv 的方案与此类似。之所以说“类似”，是因为部分架构（包括 m68k、mips、powerpc32、powerpc64）将线程指针置于 TCB 末尾再加一个位移的位置。

假设主可执行文件和两个直接加载的共享对象包含 `PT_TLS` 段；那么 TCB 和静态 TLS 数据块的布局如下所示。1  
2  
3  
4  
5  
TCB TP_WITHOUT_DISPLACEMENT [GAP] tlsblock0 tlsblock1 tlsblock2  
  
TP_WITHOUT_DISPLACEMENT % tls_align == 0  
将 TP 设置为 TP_WITHOUT_DISPLACEMENT + displacement  
若 `displacement` 为 0 且没有 GAP，`tlsblock0` 的 TP 偏移量为 `exe.tls.p_vaddr&(exe.tls.p_align-1)`。

`TP_WITHOUT_DISPLACEMENT` 按全部 `PT_TLS` 段最大的 `p_align` 对齐。

`tlsblock0` 的 TP 偏移量由链接器和动态加载器共享。可相对于 `TP_WITHOUT_DISPLACEMENT` 按如下方式计算：1  
2  
3  
4  
5  
exe.tls_id= ++tls_cnt; // 将 tls_cnt 设为 1  
// GAP_ABOVE_TP 对于 aarch32 为 8，对于 aarch64 为 16  
exe.tls.offset = GAP_ABOVE_TP + ((-GAP_ABOVE_TP+exe.tls.p_vaddr) & (exe.tls.p_align-1));  
tls_offset = exe.tls.offset + exe.tls.p_memsz;  
tls_align = max(exe.tls.p_align, MIN_TLS_ALIGN);

例如，在 powerpc64 上，位移量为 0x7000，这意味着 TP（r13 寄存器）被设置为线程控制块末尾（`TP_WITHOUT_DISPLACEMENT`）加上 0x7000。可执行文件中值为 TLS 的 `st_value==0` 符号所分配的空间位于 `r13-0x7000 + exe.tls.p_vaddr%exe.tls.p_align`。由于 `exe.tls.p_vaddr%exe.tls.p_align` 通常为 0，访问 `st_value==0` 的代码序列可能如下所示：1  
2  
addis 3, 13, 0  
lwz 3, -0x7000(3)

一条 add 指令可访问 `[r13-0x8000, r13+0x8000)`，即 `[TP_WITHOUT_DISPLACEMENT-0x1000, TP_WITHOUT_DISPLACEMENT+0xf000)`。若线程控制块不大于 0x1000，其成员可通过单条 add 指令访问。

arm 和 aarch64 的位移量为零，但会在 TP 处保留两个字（即 `tlsblock0` 前的间隙）。`tlsblock0` 的 TP 偏移量为 `sizeof(void*)*2 + ((p_vaddr-sizeof(void*)*2)&(p_align-1))`。

动态加载器放置 `tlsblock1` 和 `tlsblock2` 时会使用最小的对齐填充。其偏移量不是由链接器确定的，因此理论上动态加载器可以添加任意数量的填充。如果我们将不带位移的 TP 作为锚点，则立即加载的共享对象的 `PT_TLS` 段偏移量可按如下方式确定：1  
2  
3  
4  
5  
6  
7  
for (int i = 0; i \< n_dso_with_tls; i++) {  
 p = dso_with_tls[i];  
 p-\>tls_id = ++tls_cnt;  
 p-\>tls.offset = tls_offset + ((-tls_offset+p-\>tls.p_vaddr) & (p-\>tls.p_align-1)); // tls_offset = p_vaddr (mod p_align)  
 tls_offset = p-\>tls.offset + p-\>tls.p_memsz;  
 tls_align = max(tls_align, p-\>tls.p_align);  
}

---

i386、x86-64、s390 和 sparc 使用变体 II。在变体 II 中，静态的 TLS 块位于线程指针的下方（之前）。线程指针指向线程控制块的起始位置。

假设主可执行文件和两个立即加载的共享对象包含 `PT_TLS` 段，那么 TCB 和静态 TLS 块的放置情况如下。1  
2  
3  
4  
tlsblock2 tlsblock1 tlsblock0 TP TCB  
  
TP % tls_align == 0  
tlsblock0 的 TP 偏移量为 -exe.tls.p_memsz - ((-exe.tls.p_memsz-exe.tls.p_vaddr)&(exe.tls.p_align-1))。

TP 按所有 `p_align` 段中最大的 `PT_TLS` 对齐。

`tlsblock0` 的 TP 偏移量是一个在链接器和动态加载器之间共享的值。可以按如下方式计算：1  
2  
3  
4  
exe.tls_id = ++tls_cnt; // 将 tls_cnt 设置为 1  
tls_offset = exe.tls.p_memsz + ((-(uintptr_t)exe.tls.p_vaddr-exe.tls.p_memsz) & (exe.tls.p_align-1));  
exe.tls.offset = -tls_offset;  
tls_align = max(exe.tls.p_align, MIN_TLS_ALIGN);

若觉得上式令人困惑，确实如此；-) 正常情况下可忽略对齐要求，`tlsblock0` 的 TP 偏移量就是 `-p_memsz`。当 `p_vaddr%p_align!=0` 时，glibc 的变体 II 存在 [BZ24606](https://sourceware.org/bugzilla/show_bug.cgi?id=24606) 问题。我将该问题报告给 FreeBSD rtld，并在 [此提交](https://github.com/freebsd/freebsd-src/commit/e6c76962031625d51fe4225ecfa15c85155eb13a) 中修正 i386/amd64 的公式。

动态加载器放置 `tlsblock1` 和 `tlsblock2` 时会使用最小的对齐填充，尽管它们的放置可以更灵活，因为其偏移量不由链接器确定。1  
2  
3  
4  
5  
6  
7  
for (int i = 0; i \< n_dso_with_tls; i++) {  
 p = dso_with_tls[i];  
 p-\>tls_id = ++tls_cnt;  
 tls_offset += p-\>tls.p_memsz + ((-p-\>tls.p_memsz-p-\>tls.p_vaddr) & (p-\>tls.p_align-1));  
 p-\>tls.offset = -tls_offset; // -tls_offset = p_vaddr (mod p_align)  
 tls_align = max(tls_align, p-\>tls.p_align);  
}

## 对齐

对于一个 TLS 变量来说，其对齐方式描述了它在 TLS 初始化映像中的位置是如何对齐的。如果 `PT_TLS` 程序头满足 `p_vaddr%p_align==0`，那么 `st_value` 也会按照变量的对齐方式进行对齐。

## glibc 的 TLS 实现

```plaintext
// nptl/descr.h
struct pthread
{
  union
  {
#if !TLS_DTV_AT_TP
    tcbhead_t header;
...

// sysdeps/x86_64/nptl/tls.h
typedef struct
{
  void *tcb;
  dtv_t *dtv;
  ...
};
```

在 x86-64 上，`TLS_DTV_AT_TP` 为 0，`struct pthread` 位于 `fs:0`，`dtv` 位于 `fs:8`。

## 调试器：定位 TLS 变量

编译器用 `DW_OP_form_tls_address`（操作码 `0x9b`）编码 TLS 变量的位置；其前是变量的 DTPOFF，即相对于模块 TLS 块起点的偏移量。DTPOFF 值由重定位编码，并由链接器解析。

当 GDB 求值 `DW_OP_form_tls_address` 时，它有两部分：(1) 变量所在的模块（通过其 `link_map` 地址）和 (2)DTPOFF 偏移量，并且必须计算当前线程的运行时地址。

### libthread_db 路径

GDB 在 Linux 上的主要路径是通过 `libthread_db`，这是 glibc 附带的一个辅助库（`nptl_db/`）。GDB（`linux-thread-db.c`）调用：

```c
td_thr_tls_get_addr(thread_handle, link_map_addr, dtpoff, &result_addr)
```

实现（`nptl_db/td_thr_tls_get_addr.c`）从被调试进程读取 `link_map.l_tls_modid` 获取模块的 DTV 索引，再调用 `td_thr_tlsbase()`（`nptl_db/td_thr_tlsbase.c`），该函数会：

- 对于动态 TLS：读取 `pthread.dtvp`（线程的 DTV 指针），检查 `dtv[0].counter`（DTV 世代）是否与 `_dl_tls_dtv_slotinfo_list` 中该模块所需世代一致，然后返回 `dtv[modid].pointer.val`。
- 对于静态 TLS（启动时加载）：根据线程指针和 `link_map.l_tls_offset` 计算地址。

结构元数据（内部 glibc 结构体的字段偏移量）通过 `nptl_db/structs.def` 发布，因此 GDB 无需 glibc 调试符号即可读取它们。

### 内部回退

[提交 85e1d8f93df6](https://sourceware.org/git/?p=binutils-gdb.git;a=commit;h=85e1d8f93df69a8e39ae9965a8a1cf02546e92a7) 在 `gdb/svr4-tls-tdep.c` 中加入内部 TLS 解析路径。当 `libthread_db` 不可用，或启用了维护设置 `force-internal-tls-address-lookup` 时使用它。GDB 会直接遍历 TLS 数据结构：

1. **检测 C 库**：检查 ELF 解释器路径是否包含 `/ld-musl-`（musl）；否则假定为 glibc。
2. **计算模块 ID**：GDB 通过 solib 观察者跟踪共享库加载和卸载时的 `link_map` 地址，并自行分配模块 ID，以镜像动态链接器的行为。
3. **寻找 DTV**：

    - **x86-64**：线程指针为 `fsbase`。glibc 和 musl 都把 `struct pthread` 放在 `fsbase`，并把 `dtv` 作为第二个指针大小的字段（glibc 是 `tcbhead_t.dtv`；musl 是 `struct pthread.dtv`，因为 x86-64 未定义 `TLS_ABOVE_TP`）。因此 `dtv_ptr_addr = fsbase + sizeof(pointer)`。
    - **RISC-V**：线程指针为 `tp`，布局因 libc 而异：

          - glibc 的 `tcbhead_t = {dtv, private}` 位于 `tp` 之前：`dtv_ptr_addr = tp - 2*sizeof(pointer)`。
          - musl 定义 `TLS_ABOVE_TP`，因此 `dtv` 是 `struct pthread` 的**最后一个字段**（`pthread_impl.h` 的第 3 部分），而 `tp` 指向结构体末尾之后：`dtv_ptr_addr = tp - sizeof(pointer)`。
4. **索引 DTV**：读取 `dtv[modid]`。glibc 的每个 DTV 条目宽两个指针，musl 中则宽一个指针。
5. **应用 `DTP_OFFSET`**（仅 musl）：musl 会按 `DTP_OFFSET` 偏置 DTV 条目（例如 RISC-V 上为 `0x800`，见 `arch/riscv64/pthread_arch.h`）。最终地址为 `dtv[modid] - DTP_OFFSET + dtpoff`。

## 异步信号安全的 TLS

C11 7.14.1“信号处理”规定：

> 如果信号的发生并非调用 abort 或 raise 函数的结果，那么在下列情况下行为未定义：信号处理函数引用任何具有静态或线程存储期、且不是无锁原子对象的对象（向声明为 volatile sig_atomic_t 的对象赋值除外）；或者信号处理函数调用标准库中 abort、_Exit、quick_exit 以外的函数，以及首个参数等于引发处理函数调用之信号编号的 signal 函数以外的函数。此外，如果对 signal 函数的这种调用返回 SIG_ERR，则 errno 的值不确定。

C++11 [support.signal] 规定：

> 除非求值包含以下情况之一，否则它就是信号安全的：
>  
> 访问具有线程存储期的对象；
>  
> 如果信号处理函数的调用包含非信号安全的求值，则其行为未定义。

尽管如此，从信号处理函数访问 TLS 仍然很有用，例如 CPU 和内存分析器就有这种需求，因此这类访问需要具备异步信号安全性。Google 因使用 JVM 和通过 dlopen 加载的 JNI 库而报告过这个问题（[对来自 dlopen() 加载库的 __thread 变量进行异步信号安全访问？](https://sourceware.org/legacy-ml/libc-alpha/2012-06/msg00335.html)）。他们最终采用了一个未上游合并、使用自定义分配器的补丁。

下面详细讨论这个问题。

Local-exec 和 initial-exec TLS 模型天然满足这一要求，因为静态 TLS 块的大小在程序启动时就已固定，而且每个线程都有一个预先分配的副本。

对于使用 general-dynamic 或 local-dynamic TLS 模型、由 dlopen 加载的共享对象，有两种情况。

- 动态加载器在 `dlopen` 时为所有当前运行的线程分配足够的存储空间，并在 `pthread_create` 时分配足够的存储空间。musl 选择了这种方式。在 dlopen 时，动态加载器需要阻止信号递送、获取线程列表锁，并为每个线程安装新的动态线程向量。
- 延迟分配 TLS。TLS 存储在首次调用 `__tls_get_addr` 时分配。glibc 和许多其他库选择了这种实现。分配通常由 malloc 完成，而 malloc 不具备异步信号安全性。

延迟分配 TLS 的优点是，不会让无须访问新共享对象 TLS 的线程承担额外开销。然而，要让 `__tls_get_addr` 具备异步信号安全性很困难。既延迟分配、又保证动态 TLS 访问绝不失败是不可能的（[TLS Redux](https://sourceware.org/pipermail/libc-alpha/2014-January/047799.html)）。如果 `__tls_get_addr` 无法分配内存，理想行为是“安全失败”（例如终止进程），而不是出现各种未定义行为或死锁。

一种变通方法是让共享对象使用 initial-exec TLS 模型，但这会消耗静态 TLS 空间这一全局资源。

如果未来实现了在 dlopen 时立即分配 TLS 的机制，可以想象它可能需要新的符号版本，因为可能有程序依赖延迟 TLS 分配。

## 大代码模型

许多 64 位架构具有小代码模型。有些则定义了大代码模型。详见[重定位溢出与代码模型](https://maskray.me/blog/2023-05-14-relocation-overflow-and-code-models)。

小代码模型通常将节的地址和大小限制在 4GiB 或 2GiB 范围内，而大代码模型通常不做这种假设。TLS 通常很小，而且即使使用大代码模型，代码模型仍会施加一些限制。

对于 local-exec TLS 模型，符号通常通过相对于寄存器（线程指针）的偏移量引用，因此无须为大代码模型另作区分。

对于 initial-exec TLS 模型，由于需要加载 GOT，且 GOT 是数据段的一部分，大代码模型在技术上应该实现一种不受代码与数据之间距离限制的代码序列。GCC 尚未实现此类代码序列。

对于 general-dynamic 和 local-dynamic TLS 模型，通常需要加载 GOT 并调用 `__tls_get_addr`。如前所述，GOT 的加载需要不受 32 位限制。对于 `__tls_get_addr` 调用，在已实现范围扩展 thunk 的架构上，由于链接器可以将调用重定向到安排调用的 thunk，因此无需特殊处理。

x86-64 尚未实现 thunk。用 x86-64 的 `gcc -S -fpic -mcmodel=large` 编译一个程序，可以看到 `__tls_get_addr` 调用是间接的。这样可以避免直接 CALL 指令施加的正负 2GiB 距离限制。

```plaintext
movabsq	$_GLOBAL_OFFSET_TABLE_-.L2, %r11
pushq	%rbx
leaq	.L2(%rip), %rbx
addq	%r11, %rbx
leaq	a@tlsgd(%rip), %rdi
movabsq	$__tls_get_addr@PLTOFF, %rax
addq	%rbx, %rax
call	*%rax
popq	%rbx
movl	(%rax), %eax
ret
```

目前对大代码模型 TLS 的支持相当有限。大多数配置并未解除 GOT 加载的限制。在 aarch64 上，GCC 和 Clang 都尚未实现 `-fpic -mcmodel=large`。

## 线程专有数据键

ELF TLS 的一种替代方案是线程专有数据键：`pthread_key_create`、`pthread_setspecific`、`pthread_getspecific` 和 `pthread_key_delete`。该方案可以看作一种支持键复用、实现更简单的 `__tls_get_addr`。C11 提供了对应的 `tss_create`、`tss_set`、`tss_get` 和 `tss_delete`，但很少使用。Windows 也提供类似的 API：`TlsAlloc`、`TlsSetValue`、`TlsGetValue`、`TlsFree`。

键的最大数量通常有限制：glibc 上一般是 1024，musl 上是 128。因此，可能需要大量数据键的应用程序通常会在线程专有数据键之上创建封装，例如 Chromium 的 `base/threading/thread_local_storage.h`。

POSIX.1-2017 并未要求 `pthread_setspecific`/`pthread_getspecific` 具备异步信号安全性。尽管如此，大多数实现仍使 `pthread_getspecific` 具备异步信号安全性；`pthread_setspecific` 则不一定如此。

## `-femulated-tls`

`-femulated-tls` 使用线程专有数据键实现模拟 TLS，相当于对所有情况都使用 general-dynamic TLS 模型。

```c
__thread int tls0;
extern __thread int tls1;
int foo() { return tls0 + tls1; }
```

```plaintext
  adrp    x0, :got:__emutls_v.tls0
  ldr     x0, [x0, :got_lo12:__emutls_v.tls0]  // load __emutls_control structure
  bl      __emutls_get_address                 // get load address
  ldr     w19, [x0]                            // load
  adrp    x0, :got:__emutls_v.tls1
  ldr     x0, [x0, :got_lo12:__emutls_v.tls1]  // load __emutls_control structure
  bl      __emutls_get_address                 // get load address
  ldr     w8, [x0]                             // load

  .type   __emutls_v.tls0,@object         // @__emutls_v.tls0
  .data
  .globl  __emutls_v.tls0
  .p2align        3, 0x0
__emutls_v.tls0:                          // A __emutls_control instance
  .xword  4                               // size
  .xword  4                               // alignment
  .xword  0                               // index, initialized to 0
  .xword  0                               // pointer to the initializer
  .size   __emutls_v.tls0, 32
```

每个线程局部变量定义都关联一个 `__emutls_control` 实例，其中记录大小、对齐、索引和初始化器。

`__emutls_get_address` 的运行时实现类似延迟 TLS 分配方案中的 `__tls_get_addr`。每个线程都有一个对象数组（`emutls_address_array`），每个元素都是指向变量值的指针。每个线程局部变量都会分配到该数组中的一个索引。

低效来自以下几个方面：

- 没有链接器优化。
- 运行时不是从线程指针（通常可在寄存器中获取）获取动态线程向量，而是需要调用 `pthread_getspecific` 来获取向量。
- 动态加载器不了解模拟 TLS，因此通常在访问函数中通过 `pthread_once` 分配存储。

libgcc 拥有成熟的运行时。compiler-rt 中的运行时由 Android 团队于 2015 年贡献。

目前，Android API 级别低于 29 的目标以及 OpenBSD 目标在 Clang 中默认使用 `-femulated-tls`。参见 `hasDefaultEmulatedTLS`。

## C++ thread_local

C++ thread_local 在 `__thread` 的基础上增加了额外特性：首次使用前动态初始化，以及在线程退出时析构。

实现选择延迟初始化 TLS。如果 thread_local 变量需要动态初始化或具有非平凡析构函数，编译器会调用 TLS 包装函数（`_ZTW*`，位于 COMDAT 组中），而不是直接引用变量。TLS 包装函数会调用 TLS 初始化函数（`_ZTH*`，弱符号），后者是 `__tls_init` 的别名。`__tls_init` 调用构造函数，并通过 `__cxa_thread_atexit` 注册析构函数。

`__cxa_thread_atexit` 之所以复杂，是因为定义在 dlopen 加载的共享对象中的 thread_local 变量，需要在 dlclose 时、线程退出之前完成析构。libsupc++ 和 libc++abi 定义了 `__cxa_thread_atexit`：如果 libc 实现提供 `__cxa_thread_atexit_impl`，就调用它；否则使用基于线程专有数据键的通用实现。

例如，`x` 需要一个 TLS 包装函数。编译器可能内联该包装函数和 `__tls_init`。

```cpp
extern thread_local int x;
int foo() { return x; }
```

汇编如下。它使用未定义弱符号 `_ZTH1x` 检查 TLS 初始化函数是否存在；如果存在，就调用该函数。随后通过常规的 initial-exec、general-dynamic TLS 模型或 TLSDESC 引用变量。

```plaintext
_Z3foov:
  pushq %rax
  cmpq $0, _ZTH1x@GOTPCREL(%rip)
  je .LBB0_2
  callq _ZTH1x@PLT
.LBB0_2:
  movq x@GOTTPOFF(%rip), %rax
  movl %fs:(%rax), %eax
  popq %rcx
  retq

.weak _ZTH1x
```

如果确定 `x` 不需要动态初始化，C++20 的 constinit 可以使它与传统的 `__thread` 一样高效。较旧的语言标准也可以使用 `[[clang::require_constant_initialization]]`。

```cpp
extern thread_local constinit int x;
```

也可以改用指针，并通过另一个线程局部变量或 `pthread_key_create` 注册线程析构函数。例如，原本直接引用带析构函数的线程局部变量：1  
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
//--- a.cc  
#include \<assert.h\>  
#include \<stdio.h\>  
#include \<thread\>  
struct A { A(); ~A(); int x; };  
static thread_local A a;  
A &foo() { return a; }  
void th() {  
 printf("%d\\n", foo().x++);  
 printf("%d\\n", foo().x++);  
}  
int main() {  
 { std::jthread t(th); }  
 th();  
}  
  
//--- b.cc  
#include \<stdio.h\>  
struct A { A(); ~A(); int x; };  
A::A() : x(0) {}  
A::~A() { puts("~A"); }

你可以使用一个指针，仅初始化一次，然后使用另一个变量来销毁它。

```cpp
//--- a.cc
#include <assert.h>
#include <stdio.h>
#include <thread>

struct A { A(); ~A(); int x; };
static thread_local A *a;
struct ADtor { ~ADtor() { delete a; }; };
static thread_local ADtor a_dtor;

A &foo() { return *a; }
void init_tls() {
  assert(!a);
  a = new A;
  // Use a_dtor to ensure its dtor will be called at thread exit. https://gcc.gnu.org/bugzilla/show_bug.cgi?id=61991
  (void)&a_dtor;
}

void th() {
  init_tls();
  printf("%d\n", foo().x++);
  printf("%d\n", foo().x++);
}

int main() {
  { std::jthread t(th); }
  th();
}

//--- b.cc
#include <stdio.h>
struct A { A(); ~A(); int x; };
A::A() : x(0) {}
A::~A() { puts("~A"); }
```

下面的示例中，`__tls_init` 需要调用 `__cxa_thread_atexit`。

```cpp
struct S { S(); ~S(); };
thread_local S s;
S &foo() { return s; }
```

## 未定义弱引用 TLS 符号

常规的未解析弱引用符号值为零。TLS 符号位于一个独立的地址空间中，因此该规则不适用。

## macOS TLS

macOS 很晚才加入 TLS 支持。其方案与 ELF 的 TLS 描述符类似，但没有优良的自定义调用约定保证。换句话说，其性能可能比 ELF 的 general-dynamic TLS 模型更差。令我惊讶的是，即使具有内部链接的线程局部变量也需要一次间接函数调用。

```cpp
thread_local int tls;
int f() { return tls; }
```

```plaintext
// x86-64
movq _tls@TLVP(%rip), %rdi     // X86_64_RELOC_TLV(_tls)
callq *(%rdi)                  // calls getAddrFunc in libdyld.dylib
movl (%rax), %eax
```

```plaintext
adrp x0, _tls@TLVPPAGE         // ARM64_RELOC_TLVP_LOAD_PAGEOFF12(_tls)
ldr x0, [x0, _tls@TLVPPAGEOFF] // ARM64_RELOC_TLVP_LOAD_PAGE21(_tls)
ldr x8, [x0]
blr x8                         // x0 = &tls
ldr w0, [x0]                   // x0 = tls
```

`_tls@TLVP` 引用 `__DATA,__thread_vars` 中的一个 TLV 描述符。每个描述符包含三个字：

- `void* (*thunk)(struct TLVDescriptor*)`
- `unsigned long key`：线程专有数据键（每个库唯一），表示 TLS 块
- `unsigned long offset`：块内的偏移量

[dyld](https://github.com/apple-oss-distributions/dyld) 遍历这些描述符，并将第一个字（`thunk`）设为 `getAddrFunc`。

`__attribute__((tls_model(...)))` 属性在 Clang 中被忽略。

## Windows TLS

代码序列从线程环境块中取出 `ThreadLocalStoragePointer`（偏移量 88），并用 `_tls_index` 对其进行索引。返回值再以变量相对于 `.tls` 节起始位置的偏移量索引。该方案类似 ELF 的 local-dynamic TLS 模型，只是以数组索引操作取代了 `__tls_get_desc` 调用。

```plaintext
movl _tls_index(%rip), %eax
movq %gs:88, %rdx
movq (%rdx,%rax,8), %rax
movl %ecx, tls@SECREL32(%rax)
```

不支持从另一个 DLL 引用 TLS 变量。

```cpp
__declspec(dllimport) extern thread_local int tls;
// error C2492: 'tls': data with thread storage duration may not have dll interface
```

其中还有很多细节，但我对 Windows 的了解不足以继续展开 ;-) 感兴趣的读者可以参阅 [Thread Local Storage, part 3: Compiler and linker support for implicit TLS](http://www.nynaeve.net/?p=183)。

## libc 的 TLS 块 API

Sanitizer 运行时需要在多种场景中使用 TLS 块。关于 glibc 的功能请求，请参见 [https://sourceware.org/bugzilla/show_bug.cgi?id=16291](https://sourceware.org/bugzilla/show_bug.cgi?id=16291)。下文将详细说明。

在 LLVM 中，OrcJIT 希望能够注册 TLS 块。Lang Hames 告诉我，他已经在 Orc 运行时中实现 dyld 的 TLS 支持 API，使原生 TLS 得以工作。

Florian Weimer 于 2021 年 5 月发布了[线程属性 API](https://www.openwall.com/lists/libc-coord/2021/05/21/1)。

## 为什么 compiler-rt 需要知道 TLS 块？

### AddressSanitizer "asan"（`-fsanitize=address`）

AddressSanitizer 的主要任务是检测可寻址性问题。如果普通内存字节不可寻址（即访问它属于未定义行为），就称该字节已被毒化，关联的影子内存则编码可寻址性信息（全部未毒化、全部毒化或部分毒化）。

创建线程时，运行时应取消对线程栈和静态 TLS 块的毒化，以允许访问。（`test/asan/TestCases/Linux/unpoison_tls.cpp`；由 [`[asan] Make ASan report the correct thread address ranges to LSan.`](https://github.com/llvm/llvm-project/commit/09886cd17ab8e5e601fda0e2aa21ff28c1a8fa63) 引入。）在线程退出时，运行时还会取消对线程栈和 TLS 块的毒化，以允许之后的 TSD 析构函数访问它们。

注意：如果分配由 rtld/libc 在内部完成且未被拦截，就无须取消该范围的毒化，因为关联的影子内存理应全为零。但如果分配被拦截，运行时应取消该范围的毒化，以防它复用了先前恰好包含已毒化字节的分配。

在 glibc 中，`_dl_allocate_tls` 和 `_dl_deallocate_tls` 调用内部的 malloc/free 函数，不会被拦截。因此这些分配对运行时不可见，影子字节也全为零。

### 硬件辅助 AddressSanitizer "hwasan"（`-fsanitize=hwaddress`）

它的 `ClearShadowForThreadStackAndTLS` 与 asan 的对应机制类似。

### LeakSanitizer "lsan"（`-fsanitize=leak`）

LeakSanitizer 检测内存泄漏。在许多目标上，它集成在 AddressSanitizer 中并默认启用，但也可以单独使用。检查器由 `atexit` 钩子触发（默认选项为 `LSAN_OPTIONS=detect_leaks=1:leak_check_at_exit=1`），也可以通过 `__lsan_do_leak_check` 调用。

每个受支持的平台都会提供入口点 `StopTheWorld`（例如 Linux 的[实现](https://code.woboq.org/llvm/compiler-rt/lib/sanitizer_common/sanitizer_stoptheworld_linux_libcdep.cpp.html#144)），执行以下操作：

- 调用 clone 系统调用，创建与调用进程共享地址空间的新进程。
- 在新进程中遍历 `/proc/$pid/task/`，列出所有线程。
- 在新进程中调用 `SuspendThread`（使用 ptrace 的 `PTRACE_ATTACH`）挂起线程。

`StopTheWorld` 返回后，运行时执行标记清除、报告泄漏，然后调用 `ResumeAllThreads`（使用 ptrace 的 `PTRACE_DETACH`）。

注意：该实现不能调用 libc 函数，也不会执行代码注入。根集合包括每个线程的静态和动态 TLS 块。

（`pthread_create` 拦截器会调用 `AdjustStackSize`，后者通过 `GetTlsSize` 计算最小栈大小。[相关实现](https://code.woboq.org/llvm/compiler-rt/lib/sanitizer_common/sanitizer_posix_libcdep.cpp.html#411)；我不确定 musl 是否需要这样做。）

拦截 `__tls_get_addr` 对 lsan 有用，但并非必需。首先，Linux 的 `InitializePlatformSpecificModules` 实现会忽略动态加载器产生的泄漏。其次，`__tls_get_addr` 发起的分配会被 `kStdSuppressions` 中的内置规则 `leak:*tls_get_addr` 抑制。

当前 lsan 实现对 `GetTls` 有更多要求：它不拦截 `pthread_setspecific`，而是要求 `GetTls` 返回的范围包含指向 `pthread_setspecific` 区域的指针，否则就会产生泄漏误报。

此外，lsan 在 `pthread_create` 时获取静态 TLS 边界，并期望这些边界包含动态加载模块的 TLS 块。这意味着 `GetTls` 返回的范围必须包含静态 TLS 预留空间。

（你可能会问：线程控制块中有 DTV 指针，为什么 lsan 不能跟踪它所引用的分配？这是因为 rtld/libc 实现通常把线程的静态 TLS 块作为线程栈的一部分分配，而运行时看不到这些分配。）

在 glibc 上，`GetTls` 返回的范围包含线程专有数据键所用的 `pthread::{specific_1stblock,specific}`。目前还有一个变通办法，用于忽略 ld.so 分配的动态 TLS 块。注意：如果 `pthread::{specific_1stblock,specific}` 指针经过加密，lsan 就无法跟踪该分配。

### MemorySanitizer "msan"（`-fsanitize=memory`）

MemorySanitizer 检测对未初始化内存的使用。如果普通内存字节中存在未初始化（已毒化）的位，其关联影子字节中就会有置 1 的位。

它与 asan 类似。创建线程时，运行时应取消对线程栈和静态 TLS 块的毒化，以允许访问。（`test/msan/tls_reuse.cpp`）在线程退出时，运行时还会取消对线程栈和 TLS 块的毒化，以允许 TSD 析构函数访问它们。

msan 需要完成比 asan 更多的工作：`__tls_get_addr` 拦截器（`DTLS_on_tls_get_addr`）会检测新的动态 TLS 块，并取消影子内存的毒化。ld.so 会调用不可插入的 `memset` 清空这些块。否则，如果动态 TLS 块复用先前带有已毒化字节的分配，就可能产生误报。一种较为可靠的触发方式是（`test/msan/dtls_test.cpp`；[https://github.com/google/sanitizers/issues/547](https://github.com/google/sanitizers/issues/547)）：

- 在线程中，将未初始化（已毒化）的值写入动态 TLS 块
- 销毁该线程
- 创建新线程
- 尝试让新线程复用已毒化的动态 TLS 块。

注意：aarch64 默认使用 TLSDESC，因此没有可插入的符号。

在 glibc 2.19 的开发过程中，[提交 1f33d36a8a9e78c81bed59b47f260723f56bb7e6](https://sourceware.org/git/?p=glibc.git;a=commit;h=1f33d36a8a9e78c81bed59b47f260723f56bb7e6)（"Patch 2/4 of the effort to make TLS access async-signal-safe."）被合入。`DTLS_on_tls_get_addr` 检测 `__signal_safe_memalign` 头；如果对应块不在静态 TLS 边界内，就将其视为动态 TLS 块。[提交 dd654bf9ba1848bf9ed250f8ebaa5097c383dcf8](https://sourceware.org/git/?p=glibc.git;a=commit;h=dd654bf9ba1848bf9ed250f8ebaa5097c383dcf8)（"Revert \"Patch 2/4 of the effort to make TLS access async-signal-safe.\""）撤销了 `__signal_safe_memalign`，但该实现仍保留在 grte 分支中。

另请参阅 [Re: glibc 2.19 - asyn-signal safe TLS and ASan.](https://groups.google.com/g/address-sanitizer/c/BfwYD8HMxTM)

与 lsan 类似，`pthread_create` 拦截器会调用 `AdjustStackSize`，后者通过 `GetTlsSize` 计算最小栈大小。

### ThreadSanitizer "tsan"（`-fsanitize=thread`）

与 lsan 类似，`pthread_create` 拦截器会调用 `AdjustStackSize`，后者通过 `GetTlsSize` 计算最小栈大小。

与 msan 类似，运行时会取消 TLS 块的毒化以避免误报。`test/tsan/dtls.c`（D20927）对此进行了测试。tsan 也需要拦截 `__tls_get_addr`。aarch64 的 TLSDESC 没有可插入符号，同样会造成问题。

我曾误以为 [https://reviews.llvm.org/D93866](https://reviews.llvm.org/D93866) 是一种变通方案。[https://sourceware.org/pipermail/libc-alpha/2021-January/121352.html](https://sourceware.org/pipermail/libc-alpha/2021-January/121352.html) 解释说，该代码自 2012 年以来实际上没有发生实质变化。

对于动态 TLS 块，较旧的 glibc（例如 2.23）会调用 `__libc_memalign`，该调用会被拦截（`tsan/rtl/tsan_interceptors_posix.cpp`）；从 BZ #17730 起，较新的 glibc（例如 2.32）会调用 `malloc`。

### NumericalSanitizer "nsan"（`-fsanitize=numerical`）

与 msan 和 dfsan 类似，运行时会取消 TLS 块的毒化以避免误报（[#102718](https://github.com/llvm/llvm-project/pull/102718)）。

### glibc TLS 分配

对于动态 TLS 块，`allocate_and_init` 会分配相应存储。

对于新线程，glibc 在 Variant II 架构上会分配一块内存区域，把静态 TLS 块（其中包含 pthread 结构）放在末尾（`nptl/allocatestack.c`），剩余空间则用作线程栈。栈指针可能仅比 canary 地址（x86-64 上为 %fs:0x28）低几百字节，因此一次较大的越界写入就可能覆盖它。

### Android bionic

Android bionic（API 级别 31）在 `libc/include/sys/thread_properties.h` 中引入了一些 TLS API。compiler-rt 会使用 `__libc_get_static_tls_bounds` 和 `__libc_iterate_dynamic_tls`。

```c
/**
 * Gets the bounds of static TLS for the current thread.
 *
 * Available since API level 31.
 */
void __libc_get_static_tls_bounds(void** __static_tls_begin,
                                  void** __static_tls_end) __INTRODUCED_IN(31);

/**
 * Iterates over all dynamic TLS chunks for the given thread.
 * The thread should have been suspended. It is undefined-behaviour if there is concurrent
 * modification of the target thread's dynamic TLS.
 *
 * Available since API level 31.
 */
void __libc_iterate_dynamic_tls(pid_t __tid,
                                void (*__cb)(void* __dynamic_tls_begin,
                                             void* __dynamic_tls_end,
                                             size_t __dso_id,
                                             void* __arg),
                                void* __arg) __INTRODUCED_IN(31);
```

dalias 的笔记

```plaintext
<@dalias> i think the api proposed there looks wrong
<@dalias> e.g. "static tls bounds" supposes a particular implementation where static is a single block range and static and dynamic are distinct
<@dalias> the interfaces proposed for dynamic are even worse
<@dalias> allowing interposition of individual dynamic tls area creation
<@dalias> supposing that they're created individually and ignoring that any interposition here would be extremely unsafe
<@dalias> the alternative prposed __libc_iterate_dynamic_tls is just a renamed dl_iterate_phdr without the glibc bug
<@dalias> and is pointless -- just fix the glibc bug
<@dalias> "When a thread (or dynamic TLS) is destroyed, the shadow for the stack (or dynamic TLS) should be unpoisoned"
<@dalias> this is backwards -- it should be poisoned because it's no longer valid. the stated desired behavior is based on bad glibc implementation internals (reuse of the stack/tls memory) and ignores that something should be done to unpoison it at the moment it's reused, not when it's freed for reuse
```

测试 TLS：1  
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
28  
29  
30  
31  
32  
33  
34  
35  
36  
37  
38  
39  
40  
41  
cat \> ./a.c \<\<eof  
#include \<assert.h\>  
int foo();  
int bar();  
int main() {  
 assert(foo() == 2);  
 assert(foo() == 4);  
 assert(bar() == 2);  
 assert(bar() == 4);  
}  
eof  
  
cat \> ./b.c \<\<eof  
__thread int tls0;  
extern __thread int tls1;  
int foo() { return ++tls0 + ++tls1; }  
static __thread int tls2, tls3;  
int bar() { return ++tls2 + ++tls3; }  
eof  
  
echo '__thread int tls1;' \> ./c.c  
  
sed 's/ /\\t/' \> ./Makefile \<\<'eof'  
.MAKE.MODE = meta curDirOk=true  
  
CC := gcc -m32 -g -fpic -mtls-dialect=gnu2  
LDFLAGS := -m32 -Wl,-rpath=.  
  
all: a0 a1 a2  
  
run: all  
 ./a0 && ./a1 && ./a2  
  
c.so: c.o; ${LINK.c} -shared $\> -o $@  
bc.so: b.o c.o; ${LINK.c} -shared $\> -o $@  
b.so: b.o c.so; ${LINK.c} -shared $\> -o $@  
  
a0: a.o b.o c.o; ${LINK.c} $\> -o $@  
a1: a.o b.so; ${LINK.c} $\> -o $@  
a2: a.o bc.so; ${LINK.c} $\> -o $@  
eof

```sh
bmake run && bmake CFLAGS=-O1 run
```

## 杂项

在 AArch32 上，许多 TLS 代码序列需要常量池，因此 TLS 与 `-mexecute-only` 不兼容。
