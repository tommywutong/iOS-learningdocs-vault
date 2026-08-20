---
title: Concurrency Programming Guide
apple_id: TP40008091
resource_type: Guide
platform: watchOS|iOS|macOS
topic: Performance
technology: null
published: '2012-12-13'
source_url: https://developer.apple.com/library/archive/documentation/General/Conceptual/ConcurrencyProgrammingGuide/Glossary/Glossary.html
archived_at: '2026-07-15T07:33:45.685835Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Concurrency Programming Guide](Introduction.md)


[Next](Document%20Revision%20History.md)[Previous](Migrating%20Away%20from%20Threads.md)

# Glossary

- __application__

  A specific style of [program](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4daojrfvbuqmjqgqwvgvzrgm) that displays a graphical interface to the user.

- __asynchronous design approach__

  The principle of organizing an application around blocks of code that can be run concurrently with an application’s main thread or other threads of execution. Asynchronous tasks are started by one thread but actually run on a different thread, taking advantage of additional processor resources to finish their work more quickly.

- __block object__

  A C construct for encapsulating inline code and data so that it can be performed later. You use blocks to encapsulate tasks you want to perform, either inline in the current thread or on a separate thread using a dispatch queue. For more information, see _[Blocks Programming Topics](../../Cocoa/Blocks%20Programming%20Topics/Introduction.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga3tkmbs)_.

- __concurrent operation__

  An operation object that does not perform its task in the thread from which its `start` method was called. A concurrent operation typically sets up its own thread or calls an interface that sets up a separate thread on which to perform the work.

- __condition__

  A construct used to synchronize access to a resource. A thread waiting on a condition is not allowed to proceed until another thread explicitly signals the condition.

- __critical section__

  A portion of code that must be executed by only one thread at a time.

- __custom source__

  A [dispatch source](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4daojrfvbuqmjqgqwvgvzrhe) used to process application-defined events. A custom source calls your custom event handler in response to events that your application generates.

- __descriptor__

  An abstract identifier used to access a file, socket, or other system resource.

- __dispatch queue__

  A [Grand Central Dispatch (GCD)](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4daojrfvbuqmjqgqwvgvzsgm) structure that you use to execute your application’s tasks. GCD defines dispatch queues for executing tasks either serially or concurrently.

- __dispatch source__

  A [Grand Central Dispatch (GCD)](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4daojrfvbuqmjqgqwvgvzsgm) data structure that you create to process system-related events.

- __descriptor dispatch source__

  A [dispatch source](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4daojrfvbuqmjqgqwvgvzrhe) used to process file-related events. A file descriptor source calls your custom event handler either when file data is available for reading or writing or in response to file system changes.

- __dynamic shared library__

  A binary executable that is loaded dynamically into an application’s process space rather than linked statically as part of the application binary.

- __framework__

  A type of bundle that packages a dynamic shared library with the resources and header files that support that library. For more information, see _[Framework Programming Guide](../../Mac%20OSX/Framework%20Programming%20Guide/Introduction%20to%20Framework%20Programming%20Guide.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgeydambqge4dg2i)_.

- __global dispatch queue__

  A [dispatch queue](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4daojrfvbuqmjqgqwvgvzz) provided to your application automatically by [Grand Central Dispatch (GCD)](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4daojrfvbuqmjqgqwvgvzsgm). You do not have to create global queues yourself or retain or release them. Instead, you retrieve them using the system-provided functions.

- __Grand Central Dispatch (GCD)__

  A technology for executing asynchronous tasks concurrently. GCD is available in OS X v10.6 and later and iOS 4.0 and later.

- __input source__

  A source of asynchronous events for a thread. Input sources can be port based or manually triggered and must be attached to the thread’s run loop.

- __joinable thread__

  A thread whose resources are not reclaimed immediately upon termination. Joinable threads must be explicitly detached or be joined by another thread before the resources can be reclaimed. Joinable threads provide a return value to the thread that joins with them.

