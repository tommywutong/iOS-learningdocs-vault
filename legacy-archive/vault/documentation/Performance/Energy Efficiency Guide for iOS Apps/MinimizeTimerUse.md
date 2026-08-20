---
title: Energy Efficiency Guide for iOS Apps
apple_id: TP40015243
resource_type: Guide
platform: watchOS|iOS
topic: Performance
technology: null
published: '2016-09-13'
source_url: https://developer.apple.com/library/archive/documentation/Performance/Conceptual/EnergyGuide-iOS/MinimizeTimerUse.html
archived_at: '2026-07-18T01:47:58.691337Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Energy Efficiency Guide for iOS Apps](index.md)



## Minimize Timer Use

You can reduce your app’s energy usage by implementing energy-efficient APIs instead of timers. The `NSURLSession` API, for example, provides the ability to perform out-of-process background URL sessions and receive notifications when they are complete. See [Defer Networking](DeferNetworking.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge2tenbtfvbuqmjyfvjvomi). If you must use timers, employ them efficiently.

### The High Cost of Timers

A timer lets you schedule a delayed or periodic action. A timer waits until a certain interval has elapsed and then fires, performing a specific action such as sending a message to its target object. Waking the system from an idle state incurs an energy cost when the CPU and other systems are awakened from their low-power, idle states. If a timer causes the system to wake, it incurs that cost.

Apps often use timers unnecessarily. If you use timers in your app, consider whether you truly need them. For example, some apps use timers to poll for state changes when they should respond to events instead. Other apps use timers as synchronization tools when they should use semaphores or other locks to achieve the greatest efficiency. Some timers are executed without suitable timeouts, causing them to continue firing when they’re no longer needed. Regardless of the scenario, if there are many timer-invoked wakeups, the energy impact is high.

### Get Event Notifications Without Using Timers

Some apps use timers to monitor for changes to file contents, network availability, and other state changes. Timers prevent the CPU from going to or staying in the idle state, which increases energy usage and consumes battery power.

Instead of using timers to watch for events, use a more efficient service, such as a dispatch source. See Listing 5-1.

__Listing 5-1__Recommended: Use an energy-efficient dispatch source to obtain file change notifications

Objective-C

1. `const char *myFile = [@"/Path/To/File" fileSystemRepresentation];`
2. `int fileDescriptor = open(myFile, O_EVTONLY);`
3. `dispatch_queue_t myQueue = dispatch_get_main_queue();`
4. `const uint64_t dispatchFlags = DISPATCH_VNODE_DELETE | DISPATCH_VNODE_WRITE;`
5. `dispatch_source_t mySource = dispatch_source_create(DISPATCH_SOURCE_TYPE_VNODE, fileDescriptor, dispatchFlags, myQueue);`
6. `dispatch_source_set_event_handler(mySource, ^{`
7. `[self checkForFile];`
8. `});`
9. `dispatch_resume(mySource);`

Swift

1. `let myFile = @"/Path/To/File"`
2. `let fileDescriptor = open(myFile.fileSystemRepresentation, O_EVTONLY)`
3. `let myQueue = dispatch_get_main_queue()`
4. `let dispatchFlags = DISPATCH_VNODE_DELETE | DISPATCH_VNODE_WRITE`
5. `let mySource = dispatch_source_create(DISPATCH_SOURCE_TYPE_VNODE, fileDescriptor, dispatchFlags, myQueue)`
6. `dispatch_source_set_event_handler(mySource) {`
7. `self.checkForFile()`
8. `}`
9. `dispatch_resume(mySource)`

Use event notifications for system-provided services whenever possible. Table 5-1 provides a list of common system notifications along with their corresponding coding approaches.

__Table 5-1__Obtaining event notifications for system services

