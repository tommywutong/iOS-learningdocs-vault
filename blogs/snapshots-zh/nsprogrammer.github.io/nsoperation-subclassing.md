---
title: NSOperation 子类化
source_url: 'https://nsprogrammer.github.io/jekyll/update/2021/07/02/nsoperation.html'
source_domain: nsprogrammer.github.io
source_group: single-site
original_language: en
published: 2021-07-02
archived_at: 2026-07-27
content_hash: 'sha256:2a3eed9d3a34e7ca'
plan_ref: 第四周：线程、GCD、Operation 与锁 / Day 4｜Operation 是“可管理的任务图”（对应 W3-05）
plan_week: 第四周：线程、GCD、Operation 与锁
plan_day: Day 4｜Operation 是“可管理的任务图”（对应 W3-05）
container: '//*[contains(@class,''post-content'')]'
container_source: guess
translated: true
---

> 原文：[NSOperation Subclassing](https://nsprogrammer.github.io/jekyll/update/2021/07/02/nsoperation.html)

## 为什么要写这篇博文？

关于 [`NSOperation`](https://developer.apple.com/documentation/foundation/nsoperation) 的资料已经很多了，所以这篇文章可能只是网络空间中的又一点噪音。

然而，这也是我从同行那里得到的最多的问题之一，因为其中存在许多细微差别，导致很难靠记忆牢固掌握，或者通过 Google 搜索确切地找到答案。

因此，这篇文章不会介绍 `NSOperation` 的优点，也不会回顾该 API 多年来的历史变迁，甚至不会提供使用该 API 的示例……它仅仅记录如何对 `NSOperation` 进行子类化（subclass），以使其能够用于你的各种使用场景。

## NSOperation 简短前言

自从 `NSOperation` 在 _Mac OS X 10.5_ 中引入以来，我见证了它坎坷的发展历程。它确实有一段充满 bug 的历史，损害了开发者社区对这个 API 的看法。但从 _iOS 10_ / _macOS 10.12_ 开始，它已经稳定下来，并且确实是 Apple 平台上组织大型工作单元的_最佳_方式。回顾其问题历史固然有趣，但那已经是过去的事了，我们现在可以专注于它已然稳固的现状。这意味着（在撰写本文时）已经有 5 个版本的坚实支持，所以它不再像过去那样存在风险。

将所有“重量级”工作放入 `NSOperation` 中，可以让你利用许多特性，这些特性如果自己构建会非常复杂，而且与 Apple 自身优化的 API 相比，效率也较低。在这篇文章中，我不会介绍其优点或特性，只专注于“**如何对 NSOperation 进行子类化**”这个主题。

### 关于 _async await_ 的说明

在 WWDC 2021 中为 iOS 15+ 引入的全新 `async await` 是 Swift 的一个优秀补充，将为进行异步和并发（concurrency）编程的开发者提供巨大价值。然而，`async await` 和 `NSOperation` 之间并不存在竞争关系；说 `async await` 引入后 `NSOperation` 就没用了，就好比说因为存在 `GCD` 所以 `NSOperation` 就没用了。它们服务于不同的目的，并且实际上是互补的。~~你可以毫无问题地使用 `async await` 来实现你的 `NSOperation`（Swift 中的 `Operation`）！~~ _更新：_ 我实际上花了大量时间在这上面，但找不到使用 `async await` 实现 `NSOperation` 的方法…… 从异步上下文使用 `NSOperation` 很简单，但我无法让 `NSOperation` 内部的 KVO 配合 Swift 的新并发特性工作 🤷‍♂️。

## NSOperation 介绍

`NSOperation` 实际上提供了一个 API 来封装一个工作单元，该单元可以提交到优先级队列，即 [`NSOperationQueue`](https://developer.apple.com/documentation/foundation/nsoperationqueue)。

`NSOperation` 类本身用处不大。要真正发挥作用，必须对其进行子类化（subclass），以便执行“工作”，并采用 `NSOperation` 的模式来利用其提供的所有优势。

Apple 提供了两个具体的子类作为入门方式，这实际上实现了使用 `NSOperation` 执行工作的 3 种特定方式。

1. 基于 `block` 的工作可以使用 `NSBlockOperation`
2. 基于 Objective-C 对象的工作可以使用 `NSInvocationOperation`
    - 这使得通过 `target` 和 `selector`（选择器），或通过 `NSInvocation` 来执行工作成为可能

尽管拥有这些便利的具体类很有价值，但对于复杂的操作，可能需要更多的控制（control）。这就是自定义子类的用武之地。

## NSOperation 的结构剖析

[`NSOperation`](https://developer.apple.com/documentation/foundation/nsoperation) 有许多控制其工作方式的属性（property）。

有一些 KVO 属性用于控制操作的执行并发出其进度信号：

- `isCancelled`
- `isExecuting`
- `isFinished`
- `isReady`

有一些属性控制其执行：

- `qualityOfService`
- `queuePriority`
- `dependencies`
- `completionBlock`

还有一个用于区分其运行行为（operating behavior）的属性：

- `isAsynchronous`

## 异步操作 vs 同步操作

在深入研究 `NSOperation` 的其他部分之前，有必要提前指出 `NSOperation` 有两种模式：`isAsynchronous` 为 `NO` 以及 `isAsynchronous` 为 `YES`。

这个属性澄清了操作的运行方式（异步 vs 同步），但实际上完全区分了我们_如何_对 `NSOperation` 进行子类化。这可能是对 `NSOperation` 进行子类化时最重要的一个说明——一个基类根据操作是异步还是同步，有两种完全不同的子类化模式。

实际上，同步 `NSOperation` 子类可以将所有与 KVO 相关的记账工作交由超类实现处理。它们只需要实现“工作”，使其同步运行即可。所有 Apple 提供的具体 `NSOperation` 类（`NSBlockOperation` 和 `NSInvocationOperation`）都是同步的。

而对于异步子类化，则需要非常小心和细致，才能正确地让事物在系统内运作。

## NSOperation 的 KVO 属性

`NSOperation`（以及与之相关的其他依赖 `NSOperation` 实例）的执行受 KVO 状态属性（state property）的制约。

首先是 `isReady`。当 `isReady` 为 `NO` 时，操作不会被 `NSOperationQueue` 出队。一旦 `isReady` 变为 `YES`，操作就可以开始（当然，前提是 `NSOperationQueue` 有容量来运行它）。

然后，当操作启动时，它将 `isExecuting` 从 `NO` 变为 `YES`。

接着工作发生，无论它是同步还是异步。

工作完成后，`isExecuting` 变回 `NO`。

最后，操作完成，将 `isFinished` 从 `NO` 变为 `YES`。

以上所有过程对于同步 `NSOperation` 子类来说是完全自动管理的。而异步子类则必须完全自行管理这些状态（state）及其过渡（transition）。

此外，还有 `isCancelled` 属性。默认情况下，在 `NSOperation` 上调用 `cancel` 只会将 `isCancelled` 翻转为 `YES`。当工作正在执行时，执行的“工作”部分负责在适当的地方检查 `isCancelled`，并提前结束（对于同步操作是提前返回，对于异步操作则是将 `isExecuting` 设置为 `NO`，将 `isFinished` 设置为 `YES`）。

## 特别说明 _isReady_

`isReady` 属性值得特别关注。该属性阻止操作在队列中运行，直到它被设置为 `YES`。这个属性实际上与 `NSOperation` 的所有 `dependencies` 的 `isFinished == YES` 耦合在一起。不幸的是，实现细节是隐藏的，因此如果你在子类中覆盖 `isReady`，你将无法正确反映依赖图（dependency graph），所以覆盖 `isReady` 实际上意味着你用自定义行为替换了原有行为，而 `dependencies` 将不再生效。

除了 `isReady` 与 `dependencies` 完成状态耦合之外，当 `isCancelled` 在操作实际启动之前被设置为 `YES` 时，它也会翻转为 `YES`。这使得操作可以快速启动并立即完成，从而将其从队列中清除并解除对依赖它的操作的阻塞。

最终，`isReady` 存在足够的细微差别和麻烦，因此最好_永远不要_覆盖它。如果你需要应用自定义行为来影响 `isReady`，最简单的选择是使用其他 `NSOperation` 对象作为依赖。一旦你将 `isReady` 仅仅视为 `areAllDependenciesFinished`（所有依赖是否都已完成），推理起来就容易得多，并且你可以轻松地通过将其他操作作为 `dependencies` 来为运行你的操作构建阻塞行为。

## 实现同步 NSOperation

同步 `NSOperation` 子类化是最直接的选择，所以让我们看看它可能的样子。

根据文档，你真正需要做的就是实现 `main` 方法，并在其中执行同步工作。

### Objective-C 代码

```objc
@interface MySyncOperation : NSOperation
@end

@implementation MySyncOperation

- (void)main
{
    ... run work ...

    if (self.isCancelled) {
       return;
    }

    ... run more work ...

    if (self.isCancelled) {
       return;
    }

    ... run final work ...
}

@end
```

### Swift 代码

```swift
class MySyncOperation: Operation {

    override func main() {
        ... run work ...

        guard !self.isCancelled else { return }

        ... run more work ...

        guard !self.isCancelled else { return }

        ... run final work ...
    }

}
```

## 实现异步 NSOperation

异步 `NSOperation` 子类化有更多的细微差别。

你将覆盖 `start` 而不是 `main`。你还需要覆盖状态属性（state property）。

保持线程（thread）安全非常重要，因为你不知道状态访问器（state accessor）会在哪个线程（thread）上被调用。在我的示例实现中，我将使用 `@synchronized(self)`，它在底层会产生一个递归的 pthread 互斥锁（mutex）。如果你想使用不同的同步机制，也可以，但请记住几点。

首先，为了最大程度的稳健性，你需要在临界区（critical section）内封装对多个不同状态值（state value）的读取和写入。这意味着使每个状态值（state value）原子化对于最大线程安全是不够的。你可能可以只保持状态值（state value）的原子性，但除非你能证明存在性能需求，否则使用临界区封装状态读写将是更简单的选择。

其次，你还需要确保临界区支持递归。由于我们在更新状态（state）时管理 KVO，这会导致在临界区内访问 KVO 属性（每次 `willChangeValueForKey:` 和 `didChangeValueForKey:` 调用都会访问给定 key 的属性）。如果你选择原子状态值而不是临界区模式，你就不必担心递归问题（但竞态条件（race condition）的风险会更高）。

### Objective-C 代码

```objc
@interface MyAsyncOperation : NSOperation
@end

@implementation MyAsyncOperation
{
    struct {
        BOOL isCancelled;
        BOOL isExecuting;
        BOOL isFinished;
    } _state;
    dispatch_queue_t _queue;
}

- (instancetype)init
{
    if (self = [super init]) {
        _queue = ... the queue to execute on ...;
    }
    return self;
}

#pragma mark 状态访问器

- (BOOL)isFinished
{
    @synchronized(self) {
        return _state.isFinished;
    }
}

- (BOOL)isExecuting
{
    @synchronized(self) {
        return _state.isExecuting;
    }
}

- (BOOL)isCancelled
{
    @synchronized(self) {
        return _state.isCancelled;
    }
}

- (BOOL)isAsynchronous
{
    return YES;
}

#pragma mark 方法覆盖

- (void)start
{
    @synchronized(self) {
        if (_state.isCancelled) {
            [self _finish];
            return;
        }

        [self willChangeValueForKey:@"isExecuting"];
        _state.isExecuting = YES;
        [self didChangeValueForKey:@"isExecuting"];
    }

    dispatch_async(_queue, ^{
        [self _run];
    );
}

- (void)cancel
{
    @synchronized(self) {
        if (!_state.isCancelled) {
            [self willChangeValueForKey:@"isCancelled"];
            _state.isCancelled = YES;
            [self didChangeValueForKey:@"isCancelled"];

         [self _finish];
       }
    }
}

#pragma mark 私有方法

- (void)_run __attribute__((objc_direct))
{
    if (self.isCancelled) {
        return;
    }

    ... do work ...

    if (self.isCancelled) {
        return;
    }

    ... do more work ...

    if (self.isCancelled) {
        return;
    }

    @synchronized(self) {
        [self _finish];
    }
}

/* 此方法必须在安全的同步临界区内调用 */
- (void)_finish __attribute__((objc_direct))
{
    const BOOL shouldFinish = !_state.isFinished;
    const BOOL shouldStopExecuting = _state.isExecuting;

    if (shouldFinish) {
        [self willChangeValueForKey:@"isFinished"];
    }
    if (shouldStopExecuting) {
        [self willChangeValueForKey:@"isExecuting"];
    }

    _state.isFinished = YES;
    _state.isExecuting = NO;

    if (shouldStopExecuting) {
        [self didChangeValueForKey:@"isExecuting"];
    }
    if (shouldFinish) {
        [self didChangeValueForKey:@"isFinished"];
    }
}

@end
```

### Swift 代码

使用 `NSRecursiveLock` 实现。功能上与 Objective-C 版本相同。~~可以使用 Swift 5.5 的 `async/await` 来实现，但在异步上下文和非异步上下文之间来回切换会有些混乱——如果有简洁的实现，欢迎与我分享 :)~~ _更新_ 我找不到在 Swift 中使用 `async await` 实现 `NSOperation` 的方法——如果你能找到，请分享！

```swift
class MyAsyncOperation: Operation {

    struct State {
        var isCancelled: Bool
        var isExecuting: Bool
        var isFinished: Bool
    }

    private let state = State()
    private let lock = NSRecursiveLock()
    private let queue: DispatchQueue

    init() {
        queue = ... the queue to execute on ...
    }

    // MARK: 状态访问器

    public override var isFinished: Bool {
        self.lock.lock()
        defer { self.lock.unlock() }

        return self.state.isFinished
    }

    public override var isExecuting: Bool {
        self.lock.lock()
        defer { self.lock.unlock() }

        return self.state.isExecuting
    }

    public override var isCancelled: Bool {
        self.lock.lock()
        defer { self.lock.unlock() }

        return self.state.isCancelled
    }

    public override var isAsynchronous: Bool {
        return true
    }

    // MARK: 方法覆盖

    public override func start() {
        self.lock.lock()
        defer { self.lock.unlock() }

        guard !self.state.isCancelled else {
            self.finish()
            return
        }

        self.willChangeValue(forKey: "isExecuting")
        self.state.isExecuting = true
        self.didChangeValue(forKey: "isExecuting")

        self.queue.async {
            self.run()
        }
    }

    public override func cancel() {
        self.lock.lock()
        defer { self.lock.unlock() }

        if !self.state.isCancelled {
            self.willChangeValue(forKey: "isCancelled")
            self.state.isCancelled = true
            self.didChangeValue(forKey: "isCancelled")
            self.finish()
        }
    }

    // MARK: 私有方法

    private func run() {
        guard !self.isCancelled else {
            return
        }

        ... do work ...

        guard !self.isCancelled else {
            return
        }

        ... do more work ...

        guard !self.isCancelled else {
            return
        }

        self.lock.lock()
        defer { self.lock.unlock() }
        self.finish()
    }

    /* 此函数必须在安全的同步临界区内调用 */
    private func finish() {
        let shouldFinish = !self.state.isFinished
        let shouldStopExecuting = self.state.isExecuting

        if shouldFinish {
            self.willChangeValue(forKey: "isFinished")
        }
        if shouldStopExecuting {
            self.willChangeValue(forKey: "isExecuting")
        }

        self.state.isFinished = true
        self.state.isExecuting = false

        if shouldStopExecuting {
            self.didChangeValue(forKey: "isExecuting")
        }
        if shouldFinish {
            self.didChangeValue(forKey: "isFinished")
        }
    }

}
```

## 最后的想法

`NSOperation` 是一种强大的方式，可以封装工作，并通过依赖关系和 `NSOperationQueue` 的优先级排序来构建工作的组合。它可靠、灵活，并且可以根据你的使用场景进行扩展。

最重要的事情是确保你正确实现了 `NSOperation` 子类，这伴随着许多细微差别。不过，一旦你掌握了一次，它就是一个易于重复的过程，可以大规模利用，特别是如果你抽象出异步操作的基础实现的话。
