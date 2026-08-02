---
title: Energy Efficiency Guide for Mac Apps
apple_id: TP40013929
resource_type: Guide
platform: macOS
topic: Performance
technology: null
published: '2016-09-13'
source_url: https://developer.apple.com/library/archive/documentation/Performance/Conceptual/power_efficiency_guidelines_osx/RespondToThermalStateChanges.html
archived_at: '2026-07-18T01:50:23.583371Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Energy Efficiency Guide for Mac Apps](index.md)



## Respond to Thermal State Changes

As more apps use more resources on a device, the system may begin enacting measures to stay cool and responsive. Strictly adhering to energy guidelines is the best way for app developers to proactively assist the system in this regard. However, apps can register to receive notifications when thermal state changes occur, such as when another app on the system is operating inefficiently and causes the temperature to rise. Apps can also call Foundation framework APIs in `NSProcessInfo` to inquire about the thermal state of the device at any time.

Through thermal state awareness, apps with a high energy impact can take corrective actions to help the system return to an acceptable level if heat elevation does occur. As a result of a collaborative effort to keep heat low, users will experience cooler, quieter, and more responsive devices that also have great battery life.

> [!IMPORTANT]
> 

### Thermal States

There are four possible thermal states for a device, which are defined in `NSProcessInfoThermalState`. See Table 18-1.

__Table 18-1__Impact and recommendations for different thermal states

| State/constant | Impact | Recommended action |
| --- | --- | --- |
| Nominal /  `NSProcessInfoThermalStateNominal` | The device's temperature-related conditions (thermals) are at an acceptable level. There is no noticeable negative impact to the user. | No corrective action is necessary. As always, all apps should be proactive about optimizing energy use, in order to help ensure that thermals do not begin to rise. For example, discretionary background work should be assigned quality of service levels and scheduled for execution at optimal times using `NSBackgroundActivityScheduler` or an `NSURLSession` background session. |
| Fair /  `NSProcessInfoThermalStateFair` | Thermals are minimally elevated. On devices with fans, those fans may become active, audible, and distracting to the user. Energy usage is elevated, potentially reducing battery life. | Although no corrective action is required, reaching this level provides an opportunity for greater proactive action. An app can begin reducing CPU usage and enacting other energy-saving measures to help ensure that the thermal state doesn’t rise any further. |
| Serious /  `NSProcessInfoThermalStateSerious` | Thermals are highly elevated. Fans are active, running at maximum speed, audible, and distracting to the user. System performance may also be impacted as the system begins enacting countermeasures to reduce thermals to a more acceptable level. | Apps should begin to take corrective action to help the system reduce thermals and create a more optimal user experience. To achieve this, wherever possible, apps should:   - Reduce CPU usage. - Reduce GPU usage. - Reduce I/O. - Reduce frame rates. - Use lower-quality visual effects. |
| Critical /`NSProcessInfoThermalStateCritical` | Thermals are significantly elevated. The device needs to cool down. | Apps can help the system by taking immediate corrective action to reduce usage of the CPU, GPU, and I/O to the absolute minimum level necessary in order to respond to user actions. Wherever possible, apps can stop using peripherals, such as the camera. |

### Register for Thermal State Notifications

An app can register to receive notifications when the thermal state of a device changes. These notifications are posted on the global dispatch queue.

To register for thermal notifications, send the message [addObserver:selector:name:object:](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSNotificationCenter/Description.html#//apple_ref/occ/instm/NSNotificationCenter/addObserver:selector:name:object:) to the default notification center of your app (an instance of [NSNotificationCenter](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSNotificationCenter/Description.html#//apple_ref/occ/cl/NSNotificationCenter)). Pass it a selector to call and `NSProcessInfoThermalStateDidChangeNotification`, as shown in Listing 18-1.

Once an app receives notification of a thermal state change, it can query `thermalState` in order to determine the current thermal state. See Listing 18-2. The app can then take proactive or corrective action, as appropriate.

__Listing 18-1__Registering for thermal state change notifications

Objective-C

1. `[NSNotificationCenter defaultCenter] addObserver:self`
2. `selector: @selector(yourMethodName:)`
3. `name: NSProcessInfoThermalStateDidChangeNotification`
4. `object: nil];`

Swift

1. `NSNotificationCenter.defaultCenter().addObserver(`
2. `self,`
3. `selector: "yourMethodName:",`
4. `name: NSProcessInfoThermalStateDidChangeNotification,`
5. `object: nil`
6. `)`

> [!NOTE]
> 

### Determine the Thermal State

An app can query the current thermal state of a device at any time by accessing the `thermalState` property of `NSProcessInfo`, as shown in Listing 18-2. If the device’s thermal state is unknown, or if the device doesn’t support thermal awareness, then this property will always present thermals as nominal.

__Listing 18-2__Accessing the thermal state of a device

Objective-C

1. `NSProcessInfoThermalState state = [[NSProcessInfo processInfo] thermalState];`
2. `if (state == NSProcessInfoThermalStateFair) {`
3. `// Thermals are fair. Consider taking proactive measures to prevent higher thermals.`
4. `} else if (state == NSProcessInfoThermalStateSerious) {`
5. `// Thermals are highly elevated. Help the system by taking corrective action.`
6. `} else if (state == NSProcessInfoThermalStateCritical) {`
7. `// Thermals are seriously elevated. Help the system by taking immediate corrective action.`
8. `} else {`
9. `// Thermals are okay. Go about your business.`
10. `};`

Swift

1. `let state = NSProcessInfo.processInfo().thermalState;`
2. `if state == NSProcessInfoThermalStateFair {`
3. `// Thermals are fair. Consider taking proactive measures to prevent higher thermals.`
4. `} else if state == NSProcessInfoThermalStateSerious {`
5. `// Thermals are highly elevated. Help the system by taking corrective action.`
6. `} else if state == NSProcessInfoThermalStateCritical {`
7. `// Thermals are seriously elevated. Help the system by taking immediate corrective action.`
8. `} else {`
9. `// Thermals are okay. Go about your business.`
10. `}`

[Check the Battery Status Menu](MonitoringBatteryUsage.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgeztsmrzfvbuqmrtfvjvomi)

[Test Performance](TestPerformance.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgeztsmrzfvbuqmrzfvjvomi)
