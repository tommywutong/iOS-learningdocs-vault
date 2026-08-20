---
title: 多线程编程指南
apple_id: 10000057i
resource_type: Guide
platform: watchOS|tvOS|iOS|macOS
topic: Performance
technology: null
published: '2014-07-15'
source_url: https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/Multithreading/AboutThreads/AboutThreads.html
archived_at: '2026-07-15T07:16:46.743079Z'
---
> 导航：[总目录](../../../README.md) · [文档](../../../_indexes/documentation.md) · [多线程编程指南](Introduction.md)


[下一页](Thread%20Management.md)[上一页](Introduction.md)

# 关于多线程编程

多年来，计算机的最高性能在很大程度上受限于计算机核心那颗单一微处理器的速度。然而，随着单个处理器的速度开始触及其实际极限，芯片制造商转向了多核设计，让计算机有机会同时执行多个任务。尽管 OS X 会尽可能利用这些核心来执行系统相关的任务，但你自己的应用程序也可以通过线程利用这些核心。

线程（thread）是在应用程序内部实现多条执行路径的一种相对轻量级的方式。在系统层面，各个程序并排运行，系统会根据每个程序自身以及其他程序的需求，分配各自的执行时间。然而，在每个程序内部，都存在一个或多个执行线程，它们可以用来同时或近乎同时地执行不同的任务。系统本身实际上会管理这些执行线程，调度它们在可用的核心上运行，并按需抢占式地中断它们，以便让其他线程运行。

从技术角度来看，线程是管理代码执行所需的内核级和应用程序级数据结构的组合。内核级结构负责协调向线程分派事件，以及在某个可用核心上对线程进行抢占式调度。应用程序级结构则包括用于存储函数调用的调用栈，以及应用程序管理和操作线程属性与状态所需的结构。

在非并发的应用程序中，只存在一条执行线程。该线程随应用程序的 `main` 例程开始和结束，并逐一分支到不同的方法或函数，以实现应用程序的整体行为。相比之下，支持并发的应用程序以一条线程开始，并根据需要添加更多线程，以创建额外的执行路径。每条新的路径都有自己独立的自定义起始例程，独立于应用程序 `main` 例程中的代码运行。在应用程序中使用多条线程可以带来两个非常重要的潜在优势：

- 多线程可以提升应用程序在用户感知层面的响应速度。
- 多线程可以提升应用程序在多核系统上的实时性能。

如果你的应用程序只有一条线程，那么这一条线程就必须完成所有工作。它必须响应事件、更新应用程序的窗口，并执行实现应用程序行为所需的全部计算。只有一条线程的问题在于，它一次只能做一件事。那么，当某个计算需要很长时间才能完成时会发生什么呢？在你的代码忙于计算所需的数值时，应用程序就会停止响应用户事件、停止更新窗口。如果这种情况持续足够长的时间，用户可能会认为你的应用程序已经卡死，并试图强行退出它。然而，如果你把自定义计算转移到一条独立的线程上，应用程序的主线程就可以更及时地响应用户交互。

如今多核计算机已经十分普遍，线程为某些类型的应用程序提供了一种提升性能的方式。执行不同任务的线程可以在不同的处理器核心上同时进行，从而使应用程序有可能在给定的时间内完成更多的工作。

当然，线程并不是解决应用程序性能问题的万能药。线程带来好处的同时，也带来了潜在的问题。在应用程序中拥有多条执行路径，会给你的代码增加相当程度的复杂性。每条线程都必须与其他线程协调自己的行为，以防止破坏应用程序的状态信息。由于同一个应用程序内的所有线程共享同一块内存空间，它们可以访问所有相同的数据结构。如果两条线程同时尝试操作同一个数据结构，其中一条线程的更改可能会覆盖另一条线程的更改，从而导致最终的数据结构被破坏。即使已经采取了适当的保护措施，你仍然需要提防编译器优化给你的代码引入的细微（乃至不那么细微的）错误。

在深入讨论线程及其配套技术之前，有必要先定义一些基本术语。

如果你熟悉 UNIX 系统，可能会发现本文档对“任务”一词的使用方式有所不同。在 UNIX 系统中，“任务”一词有时用于指代一个正在运行的进程。

本文档采用以下术语：

- 术语 _线程（thread）_ 用于指代代码的一条独立执行路径。
- 术语 _进程（process）_ 用于指代一个正在运行的可执行文件，其中可以包含多个线程。
- 术语 _任务（task）_ 用于指代需要执行的工作这一抽象概念。

