---
title: Porting to Mac OS X from Windows Win32 API
apple_id: 10000190i
resource_type: Guide
platform: macOS
topic: Cross Platform
technology: null
published: '2011-01-05'
source_url: https://developer.apple.com/library/archive/documentation/Porting/Conceptual/win32porting/Articles/mprocessing.html
archived_at: '2026-07-18T01:50:59.718887Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Porting to Mac OS X from Windows Win32 API](Porting%20to%20Mac%20OS%20X%20from%20Windows%20Win32%20API.md)


[Next](Networking%20in%20Mac%20OS%20X.md)[Previous](Printing%20for%20Carbon%20Applications.md)

# Multiprocessing

Dual-processor computers are now a significant part of Apple's hardware product line, and Mac OS X is designed to take advantage of them. If your Win32 application uses threading to take advantage of multiple processors, you can achieve similar performance when you port your application to Mac OS X. This section tells you how to get started.

For your information, Mac OS X supports multiple threading packages, including POSIX threads. (See Chapter 14 of _Inside Mac OS X: System Overview_ for details.) If your Win32 application is already threaded, the Mac OS X API that most closely matches your code may be the Multiprocessing Services API, which is what this section covers.

Mac OS X and the Win32 platform take similar approaches to their support of multiprocessing, and the APIs involved are similar in structure and design. Here are the major similarities:

- Both approach the creation of multiprocessor-ready applications by splitting the application into multiple independent threads (called _tasks_ in the Mac OS X Multiprocessing Services API), which the underlying operating system then schedules to run on multiple processors.
- Both implement symmetric multiprocessing (SMP).
- Both automatically assign threads/tasks to available processors in a way meant to maximize overall execution speed.
- On both platforms, applications created using threads/tasks run well on both single-processor and multiprocessor computers.
- Both use critical sections (called _critical regions_ in Mac OS X) to restrict access to a given shared memory range to one thread/task at a time.
- Both provide semaphores for use as a synchronization mechanism among cooperating threads/tasks.

There are three ways to port your Win32 threaded code to Mac OS X using the Multiprocessing Services API:

- writing "glue" code
- modifying existing code to use Multiprocessing Services routines
- rewriting your code to be more efficient

Which one you choose depends, of course, upon the priorities and limitations of your situation.

Before you decide on a porting approach, you should familiarize yourself with the Mac OS X APIs you will be using. As is the case on the Win32 platform, some APIs work in a multithreaded environment, others do not, and still others work if you observe certain restrictions. The issue of multithreading support may force you to change the approach you use to port your application to Mac OS X.

In this approach, you leave your source code unchanged and concentrate on writing glue code that implements your multiprocessing APIs using Multiprocessing Services routines. This way, your code continues to run, believing that it is still operating on a multiple-processor Win32 computer.

The primary advantage of this approach is that if it is implemented correctly, you do not need to modify or retest the application code that uses threads, semaphores, critical sections, and so on. In addition, once you have the glue code working, you can port new Win32 applications to Mac OS X with minimal effort.

There are several significant disadvantages to this approach, however. First, the glue code necessarily introduces some processing overhead, and the ported application may run unacceptably slow. Second, writing the glue code is not a trivial task, and your schedule may not include the time needed to design, implement, and debug it.

This approach involves leaving your program logic intact but replacing Win32-specific code with Mac OS X code that does the same thing.

The primary advantage of this approach over the glue-code approach is that the resulting code will run faster then it would using glue code. Depending on the complexity and length of your Win32 code, the porting process may be faster and easier.

This approach has two significant disadvantages. First, you will need to retest the ported application code. Second, this approach leaves you with two versions of your source code that must be maintained and enhanced separately.

On the Win32 side, the prevailing programming paradigm for multi-threaded applications centers around suspending threads that run too long and killing threads when necessary; these are actions that waste processor time needlessly. Applications that are structured around the producer/consumer model make better use of multithreading on any platform, and you should consider rewriting your Win32 code to use it.

An added advantage to switching to the producer/consumer model is that Mac OS X was designed to work well with it. When a task (thread) blocks, Mac OS X automatically suspends it quickly and with virtually no processor or memory overhead; when a task becomes unblocked, Mac OS X automatically and quickly reactivates it. Task creation and destruction, on the other hand, incur significantly greater overhead.

Tasks are suspended and resumed millions of times over their lifetimes, so these operations should be as efficient as possible. The producer/consumer model, in general, has no need to terminate a thread implementing a producer or consumer prematurely, though it switches tasks often. These two facts, taken together, explain why Mac OS X and the producer/consumer model are such a good fit.

The advantage of converting your program logic to use the producer/consumer model is that your application will run faster and will be easier to maintain on both the Win32 and Mac OS X platforms. The disadvantage is, of course, the time needed to rewrite and debug a major portion of your code.

A Multiprocessing Services task is a preemptively scheduled thread that is layered on top of a POSIX thread. The Multiprocessing Services API includes support for the following:

- _Tasks_: creating, terminating, and setting the relative priority of preemptive tasks
- _Critical regions_: creating, deleting, exiting, and attempting to enter critical regions
- _Semaphores_: creating, removing, signaling, and waiting on a semaphore
- _Memory allocation_: creating and manipulating a nonrelocatable block of memory available only to the threads of the current application (process)
- _Message queues_: creating, deleting, and manipulating FIFO message queues (used, among other things, for implementing producer/consumer programs)
- _Timers_: creating, arming, canceling, and deleting a timer; blocking a task until a specified time
- _Per-task storage variables_: setting and retrieving the value associated with a given index number and the current task
- _Processor availability_: querying the host computer about the number of processors available and their availability
- _Event groups_: creating, removing, and working with event groups (see below)

Event groups help you build code that blocks a thread until one of multiple events occurs. This is an improvement on the Win32 routine WaitForMultipleObjects in that, with an event group, you know which event or events have occurred and can make use of that knowledge.

You can find the the Multiprocessing Services API in the Carbon section of Apple’s Developer Documentation website. For your convenience, a link to its page is listed below.

|  |  |
| --- | --- |
| Multiprocessing Services | _[Multiprocessing Services Reference](https://developer.apple.com/documentation/coreservices/carbon_core/multiprocessing_services)_ |
| books on pthreads | _Programming with POSIX Threads_, by David R. Butenhof (Addison Wesley, 1997)  _POSIX 4: Programming for the Real World_, by Bill O. Gallmeister and Mike Loukides (O'Reilly, 1994) |

[Next](Networking%20in%20Mac%20OS%20X.md)[Previous](Printing%20for%20Carbon%20Applications.md)

