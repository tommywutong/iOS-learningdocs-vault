---
title: '并发编程：API 与挑战'
source: objc.io
source_key: objcio
source_url: 'https://www.objc.io/issues/2-concurrency/concurrency-apis-and-pitfalls'
original_language: en
published: ''
status: frozen
license: 未声明（页面无版权声明，文章版权归各作者）→ 仅私有归档
archived_at: 2026-07-27
content_hash: 'sha256:ac69175e942fd5db'
translated: true
---

> 原文：[Concurrent Programming: APIs and Challenges](https://www.objc.io/issues/2-concurrency/concurrency-apis-and-pitfalls)　·　objc.io

[并发](http://en.wikipedia.org/wiki/Concurrency_%28computer_science%29)描述的是同时运行多项任务这一概念。既可以在单个 CPU 核心上以[分时](http://en.wikipedia.org/wiki/Preemption_%28computing%29)方式进行，也可以在有多个 CPU 核心时真正并行执行。

OS X 和 iOS 提供了多种不同的 API 来实现并发编程。每种 API 的能力与限制各不相同，因而适合不同的任务。它们所处的抽象层次也大相径庭。我们可以选择非常贴近底层硬件的方式操作，但这也意味着必须对正确性承担更大的责任。

并发编程是一个非常困难的主题，充满了错综复杂的问题与陷阱；在使用 Grand Central Dispatch 或 `NSOperationQueue` 这类 API 时，很容易忘记这一点。本文将首先概览 OS X 与 iOS 上的各类并发 API，然后深入探讨并发编程固有的挑战——这些挑战与你具体选用哪种 API 无关。

## OS X 与 iOS 上的并发 API

Apple 的移动与桌面操作系统为并发编程提供了相同的 API。本文将介绍 `pthread` 与 `NSThread`、Grand Central Dispatch、`NSOperationQueue`，以及 `NSRunLoop`。严格来说，运行循环（run loop）在这份列表中有些格格不入，因为它们并不能实现真正的并行。但它们与本主题关系足够密切，值得仔细看看。

我们将从较低层的 API 开始，逐步向上介绍较高层的 API。之所以这样安排，是因为高层 API 建立在底层 API 之上。不过，在为你的用例选择 API 时，应采取完全相反的顺序：选择能够完成工作的最高层抽象，并保持并发模型尽可能简单。

如果你好奇我们为何如此坚持推荐高层抽象和非常简单的并发代码，应当阅读本文的第二部分——[并发编程的挑战](#challenges-of-concurrent-programming)，以及 [Peter Steinberger 关于线程安全的文章](https://www.objc.io/issues/2-concurrency/thread-safe-class-design/)。

### 线程

[线程](http://en.wikipedia.org/wiki/Thread_%28computing%29)是进程的子单元，可由操作系统调度器独立调度。几乎所有并发 API 在底层都建立在线程之上——Grand Central Dispatch 与 operation queue 皆是如此。

多个线程可以在单个 CPU 核心上同时执行（至少在观感上是同时的）。操作系统为每个线程分配一小段计算时间片，从而让用户觉得多项任务在同时进行。若有多个 CPU 核心可用，则多个线程可以真正并行执行，从而缩短完成特定工作负载所需的总时间。

你可以使用 Instruments 中的 [CPU strategy view](http://developer.apple.com/library/mac/#documentation/DeveloperTools/Conceptual/InstrumentsUserGuide/AnalysingCPUUsageinYourOSXApp/AnalysingCPUUsageinYourOSXApp.html)，来洞察你的代码或所使用的框架代码如何被调度到多个 CPU 核心上执行。

需要牢记的重要一点是：你无法控制代码在何处、何时被调度执行，也无法控制为了轮到其他任务而暂停执行的时机与时长。这种线程调度是一种非常强大的技术。然而，它也伴随着巨大的复杂性，我们稍后会加以探讨。

暂且抛开这些复杂性不谈，你可以使用 [POSIX thread](http://en.wikipedia.org/wiki/POSIX_Threads) API，或围绕该 API 的 Objective-C 封装 `NSThread`，来创建自己的线程。下面是一个用 `pthread` 在 100 万个数中查找最小与最大值的小示例。它会派生 4 个并行运行的线程。从这个例子中应能明显看出，为何你不想直接使用 pthread。

```
#import <pthread.h>

struct threadInfo {
    uint32_t * inputValues;
    size_t count;
};

struct threadResult {
    uint32_t min;
    uint32_t max;
};

void * findMinAndMax(void *arg)
{
    struct threadInfo const * const info = (struct threadInfo *) arg;
    uint32_t min = UINT32_MAX;
    uint32_t max = 0;
    for (size_t i = 0; i < info->count; ++i) {
        uint32_t v = info->inputValues[i];
        min = MIN(min, v);
        max = MAX(max, v);
    }
    free(arg);
    struct threadResult * const result = (struct threadResult *) malloc(sizeof(*result));
    result->min = min;
    result->max = max;
    return result;
}

int main(int argc, const char * argv[])
{
    size_t const count = 1000000;
    uint32_t inputValues[count];
    
    // Fill input values with random numbers:
    for (size_t i = 0; i < count; ++i) {
        inputValues[i] = arc4random();
    }
    
    // Spawn 4 threads to find the minimum and maximum:
    size_t const threadCount = 4;
    pthread_t tid[threadCount];
    for (size_t i = 0; i < threadCount; ++i) {
        struct threadInfo * const info = (struct threadInfo *) malloc(sizeof(*info));
        size_t offset = (count / threadCount) * i;
        info->inputValues = inputValues + offset;
        info->count = MIN(count - offset, count / threadCount);
        int err = pthread_create(tid + i, NULL, &findMinAndMax, info);
        NSCAssert(err == 0, @"pthread_create() failed: %d", err);
    }
    // Wait for the threads to exit:
    struct threadResult * results[threadCount];
    for (size_t i = 0; i < threadCount; ++i) {
        int err = pthread_join(tid[i], (void **) &(results[i]));
        NSCAssert(err == 0, @"pthread_join() failed: %d", err);
    }
    // Find the min and max:
    uint32_t min = UINT32_MAX;
    uint32_t max = 0;
    for (size_t i = 0; i < threadCount; ++i) {
        min = MIN(min, results[i]->min);
        max = MAX(max, results[i]->max);
        free(results[i]);
        results[i] = NULL;
    }
    
    NSLog(@"min = %u", min);
    NSLog(@"max = %u", max);
    return 0;
}
```

`NSThread` 是围绕 pthread 的简单 Objective-C 封装。这使代码在 Cocoa 环境中看起来更熟悉。例如，你可以将线程定义为 NSThread 的子类，把希望在后台运行的代码封装在其中。对于前面的例子，我们可以像这样定义一个 `NSThread` 子类：

```
@interface FindMinMaxThread : NSThread
@property (nonatomic) NSUInteger min;
@property (nonatomic) NSUInteger max;
- (instancetype)initWithNumbers:(NSArray *)numbers;
@end

@implementation FindMinMaxThread {
    NSArray *_numbers;
}

- (instancetype)initWithNumbers:(NSArray *)numbers 
{
    self = [super init];
    if (self) {
        _numbers = numbers;
    }
    return self;
}

- (void)main
{
    NSUInteger min;
    NSUInteger max;
    // process the data
    self.min = min;
    self.max = max;
}
@end
```

要启动新线程，需要创建新的线程对象并调用其 `start` 方法：

```
NSMutableSet *threads = [NSMutableSet set];
NSUInteger numberCount = self.numbers.count;
NSUInteger threadCount = 4;
for (NSUInteger i = 0; i < threadCount; i++) {
    NSUInteger offset = (numberCount / threadCount) * i;
    NSUInteger count = MIN(numberCount - offset, numberCount / threadCount);
    NSRange range = NSMakeRange(offset, count);
    NSArray *subset = [self.numbers subarrayWithRange:range];
    FindMinMaxThread *thread = [[FindMinMaxThread alloc] initWithNumbers:subset];
    [threads addObject:thread];
    [thread start];
}
```

接下来我们可以观察各线程的 `isFinished` 属性，以检测所有新派生的线程是否已完成，然后再评估结果。不过我们把这个练习留给感兴趣的读者。要点在于：无论使用 `pthread` 还是 `NSThread` API，直接与线程打交道都相对笨拙，不太符合我们的编程心智模型。

直接使用线程可能带来的一个问题是：若你的代码与底层框架代码各自派生自己的线程，活跃线程数量会呈指数增长。这在大型项目中其实相当常见。例如，若你为利用八个 CPU 核心而创建八个线程，而这些线程所调用的框架代码又做了同样的事（因为它并不知道你已经创建了线程），很快就会有几十甚至上百个线程。涉及的每一部分代码本身都行为负责；然而最终结果却成了问题。线程并非免费。每个线程都会占用内存与内核资源。

接下来，我们将讨论两种基于队列的并发 API：Grand Central Dispatch 与 operation queue。它们通过集中管理一个大家协作使用的[线程池](http://en.wikipedia.org/wiki/Thread_pool_pattern)来缓解这一问题。

### Grand Central Dispatch

Grand Central Dispatch（GCD）在 OS X 10.6 与 iOS 4 中引入，目的是让开发者更容易利用消费设备中日益增多的 CPU 核心。我们将在[关于底层并发 API 的文章](https://www.objc.io/issues/2-concurrency/low-level-concurrency-apis/)中更详细地讨论 GCD。

使用 GCD 时，你不再直接与线程交互。相反，你把代码块加入队列，由 GCD 在幕后管理一个[线程池](http://en.wikipedia.org/wiki/Thread_pool_pattern)。GCD 决定你的代码块将在哪条具体线程上执行，并根据可用系统资源管理这些线程。这缓解了创建过多线程的问题，因为线程现在由中央管理，并对应用开发者做了抽象。

GCD 带来的另一重要变化是：作为开发者，你以队列而非线程的方式思考工作项。这种新的并发心智模型更易上手。

GCD 暴露了五个不同的队列：运行在主线程上的主队列、三个不同优先级的后台队列，以及一个优先级更低、且受 I/O 节流的后台队列。此外，你可以创建自定义队列，可以是串行队列或并发队列。尽管自定义队列是强大的抽象，你调度到其上的所有 block 最终都会下沉到系统某个全局队列及其线程池中。

![](https://www.objc.io/images/issue-2/gcd-queues@2x_82965db.png)

乍看之下，利用多个不同优先级的队列似乎相当直观。然而，我们强烈建议你几乎在所有情况下都使用默认优先级队列。把任务调度到不同优先级的队列上，若这些任务访问共享资源，很快就会导致意外行为。最严重时甚至会使整个程序陷入停滞，因为某些低优先级任务阻塞了高优先级任务的执行。你可以在[下文](#priority-inversion)阅读更多关于这一现象（称为优先级反转）的内容。

尽管 GCD 是底层的 C API，使用起来相当直观。这很容易让人忘记：在把 block 派发到 GCD 队列时，并发编程的所有注意事项与陷阱依然适用。请务必阅读下文关于[并发编程的挑战](#challenges-of-concurrent-programming)的内容，以了解潜在问题。此外，本期还有一篇出色的 [GCD API 导览](https://www.objc.io/issues/2-concurrency/low-level-concurrency-apis/)，包含许多深入解释与宝贵提示。

### Operation Queue

Operation queue 是 Cocoa 对 GCD 所暴露的队列模型的抽象。虽然 GCD 提供更多底层控制，operation queue 在其之上实现了若干便利特性，这往往使它成为应用开发者最佳且最安全的选择。

`NSOperationQueue` 类有两种不同类型的队列：主队列与自定义队列。主队列运行在主线程上，自定义队列在后台处理。无论哪种情况，这些队列所处理的任务都表示为 `NSOperation` 的子类。

你可以通过两种方式定义自己的 operation：覆盖 `main`，或覆盖 `start`。前者非常简单，但灵活性较低。作为回报，像 `isExecuting` 和 `isFinished` 这样的状态属性会为你管理：只需假定当 `main` 返回时 operation 即已完成。

```
@implementation YourOperation
    - (void)main
    {
        // do your work here ...
    } 
@end
```

若你想要更多控制，或许还想在 operation 内执行异步任务，可以覆盖 `start`：

```
@implementation YourOperation
    - (void)start
    {
        self.isExecuting = YES;
        self.isFinished = NO;
        // start your work, which calls finished once it's done ...
    }
    
    - (void)finished
    {
        self.isExecuting = NO;
        self.isFinished = YES;
    }
@end
```

注意在这种情况下，你必须手动管理 operation 的状态。为使 operation queue 能够感知此类变化，状态属性必须以 KVO 兼容的方式实现。因此，若你不是通过默认访问器方法设置它们，请确保发送正确的 KVO 消息。

为了利用 operation queue 提供的取消功能，对于运行时间较长的 operation，你应定期检查 `isCancelled` 属性：

```
- (void)main
{
    while (notDone && !self.isCancelled) {
        // do your processing
    }
}
```

定义好 operation 类之后，将 operation 加入队列非常容易：

```
NSOperationQueue *queue = [[NSOperationQueue alloc] init];
YourOperation *operation = [[YourOperation alloc] init];
[queue  addOperation:operation];
```

此外，你也可以把 block 加入 operation queue。这在例如想把一次性任务调度到主队列时很方便：

```
[[NSOperationQueue mainQueue] addOperationWithBlock:^{
    // do something...
}];
```

虽然这是一种非常便捷的把工作调度到队列的方式，定义自己的 NSOperation 子类在调试时会非常有帮助。若你覆盖了 operation 的 `description` 方法，就能轻松识别当前调度在某个队列中的所有 operation。

除了调度 operation 或 block 这些基础功能之外，operation queue 还提供了一些用 GCD 很难正确实现的特性。例如，你可以用 `maxConcurrentOperationCount` 属性轻松控制某个队列中可并发执行的 operation 数量。将其设为 1 即可得到串行队列，这对于隔离目的非常理想。

另一个便利特性是根据优先级对队列中的 operation 排序。这与 GCD 的队列优先级不同。它仅影响调度到同一队列中所有 operation 的执行顺序。若你需要比五个标准优先级更精细的执行顺序控制，可以像这样指定 operation 之间的依赖：

```
[intermediateOperation addDependency:operation1];
[intermediateOperation addDependency:operation2];
[finishedOperation addDependency:intermediateOperation];
```

这段简单的代码保证 `operation1` 与 `operation2` 会在 `intermediateOperation` 之前执行，而后者又会在 `finishedOperation` 之前执行。Operation 依赖是一种非常强大的机制，用于指定定义良好的执行顺序。这让你可以创建诸如 operation 组（保证在依赖它们的 operation 之前执行）之类的结构，或在原本并发的队列中实现串行 operation。

就其抽象本质而言，与直接使用 GCD API 相比，operation queue 会有轻微的性能开销。然而，在几乎所有情况下，这一影响都可以忽略不计，operation queue 仍是首选工具。

### 运行循环

严格来说，运行循环并非像 GCD 或 operation queue 那样的并发机制，因为它们并不能实现任务的并行执行。然而，运行循环与主 dispatch/operation 队列上任务的执行直接相关，并提供了一种异步执行代码的机制。

运行循环可能比 operation queue 或 GCD 更容易使用，因为你不必应对并发的复杂性，却仍能异步地做事。

运行循环总是绑定到某一特定线程。与主线程关联的主运行循环在每个 Cocoa 与 CocoaTouch 应用中都扮演着核心角色，因为它处理 UI 事件、定时器以及其他内核事件。每当你调度定时器、使用 `NSURLConnection`，或调用 `performSelector:withObject:afterDelay:` 时，背后都会用到运行循环来执行这些异步任务。

每当你使用依赖运行循环的方法时，重要的是要记住：运行循环可以在不同模式下运行。每种模式定义了运行循环将响应的一组事件。这是一种巧妙的方式，可在主运行循环中暂时优先处理某些任务而非其他任务。

一个典型例子是 iOS 上的滚动。在滚动时，运行循环不在其默认模式下运行，因此不会响应例如你之前调度的定时器。滚动停止后，运行循环回到默认模式，排队的事件才会被执行。若你希望定时器在滚动期间也能触发，需要以 `NSRunLoopCommonModes` 模式将其加入运行循环。

主线程始终已设置并运行着主运行循环。其他线程默认则没有配置运行循环。你也可以为其他线程设置运行循环，但很少需要这样做。多数时候使用主运行循环要容易得多。若需要做较重的工作而不想在主线程上执行，仍可在代码被主运行循环调用之后，将其派发到另一个队列。Chris 在其关于[常见后台实践](https://www.objc.io/issues/2-concurrency/common-background-practices/)的文章中有一些这一模式的好例子。

若你确实需要在另一线程上设置运行循环，别忘了至少为其添加一个输入源。若运行循环没有配置任何输入源，每次尝试运行它都会立即退出。

## 并发编程的挑战

编写并发程序会遇到许多陷阱。一旦所做之事超出最基础的范畴，就很难看清多个任务并行执行时交互中的所有不同状态。问题可能以非确定性方式出现，这使得调试并发代码更加困难。

有一个关于并发程序意外行为的著名例子：1995 年，NASA 将 Pathfinder 任务送往火星。在我们红色邻星上成功着陆后不久，任务几乎[戛然而止](http://research.microsoft.com/en-us/um/people/mbj/Mars_Pathfinder/Mars_Pathfinder.html)。火星车因不明原因不断重启——它遭遇了一种称为_优先级反转_的现象，即低优先级线程持续阻塞高优先级线程。我们将在下文更详细地探讨这一具体问题。但这个例子应当表明：即使拥有大量资源与工程人才，并发仍可能以多种方式反咬一口。

### 资源共享

许多与并发相关的祸根，根源在于多个线程访问共享资源。资源可以是属性或对象、一般意义上的内存、网络设备、文件等等。你在多个线程之间共享的任何东西都是潜在的冲突点，你必须采取安全措施来防止这类冲突。

为了演示这一问题，我们来看一个简单例子：以一个用作计数器的整数属性作为资源。假设我们有两个并行运行的线程 A 和 B，两者同时试图递增该计数器。问题在于：你在 C 或 Objective-C 中写成的一条语句，对 CPU 而言大多并非单条机器指令。要递增计数器，必须先从内存读取当前值，再加一，最后写回内存。

想象一下，若两个线程同时尝试这样做会发生什么危险。例如，线程 A 与线程 B 都从内存读取计数器的值；假设是 `17`。然后线程 A 将计数器加一并把结果 `18` 写回内存。与此同时，线程 B 也把计数器加一并在线程 A 之后把一个 `18` 写回内存。此时数据已损坏，因为计数器从 `17` 递增了两次之后却仍是 `18`。

![](https://www.objc.io/images/issue-2/race-condition@2x_8b11b31.png)

这一问题称为[竞态条件](http://en.wikipedia.org/wiki/Race_conditions#Software)，只要多个线程访问共享资源，却未确保一个线程完成对资源的操作后另一个才开始访问，就总可能发生。若你写入内存的不只是简单整数，而是更复杂的结构，甚至可能出现第二个线程在你写入过程中尝试读取该内存，从而看到一半新、一半旧或未初始化的数据。为防止这种情况，多个线程需要以互斥方式访问共享资源。

实际上，情况比这更复杂，因为现代 CPU 会为优化目的改变对内存的读写顺序（[乱序执行](http://en.wikipedia.org/wiki/Out-of-order_execution)）。

### 互斥

[互斥](http://en.wikipedia.org/wiki/Mutex)访问意味着同一时刻只有一个线程能访问某一资源。为确保这一点，每个想访问资源的线程首先需要获取其上的[_mutex_ 锁](http://en.wikipedia.org/wiki/Lock_%28computer_science%29)。操作完成后释放该锁，以便其他线程有机会访问。

![](https://www.objc.io/images/issue-2/locking@2x_f425450.png)

除了确保互斥访问外，锁还必须处理乱序执行带来的问题。若你不能依赖 CPU 按程序指令定义的顺序访问内存，仅保证互斥访问是不够的。为规避 CPU 优化策略的这一副作用，会使用[内存屏障](http://en.wikipedia.org/wiki/Memory_barrier)。设置内存屏障可确保不会跨越屏障发生乱序执行。

当然，mutex 锁本身的实现也必须没有竞态条件。这并非易事，在现代 CPU 上需要使用特殊指令。你可以在 Daniel 的[底层并发技术](https://www.objc.io/issues/2-concurrency/low-level-concurrency-apis/)一文中阅读更多关于原子操作的内容。

Objective-C 属性以将属性声明为 atomic 的形式提供语言级的加锁支持。事实上，属性默认甚至就是 atomic 的。将属性声明为 atomic 会在每次访问该属性时隐式加锁/解锁。或许会有人想把所有属性都声明为 atomic，以防万一。然而，加锁是有代价的。

获取资源上的锁总是伴随着性能开销。获取与释放锁必须没有竞态条件，这在多核系统上并非易事。而在获取锁时，线程可能因其他线程已持有该锁而不得不等待。此时该线程会休眠，并需在另一线程放弃锁时得到通知。所有这些操作都昂贵且复杂。

锁有不同种类。有些锁在没有锁争用时非常廉价，但在争用下表现不佳。另一些锁基础开销更大，但在争用下退化得更好（[锁争用](http://en.wikipedia.org/wiki/Lock_%28computer_science%29#Granularity)指一个或多个线程试图获取已被占用的锁的情况）。

这里需要权衡：获取与释放锁是有代价的（锁开销）。因此你要确保自己不会不断进入与退出[临界区](http://en.wikipedia.org/wiki/Critical_section)（即获取与释放锁）。与此同时，若你对过大范围的代码持有锁，就有锁争用的风险——其他线程常常因等待获取锁而无法工作。这并非容易解决的任务。

常见的情况是：本应并发运行的代码，由于共享资源锁的设置方式，实际上同一时刻只有一个线程在活动。往往很难预测你的代码将如何被调度到多个核心上。你可以使用 Instruments 的 [CPU strategy view](http://developer.apple.com/library/mac/#documentation/DeveloperTools/Conceptual/InstrumentsUserGuide/AnalysingCPUUsageinYourOSXApp/AnalysingCPUUsageinYourOSXApp.html) 来更好地了解是否在高效利用可用的 CPU 核心。

### 死锁

Mutex 锁解决了竞态条件问题，但不幸的是，它们同时也引入了新问题（[以及其他问题](http://en.wikipedia.org/wiki/Lock_%28computer_science%29#The_problems_with_locks)）：[死锁](http://en.wikipedia.org/wiki/Deadlock)。当多个线程彼此等待对方完成而卡住时，就会发生死锁。

![](https://www.objc.io/images/issue-2/dead-lock@2x_b45f0ac.png)

考虑下面这段交换两个变量值的示例代码：

```
void swap(A, B)
{
    lock(lockA);
    lock(lockB);
    int a = A;
    int b = B;
    A = b;
    B = a;
    unlock(lockB);
    unlock(lockA);
}
```

多数时候这运行良好。但若碰巧两个线程同时以相反的变量调用它

```
swap(X, Y); // thread 1
swap(Y, X); // thread 2
```

我们就会陷入死锁。线程 1 获取了 X 上的锁，线程 2 获取了 Y 上的锁。现在它们都在等待对方的锁，却永远无法获取。

同样，你在线程之间共享的资源越多、获取的锁越多，陷入死锁的风险就越大。这是又一个理由，让事情尽可能简单，并在线程之间尽可能少地共享资源。也请务必阅读[底层并发 API](https://www.objc.io/issues/2-concurrency/low-level-concurrency-apis/)一文中关于[以异步方式做事](https://www.objc.io/issues/2-concurrency/low-level-concurrency-apis/#async)的章节。

### 饥饿

正当你以为要考虑的问题已经够多时，又有新问题出现。对共享资源加锁可能导致[读者-写者问题](http://en.wikipedia.org/wiki/Readers-writers_problem)。在许多情况下，将资源的读访问限制为同一时刻仅一次是浪费的。因此，只要资源上没有写锁，就允许获取读锁。在这种情况下，等待获取写锁的线程可能因期间不断出现更多读锁而挨饿。

为解决这一问题，需要比简单读写锁更聪明的方案，例如给予[写者优先](http://en.wikipedia.org/wiki/Readers–writer_lock)，或使用[读-复制-更新](http://en.wikipedia.org/wiki/Read-copy-update)算法。Daniel 在其[底层并发技术](https://www.objc.io/issues/2-concurrency/low-level-concurrency-apis/#multiple-readers-single-writer)一文中展示了如何用 GCD 实现不受写者饥饿影响的多读者/单写者模式。

### 优先级反转

我们以 NASA Pathfinder 火星车遭受并发问题为例开启本节。现在我们将更仔细地看看 Pathfinder 为何几乎失败，以及你的应用为何可能遭受同一问题——称为[优先级反转](http://en.wikipedia.org/wiki/Priority_inversion)。

优先级反转描述的是这样一种状况：较低优先级的任务阻塞了较高优先级任务的执行，从而实际上反转了任务优先级。由于 GCD 暴露了不同优先级的后台队列，包括一个甚至受 I/O 节流的队列，了解这种可能性是有益的。

当高优先级与低优先级任务共享同一资源时，就可能出现该问题。低优先级任务获取共享资源的锁后，本应迅速完成以释放锁，让高优先级任务能无显著延迟地执行。由于高优先级任务在低优先级任务持有锁期间被阻塞无法运行，中等优先级任务就有机会运行并抢占低优先级任务，因为中等优先级任务此时在所有可运行任务中优先级最高。此刻，中等优先级任务阻碍了低优先级任务释放其锁，从而实际上相对于仍在等待的高优先级任务获得了优先级。

![](https://www.objc.io/images/issue-2/priority-inversion@2x_72e6760.png)

在你自己的代码中，事情可能不像火星车重启那样戏剧性，因为优先级反转经常以较轻微的方式发生。

总体而言，不要使用不同的优先级。你往往最终会变成高优先级代码等待低优先级代码完成。使用 GCD 时，始终使用默认优先级队列（直接使用，或作为目标队列）。若使用不同优先级，十有八九反而会让事情更糟。

由此得到的教训是：使用多个不同优先级的队列在纸面上听起来不错，但它给并发程序增加了更多复杂性与不可预测性。若你曾遇到奇怪问题——高优先级任务似乎无缘无故卡住——或许你会想起本文以及那个连 NASA 工程师都曾遭遇的问题：优先级反转。

## 结论

我们希望已展示出并发编程及其问题的复杂性，无论 API 看起来多么直观。最终行为很快就会变得难以看清，调试这类问题往往非常困难。

另一方面，并发是利用现代多核 CPU 计算能力的强大工具。关键在于保持并发模型尽可能简单，从而限制必要的加锁量。

我们推荐的一个安全模式是：在主线程上取出你要处理的数据，然后用 operation queue 在后台做实际工作，最后再回到主线程交付后台工作的结果。这样，你无需自己做任何加锁，大大降低了出错机会。

---
