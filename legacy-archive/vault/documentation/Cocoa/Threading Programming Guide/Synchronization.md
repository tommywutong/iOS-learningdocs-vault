---
title: 多线程编程指南
apple_id: 10000057i
resource_type: Guide
platform: watchOS|tvOS|iOS|macOS
topic: Performance
technology: null
published: '2014-07-15'
source_url: https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/Multithreading/ThreadSafety/ThreadSafety.html
archived_at: '2026-07-15T07:16:47.600610Z'
---
> 导航：[总目录](../../../README.md) · [文档](../../../_indexes/documentation.md) · [多线程编程指南](Introduction.md)


[下一页](Thread%20Safety%20Summary.md)[上一页](Run%20Loops.md)

# 同步

应用程序中存在多个线程时，就会带来与从多个执行线程安全访问资源有关的潜在问题。两个线程修改同一个资源时，可能会以意想不到的方式相互干扰。例如，一个线程可能会覆盖另一个线程所做的更改，或者使应用程序进入一种未知且可能无效的状态。如果幸运的话，被破坏的资源可能只会导致明显的性能问题或崩溃，这类问题相对容易追查和修复。但如果不走运，这种破坏可能会导致隐蔽的错误，这些错误要到很久以后才会显现出来，甚至可能需要对你底层的编码假设进行大规模的返工。

说到线程安全，好的设计是你所拥有的最好的保护手段。避免共享资源、尽量减少线程之间的交互，能降低这些线程相互干扰的可能性。不过，完全没有干扰的设计并非总是可行的。在你的线程必须交互的情况下，你需要使用同步工具来确保它们交互时是安全的。

OS X 和 iOS 提供了大量供你使用的同步工具，从提供互斥访问的工具，到能在你的应用程序中正确排列事件顺序的工具，应有尽有。以下各节将介绍这些工具，以及如何在代码中使用它们来实现对程序资源的安全访问。

为了防止不同线程意外地更改数据，你既可以将应用程序设计成不存在同步问题，也可以使用同步工具。虽然完全避免同步问题是更可取的做法，但这并不总是可行的。以下各节介绍了可供你使用的同步工具的基本类别。

原子操作是一种作用于简单数据类型的简单同步形式。原子操作的优点在于它们不会阻塞与之竞争的线程。对于诸如递增计数器变量这类简单操作而言，这样做可以带来比加锁好得多的性能。

