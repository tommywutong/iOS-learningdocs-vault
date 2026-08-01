---
title: 在调试器中跳过无聊的函数
source: MaskRay (宋方睿)
source_key: maskray
source_url: 'https://maskray.me/blog/2024-12-30-skipping-boring-functions-in-debuggers'
original_language: en
published: 2024-12-30
status: active
license: 未声明 → 仅私有归档
archived_at: 2026-07-27
content_hash: 'sha256:d2f201edbb778f8a'
translated: true
---

> 原文：[在调试器中跳过无聊的函数](https://maskray.me/blog/2024-12-30-skipping-boring-functions-in-debuggers)　·　MaskRay (宋方睿)

[2024-12-30](https://maskray.me/blog/2024-12-30-skipping-boring-functions-in-debuggers)

# 在调试器中跳过无聊的函数

在调试器中，单步进入参数中包含函数调用的函数时，可能会进入嵌套的函数调用；即使这些调用如 C++ STL 中的函数一样简单且乏味，也会如此。

## GDB

请看下面的示例：

```cpp
#include <cstdio>
#include <memory>
#include <vector>
using namespace std;

void foo(int i, int j) {
  printf("%d %d\n", i, j);
}

int main() {
  auto i = make_unique<int>(3);
  vector v{1,2};
  foo(*i, v.back()); // step into
}
```

当 GDB 停在对 `foo` 的调用处时，`step`（`s`）命令会进入 `std::vector::back` 和 `std::unique_ptr::operator*`。虽然可以执行 `finish`（`fin`），然后再次执行 `s`，但这既耗时又容易分散注意力，处理复杂的参数表达式时尤其如此。

```plaintext
% g++ -g a.cc -o a
% gdb ./a
...
(gdb) s
std::vector<int, std::allocator<int> >::back (this=0x7fffffffddd0) at /usr/include/c++/14.2.1/bits/stl_vector.h:1235
1235          back() _GLIBCXX_NOEXCEPT
(gdb) fin
Run till exit from #0  std::vector<int, std::allocator<int> >::back (this=0x7fffffffddd0) at /usr/include/c++/14.2.1/bits/stl_vector.h:1235
0x00005555555566f8 in main () at a.cc:13
13        foo(*i, v.back());
Value returned is $1 = (__gnu_cxx::__alloc_traits<std::allocator<int>, int>::value_type &) @0x55555556c2d4: 2
(gdb) s
std::unique_ptr<int, std::default_delete<int> >::operator* (this=0x7fffffffddc0) at /usr/include/c++/14.2.1/bits/unique_ptr.h:447
447             __glibcxx_assert(get() != pointer());
(gdb) fin
Run till exit from #0  std::unique_ptr<int, std::default_delete<int> >::operator* (this=0x7fffffffddc0) at /usr/include/c++/14.2.1/bits/unique_ptr.h:447
0x0000555555556706 in main () at a.cc:13
13        foo(*i, v.back());
Value returned is $2 = (int &) @0x55555556c2b0: 3
(gdb) s
foo (i=3, j=2) at a.cc:7
7         printf("%d %d\n", i, j);
```

这个问题在 2003 年就被记录为功能请求：[https://sourceware.org/bugzilla/show_bug.cgi?id=8287](https://sourceware.org/bugzilla/show_bug.cgi?id=8287)。幸运的是，GDB 提供了 [`skip` 命令](https://sourceware.org/gdb/current/onlinedocs/gdb.html/Skipping-Over-Functions-and-Files.html)，可跳过名称匹配正则表达式的函数，或文件名匹配 glob 模式的文件（这是 GDB 7.12 引入的功能）。你可以跳过所有以 `std::` 开头的解修饰函数名。

```plaintext
skip -rfu ^std::
```

或者，也可执行 `skip -gfi /usr/include/c++/*/bits/*` 来跳过这些 libstdc++ 文件。

注意：

`skip` 命令的文件匹配使用带有 [`FNM_FILE_NAME`](https://man7.org/linux/man-pages/man3/fnmatch.3.html) 标志的 `fnmatch` 函数。这意味着通配符（`*`）不会匹配斜杠。因此，skip `-gfi /usr/*` 无法排除 `/usr/include/c++/14.2.1/bits/stl_vector.h`。

我曾建议[移除 `FNM_FILE_NAME` 标志](https://sourceware.org/pipermail/gdb-patches/2024-December/214422.html)。有了 GDB 17，我就能通过以下方式跳过一个项目目录：  
 1  
skip -gfi */include/llvm/ADT/*

而不是：1  
skip -gfi /home/ray/llvm/llvm/include/llvm/ADT/*

### 被跳过函数所调用的用户函数

调试时，若一个函数（姑且称为 "A"）被跳过，则所有由 "A" 调用的用户定义函数也会被跳过。

例如，请看下面的代码片段：

```cpp
std::vector<int> a{1, 2};
if (std::all_of(a.begin(), a.end(), predicate)) {
}
```

如果 `std::all_of` 因 `skip` 命令被跳过，那么在 if 语句处执行 `s` 时，`std::all_of` 内部调用的 `predicate` 也会被跳过。

## LLDB

默认情况下，使用 `s`（`step`、`thread step-in`）命令时，LLDB 会避免进入名称以 `std::` 开头的函数。此行为由一项设置控制：

```plaintext
(lldb) settings show target.process.thread.step-avoid-regexp
target.process.thread.step-avoid-regexp (regex) = ^std::
(lldb) set sh target.process.thread.step-avoid-libraries
target.process.thread.step-avoid-libraries (file-list) =
```

`target.process.thread.step-avoid-libraries` 可用于跳过定义在某个库中的函数。

虽然 `settings set` 命令很长，但可以将其缩写为 `set set`。

## Visual Studio

Visual Studio 提供调试功能 [_Just My Code_](https://learn.microsoft.com/en-us/visualstudio/debugger/just-my-code?view=vs-2022)，可自动单步跳过对系统、框架及其他非用户代码的调用。

它还支持 `Step Into Specific` 命令，这一点颇有意思。

其实现方式是在每个用户函数的开头插入对 `__CheckForDebuggerJustMyCode` 的调用。该函数（`void __CheckForDebuggerJustMyCode(const char *flag)`）接收定义在 `.msvcjmc` 节中的全局变量，并据此判断调试器是否应停止。

这项 LLDB 功能请求对此有很好的说明：[https://github.com/llvm/llvm-project/issues/61152](https://github.com/llvm/llvm-project/issues/61152)。

对于 `all_of` 示例，这项功能或许能让调试器停在 `test` 处。

```cpp
std::vector<int> a{1, 2};
if (std::all_of(a.begin(), a.end(), test)) {
}
```

## Fuchsia zxdb

Fuchsia 的调试器“zxdb”提供 ["ss"](https://fuchsia.dev/fuchsia-src/development/debugger/execution) 命令，与 Visual Studio 的 "Step Into Specific" 类似。

```plaintext
[zxdb] ss
  1 std::string::string
  2 MyClass::MyClass
  3 HelperFunctionCall
  4 MyClass::~MyClass
  5 std::string::~string
  quit
>
```
