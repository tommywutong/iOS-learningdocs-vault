---
title: UndefinedBehaviorSanitizer 详解
source: MaskRay (宋方睿)
source_key: maskray
source_url: 'https://maskray.me/blog/2023-01-29-all-about-undefined-behavior-sanitizer'
original_language: en
published: 2023-01-29
status: active
license: 未声明 → 仅私有归档
archived_at: 2026-07-27
content_hash: 'sha256:ac1ee21c41bdef31'
translated: true
---

> 原文：[UndefinedBehaviorSanitizer 详解](https://maskray.me/blog/2023-01-29-all-about-undefined-behavior-sanitizer)　·　MaskRay (宋方睿)

[2023-01-29](https://maskray.me/blog/2023-01-29-all-about-undefined-behavior-sanitizer)

# UndefinedBehaviorSanitizer 详解

更新于 2025-01。

[UndefinedBehaviorSanitizer](https://clang.llvm.org/docs/UndefinedBehaviorSanitizer.html)（UBSan）是用于 C/C++ 的未定义行为检测器，由代码插桩和运行时组成，两部分都有多种独立实现。

Clang 于 2009 年 12 月[实现了](https://github.com/llvm/llvm-project/commit/a3e2ff19e59c587ea14611eb64400c6d0ecabcee)最初的几项检查，当时名为 `-fcatch-undefined-behavior`。2012 年加入 `-fsanitize=undefined` 后，`-fcatch-undefined-behavior` 被[移除](https://github.com/llvm/llvm-project/commit/b1b0ab41e79f4f11ab21e6e56ded7147241f8615)。GCC 4.9 于 2013 年 8 月[实现了](https://maskray.me/blog/de5a5fa1395db2cb5da4d0593fef40ec22378576) `-fsanitize=undefined`。

Clang 使用的运行时位于 `llvm-project/compiler-rt/lib/ubsan`。GCC 会不时同步 compiler-rt 中 Sanitizer 部分的下游分支（`libsanitizer`）。本文末尾还列出了一些替代运行时实现。

## 可用的检查

UndefinedBehaviorSanitizer 提供了许多可检测的未定义行为[检查](https://clang.llvm.org/docs/UndefinedBehaviorSanitizer.html)。你可以指定 `-fsanitize=xxx,yyy`（其中 xxx 和 yyy 是具体检查的名称），或者更常见的是指定 `-fsanitize=undefined` 来启用所有检查。

部分检查虽然不涉及语言标准意义上的未定义行为，但常常是代码坏味道，会带来出乎意料的结果。这些检查包括 `implicit-unsigned-integer-truncation`, `implicit-integer-sign-change`, `unsigned-integer-overflow` 等。

我们可以使用 `-###` 来获取默认的 UBSan 检查列表。 1  
2  
% clang -fsanitize=undefined -xc /dev/null '-###'  
... -fsanitize=alignment,array-bounds,bool,builtin,enum,float-cast-overflow,function,integer-divide-by-zero,nonnull-attribute,null,pointer-overflow,return,returns-nonnull-attribute,shift-base,shift-exponent,signed-integer-overflow,unreachable,vla-bound,vptr" "-fsanitize-recover=alignment,array-bounds,bool,builtin,enum,float-cast-overflow,function,integer-divide-by-zero,nonnull-attribute,null,pointer-overflow,returns-nonnull-attribute,shift-base,shift-exponent,signed-integer-overflow,vla-bound,vptr" ...

GCC 实现的[检查种类略少于](https://gcc.gnu.org/onlinedocs/gcc/Instrumentation-Options.html##:~:text=fsanitize=undefined) Clang。

如果启用了“undefined”组中的任何检查，`#if __has_feature(undefined_behavior_sanitizer)` 将生效。

## 模式

UBSan 提供了 3 种模式，以便在代码体积与诊断详细程度之间进行权衡。

- 默认模式
- 最小运行时（`-fsanitize-minimal-runtime`）
- 陷阱模式（`-fsanitize-trap=undefined`）：无运行时

我们使用以下程序来比较插桩和运行时的行为。 1  
2  
3  
4  
5  
6  
7  
8  
#include \<stdio.h\>  
int foo(int a) { return a * 2; }  
int main() {  
 int x;  
 scanf("%d", &x);  
 printf("a %d\\n", foo(x));  
 printf("b %d\\n", foo(x));  
}

### 默认模式

使用总括选项 `-fsanitize=undefined` 或具体选项 `-fsanitize=signed-integer-overflow` 时，Clang 会为 `foo` 生成以下 LLVM IR：

```llvm
define dso_local i32 @foo(i32 noundef %a) local_unnamed_addr #0 {
entry:
  %0 = add i32 %a, 1073741824
  %1 = icmp sgt i32 %0, -1
  br i1 %1, label %cont, label %handler.mul_overflow, !prof !4, !nosanitize !5

handler.mul_overflow:                             ; preds = %entry
  %2 = zext i32 %a to i64, !nosanitize !5
  tail call void @__ubsan_handle_mul_overflow(ptr nonnull @1, i64 %2, i64 2) #3, !nosanitize !5
  br label %cont, !nosanitize !5

cont:                                             ; preds = %handler.mul_overflow, %entry
  %3 = shl i32 %a, 1
  ret i32 %3
}
```

`add` 和 `icmp` 指令检查参数是否位于 [-0x40000000, 0x40000000) 范围内（即不会溢出）。如果是，就进入 `cont` 分支并返回未溢出的结果；否则，生成的代码会调用运行时实现的 `__ubsan_handle_mul_overflow` 回调，并传入描述源代码位置的参数。

默认情况下，除 `return,unreachable` 外，所有 UBSan 检查都可恢复（即非致命）。`__ubsan_handle_mul_overflow`（或其他回调）输出错误后，程序仍会继续执行。运行时会标记该源代码位置，并[抑制](https://github.com/llvm/llvm-project/commit/765c266892d712db91b2a1677584f09feb862109)此后来自同一位置的错误。这种去重机制可以减少日志噪音；一次程序运行仍可能报告多个不同源代码位置的错误。

可以让 Clang 在出现 UBSan 错误时退出程序（错误码默认为 1，可用 `UBSAN_OPTIONS=exitcode=2` 自定义）。只需指定 `-fno-sanitize-recover`（`-fno-sanitize-recover=all` 的别名）、`-fno-sanitize-recover=undefined` 或 `-fno-sanitize-recover=signed-integer-overflow`。此时会生成一个不返回的回调来代替 `__ubsan_handle_mul_overflow`。注意，生成的 LLVM IR 会以 `unreachable` 指令结束基本块。1  
2  
3  
4  
handler.mul_overflow: ; preds = %entry  
 %2 = zext i32 %a to i64, !nosanitize !5  
 tail call void @__ubsan_handle_mul_overflow_abort(ptr nonnull @1, i64 %2, i64 2) #4, !nosanitize !5  
 unreachable, !nosanitize !5

#### 链接

UBSan 回调由运行时提供。执行链接操作时，需要告诉编译器驱动程序链接该运行时，可以通过指定 `-fsanitize=undefined` 实现。（实际上，任何需要运行时的具体 UBSan 检查都可以，例如 `-fsanitize=signed-integer-overflow`。）

```sh
clang -c -O2 -fsanitize=undefined a.c
clang -fsanitize=undefined a.o -o a
```

某些检查（`function,vptr`）会调用实现在 `libclang_rt.ubsan_standalone_cxx.a` 中的 C++ 特定回调。我们需要使用 `clang++ -fsanitize=undefined` 来进行链接操作（或使用 `clang -fsanitize=undefined -fsanitize-link-c++-runtime`).

```plaintext
% clang -fsanitize=undefined a.o '-###' |& grep --color ubsan
... "--whole-archive" ".../libclang_rt.ubsan_standalone.a" "--no-whole-archive" "--dynamic-list=.../libclang_rt.ubsan_standalone.a.syms" ...
% clang++ -fsanitize=undefined a.o '-###' |& grep --color ubsan
... "--whole-archive" ".../libclang_rt.ubsan_standalone.a" "--no-whole-archive" "--dynamic-list=.../libclang_rt.ubsan_standalone.a.syms" "--whole-archive" ".../libclang_rt.ubsan_standalone_cxx.a" "--no-whole-archive" "--dynamic-list=.../libclang_rt.ubsan_standalone_cxx.a.syms" ...
% clang++ -fsanitize=undefined -shared-libsan a.o '-###' |& grep --color ubsan
... ".../libclang_rt.ubsan_standalone.so" ...
```

当链接可执行文件时，在多数目标上使用默认的 `-static-libsan` 模式，Clang Driver 会将 `--whole-archive $resource_dir/lib/$triple/libclang_rt.ubsan.a --no-whole-archive` 传递给链接器。GCC 及一些平台倾向于共享运行时/动态运行时。参见[All about sanitizer interceptors](https://maskray.me/blog/2023-01-08-all-about-sanitizer-interceptors#elf-platforms).

某些 Sanitizer（`address`、`memory`、`thread` 等）会附带一份 UBSan 运行时文件。

### 最小运行时

默认模式提供详细的诊断信息，帮助程序员识别未定义行为。但另一方面，详细的日志有助于攻击者，且在某些配置中代码体积可能成为问题。

UBSan 提供一种最小运行时模式，只记录极少量信息。为编译操作和链接操作都指定 `-fsanitize-minimal-runtime` 以启用该模式。

```plaintext
% clang -fsanitize=undefined -fsanitize-minimal-runtime a.c -o a
% ./a <<< 1073741824
ubsan: mul-overflow by 0x000055565bab6839
a -2147483648
b -2147483648
% clang -fsanitize=undefined -fno-sanitize-recover -fsanitize-minimal-runtime a.c -o a
% ./a <<< 1073741824
ubsan: mul-overflow by 0x000056443f9a7839
[1]    3857513 IOT instruction  ./a <<< 1073741824
```

在生成的 LLVM IR 中，会使用另一组回调 LLVM。它们不接受参数，因此使检测后的代码体积显著减小。`__ubsan_handle_*_minimal`

```llvm
handler.mul_overflow:                             ; preds = %entry
  tail call void @__ubsan_handle_mul_overflow_minimal() #4, !nosanitize !6
  br label %cont, !nosanitize !6
```

UBSan 最小运行时使用一组独立的运行时文件（UBS）来减小运行时大小。1`libclang_rt.ubsan_minimal.*`  
2  
% clang -fsanitize=undefined -fsanitize-minimal-runtime a.c '-###' |& grep --color=auto ubsan_minimal  
... "--whole-archive" "/tmp/Rel/lib/clang/17/lib/x86_64-unknown-linux-gnu/libclang_rt.ubsan_minimal.a" "--no-whole-archive" "--dynamic-list=/tmp/Rel/lib/clang/17/lib/x86_64-unknown-linux-gnu/libclang_rt.ubsan_minimal.a.syms" ...

2025 年 11 月，新增了 `-fsanitize-handler-preserve-all-regs`，为最小运行时回调赋予 minimal-runtime 调用约定（它们被重命名为 `preserve_all`）。`__ubsan_handle_*_minimal_preserve` 调用的定义是保留所有寄存器，因此编译器不再围绕每次检查溢出/重载 caller-saved 寄存器，从而进一步缩小检测后的代码。该驱动程序仅在 AArch64 和 `preserve_all` 上同时与 caller-saved 一起时才启用该选项。`-fsanitize-minimal-runtime`x86-64.

### 陷阱模式

当 `-fsanitize=signed-integer-overflow` 生效时，我们可以指定 `-fsanitize-trap=signed-integer-overflow`，使 Clang 发射陷阱指令而非回调。与默认模式相比，这将大幅减小检测带来的代码体积膨胀。

通常，我们指定总括选项[`-fsanitize-trap=undefined`](https://reviews.llvm.org/D10464)或 `-fsanitize-trap`（作为 `-fsanitize-trap=all`). 1  
clang -S -emit-llvm -O2 -fsanitize=undefined -fsanitize-trap=undefined a.c

（最初的 `-fcatch-undefined-behavior` 补丁于 2013 年添加了 `-fsanitize-undefined-trap-on-error`，该选项现在是 `-fsanitize-trap=undefined`. `-fsanitize-undefined-trap-on-error` 的别名。[GCC 在 Clang 中已废弃，不应用于新项目。](https://gcc.gnu.org/PR109489).)

功能请求 LLVM。）LLVM 不同于调用回调，生成的 LLVM IR 会调用 LLVM 内建函数 `llvm.ubsantrap`，该函数降级为一条终止程序的陷阱指令。作为避免 UBSan 回调的附带好处，我们不需要运行时。因此，UBS 可以省略链接操作。注意：`-fsanitize=undefined` 覆盖 `-fsanitize-trap=xxx``-fsanitize-recover=xxx`.

```llvm
define dso_local i32 @foo(i32 noundef %a) local_unnamed_addr #0 {
entry:
  %0 = add i32 %a, 1073741824
  %1 = icmp sgt i32 %0, -1
  br i1 %1, label %cont, label %trap, !nosanitize !5

trap:                                             ; preds = %entry
  tail call void @llvm.ubsantrap(i8 12) #4, !nosanitize !5
  unreachable, !nosanitize !5

cont:                                             ; preds = %entry
  %2 = shl nsw i32 %a, 1
  ret i32 %2
}
```

`llvm.ubsantrap` 有一个整数参数。在某些架构上，这可以改变陷阱指令的编码，对应不同的错误类型。

在 x86-64 上，`llvm.ubsantrap` 会降级为 4 字节的 `ud1l ubsan_type(%eax),%eax`（带地址大小覆盖前缀的 UD1；`ud1l` 是 AT&T 语法）。AArch64 则提供带 16 位立即数的 `BRK`。

然而，许多其他架构没有为其陷阱指令提供足够的编码空间。例如，PowerPC 提供 `trap`（作为 `tw 31,0,0` 的别名）。在 `tw TO,RA,RB` 中，当我们指定 `RA=RB=0` 时，5 位的 `TO` 只能使用 4 位，这是不够的。

对于 AArch64 和 x86-64，我们可以注册一个信号处理程序来反汇编 `si->si_addr` 处的指令。它可以区分 UBSan 检查错误与其他故障。我们甚至可以解析 UBS 中的 UBSan 类型编号 UBS[`#define LIST_SANITIZER_CHECKS`](https://github.com/llvm/llvm-project/blob/main/clang/lib/CodeGen/CodeGenFunction.h)，并给出更好的诊断信息。

```cpp
#include <signal.h>
#include <stdint.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

static void handler(int signo, siginfo_t *si, void *uc) {
#ifdef __aarch64__
  if (signo == SIGTRAP && si && si->si_addr) {
    uint32_t insn;
    memcpy(&insn, si->si_addr, sizeof(insn));
    if ((insn & 0xffe0001f) == 0xd4200000 && ((insn >> 13) & 255) == 'U') {
      char buf[64];
      int len = snprintf(buf, sizeof buf, "TRAP(%u) at %p, possibly UBSan error\n", (insn>>5 & 255), si->si_addr);
      write(STDOUT_FILENO, buf, len);
    }
  }
#endif
#ifdef __x86_64__
  if (signo == SIGILL && si && si->si_code == ILL_ILLOPN && si->si_addr) {
    auto *pc = reinterpret_cast<const unsigned char *>(si->si_addr);
    if (pc[0] == 0x67 && pc[1] == 0x0f && pc[2] == 0xb9 && pc[3] == 0x40) {
      char buf[64];
      int len = snprintf(buf, sizeof buf, "UD1 at %p, possibly UBSan error\n", pc);
      write(STDOUT_FILENO, buf, len);
    }
  }
#endif
  abort();
}

int foo(int a) { return a * 2; }

int main() {
  struct sigaction sa = {};
  sa.sa_flags = SA_SIGINFO;
  sa.sa_sigaction = &handler;
#if defined(__aarch64__)
  sigaction(SIGTRAP, &sa, nullptr);
#elif defined(__x86_64__)
  sigaction(SIGILL, &sa, nullptr);
#endif

  int x;
  scanf("%d", &x);
  printf("a %d\n", foo(x));
  printf("b %d\n", foo(x));
}
```

```plaintext
% clang++ -fsanitize=undefined -fsanitize-trap=undefined a.cc -o a
% ./a <<< 1073741824
TRAP(12) at 0xaaaaea87eb48, possibly UBSan error
[1]    529341 abort (core dumped)  ./a <<< 1073741824
```

TODO: [arm64：支持 Clang UBSANtrap 代码以改进报告](https://lore.kernel.org/r/20230203173946.gonna.972-kees@kernel.org)

#### 合并陷阱

优化时，Clang 会把一个函数内同类检查的所有陷阱点合并为一个 `llvm.ubsantrap`，因此不同故障会共用同一陷阱地址。这可以节省代码体积，却也意味着出错时的程序计数器无法再区分具体检查。指定 [`-fno-sanitize-merge`](https://github.com/llvm/llvm-project/pull/120464)（也可按检查指定，例如 `-fno-sanitize-merge=signed-integer-overflow`），可以让每项检查拥有独立的陷阱。该选项取代了旧的 `-mllvm -ubsan-unique-traps`。

#### 为陷阱添加调试信息

除了在运行时解码陷阱指令，还可以让 Clang 在调试信息中记录检查（两个选项都需要 `-g`）。[`-fsanitize-annotate-debug-info`](https://github.com/llvm/llvm-project/pull/138577) 会为每项检查附加一个以检查名命名的人工内联函数（例如 `__ubsan_check_add_overflow`），使调试器能把故障归因到正确检查。`-fsanitize-debug-trap-reasons`（陷阱模式下默认为 `detailed`）更进一步，会嵌入出错表达式，并生成一个 `DISubprogram`，例如名为 `__clang_trap_msg$Undefined Behavior Sanitizer$signed integer addition overflow in 'a + b'`。

### 循环模式

在 2026 年 2 月，`-fsanitize-trap-loop`an 或 UBS 检查在陷阱模式下失败，此选项会导致程序死循环而不是执行陷阱指令。CFI 检查在 trapping 模式下失败时，此选项会使程序在一个无限循环中空转，而不是执行 trap 指令。

```sh
clang -fsanitize=undefined -fsanitize-trap=all -fsanitize-trap-loop a.c
```

Clang 不再发出 `llvm.ubsantrap`，而是调用 `llvm.looptrap` 内建函数（一种 `noreturn` 形式，由后续的优化阶段降级为 `llvm.cond.loop`），后者变为一个条件分支，该分支跳转到自身。这种方法有两个优点：

- **性能**：实验表明，在 AMD 和较旧的 Intel 微架构上，无限循环中的条件分支（未实际跳转时）比跳向陷阱指令的条件分支执行得更高效。
- **代码体积**：避免了发出陷阱指令以及可能的长分支指令。

在 i386 和 x86_64 上，该循环保证只包含一条跳向自身的 2 字节短条件分支指令。具体而言，第一个字节介于 0x70 与 0x7F 之间（Jcc rel8），第二个字节为 0xFE（-2，即跳回自身）。

这种行为可以直接使用，也可以配合中断处理程序或其他自省机制：当机制检测到程序卡在这种无限循环中时，就终止程序。相关 RFC：[https://discourse.llvm.org/t/rfc-optimizing-conditional-traps/89456](https://discourse.llvm.org/t/rfc-optimizing-conditional-traps/89456)

## 与其他 Sanitizer 一起使用

UBSan 可以与许多其他 Sanitizer 一起使用。

```sh
clang -fsanitize=address,undefined a.c
clang -fsanitize=fuzzer,undefined -fno-sanitize-recover a.c
clang -fsanitize=hwaddress,undefined a.c
clang -fsanitize=memory,undefined a.c
clang -fsanitize=thread,undefined a.c
clang -fsanitize=cfi,undefined -flto -fvisibility=hidden a.c
```

通常需要用多种 Sanitizer 测试同一个项目。将 UBSan 与另一种 Sanitizer 结合使用可以减少配置数量。实践中，人们更常使用 `-fsanitize=address,undefined` 和 `-fsanitize=hwaddress,undefined`，而非其他组合。当然，在另一套插桩之上再加入 UBSan 会带来更多开销和体积膨胀。

UBSan 与 libFuzzer 结合使用也很有意思。可以运行 `-fsanitize=fuzzer,address,undefined -fno-sanitize-recover`，让 libFuzzer 在检测到 AddressSanitizer 或 UndefinedBehaviorSanitizer 错误时中止。注意：libFuzzer 的最初开发者已经[停止](https://llvm.org/docs/LibFuzzer.html#status)积极开发 libFuzzer，转而开发 [Centipede](https://github.com/google/centipede)。

## 运行时选项

如前所述，大多数 UBSan 检查默认可恢复。指定 `halt_on_error=1` 可以得到类似于编译时选项 `-fno-sanitize-recover=undefined` 的行为。

```plaintext
% UBSAN_OPTIONS=halt_on_error=1 ./a <<< 1073741824
a.c:2:27: runtime error: signed integer overflow: 1073741824 * 2 cannot be represented in type 'int'
SUMMARY: UndefinedBehaviorSanitizer: undefined-behavior a.c:2:27 in
```

我们可以定义 `__ubsan_default_options` 来设置默认选项。1  
2  
3  
extern "C" const char *__ubsan_default_options() {  
 return "print_stacktrace=1";  
}

## 问题抑制

GNU 函数特性 GNU 可以禁用对某个函数的插桩。（`__attribute__((no_sanitize("undefined")))` 可以禁用某个函数的插装。（GCC 另外支持一个已废弃的特性 `__attribute__((no_sanitize_undefined)))`.)

如果 `$resource_dir/share/ubsan_ignorelist.txt`，该文件将被用作默认的系统忽略列表（可以通过 `-fsanitize-system-ignorelist=` 覆盖）。格式参见 [Sanitizer 特殊大小写列表](https://clang.llvm.org/docs/SanitizerSpecialCaseList.html)。该文件指示 Clang CodeGen 对指定的函数或文件禁用插桩。可以多次指定 `-fsanitize-ignorelist=` 来使用更多的忽略列表。

在大型代码库中，启用一项检查意味着需要修复所有现有问题，或通过 `no_sanitize` 函数特性来绕过它们。忽略列表提供了一种逐步启用检查的机制。这对于需要与新版代码交涉的工具链维护者来说非常有用。

例如，一旦除 `[a-m]*` 之外的所有源文件都没有 UBSan 错误（或已通过函数特性抑制），我们可以在 UBS 中使用以下模式。1  `ubsan_ignorelist.txt`. 1  
2  
3  
[alignment]  
src:[a-m]*  
src:./[a-m]*

`./` 用于头文件。

也可以在运行时进行抑制。UBSan 支持一个运行时选项 UBS：`UBSAN_OPTIONS=suppressions=a.supp`。`suppressions`: `UBSAN_OPTIONS=suppressions=a.supp`.

## 堆栈回溯

默认情况下，诊断信息不包含堆栈跟踪。指定 `print_stacktrace=1` 即可获取。如果程序使用 `-g1` 或 `-g` 编译，且 `llvm-symbolizer` 位于 `PATH` 目录中，则可以获得符号化的堆栈跟踪。

```plaintext
% UBSAN_OPTIONS=print_stacktrace=1 ./a <<< 1073741824
a.c:2:27: runtime error: signed integer overflow: 1073741824 * 2 cannot be represented in type 'int'
    #0 0x55f582e9d2f1 in foo /tmp/c/a.c:2:27
    #1 0x55f582e9d2f1 in main /tmp/c/a.c:6:20
    #2 0x7fe67838f189 in __libc_start_call_main csu/../sysdeps/nptl/libc_start_call_main.h:58:16
    #3 0x7fe67838f244 in __libc_start_main csu/../csu/libc-start.c:381:3
    #4 0x55f582e75d80 in _start (/tmp/c/a+0x17d80)

SUMMARY: UndefinedBehaviorSanitizer: undefined-behavior a.c:2:27 in
a -2147483648
b -2147483648
```

与其他清理程序类似，UBSan 运行时支持使用 DWARF 调用帧信息和帧指针进行堆栈展开。许多目标默认启用 `.eh_frame`（DWARF 调用帧信息的一个变体）(`-fasynchronous-unwind-tables`)。如果已禁用它，请确保 `-fno-omit-frame-pointer` 已生效（许多目标在使用 `-fomit-frame-pointer` 及更高优化级别时默认使用 `-O1`）。

## `-fsanitize=alignment`

非对齐内存访问在某些架构上成本高昂，或者会导致陷阱。

C11 6.3.2.3 规定：

> 整数可转换为任何指针类型。除先前指定的情况外，结果是实现定义的，可能未正确对齐，可能不指向引用类型的实体，并且可能是一个陷阱表示。implementation-defined，可能未正确对齐，可能不指向引用类型的实体，并且可能是陷阱表示。
>  
> 指向对象类型的指针可以转换为指向不同对象类型的指针。如果结果指针未针对引用类型正确对齐，则行为未定义。...

C++ 没有这么明确。不过，我认为 [basic.align] 第 1 段足以说明：

> ... 对象类型对该类型的每个对象施加了对齐要求；...

此外，C++ [expr.static.cast]p14 关于来自未对齐指针的转换指出：

> “指向 cv1 void 的指针”类型的纯右值可以转换为“指向 cv2 T 的指针”类型的纯右值，其中 T 是对象类型，且 cv2 的 cv 限定与 cv1 相同或更严格。如果原始指针值表示内存中某字节的地址 A，而 A 不满足 T 的对齐要求，则结果指针值未指定。……

这允许结果指针值为无效指针值，随后编译器可以赋予其任何我们认为合适的语义，例如不允许将其传递给 memcpy。

GCC 和 Clang 都通过检测内存访问操作（而不是构造指针的位置）来实现 `-fsanitize=alignment`。以下是列表。

```cpp
*p  // load
*p = 1;  // store
int &r = *p;  // bind a reference
s->member  // member access within misaligned address
new (s) S  // placement new at a misaligned address
char *__attribute__((assume_aligned(64))) x   // actually misaligned
__builtin_assume_aligned(p, 64)  // when p is misaligned
```

[RFC：在 Clang 中强制执行指针类型对齐](https://lists.llvm.org/pipermail/llvm-dev/2016-January/094012.html)介绍了 Clang 的决定。

如果 `p` 未对齐，它应该是指向 `char`, `unsigned char` 或 `std::byte` 的指针，并且可以使用以下代码。（较新的 Clang 的 `-fsanitize=alignment` 会在 `p` 未对齐时报告运行时失败。）1  
2  
3  
t x;  _t x;  
memcpy(&x, p, sizeof(uint32_t)); // 从非对齐指针加载  
memcpy(p, &x, sizeof(uint32_t)); // 存储到非对齐指针

如果使用专用的非对齐加载/存储函数不方便，我们可以利用 GCC 扩展：

```c
typedef int32_t __attribute__((aligned(1))) unaligned_int32_t;
// (C++ specific) Or: using unaligned_int32_t __attribute__((aligned(1))) = int32_t;

int32_t foo_a(int32_t *x) { return *x; } // instrumented by -fsanitize=alignment
unaligned_int32_t foo_u(unaligned_int32_t *x) { return *x; } // not instrumented
```

- [https://github.com/Blosc/c-blosc2/pull/550](https://github.com/Blosc/c-blosc2/pull/550)
- ffmpeg 有一个 `--disable-fast-unaligned` 配置选项

关于硬件对齐检查的说明：

在 x86 中，如果在 CR0 寄存器中设置了 AM 位，并且在 EFLAGS 寄存器中设置了 AC 位，则会启用对用户模式数据访问的对齐检查。user-mode 用户模式

```cpp
#include <stdio.h>
alignas(8) char a[100];
int main() {
  long b;
  asm("pushf\norq $(1<<18), (%%rsp)\npopf\n"
      "movq 0(%1), %0\n" // if 0 is changed to 1, SIGBUS due to alignment check
      "pushf\nandq $~(1<<18), (%%rsp)\npopf\n"
      : "=r"(b) : "r"(a));
  printf("%ld\n", b);
}
```

如果同时启用对齐检查和延迟 PLT 绑定，`printf` 调用会在 `../sysdeps/x86_64/multiarch/../multiarch/strcmp-sse2.S` 的 `movlpd (%rdi),%xmm1` 中触发对齐检查异常。指定 `-Wl,-z,now` 后，程序可以在 Intel CPU 上成功执行，但在 AMD CPU 上仍可能因为 `__printf_buffer` 中未对齐的 `movups %xmm1,0xc8(%rsp)` 而失败。

## `-fsanitize=enum`

C++ [dcl.enum] 指出：

> 对于底层类型固定的枚举，其值就是该底层类型的值。否则，其值由一个假想整数类型表示，该类型的最小宽度 M 足以表示所有枚举项。足以容纳该枚举类型所有值的最小位域宽度也是 M。枚举可以具有未由任何枚举项定义的值。如果枚举项列表为空，则其取值如同该枚举只有一个值为 0 的枚举项。

## `-fsanitize=function`

请参阅 [Control-flow integrity -fsanitize=function](https://maskray.me/blog/2022-12-18-control-flow-integrity#fsanitizefunction).

## `-fsanitize=local-bounds`

`array-bounds`（属于 `-fsanitize=undefined`）是一项 Clang CodeGen 检查，只在源表达式中能看到边界时触发，例如 `a[i]` 中的 `a` 具有数组类型。`local-bounds` 是另一项更激进的检查，以 LLVM pass（`BoundsChecking`）实现，并从对象大小推导边界，因此也能捕获通过退化指针等方式丢失数组类型的访问：

```c
int a[4];
int *p = a;
return p[i]; // array-bounds is blind here; local-bounds catches it
```

它被有意排除在 `-fsanitize=undefined` 之外，因为可能产生大量噪音。可以用 `-fsanitize=local-bounds` 启用它，或用 `-fsanitize=bounds` 同时启用 `array-bounds` 和 `local-bounds`。由于它以 pass 形式运行，而不是在 Clang CodeGen 中执行，因此也有下文针对 `-fsanitize=object-size` 提到的执行顺序问题。

## 杂项

在 Clang 中，与许多其他 Sanitizer 不同，UndefinedBehaviorSanitizer 作为 Clang CodeGen 的一部分执行，而不是作为优化流水线中的 LLVM pass。（`-fsanitize=object-size` 较为特殊，因为它需要 clangCodeGen 之后的 pass。）

在默认模式和最小运行时模式下，UBSan 插桩会加入回调，使被插桩函数不再是叶函数。

`-ftrapv` 检查可以用 `-fsanitize=signed-integer-overflow -fsanitize-trap=signed-integer-overflow` 代替。`-ftrapv` 基本已经过时。

## 选定的应用

`compiler-rt/lib/ubsan` 使用 C++ 编写，其中一些特性在某些环境（例如部分操作系统内核）中不可用。在内核中采用 UBSan 通常需要重新实现运行时，一般使用 C。

在 Linux 内核中，[UBSAN: run-time 于 2016 年引入了 ](https://git.kernel.org/linus/c6d308534aef6c99904bf5862066360ae067abc4)`CONFIG_UBSAN` 以及一个运行时实现。

NetBSD 在 2018 年[了 µUBS](https://blog.netbsd.org/tnf/entry/introduction_to_%C2%B5ubsan_a_clean) µUBSan。

Android 的文档：[https://source.android.com/docs/security/test/sanitizers#undefinedbehaviorsanitizer](https://source.android.com/docs/security/test/sanitizers#undefinedbehaviorsanitizer)

## 选择性 UBSan

https://discourse.llvm.org/t/rfc-add-llvm-allow-runtime-check-intrinsic/77641

过多的插桩可能会使代码体积膨胀。一种解决方案是利用 PGO 性能分析文件，选择性地移除频繁执行的基本块中的插桩。

当指定了 `-mllvm -ubsan-guard-checks` 时，插入的 UBSan 检查将由 [`llvm.allow.ubsan.check`](https://llvm.org/docs/LangRef.html#llvm-allow-ubsan-check-intrinsic) 测试保护。`llvm::LowerAllowCheckPass` 利用 profile 将 `llvm.allow.ubsan.check` 调用替换为 0 或 1，具体取决于基本块的热度（cl::opt `lower-allow-check-percentile-cutoff-hot`). `llvm::LowerAllowCheckPass` 需要位于内联器和 profile 匹配之后。

 降低为对 intrinsic 的调用 `__builtin_allow_runtime_check("check")``llvm.allow.runtime.check`，这与 `llvm.allow.ubsan.check`.

面向用户的 Clang 选项是 `-fsanitize-skip-hot-cutoff=`。它接受一个由逗号分隔的 `<sanitizer>=<fraction>` 对列表，例如 `-fsanitize-skip-hot-cutoff=array-bounds=0.99`。该比例表示累计权重的百分位：`0.0` 不跳过任何检查，`1.0` 跳过所有已插桩的块；中间值会移除最热的一组块中的检查，这些块合计占据相应比例的性能剖析计数（因此提高该值会逐步移除更冷块中的检查）。
