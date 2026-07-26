---
title: NSOperation Subclassing
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
---

> 原文：[NSOperation Subclassing](https://nsprogrammer.github.io/jekyll/update/2021/07/02/nsoperation.html)

## Why this post?

There are plenty of resources on [`NSOperation`](https://developer.apple.com/documentation/foundation/nsoperation) out in there, so it is probably just more noise in the ether.

However, it is also one of the questions I get the most from industry colleagues, because there’s nuance and that makes it tough to commit to memory or concretely discover with a Google search.

So this post will not go into the benefits of `NSOperation` or give a history review of the API over the years or even provide examples of using the API… it is just going to document how to subclass `NSOperation` so that it can be used for your use cases.

## Short NSOperation Preamble

Having used `NSOperation` since its introduction in _Mac OS X 10.5_, I have seen it go through a bumpy ride. It definitely has a history of bugs that have hurt the developer community’s perception for this API, but as of _iOS 10_ / _macOS 10.12_ it has stabilized and is very much _the_ way to organize large units of work on Apple platforms. As interesting as going through the history of problems would be, that is in the past and we can focus on it being solid now. That’s means (at the time of this post) there are 5 releases worth of rock solid support, so it isn’t the same risk as it has been in the past.

Putting everything “substantial” in an `NSOperation` gives you many features to leverage that would be complicated to build on your own, not to mention inefficient compared to Apple’s own optimized API. I’m not going to go through the benefits or features in this post, just keeping it on topic to _“how to subclass NSOperation”_.

### Note on _async await_

The new `async await` available for iOS 15+ introduced at WWDC 2021 is an excellent addition to Swift that will offer a great deal of value to developers doing async and concurrent programming. There is no competition between `async await` and `NSOperation` though; saying that `NSOperation` is no longer useful since `async await` was introduced would be akin to saying `NSOperation` is no longer useful because `GCD` exists. They serve different purposes and actually complement each other. ~~You can implement your `NSOperation` (`Operation` in Swift) using `async await` without issue!~~ _Update:_ I actually spent a good amount of time on this and can’t figure out a way to implement `NSOperation` using `async await`… It is simple enough to use `NSOperation` from async contexts, but I could not get the KVO inside `NSOperation` to work using the new concurrency features of Swift 🤷‍♂️.

## NSOperation Intro

`NSOperation` effectively offers an API to encapsulate a unit of work that can be submitted to a priority queue, an [`NSOperationQueue`](https://developer.apple.com/documentation/foundation/nsoperationqueue).

The `NSOperation` class itself is not terribly useful. To really have utility, it must be subclassed so that “work” can be executed and the pattern of `NSOperation` can be adopted to make use of all the benefits that `NSOperation` has to offer.

Apple gives use two concrete subclasses as a way to get started, which effectively enables 3 specific ways of performing work with an `NSOperation`.

1. Block based work can use `NSBlockOperation`
2. Objective-C object based work can use `NSInvocationOperation`

    - This makes it possible to have the work performed via `target` and `selector`, or via an `NSInvocation`

As valuable as having these convient concrete classes are, more control can be necessary for complex operations. This is where custom subclasses come in.

## Anatomy of an NSOperation

The [`NSOperation`](https://developer.apple.com/documentation/foundation/nsoperation) has a number of properties that control how it works (obviously).

There are KVO properties for controlling the operation execution and signal its progress:

- `isCancelled`
- `isExecuting`
- `isFinished`
- `isReady`

There are properties controlling it’s exectuion:

- `qualityOfService`
- `queuePriority`
- `dependencies`
- `completionBlock`

The property to distinguish its operating behavior:

- `isAsynchronous`

## Asynchronous vs Synchronous Operations

Before we go into the other parts of `NSOperation`, it is worth calling out up front that there are two modes for `NSOperation`: `isAsynchronous` being `NO` and `isAsynchronous` being `YES`.

This property disambiguates the way the operation operations (asynchronously vs synchronously), but actually completely splits _how_ we subclass `NSOperation`. This is probably the most important callout to make when subclassing `NSOperation` – the single base class has two completely different patterns to follow when subclassing based on whether the operation is asynchronous or synchronous.

Effectively, synchronous `NSOperation` subclasses can defer all of the KVO related bookkeeping to the super class’ implementation. They just need to implement the “work”, to run synchronously, and that is it. All the Apple provided concrete `NSOperation` classes (`NSBlockOperation` and `NSInvocationOperation`) are synchronous.

When it comes to asynchronous subclassing, there is a great deal of care and nuance required to properly having things operate within the system.

## The KVO Properties of NSOperation

The execution of an `NSOperation` (and other dependent `NSOperation` instances for that matter) is gated by the state of the KVO state properties.

First is `isReady`. While `isReady` is `NO`, the operation will not be dequeued by the `NSOperationQueue`. Once `isReady` becomes `YES`, the operation can start (as long as there is capacity for the `NSOperationQueue` to run it, of course).

Then, when the operation starts, it moves `isExecuting` from `NO` to `YES`.

Then the work happens, whether it is synchronous or asynchronous.

On the work’s completion, `isExecuting` goes back to `NO`.

Finally, the operation finishes by moving `isFinished` from `NO` to `YES`.

All of the above is completely managed for you by synchronous `NSOperation` subclasses. Asynchronous subclasses must manage this state and their transitions all on their own.

Additionally, there is the `isCancelled` property. By default, calling `cancel` on an `NSOperation` just flips `isCancelled` to `YES`. As work is executing, the “working” part of the execution is responsible for checking `isCancelled` at appropriate places and finishing early (returning early for synchronous operations, and setting `isExecuting` to `NO` and `isFinished` to `YES` for asynchronous operations).

## _isReady_ specifically

The `isReady` property deserves some special attention. The property prevents the operation from running in a queue until it is set to `YES`. This property is effectively coupled to all the `dependencies` of the `NSOperation` being `isFinished == YES`. Unfortunately, the implementation details are hidden so if you override `isReady` in your subclass you will not be able to properly reflect the dependency graph so overriding `isReady` effectively means you are replacing the behavior with your own and the `dependencies` will no longer have an effect.

Beyond `isReady` being coupled to `dependencies` being finished, it will also flip to `YES` when `isCancelled` is set to `YES` before the operation has actually started in its queue. This makes it possible to rapidly have the operation start and immediately finish, clearing it from the queue and unblocking operations that depend on it.

Ultimately, there is enough nuance and trouble around `isReady` that it is best to _never_ override it. If you need to apply custom behavior to have `isReady` depend on, the simplest choice is to use other `NSOperation` objects as dependencies. Once you think of `isReady` as just `areAllDependenciesFinished`, it becomes much easier to reason about and you can easily build blocking behavior for running your operation with other operations as `dependencies`.

## Implementing Synchronous NSOperation

Synchronous `NSOperation` subclassing is the most straightforward option, so let’s go through what that can look like.

Per the documentation, all you really need to do is implement `main` with synchronously executing work.

### Objective-C Code

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

### Swift Code

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

## Implementing Asynchronous NSOperation

Asynchronous `NSOperation` subclassing has a lot more nuance to it.

Instead of overriding `main`, you will override `start`. You also need to override the state properties.

It is important to keep things thread safe, you don’t know what thread any of the state accessors will be called from. In my sample implementations, I will use `@synchronized(self)` which effectively yields a recursive pthread mutex under the hood. If you want to use a different synchronization mechanism, feel free, but keep a few things in mind.

First, for maximum robustness, you will want to encapsulate multiple reads and writes to different states values within in a critical section. That means making each state value atomic is insufficient for maximum thread safety. You might be able to get away with only keeping your state values atomic, but unless you can prove there is a performance need, encapsulating state reads/writes with critical sections is going to be the simpler choice.

Second, you’ll also need to be sure that your critical sections support recursion. Since we are managing KVO as we update state, that will lead to accessing the KVO property while in the critical section (every `willChangeValueForKey:` and `didChangeValueForKey:` call will access the property of the given key). If you go with atomic state values instead of a critical section pattern, you won’t need to worry about recursion (but the race conditions will be more of a risk).

### Objective-C Code

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

#pragma mark State Accessors

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

#pragma mark Method Overrides

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

#pragma mark Private Methods

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

/* this method must be called from a safely synchronized critical section */
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

### Swift Code

Implemented with `NSRecursiveLock`. Same functionally as the Objective-C version. ~~Can implement using `async/await` with Swift 5.5, but it will get somewhat messy with back and forth between async contexts and non-async contexts – feel free to share with me a clean implementation :)~~ _Update_ I could not figure out how to implement `NSOperation` in Swift using `async await` – if you can, please share!

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

    // MARK: State Accessors

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

    // MARK: Method Overrides

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

    // MARK: Private Methods

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

    /* this func must be called from a safely synchronized critical section */
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

## Final Thoughts

`NSOperation` is a powerful way to encapsulate work and construct composition of work through dependencies and with the priority ordering of an `NSOperationQueue`. It is reliable, flexible and extendable to your use cases.

The biggest thing is to be sure you are properly implementing your `NSOperation` subclasses, which comes with a lot of nuance. Once you have it down once though, it is an easily repeatable process that can be leveraged at scale, especially if you abstract out the base implementation of an async operation.
