---
title: Energy Efficiency Guide for iOS Apps
apple_id: TP40015243
resource_type: Guide
platform: watchOS|iOS
topic: Performance
technology: null
published: '2016-09-13'
source_url: https://developer.apple.com/library/archive/documentation/Performance/Conceptual/EnergyGuide-iOS/WorkLessInTheBackground.html
archived_at: '2026-07-18T01:48:34.447913Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Energy Efficiency Guide for iOS Apps](index.md)



## Work Less in the Background

When the user isn’t actively using your app, the system places it into a background state. The system may eventually suspend your app if it’s not performing important work, such as finishing a task the user initiated or running in a specially declared background execution mode.

> [!IMPORTANT]
> 

You can use Energy organizer to view crash and energy reports that are generated from log information collected automatically from TestFlight users and with permission from users of the App Store versions of your apps. To learn more, see [Energy organizer](https://help.apple.com/xcode/mac/current/#/dev36a5a9141).

### Common Causes of Energy Wasted by Background Apps

Apps performing unnecessary background activity waste energy. The following are some common causes of wasted energy in background apps:

- Not notifying the system when background activity is complete
- Playing silent audio
- Performing location updates
- Interacting with Bluetooth accessories
- Downloads that could be deferred

### Suspend Activity When Your App Becomes Inactive or Moves to the Background

Implement [UIApplicationDelegate](https://developer.apple.com/documentation/uikit/uiapplicationdelegate) methods in your app delegate to receive calls and suspend activity when your app becomes inactive or transitions from the foreground to the background.

### applicationWillResignActive

The [applicationWillResignActive:](https://developer.apple.com/documentation/uikit/uiapplicationdelegate/1622950-applicationwillresignactive) method is called when your app enters an inactive state, such as when a phone call or text message comes in, or the user switches to another app and your app begins transitioning to a background state. This is a good place to pause activity, save data, and prepare for possible suspension. See Listing 3-1.

__Listing 3-1__Responding when your app becomes inactive

Objective-C

1. `- (void)applicationWillResignActive:(UIApplication *)application {`
2. `// Halt operations, animations, and UI updates`
3. `}`

Swift

1. `optional func applicationWillResignActive(_ application: UIApplication) {`
2. `// Halt operations, animations, and UI updates`
3. `})`

> [!IMPORTANT]
> 

### applicationDidEnterBackground

The [applicationDidEnterBackground:](https://developer.apple.com/documentation/uikit/uiapplicationdelegate/1622997-applicationdidenterbackground) method is called immediately after your app enters a background state. Stop any operations, animations, and UI updates immediately. See Listing 3-2.

__Listing 3-2__Responding when your app transitions to a background app

Objective-C

1. `- (void)applicationDidEnterBackground:(UIApplication *)application {`
2. `// Halt operations, animations, and UI updates immediately`
3. `}`

Swift

1. `optional func applicationDidEnterBackground(_ application: UIApplication) {`
2. `// Halt operations, animations, and UI updates immediately`
3. `})`

iOS allows only a few seconds for the `applicationDidEnterBackground` method to run. If your app needs more time to finish performing essential user initiated tasks, it should request more background execution time—the system allows up to a few more minutes of time on request. Call the [beginBackgroundTaskWithExpirationHandler:](https://developer.apple.com/documentation/uikit/uiapplication/1623031-beginbackgroundtaskwithexpiratio) method and pass it a handler, to be called if the extra time runs out. Next, run the remaining tasks on a dispatch queue or secondary thread.

When background tasks are done, call the [endBackgroundTask:](https://developer.apple.com/documentation/uikit/uiapplication/1622970-endbackgroundtask) method to let the system know processing is complete. If you don’t call this method and background execution time exhausts, then the completion handler is called to give you one last shot at wrapping things up. After that, your app is suspended. See Listing 3-3.

> [!IMPORTANT]
> 

__Listing 3-3__Requesting additional background processing time

Objective-C

1. `// Request additional background execution time`
2. `UIBackgroundTaskIdentifier bgTaskID = [[UIApplication sharedApplication] beginBackgroundTaskWithExpirationHandler:^{`
3. `// Completion handler to be performed if time runs out`
4. `}];`
6. `// Initiate background tasks`
8. `// Notify the system when the background tasks are done`
9. `[[UIApplication sharedApplication] endBackgroundTask:bgTaskID];`

Swift

1. `// Request additional background execution time`
2. `var bgTaskID: UIBackgroundTaskIdentifier = 0`
3. `bgTaskID = UIApplication.sharedApplication().beginBackgroundTaskWithExpirationHandler() {`
4. `// Completion handler to be performed if time runs out`
5. `}`
7. `// Initiate background tasks`
9. `// Notify the system when the background tasks are done`
10. `UIApplication.sharedApplication().endBackgroundTask(bgTaskID)`

### Resume Activity When Your App Becomes Active

Implement `UIApplicationDelegate` methods in your app delegate to receive calls and resume activity when your app becomes active again.

### applicationWillEnterForeground

The [applicationWillEnterForeground:](https://developer.apple.com/documentation/uikit/uiapplicationdelegate/1623076-applicationwillenterforeground) method is called immediately before your app transitions from a background app to the active app. Start resuming operations, loading data, reinitializing the UI, and getting your app ready for the user. See Listing 3-4.

__Listing 3-4__Responding right before your app transitions to the foreground

Objective-C

1. `- (void)applicationWillEnterForeground:(UIApplication *)application {`
2. `// Prepare to resume operations, animations, and UI updates`
3. `}`

Swift

1. `optional func applicationWillEnterForeground(_ application: UIApplication) {`
2. `// Prepare to resume operations, animations, and UI updates`
3. `})`

### applicationDidBecomeActive

The [applicationDidBecomeActive:](https://developer.apple.com/documentation/uikit/uiapplicationdelegate/1622956-applicationdidbecomeactive) method is called immediately after your app becomes the active app, after being launched by the system or transitioning from a background or inactive state. Fully resume any operations that were halted. See Listing 3-5.

__Listing 3-5__Responding after your app transitioned to the foreground

Objective-C

1. `- (void)applicationDidBecomeActive:(UIApplication *)application {`
2. `// Resume operations, animations, and UI updates`
3. `}`

Swift

1. `optional func applicationDidBecomeActive(_ application: UIApplication) {`
2. `// Resume operations, animations, and UI updates`
3. `})`

### Resolving Runaway Background App Crashes

iOS employs a CPU Monitor that watches background apps for excessive CPU usage and terminates them if they fall outside of certain limits. Most apps performing normal background activity should never encounter this situation. However, if your app reaches the limits and is terminated, the crash log indicates the reason for the termination. An exception type of `EXC_RESOURCE` and subtype of `CPU_FATAL` is specified, along with a message indicating that limits were exceeded. See Listing 3-6.

__Listing 3-6__Example of an Excess CPU Usage Crash Log Entry

1. `Exception Type: EXC_RESOURCE`
2. `Exception Subtype: CPU_FATAL`
3. `Exception Message: (Limit 80%) Observed 89% over 60 seconds`

The log also includes a stack trace, which lets you determine what your app was doing right before it was terminated. By analyzing the stack trace, you can identify the location of the runaway code and resolve it.

> [!NOTE]
> 

[Fundamental Concepts](FundamentalConcepts.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge2tenbtfvbuqnbnknltc)

[Prioritize Work with Quality of Service Classes](PrioritizeWorkWithQoS.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge2tenbtfvbuqmzzfvjvomi)
