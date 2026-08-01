---
title: Sanitizer 拦截器详解
source: MaskRay (宋方睿)
source_key: maskray
source_url: 'https://maskray.me/blog/2023-01-08-all-about-sanitizer-interceptors'
original_language: en
published: 2023-01-08
status: active
license: 未声明 → 仅私有归档
archived_at: 2026-07-27
content_hash: 'sha256:857124568e727ca7'
translated: true
---

> [Sanitizer 拦截器详解](https://maskray.me/blog/2023-01-08-all-about-sanitizer-interceptors)　·　MaskRay (宋方睿)

[2023-01-08](https://maskray.me/blog/2023-01-08-all-about-sanitizer-interceptors)

# Sanitizer 拦截器详解

2025 年 8 月更新。

许多 Sanitizer 需要了解程序中的每个函数。用户函数经过插桩，因此 Sanitizer 运行时能够识别它们。部分库函数（例如 mmap、munmap、内存分配与释放函数、longjmp、vfork）需要特殊处理：Sanitizer 利用符号插位，把对这类函数的调用重定向到自己的实现，即拦截器。其他库函数可以像普通用户代码一样处理。对函数插桩或为它提供拦截器都可以。

在某些情况下，插桩是不可行的：

- 汇编源文件通常不会调用（或不便于调用）Sanitizer 回调
- 许多 libc 实现无法被插桩。[何时能用 Clang 构建 glibc？](https://maskray.me/blog/2021-10-10-when-can-glibc-be-built-with-clang#asm-label-after-first-use)
- 某些函数如果被插桩而不是拦截，会出现性能问题（主要是 `mem*` 和 `str*`)

而且拦截器可能是实际可行的选择。

本文讨论拦截器的工作原理，以及 Sanitizer 为什么需要拦截器。

## 拦截器的工作原理

以下是简要总结，后续我会详细说明。

- ELF 平台：`__interceptor_$name` 有一个弱别名 `$name`，其名称与被拦截的函数相同。
- Apple 平台：`__DATA,__interpose` 保存了拦截器（`wrap_$name`）和被拦截函数的地址。
- Windows：对拦截函数进行热补丁

### ELF 平台

在 Clang 中，ELF 平台上的 Sanitizer 运行时文件名为 `$resource_dir/lib/$triple/libclang_rt.*.{a,so}`。在较旧的 `LLVM_ENABLE_PER_TARGET_RUNTIME_DIR=off` 配置下（LLVM 15.0.0 之前的默认配置），文件名为 `$resource_dir/lib/libclang_rt.*-$arch.{a,so}`。`.a` 文件称为静态运行时，`.so` 文件称为共享运行时或动态运行时。截至 2023 年 1 月，Android 和 Fuchsia 默认使用共享运行时，其他 ELF 平台（Linux、*BSD 等）默认使用静态运行时。

在 GCC 中，Sanitizer 运行时文件名为 `lib*san.{a,so}`。默认使用共享运行时；指定 `-static-libasan` 可改用静态运行时。

### 静态运行时

大多数静态运行时文件仅在链接可执行文件时使用。在 `-static-libsan` 模式下，链接可执行文件时，Clang Driver 会将 `--whole-archive $resource_dir/lib/libclang_rt.$name.a --no-whole-archive` 传递给链接器。对于以下示例，如果 `libclang_rt.$name.a` 定义了 `malloc` 和 `free`, 可执行文件将获得这些定义。

```sh
printf '#include <stdlib.h>\nint main() { void *p = malloc(42); free(p); }' > a.c
clang -fsanitize=address a.c -o a
```

`malloc`, `free` 被导出到 `.dynsym`，因为它们被一个链接时共享对象（glibc link-time）定义或引用，即使没有指定 `libc.so.6`。详见 `-Wl,--export-dynamic` 解释 [GNU 风格链接器选项#--export-dynamic](https://maskray.me/blog/2020-11-15-explain-gnu-linker-options#export-dynamic)。`-Wl,--gc-sections` 无法丢弃这些拦截器，因为 `.dynsym` 符号被视为 GC 根。

另外，请注意这些定义是弱且无版本化的。

```text
% nm -D a | grep -w 'malloc\|free'
00000000000ead10 W free
00000000000eb010 W malloc
```

链接共享对象时，不使用静态运行时。链接器选项 `-z defs` (`--no-undefined` 可能导致未定义符号错误。

在 Linux glibc 上，共享对象具有一个带版本化的引用。

```sh
printf '#include <stdlib.h>\nvoid *foo() { return malloc(42); }' > b.c
clang -fsanitize=address -fpic -shared b.c -o b.so
```

```text
% nm -D b.so | grep 'malloc\|free'
                 U malloc@GLIBC_2.2.5
```

如果让 `b.so` 成为可执行文件 `a` 的链接时依赖项，或在运行时 dlopen `b.so`，那么 `b.so` 中对 `malloc@GLIBC_2.2.5` 的引用会绑定到 `a` 中的定义。动态加载器会计算一个广度优先的符号搜索列表（`executable, needed0, needed1, needed2, needed0_of_needed0, needed1_of_needed0, ...`）。对于每个符号引用，动态加载器遍历该列表，找到第一个提供定义的组件。可执行文件提供了定义，因此搜索到可执行文件便会停止。参见 [ELF 插位与 -Bsymbolic](https://maskray.me/blog/2021-05-16-elf-interposition-and-bsymbolic)。

实际上，我们还使用了一条规则：`malloc@GLIBC_2.2.5` 引用可以绑定到 `malloc` 的 `VER_NDX_GLOBAL` 定义。请参见 [关于符号版本化的所有信息#rtld-behavior](https://maskray.me/blog/2020-11-26-all-about-symbol-versioning#rtld-behavior).

由于可执行文件定义了 `malloc` 和 `free`，因此其对这两个符号的调用不使用 PLT。这是与共享运行时相比的一个优势。从共享对象发出的调用仍然需要 PLT。预加载 malloc 函数不起作用，因为可执行文件的定义具有更高优先级。

从 LLVM 17 开始，[拦截器涉及四个符号](https://reviews.llvm.org/D151085). `func` 具有 `STB_WEAK` 绑定，并别名为一个跳板（`__interceptor_trampoline_func`），该跳板跳转到一个弱函数 `__interceptor_func`. `__interceptor_func` 别名为一个 `STB_GLOBAL` 函数 `___interceptor_func`，该函数提供 sanitizer 拦截器实现。

```plaintext
% readelf -Ws $(clang --print-file-name=libclang_rt.asan.a) | grep -E 'malloc$'
  3638: 0000000000000000     0 NOTYPE  GLOBAL DEFAULT  UND ___interceptor_malloc
     6: 0000000000000000     0 SECTION LOCAL  DEFAULT   11 .text.___interceptor_malloc
    51: 000000000000000a     5 FUNC    WEAK   DEFAULT    2 malloc
    52: 000000000000000a     5 FUNC    GLOBAL DEFAULT    2 __interceptor_trampoline_malloc
    53: 0000000000000000   270 FUNC    WEAK   DEFAULT   11 __interceptor_malloc
   107: 0000000000000000   270 FUNC    GLOBAL DEFAULT   11 ___interceptor_malloc
```

```plaintext
malloc:
__interceptor_trampoline_malloc:
  jmp __interceptor_malloc

__interceptor_malloc:
___interceptor_malloc:
  // sanitizer interceptor implementation
```

用户代码可以定义一个 `STB_GLOBAL` `func` 来[覆盖](https://github.com/llvm/llvm-project/commit/7fb7330469af52ae1313b2b47c273e62c61a4dd5)拦截器，并调用 `__interceptor_func` 以获取 sanitizer 定义。

`__interceptor_func` 是弱符号，因此它可以被 out-of-tree 采样拦截器覆盖。该 out-of-tree 采样拦截器运行时可能会定义一个 `STB_GLOBAL` `__interceptor_func`，以便在大多数时候调用真正的 `malloc`，有时则调用 sanitizer 拦截器 `___interceptor_malloc`.

在 LLVM 17 之前，拦截器以两个符号的形式提供，一个名为 `__interceptor_$name`，具有 `STB_GLOBAL` 绑定，另一个名为 `$name`，具有 `STB_WEAK` 绑定。

```plaintext
% readelf -Ws $(clang-16 --print-file-name=libclang_rt.asan.a) | grep -E ' (malloc|__interceptor_malloc)$'
  2196: 0000000000000000     0 NOTYPE  GLOBAL DEFAULT  UND __interceptor_malloc
    57: 0000000000000000   295 FUNC    GLOBAL DEFAULT   10 __interceptor_malloc
   121: 0000000000000000   295 FUNC    WEAK   DEFAULT   10 malloc
```

在 Clang 中，Android、Fuchsia 和 Darwin 默认使用共享运行时；GCC 在 Linux 上也默认使用此模式。在默认使用静态运行时的目标上，可用 `-shared-libsan` 选择此配置。可执行文件和共享对象都会链接到 `libclang_rt.$name.so`。下面是 Linux glibc 上的示例。

```text
% clang -fsanitize=address -shared-libsan a.c -o a
% readelf -Wd a | grep 'clang_rt\|libc'
 0x0000000000000001 (NEEDED)             Shared library: [libclang_rt.asan.so]
 0x0000000000000001 (NEEDED)             Shared library: [libc.so.6]
% readelf -d b.so | grep 'clang_rt\|libc'
 0x0000000000000001 (NEEDED)             Shared library: [libclang_rt.asan.so]
 0x0000000000000001 (NEEDED)             Shared library: [libc.so.6]
% readelf -W --dyn-syms $(clang --print-file-name=libclang_rt.asan.so) | grep -w malloc
  1295: 000000000011a2d0   295 FUNC    WEAK   DEFAULT   11 malloc
```

在符号搜索列表中，`libclang_rt.asan.so` 出现在 `libc.so.6` 之前，因此来自 `malloc` 和`a`的 `b.so` 引用将被绑定到 `malloc` 中的 `libclang_rt.asan.so` 定义。带版本引用可绑定到 `VER_NDX_GLOBAL` 定义的规则再次生效。

预加载共享对象是危险的，asan 运行时会对此发出警告。

```plaintext
% clang -fsanitize=address -shared-libsan -Wl,-rpath=$(dirname $(clang --print-file-name=libclang_rt.asan.so)) a.c -o a
% LD_PRELOAD=/lib/x86_64-linux-gnu/libjemalloc.so.2 ./a
==1650190==ASan runtime does not come first in initial library list; you should either link runtime to your application or manually preload it with LD_PRELOAD.
```

当使用 `dlopen` 标签时，[拦截器无法正常工作](https://github.com/llvm/llvm-project/issues/28164)标签被使用时。`DT_RUNPATH` 标签被使用时。

### `dlsym RTLD_NEXT`

拦截器需要调用被拦截的库函数。在初始化期间，运行时对所有被拦截的函数调用 `dlsym(RTLD_NEXT, $name)` 并保存地址。拦截器 `__interceptor_$name` 调用保存的 `dlsym(RTLD_NEXT, $name)`.

的返回值。`libclang_rt.asan.so` 在之前的示例中，无论定义是在可执行文件中还是在 `libc.so.6` 中，该组件在符号搜索列表中都优先于 `dlsym(RTLD, $name)`。因此 `libc.so.6`.

会返回 `dlsym(RTLD_NEXT, name)` 中_name_中最旧版本定义的地址。`libc.so.6` 中[https://github.com/google/sanitizers/issues/1371](https://github.com/google/sanitizers/issues/1371)的最旧版本定义的地址。我们因此使用了旧的语义。这通常没什么问题，但并不理想（关于 `regexec` 的问题，请参阅[）。我修复了 glibc 2.36（](https://sourceware.org/bugzilla/show_bug.cgi?id=14932)），使 `dlsym(RTLD_NEXT, name)` 现在返回默认版本定义。

这个修复导致了一个有趣的问题。glibc 2.34 将[设为非默认版本定义，](https://sourceware.org/git/?p=glibc.git;a=commit;h=99f841c441feeaa9a3d97fd91bb3d6ec8073c982) `__pthread_mutex_lock` 非默认版本定义，non-default 设为非默认版本定义，因此 `dlsym(RTLD_NEXT, "__pthread_mutex_lock")` 会返回 NULL。我通过在构建时如果 glibc[禁用该拦截器来修复它](https://github.com/llvm/llvm-project/commit/fb32a69855341630a7084364c66083264e1d18bf)≥2.34\>，则禁用该拦截器。

由于 `dlsym RTLD_NEXT` 会被频繁调用，当可执行文件加载 O(1000) 个 DSO 时，rtld 的开销会成为显著瓶颈。大多数 rtld 实现都会遍历所有 DSO，并且往往到搜索列表末尾才能找到符号（例如 glibc 的 `libc.so.6`）。

### Apple 平台

在 Apple 平台上，Sanitizer 使用 dyld 的功能拦截符号，且只支持动态运行时。

运行时定义了一个特殊段 `__DATA,__interpose`，其中包含一个对列表，保存拦截器（名为 `wrap_$name`）和拦截函数的地址。只要调用并非来自定义拦截器的库，dyld 就会将调用重定向到拦截器。

假设我们有一个拦截器 `wrap_strcmp`。它调用真正的定义 `strcmp`。dyld 会将引用绑定到 `libsystem_kernel.dylib` 中的真正定义，而不是 `wrap_strcmp`.

```cpp
// compiler-rt/lib/interception/interception.h
// For a function foo() and a wrapper function bar() create a global pair
// of pointers { bar, foo } in the __DATA,__interpose section.
// As a result all the calls to foo() will be routed to bar() at runtime.
#define INTERPOSER_2(func_name, wrapper_name) __attribute__((used)) \
const interpose_substitution substitution_##func_name[] \
    __attribute__((section("__DATA, __interpose"))) = { \
    { reinterpret_cast<const uptr>(wrapper_name), \
      reinterpret_cast<const uptr>(func_name) } \
}
```

让我们用一个简化的例子来感受一下。1  
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
cat \> a.c \<\<eof  
#include \<string.h\>  
  
int initialized;  
int main(int argc, char *argv[]) {  
 initialized = 1;  
 return strcmp(argv[1], argv[2]);  
}  
eof  
cat \> b.c \<\<eof  
#include \<stdio.h\>  
#include \<string.h\>  
  
extern int initialized;  
int wrap_strcmp(const char *a, const char *b) {  
 if (initialized)  
 printf("strcmp: %s %s\\n", a, b);  
 return strcmp(a, b);  
}  
  
__attribute__((used, section("__DATA, __interpose")))  
static void *const interpose[] = {(void *)wrap_strcmp, (void *)strcmp};  
eof  
clang -dynamiclib -Wl,-U,_initialized b.c -o b.dylib # or use -Wl,-undefined,dynamic_lookup  
clang a.c b.dylib -o a  
./a a a

### Windows

请参阅 [适用于 Windows 的 AddressSanitizer，2014 年 LLVM 开发者会议](https://llvm.org/devmtg/2014-10/Slides/ASan%20for%20Windows.pdf)。当前实现在 `compiler-rt/lib/interception/interception_win.cpp`。拦截器通过在拦截函数的入口块进行热修补来实现。

链接运行时有多种方式。

对于 `/MT`,

- 一些函数（例如 e.g. `malloc`）由该库定义。运行时只需将拦截器定义为相同的名称。
- 许多函数是通过 dllimport 导入的。运行时调用 `__interception::OverrideFunction` 来尝试多种热修补技术。

对于 `/MD`，运行时维护一个感兴趣的 DLL 列表，检查哪个 DLL 定义了被拦截的函数，并调用 `__interception::OverrideFunction` 进行热修补。

热修补后，被拦截函数的第一条指令将直接或通过蹦床跳转到拦截器。拦截器将跳转回来。

`compiler-rt/lib/asan/asan_win_dll_thunk.cpp` 需要针对新的 asan 拦截器进行更新。

## 拦截器要求

### AddressSanitizer

AddressSanitizer 检测内存可寻址性错误。对于已映射的内存区域，它使用影子内存记录用户字节是否不可寻址（已毒化）；访问这类字节会被视为错误（`heap-buffer-overflow, heap-use-after-free, stack-buffer-overflow, stack-use-after-{return,scope}` 等）。每 8 个按粒度对齐的用户字节映射到一个影子内存字节。（可以通过修改来支持其他粒度，例如现已删除的 Myriad RTEMS 移植使用 32 作为粒度。）

影子内存字节为 0（_未毒化_，所有 8 个字节都可寻址）或一个 non-zero 整数（_已毒化_，并非所有 8 个字节都可寻址）。该 non-zero 整数可能小于 8（前 X 个字节可寻址）或是一个预定义的特殊值（用于指示 bug 类别）。

在拦截器的开头，如果运行时尚未初始化，则会调用 `AsanInitFromRtl`。

mmap 和 munmap 不需要特殊处理。

当从映射区域预留一块内存用于堆分配时，关联的影子内存会被毒化为 0xfa（`kAsanHeapLeftRedzoneMagic`）。对于 malloc-family 函数，其拦截器会记录分配信息（线程 ID、请求大小、堆栈回溯、分配类型（`malloc, new, new[]` 等））并解除影子的毒化（设置为零），如果之前未分配，则可能为 0xfa。

对于 free-family 函数，其拦截器会检测双重释放和 alloc-dealloc 类型不匹配 bug，记录释放信息（线程 ID、堆栈回溯），并使用 0xfd（`kAsanHeapFreeMagic`）对影子进行毒化。对被释放内存的已检测/被拦截访问将导致错误。

对于执行内存读取或写入的库函数，其拦截器会模拟一次已检测的内存读取/写入：检查影子内存，并在遇到已毒化字节时报告错误。

某些库函数会在内部分配内存。一种实现通常谨慎地使用可拦截符号 `malloc` 而不是私有别名，这样分配/释放操作将被 AddressSanitizer 知晓，并正确地解除毒化/毒化。

一个既未经检测也未被拦截的 non-special 函数只会导致检测到的错误更少。

#### 作用域后栈使用

一个经检测的函数会毒化栈变量以捕获作用域后栈使用 bug。检测会在函数返回前解除栈变量的毒化。如果进程创建一个带有共享内存的子进程，并且子进程由于无返回函数（包括 throw 表达式）而退出，那么未毒化的影子内存可能会导致对第一个进程的[误报](https://github.com/google/sanitizers/issues/37)。这可以通过在调用无返回函数之前调用 `__asan_handle_no_return` 来保守地解除整个栈的毒化来修复。

`vfork` 存在[类似](https://github.com/google/sanitizers/issues/925)的问题，需要一个拦截器。

longjmp-family 函数也存在类似问题。栈内存可能会被重用，导致误报。这些函数在运行时中被拦截，以调用 `__asan_handle_no_return`.

https://github.com/android/ndk/issues/988

### HWAddressSanitizer

HWAddressSanitizer 使用不同的算法（软件内存标记）检测可寻址性 bug（与 AddressSanitizer 的主要功能检测同一类错误）。16 粒度对齐的用户字节与一个 non-zero 标签关联。该标签实现为一个字节，存储在影子内存中。

一次内存分配会选择一个随机的 non-zero 标签，并将其设置在返回指针的高位中。所分配区块的影子内存会填入该标签。为了支持使用 non-zero 高位访问指针，需要硬件特性（ARM 最高字节忽略、Intel 线性地址掩码、RISC-V 指针掩码）或页面别名。

拦截器的行为与 AddressSanitizer 类似。

mmap 与 munmap 无需特殊处理。

对于经过插桩的内存读取或写入操作，其拦截器会模拟一次插桩内存读/写：将指针标签与影子内存中存储的标签进行对比，并在不匹配时报告错误。

为了检测 use-after-free，内存释放需要清除关联的影子内存。

对于拦截器，执行与 AddressSanitizer 类似的操作：将指针标签与影子内存进行对比，并在不匹配时报告错误。

HWAdressSanitizer 已[部署](https://source.android.com/docs/security/test/hwasan)于 Android 上。其 C 库 bionic 已插桩，因此几乎不需要拦截器。

未来若要在 glibc 中使用 HWAdressSanitizer，要么需要提供拦截器，要么对 glibc 进行插桩。

longjmp-family 系列函数存在与 AddressSanitizer 类似的问题。栈内存可能被重用，导致误报。这些函数会被拦截，调用 `__hwasan_handle_longjmp` 来清除影子内存。`vfork` 需要一个与 AddressSanitizer 类似的拦截器。

### ThreadSanitizer

在旧版运行时（tsan v2）中，8 个对齐的用户字节映射到 32 字节的影子单元，其中包含 4 个影子值。该表示使用 13 位记录线程 ID（最多支持 8192 个线程），并使用 42 位记录向量时钟时间戳。

在新版运行时（tsan v3）中，8 个对齐的用户字节映射到 16 字节的影子单元，其中包含 4 个影子值。一个影子值记录了所访问字节的位掩码（8 位）、一个线程槽 ID（8 位）、一个向量时钟时间戳（14 位）、is_read（1 位）、is_atomic（1 位）。时间戳的增长变慢（仅在原子释放、互斥锁解锁、线程创建/销毁时递增），因此可以缩减时间字段。

在拦截器开始时，运行时会调用 `cur_thread_init` 并获取当前函数的线程状态和返回地址。对于执行内存读取或写入的库函数，其拦截器会模拟一次插桩内存读/写：将访问记录为线程事件（`EventAccess`），形成一个新的影子值，并检查影子单元中现有的影子值（最多 4 个）。如果当前影子值与之前的影子值在被访问字节的位掩码中存在交互，并且具有不同的线程槽 ID、至少有一个写操作、至少有一个 non-atomic 访问，则报告数据争用。否则，将新的影子值替换其中一个旧值。

pthread 互斥锁函数，例如 `pthread_mutex_{init,destroy,lock,trylock,timedlock,unlock}`（以及 `pthread_{rwlock,spin,cond,barrier}_*` `pthread_once`）会被拦截，以记录互斥锁的生命周期和同步点。

大多数 libc 函数不具有同步语义。

既未插桩也未拦截的 non-special 函数只会导致检测到的错误减少。

### MemorySanitizer

MemorySanitizer 使用影子内存来跟踪内存区域是否包含未初始化的值。

一个用户字节映射到一个影子内存字节。影子内存字节为 0（_未污染_，所有 8 位均已初始化）或一个 non-zero 整数（_已污染_，某些位未初始化）。

在拦截器开始时，如果运行时尚未初始化，则会调用 `__msan_init`。然后对 `__errno_location()` 的返回值进行反污染处理。为了支持 `-fsanitize=memory,fuzzer`，拦截器会因[检查](https://reviews.llvm.org/D48891)由于 libFuzzer 是否禁用了拦截器而引入少量开销。这样做是为了使 libFuzzer 运行时无需被 MemorySanitizer 插桩。

对于执行内存读取的库函数：如果影子内存已被污染，则报告一个 use-of-uninitialized-value 错误。对于执行内存写入的库函数：对影子内存进行反污染处理，i.e 将内存区域标记为已初始化。

如果执行内存写入的未插桩函数没有拦截器，那么在进行后续内存读取时，由于缺少反污染处理，可能会导致误报。此特性与 AddressSanitizer/ThreadSanitizer 不同，后两者缺少拦截器通常只会导致检测到的错误减少。

### DataFlowSanitizer

[DataFlowSanitizer](https://clang.llvm.org/docs/DataFlowSanitizer.html)是一种动态数据流分析（污点分析）工具。它允许为用户字节标记最多 8 个标签。当一个用户字节影响到另一个字节的计算时，编译器插桩会传播标签。该过程类似于 MemorySanitizer 中的未初始化值传播。一个用户字节映射到一个支持 8 个标签的影子内存字节。

在拦截器开始时，如果运行时尚未初始化，则会调用 `dfsan_init`。然后清除 `__errno_location()` 的标签。

对于 malloc-family 或 free-family 函数，默认情况下，其拦截器会清除标签（假设这些字节不受其他值的影响）。

对于执行内存写入或返回值的库函数，其拦截器会传播源值的标签。

执行内存写入且既未插桩也未拦截的 non-special 函数会丢失标签传播。这可能会导致漏报。

### NumericalSanitizer

NumericalSanitizer 使用影子内存来跟踪浮点类型和值。用法与 MemorySanitizer 类似。然而，误报率显著更低。这是因为易产生误报的场景不太可能被利用：

- 分配、存储一个浮点数，然后释放
- calloc/mmap，实际上重用了之前的分配，其中包含一个 non-zero 的浮点数值
- 执行类似 read-write 的读写操作。影子内存中保存了一个 `*p += f` 的浮点数值，与实际零值不匹配。non-zero 浮点值，与实际为零的值不匹配。

### Standalone LeakSanitizer

对于大多数主要的 64 位平台（Apple 除外），AddressSanitizer 会集成 LeakSanitizer 并默认启用它。LeakSanitizer 也可以单独使用，仅用于检测内存泄漏错误。请参阅[关于 LeakSanitizer 的一切](https://maskray.me/blog/2023-02-12-all-about-leak-sanitizer).

独立的 LeakSanitizer 拦截的函数非常少：malloc-family 和 free-family 函数（类似预加载的内存分配器），以及少数几个函数，比如 `pthread_create`.

在拦截器的起始位置，如果运行时尚未初始化，则会调用 `__lsan_init`。

对于 malloc-family 函数，其拦截器会记录分配信息（请求的大小、堆栈跟踪）。

对于 `pthread_create`，其拦截器 [确保](https://github.com/llvm/llvm-project/commit/bdeff959a166594abf76206d0eae397e4cc17747) 正确的线程 ID，忽略来自实际 `pthread_create` 的分配，并注册新线程。

在退出时，LeakSanitizer 会执行一次 GC 风格的 stop-the-world 操作，并扫描所有可达的内存块。对于不可达的内存块，使用记录的信息报告一个错误。

### Scudo 强化分配器与 GWP-ASan

Scudo 是一种 user-mode 内存分配器，旨在能够抵御 heap-related 的安全漏洞。[GWP-ASan](https://llvm.org/docs/GwpAsan.html) 使用 Scudo 作为主分配器，并让 Scudo 将采样的内存分配移交给其自己的内存分配器。

在 Scudo 中，只有与内存分配器相关的函数会被拦截。

### Realtime Sanitizer

对于标记了 `[[clang::nonblocking]]` 特性的函数，Realtime Sanitizer 会识别出对执行时间可能不确定的库函数的调用。non-deterministic 许多库函数会被拦截。

MemProf

### MemProf

TODO 不是 sanitizer，但它使用了 sanitizer 拦截器。

## 可移植性与可维护性

Sanitizer 支持许多操作系统和架构。

- [https://clang.llvm.org/docs/AddressSanitizer.html#supported-platforms](https://clang.llvm.org/docs/AddressSanitizer.html#supported-platforms)
- [https://clang.llvm.org/docs/MemorySanitizer.html#supported-platforms](https://clang.llvm.org/docs/MemorySanitizer.html#supported-platforms)
- [https://clang.llvm.org/docs/ThreadSanitizer.html#supported-platforms](https://clang.llvm.org/docs/ThreadSanitizer.html#supported-platforms)
- ...

实现拦截器（尽管代码可以共享）可能是将 sanitizer 移植到新平台时最具挑战性的部分。

- libc 实现或多或少都会支持一些扩展。这些函数需要被拦截。
- 较新标准中的类型定义可能不被其实现支持。需要进行版本分发，或者提供一个 shim。

因此，Sanitizer 运行时中散布着 `#if` 条件包含。带有组合爆炸的运行时测试有时会使调试变得棘手。

因此，支持一个新的操作系统必须非常谨慎。我认为 sanitizer 维护者倾向于专注于为 libc 进行插桩的能力，并在考虑新操作系统时提供 sanitizer 回调。有人可能会问，当 sanitizer 运行时更新并需要与旧版 libc 协同工作时，这是否会给其带来压力。看起来 sanitizer 运行时中拦截的读/写行为部分相当稳定，因此与多个 libc 版本协同工作似乎是可行的。

### glibc

正如本文开头所述，glibc [无法用 Clang 构建](https://maskray.me/blog/2021-10-10-when-can-glibc-be-built-with-clang#asm-label-after-first-use)。我希望在未来几年内这种情况会有所改变。

好的，一个观察结果：新版本的 glibc 通常需要 sanitizer 拦截器进行适配。

Linux 内核的用户空间 API 与 glibc 历来配合不佳，这种不协调偶尔会给项目带来可移植性问题。Sanitizer 拦截器大量使用 `#include <linux/*.h>`，因此也会受到影响。例如，我提交了 [D129471](https://reviews.llvm.org/D129471)，移除 `#include <linux/fs.h>`，以解决它与 glibc 2.36 中 `fsconfig_command/mount_attr` 的冲突。TODO：说明为何难以从 `compiler-rt/lib/sanitizer_common/sanitizer_platform_limits_posix.cpp` 中移除 `#include <linux/*.h>`。

### musl

2021 年 1 月，我把 [`asan, cfi, lsan, msan, tsan, ubsan` 移植到 Linux musl](https://github.com/llvm/llvm-project/commit/7afdc89c2054d6fa3a6c2f2f24411becfc764676)，并在此过程中学到了很多。有些地方的代码可读性似乎也有所改善：原先受 glibc 思维影响的条件得到了更准确的表达，例如把“Linux 但不是 Android”或“除 X/Y/Z 外的所有操作系统”（X/Y/Z 基本列举了所有非 glibc 平台）改成“Linux glibc”。维护这一移植的成本很低，2021 和 2022 年我只应用了极少的修复。

musl 提供了 `_LARGEFILE64_SOURCE` 符号（`mmap64, pread64, readdir64, stat64` 等）用于 glibc ABI 兼容性，但这些符号并非用于链接。musl 1.2.4 将不允许链接 LFS64 符号[，因此这些拦截器不得不被移除](https://reviews.llvm.org/D141186).

## 有趣的问题

### Non-intercepted 调用了被拦截库函数的未被拦截库函数

#### MemorySanitizer/DataFlowSanitizer 与 ptsname

`ptsname` 以前不会被拦截，这导致 MemorySanitizer 出现误报。

在 glibc 中，`ptsname` 会使用一个静态变量（MemorySanitizer 未知，具有零值的影子字节）调用 `__ptsname_r`。由于 `__ptsname_r` 未被插桩，`numbuf` 的影子内存取决于该内存区域上次的影子值，而 `numbuf` 恰好占据该区域。如果 `memcpy` 是可插入的，其拦截器会将错误的（已污染的）影子字节复制到 `buf`，如果调用者访问 `buf`，则可能导致误报。  
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
int  
__ptsname_r (int fd, char *buf, size_t buflen)  
{  
 ...  
 char numbuf[21];  
 ...  
 numbuf[sizeof (numbuf) - 1] = '\\0';  
 p = _itoa_word (ptyno, &numbuf[sizeof (numbuf) - 1], 10, 0);  
 ...  
 memcpy (__stpcpy (buf, devpts), p, &numbuf[sizeof (numbuf)] - p);  
 ...  
}

修复方法是[instrument](https://reviews.llvm.org/D88547) `ptsname``ptsname_r`.

在 2018 年之前的 glibc 中（[BZ #18822](https://sourceware.org/bugzilla/show_bug.cgi?id=18822)），许多函数都有 PLT 调用。其中潜伏着许多类似上述的问题。

### `_FORTIFY_SOURCE`

简而言之，使用 sanitizer 时应禁用 `_FORTIFY_SOURCE`。如果 `-D_FORTIFY_SOURCE=2` 是在你指定的选项之后追加的，请使用 `-Wp,-U_FORTIFY_SOURCE` 来覆盖它。

当启用 `_FORTIFY_SOURCE` 时，某些库函数会被重定向到 `*_chk`。拦截器不提供 `*_chk`（有一个例外[https://reviews.llvm.org/D40951](https://reviews.llvm.org/D40951)），所以最终我们只能检测到更少的错误（e.gasan、tsan）或出现误报（msan）。

请参阅 [https://github.com/google/sanitizers/issues/247](https://github.com/google/sanitizers/issues/247).

### Android 链接器命名空间与 libc++ 拦截器

[https://github.com/android/ndk/issues/988](https://github.com/android/ndk/issues/988)
