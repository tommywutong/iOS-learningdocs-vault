---
title: 我终于搞明白了 weakSelf 和 strongSelf
source_url: 'https://dhoerl.wordpress.com/2013/04/23/i-finally-figured-out-weakself-and-strongself/'
source_domain: dhoerl.wordpress.com
source_group: single-site
original_language: en
published: 2013-04-23
archived_at: 2026-07-27
content_hash: 'sha256:99735e59a5d809c6'
plan_ref: 第二周：weak、属性关键字与 Block / Day 5｜循环引用是 Day 4 所有权图的推论（对应 W2-14、W2-16）
plan_week: 第二周：weak、属性关键字与 Block
plan_day: Day 5｜循环引用是 Day 4 所有权图的推论（对应 W2-14、W2-16）
container: '//*[contains(@class,''entry-content'')]'
container_source: guess
---

> 原文：[I finally figured out weakSelf and strongSelf](https://dhoerl.wordpress.com/2013/04/23/i-finally-figured-out-weakself-and-strongself/)

使用 block 和异步派发时的一个问题是，你可能会陷入保留循环（retain cycle）——block 会保留 `self`，有时是以很隐蔽的方式。例如，如果你直接引用了实例变量（ivar），代码中写的是 `theIvar`，但编译器实际生成的是 `self->theIvar`。这样一来，作为强引用变量的 `self` 就被保留了，队列保留了 block，而对象又保留了队列。

Apple 建议先把 `self` 赋给一个弱引用自动变量，然后在 block 中引用它（见参考资料 1）。由于 block 捕获的是变量及其修饰符（即 `__weak` 限定符），因此对 `self` 不存在强引用，对象可以被释放，而此时被捕获的弱引用变量会变为 nil。

> __weak __typeof__(self) weakSelf = self;
> dispatch_group_async(_operationsGroup, _operationsQueue, ^
> {
> [weakSelf doSomething];
> } );

想到这个问题时，我担心 `weakSelf` 可能在 `doSomething` 执行到一半时变成 nil，但在 Xcode 邮件列表上发了几篇帖子后，有人给了我一份 clang 文档的参考链接，其中明确指出，表达式中的任何对象都会在整个表达式执行期间被保留，直到表达式结束后才会释放（见参考资料 2）。呼，松了一口气！

但是下面这种情况呢？

> __weak __typeof__(self) weakSelf = self;
> dispatch_group_async(_operationsGroup, _operationsQueue, ^
> {
> [weakSelf doSomething];
> [weakSelf doSomethingElse];
> } );

嗯，在这种情况下，`weakSelf` 在第一个方法执行时可能非 nil，但到第二个方法时就不一定了。唔——上面的例子还算简单，大多数实际代码中 `weakSelf` 的用法会复杂得多。

Apple 把第二种情况称为「非平凡」（non-trivial）（见参考资料 1），并采取了一组乍看很奇怪的步骤：先创建 `weakSelf` 对象，再将其赋给 `strongSelf`：

> __weak __typeof__(self) weakSelf = self;
> dispatch_group_async(_operationsGroup, _operationsQueue, ^
> {
> __typeof__(self) strongSelf = weakSelf;
> [strongSelf doSomething];
> [strongSelf doSomethingElse];
> } );

或者用 Swift：

> dispatch_async(dispatch_get_main_queue()) { [weak self] in
> if let strongSelf = self {
> //…
> }
> }
> // 参见《The Swift Programming Language》中的“Resolving Strong Reference Cycles for Closures”

我翻来覆去地看，想自己推理出原因（看来是我太迟钝了）。最后，灯泡终于亮了，我想通了！当 block 运行时，它只捕获了 `weakSelf`。在 block 启动的那一刻，`weakSelf` 要么是 `self`，要么是 nil。你的代码（就像 Apple 的例子那样）可以测试 `strongSelf` 是否被设置，如果设置了，你就可以使用 `strongSelf->theIvar` 或更常见的 `strongSelf.someProperty`（后者在 nil 消息传递中也能正常工作，前者在 `strongSelf` 为 nil 时会崩溃）。

如果 `weakSelf` 等于 `self`，那么 `strongSelf` 会保留它，并且这个强引用会一直保持到 block 返回并释放它为止。这是一种全有或全无的机制。

终于搞明白了这一点，我心情大好，这也让我的 block 编码变得轻松多了。

注意：

如果你对 `__typeof__(self)` 的用法感到困惑，它是一个非标准的 clang 宏，用于获取括号内对象的类，最初源自 GCC。使用它的好处是，你可以把这行代码做成摘要卡片（Code Snippet）（我把它叫做「WeakSelf」），这样就不必不断调整类名了。

1) 《Programming With ARC Release Notes》中搜索“For non-trivial cycles, however, you should use”

2) [http://clang.llvm.org/docs/AutomaticReferenceCounting.html](http://clang.llvm.org/docs/AutomaticReferenceCounting.html)：

对于 `__weak` 对象，当前的所指对象会被保留，然后在当前完整表达式结束时释放。这个过程必须与赋值操作以及对所指对象的最终释放操作原子性地执行。
