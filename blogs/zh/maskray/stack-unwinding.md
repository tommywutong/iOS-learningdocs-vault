---
title: 栈展开
source: MaskRay (宋方睿)
source_key: maskray
source_url: 'https://maskray.me/blog/2020-11-08-stack-unwinding'
original_language: en
published: 2020-11-08
status: active
license: 未声明 → 仅私有归档
archived_at: 2026-07-27
content_hash: 'sha256:0949732ee666e965'
translated: true
---

> 原文：[栈展开](https://maskray.me/blog/2020-11-08-stack-unwinding) · MaskRay（宋方睿）

[2020-11-08](https://maskray.me/blog/2020-11-08-stack-unwinding)

# 栈展开

2025 年 11 月更新。

栈展开的主要用途是：

- 为调试器、崩溃报告器、性能分析器、垃圾收集器等获取栈回溯。
- 使用 personality 例程和语言特定数据区实现 C++ 异常（Itanium C++ABIlanguage-specificABI）。请参阅[C++ 异常处理 ABI](https://maskray.me/blog/2020-12-12-c++-exception-handling-abi)

有些人用“栈遍历”指代获取栈回溯，而“栈展开”指代同时恢复被调用者保存寄存器的增强操作。在本文中，我们不区分这两者。callee-saved

栈展开任务可分为两类：

- 同步型：由程序自身触发，如 C++ 抛出异常、获取自身栈回溯等。此类栈展开仅发生在函数调用处（在函数体内，不会出现在序言/尾声区域中）
- 异步型：由垃圾收集器、信号或外部程序触发。此类栈展开可出现在函数序言/尾声区域中

，GCC 支持 `-fnon-call-exceptions`，但其行为不明确（[PR70387](https://gcc.gnu.org/bugzilla/show_bug.cgi?id=70387)该特性似乎已被已停用的 GNU

```plaintext
% cat a.cc
#include <stdio.h>
void nop() {}
int main() {
  int i = 0;
  int* volatile p = &i;
  try {
    nop();
    printf("%d\n", 1 / *p);
    nop();
  } catch (...) { puts("oops"); }
}
% g++ a.cc -o a -fnon-call-exceptions -fasynchronous-unwind-tables
% ./a
[1]    16959 floating point exception (core dumped)  ./a
```

## 机制

- 帧指针
- DWARF `.eh_frame`
- 其他展开格式
- 硬件辅助的栈遍历功能

## 帧指针

最经典也最简单的栈展开方式基于帧指针：固定一个寄存器作为帧指针（x86-64 上为 RBP），在函数序言中把旧帧指针保存到栈帧，再把帧指针更新为所保存帧指针所在的地址。当前帧指针与栈中保存的各级帧指针共同构成单链表。

```plaintext
pushq %rbp
movq %rsp, %rbp # after this, RBP references the current frame
...
popq %rbp
retq  # RBP references the previous frame
```

获取初始帧指针值（`__builtin_frame_address`）后，持续解引用帧指针即可获取所有栈帧的帧指针值。该方法不适用于序言/尾声中的某些指令。

注意：在 RISC-V 和 LoongArch 上，前一帧的帧指针保存在 `fp[-2]`，而不是 `fp[0]`。RISC-V 的相关讨论见[考虑标准化 fp 所指向的栈槽](https://github.com/riscv-non-isa/riscv-elf-psabi-doc/issues/18)。

以下代码适用于许多架构。可以启用 `-rdynamic`（`g++ a.cc -rdynamic`）来符号化全局函数名。1  
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
#include \<dlfcn.h\>  
#include \<stdio.h\>  
[[gnu::noinline]] void qux() {  
 void **fp = (void **)__builtin_frame_address(0);  
 for (;;) {  
#if defined(__riscv) || defined(__loongarch__)  
 void **next_fp = fp[-2], *pc = fp[-1];  
#elif defined(__powerpc__)  
 void **next_fp = fp[0];  
 void *pc = next_fp \<= fp ? 0 : next_fp[2];  
#else  
 void **next_fp = (void **)*fp, *pc = fp[1];  
#endif  
 printf("%p %p", next_fp, pc);  
 Dl_info info;  
 if (dladdr(pc, &info) && info.dli_sname)  
 printf(" %s + 0x%tx", info.dli_sname, (char *)pc - (char *)info.dli_saddr);  
 puts("");  
 if (next_fp \<= fp)  
 break;  
 fp = next_fp;  
 }  
}  
[[gnu::noinline]] void bar() { qux(); }  
[[gnu::noinline]] void foo() { bar(); }  
int main() { foo(); }

基于帧指针的方法很简单，但有几个缺点。

当上述代码以 `-O1` 或更高优化级别编译，并移除 `[[gnu::noinline]]` 属性后，`foo` 和 `bar` 会执行尾调用，程序输出中不会出现 `foo` 与 `bar` 的栈帧。`-fno-omit-frame-pointer` 不会抑制尾调用优化。

编译器默认采用 `-fomit-frame-pointer` 影响很大。许多目标在 `-O1` 或更高优化级别下默认使用 `-fomit-frame-pointer`，因此实际中不能保证所有库都含有帧指针。展开线程栈时，应在解引用 `next_fp` 前检查它是否像一个栈地址，以免发生段错误。

如果能够向目标线程注入代码，`pthread_attr_getstack` 可以取得栈边界，是检查页面可访问性的高效方法。

```c
pthread_attr_t attr;
void *addr = 0;
size_t size = 0;
pthread_getattr_np(pthread_self(), &attr);
pthread_attr_getstack(&attr, &addr, &size);
pthread_attr_destroy(&attr);
```

另一种方法是解析 `/proc/*/maps`，判断地址是否可读（速度较慢）。还有一个巧妙的方法：1  
2  
3  
4  
5  
6  
7  
8  
9  
#include \<fcntl.h\>  
#include \<unistd.h\>  
  
// 或使用管道的写端。
int fd = open("/dev/random", O_WRONLY);  
assert(fd \>= 0);  
if (write(fd, address, 1) \< 0)  
 // 不可读
close(fd);

在 Linux 上，`rt_sigprocmask`
2  
3  
4  
5  
6  
7  
8  
9  
#include \<errno.h\>  
#include \<fcntl.h\>  
#include \<syscall.h\>  
#include \<unistd.h\>  
  
errno = 0;  
syscall(SYS_rt_sigprocmask, ~0, address, (void *)0, /*sizeof(kernel_sigset_t)=*/8);  
if (errno == EFAULT)  
 // not readable

此外，为帧指针保留一个寄存器会增加文本大小并产生负面性能影响（序言、尾声的额外指令开销以及因少一个寄存器而造成的寄存器压力），在缺乏寄存器的 x86-32 上可能相当显著。在拥有相对充足寄存器的架构上，e.g. x86-64，性能损失可能非常小，比如 1%。

### 编译器行为

- 不维护 FP 链：`-fomit-frame-pointer -momit-leaf-frame-pointer`（开销最小）

    - 在某些目标上不会保留 FP，也就是说 FP 仍可分配给其他用途。
    - 另一些目标会保留 FP，例如 Clang 21 起的 Windows AArch64，以及使用 `-mframe-chain=aapcs` 或 `-mframe-chain=aapcs+laf` 的 AArch32。
- 为非叶函数维护 FP；叶函数保留 FP 寄存器但不执行 push/pop：`-fno-omit-frame-pointer -momit-leaf-frame-pointer`
- 为所有函数维护 FP：`-fno-omit-frame-pointer -mno-omit-leaf-frame-pointer`（开销最大）

在 Clang 支持的许多目标上，`-O` 隐式地包含了 `-fomit-frame-pointer`.

对于叶函数（那些不调用其他函数的函数），尽管仍然应保留帧指针寄存器以保证一致性，但 push/pop 操作通常是不必要的。编译器提供 `-momit-leaf-frame-pointer`（具有 target-specific 的默认值）来减小代码尺寸。

此优化的可行性取决于目标架构：

- 在 AArch64 上，返回地址在链接寄存器（X30）中可用。可以通过检查 X30 来获取直接调用者，因此 `-momit-leaf-frame-pointer` 不会影响展开。
- 在 x86-64 上，执行序言指令后，返回地址存储在 RSP 加上一个偏移量的位置。展开器需要知道栈帧大小才能取回返回地址，否则必须利用叶帧的 DWARF 信息，然后切换到父帧的 FP 链。

除了这一架构性考量外，在 `-momit-leaf-frame-pointer` 上使用 x86-64:

- 还有更多实际原因：hand-written 许多手动编写的汇编实现（包括大量 glibc 函数）没有建立帧指针，无论如何都会在帧指针链中造成缺口。
- 在序言序列 `push rbp; mov rbp, rsp` 中，第一条指令执行后，RBP 尚未引用当前栈帧。当启用了 shrink-wrapping 优化时，RBP 仍持有旧值的指令区域变大，增加了帧指针不可靠的时间窗口。

考虑到这些 trade-offs，出现了三种常见的配置：

GCC 8 已知会在 x86 上省略函数不需要帧记录时的帧指针（[i386：在没有栈访问时不使用帧指针](https://gcc.gnu.org/git/gitweb.cgi?p=gcc.git;h=8e941ae950ddce1745b4d6819a7131908dd7de24)）。有一个特性请求：[强制帧指针的选项](https://gcc.gnu.org/bugzilla/show_bug.cgi?id=98018).

的 shrink wrapping 优化（可通过 GCC 禁用），`-fno-omit-frame-pointer` 并不能确保在函数开头存在 `-fno-shrink-wrap`), `-fno-omit-frame-pointer`。`push rbp; mov rbp, rsp`

GCC 的 `-fschedule-insns2` 优化可能会在 `push rbp` 和 `mov rbp, rsp` 之间插入无关指令。（https://gcc.gnu.org/PR55667） 1  `mov rbp, rsp`. ([https://gcc.gnu.org/PR55667](https://gcc.gnu.org/PR55667)) 1  
2  
3  
4  
5  
// GCC 会为 aarch64 和 x86-64  
int f(int &, float);  
int g(int i, float t) {  
 return f(i, t) + f(i, t);  
}

GCC x86 存在[缺少使用 `-fno-omit-frame-pointer` 的优化 `-fno-omit-frame-pointer`](https://gcc.gnu.org/bugzilla/show_bug.cgi?id=108386).

GCC 的 s390x 移植可能会将链接寄存器和 FP 保存到叶函数中的 floating-point 寄存器。

## libunwind

C++ 异常以及性能分析器/崩溃报告器的栈展开通常使用 libunwindAPI 和 DWARF Call Frame Information。在 1990 年代，Hewlett-Packard 定义了一组 libunwindAPI，分为两类：

- `unw_*`：入口点是 `unw_init_local`（本地展开，当前进程）和 `unw_init_remote`（远程展开，其他进程）。通常使用 libunwind 的应用程序使用此 API。例如，Linux perf 会调用 `unw_init_remote`
- `_Unwind_*`：这部分已标准化为 Level 1：Base ABI of [Itanium C++ ABI: 异常处理](https://itanium-cxx-abi.github.io/cxx-abi/abi-eh.html)。Level 2 C++ ABI 会调用这些 `_Unwind_*` API。其中，`_Unwind_Resume` 是唯一直接由 C++ 编译代码调用的 API。`_Unwind_Backtrace` 被少数应用程序用来获取栈回溯。其他函数由 libsupc++/libc++abi 的 `__cxa_*` 函数和 `__gxx_personality_v0` 调用。

Hewlett-Packard 已开源[https://www.nongnu.org/libunwind/](https://www.nongnu.org/libunwind/)（此外还有许多名为 "libunwind" 的项目）。此 API 在 Linux 上的常见实现有：

- libgcc/unwind-*（`libgcc_s.so.1`* (`libgcc_s.so.1` 或 `libgcc_eh.a`）：实现了 `_Unwind_*` 并引入了一些扩展：`_Unwind_Resume_or_Rethrow, _Unwind_FindEnclosingFunction, __register_frame` 等。
- llvm-project/libunwind (`libunwind.so` 或 `libunwind.a`) 是 HP API 的一个简化实现，提供了部分 `unw_*`，但未实现 `unw_init_remote`。部分代码取自 ld64。如果使用 Clang，你可以使用 `--rtlib=compiler-rt --unwindlib=libunwind` 来选择
- glibc 对 `_Unwind_Find_FDE` 的内部实现，通常不导出，且与 `__register_frame_info`

## DWARF 调用帧信息

程序中不同地址区域所需的展开指令由 DWARF 调用帧信息（CFI）描述。在 ELF 平台上使用一种名为 `.eh_frame` 的变体。详见 [Linux 标准基础核心规范：通用部分](https://refspecs.linuxfoundation.org/lsb.shtml)。编译器、汇编器、链接器和 libunwind 都提供了相应支持。

`.eh_frame` 由公共信息条目（CIE）和帧描述条目（FDE）组成。CIE 包含以下字段：

- length（长度）：length 字段的大小加上 length 的值必须是地址大小的整数倍。
- CIE_id：常量 0，用于区分 CIE 与 FDE。在 FDE 中，该字段非零，表示 CIE_pointer
- version（版本）：常量 1（对于 GAS 的 RISC-V 移植版本为 3）。
- augmentation：以 NUL 结尾的字符串，用于描述 CIE/FDE 参数列表。

    - `z`：存在 augmentation_data_length 和 augmentation_data 字段，用于提供解释其余字节的参数
    - `P`：从 augmentation_data 中读取一个字节（编码）和一个由该编码决定长度的值，用来表示 personality 例程指针
    - `L`：从 augmentation_data 中读取一个字节，表示 FDE 中语言特定数据区（LSDA）的编码；FDE 的 augmentation 数据存放 LSDA
    - `R`：从 augmentation_data 中读取一个字节，表示 FDE 中 initial_location 与 address_range 的编码
    - `S`：关联的 FDE 描述一个信号帧（供 `unw_is_signal_frame` 使用）
- code_alignment_factor：假设指令长度为 2 或 4 的倍数（RISC），它是 `DW_CFA_advance_loc` 等参数的乘数
- data_alignment_factor：`DW_CFA_offset DW_CFA_val_offset` 等参数的乘数
- return_address_register：在 CIE 版本 3 及以上，从一个字节改为 ULEB128。
- augmentation_data_length：仅当 augmentation 包含 `z` 时存在。
- augmentation_data：仅当 augmentation 包含 `z` 时存在，用于提供描述 augmentation 的参数。对于 `P`，参数指定 personality（1 字节编码及编码后的指针）；对于 `R`，参数指定 FDE initial_location 的编码。
- initial_instructions：用于展开的字节码，是所有使用该 CIE 的 FDE 所共有的前缀
- padding（填充）

在 `.debug_frame` 版本 4 及以上中，存在 address_size（地址大小，4 或 8）和 segment_selector_size（段选择器大小）。`.eh_frame` 的 CIE 版本 1 没有这两个字段。（GAS 自 2019 年起支持使用 `--gdwarf-cie-version={1,3,4}` 来设置 CIE 版本。RISC-V 移植版本默认使用版本 3，以使 return_address_register 可以使用寄存器编号 \>= 256。版本 4 额外添加了 segment_selector_size，但此字段并无实际用途。）

每个 FDE 都关联一个 CIE。FDE 包含以下字段：

- length：FDE 本身的长度。若值为 0xffffffff，接下来的 8 个字节（extended_length）记录实际长度。除非刻意构造，否则不会使用 extended_length
- CIE_pointer：用当前位置减去 CIE_pointer，得到关联的 CIE
- initial_location：FDE 所描述的第一个位置的地址；该值通过引用节符号的重定位编码
- address_range：initial_location 与 address_range 共同描述一个地址范围
- augmentation_data_length：关联 CIE 的 augmentation 包含 `z` 时存在
- augmentation_data：关联 CIE 的 augmentation 包含 `z` 时存在

    - 如果关联 CIE 的 augmentation 包含 `L`，语言特定数据区会记录在这里
- instructions：用于展开的字节码，本质上是 (address, opcode) 对
- padding：填入足够的 `DW_CFA_nop` 指令（零值），使大小与 `length` 字段匹配。对于 64 位对象，最后一个 FDE 按 8 字节对齐，其他 FDE 按 4 字节对齐

CIE 可以选择引用文本节中的 personality 例程（`.cfi_personality` 指令）。FDE 可以选择引用 `.gcc_except_table` 中与它关联的 LSDA（`.cfi_lsda` 指令）。personality 例程与 LSDA 用于 Itanium C++ ABI 的第 2 层 C++ ABI。

`llvm-dwarfdump --eh-frame` 和 `objdump -Wf` 可以转储该节。`objdump -WF`（`--dwarf=frames-interp` 的简写）会给出表格形式的输出。

```plaintext
load "elf.pk";
load "dwarf-frame.pk";

type EhFrameCIE = struct {
  Dwarf_Initial_Length length;
  uint32 cie_id == 0;
  uint8 version;
  string augmentation;
  ULEB128 code_alignment_factor;
  LEB128 data_alignment_factor;
  ULEB128 return_address_register;
  if (strchr(augmentation, 'z') < augmentation'length)
    ULEB128 augmentation_length;
  if (strchr(augmentation, 'z') < augmentation'length)
    uint8[augmentation_length.value] augmentation_data;
  uint8[length.value + length'size - OFFSET] initial_instructions;
};

type EhFrameFDE = struct {
  Dwarf_Initial_Length length;
  uint32 cie_pointer;
  int32 initial_location; // augmentation 'R' decides the type
  int32 address_range; // augmentation 'R' decides the type
  uint8[length.value + length'size - OFFSET] instructions;
};

type EhFrameEntry = union {
  EhFrameCIE cie;
  EhFrameFDE fde;
};
```

### `.eh_frame` 与 `.debug_frame`

某些目标默认使用 `-fasynchronous-unwind-tables`，另一些则默认使用 `-fno-asynchronous-unwind-tables`。

以下是 GCC 和 Clang 的行为：1  
2  
3  
4  
5  
编译器选项 生成的节
-fasynchronous-unwind-tables -fexceptions .eh_frame  
-fno-asynchronous-unwind-tables -fexceptions .eh_frame  
-fasynchronous-unwind-tables -fno-exceptions .eh_frame  
-fno-asynchronous-unwind-tables -fno-exceptions none (-g0) or .debug_frame (-g1 and above)

`.eh_frame` 基于 DWARF v2 引入的 `.debug_frame`，但二者存在一些差异：

- `.eh_frame` 带有 `SHF_ALLOC` 标志（表示该节属于进程映像），`.debug_frame` 则没有，因此后者的使用场景很少。
- `.debug_frame` 支持 DWARF64 格式（即 64 位偏移，但体积稍大），`.eh_frame` 不支持；实际上可以扩展，只是没有需求。
- `.debug_frame` 的 CIE 使用 augmentation，而不使用 augmentation_data_length 和 augmentation_data。
- DWARF v5 没有提到 `.debug_frame` 的 FDE 中的 augmentation。
- CIE 中的版本字段不同。
- FDE 中的 CIE_pointer 含义不同：`.debug_frame` 使用节偏移（绝对值），`.eh_frame` 使用相对偏移。`.eh_frame` 的这一改动很巧妙。如果 `.eh_frame` 长度超过 32 位，`.debug_frame` 必须改用 DWARF64 才能表示 CIE_pointer；相对偏移则无需担心这一问题（FDE 与 CIE 的距离超过 32 位时，再增加一个 CIE 即可）。
- 在 `.eh_frame` 中，augmentation 总是包含 `zR`；对 AArch64/PowerPC64/x86-64 的小代码模型，FDE 编码通常为 `DW_EH_PE_pcrel|DW_EH_PE_sdata4`。GCC 中的 initial_location 占 4 字节（即使使用 `-mcmodel=large`）；`.debug_frame` 在 64 位架构上需要 8 字节 initial_location。因此 `.eh_frame` 通常小于等价的 `.debug_frame`。

对于两个其他方面等价的可重定位目标文件，一个使用 `.debug_frame`，另一个使用 `.eh_frame`，则 `size(.debug_frame)+size(.rela.debug_frame)` \> `size(.eh_frame)+size(.rela.eh_frame)`，前者可能大约多 20%。如果压缩 `.debug_frame`（`.eh_frame` 无法压缩），则 `size(compressed .debug_frame)+size(.rela.debug_frame) < size(.eh_frame)+size(.rela.eh_frame)`。

---

对于下面的函数：1  
2  
3  
void f() {  
 __builtin_unwind_init();  
}

编译器生成 `.cfi_*`（CFI 指令）来标注汇编代码；`.cfi_startproc` 与 `.cfi_endproc` 标记 FDE 区域，其他 CFI 指令描述展开规则。调用帧由栈上的一个地址表示，该地址称为规范帧地址（CFA），通常就是调用点的栈指针值。下面的示例展示 CFI 指令的用法：1  
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
f:
# 在函数入口处，CFA= rsp+8
 .cfi_startproc
# %bb.0:
 pushq %rbp
# 重新定义 CFA= rsp+16
 .cfi_def_cfa_offset 16
# rbp 保存在地址 CFA-16  
 .cfi_offset %rbp,_-16  
 movq %rsp, %rbp
# CFA= rbp+16。CFA 在 rsp 改变时无需重新定义
 .cfi_def_cfa_register %rbp
 pushq %r15
 pushq %r14
 pushq %r13
 pushq %r12
 pushq %rbx
# rbx 保存在地址 CFA-56  
 .cfi_offset %rbx,_-56  
 .cfi_offset %r12,_-48  
 .cfi_offset %r13,_-40  
 .cfi_offset %r14,_-32  
 .cfi_offset %r15,_-24  
 popq %rbx
 popq %r12
 popq %r13
 popq %r14
 popq %r15
 popq %rbp
# CFA= rsp+8
 .cfi_def_cfa %rsp, 8
 retq
.Lfunc_end0:
 .size f, .Lfunc_end0-f  
 .cfi_endproc

汇编器解析 CFI`.eh_frame` 指令并生成 `.eh_frame`（该机制由 Alan Modra 于 2003 年引入）。链接器收集 .o/.a 文件中的 `.eh_frame`. [输入段以生成输出](https://sourceware.org/git/?p=binutils-gdb.git;a=commit;h=9b8ae42e78e6c3e3bc67c31673233568c27d9e71), GNU。`.cfi_personality``.cfi_lsda`.

### `.eh_frame_hdr``PT_GNU_EH_FRAME`

和 FDE。`.eh_frame`FDE__CIEFDE[https://sourceware.org/pipermail/binutils/2001-December/015674.html](https://sourceware.org/pipermail/binutils/2001-December/015674.html)`.eh_frame_hdr`_FDE

```plaintext
type EhFrameHdr = struct {
  uint8 version;
  uint8 eh_frame_ptr_enc;
  uint8 fde_count_enc;
  uint8 table_enc;
  int32 eh_frame_ptr; // eh_frame_ptr_enc decides the type
  int32 fde_count; // fde_count_enc decides the type

  type Entry = struct {
    int32 initial_location; // table_enc decides the type
    int32 address; // table_enc decides the type
  };
  Entry[fde_count] table;
};
```

链接器会收集所有 `.eh_frame` 输入节。使用 `--eh-frame-hdr` 时，`ld` 生成 `.eh_frame_hdr`，并创建一个覆盖 `.eh_frame_hdr` 的 `PT_GNU_EH_FRAME` 程序头。展开器可以解析程序头，查找 `PT_GNU_EH_FRAME` 来定位 `.eh_frame_hdr`。下面给出一个示例。

Clang 和 GCC 通常会向 ld 传递 `--eh-frame-hdr`，例外是 `gcc -static` 不会传递 `--eh-frame-hdr`。这种差异是与 `__register_frame_info` 有关的历史选择。

GNU ld 只支持 `eh_frame_ptr_enc = DW_EH_PE_pcrel | DW_EH_PE_sdata4;`（PC 相对的 `int32_t`）、`fde_count_enc = DW_EH_PE_udata4;`（`uint32_t`），以及 `table_enc = DW_EH_PE_datarel | DW_EH_PE_sdata4;`（相对于 `.eh_frame_hdr` 的 `int32_t`）。（没有 FDE 时，GNU ld 也支持 `DW_EH_PE_omit`。）

当偏移超出 32 位范围时，ld.lld 23 支持对 `eh_frame_ptr_enc` 与 `table_enc` 使用 `DW_EH_PE_sdata8`，从而支持采用大代码模型的大型二进制文件。

( 1  
2  
3  
4  
5  
load "eh_frame_hdr.pk"  
load elf  
var efile = Elf64_File @ 0#B  
var hdr = efile.get_sections_by_name(".eh_frame_hdr")[0]  
printf "%Tv\\n", EhFrameHdr @ hdr.sh_offset  
 )

### `__register_frame_info`

在 `.eh_frame_hdr` 和 `PT_GNU_EH_FRAME` 出现之前，crtbegin（`crtstuff.c`）中有一个静态构造函数 `frame_dummy`，它调用 `__register_frame_info` 来注册可执行文件的 `.eh_frame`。

如今，`__register_frame_info` 只供使用 `-static` 链接的程序使用。相应地，如果链接时指定 `-Wl,--no-eh-frame-hdr`，就无法展开栈（若使用 C++ 异常，程序会调用 `std::terminate`）。

### libunwind 示例

```c
#include <libunwind.h>
#include <stdio.h>

void backtrace() {
  unw_context_t context;
  unw_cursor_t cursor;
  // Store register values into context.
  unw_getcontext(&context);
  // Locate the PT_GNU_EH_FRAME which contains PC.
  unw_init_local(&cursor, &context);
  size_t rip, rsp;
  do {
    unw_get_reg(&cursor, UNW_X86_64_RIP, &rip);
    unw_get_reg(&cursor, UNW_X86_64_RSP, &rsp);
    printf("rip: %zx rsp: %zx\n", rip, rsp);
  } while (unw_step(&cursor) > 0);
}

void bar() {backtrace();}
void foo() {bar();}
int main() {foo();}
```

如果使用 llvm-project/libunwind：1  
$CC a.c -Ipath/to/include -Lpath/to/lib -lunwind

如果使用 nongnu.org/libunwind，有两种选择：（a）在 `#include <libunwind.h>` 前加入 `#define UNW_LOCAL_ONLY`；（b）多链接一个库，在 x86-64 上是 `-l:libunwind-x86_64.so`。使用 Clang 时，也可以执行 `clang --rtlib=compiler-rt --unwindlib=libunwind -I path/to/include a.c`；除了提供 `unw_*` 外，这还能确保不链接 `libgcc_s.so`。

- `unw_getcontext`：获取寄存器值（包括 PC）
- `unw_init_local`

    - 使用 `dl_iterate_phdr` 遍历可执行文件和共享对象，找到包含 PC 的 `PT_LOAD` 程序头
    - 找到当前模块的 `PT_GNU_EH_FRAME`（`.eh_frame_hdr`），并保存到 `cursor` 中
- `unw_step`

    - 二分查找与 PC 对应的 `.eh_frame_hdr` 条目，记录找到的 FDE 及其指向的 CIE
    - 执行 CIE 中的 initial_instructions
    - 执行 FDE 中的指令（字节码）。一个自动机维护当前位置与 CFA：`DW_CFA_advance_loc` 推进位置，`DW_CFA_def_cfa_*` 更新 CFA，`DW_CFA_offset` 表示某寄存器的值保存在 CFA+offset 处
    - 当当前位置大于或等于 PC 时，自动机停止。换言之，已执行的指令是 FDE 指令的一个前缀

展开器根据程序计数器找到适用的 FDE，并执行程序计数器之前的所有 CFI 指令。

最常见的指令是：

- `DW_CFA_def_cfa_*`
- `DW_CFA_offset`
- `DW_CFA_advance_loc`

在 `-DCMAKE_BUILD_TYPE=Release -DLLVM_TARGETS_TO_BUILD=X86` 的 clang 构建中，`.text` 为 51.7 MiB，`.eh_frame` 为 4.2 MiB，`.eh_frame_hdr` 为 646 B。共有 2 个 CIE 和 82745 个 FDE.

### DWARF CFI 的备注 DWARF CFI

某些条件执行状态无法用 CFI 指令表达。例如，在下面的 `popne {some registers}` 和 `bne label` 之间的代码中，寄存器可能在栈上也可能不在栈上，而 DWARF CFI 无法表示这种场景。

```plaintext
// AArch32
cmp   this, that
popne {some registers}
...
bne   label
```

CFI 指令适合编译器生成代码，但在 hand-written 汇编中编写起来很繁琐。2015 年，Alex Dowad 为 musl libc 贡献了一个 awk 脚本，用于解析汇编并自动生成 CFI 指令。实际上，生成精确的 CFI 指令对编译器来说也很有挑战性。对于一个不使用帧指针的函数，调整 SP 需要输出一条 CFI 指令来重新定义 CFA. GCC。GCC 不解析内联汇编，因此在内联汇编中调整 SP 常常会导致不精确的 CFI.

```c
void foo() {
  asm("subq $128, %rsp\n"
  // Cannot unwind if -momit-leaf-frame-pointer
      "nop\n"
      "addq $128, %rsp\n");
}

int main() {
  foo();
}
```

在 glibc 中，[x86: 移除架构特定的低层级锁实现 arch-specific](https://sourceware.org/git/?p=glibc.git;a=commit;h=c50e1c263ec15e98da3235e663049156fd1afcfa) 移除了 `sysdeps/unix/sysv/linux/x86_64/lowlevellock.h`。该文件曾经执行类似如下的操作 1  
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
lll_lock(futex, private) \\  
 (void) \\  
 ({ int ignore1, ignore2, ignore3; \\  
 if (__builtin_constant_p (private) && (private) == LLL_PRIVATE) \\  
 __asm __volatile (__lll_lock_asm_start \\  
 "1:\\tlea %2, %%" RDI_LP "\\n" \\  
 "2:\\tsub $128, %%" RSP_LP "\\n" \\  
 ".cfi_adjust_cfa_offset 128\\n" \\  
 "3:\\tcallq __lll_lock_wait_private\\n" \\  
 "4:\\tadd $128, %%" RSP_LP "\\n" \\  
 ".cfi_adjust_cfa_offset -128\\n" \\  
 "24:" \\  
 : "=S" (ignore1), "=&D" (ignore2), "=m" (futex), \\  
 "=a" (ignore3) \\  
 : "0" (1), "m" (futex), "3" (0) \\  
 : "cx", "r11", "cc", "memory"); \\  
...

`.cfi_adjust_cfa_offset 128` 适用于以 RSP 作为 CFA 的帧，但不适用于 RBP。遗憾的是，很难保证某个帧不使用 RBP；即使指定 `-fomit-frame-pointer`，某些条件下也会切换到 RBP。

LLVM 的 CFIInstrInserter pass 可以插入 `.cfi_def_cfa_* .cfi_offset .cfi_restore`，调整 CFA 与被调用者保存寄存器。LLVM 的 [CFIFixup pass](https://reviews.llvm.org/D114545) 可以插入 `.cfi_restore_state .cfi_remember_state`。CFIFixup 生成的信息更节省空间，因此优先使用。

DWARF 方案的信息密度也很低，各种紧凑展开方案在这方面有所改进。举几个问题：

- CIE address_size：没有人会为同一架构使用不同值。即便真的这样做（例如 AArch64 和 x86-64 的 ILP32 ABI），这些信息也已能从别处获得。
- CIE segment_selector_size：设计者考虑到 x86 是好事，但如今 x86 自身已不再需要它 :/
- CIE code_alignment_factor 与 data_alignment_factor：有这种需要的 RISC 架构可以直接硬编码这些值。
- CIE return_address_register：我不知道一种架构为什么会想用不同寄存器保存返回地址。
- length：DWARF 的 8 字节形式显然设计过度。对于标准形式的序言/尾声，本不需要该字段。
- initial_location 与 address_range：如果总要使用二分查找索引表，为什么还需要长度字段？
- instructions：字节码很灵活，但函数的序言/尾声通常具有标准形式，少量被调用者保存寄存器可以用更紧凑的方式编码。
- augmentation_data：它带来了灵活性，但实际很少有函数需要 personality 与 LSDA 指针之外的信息。

FP 之外的被调用者保存寄存器通常并不需要，但没有编译器选项可以丢弃这些信息。

binutils 在 2024 年实现了[`as --scfi=experimental`](https://sourceware.org/binutils/wiki/gas/SCFI)，用于从 AArch64 和 x86 的汇编文件中生成 CFI 指令。

#### `SHT_X86_64_UNWIND`

`.eh_frame` 在链接器/动态加载器中有特殊处理，因此按惯例应使用独立的节类型，但在设计时使用了 `SHT_PROGBITS`。在 x86-64 psABI 中，`.eh_frame` 的类型是 `SHT_X86_64_UNWIND`（受 Solaris 影响）。

- 在 GNU as 中，`.section .eh_frame,"a",@unwind` 将生成 `SHT_X86_64_UNWIND`，而 `.cfi_*` 将生成 `SHT_PROGBITS`.
- 从 Clang 3.8 开始，`.cfi_*` 生成 `SHT_X86_64_UNWIND`

`.section .eh_frame,"a",@unwind` 很少见（可见于 glibc 的 x86 移植、libffi、LuaJIT 等软件包），因此检查 `.eh_frame` 的类型是区分 Clang/GCC 目标文件的好办法 :) 我为 ld.lld 11.0.0 提交了 [D85785](https://reviews.llvm.org/D85785)，允许可重定位链接中的 `.eh_frame` 混用不同类型 ;-)

对未来的架构的建议：在定义 processor-specific 节类型时，请不要将 0x70000001（`SHT_ARM_EXIDX=SHT_IA_64_UNWIND=SHT_PARISC_UNWIND=SHT_X86_64_UNWIND=SHT_LOPROC+1`）用于除展开以外的用途 :) `SHT_CSKY_ATTRIBUTES=0x70000001`:)

#### 链接器视角

通常，在 COMDAT 组和 `-ffunction-sections`, `.data`/`.rodata` 需要像 `.text` 那样进行拆分，但 `.eh_frame` 是整体的。与许多其他元数据节类似，整体节的主要问题是链接器中的垃圾回收具有挑战性。与某些其他元数据节不同，简单地放弃垃圾回收并非选择：

- `.eh_frame_hdr` 是一个二分查找索引表，重复/未使用的条目可能会混淆客户。
- `.eh_frame` 并不小。用户希望丢弃未使用的 FDE.

ld.lld 对 `.eh_frame` 有一些特殊处理：

- 在非可重定位链接中，`.eh_frame` 输入节表示为 `EhInputSection`，而不是常规 `InputSection`，以便执行子节处理：去重 CIE，并回收 FDE。
- `splitSections`，在 `markLive` 之前，将 `.eh_frame` 拆分成多个部分，为垃圾回收做准备。
- `markLive` 需要保留 `.eh_frame` 的各个部分。
- `combineEhSections` 合并存活的各个部分。
- 扫描重定位时，允许从 `.eh_frame` 重定位到因 COMDAT 组规则而丢弃之节中的 `STT_SECTION` 符号。通常不允许从组外发起这种 `STB_LOCAL` 重定位。
- 即使指定 `-z notext`，也不在 `.eh_frame` 中生成动态重定位。（[D143136](https://reviews.llvm.org/D143136)）
- `-M` 需要特殊代码。

链接器处理 `.eh_frame` 时，需要在概念上把 `.eh_frame` 拆成 CIE/FDE。ld.lld 会在为 `--gc-sections` 标记存活节之前拆分 `.eh_frame`，并分别处理 CIE 和 FDE：

- CIE 中的重定位会引用 personality 例程符号，因此应标记这些例程。personality 例程通常不会被其他方式引用，如果扫描 CIE 重定位时不保留，就会被丢弃。
- FDE 中的重定位可能引用代码函数（通过 initial_location）和 LSDA（通过 augmentation_data）。代码函数（由 `SHF_EXECINSTR` 标志识别）不会被标记；既不属于节组、也不带 `SHF_LINK_ORDER` 标志的 LSDA 会被标记。

ld.lld 会合并相同的 CIE。

GNU ld 和 gold 支持 `--ld-generated-unwind-info`，可为 PLT 条目合成 CFI。这能提高 CFI 覆盖率，但我认为如今基本已经过时。参见 [GNU 风格链接器选项详解中的 `--no-ld-generated-unwind-info`](https://maskray.me/blog/2020-11-15-explain-gnu-linker-options)。注意，这种机制不适用于范围扩展 thunk（同样是链接器合成的代码）。

使用 `--icf` 时，两个文本节的内容与重定位可能相同，但 LSDA 不同，例如两个函数含有不同类型的 catch 块，因此不能合并。为简化处理，可以把[所有由 LSDA 引用的文本节](https://reviews.llvm.org/D84610)标记为不参与 ICF。

## 紧凑展开信息

Apple 设计了紧凑展开格式用于同步展开，自 2009 年的 Mac OS X 10.6 起已投入生产使用。虽然没有正式文档，但你可以查看 [The Apple Compact Unwinding Format: Documented and Explained](https://faultlore.com/blah/compact-unwinding/).

llvm-project 源码：`llvm/lib/MC`, `lld/MachO/UnwindInfoSection.cpp`, `libunwind/src/CompactUnwinder.hpp`, `lldb/source/Symbol/CompactUnwindInfo.cpp`

**编译器输出。** LLVM 在 `__LD,__compact_unwind` 段中生成“紧凑展开组描述”记录。在 arm64 平台上，`__eh_frame` 可以从编译器输出中省略。([D12258 和 OmitDwarfIfHaveCompactUnwind](https://reviews.llvm.org/D122258))

```plaintext
// Compiler output: a single unwind group descriptor in __LD,__compact_unwind
.quad _foo
.set L1, Lfoo_end-_foo
.long L1
.long compact_unwind_description
.quad personality
.quad lsda_address
```

**链接器处理。** “紧凑展开组描述”记录并不紧凑——8 字节字段可以进一步压缩。链接器合并来自输入文件的组描述符，并构建 `__TEXT,__unwind_info`（紧凑展开信息）。在典型的可执行文件中，大部分展开信息位于 `__unwind_info`，`__eh_frame` 则非常小（如果存在的话）。

紧凑展开格式基于以下几个关键原则：

- **标准序言/尾声编码：** 大多数函数都有常规的序言和尾声。在一定的代码生成限制下（例如寄存器保存顺序固定、序言/尾声中没有无关指令），它们可以用一个 32 位描述符编码。不维护帧指针链的函数需要更严格的序言和尾声指令。少数无法以这种方式编码的情况会回退到 DWARF CFI。
- **两级页表结构：** 这可以进一步压缩 32 位描述符，并支持高效查找。

    - 节头可以引用任意数量的页。每页为 4096 字节，可描述数百个条目。
    - 页头由一个通用的一级头和一个常规或压缩的二级头组成。
    - 一级头连续存放在 personality 例程之后。一级头描述该页映射的首个地址（使条目能使用更小的相对地址）、二级头的偏移量，以及 LSDA 数组中的基准偏移量。注意，一个一级头只指向一个二级头。
    - 二级头存放在各自的 4096 字节页内，后面紧跟其条目。（头字段 `entryPageOffset` 是常量。）
    - 压缩二级格式可以为常用描述符使用局部调色板。
- **压缩页条目：** 在使用压缩二级头部的页面中，条目编码了一个 24 位相对指令地址和一个 8 位描述符索引。
- **独立的 LSDA 存储：** LSDA 条目以 8 字节的 (function_offset, lsda_offset) 对单独存储。这种设计针对无 LSDA 的情况做了优化，但当超过 50% 的条目需要 LSDA 时开销较大。[粗略估算](https://discourse.llvm.org/t/rfc-improving-compact-x86-64-compact-unwind-descriptors/47471/20)表明当前方法仍然有益。

**紧凑展开描述符。** 这在 `libunwind/include/mach-o/compact_unwind_encoding.h` 中被称为“编码”。“The Apple Compact Unwinding Format: Documented and Explained”称之为“操作码”。

- `unwind_info_section_header::commonEncodingsArraySectionOffset` 指向一个全局调色板，其中包含常用的紧凑展开描述符。
- 常规页面直接与条目地址一起存储紧凑展开描述符。
- 压缩页面使用本地调色板，以更高效地存储紧凑展开描述符。

**描述符编码。** `__TEXT,__unwind_info` 中的紧凑展开描述符编码如下：1  
2  
3  
4  
5  
6  
7  
uint32_t mode_specific_encoding : 24; // 随模式而变化  
  
uint32_t mode : 4; // UNWIND_X86_64_MODE_MASK == UNWIND_ARM64_MODE_MASK  
  
uint32_t has_lsda : 1;  
uint32_t personality_index : 2;  
uint32_t is_not_function_start : 1;

personality 例程编码为一个 2 位索引，其中索引 0 表示没有 personality。仅为 personality 例程保留 3 个条目，C++ 和 ObjC 占用其中 2 个。自 2023 年以来，LLVM [默认对非规范 personality 例程回退到 DWARF](https://github.com/llvm/llvm-project/commit/e60b30d5e3878e7d91f8872ec4c4dca00d4a2dfc)。

在 `.gcc_except_table` 中，call site 偏移量和 landing pad 偏移量是相对于 `.cfi_lsda` 指令位置（通常是函数起始地址）的。当一个函数拥有多个紧凑展开描述符并使用单个 `.cfi_lsda` 指令，且 Itanium C++ABI 第一级展开器找到了一个并非第一个的描述符时，它需要向后扫描以找到函数起始地址。

### x86-64 模式

定义了五种模式：

- 0：保留
- 1：基于 FP 的帧：RBP 是帧指针，帧大小可变
- 2：基于 SP 的帧：不使用帧指针，帧大小在编译期间固定
- 3：大型基于 SP 的帧：不使用帧指针，帧大小在编译期间固定，但该值很大，无法用模式 2 表示
- 4：DWARF CFI 转义

**基于 FP 的帧（`UNWIND_X86_64_MODE_RBP_FRAME`）**

模式特定编码如下：1  
2  
3  
uint32_t regs : 15; // 最多 5 个已保存寄存器  
uint32_t : 1; // 0  
uint32_t frame_offset : 8; // 首个已保存寄存器位于 [RBP-8*frame_offset]

x86-64 上的被调用者保存寄存器为 RBX、R12、R13、R14、R15 和 RBP，其中 RBP 无需再次保存。3 位可以编码一个寄存器，15 位可以编码一个由 5 个寄存器组成的序列。

**基于 SP 的帧，立即数（`UNWIND_X86_64_MODE_STACK_IMMD`）**

模式特定编码如下：1  
2  
3  
4  
uint32_t reg_permutation : 10;  
uint32_t cnt : 3;  
uint32_t : 3;  
uint32_t size : 8;

cnt 表示已保存寄存器的数量（最多 6 个）。reg_permutation 表示已保存寄存器的序列号。size*8 表示栈帧大小。

**基于 SP 的帧，间接数（`UNWIND_X86_64_MODE_STACK_IND`）**

模式特定编码如下：1  
2  
3  
4  
uint32_t reg_permutation : 10;  
uint32_t cnt : 3;  
uint32_t adj : 3;  
uint32_t size_offset : 8;

与基于 SP 的帧类似。特别之处在于，栈帧大小从代码节中读取。RSP 调整量通常由 `subq imm, %rsp` 表示，而 size_offset 表示该指令与函数起始位置之间的距离。实际栈大小还包括 adj*8。

**DWARF CFI 转义（`UNWIND_X86_64_MODE_DWARF`)**

如果由于各种原因无法用紧凑展开描述符表示，就必须回退到 DWARF CFI。

### ARM64 模式

**SP-based 帧（`UNWIND_ARM64_FRAMELESS`)**

**DWARF CFI 转义（`UNWIND_ARM64_MODE_DWARF`)**

**FP-based 帧（`UNWIND_ARM64_FRAME`)**

### 缺乏对异步栈回溯的支持

在当前的 LLVM 实现中，每个函数仅由一个紧凑展开描述符表示。

对于发生在基于 RSP 的帧序言中的栈遍历请求，跟踪器可以使用 PC 偏移量和已保存寄存器推断规范帧地址。然而，如果序言中出现无关指令，这种方法就会失效。LLVM 会确保其中没有此类无关指令。

当启用了收缩包装时，序言可能不在函数的起始位置。由于当前描述符并未描述序言的偏移量，因此在这种情况下无法正确执行展开。

类似地，如果异步栈遍历请求出现在并非函数末尾处的尾声（由尾部复制优化导致），SP 调整则未被描述，从而导致规范帧地址计算错误。当前，尾部复制会跳过 CFI 指令（参见 [https://reviews.llvm.org/D40979](https://reviews.llvm.org/D40979)).

基于 FP 的帧较少遇到此类问题。Apple 的 arm64 平台要求使用帧指针，从根本上避免了许多此类问题。

总体而言，这一限制受到关注较少，很可能是因为分析器只会损失一小部分分析精度。

### 异步展开扩展

事实上，只要使用多个描述符描述函数的各个区域，仍然可以准确展开。OpenVMS 基于 ELF 的 x86-64 移植也采用了这种格式，详见其《VSI OpenVMS Calling Standard》和 2018 年的文章 [[RFC] Improving compact x86-64 compact unwind descriptors](https://lists.llvm.org/pipermail/llvm-dev/2018-January/120741.htm)。遗憾的是，他们没有开源该实现。

此方法基于合理假设：

- 任何对保留寄存器的使用必须延迟到所有保留寄存器都已保存之后。
- 在具有基于 RBP 的帧的函数中，序言必须包含相邻的 `push rbp; mov rbp, rsp` 指令，尾声必须包含相邻的 `mov rsp, rbp; pop rbp` 指令。
- 对于带有异常处理函数的收缩包装优化，可能引发异常的指令（浮点异常与访问违规）不能移入序言。

然后，它重新利用 `length` 字段：

- 单个展开组描述一个（prologue_start_offset, prologue_size, epilogue_is_present）元组。

    - 2025 年的讨论建议用 `epilogue_end` 取代 `epilogue_is_present`，表示寄存器保存序列结束位置与下一个描述符起始位置之间的间隔大小。
- 序言在概念上分为两部分：第一部分延伸到并包括减小 RSP 的那条指令；第二部分延伸到最后一个保留寄存器保存之后、但在任何保留寄存器被修改之前的位置（此位置不唯一，从而提供灵活性）。

    - 在序言中展开时，可以根据 PC 和已保存寄存器集合推断 RSP 寄存器值。
- 由于寄存器恢复是幂等的（在展开过程中多次恢复保留寄存器不会造成损害），因此无需描述 `pop $reg` 序列。展开组只需一个位来描述是否存在 1 字节的 `ret` 指令。
- 紧凑展开组描述符中的 `length` 字段被重新利用来描述序言的两个部分。
- 通过组合多个展开组，并可能使用零大小的序言或省略尾声中的 `ret` 指令，可以描述采用收缩包装或尾部复制优化的函数。
- 空帧组（无序言或尾声）是默认值，可用于描述跳板与 PLT 存根。

该提案未说明如何在 `-ffunction-sections` 构建中编码函数。为单个函数使用两个展开组代价过高。

```plaintext
f0:
  ...
  ret

  .p2align 4
f1:
  ...
  ret
```

**新一代紧凑展开信息**

aengelke 在[一篇 discourse 讨论](https://discourse.llvm.org/t/rfc-improving-compact-x86-64-compact-unwind-descriptors/47471/11?u=maskray) 中建议将 mode-specific 编码从 24 位增至 32 位。结合序言起点、尾声终点、异常处理函数和模式字段，可构成一个 64 位的紧凑展开描述符。

我们可以更新 `.eh_frame_hdr`，使用 12 字节结构同时编码 32 位地址和 64 位紧凑展开描述符。紧凑展开描述符通过特殊的 `mode` 支持 DWARF CFI 转义，因此可消除已被紧凑展开描述符取代的 `.eh_frame` FDE。

一个可选的分页表可以消除 32 位地址限制，并实现对紧凑展开描述符的去重。

```cpp
struct CompactUnwindDescriptor {
  uint64_t reserved : 11;
  // Offset of prologue start into function; -1 implies no prologue.
  // The linker can fold NULL descriptors into non-(-1) prologue_start.
  uint64_t prologue_start : 7;
  // Number of bytes after the end of the register-restore sequence
  // before the beginning of the next descriptor.
  uint64_t epilogue_end : 6;
  // Index into personality function table. 0 implies no personality.
  uint64_t personality_fn : 4;
  // Descriptor mode. 0 means a null frame. 1 means DWARF CFI escape.
  // Other values are arch-specific.
  uint64_t mode : 4;

  // Architecture and mode-specific encoding.
  uint32_t mode_specific_encoding;
};

// RBP-based frame
  /// Size of the prologue, marks the point where all CSRs are saved.
  uint64_t prologue_size : 8;
  /// Saved registers. Details to be discussed. A simple format would be
  /// one bit in the sequence rbp,r15,r14,r13,r12,rbx, indicating whether
  /// it is saved (that'd require just 6 bits).
  uint64_t saved_regs : 24;

// RSP-based frame
  /// Size of the stack frame * 16 (ABI requires 16B alignment).
  /// There is no need for a large frame mode, this currently covers
  /// 16 MiB, which should be enough. (Compilers can use the RBP mode
  /// or DWARF if they require larger stack frames.)
  uint64_t frame_size : 20;
  /// TBD: Specification of alternative push/pop sequence for APX.
  uint64_t is_apx : 1;
  /// TBD: Specification of instruction sequence for -fstack-clash-protection
  uint64_t with_scp : 1;
  /// TBD: I'm sure I forgot things we might need to handle.
  uint64_t reserved : 2;
  /// One bit in the sequence rbp,r15,r14,r13,r12,rbx, indicating whether
  /// it is saved (that'd require just 6 bits). I.e., the first saved reg
  /// of this list is at [CFA-16], the second at [CFA-24], etc.
  /// Maybe we need more options for IPRA, I'm unsure, so I added two
  /// unused bits for now.
  uint64_t saved_regs : 8;
```

**基线实现**

2025 年 11 月，我创建了一个分支，将紧凑展开信息移植到 ELF 作为基准。[https://github.com/MaskRay/llvm-project/tree/demo-unwind](https://github.com/MaskRay/llvm-project/tree/demo-unwind)

**X86 后端**

- 将 Mach-O 紧凑展开代码泛化，使其也适用于 ELF 目标。
- 添加 "epilog-cfi" 选项以允许禁用尾声 CFI（Darwin 上会禁用；参见 https://reviews.llvm.org/D42848）。当前的紧凑展开代码无法处理 `popq %rbp; .cfi_def_cfa %rsp, 8; ret`

**集成汇编器**

- 为紧凑展开生成带有扩充字符 'C' 的 .eh_frame CIE
- 用 64 位展开描述符取代 FDE 指令（从 Mach-O 的 32 位格式扩展而来，以支持未来的异步展开）
- 扩充字符 'C' 机制应视为实验性。作为先例，MIPS 紧凑异常表改用单独的 `.eh_frame_entry` 节。

**链接器 (lld)**

- 将 FDE 分为两组：基于描述符的（扩充字符 'C'）和基于指令的
- 当存在紧凑 FDE 时，生成版本 2 的 .eh_frame_hdr，其中使用 12 字节表项：(pc_ptr, unwind_descriptor_or_fde_ptr)
- TODO：将 LSDA 放入独立的存储区

**其他工具**

- llvm-readelf --unwind：转储 .eh_frame_hdr 和 .eh_frame 中的展开描述符
- llvm-dwarfdump --eh-frame：识别 .eh_frame CIE 中的扩充字符 'C'

当前的 `.eh_frame_hdr` 格式（TODO：需要彻底调整）

```plaintext
uint32_t version; // 2
uint32_t eh_frame_ptr_enc; // DW_EH_PE_pcrel | DW_EH_PE_sdata4
uint32_t fde_count_enc; // DW_EH_PE_udata4
uint32_t table_enc; // DW_EH_PE_datarel | DW_EH_PE_sdata8
uint32_t eh_frame_ptr; // offset to .eh_frame
uint32_t fde_count;

struct { uint32_t pc_ptr; uint64_t unwind_desc_or_fde_ptr; } entries[];
// TODO struct { uint32_t pc_ptr; uint32_t lsda_ptr; } lsda[];
```

**AArch64**

[https://www.codalogic.com/blog/2022/10/20/Aarch64-Stack-Frames-Again](https://www.codalogic.com/blog/2022/10/20/Aarch64-Stack-Frames-Again) 使用以下示例展示了 GCC 和 Clang 生成的不同栈帧：

```cpp
#include <string>
#include <iostream>

std::string merge( std::string a, std::string b, std::string c ) {
    std::string d = a + b;
    std::string e = a + d + b;
    return d + e;
}
```

**RISC-V**

`-msave-restore` 可能生成库调用，在序言和尾声代码中保存和恢复非易失性寄存器。紧凑展开实现需要考虑这种情况。

Zcmp 扩展（主要面向嵌入式 CPU）提供了保存和恢复 ra 及 s{0-11} 的指令。然而，寄存器保存顺序[与 `-fno-omit-frame-pointer` 不兼容](https://github.com/riscvarchive/riscv-code-size-reduction/issues/194)。Xqccmp 是 Zcmp 的一个变体，与 `-fno-omit-frame-pointer` 兼容。

GCC 和 Clang 会生成多条 `addi sp, sp, imm` 指令来调整栈指针。这使得支持异步紧凑型展开信息变得具有挑战性。1
2  
void bar(int *);  
void foo() { int x[1101]; bar(x); }

## ARM 异常处理

分为 `.ARM.exidx` 和 `.ARM.extab`

`.ARM.exidx` 是用于二分查找的索引表，由双字条目组成。第一个字是指向区域起始位置的 31 位 PC 相对偏移量。第二个字用下面的程序描述更清楚：1
2  
3  
4  
5  
6  
7  
8  
9  
if (indexData == EXIDX_CANTUNWIND)  
 return false; // 类似缺失 .eh_frame 条目；若发生 C++ 异常则调用 std::terminate  
if (indexData & 0x80000000) {  
 extabAddr = &indexData;  
 extabData = indexData; // 内联
} else {
 extabAddr = &indexData + signExtendPrel31(indexData);  
 extabData = read32(&indexData + signExtendPrel31(indexData)); // 存储在 .ARM.extab  
}

`tableData & 0x80000000` 表示紧凑模型条目，否则表示通用模型条目。

`.ARM.exidx` 相当于增强的 `.eh_frame_hdr`，紧凑模型相当于在 `.eh_frame` 中内联 personality 和 LSDA。考虑以下三种情况：

- 如果不会触发 C++ 异常，也不会调用可能抛出异常的函数：不需要 personality，只需一个 `EXIDX_CANTUNWIND` 条目，也不需要 `.ARM.extab`
- 如果触发 C++ 异常但不需要着陆垫：personality 为 `__aeabi_unwind_cpp_pr0`，只需一个紧凑模型条目，也不需要 `.ARM.extab`
- 如果存在 catch：`__gxx_personality_v0` 是必需的，`.ARM.extab` 是必需的

`.ARM.extab` 相当于合并的 `.eh_frame` 和 `.gcc_except_table`.

AArch64 没有对应的 `.ARM.extab`。有关功能请求，请参见 [https://github.com/ARM-software/abi-aa/issues/344](https://github.com/ARM-software/abi-aa/issues/344)。

### 通用型模型

```c
uint32_t personality; // bit 31 is 0
uint32_t : 24;
uint32_t num : 8;
uint32_t opcodes[];   // opcodes, variable length
uint8_t lsda[];       // variable length
```

仍在构建中。

## x86-64 异常处理

[https://learn.microsoft.com/en-us/cpp/build/exception-handling-x64?view=msvc-170](https://learn.microsoft.com/en-us/cpp/build/exception-handling-x64?view=msvc-170)

`MSVC /d2epilogunwind` 启用 Windows x64 Unwind V2 信息。

另请参阅 `llvm/lib/Target/X86/X86WinEHUnwindV2.cpp`。如果存在 `.seh_endepilogue`，则在尾声中的第一个 POP 之前添加 `.seh_unwindv2start`；如果没有这样的 POP，则在 `seh_endepilogue` 之前添加。该指令会生成一个 `UOP_Epilog` 代码。

## ARM64 异常处理

更新：[ARM64 帧展开代码详情](https://www.corsix.org/content/windows-arm64-unwind-codes)

请参阅 [https://docs.microsoft.com/en-us/cpp/build/arm64-exception-handling](https://docs.microsoft.com/en-us/cpp/build/arm64-exception-handling)，这是我最喜欢的编码方案。它支持从序言或尾声中间开始展开，也支持函数片段（用于表示收缩包装等非常规栈帧）。

信息保存在 `.pdata` 和 `.xdata` 两个节中。

```c
uint32_t function_start_rva;
uint32_t Flag : 2;
uint32_t Data : 30;
```

规范形式的函数使用压缩展开数据，不需要 `.xdata` 记录；无法用压缩展开数据表示的描述符则存储在 `.xdata` 中。

### 压缩展开数据

```c
uint32_t FunctionStartRVA;
uint32_t Flag : 2;
uint32_t FunctionLength : 11;
uint32_t RegF : 3;
uint32_t RegI : 4;
uint32_t H : 1;
uint32_t CR : 2;
uint32_t FrameSize : 9;
```

## MIPS 紧凑异常表

该规范可在[https://github.com/itanium-cxx-abi/cxx-abi/blob/main/MIPSCompactEH.pdf](https://github.com/itanium-cxx-abi/cxx-abi/blob/main/MIPSCompactEH.pdf).

Binutils 于 2015 年[提供了支持](https://sourceware.org/cgit/binutils-gdb/commit/?id=2f0c68f23bb3132cd5ac466ca8775c0d9e4960cd)，但[GCC 补丁](https://inbox.sourceware.org/gcc-patches/FD3DCEAC5B03E9408544A1E416F112420192C8DEFB@NA-MBX-04.mgc.mentorg.com/)仍未合并。

以下基于我对该格式的理解。

**编译器输出。** 指令 `.cfi_sections .eh_frame_entry` 告知汇编器向 `.eh_frame_entry` 节发出索引表条目。然后，可以使用 `.cfi_fde_data` 和 `.cfi_inline_lsda` 指令。[`.cfi_fde_data opcode1, ...`](https://sourceware.org/binutils/docs/as/CFI-directives.html) 位于一对 `.cfi_startproc` 和 `.cfi_endproc` 之间，描述帧展开操作码，每个操作码占用一个字节。帧展开操作码描述了序言指令的语义，类似于 WindowsARM64 帧展开码。

**汇编器处理。** 为每个包含紧凑展开信息的节生成一个 `.eh_frame_entry.*` 节。每个 `.eh_frame_entry` 是一个 4 字节对，其中第一个字类似于 `.eh_frame_hdr` 条目中的第一个字。一个 `.eh_frame_entry` 条目采用以下三种形式之一：

- 内联紧凑：`(even pc, unwind_data)`。当最多有 3 个操作码（3 字节）且没有个性例程时，可使用此形式。
- Out-of-line 紧凑：`(odd pc, even unwind_ptr)` 其中 `unwind_ptr` 指向 `.gnu_extab` 节中的展开数据。
- 传统：`(odd pc, odd legacy_unwind_ptr)` 其中 `legacy_unwind_ptr` 指向传统 `.eh_frame` 节。

TODO：描述 `.cfi_inline_lsda`，它似乎与 `__gnu_compact_pr[1-3]` 有关。

**链接器处理。** GNU ld 将 `.eh_frame_entry` 和 `.eh_frame_entry.*` 节连接起来，并按地址排序。以下内部链接器脚本片段在条目之前添加了一个头部：

```plaintext
.eh_frame_hdr   : { *(.eh_frame_hdr) *(.eh_frame_entry .eh_frame_entry.*) }
```

尽管节名仍保留传统的 `.eh_frame_hdr`，但版本已设置为 2。`.eh_frame_hdr` 由传统的 `PT_GNU_EH_FRAME` 程序头覆盖。链接器还定义符号 `__GNU_EH_FRAME_HDR` 以持有 `.eh_frame_hdr` 地址。

TODO：描述 LSDA 表示，它比传统的 `.gcc_except_table` 节更紧凑。

虽然当前实现似乎仅支持同步展开，但自然可以扩展到异步展开。[https://inbox.sourceware.org/gcc-patches/55F0C4D5.6080507@redhat.com/](https://inbox.sourceware.org/gcc-patches/55F0C4D5.6080507@redhat.com/) 表明可以引入操作码来描述 `DW_CFA_remember_state`/`DW_CFA_restore_state`。TODO：这可能类似 Windows ARM64 中的 `END_C`，用于仍有展开状态但长度为零的序言。

## Linux 内核 ORC 展开表

对于 x86-64，Linux 内核使用自己的展开表：ORC。你可以在[https://www.kernel.org/doc/html/latest/x86/orc-unwinder.html](https://www.kernel.org/doc/html/latest/x86/orc-unwinder.html) 和 lwn.net 上找到其文档，另外还有一篇[ORC 即将到来](https://lwn.net/Articles/728339/).

objtool 会解码指令并分析调用帧信息。指定 `--orc` 时（例如 `tools/objcopy/objtool --orc --link vmlinux.o`），objtool 会生成 `.orc_header`、`.orc_unwind` 和 `.orc_unwind_ip`。对于由以下代码汇编而成的目标文件：1
2  
3  
4  
.globl foo
.type foo, @function
foo:
 ret

展开信息会在两个地址发生变化：foo 的起始位置和结束位置，因此会生成 2 个 ORC 条目。如果 DWARF CFA 在函数中间发生变化（例如由于 push/pop 操作），则可能产生更多条目。

`.orc_unwind_ip` 包含两个条目，代表 PC-relative 地址。1
2  
3  
4  
重定位节 'rela.orc_unwind_ip' 位于偏移量 0x2028 处，包含 2 个条目：
 偏移量 信息                类型              符号的值        符号名称       + 加数
0000000000000000 0000000500000002 R_X86_64_PC32 0000000000000000 .text + 0
0000000000000004 0000000500000002 R_X86_64_PC32 0000000000000000 .text + 1

`.orc_unwind` 包含两个类型为 `orc_entry` 的条目。这些条目编码了上一帧的 IP/SP/BP 的存储方式。1
2  
3  
4  
5  
6  
7  
8  
struct orc_entry {  
 s16 sp_offset; // sp_offset 和 sp_reg 编码上一帧 SP 的存储位置  
 s16 bp_offset; // bp_offset 和 bp_reg 编码上一帧 BP 的存储位置  
 unsigned sp_reg:4;
 unsigned bp_reg:4;
 unsigned type:2; // 上一帧 IP 的存储方式
 unsigned end:1;
} __attribute__((__packed__));

你可能会发现，此方案与 Apple 紧凑展开描述符中的 `UNWIND_MODE_BP_FRAME` 和 `UNWIND_MODE_STACK_IMMD` 很相似。ORC 方案使用 16 位整数，因此推测不需要 `UNWIND_MODE_STACK_IND`。展开时，除 BP 外的大多数被调用者保存寄存器都用不到，所以 ORC 不会记录它们。

链接器会解析 `.orc_unwind_ip` 中的重定位，并创建 `__start_orc_unwind_ip/__stop_orc_unwind_ip/__start_orc_unwind/__stop_orc_unwind` 符号来界定节内容。随后，主机工具 `scripts/sorttable` 会对 `.orc_unwind_ip` 和 `.orc_unwind` 的内容排序。为展开一个栈帧，`unwind_next_frame` 会：

- 在 `.orc_unwind_ip` 表中进行二分查找，以确定相关的 ORC 条目
- 使用当前 SP、`orc->sp_reg` 和 `orc->sp_offset` 取得上一帧的 SP。
- 使用 `orc->type` 和其他值取得上一帧的 IP。
- 使用当前 BP、上一帧的 SP、`orc->bp_reg` 和 `orc->bp_offset` 取得上一帧的 BP。`bp->reg` 可以是 `ORC_REG_UNDEFINED/ORC_REG_PREV_SP/ORC_REG_BP`。

## SFrame

SFrame 是从 ORC 展开表扩展而来的栈遍历格式，预期用于性能分析器。然而，它牺牲了一些功能（例如 personality、LSDA、被调用者保存寄存器），不适用于 C++ 异常。此外，其栈偏移量不如 `.eh_frame` 的字节码式 CFI 指令紧凑。

另请参阅[关于 SFrame 的评论](https://maskray.me/blog/2025-09-28-remarks-on-sframe)。

### LLVM

在 LLVM 中，`Function::needsUnwindTableEntry` 决定是否应发出 CFI 指令：`hasUWTable() || !doesNotThrow() || hasPersonalityFn()`

在 ELF 目标上，如果函数具有 `uwtable` 或 `personality`，或者没有 `nounwind`（即 `needsUnwindTableEntry`），模块会被标记为需要 `.eh_frame`。随后，如果指定了 `needsUnwindTableEntry` 或 `-g[123]`，该函数就会获得 `.eh_frame`。

若要确保没有 `.eh_frame`，每个函数都需要 `nounwind`.

`uwtable(sync)` 和 `uwtable(async)` 指定展开信息的量。（参见 [[RFC] 异步展开表特性](https://lists.llvm.org/pipermail/llvm-dev/2021-November/153768.html).

如果没有生成 `.eh_frame`，但至少一个函数使 `Function::needsUnwindTableEntry` 返回 true，则在 `llvm::MachineModuleInfo::DbgInfoAvailable` 为 true 或指定 `-fforce-dwarf-frame` 时生成 `.debug_frame`。

`lib/CodeGen/AsmPrinter/AsmPrinter.cpp:352`

### 结语

对于未来应如何针对性能分析发展栈展开策略，仍有待解决。我们至少有 3 条路线：

- 紧凑展开方案。
- 硬件辅助。借助影子调用栈之类的安全加固功能。但这不太可能提供关于 callee-saved 寄存器的更多信息。
- 主要基于 FP。人们因为性能损失而避免使用 FP。如果 `-fno-omit-frame-pointer -mno-omit-leaf-frame-pointer` 对性能影响不大，它可能比 `.eh_frame` 中的某些信息更合适。展开信息可以用来填补空缺，例如处理收缩包装。

展开信息很难达到 100% 的覆盖率。链接器生成的代码（PLT 和范围扩展桩）通常没有展开信息覆盖。
