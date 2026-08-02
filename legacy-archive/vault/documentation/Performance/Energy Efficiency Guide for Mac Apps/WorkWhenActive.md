---
title: Energy Efficiency Guide for Mac Apps
apple_id: TP40013929
resource_type: Guide
platform: macOS
topic: Performance
technology: null
published: '2016-09-13'
source_url: https://developer.apple.com/library/archive/documentation/Performance/Conceptual/power_efficiency_guidelines_osx/WorkWhenActive.html
archived_at: '2026-07-18T01:50:31.054304Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Energy Efficiency Guide for Mac Apps](index.md)



## Notify Your App When Active State Changes

As previously discussed, your app is automatically placed into a lower-powered state (App Nap) when certain criteria are met. However, you shouldn’t wait for the system to enact this measure. Your app can begin winding down activity once it’s notified that it’s about to become inactive (no longer frontmost), even if all or part of its window is still visible.

### Implement Active App Transition Delegate Methods

Implement [NSApplicationDelegate](https://developer.apple.com/documentation/appkit/nsapplicationdelegate) methods in your app delegate to receive calls when the active state of your app—whether it’s in the foreground—changes.

### applicationWillResignActive

The [applicationWillResignActive:](https://developer.apple.com/documentation/appkit/nsapplicationdelegate/1428539-applicationwillresignactive) method is called immediately before your app is no longer the foreground (frontmost) app, as shown in Listing 4-1. This is a good place to start winding down activity that can be stopped entirely once the change in state has completed.

__Listing 4-1__Preparing to stop operations before your app becomes inactive

Objective-C

1. `- (void)applicationWillResignActive:(NSNotification *)aNotification {`
2. `// Prepare to halt operations, animations, and UI updates`
3. `}`

Swift

1. `func applicationWillResignActive(_ aNotification: NSNotification) {`
2. `// Prepare to halt operations, animations, and UI updates`
3. `})`

### applicationDidResignActive

The [applicationDidResignActive:](https://developer.apple.com/documentation/appkit/nsapplicationdelegate/1428636-applicationdidresignactive) method is called immediately after your app gives up its position as the foreground app, as shown in Listing 4-2. Stop any power-intensive operations, animations, and UI updates to the extent possible.

__Listing 4-2__Stopping operations when your app becomes inactive

Objective-C

1. `- (void)applicationDidResignActive:(NSNotification *)aNotification {`
2. `// Halt operations, animations, and UI updates`
3. `}`

Swift

1. `func applicationDidResignActive(_ aNotification: NSNotification) {`
2. `// Halt operations, animations, and UI updates`
3. `})`

### applicationWillBecomeActive

The [applicationWillBecomeActive:](https://developer.apple.com/documentation/appkit/nsapplicationdelegate/1428699-applicationwillbecomeactive) method is called immediately before your app comes to the front, as shown in Listing 4-3. Start resuming operations.

__Listing 4-3__Preparing to resume operations before your app becomes active

Objective-C

1. `- (void)applicationWillBecomeActive:(NSNotification *)aNotification {`
2. `// Prepare to resume operations, animations, and UI updates`
3. `}`

Swift

1. `func applicationWillBecomeActive(_ aNotification: NSNotification) {`
2. `// Prepare to resume operations, animations, and UI updates`
3. `})`

### applicationDidBecomeActive

The [applicationDidBecomeActive:](https://developer.apple.com/documentation/appkit/nsapplicationdelegate/1428577-applicationdidbecomeactive) method is called immediately after your app becomes the frontmost app, as shown in Listing 4-4. Fully resume operations that were halted.

__Listing 4-4__Resuming operations when your app becomes active

Objective-C

1. `- (void)applicationDidBecomeActive:(NSNotification *)aNotification {`
2. `// Resume operations, animations, and UI updates`
3. `}`

Swift

1. `func applicationDidBecomeActive(_ aNotification: NSNotification) {`
2. `// Resume operations, animations, and UI updates`
3. `})`

### Implement Active App Transition Notifications

In addition to implementing app transition delegate methods, register to receive notifications when changes in state occur by sending the message `addObserver:selector:name:object:` to the default notification center of your app (an instance of [NSNotificationCenter](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSNotificationCenter/Description.html#//apple_ref/occ/cl/NSNotificationCenter)). Pass it a selector to call and the name of the notification to receive. For changes in active state, register for any of the following notifications:

- [NSApplicationWillResignActiveNotification](https://developer.apple.com/documentation/appkit/nsapplicationwillresignactivenotification)
- [NSApplicationDidResignActiveNotification](https://developer.apple.com/documentation/appkit/nsapplicationdidresignactivenotification)
- [NSApplicationWillBecomeActiveNotification](https://developer.apple.com/documentation/appkit/nsapplication/1428383-willbecomeactivenotification)
- [NSApplicationDidBecomeActiveNotification](https://developer.apple.com/documentation/appkit/nsapplicationdidbecomeactivenotification)

Listing 4-5 demonstrates how to register for a notification.

__Listing 4-5__Registering for an app transition notification

Objective-C

1. `[[NSNotificationCenter defaultCenter] addObserver:self`
2. `selector:@selector(yourMethodName:)`
3. `name:NSApplicationDidResignActiveNotification`
4. `object:nil];`
5. `)`

Swift

1. `NSNotificationCenter.defaultCenter().addObserver(`
2. `self,`
3. `selector: "yourMethodName:",`
4. `name: NSApplicationDidResignActiveNotification,`
5. `object: nil`
6. `)`

[Extend App Nap](AppNap.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgeztsmrzfvbuqmrnknltc)

[Notify Your App When Visibility Changes](WorkWhenVisible.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgeztsmrzfvbuqmjyfvjvomi)
