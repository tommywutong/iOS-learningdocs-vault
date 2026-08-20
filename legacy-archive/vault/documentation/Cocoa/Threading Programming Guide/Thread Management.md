---
title: 多线程编程指南
apple_id: 10000057i
resource_type: Guide
platform: watchOS|tvOS|iOS|macOS
topic: Performance
technology: null
published: '2014-07-15'
source_url: https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/Multithreading/CreatingThreads/CreatingThreads.html
archived_at: '2026-07-15T07:16:46.754022Z'
---
> 导航：[总目录](../../../README.md) · [文档](../../../_indexes/documentation.md) · [多线程编程指南](Introduction.md)


[下一页](Run%20Loops.md)[上一页](About%20Threaded%20Programming.md)

# 线程管理

OS X 或 iOS 中的每个进程（应用程序）都由一个或多个线程组成，每个线程代表贯穿应用程序代码的单条执行路径。每个应用程序都从单个线程开始运行，该线程执行应用程序的 `main` 函数。应用程序可以派生额外的线程，每个线程执行特定函数的代码。

当应用程序派生一个新线程时，该线程会成为应用程序进程空间内的一个独立实体。每个线程都有自己的执行栈，并由内核单独调度运行。线程可以与其他线程和其他进程通信、执行 I/O 操作，以及完成你需要它做的其他任何事情。不过，由于它们处于同一个进程空间内，一个应用程序中的所有线程共享同一个虚拟内存空间，并拥有与进程本身相同的访问权限。

本章概述了 OS X 和 iOS 中可用的线程技术，并给出了在应用程序中使用这些技术的示例。

在内存使用和性能方面，多线程会给你的程序（以及系统）带来实实在在的开销。每个线程都需要在内核内存空间和程序内存空间中分配内存。用于管理线程并协调其调度的核心结构以固定内存（wired memory）的形式存储在内核中。线程的栈空间和线程私有数据则存储在程序的内存空间中。这些结构大多是在你首次创建线程时创建并初始化的——由于需要与内核进行交互，这个过程的开销可能相对较大。

表 2-1 量化了在应用程序中创建一个新的用户级线程所涉及的大致开销。其中一些开销是可配置的，例如为次要线程分配的栈空间大小。创建线程的时间开销只是一个粗略的估算值，仅应用于彼此之间的相对比较。线程创建耗时会因处理器负载、计算机速度以及可用的系统和程序内存量的不同而有很大差异。

__表 2-1__  线程创建开销

| 项目 | 大致开销 | 说明 |
| --- | --- | --- |
| 内核数据结构 | 大约 1 KB | 这部分内存用于存储线程数据结构和属性，其中大部分以固定内存的形式分配，因此不能被分页到磁盘。 |
| 栈空间 | 512 KB（次要线程）  8 MB（OS X 主线程）  1 MB（iOS 主线程） | 次要线程允许的最小栈大小为 16 KB，且栈大小必须是 4 KB 的倍数。这部分内存空间会在线程创建时预留在你的进程空间中，但与该内存关联的实际页面要到需要时才会创建。  |
| 创建耗时 | 大约 90 微秒 | 该值反映的是从最初调用创建线程到线程的入口点例程开始执行之间的时间。这些数值是通过分析在一台配备 2 GHz Core Duo 处理器、1 GB 内存、运行 OS X v10.5 的基于 Intel 的 iMac 上创建线程期间产生的平均值和中位数得出的。 |

编写多线程代码时还需要考虑的另一项开销是开发成本。设计一个多线程应用程序有时需要从根本上改变你组织应用程序数据结构的方式。做出这些改变可能是为了避免使用同步机制——如果应用程序设计不当，同步本身就可能带来巨大的性能损失。设计这些数据结构以及调试多线程代码中的问题，都会增加开发一个多线程应用程序所需的时间。然而，如果你的线程把太多时间花在等待锁或无所事事上，回避这些开发成本反而会在运行时造成更大的问题。

创建底层线程相对简单。在所有情况下，你都必须有一个函数或方法作为线程的主入口点，并且必须使用可用的线程例程之一来启动线程。以下各节展示了几种常用线程技术的基本创建过程。使用这些技术创建的线程会继承一组默认属性，具体取决于你使用的技术。关于如何配置线程的信息，参见 [配置线程属性](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgeydambqga2to2jninedcnjnknltq)。

