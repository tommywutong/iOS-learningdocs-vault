---
title: Objective-C 中的循环容器 - Low Level Bits 🇺🇦
source: Low Level Bits (Alex Denisov)
source_key: lowlevelbits
source_url: 'https://lowlevelbits.org/circular-containers-in-objective-c/'
original_language: en
published: ''
status: active
license: © 2014-2025 → 仅私有归档
archived_at: 2026-07-27
content_hash: 'sha256:314df30b292eeaf4'
translated: true
---

> 原文：[Circular Containers in Objective-C - Low Level Bits 🇺🇦](https://lowlevelbits.org/circular-containers-in-objective-c/)　·　Low Level Bits (Alex Denisov)

# Objective-C 中的循环容器

_发布于 2015 年 4 月 13 日_

前阵子我不小心写出了这段代码：

```objective
NSMutableArray *environments = [NSMutableArray new];
for (NSString *key in [dictionary allKeys]) {
    XCCEnvironment *environment = [[XCCEnvironment alloc] initWithName:key
                                                            parameters:dictionary[key]];
    [environments addObject:environments];
}
return environments;
```

你发现这里的问题了吗？反正我当时没发现。

### 问题

运行程序后，我遇到了崩溃：

```
-[__NSArrayM someSelector]: unrecognized selector sent to instance 0x100211d80
```

`environments` 的调用方期望拿到 `XCCEnvironment`，却得到了 `NSMutableArray`。

一开始我不清楚为什么会这样，但仔细看了看代码，发现我把数组放进了它自身：

```objective
// ...
NSMutableArray *environments = [NSMutableArray new];
// ...
[environments addObject:environments];
// ...
```

文档没有说明集合（collection）在这种情况下的行为，我找到的唯一有价值的（依我之见）读物是 Mike Ash 的博客文章 [Let’s break Cocoa](https://www.mikeash.com/pyblog/friday-qa-2014-01-10-lets-break-cocoa.html)。

文章指出，可变数组、字典和集合（set）如果被你做成所谓的循环容器（circular container），会变得非常疯狂。另一个问题是，在启用了 ARC 的情况下会导致内存泄漏：集合会保留自身。

### 解决方案

我相信正常情况下开发者不会把集合放进自身。不过，这跟「程序员不会解引用空指针」是一类信念——它仍然会发生，而且可能是一种有些意外的行为。

我很确信 clang 能够阻止我和其他人犯这个错，但我没找到任何执行此检查的警告/标志/设置。

最终我决定自己实现它。实现花了两三个晚上，但现在它已经 [进入主线](https://github.com/llvm-mirror/clang/commit/5dc6c6cd87f3a86fe9d5ba9d1b3892252c7de248) 了。

实际的补丁会检查以下可变集合：

- NSMutableArray
- NSMutableDictionary
- NSMutableSet
- NSMutableOrderedSet
- NSCountedSet

并在你试图把集合放进自身时显示警告。

该警告可以分别通过 `-wobjc-circular-container` / `-wno-objc-circular-container` 启用/禁用，不过它是「默认」启用的。

### 总结

最近的 clang 版本已经包含此功能，但 Xcode 里还不可用，我猜它会随着下一个大版本出现——大约一年后。

但不管怎样，拥有开源工具真的非常棒：你可以调整它、扩展它，让自己和他人的生活变得更好一点。

Happy hacking!

**更新**

该功能进入了 WWDC 2016 的 [What’s new in LLVM](https://developer.apple.com/videos/play/wwdc2016/405/) 议题。

![](https://lowlevelbits.org/img/circular-containers/wwdc.png)