OS X 和 iOS 包含了大量对 32 位和 64 位值执行基本数学和逻辑运算的操作。这些操作中包括比较并交换（compare-and-swap）、测试并置位（test-and-set）以及测试并清零（test-and-clear）操作的原子版本。有关支持的原子操作列表，请参阅 `/usr/include/libkern/OSAtomic.h` 头文件，或参阅 [atomic](https://developer.apple.com/library/archive/documentation/System/Conceptual/ManPages_iPhoneOS/man3/atomic.3.html#//apple_ref/doc/man/3/atomic) man 手册页。

为了获得最佳性能，编译器常常会对汇编级指令重新排序，以尽量让处理器的指令流水线保持满载。作为这种优化的一部分，编译器可能会对访问主内存的指令重新排序，只要它认为这样做不会产生错误的数据。遗憾的是，编译器并非总能检测出所有依赖内存的操作。如果表面上看起来彼此独立的变量实际上会相互影响，编译器的优化就可能以错误的顺序更新这些变量，从而产生潜在的错误结果。

内存屏障（memory barrier）是一种非阻塞的同步工具，用于确保内存操作按正确的顺序发生。内存屏障就像一道栅栏，它强制处理器必须先完成屏障之前的所有加载和存储操作，才允许执行屏障之后的加载和存储操作。内存屏障通常用于确保一个线程执行的内存操作（但对另一个线程可见）总是按预期的顺序发生。在这种情况下，如果缺少内存屏障，可能会让其他线程看到看似不可能出现的结果。（相关示例请参阅维基百科关于[内存屏障](http://en.wikipedia.org/wiki/Memory_barrier)的条目。）要使用内存屏障，你只需在代码中的合适位置调用 `OSMemoryBarrier` 函数即可。

volatile 变量对单个变量施加了另一种类型的内存约束。编译器常常会通过将变量的值加载到寄存器中来优化代码。对于局部变量而言，这通常不是问题。然而，如果该变量对另一个线程可见，这种优化可能会导致另一个线程注意不到对它所做的任何更改。将 `volatile` 关键字应用于某个变量，会强制编译器每次使用该变量时都从内存中重新加载它。如果一个变量的值可能随时被编译器无法检测到的外部来源更改，你就应该将其声明为 `volatile`。

由于内存屏障和 volatile 变量都会减少编译器所能执行的优化数量，所以应当谨慎使用它们，只在确保正确性确实需要的地方才使用。有关使用内存屏障的信息，请参阅 [OSMemoryBarrier](https://developer.apple.com/library/archive/documentation/System/Conceptual/ManPages_iPhoneOS/man3/OSMemoryBarrier.3.html#//apple_ref/doc/man/3/OSMemoryBarrier) man 手册页。

锁是最常用的同步工具之一。你可以使用锁来保护代码中的_临界区（critical section）_，这是一段一次只允许一个线程访问的代码。例如，一个临界区可能会操作某个特定的数据结构，或者使用某种一次最多只支持一个客户端的资源。通过在这段代码周围加锁，你可以排除其他线程做出可能影响代码正确性的更改。

表 4-1 列出了程序员常用的一些锁。OS X 和 iOS 为其中的大多数锁类型提供了实现，但并非全部都有。对于不支持的锁类型，说明列会解释这些锁没有在该平台上直接实现的原因。

__表 4-1__  锁的类型

| 锁 | 说明 |
| --- | --- |
| Mutex | 互斥（mutually exclusive，简称 _mutex_）锁充当资源周围的一道保护屏障。mutex 是一种信号量，一次只授予一个线程访问权限。如果某个 mutex 正在使用中，而另一个线程试图获取它，该线程就会阻塞，直到原来持有该 mutex 的线程将其释放为止。如果多个线程争用同一个 mutex，一次也只允许一个线程访问它。 |
| Recursive lock（递归锁） | 递归锁是互斥锁的一种变体。递归锁允许同一个线程在释放锁之前多次获取该锁。其他线程会一直保持阻塞，直到该锁的持有者以获取次数相同的次数释放该锁为止。递归锁主要用于递归迭代过程中，但也可以用于多个方法各自都需要单独获取该锁的情况。 |
| Read-write lock（读写锁） | 读写锁也被称为共享-互斥（shared-exclusive）锁。这类锁通常用于较大规模的操作，如果被保护的数据结构经常被读取、只是偶尔被修改，读写锁能显著提升性能。在正常操作期间，多个读取者可以同时访问该数据结构。不过，当某个线程想要写入该结构时，它会阻塞，直到所有读取者都释放锁为止，此时它才会获取该锁并可以更新该结构。当一个写入线程正在等待该锁时，新的读取线程会阻塞，直到该写入线程完成为止。系统仅支持使用 POSIX 线程实现读写锁。有关如何使用这些锁的更多信息，请参阅 [pthread](https://developer.apple.com/library/archive/documentation/System/Conceptual/ManPages_iPhoneOS/man3/pthread.3.html#//apple_ref/doc/man/3/pthread) man 手册页。 |
| Distributed lock（分布式锁） | 分布式锁在进程级别提供互斥访问。与真正的 mutex 不同，分布式锁不会阻塞某个进程或阻止其运行。它只是报告该锁是否正忙，并让进程自行决定如何处理。 |
| Spin lock（自旋锁） | 自旋锁会反复轮询其加锁条件，直到该条件变为真为止。自旋锁最常用于多处理器系统中锁的预期等待时间很短的场合。在这些情况下，轮询往往比阻塞线程更高效，因为阻塞线程涉及上下文切换和线程数据结构的更新。由于自旋锁具有轮询的性质，系统不提供任何自旋锁的实现，但你可以很方便地在特定场景中自行实现它们。有关在内核中实现自旋锁的信息，请参阅 _[内核编程指南](../../Darwin/Kernel%20Programming%20Guide/About%20This%20Document.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaydsmbv)_。 |
| Double-checked lock（双重检查锁） | 双重检查锁试图通过在加锁之前先测试加锁条件，来减少加锁的开销。由于双重检查锁具有潜在的不安全性，系统不为其提供明确的支持，也不建议使用这种锁。 |

有关如何使用锁的信息，请参阅[使用锁](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgeydambqga2to2jninedqlktk4ytm)。

条件（condition）是另一种类型的信号量，它允许线程在某个条件成立时相互发送信号。条件通常用于指示某种资源是否可用，或者用于确保任务按特定顺序执行。当一个线程测试某个条件时，除非该条件已经成立，否则它会阻塞。它会一直保持阻塞状态，直到其他线程显式地改变并发出该条件的信号为止。条件与互斥锁的区别在于，可能允许多个线程同时访问该条件。条件更像是一个把关者，会根据某些指定的条件让不同的线程通过关卡。

使用条件的一种方式是管理一个待处理事件池。事件队列会使用一个条件变量，在队列中有事件时向等待中的线程发送信号。如果有一个事件到达，队列就会适当地发出该条件的信号。如果已经有一个线程在等待，它就会被唤醒，随后从队列中取出该事件并进行处理。如果几乎同时有两个事件进入队列，队列就会两次发出该条件的信号，以唤醒两个线程。

系统在几种不同的技术中都提供了对条件的支持。不过，条件的正确实现需要谨慎编码，因此在自己的代码中使用它们之前，你应该先查看[使用条件](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgeydambqga2to2jninedqlktk42a)中的示例。

Cocoa 应用程序有一种方便的方式，能以同步的方式向单个线程传递消息。[NSObject](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSObject/Description.html#//apple_ref/occ/cl/NSObject) 类声明了一些方法，用于在应用程序的某个活动线程上执行一个选择器（selector）。这些方法可以让你的线程异步地传递消息，同时保证这些消息会由目标线程同步执行。例如，你可以使用执行选择器（perform selector）消息，将一次分布式计算的结果传递给应用程序的主线程或某个指定的协调线程。每一个执行选择器的请求都会被排入目标线程运行循环的队列中，然后这些请求会按接收到的顺序依次处理。

有关执行选择器例程的概要以及如何使用它们的更多信息，请参阅 [Cocoa 执行选择器源](Run%20Loops.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgeydambqga2to2jninedcnrnknltina)。

同步有助于确保代码的正确性，但要以牺牲性能为代价。即便在不存在争用的情况下，使用同步工具也会引入延迟。锁和原子操作通常都要用到内存屏障和内核级同步，以确保代码得到妥善保护。而如果存在锁的争用，你的线程可能会阻塞，遭遇更大的延迟。

表 4-2 列出了在不存在争用的情况下，与 mutex 和原子操作相关的一些大致开销。这些测量结果是对数千个样本取平均时间得到的。不过，正如线程创建时间一样，即便是在不存在争用的情况下，mutex 的获取时间也会因处理器负载、计算机速度以及可用的系统和程序内存量的不同而有很大差异。

__表 4-2__  mutex 与原子操作的开销

| 项目 | 大致开销 | 说明 |
| --- | --- | --- |
| Mutex 获取时间 | 约 0.2 微秒 | 这是不存在争用情况下的加锁获取时间。如果该锁被另一个线程持有，获取时间可能会大得多。这些数据是通过分析在一台配备 2 GHz Core Duo 处理器和 1 GB 内存、运行 OS X v10.5 的基于 Intel 的 iMac 上，mutex 获取过程中产生的平均值和中位数得出的。 |
| 原子比较并交换 | 约 0.05 微秒 | 这是不存在争用情况下的比较并交换时间。这些数据是通过分析该操作在一台配备 2 GHz Core Duo 处理器和 1 GB 内存、运行 OS X v10.5 的基于 Intel 的 iMac 上产生的平均值和中位数得出的。 |

在设计并发任务时，正确性永远是最重要的因素，但你也应该考虑性能方面的因素。如果代码在多线程下能正确执行，但速度却比同样的代码在单线程下运行还慢，那几乎算不上什么改进。

如果你是在对一个现有的单线程应用程序进行改造，你应该始终先对关键任务的性能进行一组基准测量。在添加额外的线程之后，你应该再对相同的任务进行新的测量，并将多线程情况下的性能与单线程情况下的性能进行比较。如果在调优代码之后，多线程仍未能提升性能，你可能需要重新考虑你的具体实现方式，或者干脆重新考虑是否要使用线程。

有关性能以及用于收集指标的工具的信息，请参阅 _[性能概述](../../Performance/Performance%20Overview/Introduction.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytimjq)_。有关锁和原子操作开销的具体信息，请参阅[线程开销](Thread%20Management.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgeydambqga2to2jninedcnjnknlto)。

说到多线程应用程序，没有什么比处理信号（signal）的问题更让人恐惧或困惑的了。信号是一种底层的 BSD 机制，可用于向进程传递信息或以某种方式操纵进程。有些程序使用信号来检测某些事件，例如子进程的终止。系统使用信号来终止失控的进程，并传递其他类型的信息。

信号本身做什么并不是问题所在，问题在于当你的应用程序有多个线程时，信号的行为方式。在单线程应用程序中，所有信号处理程序都运行在主线程上。而在多线程应用程序中，那些不与特定硬件错误（例如非法指令）绑定的信号，会被传递给当时恰好在运行的那个线程。如果多个线程同时在运行，该信号就会被传递给系统碰巧选中的那一个线程。换句话说，信号可能被传递给应用程序的任何线程。

在应用程序中实现信号处理程序的第一条规则是，避免假设哪个线程会处理该信号。如果某个特定线程想要处理给定的信号，你就需要想办法在信号到达时通知那个线程。你不能想当然地认为，从某个线程安装信号处理程序，就会使该信号被传递给同一个线程。

有关信号以及安装信号处理程序的更多信息，请参阅 [signal](https://developer.apple.com/library/archive/documentation/System/Conceptual/ManPages_iPhoneOS/man3/signal.3.html#//apple_ref/doc/man/3/signal) 和 [sigaction](https://developer.apple.com/library/archive/documentation/System/Conceptual/ManPages_iPhoneOS/man2/sigaction.2.html#//apple_ref/doc/man/2/sigaction) man 手册页。

同步工具是使代码线程安全的一种有用方式，但它们并非万能良药。如果使用过度，锁和其他类型的同步原语实际上可能会使应用程序的多线程性能低于非多线程时的性能。在安全性和性能之间找到恰当的平衡，是一门需要经验积累的艺术。以下各节提供了一些技巧，帮助你为应用程序选择合适的同步级别。

对于你所从事的任何新项目，甚至对于现有项目，将代码和数据结构设计成不需要同步的形式，是最好的解决方案。虽然锁和其他同步工具很有用，但它们确实会影响任何应用程序的性能。而且，如果整体设计导致某些特定资源出现高争用，你的线程可能要等待更长的时间。

实现并发的最佳方式是减少并发任务之间的交互和相互依赖关系。如果每个任务都操作自己的私有数据集，它就不需要使用锁来保护这些数据。即使在两个任务确实共享同一个公共数据集的情况下，你也可以考虑对该数据集进行分区，或者为每个任务提供各自的一份副本。当然，复制数据集也有其代价，所以你必须在做决定之前，权衡这些代价与同步的代价。

只有当应用程序中的所有线程都一致地使用同步工具时，这些工具才有效。如果你创建了一个 mutex 来限制对某个特定资源的访问，那么你所有的线程在试图操作该资源之前，都必须获取同一个 mutex。如果做不到这一点，就会破坏该 mutex 所提供的保护，这是一种编程错误。

在使用锁和内存屏障时，你应该始终仔细考虑它们在代码中的位置。即使是看起来放置得当的锁，实际上也可能让你产生一种虚假的安全感。下面这一系列示例试图通过指出看似无害的代码中的缺陷，来说明这个问题。这些示例的基本前提是：你有一个可变数组，其中包含一组不可变对象。假设你想调用数组中第一个对象的某个方法，你可能会使用以下代码来实现：

```objc
NSLock* arrayLock = GetArrayLock();
NSMutableArray* myArray = GetSharedArray();
id anObject;

[arrayLock lock];
anObject = [myArray objectAtIndex:0];
[arrayLock unlock];

[anObject doSomething];
```

因为该数组是可变的，围绕该数组加的锁能阻止其他线程在你取得所需对象之前修改该数组。而且，由于你取出的对象本身是不可变的，围绕 `doSomething` 方法的调用就不需要加锁。

不过，前面这个示例存在一个问题。如果你释放了锁，而另一个线程随即进入并把数组中的所有对象都移除，而你还没来得及执行 `doSomething` 方法，会发生什么？在没有垃圾回收的应用程序中，你的代码所持有的对象可能会被释放，导致 `anObject` 指向一个无效的内存地址。为了解决这个问题，你可能会决定简单地重新调整现有代码，在调用 `doSomething` 之后再释放锁，如下所示：

```objc
NSLock* arrayLock = GetArrayLock();
NSMutableArray* myArray = GetSharedArray();
id anObject;

[arrayLock lock];
anObject = [myArray objectAtIndex:0];
[anObject doSomething];
[arrayLock unlock];
```

通过把 `doSomething` 调用移到锁内部，你的代码可以保证在调用该方法时，该对象仍然有效。不幸的是，如果 `doSomething` 方法需要执行很长时间，这可能会导致你的代码长时间持有该锁，从而造成性能瓶颈。

这段代码的问题并不在于临界区界定得不好，而在于没有理解真正的问题所在。真正的问题是一个内存管理问题，它只有在存在其他线程的情况下才会被触发。由于该对象可能被另一个线程释放，更好的解决方案是在释放锁之前先保留（retain）`anObject`。这个方案解决了对象被释放这个真正的问题，同时又不会引入潜在的性能损耗。

```objc
NSLock* arrayLock = GetArrayLock();
NSMutableArray* myArray = GetSharedArray();
id anObject;

[arrayLock lock];
anObject = [myArray objectAtIndex:0];
[anObject retain];
[arrayLock unlock];

[anObject doSomething];
[anObject release];
```

尽管前面这些示例本质上都非常简单，但它们的确说明了一个非常重要的观点。谈到正确性，你必须超越表面上显而易见的问题来思考。内存管理以及你设计中的其他方面，也可能受到多线程存在的影响，因此你必须提前考虑这些问题。此外，在涉及安全性的问题上，你应该始终假设编译器会做出最坏的处理方式。这种意识和警惕性应该有助于你避免潜在的问题，并确保代码行为正确。

有关如何使程序线程安全的更多示例，请参阅[线程安全概要](Thread%20Safety%20Summary.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgeydambqga2to2jninedcmrnknltc)。

任何时候，只要一个线程试图同时持有多个锁，就存在发生死锁的可能。死锁发生在两个不同的线程都持有对方所需要的锁，并且都试图获取对方所持有的锁的情况下。结果就是每个线程都永久阻塞，因为它永远也无法获取另一个锁。

活锁与死锁类似，发生在两个线程争夺同一组资源时。在活锁的情况下，一个线程放弃它持有的第一个锁，试图获取第二个锁。一旦它获取了第二个锁，它又会返回去尝试再次获取第一个锁。它之所以陷入停滞，是因为它把所有时间都花在释放一个锁、试图获取另一个锁上，而没有做任何实际的工作。

避免死锁和活锁情况的最佳方式是一次只持有一个锁。如果你必须一次获取多个锁，你应该确保其他线程不会尝试做类似的事情。

如果你已经在使用某个 mutex 来保护一段代码，不要想当然地认为你还需要使用 `volatile` 关键字来保护该段代码中的重要变量。mutex 本身就包含一个内存屏障，能确保加载和存储操作的正确顺序。在临界区内给某个变量加上 `volatile` 关键字，会强制每次访问该变量时都从内存中重新加载它的值。在特定情况下，这两种同步技术的组合可能是必要的，但也会导致明显的性能损耗。如果单靠 mutex 就足以保护该变量，就应该省去 `volatile` 关键字。

同样重要的是，你不应该试图用 volatile 变量来取代 mutex 的使用。一般来说，mutex 和其他同步机制在保护数据结构完整性方面，都比 volatile 变量更好。`volatile` 关键字只能确保某个变量是从内存中加载的，而不是存放在寄存器中，它并不能确保该变量被你的代码正确地访问。

非阻塞同步（nonblocking synchronization）是一种执行某些类型操作、同时避免锁的开销的方式。虽然锁是同步两个线程的有效方式，但获取一个锁是一个相对昂贵的操作，即使在不存在争用的情况下也是如此。相比之下，许多原子操作只需要极短的时间就能完成，而且效果可以和锁一样好。

原子操作让你可以对 32 位或 64 位的值执行简单的数学和逻辑运算。这些操作依赖特殊的硬件指令（以及一个可选的内存屏障），以确保在给定操作完成之前，受影响的内存不会被再次访问。在多线程的情况下，你应该始终使用包含内存屏障的原子操作，以确保内存在各线程之间得到正确的同步。

表 4-3 列出了可用的原子数学和逻辑运算及其对应的函数名。这些函数都声明在 `/usr/include/libkern/OSAtomic.h` 头文件中，你也可以在其中找到完整的语法。这些函数的 64 位版本只能在 64 位进程中使用。

__表 4-3__  原子数学与逻辑运算

| 操作 | 函数名 | 说明 |
| --- | --- | --- |
| 加法 | [OSAtomicAdd32](https://developer.apple.com/library/archive/documentation/System/Conceptual/ManPages_iPhoneOS/man3/OSAtomicAdd32.3.html#//apple_ref/doc/man/3/OSAtomicAdd32)  [OSAtomicAdd32Barrier](https://developer.apple.com/library/archive/documentation/System/Conceptual/ManPages_iPhoneOS/man3/OSAtomicAdd32Barrier.3.html#//apple_ref/doc/man/3/OSAtomicAdd32Barrier)  [OSAtomicAdd64](https://developer.apple.com/library/archive/documentation/System/Conceptual/ManPages_iPhoneOS/man3/OSAtomicAdd64.3.html#//apple_ref/doc/man/3/OSAtomicAdd64)  [OSAtomicAdd64Barrier](https://developer.apple.com/library/archive/documentation/System/Conceptual/ManPages_iPhoneOS/man3/OSAtomicAdd64Barrier.3.html#//apple_ref/doc/man/3/OSAtomicAdd64Barrier) | 将两个整数值相加，并将结果存储到其中一个指定的变量中。 |
| 递增 | [OSAtomicIncrement32](https://developer.apple.com/library/archive/documentation/System/Conceptual/ManPages_iPhoneOS/man3/OSAtomicIncrement32.3.html#//apple_ref/doc/man/3/OSAtomicIncrement32)  [OSAtomicIncrement32Barrier](https://developer.apple.com/library/archive/documentation/System/Conceptual/ManPages_iPhoneOS/man3/OSAtomicIncrement32Barrier.3.html#//apple_ref/doc/man/3/OSAtomicIncrement32Barrier)  [OSAtomicIncrement64](https://developer.apple.com/library/archive/documentation/System/Conceptual/ManPages_iPhoneOS/man3/OSAtomicIncrement64.3.html#//apple_ref/doc/man/3/OSAtomicIncrement64)  [OSAtomicIncrement64Barrier](https://developer.apple.com/library/archive/documentation/System/Conceptual/ManPages_iPhoneOS/man3/OSAtomicIncrement64Barrier.3.html#//apple_ref/doc/man/3/OSAtomicIncrement64Barrier) | 将指定的整数值加 1。 |
| 递减 | [OSAtomicDecrement32](https://developer.apple.com/library/archive/documentation/System/Conceptual/ManPages_iPhoneOS/man3/OSAtomicDecrement32.3.html#//apple_ref/doc/man/3/OSAtomicDecrement32)  [OSAtomicDecrement32Barrier](https://developer.apple.com/library/archive/documentation/System/Conceptual/ManPages_iPhoneOS/man3/OSAtomicDecrement32Barrier.3.html#//apple_ref/doc/man/3/OSAtomicDecrement32Barrier)  [OSAtomicDecrement64](https://developer.apple.com/library/archive/documentation/System/Conceptual/ManPages_iPhoneOS/man3/OSAtomicDecrement64.3.html#//apple_ref/doc/man/3/OSAtomicDecrement64)  [OSAtomicDecrement64Barrier](https://developer.apple.com/library/archive/documentation/System/Conceptual/ManPages_iPhoneOS/man3/OSAtomicDecrement64Barrier.3.html#//apple_ref/doc/man/3/OSAtomicDecrement64Barrier) | 将指定的整数值减 1。 |
| 逻辑 OR | [OSAtomicOr32](https://developer.apple.com/library/archive/documentation/System/Conceptual/ManPages_iPhoneOS/man3/OSAtomicOr32.3.html#//apple_ref/doc/man/3/OSAtomicOr32)  [OSAtomicOr32Barrier](https://developer.apple.com/library/archive/documentation/System/Conceptual/ManPages_iPhoneOS/man3/OSAtomicOr32Barrier.3.html#//apple_ref/doc/man/3/OSAtomicOr32Barrier) | 对指定的 32 位值和一个 32 位掩码执行逻辑 OR 运算。 |
| 逻辑 AND | [OSAtomicAnd32](https://developer.apple.com/library/archive/documentation/System/Conceptual/ManPages_iPhoneOS/man3/OSAtomicAnd32.3.html#//apple_ref/doc/man/3/OSAtomicAnd32)  [OSAtomicAnd32Barrier](https://developer.apple.com/library/archive/documentation/System/Conceptual/ManPages_iPhoneOS/man3/OSAtomicAnd32Barrier.3.html#//apple_ref/doc/man/3/OSAtomicAnd32Barrier) | 对指定的 32 位值和一个 32 位掩码执行逻辑 AND 运算。 |
| 逻辑 XOR | [OSAtomicXor32](https://developer.apple.com/library/archive/documentation/System/Conceptual/ManPages_iPhoneOS/man3/OSAtomicXor32.3.html#//apple_ref/doc/man/3/OSAtomicXor32)  [OSAtomicXor32Barrier](https://developer.apple.com/library/archive/documentation/System/Conceptual/ManPages_iPhoneOS/man3/OSAtomicXor32Barrier.3.html#//apple_ref/doc/man/3/OSAtomicXor32Barrier) | 对指定的 32 位值和一个 32 位掩码执行逻辑 XOR 运算。 |
| 比较并交换 | [OSAtomicCompareAndSwap32](https://developer.apple.com/library/archive/documentation/System/Conceptual/ManPages_iPhoneOS/man3/OSAtomicCompareAndSwap32.3.html#//apple_ref/doc/man/3/OSAtomicCompareAndSwap32)  [OSAtomicCompareAndSwap32Barrier](https://developer.apple.com/library/archive/documentation/System/Conceptual/ManPages_iPhoneOS/man3/OSAtomicCompareAndSwap32Barrier.3.html#//apple_ref/doc/man/3/OSAtomicCompareAndSwap32Barrier)  [OSAtomicCompareAndSwap64](https://developer.apple.com/library/archive/documentation/System/Conceptual/ManPages_iPhoneOS/man3/OSAtomicCompareAndSwap64.3.html#//apple_ref/doc/man/3/OSAtomicCompareAndSwap64)  [OSAtomicCompareAndSwap64Barrier](https://developer.apple.com/library/archive/documentation/System/Conceptual/ManPages_iPhoneOS/man3/OSAtomicCompareAndSwap64Barrier.3.html#//apple_ref/doc/man/3/OSAtomicCompareAndSwap64Barrier)  [OSAtomicCompareAndSwapPtr](https://developer.apple.com/library/archive/documentation/System/Conceptual/ManPages_iPhoneOS/man3/OSAtomicCompareAndSwapPtr.3.html#//apple_ref/doc/man/3/OSAtomicCompareAndSwapPtr)  [OSAtomicCompareAndSwapPtrBarrier](https://developer.apple.com/library/archive/documentation/System/Conceptual/ManPages_iPhoneOS/man3/OSAtomicCompareAndSwapPtrBarrier.3.html#//apple_ref/doc/man/3/OSAtomicCompareAndSwapPtrBarrier)  [OSAtomicCompareAndSwapInt](https://developer.apple.com/library/archive/documentation/System/Conceptual/ManPages_iPhoneOS/man3/OSAtomicCompareAndSwapInt.3.html#//apple_ref/doc/man/3/OSAtomicCompareAndSwapInt)  [OSAtomicCompareAndSwapIntBarrier](https://developer.apple.com/library/archive/documentation/System/Conceptual/ManPages_iPhoneOS/man3/OSAtomicCompareAndSwapIntBarrier.3.html#//apple_ref/doc/man/3/OSAtomicCompareAndSwapIntBarrier)  [OSAtomicCompareAndSwapLong](https://developer.apple.com/library/archive/documentation/System/Conceptual/ManPages_iPhoneOS/man3/OSAtomicCompareAndSwapLong.3.html#//apple_ref/doc/man/3/OSAtomicCompareAndSwapLong)  [OSAtomicCompareAndSwapLongBarrier](https://developer.apple.com/library/archive/documentation/System/Conceptual/ManPages_iPhoneOS/man3/OSAtomicCompareAndSwapLongBarrier.3.html#//apple_ref/doc/man/3/OSAtomicCompareAndSwapLongBarrier) | 将某个变量与指定的旧值进行比较。如果两个值相等，该函数会将指定的新值赋给该变量；否则不做任何操作。比较和赋值是作为一个原子操作完成的，该函数会返回一个布尔值，表明交换是否真的发生了。 |
| 测试并置位 | [OSAtomicTestAndSet](https://developer.apple.com/library/archive/documentation/System/Conceptual/ManPages_iPhoneOS/man3/OSAtomicTestAndSet.3.html#//apple_ref/doc/man/3/OSAtomicTestAndSet)  [OSAtomicTestAndSetBarrier](https://developer.apple.com/library/archive/documentation/System/Conceptual/ManPages_iPhoneOS/man3/OSAtomicTestAndSetBarrier.3.html#//apple_ref/doc/man/3/OSAtomicTestAndSetBarrier) | 测试指定变量中的某一位，将该位置为 1，并以布尔值的形式返回该位原来的值。位的测试依据的公式是：字节 `((char*)address + (n >> 3))` 的 `(0x80 >> (n & 7))`，其中 `n` 是位号，`address` 是指向该变量的指针。这个公式实际上是把该变量拆分成若干个 8 位大小的块，并将每个块中的位顺序反转。例如，要测试一个 32 位整数的最低位（第 0 位），你实际上需要指定位号为 7；同样，要测试最高位（第 32 位），你需要指定位号为 24。 |
| 测试并清零 | [OSAtomicTestAndClear](https://developer.apple.com/library/archive/documentation/System/Conceptual/ManPages_iPhoneOS/man3/OSAtomicTestAndClear.3.html#//apple_ref/doc/man/3/OSAtomicTestAndClear)  [OSAtomicTestAndClearBarrier](https://developer.apple.com/library/archive/documentation/System/Conceptual/ManPages_iPhoneOS/man3/OSAtomicTestAndClearBarrier.3.html#//apple_ref/doc/man/3/OSAtomicTestAndClearBarrier) | 测试指定变量中的某一位，将该位置为 0，并以布尔值的形式返回该位原来的值。位的测试依据的公式是：字节 `((char*)address + (n >> 3))` 的 `(0x80 >> (n & 7))`，其中 `n` 是位号，`address` 是指向该变量的指针。这个公式实际上是把该变量拆分成若干个 8 位大小的块，并将每个块中的位顺序反转。例如，要测试一个 32 位整数的最低位（第 0 位），你实际上需要指定位号为 7；同样，要测试最高位（第 32 位），你需要指定位号为 24。 |

大多数原子函数的行为应该都相当直观，符合你的预期。不过，清单 4-1 展示了原子测试并置位和比较并交换操作的行为，这两者要稍微复杂一些。对 `OSAtomicTestAndSet` 函数的前三次调用演示了，作用在一个整数值上的位操作公式及其结果可能与你预期的有所不同。后两次调用展示了 `OSAtomicCompareAndSwap32` 函数的行为。在所有这些情况下，这些函数都是在不存在争用的情况下调用的，即没有其他线程在操作这些值。

__清单 4-1__  执行原子操作

```c
int32_t  theValue = 0;
OSAtomicTestAndSet(0, &theValue);
// theValue 现在是 128。

theValue = 0;
OSAtomicTestAndSet(7, &theValue);
// theValue 现在是 1。

theValue = 0;
OSAtomicTestAndSet(15, &theValue)
// theValue 现在是 256。

OSAtomicCompareAndSwap32(256, 512, &theValue);
// theValue 现在是 512。

OSAtomicCompareAndSwap32(256, 1024, &theValue);
// theValue 仍然是 512。
```

有关原子操作的信息，请参阅 [atomic](https://developer.apple.com/library/archive/documentation/System/Conceptual/ManPages_iPhoneOS/man3/atomic.3.html#//apple_ref/doc/man/3/atomic) man 手册页和 `/usr/include/libkern/OSAtomic.h` 头文件。

锁是多线程编程中一种基本的同步工具。锁能让你轻松地保护大段代码，从而确保这些代码的正确性。OS X 和 iOS 为所有类型的应用程序提供了基本的 mutex 锁，Foundation 框架还为一些特殊情况定义了 mutex 锁的额外变体。以下各节将展示如何使用其中的几种锁类型。

POSIX mutex 锁在任何应用程序中都极其容易使用。要创建 mutex 锁，你需要声明并初始化一个 `pthread_mutex_t` 结构体。要对该 mutex 锁进行加锁和解锁，你可以使用 `pthread_mutex_lock` 和 `pthread_mutex_unlock` 函数。清单 4-2 展示了初始化并使用一个 POSIX 线程 mutex 锁所需的基本代码。当你使用完该锁后，只需调用 `pthread_mutex_destroy` 即可释放该锁的数据结构。

__清单 4-2__  使用 mutex 锁

```c
pthread_mutex_t mutex;
void MyInitFunction()
{
    pthread_mutex_init(&mutex, NULL);
}

void MyLockingFunction()
{
    pthread_mutex_lock(&mutex);
    // 做一些工作。
    pthread_mutex_unlock(&mutex);
}
```


[NSLock](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSLock/Description.html#//apple_ref/occ/cl/NSLock) 对象为 Cocoa 应用程序实现了一个基本的 mutex。所有锁（包括 `NSLock`）的接口实际上都由 [NSLocking](https://developer.apple.com/documentation/foundation/nslocking) 协议定义，该协议定义了 `lock` 和 `unlock` 方法。你可以使用这些方法来获取和释放锁，就像使用任何 mutex 一样。

除了标准的加锁行为外，`NSLock` 类还增加了 [tryLock](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSLock/Description.html#//apple_ref/occ/instm/NSLock/tryLock) 和 [lockBeforeDate:](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSLock/Description.html#//apple_ref/occ/instm/NSLock/lockBeforeDate:) 方法。[tryLock](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSLock/Description.html#//apple_ref/occ/instm/NSLock/tryLock) 方法会尝试获取该锁，但如果该锁不可用，它不会阻塞，而是直接返回 `NO`。[lockBeforeDate:](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSLock/Description.html#//apple_ref/occ/instm/NSLock/lockBeforeDate:) 方法会尝试获取该锁，但如果在指定的时限内未能获取到该锁，就会解除线程的阻塞（并返回 `NO`）。

以下示例展示了如何使用 `NSLock` 对象来协调对某个可视化显示界面的更新，该界面的数据是由多个线程计算得出的。如果某个线程无法立即获取该锁，它就会继续进行计算，直到能够获取该锁并更新显示界面为止。

```objc
BOOL moreToDo = YES;
NSLock *theLock = [[NSLock alloc] init];
...
while (moreToDo) {
    /* 再进行一次计算的递增， */
    /* 直到没有更多工作要做为止。 */
    if ([theLock tryLock]) {
        /* 更新所有线程共用的显示界面。 */
        [theLock unlock];
    }
}
```


`@synchronized` 指令是一种在 Objective-C 代码中动态创建 mutex 锁的便捷方式。`@synchronized` 指令所做的事情和其他任何 mutex 锁一样——它可以防止不同的线程同时获取同一个锁。不过，在这种情况下，你不必直接创建 mutex 或锁对象，而只需使用任意一个 Objective-C 对象作为锁令牌即可，如以下示例所示：

```objc
- (void)myMethod:(id)anObj
{
    @synchronized(anObj)
    {
        // 大括号之间的所有内容都受 @synchronized 指令保护。
    }
}
```

传递给 `@synchronized` 指令的对象是一个唯一标识符，用于区分受保护的代码块。如果你在两个不同的线程中执行前面这个方法，并且每个线程为 `anObj` 参数传入不同的对象，那么每个线程都会各自持有自己的锁，并继续处理，不会被对方阻塞。但如果两次都传入相同的对象，其中一个线程就会先获取该锁，而另一个线程会阻塞，直到第一个线程完成该临界区为止。

作为一种预防措施，`@synchronized` 代码块会隐式地为受保护的代码添加一个异常处理程序。一旦抛出异常，该处理程序会自动释放该 mutex。这意味着，要使用 `@synchronized` 指令，你还必须在代码中启用 Objective-C 异常处理。如果你不想承受这个隐式异常处理程序带来的额外开销，就应该考虑改用锁类。

有关 `@synchronized` 指令的更多信息，请参阅 _[The Objective-C Programming Language](../The%20Objective-C%20Programming%20Language/Introduction.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaytcnrt)_。

以下各节介绍了使用其他几种 Cocoa 锁类型的方法。

[NSRecursiveLock](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSRecursiveLock/Description.html#//apple_ref/occ/cl/NSRecursiveLock) 类定义了一种锁，同一个线程可以多次获取该锁而不会导致该线程死锁。递归锁会记录它被成功获取的次数。每一次成功获取该锁，都必须有一次对应的解锁调用与之相抵消。只有当所有的加锁和解锁调用都相互抵消之后，该锁才会真正被释放，从而让其他线程能够获取它。

正如其名称所暗示的，这种类型的锁常常用于递归函数内部，以防止递归导致线程阻塞。你同样也可以在非递归的情况下使用它，来调用那些语义上也需要获取该锁的函数。下面是一个简单递归函数的示例，它通过递归来获取该锁。如果这段代码不使用 `NSRecursiveLock` 对象，当该函数被再次调用时，线程就会死锁。

```objc
NSRecursiveLock *theLock = [[NSRecursiveLock alloc] init];

void MyRecursiveFunction(int value)
{
    [theLock lock];
    if (value != 0)
    {
        --value;
        MyRecursiveFunction(value);
    }
    [theLock unlock];
}

MyRecursiveFunction(5);
```


[NSConditionLock](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSConditionLock/Description.html#//apple_ref/occ/cl/NSConditionLock) 对象定义了一种可以用特定值加锁和解锁的 mutex 锁。你不应该把这种锁与条件（condition）混淆（参见[条件](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgeydambqga2to2jninedqljrgi3dimru)）。它的行为与条件有些相似，但实现方式却大不相同。

通常情况下，当线程需要按特定顺序执行任务时，比如一个线程生产数据、另一个线程消费数据，你就会用到 `NSConditionLock` 对象。当生产者正在执行时，消费者会使用一个特定于你程序的条件来获取该锁。（这个条件本身只是你定义的一个整数值。）当生产者完成后，它会解锁该锁，并将锁条件设置为适当的整数值，以唤醒消费者线程，消费者线程随后就会继续处理数据。

`NSConditionLock` 对象所响应的加锁和解锁方法可以任意组合使用。例如，你可以将 `lock` 消息与 [unlockWithCondition:](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSConditionLock/Description.html#//apple_ref/occ/instm/NSConditionLock/unlockWithCondition:) 配对，或者将 [lockWhenCondition:](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSConditionLock/Description.html#//apple_ref/occ/instm/NSConditionLock/lockWhenCondition:) 消息与 `unlock` 配对。当然，后一种组合方式虽然会解锁该锁，但可能不会释放任何正在等待某个特定条件值的线程。

以下示例展示了如何使用条件锁来处理生产者-消费者问题。设想一个应用程序包含一个数据队列，生产者线程向队列中添加数据，消费者线程从队列中提取数据。生产者不需要等待某个特定条件，但它必须等待该锁可用，才能安全地向队列中添加数据。

```objc
id condLock = [[NSConditionLock alloc] initWithCondition:NO_DATA];

while(true)
{
    [condLock lock];
    /* 向队列中添加数据。 */
    [condLock unlockWithCondition:HAS_DATA];
}
```

由于该锁的初始条件被设置为 `NO_DATA`，生产者线程一开始应该能毫无困难地获取该锁。它向队列中填充数据，并将条件设置为 `HAS_DATA`。在后续的迭代中，无论队列是空的还是仍有一些数据，生产者线程都可以在新数据到达时将其添加进去。它唯一阻塞的时候，是消费者线程正在从队列中提取数据的时候。

由于消费者线程必须有数据才能处理，它会使用一个特定条件在队列上等待。当生产者把数据放入队列后，消费者线程就会被唤醒并获取它的锁。然后它就可以从队列中提取一些数据并更新队列状态。以下示例展示了消费者线程处理循环的基本结构。

```objc
while (true)
{
    [condLock lockWhenCondition:HAS_DATA];
    /* 从队列中移除数据。 */
    [condLock unlockWithCondition:(isEmpty ? NO_DATA : HAS_DATA)];

    // 在本地处理数据。
}
```


[NSDistributedLock](https://developer.apple.com/documentation/foundation/nsdistributedlock) 类可以被多台主机上的多个应用程序使用，用来限制对某个共享资源（例如一个文件）的访问。这种锁本质上是一个 mutex 锁，通过某个文件系统项（例如一个文件或目录）来实现。要让 `NSDistributedLock` 对象可用，该锁必须对使用它的所有应用程序都是可写的。这通常意味着要把它放在一个所有运行该应用程序的计算机都能访问的文件系统上。

与其他类型的锁不同，`NSDistributedLock` 不遵循 [NSLocking](https://developer.apple.com/documentation/foundation/nslocking) 协议，因此没有 `lock` 方法。`lock` 方法会阻塞线程的执行，并要求系统以预定的速率轮询该锁。为了不让你的代码承受这种代价，`NSDistributedLock` 提供了一个 [tryLock](https://developer.apple.com/documentation/foundation/nsdistributedlock/1412293-trylock) 方法，让你自行决定是否进行轮询。

由于它是通过文件系统实现的，`NSDistributedLock` 对象不会被释放，除非其所有者显式地释放它。如果你的应用程序在持有分布式锁期间崩溃，其他客户端就无法访问受保护的资源。在这种情况下，你可以使用 [breakLock](https://developer.apple.com/documentation/foundation/nsdistributedlock/1413425-breaklock) 方法来打破现有的锁，从而让你能够获取它。不过，一般应该避免打破锁，除非你确信持有该锁的进程已经死亡且无法释放该锁。

与其他类型的锁一样，当你使用完 `NSDistributedLock` 对象后，需要通过调用 `unlock` 方法来释放它。

条件是一种特殊类型的锁，你可以用它来同步操作必须进行的先后顺序。它们与 mutex 锁的区别在于一个微妙之处：一个正在等待某个条件的线程会一直保持阻塞，直到该条件被另一个线程显式地发出信号为止。

由于操作系统实现中涉及一些微妙之处，条件锁被允许出现虚假的成功返回，即便你的代码实际上并没有向其发出信号。为了避免这些虚假信号带来的问题，你应该始终将一个谓词（predicate）与你的条件锁配合使用。谓词是一种更具体的方式，用来判断你的线程是否可以安全地继续执行。条件只是让你的线程保持休眠，直到发信号的线程能够设置该谓词为止。

以下各节将展示如何在代码中使用条件。

[NSCondition](https://developer.apple.com/documentation/foundation/nscondition) 类提供了与 POSIX 条件相同的语义，但将所需的锁和条件数据结构都封装在了单个对象中。其结果是一个对象，你既可以像 mutex 一样对它加锁，又可以像条件一样在它上面等待。

清单 4-3 展示了一段代码片段，演示了在 `NSCondition` 对象上等待的事件序列。`cocoaCondition` 变量包含一个 `NSCondition` 对象，`timeToDoWork` 变量是一个整数，会在发出该条件的信号之前，立即由另一个线程递增。

__清单 4-3__  使用 Cocoa 条件

```objc
[cocoaCondition lock];
while (timeToDoWork <= 0)
    [cocoaCondition wait];

timeToDoWork--;

// 在这里执行真正的工作。

[cocoaCondition unlock];
```

清单 4-4 展示了用于向该 Cocoa 条件发出信号并递增谓词变量的代码。你应该始终在发出条件信号之前先对其加锁。

__清单 4-4__  向 Cocoa 条件发送信号

```objc
[cocoaCondition lock];
timeToDoWork++;
[cocoaCondition signal];
[cocoaCondition unlock];
```


POSIX 线程条件锁要求同时使用一个条件数据结构和一个 mutex。虽然这两种锁结构是各自独立的，但在运行时，该 mutex 锁与该条件结构是紧密关联的。等待某个信号的线程应该始终一起使用相同的 mutex 锁和条件结构。改变这种配对关系会导致错误。

清单 4-5 展示了一个条件和谓词的基本初始化及使用方式。在初始化条件和 mutex 锁之后，等待线程会进入一个 while 循环，将 `ready_to_go` 变量用作其谓词。只有当谓词被设置、条件随后被发出信号时，等待线程才会被唤醒并开始其工作。

__清单 4-5__  使用 POSIX 条件

```c
pthread_mutex_t mutex;
pthread_cond_t condition;
Boolean     ready_to_go = true;

void MyCondInitFunction()
{
    pthread_mutex_init(&mutex);
    pthread_cond_init(&condition, NULL);
}

void MyWaitOnConditionFunction()
{
    // 锁定该 mutex。
    pthread_mutex_lock(&mutex);

    // 如果谓词已经被设置，就会跳过该 while 循环；
    // 否则，线程会休眠，直到该谓词被设置为止。
    while(ready_to_go == false)
    {
        pthread_cond_wait(&condition, &mutex);
    }

    // 执行工作。（该 mutex 应该保持锁定状态。）

    // 重置该谓词并释放该 mutex。
    ready_to_go = false;
    pthread_mutex_unlock(&mutex);
}
```

发信号的线程既负责设置该谓词，也负责向条件锁发送信号。清单 4-6 展示了实现这一行为的代码。在这个示例中，信号是在该 mutex 内部发出的，以防止在等待该条件的各线程之间出现竞态条件。

__清单 4-6__  向条件锁发送信号

```c
void SignalThreadUsingCondition()
{
    // 此时，应该有工作需要另一个线程去做。
    pthread_mutex_lock(&mutex);
    ready_to_go = true;

    // 向另一个线程发出信号，让它开始工作。
    pthread_cond_signal(&condition);

    pthread_mutex_unlock(&mutex);
}
```

[下一页](Thread%20Safety%20Summary.md)[上一页](Run%20Loops.md)