自行创建线程的问题之一在于，它会给你的代码增加不确定性。线程是在应用程序中支持并发的一种相对底层且复杂的方式。如果你没有完全理解自己设计选择所带来的影响，就很容易遇到同步或时序方面的问题，其严重程度从细微的行为变化，到应用程序崩溃、用户数据损坏，不一而足。

另一个需要考虑的因素是，你是否真的需要线程或并发。线程解决的是一个特定问题：如何在同一个进程内并发地执行多条代码路径。不过，在某些情况下，你要做的工作量可能并不值得引入并发。线程会给你的进程带来大量的开销，无论是在内存消耗还是 CPU 时间方面都是如此。你可能会发现，对于预期的任务来说，这种开销过大，或者存在其他更容易实现的选择。

表 1-1 列出了一些线程的替代方案。该表既包括可以替代线程的技术（例如操作对象和 GCD），也包括那些旨在高效利用你已有的单条线程的替代方案。

__表 1-1__  线程的替代技术

| 技术 | 说明 |
| --- | --- |
| 操作对象 | 操作对象是在 OS X v10.5 中引入的，它是对通常会在次线程上执行的任务的一层封装。这层封装隐藏了执行任务时与线程管理相关的方面，让你可以专注于任务本身。你通常会将这些对象与操作队列对象配合使用，操作队列对象实际负责在一条或多条线程上管理操作对象的执行。  有关如何使用操作对象的更多信息，请参阅 _[并发编程指南](../../General/Concurrency%20Programming%20Guide/Introduction.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4daojr)_。 |
| Grand Central Dispatch（GCD） | Grand Central Dispatch 是在 Mac OS X v10.6 中引入的，它是线程的另一种替代方案，让你可以专注于需要执行的任务，而不必操心线程管理。使用 GCD 时，你只需定义想要执行的任务，并将其加入一个工作队列，由工作队列负责在合适的线程上调度你的任务。工作队列会考虑可用核心的数量和当前负载，从而比你自己使用线程实现的调度更高效地执行任务。  有关如何使用 GCD 和工作队列的信息，请参阅 _[并发编程指南](../../General/Concurrency%20Programming%20Guide/Introduction.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4daojr)_ |
| 空闲时间通知 | 对于相对简短且优先级很低的任务，空闲时间通知可以让你在应用程序不那么繁忙的时候执行该任务。Cocoa 通过 [NSNotificationQueue](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSNotificationQueue/Description.html#//apple_ref/occ/cl/NSNotificationQueue) 对象提供了对空闲时间通知的支持。要请求一个空闲时间通知，可以使用 [NSPostWhenIdle](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/TypesAndConstants/FoundationTypesConstants/Description.html#//apple_ref/c/econst/NSPostWhenIdle) 选项，向默认的 `NSNotificationQueue` 对象发布一条通知。该队列会将你的通知对象的投递延迟到运行循环进入空闲状态时。更多信息请参阅 _[通知编程主题](../Notification%20Programming%20Topics/Introduction.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgeydambqga2dg2i)_。 |
| 异步函数 | 系统接口中包含许多异步函数，可以自动为你提供并发能力。这些 API 可能会使用系统守护进程和进程，也可能创建自定义线程来执行任务并将结果返回给你。（具体实现方式其实无关紧要，因为它与你的代码是相互隔离的。）在设计应用程序时，应留意那些提供异步行为的函数，并考虑使用它们，而不是在自定义线程上使用等效的同步函数。 |
| 定时器 | 你可以在应用程序的主线程上使用定时器来执行一些周期性任务，这些任务太过琐碎，不值得为其单独使用一条线程，但仍需要按固定间隔进行处理。有关定时器的信息，请参阅[定时器源](Run%20Loops.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgeydambqga2to2jninedcnrnknltemi)。 |
| 独立进程 | 尽管比线程更重量级，但在任务只与你的应用程序有些许关联的情况下，创建一个独立的进程可能会很有用。如果某项任务需要大量内存，或者必须以 root 权限执行，你可能就需要使用一个进程。例如，你可以使用一个 64 位服务器进程来计算一个庞大的数据集，同时让 32 位的应用程序向用户展示结果。 |

如果你已经有使用线程的现有代码，OS X 和 iOS 提供了多种技术，可用于在你的应用程序中创建线程。此外，这两个系统还为管理和同步这些线程上需要完成的工作提供了支持。以下各节将介绍在 OS X 和 iOS 中使用线程时，你需要了解的一些关键技术。

虽然线程底层的实现机制是 Mach 线程，但你很少（甚至从不）需要在 Mach 层面处理线程。相反，你通常会使用更为便捷的 POSIX API 或其某个衍生形式。不过，Mach 实现确实提供了所有线程的基本特性，包括抢占式执行模型，以及让各线程相互独立进行调度的能力。

清单 2-2 列出了可以在应用程序中使用的多线程技术。

__表 1-2__  线程技术

| 技术 | 说明 |
| --- | --- |
| Cocoa 线程 | Cocoa 使用 [NSThread](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSThread/Description.html#//apple_ref/occ/cl/NSThread) 类来实现线程。Cocoa 还在 [NSObject](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSObject/Description.html#//apple_ref/occ/cl/NSObject) 上提供了一些方法，用于生成新线程，以及在已经在运行的线程上执行代码。更多信息请参阅[使用 NSThread](Thread%20Management.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgeydambqga2to2jninedcnjnknltcmi)和[使用 NSObject 生成一条线程](Thread%20Management.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgeydambqga2to2jninedcnjnknltcmy)。 |
| POSIX 线程 | POSIX 线程提供了一套基于 C 的线程创建接口。如果你编写的不是 Cocoa 应用程序，这是创建线程的最佳选择。POSIX 接口使用起来相对简单，并为配置线程提供了充分的灵活性。更多信息请参阅[使用 POSIX 线程](Thread%20Management.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgeydambqga2to2jninedcnjnknltcmq) |
| Multiprocessing Services | Multiprocessing Services 是一套遗留的、基于 C 的接口，供从旧版本 Mac OS 迁移过来的应用程序使用。该技术仅在 OS X 中可用，任何新开发工作都应避免使用它。你应当改用 `NSThread` 类或 POSIX 线程。如果你需要了解关于这项技术的更多信息，请参阅 _[Multiprocessing Services 编程指南](../../Carbon/Multiprocessing%20Services%20Programming%20Guide/Introduction%20to%20Multiprocessing%20Services%20Programming%20Guide.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaydqnjt)_。 |

在应用程序层面，所有线程的行为方式与其他平台上基本相同。线程启动后，会处于三种主要状态之一：运行、就绪或阻塞。如果一条线程当前没有在运行，那么它要么是被阻塞、正在等待输入，要么是已经就绪但尚未被调度运行。线程会在这些状态之间来回切换，直到它最终退出并进入终止状态。

创建一条新线程时，你必须为该线程指定一个入口点函数（对于 Cocoa 线程而言，则是入口点方法）。这个入口点函数就是你想要在该线程上运行的代码。当该函数返回时，或者当你显式终止该线程时，这条线程就会永久停止运行，并被系统回收。由于创建线程在内存和时间上的开销相对较高，因此建议你的入口点函数完成相当数量的工作，或者建立一个运行循环，以便反复执行工作。

有关可用的多线程技术及其使用方法的更多信息，请参阅[线程管理](Thread%20Management.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgeydambqga2to2jninedcnjnknlte)。

运行循环（run loop）是一种用于管理某条线程上异步到达的事件的基础设施。运行循环的工作方式是监视该线程的一个或多个事件源。当事件到达时，系统会唤醒该线程，并将事件分派给运行循环，再由运行循环将事件分派给你指定的处理程序。如果没有事件出现或需要处理，运行循环就会让线程进入休眠。

你创建的线程并不要求必须使用运行循环，但这样做可以为用户带来更好的体验。运行循环使得创建长期存在、且只占用极少资源的线程成为可能。由于运行循环会在无事可做时让其线程进入休眠，因此它免除了轮询的需要——轮询既浪费 CPU 周期，又会妨碍处理器本身进入休眠、节省电能。

要配置一个运行循环，你只需启动线程、获取运行循环对象的引用、安装事件处理程序，然后让运行循环运行起来即可。OS X 提供的基础设施会自动为你配置主线程的运行循环。但是，如果你打算创建长期存在的次线程，就必须自己为这些线程配置运行循环。

有关运行循环的详细信息及使用示例，请参阅[运行循环](Run%20Loops.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgeydambqga2to2jninedcnrnknltc)。

多线程编程的风险之一，是多条线程之间的资源争用。如果多条线程试图同时使用或修改同一个资源，就可能出现问题。缓解这一问题的一种方法，是彻底消除共享资源，确保每条线程都有自己专属的一套资源可供操作。不过，当维护完全独立的资源不可行时，你可能就必须使用锁、条件、原子操作等技术来同步对资源的访问。

锁（lock）为只能由一条线程一次执行的代码提供了一种简单粗暴的保护形式。最常见的锁类型是互斥锁，也称为 _mutex_。当一条线程试图获取一个当前被另一条线程持有的互斥锁时，它会阻塞，直到该锁被另一条线程释放为止。多个系统框架都提供了对互斥锁的支持，尽管它们都基于相同的底层技术。此外，Cocoa 还提供了互斥锁的若干变体，以支持不同类型的行为，例如递归。有关可用锁类型的更多信息，请参阅[锁](Synchronization.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgeydambqga2to2jninedqljrgi3dgmrq)。

除了锁之外，系统还提供了对条件（condition）的支持，用以确保应用程序内任务的正确执行顺序。条件充当一个“看门人”的角色，在其所代表的条件变为真之前，会一直阻塞给定的线程。一旦条件成立，它就会释放该线程，让其得以继续执行。POSIX 层和 Foundation 框架都直接提供了对条件的支持。（如果你使用操作对象，可以通过配置操作对象之间的依赖关系来对任务的执行进行排序，这与条件所提供的行为非常相似。）

虽然锁和条件在并发设计中非常常见，但原子操作是保护和同步数据访问的另一种方式。在可以对标量数据类型执行数学或逻辑运算的情况下，原子操作提供了一种比锁更轻量级的替代方案。原子操作利用特殊的硬件指令，确保对一个变量的修改在其他线程有机会访问它之前就已经完成。

有关可用同步工具的更多信息，请参阅[同步工具](Synchronization.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgeydambqga2to2jninedqljrgi2dqobx)。

虽然良好的设计会尽量减少所需的通信量，但在某个时刻，线程之间的通信终究是必要的。（线程的职责是为你的应用程序完成工作，但如果这项工作的结果从未被使用，那它又有什么意义呢？）线程可能需要处理新的任务请求，或者向应用程序的主线程汇报其进度。在这些情况下，你需要一种方法把信息从一条线程传递到另一条线程。幸运的是，由于各线程共享同一个进程空间，你可以有很多种通信方式可供选择。

线程之间存在多种通信方式，各有优劣。配置线程本地存储列出了你可以在 OS X 中使用的最常见通信机制。（除消息队列和 Cocoa 分布式对象外，这些技术在 iOS 中也同样可用。）该表中的技术按复杂程度递增的顺序列出。

__表 1-3__  通信机制

| 机制 | 说明 |
| --- | --- |
| 直接消息传递 | Cocoa 应用程序支持直接在其他线程上执行选择器的能力。这意味着一条线程实际上可以在任何其他线程上执行某个方法。由于这类消息是在目标线程的上下文中执行的，因此以这种方式发送的消息会在该线程上自动序列化。有关输入源的信息，请参阅 [Cocoa 选择器执行源](Run%20Loops.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgeydambqga2to2jninedcnrnknltina)。 |
| 全局变量、共享内存与对象 | 在两条线程之间传递信息的另一种简单方式，是使用全局变量、共享对象或共享内存块。尽管共享变量快速且简单，但它们也比直接消息传递更脆弱。共享变量必须用锁或其他同步机制加以仔细保护，以确保代码的正确性。如果不这样做，可能会导致竞争条件、数据损坏或程序崩溃。 |
| 条件 | 条件是一种同步工具，你可以用它来控制线程在何时执行特定的一段代码。你可以把条件想象成看门人，只有在所声明的条件得到满足时，才会放行让线程运行。有关如何使用条件的信息，请参阅[使用条件](Synchronization.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgeydambqga2to2jninedqlktk42a)。 |
| 运行循环源 | 自定义运行循环源是你设置在某条线程上、用于接收特定于应用程序的消息的一种源。由于是事件驱动的，运行循环源会在无事可做时自动让线程进入休眠，从而提升线程的效率。有关运行循环和运行循环源的信息，请参阅[运行循环](Run%20Loops.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgeydambqga2to2jninedcnrnknltc)。 |
| 端口和套接字 | 基于端口的通信是两条线程之间进行通信的一种更为精细的方式，同时也是一种非常可靠的技术。更重要的是，端口和套接字还可以用来与其他实体（例如其他进程和服务）进行通信。出于效率考虑，端口是使用运行循环源来实现的，因此当端口上没有数据等待处理时，你的线程就会进入休眠。有关运行循环以及基于端口的输入源的信息，请参阅[运行循环](Run%20Loops.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgeydambqga2to2jninedcnrnknltc)。 |
| 消息队列 | 遗留的 Multiprocessing Services 定义了一种先进先出（FIFO）队列抽象，用于管理传入和传出的数据。尽管消息队列简单方便，但其效率不如其他一些通信技术。有关如何使用消息队列的更多信息，请参阅 _[Multiprocessing Services 编程指南](../../Carbon/Multiprocessing%20Services%20Programming%20Guide/Introduction%20to%20Multiprocessing%20Services%20Programming%20Guide.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaydqnjt)_。 |
| Cocoa 分布式对象 | 分布式对象是一项 Cocoa 技术，为基于端口的通信提供了一种高层次的实现。虽然理论上可以将这项技术用于线程间通信，但强烈不建议这样做，因为它会带来大量开销。分布式对象更适合用于与其他进程通信的场景，因为在那种场景下，进程之间的开销本来就已经很高。更多信息请参阅 _[分布式对象编程主题](../Distributed%20Objects%20Programming%20Topics/Introduction%20to%20Distributed%20Objects.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgeydambqgeyde2i)_。 |

以下各节提供了一些准则，帮助你以确保代码正确性的方式实现线程。其中一些准则还就如何让你自己的多线程代码获得更好的性能提供了建议。与任何性能建议一样，你都应当在对代码做出更改之前、期间和之后，持续收集相关的性能统计数据。

手动编写线程创建代码既繁琐又容易出错，你应当尽可能避免这样做。OS X 和 iOS 通过其他 API 为并发提供了隐式支持。与其自己创建线程，不如考虑使用异步 API、GCD 或操作对象来完成这项工作。这些技术会在幕后替你完成与线程相关的工作，并且保证能正确完成。此外，GCD 和操作对象等技术在设计上会根据当前系统负载调整活跃线程的数量，从而比你自己编写的代码更高效地管理线程。有关 GCD 和操作对象的更多信息，请参阅 _[并发编程指南](../../General/Concurrency%20Programming%20Guide/Introduction.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4daojr)_。

如果你决定手动创建和管理线程，请记住，线程会消耗宝贵的系统资源。你应当尽力确保分配给线程的任何任务都具有合理的持续时间并且富有成效。与此同时，对于那些大部分时间都处于空闲状态的线程，你也不必犹豫将其终止。线程会占用不容忽视的内存量，其中一部分还是常驻内存，因此释放一条空闲线程不仅有助于降低应用程序的内存占用，还能为其他系统进程释放出更多的物理内存可供使用。

避免与线程相关的资源冲突，最简单也最容易的方法，就是让程序中的每条线程都拥有它所需数据的独立副本。当你尽量减少各线程之间的通信和资源争用时，并行代码的效果最好。

创建一个多线程应用程序并不容易。即使你非常谨慎，在代码中所有恰当的关键点上都对共享数据结构加了锁，你的代码在语义上仍然可能是不安全的。举例来说，如果你的代码期望共享数据结构按特定顺序被修改，就可能出问题。为了弥补这一点而将代码改为基于事务的模型，随后可能会抵消拥有多条线程所带来的性能优势。从一开始就消除资源争用，往往能带来更简单的设计，同时获得出色的性能。

如果你的应用程序具有图形用户界面，建议你在应用程序的主线程上接收用户相关事件并发起界面更新。这种做法有助于避免处理用户事件和绘制窗口内容时所涉及的同步问题。一些框架（例如 Cocoa）通常要求采用这种做法，但即使对于不作此要求的框架，把这类行为保留在主线程上也有简化用户界面管理逻辑的好处。

当然也存在一些值得注意的例外情况，在这些情况下从其他线程执行图形操作反而更有利。例如，你可以使用次线程来创建和处理图像，并执行其他与图像相关的计算。将这些操作放在次线程上执行可以大幅提升性能。不过，如果你不确定某个特定的图形操作是否适合这样做，那就打算在主线程上执行它。

有关 Cocoa 线程安全的更多信息，请参阅[线程安全总结](Thread%20Safety%20Summary.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgeydambqga2to2jninedcmrnknltc)。有关 Cocoa 绘图的更多信息，请参阅 _[Cocoa 绘图指南](../Cocoa%20Drawing%20Guide/Introduction%20to%20Cocoa%20Drawing%20Guide.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgazteojq)_。

一个进程会持续运行，直到所有非分离（non-detached）线程都已退出为止。默认情况下，只有应用程序的主线程会被创建为非分离线程，不过你也可以用同样的方式创建其他线程。当用户退出一个应用程序时，通常认为立即终止所有分离线程是恰当的行为，因为分离线程所完成的工作被视为可有可无的。但是，如果你的应用程序正在使用后台线程将数据保存到磁盘，或者执行其他关键工作，你可能就需要将这些线程创建为非分离线程，以防止应用程序退出时丢失数据。

将线程创建为非分离（也称为可合并，joinable）状态，需要你额外做一些工作。由于大多数高层次的线程技术默认不会创建可合并线程，你可能需要使用 POSIX API 来创建线程。此外，你还必须在应用程序的主线程中添加代码，以便在这些非分离线程最终退出时与它们进行合并（join）。有关如何创建可合并线程的信息，请参阅[设置线程的分离状态](Thread%20Management.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgeydambqga2to2jninedcnjnknltg)。

如果你正在编写一个 Cocoa 应用程序，还可以使用 [applicationShouldTerminate:](https://developer.apple.com/documentation/appkit/nsapplicationdelegate/1428642-applicationshouldterminate) 委托方法，将应用程序的终止推迟到之后的某个时间，或者干脆取消终止。在推迟终止时，你的应用程序需要等到所有关键线程都完成任务之后，再调用 [replyToApplicationShouldTerminate:](https://developer.apple.com/documentation/appkit/nsapplication/1428594-reply) 方法。有关这些方法的更多信息，请参阅 _[NSApplication Class Reference](https://developer.apple.com/documentation/appkit/nsapplication)_。

异常处理机制依赖当前的调用栈，在异常被抛出时执行任何必要的清理工作。由于每条线程都拥有自己的调用栈，因此每条线程都要负责捕获自己的异常。在次线程中未能捕获异常，与在主线程中未能捕获异常的后果是一样的：拥有该线程的进程会被终止。你无法把一个未被捕获的异常抛给另一条线程去处理。

如果你需要将当前线程中出现的异常情况通知给另一条线程（例如主线程），应当先捕获该异常，然后简单地向另一条线程发送一条消息，说明所发生的情况。根据你的模型以及你想要实现的目标，捕获到异常的那条线程随后可以继续处理（如果可行的话）、等待指示，或者干脆退出。

在某些情况下，系统可能会自动为你创建一个异常处理程序。例如，Objective-C 中的 `@synchronized` 指令就包含一个隐式的异常处理程序。

让一条线程退出的最佳方式，是让它自然地走到其主入口点例程的末尾。虽然存在一些可以立即终止线程的函数，但这些函数应当只作为最后的手段来使用。在一条线程到达其自然终点之前就将其终止，会导致该线程无法完成自我清理。如果该线程已经分配了内存、打开了文件，或者获取了其他类型的资源，你的代码可能无法回收这些资源，从而导致内存泄漏或其他潜在问题。

有关退出线程的正确方式的更多信息，请参阅[终止一条线程](Thread%20Management.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgeydambqga2to2jninedcnjnknltcma)。

尽管应用程序开发者可以控制自己的应用程序是否以多线程方式执行，但库的开发者却做不到这一点。在开发库时，你必须假设调用你的库的应用程序是多线程的，或者随时可能切换为多线程。因此，你应当始终对代码的关键区段使用锁。

对于库的开发者来说，只有在应用程序变为多线程时才创建锁，并不是明智的做法。如果你需要在某个时刻对代码加锁，应当在库的使用早期就创建锁对象，最好是在某种用于初始化库的显式调用中完成。虽然你也可以使用静态库初始化函数来创建这类锁，但应尽量只在别无他法时才这样做。执行初始化函数会增加加载库所需的时间，并可能对性能产生不利影响。

如果你正在开发一个 Cocoa 库，并且希望在应用程序变为多线程时收到通知，可以注册为 [NSWillBecomeMultiThreadedNotification](https://developer.apple.com/documentation/foundation/nsnotification/name/1417567-nswillbecomemultithreaded) 的观察者。不过，你不应该依赖于一定会收到这个通知，因为它有可能在你的库代码被调用之前就已经被派发了。

[下一页](Thread%20Management.md)[上一页](Introduction.md)