| Event to be notified about | Approach to follow for obtaining event notifications | Described in |
| --- | --- | --- |
| Updates to files | Configure a dispatch source. | [Dispatch Sources](../../General/Concurrency%20Programming%20Guide/Concurrency%20and%20Application%20Design.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4daojrfvbuqmjqgawvgvzrge) in _[Concurrency Programming Guide](../../General/Concurrency%20Programming%20Guide/Introduction.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4daojr)_ |
| Updates to systemwide files or directories | Create an event stream with the File System Events API. | _[File System Programming Guide](../../File%20Management/File%20System%20Programming%20Guide/About%20Files%20and%20Directories.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgeydmnzs)_ |
| Network events | Use the Apple Push Notification service. | _[Local and Remote Notification Programming Guide](https://developer.apple.com/library/archive/documentation/NetworkingInternet/Conceptual/RemoteNotificationsPG/index.html#//apple_ref/doc/uid/TP40008194)_ |
|  | Use Bonjour. | _[DNS Service Discovery Programming Guide](../../Networking/DNS%20Service%20Discovery%20Programming%20Guide/Introduction%20to%20DNS%20Service%20Discovery.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaydsnru)_ and _[NSNetServices and CFNetServices Programming Guide](../../Networking/NSNetServices%20and%20CFNetServices%20Programming%20Guide/About%20NSNetServices%20and%20CFNetServices.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgazdomzw)_ |

### Use GCD Tools for Synchronization Instead of Timers

Grand Central Dispatch (GCD) provides dispatch queues, dispatch semaphores, and other synchronization features that are more efficient than timers.

The code in Listing 5-2 performs work on one thread while another thread and a completion handler use a timer to periodically check whether work on the first thread has completed. Until the work in the first thread is completed, the `usleep` timer in the second thread continually wakes the system only to determine whether the work in the first thread has completed.

__Listing 5-2__Not recommended: Using an energy-inefficient timer as a synchronization tool

Objective-C

1. `BOOL workIsDone = NO;`
3. `/* thread one */`
4. `void doWork(void) {`
5. `/* wait for network ... */`
6. `workIsDone = YES;`
7. `}`
9. `/* thread two: completion handler */ /*** Not Recommended ***/`
10. `void waitForWorkToFinish(void) {`
11. `while (!workIsDone) {`
12. `usleep(100000); /* 100 ms */ /*** Not Recommended ***/`
13. `}`
14. `[WorkController workDidFinish];`
15. `}`

Swift

1. `var workIsDone = false`
3. `/* thread one */`
4. `func doWork() {`
5. `/* wait for network ... */`
6. `workIsDone = true`
7. `}`
9. `/* thread two: completion handler */ /*** Not Recommended ***/`
10. `func waitForWorkToFinish() {`
11. `while (!workIsDone) {`
12. `usleep(100000) /* 100 ms */ /*** Not Recommended ***/`
13. `}`
14. `WorkController.workDidFinish()`
15. `}`

The code in Listing 5-3 performs synchronization much more efficiently with a serial dispatch queue.

__Listing 5-3__Recommended: Using an energy-efficient dispatch queue to synchronize threads

Objective-C

1. `myQueue = dispatch_queue_create("com.myapp.myq", DISPATCH_QUEUE_SERIAL);`
2. `dispatch_block_t block;`
3. `block = dispatch_block_create(0, ^{`
4. `/* wait for network ... */`
5. `});`
7. `/* thread one */`
8. `void beginWork(void) {`
9. `dispatch_async(myQueue, block);`
10. `};`
12. `/* thread two */`
13. `void waitForWorkToFinish(void) {`
14. `dispatch_block_wait(block, DISPATCH_TIME_FOREVER);`
15. `Block_release(block);`
16. `[WorkController workDidFinish];`
17. `};`

Swift

1. `let myQueue = dispatch_queue_create("com.myapp.myq", DISPATCH_QUEUE_SERIAL)`
2. `let block = dispatch_block_create(0) {`
3. `/* wait for network ... */`
4. `}`
6. `/* thread one */`
7. `func beginWork() {`
8. `dispatch_async(myQueue, block)`
9. `}`
11. `/* thread two */`
12. `func waitForWorkToFinish() {`
13. `dispatch_block_wait(block, DISPATCH_TIME_FOREVER)`
14. `WorkController.workDidFinish()`
15. `}`

Without continually waking the system, the completion method on thread two waits for the work on the first thread to finish.

Similarly, the code in Listing 5-4 demonstrates how to perform a long-running operation on one thread, and additional work on another thread once the long-running operation completes. This technique could be used, for example, to prevent blocking work from occurring on the main thread of your app.

__Listing 5-4__Recommended: Using asynchronous dispatch queues to perform work on multiple threads

Objective-C

1. `dispatch_async(thread2_queue) {`
2. `/* do long work */`
3. `dispatch_async(thread1_queue) {`
4. `/* continue with next work */`
5. `}`
6. `};`

Swift

1. `dispatch_async(thread2_queue) {`
2. `/* do long work */`
3. `dispatch_async(thread1_queue) {`
4. `/* continue with next work */`
5. `}`
6. `}`

> [!NOTE]
> 

### If You Must Use a Timer, Employ It Efficiently

Games and other graphics-intensive apps often rely on timers to initiate screen or animation updates. Many programming interfaces delay processes for specified periods of time. Any method or function to which you pass a relative or absolute deadline is probably a timer API. For example:

- High-level timer APIs include dispatch timer sources, [CFRunLoopTimerCreate](https://developer.apple.com/documentation/corefoundation/1543570-cfrunlooptimercreate) and other CFRunLoopTimer functions, the [NSTimer](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSTimer/Description.html#//apple_ref/occ/cl/NSTimer) class, and the [performSelector:withObject:afterDelay:](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSObject/Description.html#//apple_ref/occ/instm/NSObject/performSelector:withObject:afterDelay:) method.
- Low-level timer APIs include the functions `sleep`, `usleep`, `nanosleep`, `pthread_cond_timedwait`, `select`, `poll`, `kevent`, [dispatch_after](https://developer.apple.com/documentation/dispatch/1452876-dispatch_after), and [dispatch_semaphore_wait](https://developer.apple.com/documentation/dispatch/1453087-dispatch_semaphore_wait).

If you determine that your app requires a timer, follow these guidelines for drawing the least amount of energy:

- Use timers economically by specifying suitable timeouts.
- Invalidate repeating timers when they’re no longer needed.
- Set tolerances for when timers should fire.

### Specify Suitable Timeouts

Many functions include a timeout parameter and exit when the timeout is reached. Passing a time interval to these functions causes them to operate as timers, with all the energy consumption of timers.

If your app uses an inappropriate timeout value, that usage can waste energy. For example, in the code in Listing 5-5, a timeout value of 500 nanoseconds from the current time ([DISPATCH_TIME_NOW](https://developer.apple.com/documentation/dispatch/dispatch_time_now)) is passed to the [dispatch_semaphore_wait](https://developer.apple.com/documentation/dispatch/1453087-dispatch_semaphore_wait) function. Until the semaphore is signaled, the code performs no useful work while `dispatch_semaphore_wait` continually times out.

If your app uses the [DISPATCH_TIME_FOREVER](https://developer.apple.com/documentation/dispatch/dispatch_time_forever) constant, that usage can block a function indefinitely, allowing the function to resume only when needed. The code in Listing 5-6 passes the `DISPATCH_TIME_FOREVER` constant to `dispatch_semaphore_wait`. The function blocks until it receives the semaphore.

__Listing 5-5__Not recommended: Set a timeout that isn’t acted upon by the app

Objective-C

1. `while (YES) {`
2. `dispatch_time_t timeout = dispatch_time(DISPATCH_TIME_NOW, 500 * NSEC_PER_SEC);`
3. `long semaphoreReturnValue = dispatch_semaphore_wait(mySemaphore, timeout);`
4. `if (havePendingWork) {`
5. `[self doPendingWork];`
6. `}`
7. `}`

Swift

1. `repeat {`
2. `let timeout = dispatch_time(DISPATCH_TIME_NOW, 500 * Double(NSEC_PER_SEC))`
3. `let semaphoreReturnValue = dispatch_semaphore_wait(mySemaphore, timeout)`
4. `if (havePendingWork) {`
5. `self.doPendingWork()`
6. `}`
7. `} while true`

__Listing 5-6__Recommended: Block indefinitely until a semaphore is received

Objective-C

1. `while (YES) {`
2. `dispatch_time_t timeout = DISPATCH_TIME_FOREVER;`
3. `long semaphoreReturnValue = dispatch_semaphore_wait(mySemaphore, timeout);`
4. `if (havePendingWork) {`
5. `[self doPendingWork];`
6. `}`
7. `}`

Swift

1. `repeat {`
2. `let timeout = DISPATCH_TIME_FOREVER`
3. `let semaphoreReturnValue = dispatch_semaphore_wait(mySemaphore, timeout)`
4. `if (havePendingWork) {`
5. `self.doPendingWork()`
6. `}`
7. `} while true`

In most cases, blocking indefinitely (as in Listing 5-6) is more suitable than specifying a time value. But if your app does need to wait for a timeout, specify a semaphore value that represents a meaningful state change, such as an error condition or a network timeout.

### Invalidate Repeating Timers You No Longer Need

If you use a repeating timer, invalidate or cancel it when you no longer need it. Forgetting to stop timers wastes lots of energy, and is one of the simplest problems to fix.

The code in Listing 5-7 uses a repeating [NSTimer](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSTimer/Description.html#//apple_ref/occ/cl/NSTimer) timer. When the timer is no longer needed, the code calls the [invalidate](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSTimer/Description.html#//apple_ref/occ/instm/NSTimer/invalidate) method to stop the timer from firing again, avoiding unnecessary energy use.

__Listing 5-7__Recommended: Invalidating a timer when it is no longer needed

Objective-C

1. `NSTimer *myTimer = [[NSTimer alloc] initWithFireDate:date`
2. `interval:1.0`
3. `target:self`
4. `selector:@selector(timerFired:)`
5. `userInfo:nil`
6. `repeats:YES];`
8. `/* Do work until the timer is no longer needed */`
10. `[myTimer invalidate]; /* Recommended */`

Swift

1. `var myTimer = NSTimer.initWithFireDate(date, interval: 1.0, target: self, selector:"timerFired:", userInfo:nil repeats: true)`
3. `/* Do work until the timer is no longer needed */`
5. `myTimer.invalidate() /* Recommended */`

For a repeating dispatch timer, use the [dispatch_source_cancel](https://developer.apple.com/documentation/dispatch/1385604-dispatch_source_cancel) function to cancel the timer when it’s no longer needed. For a repeating `CFRunLoop` timer, use the [CFRunLoopTimerInvalidate](https://developer.apple.com/documentation/corefoundation/1542231-cfrunlooptimerinvalidate) function.

### Specify a Tolerance for Batching Timers Systemwide

Specify a tolerance for the accuracy of when your timers fire. The system will use this flexibility to shift the execution of timers by small amounts of time—within their tolerances—so that multiple timers can be executed at the same time. Using this approach dramatically increases the amount of time that the processor spends idling while users detect no change in system responsiveness.

You can use the `setTolerance:` method to specify a tolerance for your timer, as shown in Listing 5-8. The tolerance of ten percent is set by `setTolerance:0.3` compared to `interval:3.0`.

__Listing 5-8__Recommended: Set a tolerance for `NSTimer` timers

Objective-C

1. `[myTimer setTolerace:0.3];`
2. `[[NSRunLoop currentRunLoop] addTimer:myTimer forMode:NSDefaultRunLoopMode];`

Swift

1. `myTimer.tolerance(0.3)`
2. `NSRunLoop.currentRunLoop().addTimer(myTimer, forMode:NSDefaultRunLoopMode)`

The example in Listing 5-9 shows how you can set a tolerance of ten percent using the last parameter of the [dispatch_source_set_timer](https://developer.apple.com/documentation/dispatch/1385606-dispatch_source_set_timer) function.

__Listing 5-9__Recommended: Set a tolerance for dispatch timers

Objective-C

1. `dispatch_source_t myDispatchSourceTimer = dispatch_source_create(DISPATCH_SOURCE_TYPE_TIMER, 0, 0, myQueue);`
2. `dispatch_source_set_timer(myDispatchSourceTimer, DISPATCH_TIME_NOW, 1 * NSEC_PER_SEC, NSEC_PER_SEC / 10);`
3. `dispatch_source_set_event_handler(myDispatchSourceTimer, ^{`
4. `[self timerFired];`
5. `}`
6. `);`
7. `dispatch_resume(myDispatchSourceTimer);`

Swift

1. `let myDispatchSourceTimer = dispatch_source_create(DISPATCH_SOURCE_TYPE_TIMER, 0, 0, myQueue)`
2. `dispatch_source_set_timer(myDispatchSourceTimer, DISPATCH_TIME_NOW, 1 * Double(NSEC_PER_SEC), Double(NSEC_PER_SEC) / 10)`
3. `dispatch_source_set_event_handler(myDispatchSourceTimer) {`
4. `self.timerFired()`
5. `}`
6. `dispatch_resume(myDispatchSourceTimer)`

You can specify a tolerance of ten percent of the timer interval for `CFRunLoop` timers using the `CFRunLoopTimerSetTolerance` function, as shown in Listing 5-10. The tolerance of ten percent is set by the second argument to `CFRunLoopTimerSetTolerance`, compared with the third argument to [CFRunLoopTimerCreate](https://developer.apple.com/documentation/corefoundation/1543570-cfrunlooptimercreate).

__Listing 5-10__Recommended: Set a tolerance for `CFRunLoop` timers

Objective-C

1. `CFRunLoopTimerRef myRunLoopTimer = CFRunLoopTimerCreate(kCFAllocatorDefault, fireDate, 2.0, 0, &timerFired, NULL);`
2. `CFRunLoopTimerSetTolerance(myRunLoopTimer, 0.2);`
3. `CFRunLoopAddTimer(CFRunLoopGetCurrent(), myRunLoopTimer, kCFRunLoopDefaultMode);`

Swift

1. `myRunLoopTimer = CFRunLoopTimerCreate(kCFAllocatorDefault, fireDate, 2.0, 0, 0, &timerFired, NULL)`
2. `CFRunLoopTimerSetTolerance(myRunLoopTimer, 0.2)`
3. `CFRunLoopAddTimer(CFRunLoopGetCurrent(), myRunLoopTimer, kCFRunLoopDefaultMode)`

After you specify a tolerance for a timer, it may fire anytime between its scheduled fire date and the scheduled fire date, plus the tolerance. The timer won’t fire before the scheduled fire date. For repeating timers, the next fire date is always calculated from the original fire date in order to keep future fire times on track with their original schedule.

A general guideline is to set the tolerance to at least ten percent of the interval for a repeating timer, as in the examples above. Even a small amount of tolerance has a significant positive impact on the energy usage of your app.

> [!NOTE]
> 

[Prioritize Work with Quality of Service Classes](PrioritizeWorkWithQoS.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge2tenbtfvbuqmzzfvjvomi)

[Minimize I/O](MinimizeIO.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge2tenbtfvbuqnbsfvjvomi)
