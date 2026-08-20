---
title: 全面了解 LeakSanitizer
source: MaskRay (宋方睿)
source_key: maskray
source_url: 'https://maskray.me/blog/2023-02-12-all-about-leak-sanitizer'
original_language: en
published: 2023-02-12
status: active
license: 未声明 → 仅私有归档
archived_at: 2026-07-27
content_hash: 'sha256:1caa93a90efd39b4'
translated: true
---

> [全面了解 LeakSanitizer](https://maskray.me/blog/2023-02-12-all-about-leak-sanitizer) · MaskRay (宋方睿)

[2023-02-12](https://maskray.me/blog/2023-02-12-all-about-leak-sanitizer)

# 全面了解 LeakSanitizer

Clang 和 [GCC 4.9](https://gcc.gnu.org/PR59061) 于 2013 年实现了 LeakSanitizer。[LeakSanitizer](https://clang.llvm.org/docs/LeakSanitizer.html)（LSan）是一种内存泄漏检测器。它会拦截内存分配函数，默认在 `atexit` 时检测内存泄漏。其实现完全位于运行时（`compiler-rt/lib/lsan`）中，无需插桩。

LSan 几乎没有与架构相关的代码，支持许多 64 位目标；部分 32 位目标（如 Linux arm/x86-32）也受支持。不过，位数较少的指针更容易与整数、浮点数或具有相似位模式的其他数据混淆，因此假阴性率可能较高。每个受支持的操作系统都需要提供某种“停止世界”的机制。

## 用法

LSan 可通过 3 种方式使用。

- 独立模式（`-fsanitize=leak`）
- AddressSanitizer（`-fsanitize=address`）
- HWAddressSanitizer（`-fsanitize=hwaddress`）

使用 LSan 最常见的方式是 `clang -fsanitize=address`（或 `gcc -fsanitize=address`）。对于支持 LSan 的目标（`#define CAN_SANITIZE_LEAKS 1`），AddressSanitizer（ASan）运行时默认启用 LSan。

```plaintext
% cat a.c
#include <stdlib.h>
int main() {
  void **p = malloc(42); // leak (categorized as "Direct leak")
  *p = malloc(43);       // leak (categorized as "Indirect leak")
  p = 0;
}
% clang -fsanitize=address a.c -o a
% ./a

=================================================================
==594015==ERROR: LeakSanitizer: detected memory leaks

Direct leak of 42 byte(s) in 1 object(s) allocated from:
    #0 0x55fffef9482e  (/tmp/c/a+0xea82e)
    #1 0x55fffefcf1d1  (/tmp/c/a+0x1251d1)
    #2 0x7f7301626189  (/lib/x86_64-linux-gnu/libc.so.6+0x27189) (BuildId: c4f6727c560b1c33527ff9e0ca0cef13a7db64d2)

Indirect leak of 43 byte(s) in 1 object(s) allocated from:
    #0 0x55fffef9482e  (/tmp/c/a+0xea82e)
    #1 0x55fffefcf1df  (/tmp/c/a+0x1251df)
    #2 0x7f7301626189  (/lib/x86_64-linux-gnu/libc.so.6+0x27189) (BuildId: c4f6727c560b1c33527ff9e0ca0cef13a7db64d2)

SUMMARY: AddressSanitizer: 85 byte(s) leaked in 2 allocation(s).
```

作为纯运行时功能，`-fsanitize=leak` 主要用于链接操作。链接可执行文件时，在许多目标上默认采用 `-static-libsan` 模式，Clang Driver 会向链接器传递 `--whole-archive $resource_dir/lib/$triple/libclang_rt.lsan.a --no-whole-archive`。GCC 和一些平台则偏好共享运行时/动态运行时。参见[关于 sanitizer 拦截器的一切](https://maskray.me/blog/2023-01-08-all-about-sanitizer-interceptors#elf-platforms)。 1  
2  
3  
4  
% clang -fsanitize=leak a.o '-###' |& grep --color lsan  
... --whole-archive" "/tmp/Rel/lib/clang/17/lib/x86_64-unknown-linux-gnu/libclang_rt.lsan.a" "--no-whole-archive" ...  
% gcc -fsanitize=leak a.o '-###' |& grep --color lsan  
... /usr/lib/gcc/x86_64-linux-gnu/12/liblsan_preinit.o --push-state --no-as-needed -llsan ...

`-fsanitize=leak` 也会影响编译操作，但仅限于下列 C/C++ 预处理器功能。 1  
2  
3  
4  
5  
6  
7  
8  
// Active if -fsanitize=leak  
#if __has_feature(leak_sanitizer)  
...  
#endif  
  
// Active if -fsanitize=leak or -fsanitize=address  
#if __has_feature(leak_sanitizer) || __has_feature(address_sanitizer)  
#endif

## 实现概述

独立 LSan 会拦截 malloc 系列和 free 系列函数。它使用带有块元数据的模板化 `SizeClassAllocator{32,64}`；拦截器会记录分配信息（请求大小和栈跟踪）。

AddressSanitizer 和 HWAddressSanitizer 已经拦截了 malloc 系列函数；它们的块元数据表示中都有供 LSan 使用的标志字段。

默认启用公共选项 `detect_leaks` 和 `leak_check_at_exit`。运行时通过 `atexit` 安装钩子以执行泄漏检查。或者，用户可调用 `__lsan_do_leak_check`，在退出前请求执行泄漏检查。

进行泄漏检查时，运行时执行的工作与标记-清扫垃圾回收算法非常相似：它暂停所有线程（“停止世界”），并扫描根集以找出可达的分配。根集包括：

- 因 `__lsan_ignore_object`、`__lsan::ScopedDisabler` 或 `__lsan_disable` 而被忽略的分配
- 全局区域（`__lsan::ProcessGlobalRegions`）。在 Linux 上，这些指的是由于可写 `PT_LOAD` 程序头部而产生的内存映射。这确保了全局变量可达的分配不会被误报为泄漏。
- 对每个线程而言，包括通用寄存器（默认 `use_registers=1`）、栈（默认 `use_stacks=1`）、线程本地存储（默认 `use_tls=1`）以及线程上下文中的额外指针
- 由 `__lsan_register_root_region` 注册的根区域
- 与操作系统相关的分配。目前仅限 macOS，例如 libdispatch 和 Foundation 的内存区域

（使用 ASan 且启用 `use_stacks` 时，为检测 `use-after-return` 而使用的伪栈也属于根集。参见 `compiler-rt/test/lsan/TestCases/use_after_return.cpp`。）

运行时使用洪泛填充算法，从根集中寻找可达的分配。它以保守方式查找所有看起来像指针的对齐位模式；若某个字看起来指向堆（许多 64 位目标把 `[0x600000000000, 0x640000000000)` 用作分配器空间），运行时便检查它是否指向已分配的块。按 Valgrind 的术语，引用可以是“起始指针”（指向块开头）或“内部指针”（指向块中间）。

最后，运行时遍历所有已分配的分配，并报告未标记分配的泄漏。

### 元数据

每个分配预留 2 位记录状态：泄漏、可达或忽略。为获得更好的诊断信息，“泄漏”还可分为直接泄漏或间接泄漏（Valgrind memcheck 的术语）。若一个块被标记为泄漏，从它可达的所有块都会被标记为间接泄漏。（开头示例中的 `*p = malloc(43);` 就是间接泄漏。）

```cpp
enum ChunkTag {
  kDirectlyLeaked = 0,  // default
  kIndirectlyLeaked = 1,
  kReachable = 2,
  kIgnored = 3
};
```

其思路可能是：用户修复所有直接泄漏后，若直接泄漏对象具有析构函数以释放其所引用的分配，间接泄漏也很可能随之消失。不过，间接泄漏可能构成环；修复全部直接泄漏也无法修复这样的间接泄漏。

```c
#include <stdlib.h>
#include <stdio.h>
int main() {
  void *x = malloc(8), *y = malloc(8);
  *(void **)x = y;   // in a cycle. Indirect leak
  *(void **)y = x;   // in a cycle. Indirect leak
  printf("%p %p\n", x, y);
}
```

独立 LSan 使用如下块元数据结构： 1  
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
struct ChunkMetadata {  
 u8 allocated : 8; // Must be first.  
 ChunkTag tag : 2;  
#if SANITIZER_WORDSIZE == 64  
 uptr requested_size : 54;  
#else  
 uptr requested_size : 32;  
 uptr padding : 22;  
#endif  
 u32 stack_trace_id;  
};

ASan 只是在既有块元数据中保存一个 2 位的 `ChunkTag`（`__asan::Chunkheader::lsan_tag`）。类似地，HWASan 在既有块元数据中保存一个 2 位的 `ChunkTag`（`__hwasan::Metadata::lsan_tag`）。

### 分配器

各 sanitizer 使用的分配器非常相似。为共享代码，`compiler-rt/lib/sanitizer_common` 将模板化的 `SizeClassAllocator{32,64}` 定义为分配器工厂。每个 sanitizer 实例化一个 `SizeClassAllocator{32,64}` 作为主分配器，并选择一个次级分配器。其中一个模板参数描述每个块的元数据大小；例如独立 LSan 将元数据大小设为 `sizeof(ChunkMetadata)`。

另一个模板参数定义大小类（`SizeClassMap`）。`SizeClassAllocator{32,64}`（主分配器）的实例拥有线程本地缓存（`SizeClassAllocator{32,64}LocalCache`），该缓存为每个大小类维护空闲链表。收到分配请求后，若所需大小类的空闲链表为空，运行时会对缓存调用 `Refill`，从 `SizeClassAllocator{32,64}` 取得更多块；否则缓存会从空闲链表中交出一个块给用户。

`SizeClassAllocator64` 的分配器空间总计 `kSpaceSize` 字节，划分为多个相同大小的区域（`kSpaceSize`），每个区域只服务一个大小类。每个区域都足够大，假定可以容纳其大小类的全部分配。在 `InitializeAllocator` 期间，`address_range.Init` 会用 `MAP_PRIVATE | MAP_FIXED | MAP_NORESERVE | MAP_ANON` 调用 `mmap`，将整个区域标记为 `PROT_NONE`。缓存调用 `Refill` 时，运行时会锁定对应的 `SizeClassAllocator64` 区域，并调用 `mmap` 分配新的内存映射（若 `kMetadataSize!=0`，还会分配一份元数据映射）。对于活跃分配，可以非常高效地计算它在区域中的索引及其关联元数据。独立 LSan 会把新分配且未被忽略的块标为 `kDirectlyLeaked`；ASan 也类似。

`SizeClassAllocator32` 主要用于 32 位地址空间，但也可用于 64 位地址空间。与 `SizeClassAllocator64` 一样，地址空间被划分为多个区域，不过区域更小（`kRegionSize`，通常为 1 MiB）。缓存调用 `Refill` 时，`SizeClassAllocator32` 会调用 `mmap` 分配一个服务于所需大小类的新区域。区域 ID 到大小类的映射记录在 `possible_regions_` 中（在 32 位地址空间场景中它是数组包装器）。

遍历 `SizeClassAllocator64` 简单且高效。每个大小类只有一个区域，每个区域由多个块组成。 1  
2  
3  
4  
5  
6  
7  
8  
9  
10  
void ForEachChunk(ForEachChunkCallback callback, void *arg) {  
 for (uptr class_id = 1; class_id \< kNumClasses; class_id++) {  
 RegionInfo *region = GetRegionInfo(class_id);  
 uptr chunk_size = ClassIdToSize(class_id);  
 uptr region_beg = SpaceBeg() + class_id * kRegionSize;  
 uptr region_allocated_user_size = AddressSpaceView::Load(region)-\>allocated_user;  
 for (uptr chunk = region_beg; chunk \< region_beg + region_allocated_user_size; chunk += chunk_size)  
 callback(chunk, arg);  
 }  
}

LSan 遍历块以查找已忽略的块（它们在根集中）和泄漏的块（用于错误报告）。

在 32 位地址空间中遍历 `SizeClassAllocator32` 很高效（至多 `2**32/kSpaceSize = 4096` 个区域），但在 64 位地址空间中效率很低。参见 [LSan is almost unusable on AArch64](https://github.com/google/sanitizers/issues/703) 这一问题（通过切换到 `SizeClassAllocator64` 修复）。

### 停止世界

在 Linux 上，运行时创建一个追踪线程来暂停所有其他线程。具体而言：

- 调用 `clone` 系统调用来创建一个与调用进程共享地址空间的新进程。
- 在新进程中，遍历 `/proc/$pid/task/` 以列出线程。
- 在新进程中调用 `SuspendThread`（ptrace `PTRACE_ATTACH`）暂停线程。

`StopTheWorld` 返回。运行时执行标记-清扫、报告泄漏，然后调用 `ResumeAllThreads`（ptrace `PTRACE_DETACH`）。

注意：该实现不能调用 libc 函数，也不执行代码注入。根集包含每个线程的静态/动态 TLS 块。

在 Fuchsia 上，运行时调用 `__sanitizer_memory_snapshot` 来停止世界。

## 运行时选项

LSan 提供一些运行时选项以切换行为。通过环境变量 `LSAN_OPTIONS` 指定这些运行时行为。

`LSAN_OPTIONS=use_registers=0:use_stacks=0:use_tls=0` 可以移除一些默认的根区域。`report_objects=1` 报告单个泄漏对象的地址。

`use_stacks=0`：从根集中移除栈。默认值为 1，用于防止以下提前退出代码的误报。1  
2  
3  
4  
int main() {  
 std::unique_ptr\<XXX\> a = ...;  
 if (...) exit(0);  
}

然而，默认值可能导致 LSan 检测到的泄漏更少，因为栈上可能存在悬空指针。1  
2  
struct C { int x = 0; };  
int main() { C *a = new C, *b = new C, *c = new C, *d = new C; }

下面的一些选项实现为公共选项（`compiler-rt/lib/sanitizer_common/sanitizer_flags.inc`）。

- 独立模式：使用 `LSAN_OPTIONS`
- AddressSanitizer：使用 `LSAN_OPTIONS` 或 `ASAN_OPTIONS`
- HWAddressSanitizer：使用 `LSAN_OPTIONS` 或 `HWASAN_OPTIONS`

对于独立 LSan，`exitcode=23` 是默认值。检测到泄漏时，运行时会以退出码 23 调用 exit 系统调用；对于集成到 ASan 的 LSan，默认值为 `exitcode=1`。

`verbosity=1` 会打印一些日志。

`leak_check_at_exit=0` 禁用注册 `atexit` 钩子以进行泄漏检查。

`detect_leaks=0` 会禁用全部泄漏检查，包括用户通过 `__lsan_do_leak_check` 或 `__lsan_do_recoverable_leak_check` 请求的检查。这类似于在程序中定义 `extern "C" int __lsan_is_turned_off() { return 1; }`。独立 LSan 采用 `detect_leaks=0` 时，其性能特征与纯 `SizeClassAllocator{32,64}` 相近，除栈跟踪外几乎没有额外开销。若能消除栈展开的开销，就能得到一个用于基准测试 `SizeClassAllocator{32,64}` 性能的简单方案。

若定义了 `__lsan_default_options`，其返回值会按 `LSAN_OPTIONS` 的格式解析。

## 漏报

有几个原因可能导致漏报。

首先，当 LSan 扫描根集时，它会查找看起来像指向分配器空间的指针的对齐位模式。一个整数或浮点数可能恰好具有相似的位模式，从而欺骗 LSan。

悬空指针可能欺骗 LSan。上面的 `use_stacks=0` 部分给出一个例子。让我们看另一个例子：1  
2  
3  
4  
5  
6  
7  
8  
9  
10  
#include \<vector\>  
std::vector\<int *\> *a;  
int main() {  
 a = new std::vector\<int *\>;  
 a-\>push_back(new int[1]);  
 a-\>push_back(new int[2]);  
 a-\>push_back(new int[3]);  
 a-\>pop_back();  
 a-\>pop_back();  
}

## 问题抑制

用户可以调用 `__lsan_ignore_object` 来忽略一个分配。`__lsan::ScopedDisabler` 是一个 RAII 类，用于忽略作用域内的所有分配。可以调用 `__lsan_disable` 来忽略当前线程的所有分配，直到调用 `__lsan_enable`。

以下是可能需要忽略某个分配的一些情形。

- 预构建的库存在已知泄漏
- 程序采用标记指针技巧，使指针不再看起来像指向该分配；例如 LSan 在 macOS 上已为 Objective-C 运行时的“伪装”指针[内置](https://reviews.llvm.org/D133126)支持

运行时会扫描每个被忽略的分配。可从被忽略分配到达的分配不视为泄漏。

`__lsan_register_root_region` 将一个区域注册为根。运行时扫描该区域与有效内存映射的交集（Linux 上为 `/proc/self/maps`）。`LSAN_OPTIONS=use_root_regions=0` 可以禁用已注册的区域。

要使用上述 API，请首先包含头文件 `#include <sanitizer/lsan_interface.h>`。

运行时从 3 个来源解析抑制规则：

- 默认抑制规则（`kStdSuppressions`）
- 如果定义了 `__lsan_default_suppressions`，则其返回值
- 用户指定的 `LSAN_OPTIONS=suppressions=a.supp`

抑制文件每行包含一条规则，每条规则的形式为 `leak:<pattern>`。对于泄漏，运行时检查栈回溯中的每一帧。每一帧都有一个与调用点地址关联的模块名（可执行文件或共享对象），并且在可符号化时，还有一个源文件名和函数名。如果任何模块名、源文件名或函数名与某个模式匹配（使用 glob 进行子串匹配），则该泄漏被抑制。

注意：符号化需要调试信息和符号化器（内部符号化器（默认未构建）或 `llvm-symbolizer` 目录中的 `PATH`）。

让我们看一个例子。1  
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
cat \> a.c \<\<'eof'  
#include \<stdlib.h\>  
#include \<stdio.h\>  
void *foo();  
int main() {  
 foo();  
 printf("%p\\n", malloc(42));  
}  
eof  
cat \> b.c \<\<'eof'  
#include \<stdlib.h\>  
void *foo() { return malloc(42); }  
eof  
clang -fsanitize=leak -fpic -g -shared b.c -o b.so  
clang -fsanitize=leak -g a.c ./b.so -o a  
  
which llvm-symbolizer # available  
LSAN_OPTIONS=suppressions=\<(printf 'leak:a') ./a # suppresses both leaks (by module name)  
LSAN_OPTIONS=suppressions=\<(printf 'leak:a.c') ./a # suppresses both leaks (by source file name)  
LSAN_OPTIONS=suppressions=\<(printf 'leak:b.c') ./a # suppresses the leak in b.so (by source file name)  
LSAN_OPTIONS=suppressions=\<(printf 'leak:main') ./a # suppresses both leaks (by function name)  
LSAN_OPTIONS=suppressions=\<(printf 'leak:foo') ./a # suppresses the leak in b.so (by function name)

## 杂项

独立 LeakSanitizer 可与 SanitizerCoverage 一起使用：`clang -fsanitize=leak -fsanitize-coverage=func,trace-pc-guard a.c`

测试套件已迁移。可通过 `git log -- compiler-rt/lib/lsan/lit_tests/TestCases/pointer_to_self.cc`（使用 `.cc` 而非 `.cpp`）追溯旧测试的历史。

我有一个待处理的 FreeBSD 移植 [https://github.com/MaskRay/llvm-project/tree/rt-freebsd-lsan](https://github.com/MaskRay/llvm-project/tree/rt-freebsd-lsan)。希望我能找到时间完成它。

## 类似工具

Valgrind 的 Memcheck 默认使用 `--leak-check=yes` 并执行泄漏检查。该特性自 2002 年的初始版本（`git log -- vg_memory.c`）以来就已存在。

Google 将 HeapLeakChecker 作为 gperftools 的一部分开源。它属于 TCMalloc，并与 `debugallocation.cc` 一同使用。多线程分配必须获取全局锁，速度远慢于 Sanitizer 分配器（`compiler-rt/test/lsan/TestCases/high_allocator_contention.cpp`）。`heap_check_max_pointer_offset`（默认值为 2048）指定扫描一个分配以寻找指针时使用的最大偏移量；该默认值容易造成误报。

[heaptrack](https://github.com/KDE/heaptrack) 是一个支持泄漏检查的堆内存分析器。
