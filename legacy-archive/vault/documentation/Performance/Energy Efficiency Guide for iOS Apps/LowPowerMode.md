---
title: Energy Efficiency Guide for iOS Apps
apple_id: TP40015243
resource_type: Guide
platform: watchOS|iOS
topic: Performance
technology: null
published: '2016-09-13'
source_url: https://developer.apple.com/library/archive/documentation/Performance/Conceptual/EnergyGuide-iOS/LowPowerMode.html
archived_at: '2026-07-18T01:47:55.884535Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Energy Efficiency Guide for iOS Apps](index.md)



## React to Low Power Mode on iPhones

Users who wish to prolong their iPhone’s battery life can enable Low Power Mode under Settings > Battery. In Low Power Mode, iOS conserves battery life by enacting certain energy-saving measures. For example, the system may:

- Reduce CPU and GPU performance
- Pause discretionary and background activities, including networking
- Reduce screen brightness
- Reduce the timeout for auto-locking the device
- Disable Mail fetch
- Disable motion effects
- Disable animated wallpapers

The mode automatically disables when the battery level rises to a sufficient level again.

Your app should take additional steps to help the system save energy when Low Power Mode is active. For example, your app could reduce the use of animations, lower frame rates, stop location updates, disable syncs and backups, and so on.

> [!NOTE]
> 

### Register for Power State Notifications

Your app can register to receive notifications when the power state (Low Power Mode is enabled or disabled) of the device changes. These notifications are posted on the global dispatch queue. See [Dispatch Queues](../../General/Concurrency%20Programming%20Guide/Concurrency%20and%20Application%20Design.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4daojrfvbuqmjqgawvgvzx) in _[Concurrency Programming Guide](../../General/Concurrency%20Programming%20Guide/Introduction.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4daojr)_.

To register for power state notifications, send the message [addObserver:selector:name:object:](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSNotificationCenter/Description.html#//apple_ref/occ/instm/NSNotificationCenter/addObserver:selector:name:object:) to the default notification center of your app (an instance of [NSNotificationCenter](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSNotificationCenter/Description.html#//apple_ref/occ/cl/NSNotificationCenter)). Pass it a selector to call and `NSProcessInfoPowerStateDidChangeNotification`, as shown in Listing 7-1.

Once your app is notified of a power state change, it should then query `isLowPowerModeEnabled` to determine the current power state. See Listing 7-2. If Low Power Mode is active, then your app can take appropriate steps to reduce activity. Otherwise, it can resume normal operations.

__Listing 7-1__Registering for power state change notifications

Objective-C

1. `[[NSNotificationCenter defaultCenter] addObserver:self`
2. `selector: @selector(yourMethodName:)`
3. `name: NSProcessInfoPowerStateDidChangeNotification`
4. `object: nil];`

Swift

1. `NSNotificationCenter.defaultCenter().addObserver(`
2. `self,`
3. `selector: “yourMethodName:”,`
4. `name: NSProcessInfoPowerStateDidChangeNotification,`
5. `object: nil`
6. `)`

### Determine the Power State

Your app can query the current power state at any time by accessing the `isLowPowerModeEnabled` property of the `NSProcessInfo` class, as shown in Listing 7-2. This property contains a boolean value, indicating whether Low Power Mode is enabled or disabled.

__Listing 7-2__Accessing the power state of a device

Objective-C

1. `if ([[NSProcessInfo processInfo] isLowPowerModeEnabled]) {`
2. `// Low Power Mode is enabled. Start reducing activity to conserve energy.`
3. `} else {`
4. `// Low Power Mode is not enabled.`
5. `};`

Swift

1. `if NSProcessInfo.processInfo().lowPowerModeEnabled {`
2. `// Low Power Mode is enabled. Start reducing activity to conserve energy.`
3. `} else {`
4. `// Low Power Mode is not enabled.`
5. `}`

> [!NOTE]
> 

[Minimize I/O](MinimizeIO.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge2tenbtfvbuqnbsfvjvomi)

[Energy and Networking](EnergyandNetworking.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge2tenbtfvbuqmjwfvjvomi)