使用 [NSThread](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSThread/Description.html#//apple_ref/occ/cl/NSThread) 类创建线程有两种方式：

- 使用 [detachNewThreadSelector:toTarget:withObject:](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSThread/Description.html#//apple_ref/occ/clm/NSThread/detachNewThreadSelector:toTarget:withObject:) 类方法来派生新线程。
- 创建一个新的 `NSThread` 对象并调用其 `start` 方法。（仅在 iOS 和 OS X v10.5 及更高版本中支持。）

这两种方式都会在你的应用程序中创建一个分离线程。分离线程意味着线程退出时，其资源会由系统自动回收，这也意味着你的代码之后不必显式地与该线程进行合并（join）。

由于 `detachNewThreadSelector:toTarget:withObject:` 方法在所有版本的 OS X 中都受支持，因此在使用线程的现有 Cocoa 应用程序中经常能看到它的身影。要分离出一个新线程，你只需提供想用作线程入口点的方法名称（以选择器形式指定）、定义该方法的对象，以及启动时想传给线程的任何数据。下面的示例展示了对该方法的一次基本调用，它使用当前对象的一个自定义方法来派生线程。

```objc
[NSThread detachNewThreadSelector:@selector(myThreadMainMethod:) toTarget:self withObject:nil];
```

在 OS X v10.5 之前，`NSThread` 类主要用于派生线程。虽然你可以获取一个 `NSThread` 对象并访问部分线程属性，但只能在线程运行起来之后，从线程自身内部这样做。在 OS X v10.5 中，新增了对创建 `NSThread` 对象而不立即派生对应新线程的支持。（iOS 中同样提供此支持。）这项支持使得在启动线程之前获取和设置各种线程属性成为可能，也使得之后可以用该线程对象来引用正在运行的线程。

在 OS X v10.5 及更高版本中，初始化 `NSThread` 对象的简单方式是使用 [initWithTarget:selector:object:](https://developer.apple.com/documentation/foundation/nsthread/1414773-initwithtarget) 方法。该方法接受与 `detachNewThreadSelector:toTarget:withObject:` 方法完全相同的信息，并用它来初始化一个新的 `NSThread` 实例。不过，它并不会启动线程。要启动线程，你需要显式调用线程对象的 `start` 方法，如下例所示：

```objc
NSThread* myThread = [[NSThread alloc] initWithTarget:self
                                        selector:@selector(myThreadMainMethod:)
                                        object:nil];
[myThread start];  // 真正创建线程
```

如果你有一个其线程当前正在运行的 `NSThread` 对象，向该线程发送消息的一种方式是使用应用程序中几乎任何对象都具备的 [performSelector:onThread:withObject:waitUntilDone:](https://developer.apple.com/documentation/objectivec/nsobject/1414476-performselector) 方法。在（主线程以外的）线程上执行选择器的支持是在 OS X v10.5 中引入的，是线程间通信的一种便捷方式。（iOS 中同样提供此支持。）使用这种方式发送的消息会由另一个线程作为其正常运行循环处理的一部分直接执行。（当然，这也意味着目标线程必须正在其运行循环中运行；参见 [运行循环](Run%20Loops.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgeydambqga2to2jninedcnrnknltc)。）以这种方式通信时你可能仍然需要某种形式的同步，但这比在线程之间搭建通信端口要简单。

关于其他线程通信方式的列表，参见 [设置线程的分离状态](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgeydambqga2to2jninedcnjnknltg)。

OS X 和 iOS 提供了基于 C 的支持，可以使用 POSIX 线程 API 来创建线程。这项技术实际上可以用于任何类型的应用程序（包括 Cocoa 和 Cocoa Touch 应用程序），如果你的软件要面向多个平台开发，使用它可能会更方便。用来创建线程的 POSIX 例程恰如其名，叫做 `pthread_create`。

清单 2-1 展示了使用 POSIX 调用创建线程的两个自定义函数。`LaunchThread` 函数创建一个新线程，其主例程在 `PosixThreadMainRoutine` 函数中实现。由于 POSIX 默认创建的线程是可结合的，这个示例修改了线程属性以创建一个分离线程。将线程标记为分离状态，可以让系统在线程退出时立即回收其资源。

__清单 2-1__  用 C 语言创建线程

```c
#include <assert.h>
#include <pthread.h>

void* PosixThreadMainRoutine(void* data)
{
    // 在这里做一些工作。

    return NULL;
}

void LaunchThread()
{
    // 使用 POSIX 例程创建线程。
    pthread_attr_t  attr;
    pthread_t       posixThreadID;
    int             returnVal;

    returnVal = pthread_attr_init(&attr);
    assert(!returnVal);
    returnVal = pthread_attr_setdetachstate(&attr, PTHREAD_CREATE_DETACHED);
    assert(!returnVal);

    int     threadError = pthread_create(&posixThreadID, &attr, &PosixThreadMainRoutine, NULL);

    returnVal = pthread_attr_destroy(&attr);
    assert(!returnVal);
    if (threadError != 0)
    {
         // 报告一个错误。
    }
}
```

如果你把前面清单中的代码添加到某个源文件中并调用 `LaunchThread` 函数，就会在应用程序中创建一个新的分离线程。当然，用这段代码创建出来的新线程并不会做任何有用的事情——线程启动后几乎立即就会退出。要让事情变得更有意思，你需要在 `PosixThreadMainRoutine` 函数中添加代码来完成一些实际工作。为了确保线程知道要做什么工作，你可以在创建时向它传递一个指向某些数据的指针，将这个指针作为 `pthread_create` 函数的最后一个参数传入。

要把新创建线程中的信息传回应用程序的主线程，你需要在目标线程之间建立一条通信路径。对于基于 C 的应用程序，线程间通信有几种方式，包括使用端口、条件变量或共享内存。对于长期存在的线程，你几乎总是应该建立某种线程间通信机制，让应用程序的主线程能够检查该线程的状态，或者在应用程序退出时干净地将其关闭。

关于 POSIX 线程函数的更多信息，参见 [pthread](https://developer.apple.com/library/archive/documentation/System/Conceptual/ManPages_iPhoneOS/man3/pthread.3.html#//apple_ref/doc/man/3/pthread) man page。

在 iOS 和 OS X v10.5 及更高版本中，所有对象都具备派生新线程并用它执行自身某个方法的能力。[performSelectorInBackground:withObject:](https://developer.apple.com/documentation/objectivec/nsobject/1412390-performselector) 方法会创建一个新的分离线程，并将指定的方法用作新线程的入口点。例如，假设你有某个对象（用变量 `myObj` 表示），该对象有一个名为 `doSomething` 的方法，你想在后台线程中运行它，就可以用下面的代码来实现：

```objc
[myObj performSelectorInBackground:@selector(doSomething) withObject:nil];
```

调用这个方法的效果，等同于以当前对象、选择器和参数对象作为参数，调用 [NSThread](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSThread/Description.html#//apple_ref/occ/cl/NSThread) 的 [detachNewThreadSelector:toTarget:withObject:](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSThread/Description.html#//apple_ref/occ/clm/NSThread/detachNewThreadSelector:toTarget:withObject:) 方法。新线程会立即使用默认配置派生并开始运行。在选择器内部，你必须像对待任何线程一样配置该线程。例如，你需要设置一个自动释放池（如果没有使用垃圾回收的话），并且如果打算使用运行循环，还需要对其进行配置。关于如何配置新线程的信息，参见 [配置线程属性](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgeydambqga2to2jninedcnjnknltq)。

虽然 [NSThread](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSThread/Description.html#//apple_ref/occ/cl/NSThread) 类是 Cocoa 应用程序中创建线程的主要接口，但如果使用 POSIX 线程对你来说更方便，你完全可以改用它。例如，如果你已经有使用 POSIX 线程的代码，又不想重写它，就可能会选择使用 POSIX 线程。如果你确实打算在 Cocoa 应用程序中使用 POSIX 线程，仍然应当了解 Cocoa 与线程之间的相互影响，并遵循以下各节中的准则。

对于多线程应用程序，Cocoa 框架会使用锁和其他形式的内部同步机制来确保其行为正确。不过，为了避免这些锁在单线程情况下拖累性能，Cocoa 在应用程序使用 [NSThread](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSThread/Description.html#//apple_ref/occ/cl/NSThread) 类派生出第一个新线程之前，并不会创建这些锁。如果你只使用 POSIX 线程例程来派生线程，Cocoa 就不会收到它据以得知应用程序已经变为多线程的通知。一旦发生这种情况，涉及 Cocoa 框架的操作可能会使你的应用程序变得不稳定甚至崩溃。

要让 Cocoa 知道你打算使用多个线程，你只需使用 `NSThread` 类派生一个线程，并让该线程立即退出即可。线程的入口点不需要做任何事情，仅仅是用 `NSThread` 派生一个线程这个动作本身，就足以确保 Cocoa 框架所需的锁被建立起来。

如果你不确定 Cocoa 是否认为你的应用程序是多线程的，可以使用 `NSThread` 的 [isMultiThreaded](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSThread/Description.html#//apple_ref/occ/clm/NSThread/isMultiThreaded) 方法来检查。

在同一个应用程序中混用 POSIX 锁和 Cocoa 锁是安全的。Cocoa 的锁对象和条件对象本质上只是对 POSIX 互斥锁和条件变量的封装。不过，对于给定的一把锁，你必须始终使用同一种接口来创建和操作它。换句话说，你不能用 Cocoa 的 [NSLock](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSLock/Description.html#//apple_ref/occ/cl/NSLock) 对象去操作一个你用 [pthread_mutex_init](https://developer.apple.com/library/archive/documentation/System/Conceptual/ManPages_iPhoneOS/man3/pthread_mutex_init.3.html#//apple_ref/doc/man/3/pthread_mutex_init) 函数创建的互斥锁，反之亦然。

创建线程之后（有时是之前），你可能想要配置线程环境的不同部分。以下各节介绍了你可以做出的一些改动，以及适合进行这些改动的时机。

对于你创建的每个新线程，系统都会在你的进程空间中分配一定数量的内存，用作该线程的栈。栈用于管理栈帧，线程的任何局部变量也都声明在其中。为线程分配的内存量列在 [线程开销](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgeydambqga2to2jninedcnjnknlto) 中。

如果你想改变某个线程的栈大小，必须在创建该线程之前完成设置。所有线程技术都提供了某种设置栈大小的方式，不过使用 [NSThread](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSThread/Description.html#//apple_ref/occ/cl/NSThread) 设置栈大小仅在 iOS 和 OS X v10.5 及更高版本中可用。表 2-2 列出了各项技术对应的不同选项。

__表 2-2__  设置线程的栈大小

| 技术 | 选项 |
| --- | --- |
| Cocoa | 在 iOS 和 OS X v10.5 及更高版本中，分配并初始化一个 `NSThread` 对象（不要使用 [detachNewThreadSelector:toTarget:withObject:](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSThread/Description.html#//apple_ref/occ/clm/NSThread/detachNewThreadSelector:toTarget:withObject:) 方法）。在调用线程对象的 `start` 方法之前，使用 [setStackSize:](https://developer.apple.com/documentation/foundation/nsthread/1415190-stacksize) 方法指定新的栈大小。 |
| POSIX | 创建一个新的 `pthread_attr_t` 结构，并使用 `pthread_attr_setstacksize` 函数更改默认栈大小。创建线程时，将该属性传递给 `pthread_create` 函数。 |
| Multiprocessing Services | 创建线程时，将合适的栈大小值传递给 [MPCreateTask](https://developer.apple.com/documentation/coreservices/1585779-mpcreatetask) 函数。 |

每个线程都维护着一个键值对字典，可以在该线程的任何地方访问它。你可以用这个字典来存储想要在线程整个执行期间持续保存的信息。例如，你可以用它来存储那些需要在线程运行循环的多次迭代之间持续保留的状态信息。

Cocoa 和 POSIX 以不同的方式存储线程字典，因此不能混用这两种技术的调用。不过，只要你在线程代码中坚持使用同一种技术，最终结果应该是相似的。在 Cocoa 中，你使用 [NSThread](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSThread/Description.html#//apple_ref/occ/cl/NSThread) 对象的 [threadDictionary](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSThread/Description.html#//apple_ref/occ/instm/NSThread/threadDictionary) 方法来获取一个 `NSMutableDictionary` 对象，可以向其中添加线程所需的任何键。在 POSIX 中，你使用 `pthread_setspecific` 和 `pthread_getspecific` 函数来设置和获取线程的键和值。

大多数高级线程技术默认创建分离线程。在大多数情况下，分离线程是首选，因为它们允许系统在线程完成后立即释放其数据结构。分离线程也不需要与你的程序进行显式交互，从线程中获取结果的方式完全由你自行决定。相比之下，只有当另一个线程显式地与可结合线程进行合并（join）之后，系统才会回收该线程的资源，而这个合并过程可能会阻塞执行合并操作的那个线程。

你可以把可结合线程看作类似于子线程。虽然它们仍然作为独立线程运行，但可结合线程必须先被另一个线程合并，系统才能回收它的资源。可结合线程还提供了一种显式方式，用于把数据从即将退出的线程传递给另一个线程：可结合线程在退出前，可以将一个数据指针或其他返回值传给 `pthread_exit` 函数，之后另一个线程就可以通过调用 `pthread_join` 函数来获取这些数据。

如果你确实想创建可结合线程，唯一的方式是使用 POSIX 线程——POSIX 默认创建的线程就是可结合的。要将线程标记为分离或可结合，需要在创建线程之前，使用 `pthread_attr_setdetachstate` 函数修改线程属性。线程开始运行后，你可以通过调用 `pthread_detach` 函数，把一个可结合线程改为分离线程。关于这些 POSIX 线程函数的更多信息，参见 [pthread](https://developer.apple.com/library/archive/documentation/System/Conceptual/ManPages_iPhoneOS/man3/pthread.3.html#//apple_ref/doc/man/3/pthread) man page。关于如何与线程进行合并的信息，参见 [pthread_join](https://developer.apple.com/library/archive/documentation/System/Conceptual/ManPages_iPhoneOS/man3/pthread_join.3.html#//apple_ref/doc/man/3/pthread_join) man page。

你创建的每个新线程都关联着一个默认优先级。内核的调度算法在决定运行哪些线程时会考虑线程优先级，优先级更高的线程比优先级较低的线程更有可能被运行。较高的优先级并不能保证线程获得特定数量的执行时间，只是意味着与优先级较低的线程相比，它更有可能被调度程序选中。

如果你确实想修改线程优先级，Cocoa 和 POSIX 都提供了相应的方式。对于 Cocoa 线程，可以使用 [NSThread](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSThread/Description.html#//apple_ref/occ/cl/NSThread) 的 [setThreadPriority:](https://developer.apple.com/documentation/foundation/nsthread/1407523-setthreadpriority) 类方法来设置当前运行线程的优先级。对于 POSIX 线程，则使用 `pthread_setschedparam` 函数。更多信息参见 _[NSThread Class Reference](https://developer.apple.com/documentation/foundation/nsthread)_ 或 [pthread_setschedparam](https://developer.apple.com/library/archive/documentation/System/Conceptual/ManPages_iPhoneOS/man3/pthread_setschedparam.3.html#//apple_ref/doc/man/3/pthread_setschedparam) man page。

在很大程度上，OS X 中线程入口点例程的结构与其他平台上的相同：你初始化数据结构，完成一些工作，或者可选地建立一个运行循环，并在线程代码完成后进行清理。根据你的设计，编写入口例程时可能还需要执行一些额外的步骤。

链接了 Objective-C 框架的应用程序通常必须在每个线程中至少创建一个自动释放池。如果应用程序使用托管模型——即由应用程序自行处理对象的保留和释放——自动释放池会捕获该线程中所有被自动释放的对象。

如果应用程序使用垃圾回收而不是托管内存模型，创建自动释放池就并非绝对必要。在启用垃圾回收的应用程序中存在自动释放池并无害处，在大多数情况下它只是被忽略而已。这种做法适用于某个代码模块必须同时支持垃圾回收和托管内存模型的情形：这种情况下，自动释放池必须存在以支持托管内存模型的代码，而当应用程序在启用垃圾回收的情况下运行时，它则会被直接忽略。

如果你的应用程序使用托管内存模型，创建自动释放池应该是你在线程入口例程中做的第一件事；同样地，销毁这个自动释放池也应该是你在线程中做的最后一件事。这个池能确保被自动释放的对象都被捕获，尽管它要等到线程本身退出时才会真正释放这些对象。清单 2-2 展示了使用自动释放池的基本线程入口例程的结构。

__清单 2-2__  定义你的线程入口点例程

```objc
- (void)myThreadMainRoutine
{
    NSAutoreleasePool *pool = [[NSAutoreleasePool alloc] init]; // 顶层池

    // 在这里执行线程工作。

    [pool release];  // 释放池中的对象。
}
```

由于顶层自动释放池要到线程退出时才会释放其中的对象，长期存在的线程应当创建额外的自动释放池，以便更频繁地释放对象。例如，使用运行循环的线程可能会在每次经过该运行循环时创建并释放一个自动释放池。更频繁地释放对象可以防止应用程序的内存占用增长过大，从而避免引发性能问题。不过，与任何与性能相关的行为一样，你应该实际测量代码的性能，并据此适当调整自动释放池的使用方式。

关于内存管理和自动释放池的更多信息，参见 _[高级内存管理编程指南](../Advanced%20Memory%20Management%20Programming%20Guide/About%20Memory%20Management.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgeydambqgaytc2i)_。

如果你的应用程序会捕获并处理异常，线程代码也应该做好准备，捕获可能出现的任何异常。虽然最好在异常可能发生的地方就地处理，但如果线程中抛出的异常未被捕获，会导致应用程序退出。在线程入口例程中安装一个最终的 try/catch，可以让你捕获任何未知异常并做出恰当的响应。

在 Xcode 中构建项目时，你可以使用 C++ 或 Objective-C 的异常处理风格。关于如何设置在 Objective-C 中抛出和捕获异常的信息，参见 _[异常编程主题](../Exception%20Programming%20Topics/Introduction%20to%20Exception%20Programming%20Topics%20for%20Cocoa.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgeydambqgayte2i)_。

编写想在单独线程上运行的代码时，你有两种选择。第一种是把线程的代码写成一个长任务，几乎不间断地执行完，然后在任务结束时让线程退出；第二种是让线程进入一个循环，动态地处理陆续到达的请求。第一种方式不需要对代码做任何特殊设置，你只需直接开始做想做的工作即可；而第二种方式则需要建立线程的运行循环。

OS X 和 iOS 为在每个线程中实现运行循环提供了内置支持。应用框架会自动启动应用程序主线程的运行循环；如果你创建了任何次要线程，就必须手动配置并启动其运行循环。

关于使用和配置运行循环的信息，参见 [运行循环](Run%20Loops.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgeydambqga2to2jninedcnrnknltc)。

推荐的线程退出方式是让它正常退出自己的入口点例程。虽然 Cocoa、POSIX 和 Multiprocessing Services 都提供了可以直接杀死线程的例程，但强烈不建议使用这类例程。强行杀死一个线程会导致它无法自行清理：该线程分配的内存有可能发生泄漏，线程当前正在使用的其他资源也可能得不到妥善清理，从而给之后埋下潜在的问题。

如果你预计需要在操作进行到一半时终止线程，就应当从一开始就设计线程，使其能够响应取消或退出消息。对于长时间运行的操作，这可能意味着要周期性地暂停工作，检查是否收到了这样的消息。如果确实收到了要求线程退出的消息，线程就有机会执行任何必要的清理工作并优雅地退出；否则，它可以直接继续工作，处理下一块数据。

响应取消消息的一种方式是使用运行循环输入源来接收此类消息。清单 2-3 展示了这段代码在线程主入口例程中可能呈现的结构。（该示例只展示了主循环部分，不包含设置自动释放池或配置实际工作内容的步骤。）示例在运行循环上安装了一个自定义输入源，该输入源大概可以由你的另一个线程向其发送消息；关于如何设置输入源的信息，参见 [配置运行循环源](Run%20Loops.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgeydambqga2to2jninedcnrnknlto)。在完成总工作量中的一部分之后，线程会短暂地运行一次运行循环，看看输入源上是否有消息到达。如果没有，运行循环会立即退出，循环继续处理下一块工作。由于处理程序无法直接访问 `exitNow` 局部变量，退出条件是通过线程字典中的一个键值对来传达的。

__清单 2-3__  在长时间作业中检查退出条件

```objc
- (void)threadMainRoutine
{
    BOOL moreWorkToDo = YES;
    BOOL exitNow = NO;
    NSRunLoop* runLoop = [NSRunLoop currentRunLoop];

    // 把 exitNow 这个 BOOL 值添加到线程字典中。
    NSMutableDictionary* threadDict = [[NSThread currentThread] threadDictionary];
    [threadDict setValue:[NSNumber numberWithBool:exitNow] forKey:@"ThreadShouldExitNow"];

    // 安装一个输入源。
    [self myInstallCustomInputSource];

    while (moreWorkToDo && !exitNow)
    {
        // 在这里执行较大工作量中的一块。
        // 完成后修改 moreWorkToDo 这个布尔值。

        // 运行运行循环，但如果输入源没有等待触发就立即超时。
        [runLoop runUntilDate:[NSDate date]];

        // 检查输入源处理程序是否修改了 exitNow 的值。
        exitNow = [[threadDict valueForKey:@"ThreadShouldExitNow"] boolValue];
    }
}
```

[下一页](Run%20Loops.md)[上一页](About%20Threaded%20Programming.md)

