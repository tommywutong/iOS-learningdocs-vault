---
title: 底层并发 API
source: objc.io
source_key: objcio
source_url: 'https://www.objc.io/issues/2-concurrency/low-level-concurrency-apis'
original_language: en
published: ''
status: frozen
license: 未声明（页面无版权声明，文章版权归各作者）→ 仅私有归档
archived_at: 2026-07-27
content_hash: 'sha256:ced18357d40a2481'
translated: true
---

> 原文：[Low-Level Concurrency APIs](https://www.objc.io/issues/2-concurrency/low-level-concurrency-apis)　·　objc.io

本文将讨论 iOS 与 OS X 上都可用的一些底层 API。除了 `dispatch_once` 之外，我们一般不鼓励使用其中任何内容。

但我们想展示底层有哪些可用的东西。这些底层 API 提供了极大的灵活性，而伴随灵活性而来的是大量复杂性与责任。我们在[关于常见后台实践的文章](https://www.objc.io/issues/2-concurrency/common-background-practices/)中提到的更高层 API 与模式，能让你专注于手头的任务，并省去许多麻烦。而且一般而言，除非你能投入时间与精力去调整和调试使用底层 API 的代码，否则高层 API 会提供更好的性能。

不过，了解软件栈更下层如何工作是有益的。我们希望本文能让你更好地理解这个平台，同时让你更加欣赏高层 API。

首先，我们将逐一介绍构成 _Grand Central Dispatch_ 的大部分部件。它已存在多年，Apple 持续向其添加内容并改进它。Apple 已将其开源，这意味着它也可用于其他平台。最后，我们将看看[原子操作](#atomic_operations)——又一组底层构建块。

关于并发编程有史以来写得最好的书大概是 _M. Ben-Ari_ 的《Principles of Concurrent Programming》，[ISBN 0-13-701078-8](https://en.wikipedia.org/wiki/Special:BookSources/0-13-701078-8)。若你在做任何与并发编程相关的事，你需要读这本书。它已有三十多年历史，至今仍无人能及。其简洁的文笔、出色的示例与练习，带你走过并发编程的基本构建块。它已绝版，但仍有一些副本在流通。有一个新版本叫《Principles of Concurrent and Distributed Programming》，[ISBN 0-321-31283-X](https://en.wikipedia.org/wiki/Special:BookSources/0-321-31283-X)，似乎涵盖了许多相同内容，但我自己尚未读过。

## 从前有一次……

GCD 中大概使用最广、也误用最多的特性是 `dispatch_once`。正确使用时，看起来会像这样：

```
+ (UIColor *)boringColor;
{
    static UIColor *color;
    static dispatch_once_t onceToken;
    dispatch_once(&onceToken, ^{
        color = [UIColor colorWithRed:0.380f green:0.376f blue:0.376f alpha:1.000f];
    });
    return color;
}
```

该 block 只会运行一次。而在后续调用中，检查非常高效。你可以用它初始化诸如单例之类的全局数据。注意使用 `dispatch_once_t` 会使测试变得非常困难——单例与测试并不合拍。

确保 `onceToken` 声明为 `static` 或具有全局作用域。其他任何做法都会导致未定义行为。换言之：**不要**把 `dispatch_once_t` 作为成员变量放入对象或类似结构中。

在远古时代（即几年前），人们会使用 `pthread_once`，你再也不应使用它，因为 `dispatch_once` 更易用且更不易出错。

## 延迟 / After

另一个常见伙伴是 `dispatch_after`。它让你能_稍晚一点_再做工作。它很强大，但要注意：你很容易陷入许多麻烦。常见用法如下：

```
- (void)foo
{
    double delayInSeconds = 2.0;
    dispatch_time_t popTime = dispatch_time(DISPATCH_TIME_NOW, (int64_t) (delayInSeconds * NSEC_PER_SEC));
    dispatch_after(popTime, dispatch_get_main_queue(), ^(void){
        [self bar];
    });
}
```

乍看之下这很棒。不过有几个缺点。我们无法（直接）取消提交给 `dispatch_after` 的 block。它会运行。

另一点要注意的是，人们有一种有问题的倾向：用 `dispatch_after` 来规避代码中的时序 bug。某些代码运行得太早，你可能不知道为什么，于是把它放进 `dispatch_after`。现在一切都好了。但几周后它又不工作了，而由于你不清楚代码以何种顺序运行，调试变成噩梦。别这样做。多数时候，把代码放在正确的位置更好。若 `-viewWillAppear` 太早，或许 `-viewDidAppear` 才是正确位置。

通过在自己的代码中创建直接调用（类似于 `-viewDidAppear`）而不是依赖 `dispatch_after`，你能省去许多麻烦。

若你需要在特定时间点运行某事，`dispatch_after` 或许是正确选择。也请务必看看 `NSTimer`。那个 API 稍微麻烦一点，但允许你取消定时器的触发。

## 队列

GCD 的基本构建块之一是队列。下面我们将给出几个如何使用它们的例子。使用队列时，给它们一个好标签会让你受益。调试时，该标签会显示在 Xcode（以及 lldb）中，帮助你理解应用在做什么：

```
- (id)init;
{
    self = [super init];
    if (self != nil) {
        NSString *label = [NSString stringWithFormat:@"%@.isolation.%p", [self class], self];
        self.isolationQueue = dispatch_queue_create([label UTF8String], NULL);
        
        label = [NSString stringWithFormat:@"%@.work.%p", [self class], self];
        self.workQueue = dispatch_queue_create([label UTF8String], NULL);
    }
    return self;
}
```

队列可以是_并发_的或_串行_的。默认是串行的，意味着任一时刻只有一个 block 在运行。隔离队列就是这样工作的，我们稍后会讲到。队列也可以是并发的，允许多个 block 同时运行。

GCD 队列在内部使用线程。GCD 管理这些线程，因此使用 GCD 时你无需自己创建线程。但重要的收获是：GCD 向你——API 用户——呈现的是非常不同的抽象层次。当你用 GCD 做并发工作时，你不以线程思考，而是以队列与工作项（提交到队列的 block）思考。虽然底层仍有线程，GCD 的抽象层次更适合你通常编写代码的方式。

队列与工作项还解决了连续扇出的常见问题：若我们直接使用线程，并想并发地做某事，可能把工作拆成 100 个较小的工作项，然后按可用 CPU 核心数创建线程，假设是八个。我们把工作项发送到这八个线程。在处理这些项时，我们可能作为工作的一部分调用某个函数。编写该函数的人也想使用并发，因此当你调用该函数时也会创建八个线程。现在你有 8 × 8 = 64 个线程，尽管只有八个核心——即任一时刻只有 12% 的线程能实际运行，而另外 88% 什么都不做。使用 GCD 你没有这个问题，GCD 甚至可以在系统关闭核心以省电时调整线程数量。

GCD 创建一个与核心数大致匹配的所谓[线程池](http://en.wikipedia.org/wiki/Thread_pool_pattern)。请记住线程并非免费。每个线程都会占用内存与内核资源。不过有一个问题：若你向 GCD 提交一个 block，而该代码阻塞了线程，此时该线程就不再可用于做其他工作——它被阻塞了。为了继续在队列上处理工作项（block），GCD 必须创建新线程并加入池中。

若你的代码阻塞了许多线程，这可能变得相当成问题。首先，线程消耗资源，而且创建它们也很昂贵。并且需要一些时间。在那段时间里，GCD 无法以全速处理工作项。有不少事情会导致线程阻塞，但最常见的与 I/O 相关，即从文件或网络读/写。正因如此，你不应以阻塞方式在 GCD 队列上做这些事。请查看下方的 [Input / Output 章节](#input_output)，了解如何以与 GCD 良好协作的方式做 I/O。

### 目标队列

你可以为任何自己创建的队列设置**目标队列（target queue）**。这可能非常强大。而且有助于调试。

一个类创建自己的队列而不是使用全局队列，通常被认为是良好风格。这样你可以设置该队列的名称，大大方便调试——Xcode 让你在 Debug Navigator 中看到所有队列的名称，或者若直接使用 `lldb`，`(lldb) thread list` 会打印出队列名称。一旦你大量使用异步内容，这将是非常宝贵的帮助。

使用私有队列也强化了封装。那是你的队列；由你决定如何使用它。

默认情况下，新创建的队列会转发到默认优先级的全局队列。我们稍后会更多讨论优先级。

你可以更改你的队列转发到哪个队列——你可以设置队列的目标队列。这样你可以把多个队列链接在一起。你的类 `Foo` 有一个队列，转发到类 `Bar` 的队列，后者再转发到全局队列。

当你使用队列做隔离时（我们也会讨论），这会非常有用。`Foo` 有一个隔离队列，通过转发到 `Bar` 的隔离队列，它将自动相对于 `Bar` 的隔离队列所保护的资源是线程安全的。

若你希望多个 block 在其上运行，请确保将私有队列设为并发。并注意：若队列的目标队列是串行的（即非并发），它实际上也会变成串行队列。

### 优先级

你通过将自己队列的目标队列设为某个全局队列来更改其优先级。但你应抵制这样做的诱惑。

在多数情况下，更改优先级不会达到你的意图。看似直观的东西实际上是一个非常复杂的问题。你很容易陷入所谓的[优先级反转](http://en.wikipedia.org/wiki/Priority_inversion)。我们[关于并发 API 与陷阱的文章](https://www.objc.io/issues/2-concurrency/concurrency-apis-and-pitfalls/#challenges)对这一问题有更多信息，它几乎让 NASA 的 Pathfinder 火星车变砖。

此外，你需要对 `DISPATCH_QUEUE_PRIORITY_BACKGROUND` 队列特别小心。除非你理解_节流 I/O_ 与 _按 setpriority(2) 的后台状态_ 意味着什么，否则不要使用它。否则系统可能最终让你的应用陷入停滞。它主要用于以不干扰系统其他部分做 I/O 的方式进行 I/O。但若与优先级反转结合，很容易变成危险的鸡尾酒。

## 隔离

隔离队列是 GCD 队列用法中最常见的模式之一。有两种变体。

### 保护资源

多线程编程中最常见的场景是：你有一个同一时刻只允许一个线程访问的资源。

我们[关于并发技术的文章](https://www.objc.io/issues/2-concurrency/concurrency-apis-and-pitfalls/)对并发编程中_资源_意味着什么谈得更多一些。它往往是一块内存或一个对象，同一时刻只能有一个线程访问。

假设我们需要从多个线程（队列）访问一个 `NSMutableDictionary`。我们会这样做：

```
- (void)setCount:(NSUInteger)count forKey:(NSString *)key
{
    key = [key copy];
    dispatch_async(self.isolationQueue, ^(){
        if (count == 0) {
            [self.counts removeObjectForKey:key];
        } else {
            self.counts[key] = @(count);
        }
    });
}

- (NSUInteger)countForKey:(NSString *)key;
{
    __block NSUInteger count;
    dispatch_sync(self.isolationQueue, ^(){
        NSNumber *n = self.counts[key];
        count = [n unsignedIntegerValue];
    });
    return count;
}
```

这样，只有一个线程会访问该 `NSMutableDictionary` 实例。

注意四点：

1. 不要使用这段代码。先阅读关于[多读者、单写者](#multiple-readers-single-writer)以及关于[争用](#contention)的内容。
2. 存储值时我们使用 `async`。这很重要。我们不想也不需要为了_写_完成而阻塞当前线程。读取时我们使用 `sync`，因为我们需要返回结果。
3. 根据方法接口，`-setCount:forKey:` 接受一个 `NSString`，我们会把它传到 `dispatch_async`。调用者可以传入 `NSMutableString`，并在方法返回后、block 执行前修改它。因此我们_必须_复制该字符串以保证方法正确工作。若传入的字符串不可变（即普通 `NSString`），对 `-copy` 的调用基本上是空操作。
4. `isolationQueue` 需要以 `DISPATCH_QUEUE_SERIAL`（或 `0`）的 `dispatch_queue_attr_t` 创建。

### 一个资源、多个读者与一个写者

我们可以改进上面的例子。GCD 有可让多个线程运行的并发队列。只要不同时修改，我们就可以安全地在多个线程上从 `NSMutableDictionary` 读取。当我们需要更改字典时，用_屏障（barrier）_派发该 block。这样的 block 会在所有先前调度的 block 完成后、任何后续 block 运行前运行一次。

我们将这样创建队列：

```
self.isolationQueue = dispatch_queue_create([label UTF8String], DISPATCH_QUEUE_CONCURRENT);
```

然后像这样更改 setter：

```
- (void)setCount:(NSUInteger)count forKey:(NSString *)key
{
    key = [key copy];
    dispatch_barrier_async(self.isolationQueue, ^(){
        if (count == 0) {
            [self.counts removeObjectForKey:key];
        } else {
            self.counts[key] = @(count);
        }
    });
}
```

使用并发队列时，确保所有_屏障_调用都是_async_。若使用 `dispatch_barrier_sync`，你很可能会让自己（或者说：你的代码）陷入死锁。写入_需要_屏障，并且_可以_是 async。

### 关于争用的一点说明

首先，这里有一句警告：本简单例子中我们保护的资源是 `NSMutableDictionary`。这很好地达到了示例目的。但在真实代码中，重要的是把隔离放在正确的复杂度层次上。

若你非常频繁地访问 `NSMutableDictionary`，就会陷入所谓的锁争用。锁争用绝非 GCD 或队列所特有。任何形式的加锁机制都会有同样的问题——不同加锁机制以不同方式表现。

对 `dispatch_async`、`dispatch_sync` 等的所有调用都需要执行某种形式的加锁——确保只有一个线程或特定线程运行给定的 block。GCD 在一定程度上可以避免锁而改用调度，但归根结底问题只是转移了。底层问题依旧：若你有**大量**线程同时击中同一把锁或同一个队列，就会看到性能下降。性能可能严重退化。

你需要在正确的复杂度层次上进行隔离。当你看到性能下降时，这是代码设计问题的明确信号。你需要平衡两种成本。第一种是待在临界区中太久，以致其他线程被阻止进入临界区的成本；第二种是不断进入与离开临界区的成本。在 GCD 的世界里，第一种成本描述的是：若一个 block 在你的隔离队列上运行，它可能潜在地阻止其他代码在该隔离队列上运行。第二种成本描述的是：调用 `dispatch_async` 与 `dispatch_sync` 虽然高度优化，也并非免费。

遗憾的是，什么才是正确的平衡没有通用规则：你需要测量并调整。打开 Instruments，看看你的应用在做什么。

若我们看上面的示例代码，我们的临界代码段只做非常简单的事。这可能好也可能不好，取决于如何使用。

在你自己的代码中，考虑是否最好在更高层次用隔离队列保护。例如，与其让类 `Foo` 有一个隔离队列并由它自己保护对其 `NSMutableDictionary` 的访问，不如让使用 `Foo` 的类 `Bar` 有一个隔离队列，保护对类 `Foo` 的所有使用。换言之：你会更改 `Foo`，使其不再线程安全（没有隔离队列），然后在 `Bar` 内部使用隔离队列，确保任一时刻只有一个线程在使用 `Foo`。

### 走向完全异步

让我们在此稍作岔开。如你上面所见，你可以同步或异步地派发一个 block、一个工作单元。我们在[关于并发 API 与陷阱的文章](https://www.objc.io/issues/2-concurrency/concurrency-apis-and-pitfalls/)中谈到的一个非常常见的问题是[死锁](http://en.wikipedia.org/wiki/Deadlock)。用 GCD 同步派发很容易陷入这一问题。最琐碎的情况是：

```
dispatch_queue_t queueA; // assume we have this
dispatch_sync(queueA, ^(){
    dispatch_sync(queueA, ^(){
        foo();
    });
});
```

一旦到达第二个 `dispatch_sync` 我们就会死锁：我们无法派发到 queueA，因为有人（当前线程）已经在该队列上，且永远不会离开。但还有更微妙的方式：

```
dispatch_queue_t queueA; // assume we have this
dispatch_queue_t queueB; // assume we have this

dispatch_sync(queueA, ^(){
    foo();
});

void foo(void)
{
    dispatch_sync(queueB, ^(){
        bar();
    });
}

void bar(void)
{
    dispatch_sync(queueA, ^(){
        baz();
    });
}
```

每个对 `dispatch_sync()` 的调用单独看起来都没问题，但结合起来就会死锁。

这一切都固有于同步。若我们使用异步派发，例如

```
dispatch_queue_t queueA; // assume we have this
dispatch_async(queueA, ^(){
    dispatch_async(queueA, ^(){
        foo();
    });
});
```

事情就会正常工作。_异步调用不会死锁_。因此，尽可能使用异步调用是非常可取的。与其编写返回值的函数或方法（因而必须是同步的），我们使用异步调用结果 block 的方法。这样我们就不太可能陷入死锁问题。

异步调用的缺点是难以调试。当我们在调试器中停下代码时，没有有意义的回溯可看。

把这两点都记在心里。死锁通常是更难处理的问题。

### 如何编写良好的异步 API

若你在设计供他人使用（甚至供自己使用）的 API，有几条良好实践需要牢记。

正如我们刚提到的，你应优先选择异步 API。当你创建 API 时，可能以你无法控制的方式被调用，而若你的代码可能死锁，它就会死锁。

你应这样编写函数或方法：由函数调用 `dispatch_async()`。不要让调用者去调用它。调用者应能直接调用你的函数或方法。

若你的函数或方法有结果，通过回调处理器异步交付。API 应设计成：你的函数或方法同时接受结果 block 以及交付结果所用的队列。你的函数的调用者不应不得不自己派发到该队列。原因很简单：几乎总是，调用者需要在某个特定队列上，这样代码更易读。而你的函数反正会（应该）调用 `dispatch_async()` 来运行回调处理器，所以它不妨直接在调用者需要的那个队列上做这件事。

若你在编写一个类，让该类的用户设置一个所有回调都将交付到其上的队列，大概是个好选项。你的代码会像这样：

```
- (void)processImage:(UIImage *)image completionHandler:(void(^)(BOOL success))handler;
{
    dispatch_async(self.isolationQueue, ^(void){
        // do actual processing here
        dispatch_async(self.resultQueue, ^(void){
            handler(YES);
        });
    });
}
```

若你以这种方式编写类，就很容易让类协作。若类 A 使用类 B，它会把 B 的回调队列设为自己的隔离队列。

## 迭代执行

若你在做一些数值计算，且手头的问题可以拆成性质相同的更小部分，`dispatch_apply` 会非常有用。

若你有这样的代码

```
for (size_t y = 0; y < height; ++y) {
    for (size_t x = 0; x < width; ++x) {
        // Do something with x and y here
    }
}
```

你或许只需把它改成这样就能量加快

```
dispatch_apply(height, dispatch_get_global_queue(0, 0), ^(size_t y) {
    for (size_t x = 0; x < width; x += 2) {
        // Do something with x and y here
    }
});
```

这效果如何很大程度上取决于你在那个循环内部具体做什么。

block 所做的工作必须是非平凡的，否则开销太大。除非代码受计算带宽限制，否则每个工作单元需要读写的内存能很好地装入缓存大小至关重要。这对性能可能有戏剧性影响。受临界区限制的代码可能根本表现不佳。深入讨论这些问题超出了本文范围。使用 `dispatch_apply` 可能有助于性能，但性能优化本身就是一个复杂主题。Wikipedia 有一篇关于 [Memory-bound function](https://en.wikipedia.org/wiki/Memory_bound) 的文章。内存访问速度在 L2、L3 与主内存之间变化巨大。当你的数据访问模式不适合缓存大小时，看到 10 倍的性能下降并不少见。

## 组

相当常见的是，你会发现自己把异步 block 链接在一起以执行给定任务。其中一些甚至可能并行运行。现在，若你想在该任务完成——即所有 block 都完成后——运行一些代码，「组（groups）」就是正确的工具。示例如下：

```
dispatch_group_t group = dispatch_group_create();

dispatch_queue_t queue = dispatch_get_global_queue(0, 0);
dispatch_group_async(group, queue, ^(){
    // Do something that takes a while
    [self doSomeFoo];
    dispatch_group_async(group, dispatch_get_main_queue(), ^(){
        self.foo = 42;
    });
});
dispatch_group_async(group, queue, ^(){
    // Do something else that takes a while
    [self doSomeBar];
    dispatch_group_async(group, dispatch_get_main_queue(), ^(){
        self.bar = 1;
    });
});

// This block will run once everything above is done:
dispatch_group_notify(group, dispatch_get_main_queue(), ^(){
    NSLog(@"foo: %d", self.foo);
    NSLog(@"bar: %d", self.bar);
});
```

要注意的重要一点是：这一切完全是非阻塞的。在任何时刻我们都没有告诉当前线程等待某事完成。恰恰相反，我们只是在入队多个 block。由于这种代码模式不阻塞，它不会导致死锁。

还要注意在这个小而简单的例子中，我们如何在不同队列之间切换。

### 将 dispatch_group_t 与现有 API 一起使用

一旦你把组加入工具带，就会好奇为何大多数异步 API 不把 `dispatch_group_t` 作为可选参数。但无需绝望：很容易自己加上，尽管你必须更加小心以确保代码是_平衡的_。

例如，我们可以像这样把它加到 Core Data 的 `-performBlock:` API：

```
- (void)withGroup:(dispatch_group_t)group performBlock:(dispatch_block_t)block
{
    if (group == NULL) {
        [self performBlock:block];
    } else {
        dispatch_group_enter(group);
        [self performBlock:^(){
            block();
            dispatch_group_leave(group);
        }];
    }
}
```

这让我们能使用 `dispatch_group_notify`，在一组 Core Data 操作（可能与其他 block 组合）完成时运行一个 block。

我们显然也可以对 `NSURLConnection` 做同样的事：

```
+ (void)withGroup:(dispatch_group_t)group 
        sendAsynchronousRequest:(NSURLRequest *)request 
        queue:(NSOperationQueue *)queue 
        completionHandler:(void (^)(NSURLResponse*, NSData*, NSError*))handler
{
    if (group == NULL) {
        [self sendAsynchronousRequest:request 
                                queue:queue 
                    completionHandler:handler];
    } else {
        dispatch_group_enter(group);
        [self sendAsynchronousRequest:request 
                                queue:queue 
                    completionHandler:^(NSURLResponse *response, NSData *data, NSError *error){
            handler(response, data, error);
            dispatch_group_leave(group);
        }];
    }
}
```

为使这能工作，你需要确保

- `dispatch_group_enter()` 保证在 `dispatch_group_leave()` 之前运行
- 对 `dispatch_group_enter()` 与 `dispatch_group_leave()` 的调用始终平衡（即使发生错误时也是）

## Sources

GCD 较少为人知的特性之一是事件源 `dispatch_source_t`。

就像 GCD 的大部分内容一样，这是相当底层的东西。当你需要它时，它可能极其有用。其中一些极其深奥，我们只会触及其中几种用途。其中许多在 iOS 上并不十分有用——你无法启动进程（因此没必要监视它们），也无法在应用包外写入（因此无需监视文件），等等。

GCD sources 以极其节省资源的方式实现。

### 监视进程

若某个进程正在运行，而你想知道它何时退出，GCD 已为你准备好。你也可以用它检查该进程何时 fork（即派生子进程），或信号是否被投递给该进程（例如 `SIGTERM`）。

```
@import AppKit;
// ...
NSArray *array = [NSRunningApplication 
  runningApplicationsWithBundleIdentifier:@"com.apple.mail"];
if (array == nil || [array count] == 0) {
    return;
}
pid_t const pid = [[array firstObject] processIdentifier];
self.source = dispatch_source_create(DISPATCH_SOURCE_TYPE_PROC, pid, 
  DISPATCH_PROC_EXIT, DISPATCH_TARGET_QUEUE_DEFAULT);
dispatch_source_set_event_handler(self.source, ^(){
    NSLog(@"Mail quit.");
    // If you would like continue watching for the app to quit,
    // you should cancel this source with dispatch_source_cancel and create new one
    // as with next run app will have another process identifier.
});
dispatch_resume(self.source);
```

当 Mail.app 退出时，这会打印 **Mail quit.**。

注意：在任何事件被投递给事件处理器之前，你必须调用 `dispatch_resume()`。

### 监视文件

可能性似乎近乎无穷。你可以直接监视文件的更改，更改发生时会调用 source 的事件处理器。

你也可以用它监视目录，即创建一个_监视文件夹_：

```
NSURL *directoryURL; // assume this is set to a directory
int const fd = open([[directoryURL path] fileSystemRepresentation], O_EVTONLY);
if (fd < 0) {
    char buffer[80];
    strerror_r(errno, buffer, sizeof(buffer));
    NSLog(@"Unable to open \"%@\": %s (%d)", [directoryURL path], buffer, errno);
    return;
}
dispatch_source_t source = dispatch_source_create(DISPATCH_SOURCE_TYPE_VNODE, fd, 
  DISPATCH_VNODE_WRITE | DISPATCH_VNODE_DELETE, DISPATCH_TARGET_QUEUE_DEFAULT);
dispatch_source_set_event_handler(source, ^(){
    unsigned long const data = dispatch_source_get_data(source);
    if (data & DISPATCH_VNODE_WRITE) {
        NSLog(@"The directory changed.");
    }
    if (data & DISPATCH_VNODE_DELETE) {
        NSLog(@"The directory has been deleted.");
    }
});
dispatch_source_set_cancel_handler(source, ^(){
    close(fd);
});
self.source = source;
dispatch_resume(self.source);
```

你大概应始终添加 `DISPATCH_VNODE_DELETE` 来检查文件或目录是否已被删除——然后停止监视它。

### 定时器

多数情况下，`NSTimer` 是定时器事件的首选去处。GCD 的版本更底层。它给你更多控制——请谨慎使用。

极其重要的一点是：为 GCD 定时器指定过低的_leeway_ 值会干扰操作系统节省电力的尝试。若不必要地指定过低的 leeway 值，你会消耗更多电池。

这里我们设置一个每 5 秒触发一次、允许 1/10 秒 leeway 的定时器：

```
dispatch_source_t source = dispatch_source_create(DISPATCH_SOURCE_TYPE_TIMER, 
  0, 0, DISPATCH_TARGET_QUEUE_DEFAULT);
dispatch_source_set_event_handler(source, ^(){
    NSLog(@"Time flies.");
});
dispatch_source_set_timer(source, DISPATCH_TIME_NOW, 5ull * NSEC_PER_SEC, 
  100ull * NSEC_PER_MSEC);
self.source = source;
dispatch_resume(self.source);
```

### 取消

所有 sources 都允许你添加_取消处理器_。这对于清理你为事件源创建的任何资源很有用，例如关闭文件描述符。GCD 保证在调用取消处理器之前，对事件处理器的所有调用都已完成。

参见上方[监视文件夹示例](#watching_files)中对 `dispatch_source_set_cancel_handler()` 的使用。

## Input / Output

编写在做大量 I/O 时表现良好的代码极其棘手。GCD 有一些技巧来帮助。不过多深入细节，我们将简要触及这些问题是什么，以及 GCD 如何应对它们。

传统上，当你从网络套接字读取数据时，要么必须做阻塞读（即停住一个线程直到数据可用），要么必须反复轮询。两种方法都浪费且无法扩展。然而，`kqueue` 通过在数据可用时投递事件解决了轮询问题，GCD 使用相同方法，尽管更优雅。向套接字写数据时，存在相同问题：你要么必须执行阻塞写，要么等待套接字能够接受数据。

执行 I/O 时的第二个问题是数据以小块到达；从网络读取时，由于 MTU——[最大传输单元](https://en.wikipedia.org/wiki/Maximum_transmission_unit)——块大小通常约为 1.5k 字节。不过这可以是任意大小。一旦这些数据到达，你往往对跨越多块的数据感兴趣，传统上你会把数据拼接到一个更大的缓冲区中再处理。假设（刻意的例子）你收到这八块：

```
0: HTTP/1.1 200 OK\r\nDate: Mon, 23 May 2005 22:38
1: :34 GMT\r\nServer: Apache/1.3.3.7 (Unix) (Red-H
2: at/Linux)\r\nLast-Modified: Wed, 08 Jan 2003 23
3: :11:55 GMT\r\nEtag: "3f80f-1b6-3e1cb03b"\r\nCon
4: tent-Type: text/html; charset=UTF-8\r\nContent-
5: Length: 131\r\nConnection: close\r\n\r\n<html>\r
6: \n<head>\r\n  <title>An Example Page</title>\r\n
7: </head>\r\n<body>\r\n  Hello World, this is a ve
```

若你在寻找 HTTP 头，把所有数据块拼接到更大的缓冲区再扫描 `\r\n\r\n` 会简单得多。但这样做你会大量复制数据。许多_旧_ C API 的另一个问题是缓冲区没有所有权，因此函数不得不把数据复制到自己的缓冲区中——又一次复制。复制数据看似琐碎，但当你做大量 I/O 时，这些复制会出现在你的分析工具（Instruments）中。即便你每个内存区域只复制一次，你也会产生双倍的内存带宽，并烧穿双倍的内存缓存。

### GCD 与缓冲区

更直观的部分是关于数据缓冲区。GCD 有一个 `dispatch_data_t` 类型，在某种程度上类似于 `NSData` 对 Objective-C 所做的事。不过它还能做其他事情，且更通用。

注意 `dispatch_data_t` 可以被 retain 与 release，且 `dispatch_data_t` 对象_拥有_它所持有的缓冲区。

这看似琐碎，但我们必须记住 GCD 是纯 C API，无法使用 Objective-C。传统方式是让缓冲区要么由栈支持，要么由 `malloc`'d 的内存区域支持——这些没有所有权。

`dispatch_data_t` 一个相对独特的属性是它可以由不相交的内存区域支持。这解决了我们刚提到的拼接问题。当你用以下方式拼接两个数据对象时

```
dispatch_data_t a; // Assume this hold some valid data
dispatch_data_t b; // Assume this hold some valid data
dispatch_data_t c = dispatch_data_create_concat(a, b);
```

数据对象 `c` _不会_把 `a` 和 `b` 复制到单个更大的内存区域。相反，它只会 retain `a` 和 `b`。然后你可以用 `dispatch_data_apply` 遍历 `c` 所表示的内存区域：

```
dispatch_data_apply(c, ^bool(dispatch_data_t region, size_t offset, const void *buffer, size_t size) {
    fprintf(stderr, "region with offset %zu, size %zu\n", offset, size);
    return true;
});
```

类似地，你可以用 `dispatch_data_create_subrange` 创建子范围，不会做任何复制。

### 读与写

在其核心，_Dispatch I/O_ 关乎所谓的_通道（channels）_。Dispatch I/O 通道提供了一种从文件描述符读与写的不同方式。创建此类通道最基本的方式是调用

```
dispatch_io_t dispatch_io_create(dispatch_io_type_t type, dispatch_fd_t fd, 
  dispatch_queue_t queue, void (^cleanup_handler)(int error));
```

这返回所创建的通道，然后该通道_拥有_文件描述符。在从中创建通道之后，你不得以任何方式修改该文件描述符。

有两种根本不同_类型_的通道：流与随机访问。若你打开磁盘上的文件，可以用它创建随机访问通道（因为此类文件描述符是可 `seek` 的）。若你打开套接字，可以创建流通道。

若你想为文件创建通道，最好使用 `dispatch_io_create_with_path`，它接受路径，并让 GCD 打开文件。这是有益的，因为 GCD 可以推迟打开文件——从而限制同时打开的文件数量。

类似于普通的 `read(2)`、`write(2)` 与 `close(2)`，GCD 提供 `dispatch_io_read`、`dispatch_io_write` 与 `dispatch_io_close`。读写通过回调 block 完成，每当数据被读或写时就会调用。这有效地实现了非阻塞、完全异步的 I/O。

我们无法在此详述所有细节，但这里有一个设置 TCP 服务器的例子：

首先我们创建监听套接字，并为传入连接设置事件源：

```
_isolation = dispatch_queue_create([[self description] UTF8String], NULL);
_nativeSocket = socket(PF_INET6, SOCK_STREAM, IPPROTO_TCP);
struct sockaddr_in sin = {};
sin.sin_len = sizeof(sin);
sin.sin_family = AF_INET6;
sin.sin_port = htons(port);
sin.sin_addr.s_addr= INADDR_ANY;
int err = bind(result.nativeSocket, (struct sockaddr *) &sin, sizeof(sin));
NSCAssert(0 <= err, @"");

_eventSource = dispatch_source_create(DISPATCH_SOURCE_TYPE_READ, _nativeSocket, 0, _isolation);
dispatch_source_set_event_handler(result.eventSource, ^{
    acceptConnection(_nativeSocket);
});
```

接受连接时，我们创建 I/O 通道：

```
typedef union socketAddress {
    struct sockaddr sa;
    struct sockaddr_in sin;
    struct sockaddr_in6 sin6;
} socketAddressUnion;

socketAddressUnion rsa; // remote socket address
socklen_t len = sizeof(rsa);
int native = accept(nativeSocket, &rsa.sa, &len);
if (native == -1) {
    // Error. Ignore.
    return nil;
}

_remoteAddress = rsa;
_isolation = dispatch_queue_create([[self description] UTF8String], NULL);
_channel = dispatch_io_create(DISPATCH_IO_STREAM, native, _isolation, ^(int error) {
    NSLog(@"An error occured while listening on socket: %d", error);
});

//dispatch_io_set_high_water(_channel, 8 * 1024);
dispatch_io_set_low_water(_channel, 1);
dispatch_io_set_interval(_channel, NSEC_PER_MSEC * 10, DISPATCH_IO_STRICT_INTERVAL);

socketAddressUnion lsa; // remote socket address
socklen_t len = sizeof(rsa);
getsockname(native, &lsa.sa, &len);
_localAddress = lsa;
```

若我们想设置 `SO_KEEPALIVE`（若使用 HTTP 级别的 keep-alive），需要在调用 `dispatch_io_create` 之前这样做。

创建了 `dispatch_io` 通道后，我们可以设置读处理器：

```
dispatch_io_read(_channel, 0, SIZE_MAX, _isolation, ^(bool done, dispatch_data_t data, int error){
    if (data != NULL) {
        if (_data == NULL) {
            _data = data;
        } else {
            _data = dispatch_data_create_concat(_data, data);
        }
        [self processData];
    }
});
```

若你只想从文件读或向文件写，GCD 提供两个便利包装：`dispatch_read` 与 `dispatch_write`。你向 `dispatch_read` 传入文件路径以及为每个读到的数据块调用的 block。类似地，`dispatch_write` 接受文件路径以及要写入的 `dispatch_data_t` 对象。

## 基准测试

在 GCD 的隐秘角落，你会发现一个用于优化代码的整洁小工具：

```
uint64_t dispatch_benchmark(size_t count, void (^block)(void));
```

把这个声明放进你的代码，你就可以测量给定 block 执行所需的平均纳秒数。例如

```
size_t const objectCount = 1000;
uint64_t n = dispatch_benchmark(10000, ^{
    @autoreleasepool {
        id obj = @42;
        NSMutableArray *array = [NSMutableArray array];
        for (size_t i = 0; i < objectCount; ++i) {
            [array addObject:obj];
        }
    }
});
NSLog(@"-[NSMutableArray addObject:] : %llu ns", n);
```

在我的机器上这输出

```
-[NSMutableArray addObject:] : 31803 ns
```

即向 NSMutableArray 添加 1000 个对象需要 31803 ns，或每个对象约 32 ns。

正如 `dispatch_benchmark` 的 [man page](http://opensource.apple.com/source/libdispatch/libdispatch-84.5/man/dispatch_benchmark.3) 所指出的，测量性能并不像看起来那么琐碎。特别是在比较并发代码与非并发代码时，你需要注意所运行硬件特定部件的计算带宽与内存带宽。它会因机器而异变化很大。我们上面提到的争用问题也会影响性能受临界区访问限制的代码。

不要把这放进发布代码。除了这样做相当无意义之外，它也是私有 API。它仅用于调试与性能分析工作。

用以下方式查看 man page

```
curl "http://opensource.apple.com/source/libdispatch/libdispatch-84.5/man/dispatch_benchmark.3?txt" 
  | /usr/bin/groffer --tty -T utf8
```

## 原子操作

头文件 `libkern/OSAtomic.h` 有许多用于更底层多线程编程的强大函数。虽然它是内核头文件的一部分，但意图也用于内核与驱动编程之外。

这些函数更底层，有一些额外事项你需要注意。不过若你注意了，可能会在这里找到一两件否则做不到——或没那么容易做到——的事。若你在做高性能代码和/或实现无锁与无等待算法，它大多会很有意思。

这些函数都总结在 `atomic(3)` man page 中——运行 `man 3 atomic` 获取完整文档。你会看到它谈到内存屏障。请查看 [Wikipedia 关于内存屏障的文章](https://en.wikipedia.org/wiki/Memory_barrier)。若有疑问，你大概需要内存屏障。

### 计数器

有一长串 `OSAtomicIncrement` 与 `OSAtomicDecrement` 函数，允许你以原子方式递增与递减整数值——线程安全且无需加锁（或使用队列）。若你需要从多个线程递增全局计数器以做统计，这些可能有用。若你所做的只是递增全局计数器，无屏障的 `OSAtomicIncrement` 版本就很好，且在没有争用时调用廉价。

类似地，`OSAtomicOr`、`OSAtomicAnd` 与 `OSAtomicXor` 函数可用于执行逻辑运算，`OSAtomicTest` 函数可用于设置或清除位。

### 比较并交换

`OSAtomicCompareAndSwap` 可用于像这样进行无锁惰性初始化：

```
void * sharedBuffer(void)
{
    static void * buffer;
    if (buffer == NULL) {
        void * newBuffer = calloc(1, 1024);
        if (!OSAtomicCompareAndSwapPtrBarrier(NULL, newBuffer, &buffer)) {
            free(newBuffer);
        }
    }
    return buffer;
}
```

若没有缓冲区，我们创建一个，然后若 `buffer` 为 NULL 则原子地写入 `buffer`。在当前线程与其他线程同时设置 `buffer` 的罕见情况下，我们只是释放它。由于比较并交换方法是原子的，这是惰性初始化值的线程安全方式。检查 `NULL` 与设置 `buffer` 是原子完成的。

显然，你也可以用 `dispatch_once()` 做类似的事。

### 原子队列

`OSAtomicEnqueue()` 与 `OSAtomicDequeue()` 让你以线程安全、无锁的方式实现 LIFO 队列（也称为栈）。对有严格延迟要求的代码，这可以是强大的构建块。

还有用于 FIFO 队列的 `OSAtomicFifoEnqueue()` 与 `OSAtomicFifoDequeue()`，但这些只在头文件中有文档——使用时请仔细阅读。

### 自旋锁

最后，`OSAtomic.h` 头文件定义了与自旋锁一起工作的函数：`OSSpinLock`。同样，Wikipedia 有[关于自旋锁的深入信息](https://en.wikipedia.org/wiki/Spinlock)。用 `man 3 spinlock` 查看 `spinlock(3)` man page。简短的故事是：当没有锁争用时，自旋锁非常廉价。

自旋锁在某些情况下可作为性能优化有用。一如既往：先测量，再优化。不要做乐观优化。

这里是 OSSpinLock 的一个例子：

```
@interface MyTableViewCell : UITableViewCell

@property (readonly, nonatomic, copy) NSDictionary *amountAttributes;

@end

@implementation MyTableViewCell
{
    NSDictionary *_amountAttributes;
}

- (NSDictionary *)amountAttributes;
{
    if (_amountAttributes == nil) {
        static __weak NSDictionary *cachedAttributes = nil;
        static OSSpinLock lock = OS_SPINLOCK_INIT;
        OSSpinLockLock(&lock);
        _amountAttributes = cachedAttributes;
        if (_amountAttributes == nil) {
            NSMutableDictionary *attributes = [[self subtitleAttributes] mutableCopy];
            attributes[NSFontAttributeName] = [UIFont fontWithName:@"ComicSans" size:36];
            attributes[NSParagraphStyleAttributeName] = [NSParagraphStyle defaultParagraphStyle];
            _amountAttributes = [attributes copy];
            cachedAttributes = _amountAttributes;
        }
        OSSpinLockUnlock(&lock);
    }
    return _amountAttributes;
}
```

在上面的例子中，大概不值得这么麻烦，但它展示了概念。我们使用 ARC 的 `__weak` 来确保一旦所有 `MyTableViewCell` 实例消失，`amountAttributes` 就会被 `dealloc`。然而我们仍能在所有实例间共享该字典的单个实例。

这表现良好的原因是我们不太可能命中方法的最内层部分。这相当深奥——除非有真正的需要，否则不要在你的 App 中使用它。

---
