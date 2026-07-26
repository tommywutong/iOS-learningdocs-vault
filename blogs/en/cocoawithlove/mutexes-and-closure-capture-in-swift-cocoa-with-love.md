---
title: 'Mutexes and closure capture in Swift | Cocoa with Love'
source: Cocoa with Love (Matt Gallagher)
source_key: cocoawithlove
source_url: 'https://www.cocoawithlove.com/blog/2016/06/02/threads-and-mutexes.html'
original_language: en
published: 2016-06-02
status: frozen
license: All rights reserved（页脚明示）→ 严格私有
archived_at: 2026-07-27
content_hash: 'sha256:f20f5d69a21de364'
translated: false
---

> 原文：[Mutexes and closure capture in Swift | Cocoa with Love](https://www.cocoawithlove.com/blog/2016/06/02/threads-and-mutexes.html)　·　Cocoa with Love (Matt Gallagher)

I want to briefly talk about the absence of threading and thread synchronization language features in Swift. I’ll discuss the “concurrency” proposal for Swift’s future and how, until this feature appears, Swift threading will involve traditional mutexes and shared mutable state.

Using a mutex in Swift isn’t particularly difficult but I’m going to use the topic to highlight a subtle performance nuisance in Swift: dynamic heap allocation during closure capture. We want our mutex to be fast but passing a closure to execute inside a mutex can reduce the performance by a factor of 10 due to memory allocation overhead. I’ll look at a few different ways to solve the problem.

## An absence of threading in Swift

When Swift was first announced in June 2014, I felt there were two obvious omissions from the language:

- error handling
- threading and thread synchronization

Error handling was addressed in Swift 2 and was one of the key features of that release.

As of Swift 4, threading remains largely ignored by Swift. Instead of language features for threading, Swift includes the `Dispatch` module (libdispatch, aka Grand Central Dispatch) on all platforms and implicitly suggests: use `Dispatch` instead of expecting the language to help.

Delegating responsibility to a bundled library seems particularly strange compared to other modern languages like Go and Rust that have made threading primitives and strict thread safety (respectively) core features of their languages. Even Objective-C’s `@synchronized` and `atomic` properties seem like a generous offering compared to Swift’s _nothing_.

What’s the reasoning behing this apparent omission in Swift?

## Future “concurrency” in Swift

One possible future is, somewhat tersely, discussed in the [“Concurrency” proposal in the Swift repository](https://github.com/apple/swift/blob/c760f6dfbf0179e9aff90f7bf7375f3af5331318/docs/proposals/Concurrency.rst).

> I mention this proposal to highlight that the Swift developers would like to do _something_ around concurrency in the future but keep in mind what [Swift developer Joe Groff points out](https://twitter.com/jckarter/status/739109723408994304): “that document is only a proposal and not an official statement of direction.”

This proposal appears to describe a situation where, like in [Cyclone](http://homes.cs.washington.edu/~djg/papers/cycthreads.pdf) or [Rust](http://blog.rust-lang.org/2015/04/10/Fearless-Concurrency.html), references can’t be shared between threads. In that possible scenario, the plan would be for Swift to eliminate shared memory between threads except for types that implement `Copyable` and are passed through strictly governed channels (called `Stream`s in the proposal). There’s also going to be a form of coroutine (called `Task`s in the proposal) which appear to behave like pausable/resumable asynchronous dispatch blocks.

The proposal then goes on to claim that most common threading _language_ features (Go-like `chan`nels, .NET-like `async`/`await`, Erlang-style `actor`s) can then be implemented in _libraries_ on top of the `Stream`/`Task`/`Copyable` primitives.

It all sounds great but when is Swift’s concurrency expected? Swift 5.1? Unlikely. Swift 6? Maybe. Don’t hold your breath.

## Trying to find a fast, general purpose mutex

In the short term, if we want multi-threaded behavior, we need to build it ourselves using pre-existing threading and mutex features.

The [common advice for mutexes in Swift](http://stackoverflow.com/questions/24045895/what-is-the-swift-equivalent-to-objective-cs-synchronized) is usually: use a `DispatchQueue` and invoke `sync` on it.

I love libdispatch but, in most cases, using `DispatchQueue.sync` as a mutex is in the slowest tier of solutions to the problem – more than an _order of magnitude_ slower than other options due to unavoidable closure capture overhead for the closure passed to the `sync` function. This is not because libdispatch is an inherently slow library but instead occurs due to an unavoidable complication between its API and Swift: closure capture. Specifically, any closure we pass to `DispatchQueue.sync` needs to capture a reference to the protected resource that you use within its closure and this capturing involves a heap allocation that can’t be optimized away because the contents of the function exist in another library.

> I’m going to talk about the speed of mutexes with respect to each other. If you’re interested in raw numbers, they’re in a table at the end of this article.

We don’t get heap allocation for most closures in Swift because Swift can inline them, eliminating the closure entirely. This is why most closures used entirely within your own project are fast. Since Swift always inlines the standard library, closures passed to it are also fast. For `DispatchQueue.sync` though, inlining is not possible because the contents of the function exist in a separate module (written in C) so Swift can’t optimize away the closure capture, making `DispatchQueue.sync` an unnecessarily slow choice in Swift.

The next most commonly suggested option I see is `objc_sync_enter`/`objc_sync_exit`. While the machinery here is slow, the fact that we can make the calls directly around our own code mean that we can avoid a closure and the associated capture, making it around 8 times faster than `DispatchQueue.sync`. It’s a little slower than ideal (because it is a _re-entrant_ mutex and really just wraps underlying `pthread_mutex_t` machinery in another layer) but its not too bad. However, it is limited to Apple platforms so Linux support is out.

The fastest option for a mutex used to be `OSSpinLock` – more than 20 times faster than `dispatch_sync` – but this function is now deprecated and you shouldn’t use it. Aside from the standard limitations of a spin-lock (high CPU usage if multiple threads actually try to enter simultaneously) there are some [serious scheduling problems that render make this mutex problematic on macOS and totally unusable on iOS](https://lists.swift.org/pipermail/swift-dev/Week-of-Mon-20151214/000372.html).

The fastest realistic option is `os_unfair_lock` which is 3 times faster than `objc_sync_enter`/`objc_sync_exit` and only 30% slower than `OSSpinLock`. However, this lock is not first-in-first-out (FIFO). Instead, the mutex is given to an arbitrary waiter (hence, “unfair”). You need to decide if this is a problem for your program but in general, this means that it shouldn’t be your first choice for a general purpose mutex. It’s also limited to Apple platforms.

The final choice is the old C favorite: `pthread_mutex_lock`/`pthread_mutex_unlock`. This mutex is reasonable performance mutex (just 40% slower than `os_unfair_lock`), is portable and it is fair – so you won’t get waiter starvation. Or at least it used to be fair – apparently in mac OS 10.14 and iOS 12 and later it uses a waiting policy closer to “unfair”, by default. Why? Probably to avoid accidental priority inversion. How much does unfairness matter? It’s unclear – the precise scheduling involved for the default `PTHREAD_MUTEX_POLICY_FIRSTFIT_NP` policy is unclear.

## Mutexes and closure capture pitfalls

I’m going to proceed to talk about `pthred_mutex_t` - although most of the lessons would apply equally to any of the separate `lock`/`unlock` mutexes (including `objc_sync_enter`, `os_unfair_lock`).

Let’s implement our own `sync` function using `pthread_mutex_lock`/`pthread_mutex_unlock` in a library module. I’ll ignore the initialization because what I want to focus upon is getting code to run inside the mutex. The standard approach is to implement a `sync` function. That looks a little something like this:

```swift
public class PThreadMutex {
   var mutex: pthread_mutex_t
   
   public init() { /* ... */ }
   
   public func sync<R>(execute: () throws -> R) rethrows -> R {
      pthread_mutex_lock(&mutex)
      defer { pthread_mutex_unlock(&mutex) }
      return try execute()
   }
}
```

This was supposed to be high performance but it’s not.

If I put this function in another module, the same performance problem remains: Swift can’t perform cross-module inlining so the closure can’t be inlined and closure capture costs an order of magnitude slow-down.

## Avoid capturing

We need to avoid closure capture and the associated heap allocation. Let’s avoid it by passing the relevant parameter into the closure, instead of capturing it. If our closure doesn’t _capture_ then it should need to allocate space.

```swift
public extension PThreadMutex {
   func sync_generic_param<T, R>(_ p: inout T, execute: (inout T) -> R) -> R {
      pthread_mutex_lock(&mutex)
      defer { pthread_mutex_unlock(&mutex) }
      return execute(&p)
   }
}
```

That’s better… now if I invoke this function with an `Int` as the parameter, a `Double` as the return type and the function runs at nearly full speed (about 10% slower than inlined pthread calls).

## Enable inlining

We’re still 10% slower than ideal but passing via a single generic parameter is just a little clunky. The nice thing about closures is how natural they feel.

Let’s see if we can get the closure approach working at full speed. To do this, we need to give the compiler the ability to inline the closure and eliminate the need to capture by copying the code into the file where it is used.

To do this, we can add the following extension on `PThreadMutex` to the same file where it is called:

```swift
private extension PThreadMutex {
   func sync_same_file<R>(execute: () throws -> R) rethrows -> R {
      pthread_mutex_lock(&m)
      defer { pthread_mutex_unlock(&m) }
      return try execute()
   }
}
```

This lets Swift inline the whole function, eliminating retain/release overhead and we’re finally down to the baseline 100% performance.

Yes, I’m really suggesting that you copy and paste code to avoid closure capture. If you’re using whole module optimization (default for release builds since Swift 3), you don’t have to paste it to the same file; you can paste to anywhere in the module.

But if you need maximum performance on specific functions, replicating your code in each module is what is required in Swift (until cross-module inlining arrives in some future version of the compiler).

## Semaphores, not mutexes?

After I originally wrote the article, a few people asked… why not use a `dispatch_semaphore_t` instead? The advantage with `dispatch_semaphore_wait` and `dispatch_semaphore_signal` is that no closure is required – they are separate, unscoped calls, just like `pthread_mutex_lock`/`pthread_mutex_unlock`.

You could use `dispatch_semaphore_t` to create a mutex-like construct as follows:

```swift
public struct DispatchSemaphoreWrapper {
   let s = DispatchSemaphore(value: 1)
   init() {}
   func sync<R>(execute: () -> Void)  {
      _ = s.wait(timeout: DispatchTime.distantFuture)
      defer { s.signal() }
      execute()
   }
}
```

In the same module, it’s approximately the same speed as an `os_unfair_lock`. However, if you put this in a separate module, you’ll still get the same closure capture problems for the `execute` closure that all previous separate-module implementations have had.

And there are more serious risks to abusing a semaphore this way.

Semaphores are a good way to communicate completion notifications between a worker and a listener thread (something that isn’t easily done with mutexes since they must be released on the same thread that they’re acquired). But the fact that a semaphore is not tied to a thread leads to to a number of [priority inversion](https://en.wikipedia.org/wiki/Priority_inversion) problems when used as a mutex. The system cannot apply thread priority logic to a semaphore low priority threads can starve high priority threads and deadlocks can occur between trios of waiting threads with different priorities. Priority inversion is the same type of problem that made `OSSpinLock` usable iOS and while the problem for semaphores is a little more complicated, it can still lead to your app deadlocking when multiple threads of different priority are involved.

All of this might seem a little esoteric – since you probably don’t deliberately create threads of different priorities in your own programs. However, the Cocoa frameworks add a little twist here that you need to consider: Cocoa frameworks use dispatch queues pervasively and every dispatch queue has a “QoS class” which may result in the queue running at a different thread priority. Unless you know how every task in your program is queued (including user-interface and other tasks queued by the Cocoa frameworks), you might find yourself in a multiple thread priority scenario that you didn’t plan.

It’s best to avoid this risk – at least in the general case.

## Usage

> A project containing wrappers around `PThreadMutex` and `UnfairLock` implementation is available on github: [mattgallagher/CwlUtils](https://github.com/mattgallagher/CwlUtils).

The [CwlMutex.swift](https://github.com/mattgallagher/CwlUtils/blob/master/Sources/CwlUtils/CwlMutex.swift?ts=3) file is fully self-contained so you can just copy the file, if that’s all you need. For performance, I recommend that you either make `internal`/`private` copies of the `sync` functions in the compilation units (modules or files depending on whole module optimization) where they are used or use the `unbalancedLock` and `unbalancedUnlock` functions to avoid closure capture.

The [ReadMe.md file for the project](https://github.com/mattgallagher/CwlUtils/blob/master/README.md) contains detailed information on cloning the whole repository and adding the framework it produces to your own projects.

## Conclusion

The simplest option for a mutex might remain `DispatchQueue.sync`. It has a Swift wrapper and broad support in the standard library.

If you need a significant level of performance, then `os_unfair_lock` or `pthread_mutex_t` are the only real options. There are other options but they have complications that preclude use in general circumstances. Neither of these is strictly “fair”. You can configure a `pthread_mutex_t` to be fair but it is (at least partially) unfair by default – and this might be a good thing since it avoids accidental priority deadlocks.

But regardless of your choice of mutex API, achieving maximum performance in Swift requires avoiding heap allocation and heap allocations are a common problem affecting typical `sync` functions that take a closure. The heap allocations for the closure capture context slow a typical mutex `sync` function by an order of magnitude (i.e. roughly ten times slower).

To avoid closure capture for the typical `sync` function requires that either the whole function be copied from any library module into the compilation module where it is used or that you redefine the closure function with built-in parameters to avoid the need to capture with the closure. Copy and paste between modules is often the best solution to enable inlining at this time (stack allocated closures are finally coming in Swift 5 or shortly thereafter).

Threading, asynchrony, concurrency and inlining are all topics I hope will change dramatically beyond Swift 5 but it’s still too early to hold my breath.

## Appendix: performance numbers

I ran a simple loop, 10 million times, entering a mutex, incrementing a counter, and leaving the mutex. The “slow” versions of `DispatchSemaphore` and `PThreadMutex` are compiled as part of a dynamic framework, separate to the test code.

These are the timing results:

| Mutex variant | Seconds (Swift 3.0, MacPro 4,1) | Seconds (Swift 4.2, MacBookPro 15,1) | Seconds (Swift 5.0 master 2019-01-19, MacBookPro 15,1) |
|---|---|---|---|
| `DispatchQueue.sync` | 3.530 | 3.687 | 3.484 |
| `PThreadMutex.sync` (capturing closure) | 3.124 | 2.015 | 0.384 (0.212 with exclusivity disabled) |
| `objc_sync_enter`/`objc_sync_exit` | 0.833 | 0.446 | 0.422 |
| `PThreadMutex.sync_generic_param` (non-capturing) | 0.284 | 0.184 | 0.284 (0.182 with exclusivity disabled) |
| `PThreadMutex.sync_same_file` (inlined) | 0.265 | 0.175 | 0.171 |
| `pthread_mutex_lock`/`pthread_mutex_unlock` | 0.263 | 0.175 | 0.172 |
| `os_unfair_lock_lock`/`os_unfair_lock_unlock` | 0.187 | 0.130 | 0.12 |
| `OSSpinLockLock`/`OSSpinLockUnlock` | 0.108 | 0.075 | 0.069 |

The test code used is part of the linked [CwlUtils](https://github.com/mattgallagher/CwlUtils) project but the test file containing these performance tests (CwlMutexPerformanceTests.swift) is not linked into the test module by default and must be deliberately enabled.
