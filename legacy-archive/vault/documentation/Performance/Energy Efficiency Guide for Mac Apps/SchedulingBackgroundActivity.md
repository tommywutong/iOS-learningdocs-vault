---
title: Energy Efficiency Guide for Mac Apps
apple_id: TP40013929
resource_type: Guide
platform: macOS
topic: Performance
technology: null
published: '2016-09-13'
source_url: https://developer.apple.com/library/archive/documentation/Performance/Conceptual/power_efficiency_guidelines_osx/SchedulingBackgroundActivity.html
archived_at: '2026-07-18T01:50:24.843480Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Energy Efficiency Guide for Mac Apps](index.md)



## Schedule Background Activity

Background activity includes periodic tasks that aren’t user-initiated or that aren’t blocking the user.

### Schedule Deferrable Background Activities

The `NSBackgroundActivityScheduler` API provides a simple interface for scheduling an arbitrary maintenance or background task. It’s similar to an [NSTimer](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSTimer/Description.html#//apple_ref/occ/cl/NSTimer) object, in that it lets you schedule a repeating or nonrepeating task. However, `NSBackgroundActivityScheduler` gives the system flexibility to determine the most efficient time to execute based on energy usage, thermal conditions, and CPU use.

Use the `NSBackgroundActivityScheduler` API to schedule:

- Automatic saves
- Backups
- Data maintenance
- Periodic content fetches
- Installation of updates
- Activities occurring in intervals of 10 minutes or more
- Any other deferrable tasks

> [!NOTE]
> 

### Create a Scheduler

To initialize a scheduler, call [initWithIdentifier:](https://developer.apple.com/documentation/foundation/nsbackgroundactivityscheduler/1407482-init) for `NSBackgroundActivityScheduler`, and pass it a unique identifier string in reverse DNS notation (`nil` and zero-length strings are not allowed) that remains constant across launches of your application. See Listing 12-1.

__Listing 12-1__Creating a scheduler

Objective-C

1. `NSBackgroundActivityScheduler *activity = [[NSBackgroundActivityScheduler alloc] initWithIdentifier:@"com.example.MyApp.updatecheck"];`

Swift

1. `let activity = NSBackgroundActivityScheduler(identifier: "com.example.MyApp.updatecheck")`

> [!NOTE]
> 

### Configure Scheduler Properties

Configure the scheduler with the desired scheduling properties.

- `repeats`—If set to `YES``true`, the activity is rescheduled at the specified interval after finishing.
- `interval`—For repeating schedulers, the average interval between invocations of the activity. For non-repeating schedulers, `interval` is the suggested interval of time between scheduling the activity and the invocation of the activity.
- `tolerance`—The amount of time before or after the nominal fire date when the activity should be invoked. The nominal fire date is calculated by using the interval combined with the previous fire date or the time when the activity is started. These two properties create a window in time, during which the activity may be scheduled. The system will more aggressively schedule the activity as it nears the end of the grace period after the nominal fire date. The default value is half the interval.
- `qualityOfService`—The default value is `NSQualityOfServiceBackground`. If you upgrade the quality of service above this level, the system schedules the activity more aggressively. The default value is the recommended value for most activities. For information on quality of service, see [Prioritize Work at the Task Level](PrioritizeWorkAtTheTaskLevel.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgeztsmrzfvbuqmzvfvjvomi).

Listing 12-2, Listing 12-3, and Listing 12-4 demonstrate different scheduling scenarios.

__Listing 12-2__Scheduling an activity to fire in the next 10 minutes

Objective-C

1. `activity.tolerance = 10 * 60;`

Swift

1. `activity.tolerance = 10 * 60`

__Listing 12-3__Scheduling an activity to fire between 15 and 45 minutes from now

Objective-C

1. `activity.interval = 30 * 60;`
2. `activity.tolerance = 15 * 60;`

Swift

1. `activity.interval = 30 * 60`
2. `activity.tolerance = 15 * 60`

__Listing 12-4__Scheduling an activity to fire once each hour

Objective-C

1. `activity.repeats = YES;`
2. `activity.interval = 60 * 60;`

Swift

1. `activity.repeats = true`
2. `activity.interval = 60 * 60`

### Schedule Activity with scheduleWithBlock:

When you’re ready to schedule the activity, call [scheduleWithBlock:](https://developer.apple.com/documentation/foundation/nsbackgroundactivityscheduler/1412813-schedulewithblock) and provide a block of code to execute when the scheduler runs, as shown in Listing 12-5. The block will be called on a serial background queue appropriate for the level of quality of service specified. The system automatically uses the [beginActivityWithOptions:reason:](https://developer.apple.com/documentation/foundation/nsprocessinfo/1415995-beginactivitywithoptions) method (of [NSProcessInfo](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSProcessInfo/Description.html#//apple_ref/occ/cl/NSProcessInfo)) while invoking the block, choosing appropriate options based on the specified quality of service.

When your block is called, it’s passed a completion handler as an argument. Configure the block to invoke this handler, passing it a result of type [NSBackgroundActivityResult](https://developer.apple.com/documentation/foundation/nsbackgroundactivityresult) to indicate whether the activity finished ([NSBackgroundActivityResultFinished](https://developer.apple.com/documentation/foundation/nsbackgroundactivityscheduler/result/finished)) or should be deferred ([NSBackgroundActivityResultDeferred](https://developer.apple.com/documentation/foundation/nsbackgroundactivityresult/nsbackgroundactivityresultdeferred)) and rescheduled for a later time. Failure to invoke the completion handler results in the activity not being rescheduled. For work that will be deferred and rescheduled, the block may optionally adjust scheduler properties, such as [interval](https://developer.apple.com/documentation/foundation/nsbackgroundactivityscheduler/1408819-interval) or [tolerance](https://developer.apple.com/documentation/foundation/nsbackgroundactivityscheduler/1408138-tolerance), prior to calling the completion handler.

__Listing 12-5__Scheduling background activity

Objective-C

1. `[activity`
2. `scheduleWithBlock:^(NSBackgroundActivityCompletionHandler completion) {`
3. `// Perform the activity`
4. `self.completion(NSBackgroundActivityResultFinished);`
5. `}];`

Swift

1. `activity.scheduleWithBlock() { (completion: NSBackgroundActivityCompletionHandler) in`
2. `// Perform the activity`
3. `self.completion(NSBackgroundActivityResult.Finished)`
4. `}`

### Detect Whether to Defer Activity

It’s conceivable that while a lengthy activity is running, conditions may change, resulting in the activity now requiring deferral. For example, perhaps the user has unplugged the Mac and it’s now running on battery power. Your activity can call [shouldDefer](https://developer.apple.com/documentation/foundation/nsbackgroundactivityscheduler/1412167-shoulddefer) to determine whether this has occurred. A value of `YES``true` indicates that the block should finish up what it’s currently doing and invoke its completion handler with a value of [NSBackgroundActivityResultDeferred](https://developer.apple.com/documentation/foundation/nsbackgroundactivityresult/nsbackgroundactivityresultdeferred). See Listing 12-6.

__Listing 12-6__Detecting deferred background activity

Objective-C

1. `if ([activity shouldDefer]) {`
2. `// Wrap up processing and prepare to defer activity`
3. `self.completion(NSBackgroundActivityResultDeferred);`
4. `} else {`
5. `// Continue processing`
6. `self.completion(NSBackgroundActivityResultFinished);`
7. `};`

Swift

1. `if activity.shouldDefer {`
2. `// Wrap up processing and prepare to defer activity`
3. `self.completion(NSBackgroundActivityResult.Deferred)`
4. `} else {`
5. `// Continue processing`
6. `self.completion(NSBackgroundActivityResult.Finished)`
7. `}`

### Stop Activity

Call `invalidate` to stop scheduling an activity, as shown in Listing 12-7.

__Listing 12-7__Stopping background activity

Objective-C

1. `[activity invalidate];`

Swift

1. `activity.invalidate()`

> [!NOTE]
> 

### Specify Nondeferrable Background Activities

If your app performs background work that can’t be deferred, call either [beginActivityWithOptions:reason:](https://developer.apple.com/documentation/foundation/nsprocessinfo/1415995-beginactivitywithoptions) (Listing 12-8) or [performActivityWithOptions:reason:usingBlock:](https://developer.apple.com/documentation/foundation/processinfo/1418048-performactivity) (Listing 12-9) and pass the [NSActivityBackground](https://developer.apple.com/documentation/foundation/nsactivityoptions/nsactivitybackground) constant. Doing so lets the system know that the work your app is performing is important, and helps with the prioritization and management of other tasks that may be occurring at the same time.

__Listing 12-8__Calling the `beginActivityWithOptions` method to inform the system of an asynchronous background activity

Objective-C

1. `NSOperationQueue *myQueue = [[NSOperationQueue alloc] init];`
2. `id myBackgroundActivity = [[NSProcessInfo processInfo]`
3. `beginActivityWithOptions: NSActivityBackground`
4. `reason: @"Doing important background work"];`
5. `[myQueue addOperationWithBlock:^{`
6. `// Do important background work here`
7. `[[NSProcessInfo processInfo] endActivity:myBackgroundActivity];`
8. `}];`

Swift

1. `let myQueue = NSOperationQueue()`
2. `let myBackgroundActivity = NSProcessInfo.processInfo()`
3. `myBackgroundActivity.beginActivityWithOptions(NSActivityOptions.Background,`
4. `reason: "Doing important background work")`
5. `myQueue.addOperationWithBlock() {`
6. `// Do important background work here`
7. `NSProcessInfo.processInfo().endActivity(myBackgroundActivity)`
8. `}`

__Listing 12-9__Calling the `performActivityWithOptions:reason:usingBlock:` method to inform the system of a synchronous background activity

Objective-C

1. `[[NSProcessInfo processInfo] performActivityWithOptions: NSActivityBackground`
2. `reason: @"Performing important background work."`
3. `usingBlock: ^{`
4. `// Do important background work here`
5. `}`
6. `];`

Swift

1. `NSProcessInfo.processInfo().performActivityWithOptions(NSActivityOptions.Background,`
2. `reason: "Performing important background work.") {`
3. `// Do important background work here`
4. `}`

[Manage Tasks with CTS and GCD](DiscretionaryTasks.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgeztsmrzfvbuqmzufvjvomi)

[Schedule Background Networking](SchedulingNetworkActivity.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgeztsmrzfvbuqmztfvjvomi)
