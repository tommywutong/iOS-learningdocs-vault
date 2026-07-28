---
title: 调试 dyld - Low Level Bits 🇺🇦
source: Low Level Bits (Alex Denisov)
source_key: lowlevelbits
source_url: 'https://lowlevelbits.org/debugging-dyld/'
original_language: en
published: ''
status: active
license: © 2014-2025 → 仅私有归档
archived_at: 2026-07-27
content_hash: 'sha256:abbf0a55b653c36f'
translated: true
---

> 原文：[Debugging Dyld - Low Level Bits 🇺🇦](https://lowlevelbits.org/debugging-dyld/)　·　Low Level Bits (Alex Denisov)

# 调试 dyld

_发表于 2018 年 11 月 13 日_

最近，我在调试一个有趣的问题：一个程序在尝试调用某个动态库中的特定函数时总会崩溃。起初我不清楚该如何调试这个问题。最终，我解决了这个难题——关键在于动态链接器 dyld。

在本文中，我想简要介绍一下，如果你遇到类似问题，应该从何处入手。这绝非一份详尽的指南，而是一个起点——如果之前就知道这些信息，或许能省下我几个小时。

## 从内部检查 dyld

dyld 的源代码通常是可获取的，但已过时。在撰写本文时，你可以从[这里](https://opensource.apple.com)获取 macOS High Sierra 10.13.6 的源代码。如果你运行的是最新的 macOS 10.14 Mojave，那么你最后的手段是 OS 自带的二进制文件。不过，旧版本的源代码仍然有帮助。为了了解全貌，我建议你执行以下步骤：

1. 从 [https://opensource.apple.com/](https://opensource.apple.com/) 获取最新版本的源代码。
2. 使用反汇编器（[Hopper](https://www.hopperapp.com) 是我的首选）检查 dyld 的二进制文件：`/usr/lib/dyld`、`/usr/lib/system/libdyld.dylib` 和 `/usr/lib/closure/libclosured.dylib`。
3. 禁用 [SIP](https://en.wikipedia.org/wiki/System_Integrity_Protection)（可选），并在 `lldb` 下运行你的二进制文件。你可以在所有与 dyld 相关的函数上设置断点：使用 `br set -r dyld`，或者针对 dyld3 使用 `br set -r dyld3`。

在调试过程中，请准备好频繁地在源代码和第二步中提到的三个库之间来回跳转。

## 从外部检查 dyld

还有几种其他方法可以观察 dyld 的行为，而无需查看代码、源代码或二进制文件。如果你希望对系统 App 进行操作，还需要禁用 [SIP](https://en.wikipedia.org/wiki/System_Integrity_Protection)。所有选项都通过环境变量控制。以下是我发现最有用的几个：

- `DYLD_PRINT_APIS`：有文档记录。它会打印出 dyld 内部几乎一切活动的详细追踪。示例输出如下：

```
_dyld_register_func_for_add_image(0x7fff7696ab92)
_dyld_get_image_slide(0x1000f1000)
_dyld_register_func_for_add_image(0x7fff7689cd98)
_dyld_get_image_slide(0x1000f1000)
_dyld_register_func_for_add_image(0x7fff76be67cb)
dyld_image_path_containing_address(0x7fff75221000)
...
```

看起来有些晦涩，但它对理解程序执行流程有很大帮助。

- `DYLD_PRINT_LIBRARIES`：有文档记录。它会打印出 App 启动期间加载的所有动态库。示例输出如下：

```
dyld: loaded: /usr/lib/libiconv.2.dylib
dyld: loaded: /System/Library/Frameworks/Security.framework/Versions/A/Security
dyld: loaded: /System/Library/Frameworks/CoreFoundation.framework/Versions/A/CoreFoundation
dyld: loaded: /usr/lib/libz.1.dylib
dyld: loaded: /usr/lib/libSystem.B.dylib
dyld: loaded: /usr/lib/libresolv.9.dylib
dyld: loaded: /usr/lib/system/libcache.dylib
dyld: loaded: /usr/lib/system/libcommonCrypto.dylib
dyld: loaded: /usr/lib/system/libcompiler_rt.dylib
```

- `DYLD_PRINT_WARNINGS`：无文档记录。可能会打印一些有用的信息。目前，它确定会打印一些关于 [dyld3 closures](https://allegro.tech/2018/05/Static-linking-vs-dyld3.html) 的信息。示例输出如下：

```
dyld: found closure 0x7ffff48ae9ac (size=844) in dyld shared cache
dyld: closure 0x7ffff48ae9ac not used because DYLD_FRAMEWORK_PATH changed
```

- `DYLD_*_PATH`：有文档记录。改变 dyld 查找动态库的目录顺序。使用这些变量的一个好副作用是：它们的出现会禁用 dyld3 的 closure 缓存。因此，如果你怀疑问题出在 dyld3 closures 上，可以导出任意一个 `DYLD_*_PATH` 变量来禁用它。示例如下：

```
export DYLD_FRAMEWORK_PATH=
export DYLD_LIBRARY_PATH=
```

更多信息，请查阅 dyld 的手册页（`man dyld`），或者翻阅代码、源代码或二进制文件。

## 总结

调试像 dyld 这样的组件并非易事，但确实是可行的。如果你知道其他任何提示或技巧，欢迎分享。

祝你调试愉快！
