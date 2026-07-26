---
title: Thread
framework: Foundation
symbol_kind: class
role: symbol
role_heading: Class
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.0+, macOS 10.0+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/thread
source_url: 'https://developer.apple.com/documentation/foundation/thread'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/thread.json'
content_hash: 'sha256:77f8a059f337bce7'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Foundation](../foundation.md)

# Thread

<sub>Class</sub>

A thread of execution.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
class Thread
```

## Overview

Use this class when you want to have an Objective-C method run in its own thread of execution. Threads are especially useful when you need to perform a lengthy task, but don’t want it to block the execution of the rest of the application. In particular, you can use threads to avoid blocking the main thread of the application, which handles user interface and event-related actions. Threads can also be used to divide a large job into several smaller jobs, which can lead to performance increases on multi-core computers.

The [Thread](thread.md) class supports semantics similar to those of [Operation](operation.md) for monitoring the runtime condition of a thread. You can use these semantics to cancel the execution of a thread or determine if the thread is still executing or has finished its task. Canceling a thread requires support from your thread code; see the description for [- cancel](<thread/cancel().md>) for more information.

### Subclassing Notes

You can subclass [Thread](thread.md) and override the [- main](<thread/main().md>) method to implement your thread’s main entry point. If you override [- main](<thread/main().md>), you do not need to invoke the inherited behavior by calling `super`.

## Relationships

- **Inherits From**: [NSObject](../objectivec/nsobject-swift.class.md)

- **Conforms To**: [CVarArg](../swift/cvararg.md), [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md), [CustomStringConvertible](../swift/customstringconvertible.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [NSObjectProtocol](../objectivec/nsobjectprotocol.md)

## Topics

### Initializing an NSThread Object

- [- init](<thread/init().md>) — Returns an initialized `NSThread` object.
- [- initWithTarget:selector:object:](<thread/init(target_selector_object_).md>) — Returns an `NSThread` object initialized with the given arguments.

### Starting a Thread

- [+ detachNewThreadSelector:toTarget:withObject:](<thread/detachnewthreadselector(__totarget_with_).md>) — Detaches a new thread and uses the specified selector as the thread entry point.
- [- start](<thread/start().md>) — Starts the receiver.
- [- main](<thread/main().md>) — The main entry point routine for the thread.

### Stopping a Thread

- [+ sleepUntilDate:](<thread/sleep(until_).md>) — Blocks the current thread until the time specified.
- [+ sleepForTimeInterval:](<thread/sleep(fortimeinterval_).md>) — Sleeps the thread for a given time interval.
- [+ exit](<thread/exit().md>) — Terminates the current thread.
- [- cancel](<thread/cancel().md>) — Changes the cancelled state of the receiver to indicate that it should exit.

### Determining the Thread’s Execution State

- [executing](thread/isexecuting.md) — A Boolean value that indicates whether the receiver is executing.
- [finished](thread/isfinished.md) — A Boolean value that indicates whether the receiver has finished execution.
- [cancelled](thread/iscancelled.md) — A Boolean value that indicates whether the receiver is cancelled.

### Working with the Main Thread

- [isMainThread](thread/ismainthread-swift.type.property.md) — Returns a Boolean value that indicates whether the current thread is the main thread.
- [isMainThread](thread/ismainthread-swift.property.md) — A Boolean value that indicates whether the receiver is the main thread.
- [mainThread](thread/main.md) — Returns the `NSThread` object representing the main thread.

### Querying the Environment

- [+ isMultiThreaded](<thread/ismultithreaded().md>) — Returns whether the application is multithreaded.
- [currentThread](thread/current.md) — Returns the thread object representing the current thread of execution.
- [callStackReturnAddresses](thread/callstackreturnaddresses.md) — Returns an array containing the call stack return addresses.
- [callStackSymbols](thread/callstacksymbols.md) — Returns an array containing the call stack symbols.

### Working with Thread Properties

- [threadDictionary](thread/threaddictionary.md) — The thread object’s dictionary.
- [NSAssertionHandlerKey](nsassertionhandlerkey.md) — A key with a corresponding value in the thread dictionary.
- [name](thread/name.md) — The name of the receiver.
- [stackSize](thread/stacksize.md) — The stack size of the receiver, in bytes.

### Prioritizing Thread Work

- [qualityOfService](thread/qualityofservice.md)
- [QualityOfService](qualityofservice.md) — Constants that indicate the nature and importance of work to the system.
- [+ threadPriority](<thread/threadpriority().md>) — Returns the current thread’s priority.
- [threadPriority](thread/threadpriority.md) — The receiver’s priority
- [+ setThreadPriority:](<thread/setthreadpriority(__).md>) — Sets the current thread’s priority.

### Notifications

- [NSDidBecomeSingleThreadedNotification](nsnotification/name-swift.struct/nsdidbecomesinglethreaded.md) — Not implemented. _(deprecated)_
- [NSThreadWillExitNotification](nsnotification/name-swift.struct/nsthreadwillexit.md) — An `NSThread` object posts this notification when it receives the [+ exit](<thread/exit().md>) message, before the thread exits. Observer methods invoked to receive this notification execute in the exiting thread, before it exits. _(deprecated)_
- [NSWillBecomeMultiThreadedNotification](nsnotification/name-swift.struct/nswillbecomemultithreaded.md) — Posted when the first thread is detached from the current thread. The `NSThread` class posts this notification at most once—the first time a thread is detached using [+ detachNewThreadSelector:toTarget:withObject:](<thread/detachnewthreadselector(__totarget_with_).md>) or the [- start](<thread/start().md>) method. Subsequent invocations of those methods do not post this notification. Observers of this notification have their notification method invoked in the main thread, not the new thread. The observer notification methods always execute before the new thread begins executing. _(deprecated)_

### Initializers

- [- initWithBlock:](<thread/init(block_).md>)

### Type Methods

- [+ detachNewThreadWithBlock:](<thread/detachnewthread(__).md>)

## See Also

### Threads and Locking

- [NSLocking](nslocking.md) — The elementary methods adopted by classes that define lock objects.
- [NSLock](nslock.md) — An object that coordinates the operation of multiple threads of execution within the same application.
- [NSRecursiveLock](nsrecursivelock.md) — A lock that may be acquired multiple times by the same thread without causing a deadlock.
- [NSDistributedLock](nsdistributedlock.md) — A lock that multiple applications on multiple hosts can use to restrict access to some shared resource, such as a file.
- [NSConditionLock](nsconditionlock.md) — A lock that can be associated with specific, user-defined conditions.
- [NSCondition](nscondition.md) — A condition variable whose semantics follow those used for POSIX-style conditions.
