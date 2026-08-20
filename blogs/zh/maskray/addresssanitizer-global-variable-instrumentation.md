---
title: 'AddressSanitizer：全局变量插桩'
source: MaskRay (宋方睿)
source_key: maskray
source_url: 'https://maskray.me/blog/2023-10-15-address-sanitizer-global-variable-instrumentation'
original_language: en
published: 2023-10-15
status: active
license: 未声明 → 仅私有归档
archived_at: 2026-07-27
content_hash: 'sha256:b7bb008b281a1d9d'
translated: true
---

> 原文：[AddressSanitizer：全局变量插桩](https://maskray.me/blog/2023-10-15-address-sanitizer-global-variable-instrumentation)　·　MaskRay (宋方睿)

[2023-10-15](https://maskray.me/blog/2023-10-15-address-sanitizer-global-variable-instrumentation)

# AddressSanitizer：全局变量插桩

AddressSanitizer (ASan) 是一种编译器技术，通过一些额外检查来检测与可寻址性相关的内存错误。它由编译器插桩和运行时库两部分组成。简单来说：

- 编译器对全局变量、栈帧和堆分配进行插桩，以监控影子内存。
- 编译器还会对内存访问指令进行插桩，以检查影子内存。
- 如果发生错误，插入的代码会调用一个由运行时库实现的回调函数，报告错误及其堆栈跟踪。通常，程序会在显示错误消息后终止。

本文介绍全局变量插桩。

## 全局变量插桩

AddressSanitizer 会对某些具有 LLVM 外部链接或内部链接的已定义全局变量进行插桩。变量必须满足一系列条件才会被插桩。

- 它不是线程局部变量。
- 它的对齐较小。
- 它不是由 LLVM 生成的。
- 它在 LLVM IR 中没有 `no_sanitize_address` 属性。在 C/C++ 中使用 `__attribute__((no_sanitize("address")))` 或 `__attribute__((disable_sanitizer_instrumentation))` 标注变量时，变量会获得此属性。

```c
int g0;
const long g1 = 42;
```

每个被插桩的全局变量右侧都会填充一个 redzone，以检测越界访问。1  
2  
@g0 = dso_local global { i32, [28 x i8] } zeroinitializer, comdat, align 32  
@g1 = dso_local constant { i64, [24 x i8] } zeroinitializer, comdat, align 32

在 ELF 平台上，默认情况下（自 Clang 17.0 起），每个被插桩的全局变量都会获得一个关联的 `__asan_global_$name` 变量，该变量位于 `asan_globals` 节中。此外，还有若干相关变量，包括一些未命名变量（`@0` 和 `@1`）、`__odr_asan_gen_g0` 和 `__odr_asan_gen_g1`，以及元数据节点（`!0` 和 `!1`）；后文将更详细地讨论这些内容。

```llvm
@___asan_gen_.1 = private unnamed_addr constant [3 x i8] c"g0\00", align 1
@___asan_gen_.2 = private unnamed_addr constant [3 x i8] c"g1\00", align 1
@__asan_global_g0 = private global { i64, i64, i64, i64, i64, i64, i64, i64 } { i64 ptrtoint (ptr @0 to i64), i64 4, i64 32, i64 ptrtoint (ptr @___asan_gen_.1 to i64), i64 ptrtoint (ptr @___asan_gen_ to i64), i64 0, i64 0, i64 ptrtoint (ptr @__odr_asan_gen_g0 to i64) }, section "asan_globals", comdat($g0), !associated !0
@__asan_global_g1 = private global { i64, i64, i64, i64, i64, i64, i64, i64 } { i64 ptrtoint (ptr @1 to i64), i64 4, i64 32, i64 ptrtoint (ptr @___asan_gen_.2 to i64), i64 ptrtoint (ptr @___asan_gen_ to i64), i64 0, i64 0, i64 ptrtoint (ptr @__odr_asan_gen_g1 to i64) }, section "asan_globals", comdat($g1), !associated !1
@llvm.compiler.used = appending global [4 x ptr] [ptr @g0, ptr @g1, ptr @__asan_global_g0, ptr @__asan_global_g1], section "llvm.metadata"

!0 = !{ptr @g0}
!1 = !{ptr @g1}
```

模块构造函数 `asan.module_ctor` 会处理可由垃圾回收机制移除的 `asan_globals` 输入节。该构造函数调用运行时回调来注册被插桩的全局变量，其中包括毒化 redzone 和执行 ODR 违规检查。后文将讨论 ODR 违规检查。1  
2  
3  
4  
5  
6  
define internal void @asan.module_ctor() #0 comdat {  
 call void @__asan_init()  
 call void @__asan_version_mismatch_check_v8()  
 call void @__asan_register_elf_globals(i64 ptrtoint (ptr @___asan_globals_registered to i64), i64 ptrtoint (ptr @__start_asan_globals to i64), i64 ptrtoint (ptr @__stop_asan_globals to i64))  
 ret void  
}

运行时会毒化每个被插桩全局变量的 redzone。1  
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
void __asan_register_elf_globals(uptr *flag, void *start, void *stop) {  
 if (*flag) return;  
 if (!start) return;  
 CHECK_EQ(0, ((uptr)stop - (uptr)start) % sizeof(__asan_global));  
 __asan_global *globals_start = (__asan_global*)start;  
 __asan_global *globals_stop = (__asan_global*)stop;  
 __asan_register_globals(globals_start, globals_stop - globals_start);  
 *flag = 1;  
}  
  
void __asan_register_globals(__asan_global *globals, uptr n) {  
 if (!flags()-\>report_globals) return;  
 ...  
 for (uptr i = 0; i \< n; i++)  
 RegisterGlobal(&globals[i]);  
  
 // Poison the metadata. It should not be accessible to user code.  
 PoisonShadow(reinterpret_cast\<uptr\>(globals), n * sizeof(__asan_global),  
 kAsanGlobalRedzoneMagic);  
}  
  
static void RegisterGlobal(const Global *g) {  
 ...  
 if (CanPoisonMemory())  
 PoisonRedZones(*g);  
}

redzone 的影子内存中，每个完整粒度都会填入 0xf9（`kAsanGlobalRedzoneMagic`），而不完整粒度的填充方式与部分可寻址的栈内存类似。1  
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
ALWAYS_INLINE void PoisonRedZones(const Global &g) {  
 uptr aligned_size = RoundUpTo(g.size, ASAN_SHADOW_GRANULARITY);  
 FastPoisonShadow(g.beg + aligned_size, g.size_with_redzone - aligned_size,  
 kAsanGlobalRedzoneMagic);  
 if (g.size != aligned_size) {  
 FastPoisonShadowPartialRightRedzone(  
 g.beg + RoundDownTo(g.size, ASAN_SHADOW_GRANULARITY),  
 g.size % ASAN_SHADOW_GRANULARITY, ASAN_SHADOW_GRANULARITY,  
 kAsanGlobalRedzoneMagic);  
 }  
}

## global-buffer-overflow 示例

如果访问发生在被 0xf9 毒化的 redzone 字节内，或发生在 0xf9 之前的不完整 redzone 中，运行时将报告 `global-buffer-overflow` 错误。示例如下：

```c
cat > a.c <<e
#include <string.h>
int main(int argc, char **argv) {
  static char a[10];
  memset(a, 0, 10);
  return a[argc * 5];
}
e
clang -fsanitize=address a.c -o a
```

```plaintext
% ./a 1  # a[argc * 5] == a[10] is out-of-bounds
=================================================================
==240472==ERROR: AddressSanitizer: global-buffer-overflow on address 0x5592092356aa at pc 0x5592088dc38f bp 0x7ffd457ab520 sp 0x7ffd457ab518
READ of size 1 at 0x5592092356aa thread T0
    #0 0x5592088dc38e  (/tmp/c/a+0x14238e)
    #1 0x7fd59d38f6c9  (/lib/x86_64-linux-gnu/libc.so.6+0x276c9) (BuildId: 2ac5fa07c22f99cfd5dc47c70cd5f0e78b974269)
    #2 0x7fd59d38f784  (/lib/x86_64-linux-gnu/libc.so.6+0x27784) (BuildId: 2ac5fa07c22f99cfd5dc47c70cd5f0e78b974269)
    #3 0x559208800f80  (/tmp/c/a+0x66f80)

0x5592092356aa is located 0 bytes after global variable 'main.a' defined in 'a.c' (0x5592092356a0) of size 10
SUMMARY: AddressSanitizer: global-buffer-overflow (/tmp/c/a+0x14238e)
Shadow bytes around the buggy address:
  0x559209235400: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
  0x559209235480: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
  0x559209235500: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
  0x559209235580: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
  0x559209235600: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
=>0x559209235680: 00 00 00 00 00[02]f9 f9 00 00 00 00 00 00 00 00
  0x559209235700: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
  0x559209235780: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
  0x559209235800: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
  0x559209235880: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
  0x559209235900: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
Shadow byte legend (one shadow byte represents 8 application bytes):
...
```

## ODR 违规检查器

全局变量毒化机制提供了一种直接方法，可检测两个组件之间的变量定义差异，例如主可执行文件与共享对象之间，或两个共享对象之间的差异。这可以视为一类 ODR 违规。

```sh
echo 'int var; int main() { return var; }' > a.cc
echo 'long var;' > b.cc
clang++ -fpic -fsanitize=address -shared b.cc -o b.so
clang++ -fsanitize=address a.cc ./b.so -o a
```

```plaintext
% ./a
=================================================================
==1299789==ERROR: AddressSanitizer: odr-violation (0x56107ea3f500):
  [1] size=4 'var' a.cc in /tmp/c/a
  [2] size=8 'var' b.cc in ./b.so
These globals were registered at these points:
  [1]:
    #0 0x56107df99996  (/tmp/c/a+0x7b996)
    #1 0x56107df9aab9  (/tmp/c/a+0x7cab9)
    #2 0x7f72e5a457f5  (/lib/x86_64-linux-gnu/libc.so.6+0x277f5) (BuildId: 2ac5fa07c22f99cfd5dc47c70cd5f0e78b974269)

  [2]:
    #0 0x56107df99996  (/tmp/c/a+0x7b996)
    #1 0x56107df9aab9  (/tmp/c/a+0x7cab9)
    #2 0x7f72e604dd2d  (/lib64/ld-linux-x86-64.so.2+0x4d2d) (BuildId: accffc5784c4a469d09348e3f7ec53a74096fbd3)

==1299789==HINT: if you don't care about these errors you may set ASAN_OPTIONS=detect_odr_violation=0
SUMMARY: AddressSanitizer: odr-violation: global 'var' at a.cc in /tmp/c/a
==1299789==ABORTING
```

默认模式 `detect_odr_violation=2` 还禁止变量上的符号介入。即使把 `b.cc` 中的 `long` 改为 `int`，仍会遇到 `odr-violation` 错误。相比之下，使用 `detect_odr_violation=1` 时，如果注册变量的大小相同，错误便会被抑制。1  
2  
3  
4  
5  
% ASAN_OPTIONS=detect_odr_violation=1 ./a  
% ASAN_OPTIONS=detect_odr_violation=2 ./a  
=================================================================  
==2574052==ERROR: AddressSanitizer: odr-violation (0x562d39db1200):  
...

对于名为 `$var` 的变量，会创建一个单字节变量 `__odr_asan_gen_$var`，其链接属性和可见性与原变量相同（链接属性实际上必须是 `external`）。

如果 `$var` 在两个已插桩模块中都有定义，由于符号介入，两个 `__odr_asan_gen_$var` 符号会引用同一个副本。注册 `$var` 时，运行时检查 `__odr_asan_gen_$var` 是否已经为 1；若是，程序便存在 ODR 违规，否则将 `__odr_asan_gen_$var` 设为 1。

```llvm
@__odr_asan_gen_g0 = global i8 0, align 1
@__odr_asan_gen_g1 = global i8 0, align 1

@0 = private alias { i32, [28 x i8] }, ptr @g0
@1 = private alias { i32, [28 x i8] }, ptr @g1
```

私有别名 `@0` 和 `@1` 源自 [D15642](http://reviews.llvm.org/D15642)。

如果 `a.supp` 包含以下文本，通过环境变量 `ASAN_OPTIONS=suppressions=a.supp` 运行程序时，便会抑制由变量名 `var` 引起的错误。1  
odr_violation:^var$

ODR 违规发生在两个不同的链接单元之间，例如 `exe` 和 `b.so`。采用静态链接时，如果归档成员 `b.a` 未被提取，归档成员提取语义会使该问题不再出现。

### ODR 指示器

前面的示例使用了 `-fsanitize-address-use-odr-indicator`。

在 Clang 16 之前，非 Windows 平台默认使用 `-fno-sanitize-address-use-odr-indicator`。运行时通过检查变量的 redzone 是否已被毒化来判断它是否已注册；若 redzone 已被毒化，则报告 ODR 违规。1  
2  
3  
4  
5  
@___asan_gen_.1 = private unnamed_addr constant [3 x i8] c"g0\\00", align 1  
@___asan_gen_.2 = private unnamed_addr constant [3 x i8] c"g1\\00", align 1  
@__asan_global_g0 = private global { i64, i64, i64, i64, i64, i64, i64, i64 } { i64 ptrtoint (ptr @g0 to i64), i64 4, i64 32, i64 ptrtoint (ptr @___asan_gen_.1 to i64), i64 ptrtoint (ptr @___asan_gen_ to i64), i64 0, i64 0, i64 0 }, section "asan_globals", !associated !0  
@__asan_global_g1 = private global { i64, i64, i64, i64, i64, i64, i64, i64 } { i64 ptrtoint (ptr @g1 to i64), i64 8, i64 32, i64 ptrtoint (ptr @___asan_gen_.2 to i64), i64 ptrtoint (ptr @___asan_gen_ to i64), i64 0, i64 0, i64 0 }, section "asan_globals", !associated !1  
@llvm.compiler.used = appending global [4 x ptr] [ptr @g0, ptr @g1, ptr @__asan_global_g0, ptr @__asan_global_g1], section "llvm.metadata"

此模式无需像 `__odr_asan_gen_$var` 这样的额外变量，但混用已插桩与未插桩组件时可能产生交互问题。对于共享对象，如果 `__asan_global_$var` 中对 `$var` 的引用因符号介入而指向未插桩变量，就可能误报“以下全局变量未正确对齐”。

在 Clang 16 中，我让非 Windows 目标默认使用 `-fsanitize-address-use-odr-indicator`（参见 https://reviews.llvm.org/D137227）。

（此外，[D127911](https://reviews.llvm.org/D127911) 将 ODR 指示器的符号名改为 `__odr_asan_gen_$demangled`。）

### 拷贝重定位

私有别名与拷贝重定位之间存在一种有趣的交互。该问题已在 [PR68016](https://gcc.gnu.org/PR68016) 中报告。

Clang 16 及更高版本默认使用的 `-fsanitize-address-use-odr-indicator` 无法检测下面的 `global-buffer-overflow` 错误：

```sh
echo 'int f[5] = {1};' > foo.cc
echo 'extern int f[5]; int main() { return f[5]; }' > a.cc
clang++ -fpic -fsanitize=address -mllvm -asan-use-private-alias=1 -shared foo.cc -o foo1.so
clang++ -fno-pic -fsanitize=address -mllvm -asan-use-private-alias=1 -no-pie a.cc ./foo1.so -o a1
./a1 # no error

clang++ -fpic -fsanitize=address -mllvm -asan-use-private-alias=0 -shared foo.cc -o foo0.so
clang++ -fno-pic -fsanitize=address -mllvm -asan-use-private-alias=0 -no-pie a.cc ./foo0.so -o a0
./a0 # error
```

`foo.cc` 中 `f` 的定义经过插桩，因此会创建 `__asan_global_f`。然而，由于拷贝重定位，可执行文件实际访问的是链接器创建的副本。

当 `-asan-use-private-alias=1` 生效时（自 Clang 16 起为默认设置），`__asan_global_f` 引用共享对象内未使用的副本。可执行文件访问经过拷贝重定位的变量，其 redzone 未被毒化，因此不会报错。

反之，当 `-asan-use-private-alias=0` 生效时，`__asan_global_f` 引用经过拷贝重定位的变量，并毒化可执行文件内的 redzone。因此，访问 `f[5]` 会触发预期错误。

## 垃圾回收

自 Clang 17 起，`asan.module_ctor` 默认被放置在一个 COMDAT 组中。当多个经过插桩的可重定位目标文件被链接在一起时，只会保留一个 `asan.module_ctor`。

`__asan_global_g0` 位于一个带有 `SHF_LINK_ORDER` 标志、并关联到 `g0` 定义所在节的节中。链接时，如果链接器丢弃定义 `g0` 的节，也会丢弃包含 `__asan_global_g0` 的 `asan_globals` 节。有关 `SHF_LINK_ORDER` 的更多细节，请参阅[元数据节、COMDAT 与 SHF_LINK_ORDER](https://maskray.me/blog/2021-01-31-metadata-sections-comdat-and-shf-link-order)。

在 Clang 17 之前，默认使用 `-fno-sanitize-address-globals-dead-stripping`。在此模式下，插桩会把指向被插桩全局变量的指针放入元数据数组，并调用 `__asan_register_globals`；`__asan_register_globals` 随后遍历数组并注册每个全局变量。

```llvm
@g0 = dso_local global { i32, [28 x i8] } zeroinitializer, align 32
@g1 = dso_local global { i64, [24 x i8] } zeroinitializer, align 32

@___asan_gen_.1 = private unnamed_addr constant [3 x i8] c"g0\00", align 1
@___asan_gen_.2 = private unnamed_addr constant [3 x i8] c"g1\00", align 1

@llvm.compiler.used = appending global [2 x ptr] [ptr @g0, ptr @g1], section "llvm.metadata"
@0 = internal global [2 x { i64, i64, i64, i64, i64, i64, i64, i64 }] [{ i64, i64, i64, i64, i64, i64, i64, i64 } { i64 ptrtoint (ptr @1 to i64), i64 4, i64 32, i64 ptrtoint (ptr @___asan_gen_.1 to i64), i64 ptrtoint (ptr @___asan_gen_ to i64), i64 0, i64 0, i64 ptrtoint (ptr @__odr_asan_gen_g0 to i64) }, { i64, i64, i64, i64, i64, i64, i64, i64 } { i64 ptrtoint (ptr @2 to i64), i64 4, i64 32, i64 ptrtoint (ptr @___asan_gen_.2 to i64), i64 ptrtoint (ptr @___asan_gen_ to i64), i64 0, i64 0, i64 ptrtoint (ptr @__odr_asan_gen_g1 to i64) }]

@1 = private alias { i32, [28 x i8] }, ptr @g0
@2 = private alias { i32, [28 x i8] }, ptr @g1

define internal void @asan.module_ctor() #0 {
  call void @__asan_init()
  call void @__asan_version_mismatch_check_v8()
  call void @__asan_register_globals(i64 ptrtoint (ptr @0 to i64), i64 2)
  ret void
}
```

`asan.module_ctor` 引用元数据数组 `@0`，后者又引用 `@1` 和 `@2`；`@1` 和 `@2` 分别引用全局变量 `g0` 和 `g1`。遗憾的是，这意味着基于节的垃圾回收无法丢弃 `g0` 和 `g1`。

值得注意的是，此版本的 `asan.module_ctor` 并未放置于 COMDAT 组内。在另一个编译单元中，单独的 `asan.module_ctor` 引用的是不同的元数据数组。因此，这些 `asan.module_ctor` 函数无法共享同一实现。

在一个链接后的组件中，`__asan_init` 和 `__asan_version_mismatch_check_v8` 会被多次调用，从而产生少量开销。

遗憾的是，Clang 17 默认启用 `-fsanitize-address-globals-dead-stripping` 时存在一个 bug。具体而言，如果没有全局变量且唯一模块 ID 非空，编译器会创建一个不含任何 `__asan_register_elf_globals` 调用的 COMDAT `asan.module_ctor`。如果链接器选中这个 COMDAT 副本，链接单元便缺少 `__asan_register_elf_globals` 调用，导致 redzone 未被毒化，ODR 违规检查器也无法工作。

我已在主分支中修复此问题（[#67745](https://github.com/llvm/llvm-project/pull/67745)），但 LLVM 17.0.2 尚未包含该修复。

### 全局变量元数据

在 Clang 15 之前，Clang 的插桩包含 `llvm.asan.globals`，AddressSanitizer 运行时需要依靠相应的目标文件特性进行符号化。

[D127552](https://reviews.llvm.org/D127552) 启用了用于符号化的调试信息，[D127911](https://reviews.llvm.org/D127911) 则删除了元数据节点 `llvm.asan.globals`。

## initialization-order-fiasco

AddressSanitizer 提供了一项检查，用于检测一个全局变量的动态初始化器是否访问了另一个编译单元中动态初始化的全局变量，这有助于识别某些初始化顺序问题。该检查能捕获部分初始化顺序混乱问题。

以下是一个示例：1  
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
cat \> a0.cc \<\<'eof'  
#include \<stdio.h\>  
extern int a1;  
static int fa0() { return 1; }  
int a0 = fa0();  
int main() { printf("%d %d\\n", a0, a1); }  
eof  
cat \> a1.cc \<\<'eof'  
extern int a0;  
static int fa1() { return a0+1; }  
int a1 = fa1();  
eof  
clang++ -fsanitize=address a0.cc a1.cc -o a  
 1  
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
% ASAN_OPTIONS=strict_init_order=1 ./a  
=================================================================  
==124921==ERROR: AddressSanitizer: initialization-order-fiasco on address 0x5577b1cd6b00 at pc 0x5577b12fbbca bp 0x7ffe75a0a280 sp 0x7ffe75a0a260  
READ of size 4 at 0x5577b1cd6b00 thread T0  
 #0 0x5577b12fbbc9 in fa1() /tmp/t/d/a1.cc:2:27  
 #1 0x5577b12fbbec in __cxx_global_var_init /tmp/t/d/a1.cc:3:10  
 #2 0x5577b12fbc64 in _GLOBAL__sub_I_a1.cc /tmp/t/d/a1.cc  
 #3 0x7ff44e0107f5 in call_init csu/../csu/libc-start.c:145:3  
 #4 0x7ff44e0107f5 in __libc_start_main csu/../csu/libc-start.c:347:5  
 #5 0x5577b11b46d0 in _start (/tmp/t/d/a+0x766d0)  
  
0x5577b1cd6b00 is located 0 bytes inside of global variable 'a0' defined in '/tmp/t/d/a0.cc:4' (0x5577b1cd6b00) of size 4  
 registered at:  
 #0 0x5577b11d1da4 in __asan_register_globals /usr/local/google/home/maskray/llvm/compiler-rt/lib/asan/asan_globals.cpp:363:3  
 #1 0x5577b11d2181 in __asan_register_elf_globals /usr/local/google/home/maskray/llvm/compiler-rt/lib/asan/asan_globals.cpp:346:3  
 #2 0x5577b12fbb57 in asan.module_ctor a0.cc  
 #3 0x7ff44e0107f5 in call_init csu/../csu/libc-start.c:145:3  
 #4 0x7ff44e0107f5 in __libc_start_main csu/../csu/libc-start.c:347:5  
  
SUMMARY: AddressSanitizer: initialization-order-fiasco /tmp/t/d/a1.cc:2:27 in fa1()  
...

启用 `check_initialization_order` 但禁用 `strict_init_order` 时，AddressSanitizer 会执行弱检查，允许即将初始化的编译单元访问另一个已初始化编译单元中的全局变量。在这种情况下，上面的示例不会报错：1  
2  
% ASAN_OPTIONS=check_initialization_order=1:strict_init_order=0 ./a  
1 2

对于下面的情况，弱检查仍能捕获初始化顺序问题：1  
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
cat \> a0.cc \<\<'eof'  
#include \<stdio.h\>  
extern int a1;  
int a0 = []() { return a1-1; }();  
int main() { printf("%d %d\\n", a0, a1); }  
eof  
cat \> a1.cc \<\<'eof'  
extern int a0;  
static int fa1() { return 2; }  
int a1 = fa1();  
eof  
clang++ -g -fsanitize=address a0.cc a1.cc -o a  
ASAN_OPTIONS=check_initialization_order=1:strict_init_order=0 ./a

Clang 会将 C++ 动态初始化转换成一个全局初始化函数，放在 `llvm.global_ctors` 列表中。AddressSanitizer 会用 `__asan_before_dynamic_init` 和 `__asan_after_dynamic_init` 增强这个全局初始化函数。当启用 `check_initialization_order` 时，这两个函数协同工作以检查初始化顺序问题。

对于带有初始化器的、已被插桩的全局变量，`has_dynamic_init` 元数据中的 `__asan_global` 变量会被设为 true。这些变量会被收集到 `dynamic_init_globals` 数组中。

`__asan_before_dynamic_init` 对每个编译单元调用。该函数会遍历 `dynamic_init_globals` 并毒化其中 `DynInitGlobal::initialized` 值为 false 的那些变量。随后，执行全局初始化函数。如果它访问了已被毒化的内存，则会触发初始化顺序问题的报告。之后，`__asan_after_dynamic_init` 处理这些全局变量，取消对它们的毒化。

```cpp
void __asan_before_dynamic_init(const char *module_name) {
  ...
  for (uptr i = 0, n = dynamic_init_globals->size(); i < n; ++i) {
    DynInitGlobal &dyn_g = (*dynamic_init_globals)[i];
    const Global *g = &dyn_g.g;
    if (dyn_g.initialized)
      continue;
    if (g->module_name != module_name)
      PoisonShadowForGlobal(g, kAsanInitializationOrderMagic);
    else if (!strict_init_order)
      dyn_g.initialized = true;
  }
}

void __asan_after_dynamic_init() {
  ...
  for (uptr i = 0, n = dynamic_init_globals->size(); i < n; ++i) {
    DynInitGlobal &dyn_g = (*dynamic_init_globals)[i];
    const Global *g = &dyn_g.g;
    if (!dyn_g.initialized) {
      // Unpoison the whole global.
      PoisonShadowForGlobal(g, 0);
      // Poison redzones back.
      PoisonRedZones(*g);
    }
  }
}
```

**O(N) 优化**

每个 TU 都会调用一对 `__asan_before_dynamic_init`/`__asan_after_dynamic_init`。由于 `__asan_after_dynamic_init` 会取消所有全局变量的毒化，整体复杂度为 O(N^2)，其中 N 是全局变量或 TU 的数量。

[#101837](https://github.com/llvm/llvm-project/pull/101837) 在使用 lld 的 `SANITIZER_CAN_USE_PREINIT_ARRAY` 平台（Linux，非共享库）上将复杂度优化为 O(N)。`__asan_before_dynamic_init` 已经执行增量毒化，只毒化前一个 TU 的全局变量并取消当前 TU 的毒化（见 [#101597](https://github.com/llvm/llvm-project/pull/101597)）。关键思路是抑制所有中间的 `__asan_after_dynamic_init` 调用（`allow_after_dynamic_init` 初始为 false），并通过注册在 `.init_array.65537` 中的 `UnpoisonBeforeMain` 执行一次最终的取消毒化操作。

lld 按数字后缀对 `.init_array` 子段进行排序，因此优先级 65537（大于默认的 65535）可确保 `UnpoisonBeforeMain` 在所有普通构造函数之后运行。GNU ld 不会以这种方式排序 `.init_array.65537`，因此该优化会在保证正确性的前提下退化为 O(N^2)。

---

当被访问的变量位于另一个链接单元中时，此检查适用。

例如，假设 `b.so` 由 `b0.cc` 和 `b1.cc` 组成，而主可执行文件 `a` 包含 `a0.cc` 和 `a1.cc`。1  
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
cat \> a0.cc \<\<'eof'  
#include \<stdio.h\>  
extern int a1, b0, b1;  
static int fa0() { return 1; }  
int a0 = fa0();  
int main() { printf("%d %d %d %d\\n", a0, a1, b0, b1); }  
eof  
echo 'static int fa1() { return 2; } int a1 = fa1();' \> a1.cc  
echo 'static int fb0() { return 3; } int b0 = fb0();' \> b0.cc  
echo 'static int fb1() { return 4; } int b1 = fb1();' \> b1.cc  
sed 's/^ /\\t/' \> Makefile \<\<'eof'  
.MAKE.MODE := meta curDirOk=true  
CXX := clang++  
CXXFLAGS := -g -fsanitize=address  
a: a0.cc a1.cc b.so  
 ${LINK.cc} -Wl,-rpath=. $\> -o $@  
b.so: b0.cc b1.cc  
 ${LINK.cc} -fpic -shared $\> -o $@  
clean:  
 rm -f *.meta a b.so  
eof  
bmake

在 `check_initialization_order=1,strict_init_order=0` 模式下，

- 注册 `b0.cc` 和 `b1.cc` 中的全局变量
- b0.cc：`__asan_before_dynamic_init` 将 `b0` 标记为已初始化并毒化 `b1`。运行全局初始化后，`__asan_register_globals` 取消 `b1` 的毒化
- b1.cc：`__asan_before_dynamic_init` 将 `b1` 标记为已初始化并毒化 `b0`。运行全局初始化后，`__asan_register_globals` 取消 `b0` 的毒化
- 注册 `a0.cc` 和 `a1.cc` 中的全局变量
- a0.cc：`__asan_before_dynamic_init` 将 `a0` 标记为已初始化并毒化 `a1`。运行全局初始化后，`__asan_register_globals` 取消 `a1` 的毒化
- a1.cc：`__asan_before_dynamic_init` 将 `a1` 标记为已初始化并毒化 `a0`。运行全局初始化后，`__asan_register_globals` 取消 `a0` 的毒化

在 `check_initialization_order=1,strict_init_order=1` 模式下，

- 注册 `b0.cc` 和 `b1.cc` 中的全局变量
- b0.cc：`__asan_before_dynamic_init` 毒化 `b1`，然后运行全局初始化
- b1.cc：`__asan_before_dynamic_init` 毒化 `b0`，然后运行全局初始化
- 注册 `a0.cc` 和 `a1.cc` 中的全局变量
- a0.cc：`__asan_before_dynamic_init` 毒化 `b0,b1,a1`。运行全局初始化后，`__asan_register_globals` 取消 `b0,b1,a1` 的毒化
- a1.cc：`__asan_before_dynamic_init` 毒化 `b0,b1,a0`。运行全局初始化后，`__asan_register_globals` 取消 `b0,b1,a0` 的毒化

请注意，无法检测由 `b.so` 访问 `a` 所引起的违规。

可以通过在 `asan_ignorelist.txt` 中添加以下条目来禁用插桩：1  
global:var=init

无法使用 `ASAN_OPTIONS=suppressions=a.supp` 抑制 `initialization-order-fiasco` 错误。
