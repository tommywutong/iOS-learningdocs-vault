---
title: 保护临界区
source_url: 'https://solarana.dev/2018/04/15/protecting-critical-sections/'
source_domain: solarana.dev
source_group: single-site
original_language: en
published: 2018-04-15
archived_at: 2026-07-27
content_hash: 'sha256:ed0daf78260f3c8d'
plan_ref: 第四周：线程、GCD、Operation 与锁 / Day 6｜锁的学习方式是“按约束选择”（对应 W3-11）
plan_week: 第四周：线程、GCD、Operation 与锁
plan_day: Day 6｜锁的学习方式是“按约束选择”（对应 W3-11）
container: '//*[contains(@class,''post-content'')]'
container_source: guess
translated: true
---

> 原文：[Protecting Critical Sections](https://solarana.dev/2018/04/15/protecting-critical-sections/)

在开发 App 或框架（framework）时，你迟早会遇到需要在受控环境中执行某些工作的问题。为了保证所做工作的安全性，你需要锁定那条特定路径，使其在运行时状态不会发生变化。这就叫做[临界区（critical section）](https://en.wikipedia.org/wiki/Critical_section)。幸运的是，Apple 开发平台提供了大量选项来实现可并行的代码。然而，每个选项在使用时认知负荷不同，因此根据你要达成的并发（concurrency）类型来使用不同的实现，可能对你最有利。

## POSIX Mutex

符合 [POSIX](https://en.wikipedia.org/wiki/POSIX) 标准的系统提供了 pthreads 库，其中包含一个互斥锁（[lock（锁）](https://en.wikipedia.org/wiki/Lock_(computer_science))）实现：`pthread_mutex_t`。该 API 创建了一个阻塞锁（可选择配置为递归锁），并且必须使用特定函数进行初始化和销毁。由于这些函数接收的是互斥锁的引用，你不能直接传入互斥锁的 property（属性）地址，而需要直接传入 iVar。因此，这类互斥锁的大多数实例都定义在某个全局作用域中，而不是作为 Objective-C 类的 property/iVar。但这并不意味着你不能把互斥锁存储为 property[^1](https://stackoverflow.com/questions/9086736/why-would-you-use-an-ivar)，只是需要对底层的 iVar 进行解引用（如果不小心会引入 `NULL` 解引用问题：`NULL` 的行为与 `nil` 不同）。

pthreads 库还提供了另一种变体 `pthread_rwlock_t`。这是一种[读写锁（readers/writer lock）](https://en.wikipedia.org/wiki/Readers%E2%80%93writer_lock)，允许多个线程获取临界区的值，但同一时间只允许一个线程修改临界区的值。对于可以安全允许多个只读访问者、但只允许一个写入访问者的代码场景，使用这种锁而不是标准的 `pthread_mutex_t` 可以提升性能。

示例：

```obj
// 非递归
pthread_mutex_t mutex;
pthread_mutex_init(&mutex, NULL);
pthread_mutex_lock(&mutex);
[someObject doWork];
pthread_mutex_unlock(&mutex);
pthread_mutex_destroy(&mutex);

// 递归
pthread_mutexattr_t attr;
pthread_mutexattr_init(&attr);
pthread_mutexattr_settype(&attr, PTHREAD_MUTEX_RECURSIVE);
pthread_mutex_t mutex;
pthread_mutex_init(&mutex, &attr);
pthread_mutex_lock(&mutex);
[someObject doWork];
pthread_mutex_unlock(&mutex);
pthread_mutex_destroy(&mutex);
pthread_mutexattr_destroy(&attr);
```

Apple 实现的源代码可以在[这里](https://opensource.apple.com/source/libpthread/)找到。

## @synchronized

Objective-C 提供了 `@synchronized` 指令形式的语言特性来实现同步。该指令可以应用于任意 Objective-C 对象，因此你既可以同步 `self`，也可以同步实例/类的任何 property 或关联对象。在底层，编译器会将代码转换为以下形式：

```obj
// 源代码
@synchronized(self) {
  [someObject doWork];
}

// 编译器替换，object 是指令传入的参数
@try {
  objc_sync_enter(object);
  [someObject doWork];
}
@finally {
  objc_sync_exit(object);
}
```

这些同步函数会为你分配和管理一个 `pthread_mutex_t`，并提供了一些错误处理机制，以便在执行过程中抛出异常时释放锁。然而，异常处理以及[锁实现本身](https://opensource.apple.com/source/objc4/objc4-723/runtime/objc-sync.mm.auto.html)（包含其对象表和[可重入性](https://en.wikipedia.org/wiki/Reentrancy_(computing))）带来了开销；如果你不需要这些特性，可以通过使用显式锁来消除。但作为语言构造提供，你得到了易于实现的同步。与计算机科学中的一切一样，每件事都有权衡；如果你能通过在其他地方弥补代价来承担这个成本，那就没问题。

Apple 实现的源代码可以在[这里](https://opensource.apple.com/source/objc4/)找到。

## os_unfair_lock

在 iOS 10 和 macOS 10.12 发布之前，Apple 通过[内核 API](https://developer.apple.com/documentation/kernel/osatomic.h?language=objc) 提供了原子功能（特别是 `OSSpinLock`）。然而，[自旋锁（spinlock）](https://en.wikipedia.org/wiki/Spinlock)在 iOS 上一直不可用，因为自旋会[浪费 CPU 资源](https://en.wikipedia.org/wiki/Starvation_(computer_science))，并可能导致[死锁（deadlock）](https://en.wikipedia.org/wiki/Deadlock)。现在，该 API 已被废弃，一个新的 [API](https://developer.apple.com/documentation/os/synchronization?language=objc) 可供使用：`os_unfair_lock`，它适用于所有 Apple 平台。

顾名思义，它是不公平的（[unfair](https://en.wikipedia.org/wiki/Unbounded_nondeterminism#Fairness)）。这意味着，如果有多个线程试图获取此锁，无法保证资源会被分配以使所有线程获得相同优先级，从而导致单个线程独占锁。这是一个权衡，目的是让锁在不需要公平性的情况下表现更好，并保持其较小的开销。

示例：

```obj
os_unfair_lock unfairLock = OS_UNFAIR_LOCK_INIT;
os_unfair_lock_lock(&unfairLock);
[someObject doWork];
os_unfair_lock_unlock(&unfairLock);
```

Apple 实现的源代码可以在[这里](https://opensource.apple.com/source/libplatform/)找到。

## NSLock

如果你更习惯使用 Objective-C 对象而不是处理 C API，Apple 通过 [NSLock](https://developer.apple.com/documentation/foundation/nslock?language=objc) 及其同类 [NSRecursiveLock](https://developer.apple.com/documentation/foundation/nsrecursivelock?language=objc)、[NSDistributedLock](https://developer.apple.com/documentation/foundation/nsdistributedlock?language=objc) 和 [NSConditionLock](https://developer.apple.com/documentation/foundation/nsconditionlock?language=objc)，提供了 POSIX 锁的封装。由于这些是封装，使用锁就像调用 `lock` 和 `unlock` 一样简单（除了 NSDistributedLock 和 NSConditionLock，它们有特定于实现的 API），因为底层的复杂性已被抽象化。

示例：

```obj
// 非递归
NSLock *lock = [[NSLock alloc] init];
[lock lock];
[someObject doWork];
[lock unlock];

// 递归
NSRecursiveLock *lock = [[NSRecursiveLock alloc] init];
[lock lock];
[someObject doWork];
[lock unlock];
```

## Grand Central Dispatch

除了使用锁，你还可以使用[队列](https://en.wikipedia.org/wiki/Priority_queue)（串行或并发）。将工作提交给 [GCD](https://developer.apple.com/documentation/dispatch?language=objc) 队列可以同步或异步进行，并且还有[屏障（barrier）](https://en.wikipedia.org/wiki/Barrier_(computer_science))变体，它们会等待现有提交执行完毕后再执行自身。系统提供了执行工作的默认队列：

- `QOS_CLASS_USER_INTERACTIVE`，即主（UI）队列
- `QOS_CLASS_USER_INITIATED`（原 `DISPATCH_QUEUE_PRIORITY_HIGH`）
- `QOS_CLASS_DEFAULT`（原 `DISPATCH_QUEUE_PRIORITY_DEFAULT`）
- `QOS_CLASS_UTILITY`（原 `DISPATCH_QUEUE_PRIORITY_LOW`）
- `QOS_CLASS_BACKGROUND`（原 `DISPATCH_QUEUE_PRIORITY_BACKGROUND`）

不过，你也可以创建自己的队列，就像可以创建自己的线程一样。需要注意的一点是，如果递归地进入队列，将会导致死锁，因此你需要小心处理你的调度（幸运的是，GCD 为你处理了[优先级反转（priority inversion）](https://en.wikipedia.org/wiki/Priority_inversion)问题）。

示例：

```obj
// 使用 DISPATCH_QUEUE_SERIAL 创建串行队列
dispatch_queue_attr_t attr = dispatch_queue_attr_make_with_qos_class(DISPATCH_QUEUE_CONCURRENT, QOS_CLASS_UTILITY, 0);
dispatch_queue_t queue = dispatch_queue_create("com.example.concurrent-queue", attr);
// 阻塞调用线程直至执行完成
dispatch_sync(queue, ^{
  [someObject doWork];
});
// 不阻塞调用线程，立即返回
dispatch_async(queue, ^{
  [someObject doWork];
});
// 阻塞调用线程，等待之前提交的 block 执行完毕
dispatch_barrier_sync(queue, ^{
  [someObject doWork];
});
// 不阻塞调用线程，等待之前提交的 block 执行完毕
dispatch_barrier_async(queue, ^{
  [someObject doWork];
});
```

Apple 实现的源代码可以在[这里](https://opensource.apple.com/source/libdispatch/)找到。

## NSOperationQueue

与 NSLock 类似，Apple 以 [NSOperationQueue](https://developer.apple.com/documentation/foundation/nsoperationqueue?language=objc) 的形式提供了 GCD 的封装。NSOperationQueue 不接收 block，而是接收 [NSOperation](https://developer.apple.com/documentation/foundation/nsoperation?language=objc) 的子类，例如 [NSBlockOperation](https://developer.apple.com/documentation/foundation/nsblockoperation?language=objc) 和 [NSInvocationOperation](https://developer.apple.com/documentation/foundation/nsinvocationoperation?language=objc)（你也可以创建自己的子类）。通过利用具体的操作，你还可以添加依赖关系，使得某些操作在其依赖完成之前不会执行；它还允许你取消正在执行或尚未开始的操作（你也可以挂起操作队列以暂停所有执行）。与 GCD 不同，唯一的全局操作队列是主队列，但和 GCD 一样，你可以创建自己的操作队列。

示例：

```obj
NSOperationQueue *operationQueue = [[NSOperationQueue alloc] init];
operationQueue.name = @"com.example.concurrent-operation-queue";
operationQueue.maxConcurrentOperationCount = 10; // Default is 1, aka serial
operationQueue.qualityOfService = NSQualityOfServiceUtility;
// 创建一个匿名 block 操作
[operationQueue addOperationWithBlock:^{
  [someObject doWork];
}];
// 添加一个具体 NSOperation 的实例
[operationQueue addOperation:someOperation];
```

## 信号量（Semaphore）

pthread 库和 GCD 也都提供了[信号量（semaphore）](https://en.wikipedia.org/wiki/Semaphore_(programming))实现作为一种同步形式（尽管 pthread 的实现已废弃）。信号量与锁类似，调用线程请求（锁定）共享资源，然后在完成使用时发出信号（解锁）。信号量的行为类似于阻塞锁，会阻塞调用线程直到其可用。因此，重要的是，调用信号量保护代码的线程应具有相同的优先级，因为它们不能从[优先级继承（priority inheritance）](https://en.wikipedia.org/wiki/Priority_inheritance)中受益。

POSIX 示例：

```obj
sem_t semaphore = sem_init(&semaphore, 0, 1);
sem_wait(&semaphore);
[someObject doWork];
sem_post(&semaphore);
sem_destroy(&semaphore);
```

GCD 示例：

```obj
dispatch_semaphore_t semaphore = dispatch_semaphore_create(1);
// 可以通过 dispatch_time 函数将时间配置为任何值
dispatch_semaphore_wait(semaphore, DISPATCH_TIME_FOREVER);
[someObject doWork];
dispatch_semaphore_signal(semaphore);
```

## 原子操作（Atomics）

如果你想实现无锁操作，[C11](http://en.cppreference.com/w/c/atomic) 和 [C++11](http://en.cppreference.com/w/cpp/atomic) 标准引入了内建原子操作。这些类型和函数提供了一种不使用锁的并发实现，并通过消除[数据争用（data races）](https://en.wikipedia.org/wiki/Race_condition)来[保证进展（guarantee progress）](http://en.cppreference.com/w/cpp/language/memory_model#Threads_and_data_races)。不幸的是，这仅适用于所提供的类型，而 Objective-C 类并不包含在内。但这确实意味着你可以将这些原子类型作为类中的 property，而无需实现额外的并发逻辑，因为你只需通过调用相应的原子函数来实现 getter 和 setter，或者提供便捷方法（convenience method）来获取和设置 property，而不必公开暴露该 property。

示例：

```obj
atomic_int aInt;
atomic_store(&aInt, 10); // Set initial value to 10
atomic_fetch_add(&aInt, 2); // Add 2
atomic_fetch_sub(&aInt, 1); // Subtract 1
```

## 性能

通过修改 [Peter Steinberger](https://twitter.com/steipete) 提供的此 [gist](https://gist.github.com/steipete/36350a8a60693d440954b95ea6cbbafc)（针对 Objective-C），以下是一些选项的性能表现（平均值）：

- 并发 GCD 队列：0.109 秒
- Dispatch 信号量：0.052 秒
- NSLock：0.077 秒
- NSRecursiveLock：0.104 秒
- PThread 互斥锁：0.061 秒
- 递归 PThread 互斥锁：0.088 秒
- PThread 信号量：2.100 秒
- 串行 GCD 队列：0.083 秒
- 自旋锁：0.046 秒
- Synchronize：0.170 秒
- 不公平锁：0.050 秒

指标在一台 2016 年 15 英寸 MacBook Pro 上收集，配置为 2.6GHz Intel® Core™ [i7-6700HQ](https://ark.intel.com/products/88967/Intel-Core-i7-6700HQ-Processor-6M-Cache-up-to-3_50-GHz) CPU、16GB 内存，运行 macOS 10.13.4 (17E199)，使用 Xcode 9.4ß1 (9Q1004a) 以优化级别 3 和 monolithic LTO 编译。 [源码](https://gist.github.com/madsolar8582/4537a61f5dedd9a8688cd343d41d5392)

## 故障排除

只要涉及并发，就难免会出现错误，追踪这些[海森堡 bug（heisenbugs）](https://en.wikipedia.org/wiki/Heisenbug)非常困难，因为 CPU 速度、线程数量、正在运行的应用程序等多种因素都可能影响并发操作的结果。为了帮助定位这些问题，Xcode 提供了 [Thread Sanitizer](https://developer.apple.com/documentation/code_diagnostics/thread_sanitizer)。Thread Sanitizer 通过在编译期间对源代码进行插装来检查程序执行期间的内存访问，从而查找并发代码中的错误。因此，实际运行你想要调试的代码非常重要，因为 Thread Sanitizer 无法检查未执行的代码。

另一个健全性检查工具是 Instruments 中的 [Dispatch](https://developer.apple.com/library/content/documentation/DeveloperTools/Conceptual/InstrumentsUserGuide/Instrument-Dispatch.html#//apple_ref/doc/uid/TP40004652-CH51-SW1) 模板。它允许你观察 GCD 的使用方式，并识别代码中潜在的实现问题。类似地，[Time Profiler](https://developer.apple.com/library/content/documentation/DeveloperTools/Conceptual/InstrumentsUserGuide/Instrument-TimeProfiler.html#//apple_ref/doc/uid/TP40004652-CH73-SW1) 模板可用于观察线程等待的时间以及执行所需的时间。

---

并发是困难的，无论你选择哪种方案，都会存在开销。因此，你应该选择在你感觉舒适且对你试图保护的临界区有意义的前提下性能最佳的选项。通过降低读写多线程代码所需的认知负荷，你将能在以后调试时省去很多麻烦（代码需要正常工作，而不是最聪明）。

将来，这可能不成问题。[Swift](https://swift.org/) 和 [Rust](https://www.rust-lang.org/en-US/) 都在试图创造一个程序员无需过深思考并发实现的环境。在本文撰写时，Rust 已将其方案命名为[无畏并发（Fearless Concurrency）](https://doc.rust-lang.org/book/second-edition/ch16-00-concurrency.html)，并提供了语言保证，认为其[内存模型（memory model）](https://doc.rust-lang.org/book/second-edition/ch04-00-understanding-ownership.html)结合其并发概念，可以防止程序员[搬起石头砸自己的脚](https://en.wiktionary.org/wiki/footgun)。而 Swift 由于其 [ABI（Application binary interface）](https://en.wikipedia.org/wiki/Application_binary_interface)尚不稳定，尚未实现其完整的[所有权模型（ownership model）](https://github.com/apple/swift/blob/22530b922f4fcd79b31583ec834fadd90bff07bb/docs/OwnershipManifesto.md)，并且 Swift 维护者也尚未批准并发[提案](https://github.com/apple/swift/blob/22530b922f4fcd79b31583ec834fadd90bff07bb/docs/proposals/Concurrency.rst)。