- __library__

  A UNIX feature for monitoring low-level system events. For more information see the [kqueue](https://developer.apple.com/library/archive/documentation/System/Conceptual/ManPages_iPhoneOS/man2/kqueue.2.html#//apple_ref/doc/man/2/kqueue) man page.

- __Mach port dispatch source__

  A [dispatch source](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4daojrfvbuqmjqgqwvgvzrhe) used to process events arriving on a Mach port.

- __main thread__

  A special type of [thread](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4daojrfvbuqmjqgqwvgvzr) created when its owning process is created. When the main thread of a program exits, the process ends.

- __mutex__

  A lock that provides mutually exclusive access to a shared resource. A mutex lock can be held by only one thread at a time. Attempting to acquire a mutex held by a different thread puts the current thread to sleep until the lock is finally acquired.

- __Open Computing Language (OpenCL)__

  A standards-based technology for performing general-purpose computations on a computer’s graphics processor. For more information, see _[OpenCL Programming Guide for Mac](../../Performance/OpenCL%20Programming%20Guide%20for%20Mac/About%20OpenCL%20for%20OS%20X.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4dgmjs)_.

- __operation object__

  An instance of the [NSOperation](https://developer.apple.com/documentation/foundation/nsoperation) class. Operation objects wrap the code and data associated with a task into an executable unit.

- __operation queue__

  An instance of the [NSOperationQueue](https://developer.apple.com/documentation/foundation/operationqueue) class. Operation queues manage the execution of operation objects.

- __private dispatch queue__

  A [dispatch queue](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4daojrfvbuqmjqgqwvgvzz) that you create, retain, and release explicitly.

- __process__

  The runtime instance of an application or program. A process has its own virtual memory space and system resources (including port rights) that are independent of those assigned to other programs. A process always contains at least one thread (the main thread) and may contain any number of additional threads.

- __process dispatch source__

  A [dispatch source](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4daojrfvbuqmjqgqwvgvzrhe) used to handle process-related events. A process source calls your custom event handler in response to changes to the process you specify.

- __program__

  A combination of code and resources that can be run to perform some task. Programs need not have a graphical user interface, although graphical applications are also considered programs.

- __reentrant__

  Code that can be started on a new thread safely while it is already running on another thread.

- __run loop__

  An event-processing loop, during which events are received and dispatched to appropriate handlers.

- __run loop mode__

  A collection of input sources, timer sources, and run loop observers associated with a particular name. When run in a specific “mode,” a run loop monitors only the sources and observers associated with that mode.

- __run loop object__

  An instance of the [NSRunLoop](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSRunLoop/Description.html#//apple_ref/occ/cl/NSRunLoop) class or [CFRunLoopRef](https://developer.apple.com/documentation/corefoundation/cfrunloopref) opaque type. These objects provide the interface for implementing an event-processing loop in a thread.

- __run loop observer__

  A recipient of notifications during different phases of a run loop’s execution.

- __semaphore__

  A protected variable that restricts access to a shared resource. Mutexes and conditions are both different types of semaphore.

- __signal__

  A UNIX mechanism for manipulating a process from outside its domain. The system uses signals to deliver important messages to an application, such as whether the application executed an illegal instruction. For more information see the [signal](https://developer.apple.com/library/archive/documentation/System/Conceptual/ManPages_iPhoneOS/man3/signal.3.html#//apple_ref/doc/man/3/signal) man page.

- __signal dispatch source__

  A [dispatch source](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4daojrfvbuqmjqgqwvgvzrhe) used to process UNIX signals. A signal source calls your custom event handler whenever the process receives a UNIX signal.

- __task__

  A quantity of work to be performed. Although some technologies (most notably Carbon Multiprocessing Services) use this term differently, the preferred usage is as an abstract concept indicating some quantity of work to be performed.

- __thread__

  A flow of execution in a process. Each thread has its own stack space but otherwise shares memory with other threads in the same process.

- __timer dispatch source__

  A [dispatch source](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4daojrfvbuqmjqgqwvgvzrhe) used to process periodic events. A timer source calls your custom event handler at regular, time-based intervals.

[Next](Document%20Revision%20History.md)[Previous](Migrating%20Away%20from%20Threads.md)

