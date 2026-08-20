---
title: Block 编程主题
apple_id: TP40007502
resource_type: Guide
platform: watchOS|iOS|macOS
topic: Languages & Utilities
technology: null
published: '2011-03-08'
source_url: https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/Blocks/Articles/00_Introduction.html
archived_at: '2026-07-15T07:11:18.878804Z'
---
> 导航：[总目录](../../../README.md) · [文档](../../../_indexes/documentation.md)


[下一页](Getting%20Started%20with%20Blocks.md)

# 引言

block 对象（block object）是一项 C 语言层面的语法与运行时特性。它们类似于标准的 C 函数，但除了可执行代码之外，还可以包含指向自动（栈）内存或托管（堆）内存的变量绑定。因此，一个 block 可以维护一组状态（数据），并在执行时用这些状态来影响自身的行为。

你可以用 block 来组合函数表达式，把它传给 API、按需存储起来，或者供多个线程使用。block 特别适合用作回调（callback），因为 block 同时携带了回调时要执行的代码以及执行期间所需的数据。

随 OS X v10.6 Xcode 开发者工具一同发布的 GCC 和 [Clang](http://clang.llvm.org/) 都支持 block。你可以在 OS X v10.6 及更高版本、iOS 4.0 及更高版本中使用 block。block 运行时是开源的，可以在 [LLVM 的 compiler-rt 子项目仓库](http://llvm.org/svn/llvm-project/compiler-rt/trunk/)中找到。block 也已经以 [N1370：Apple 对 C 的扩展](http://www.open-std.org/jtc1/sc22/wg14/www/docs/n1370.pdf) 的形式提交给 C 标准工作组。由于 Objective-C 和 C++ 都派生自 C，block 在设计上可以同时用于这三种语言（以及 Objective-C++）。其语法正体现了这一设计目标。

如果你想了解 block 对象是什么、以及如何在 C、C++ 或 Objective-C 中使用它们，就应该阅读本文档。

本文档包含以下章节：

- [Block 入门](Getting%20Started%20with%20Blocks.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga3tkmbsfvbuqnznknltc) 通过实际示例对 block 作快速、实用的介绍。
- [概念概览](Conceptual%20Overview.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga3tkmbsfvbuqmznknltc) 从概念层面介绍 block。
- [声明与创建 Block](Declaring%20and%20Creating%20Blocks.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga3tkmbsfvbuqnbnknltc) 说明如何声明 block 变量以及如何实现 block。
- [Block 与变量](Blocks%20and%20Variables.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga3tkmbsfvbuqnrnknltc) 描述 block 与变量之间的相互作用，并定义 `__block` 存储类型修饰符。
- [使用 Block](Using%20Blocks.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga3tkmbsfvbuqnjnknltc) 展示各种使用模式。

[下一页](Getting%20Started%20with%20Blocks.md)

