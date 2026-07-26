---
title: WKBluetoothAlertRefreshBackgroundTask
framework: WatchKit
symbol_kind: class
role: symbol
role_heading: Class
platforms: [watchOS 9.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/watchkit/wkbluetoothalertrefreshbackgroundtask
source_url: 'https://developer.apple.com/documentation/watchkit/wkbluetoothalertrefreshbackgroundtask'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/watchkit/wkbluetoothalertrefreshbackgroundtask.json'
content_hash: 'sha256:1f19136a9656f5d4'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [WatchKit](../watchkit.md)

# WKBluetoothAlertRefreshBackgroundTask

<sub>Class</sub>

A task for handling timely Bluetooth alerts in the background.

<sub>watchOS</sub>

```swift
class WKBluetoothAlertRefreshBackgroundTask
```

## Overview

Your app can receive [WKBluetoothAlertRefreshBackgroundTask](wkbluetoothalertrefreshbackgroundtask.md) tasks to handle timely alerts in the background. Use these tasks to reconnect a peripheral and handle a critical alert. Apps that use timely alerts can also scan for a specific system identifier (UUID) while in the background. You can then perform the initial connection and pair the devices if necessary.

To receive timely alerts, your peripheral must use Generic Attribute Profile (GATT) transactions. Call [setNotifyValue(_:for:)](<../corebluetooth/cbperipheral/setnotifyvalue(__for_).md>) to enable notifications for the specified characteristic. Then, any changes to the peripheral’s characteristic wakes your app using a [WKBluetoothAlertRefreshBackgroundTask](wkbluetoothalertrefreshbackgroundtask.md) task. Use this task to reconnect to the peripheral and handle the critical alert.

> [!note] Note
> In watchOS 9 and later, SwiftUI Background tasks are the preferred way to handle background tasks and interactions. For more information, [backgroundTask(_:action:)](<../swiftui/scene/backgroundtask(__action_).md>).

The critical alerts and background scans share a budget. Your app can only use five timely alerts or background scans within a rolling 24-hour window.

When your app receives a timely alert and your budget has only one Bluetooth alert task remaining, the system raises a [leGattNearBackgroundNotificationLimit](../corebluetooth/cberror-swift.struct/legattnearbackgroundnotificationlimit.md) error. If you exceed the budget, it raises a [leGattExceededBackgroundNotificationLimit](../corebluetooth/cberror-swift.struct/legattexceededbackgroundnotificationlimit.md) error. The system passes these errors to your [CBPeripheralDelegate](../corebluetooth/cbperipheraldelegate.md), by calling methods like the [peripheral(_:didUpdateValueFor:error:)](<../corebluetooth/cbperipheraldelegate/peripheral(__didupdatevaluefor_error_)-1xyna.md>) method.

If you exceed your budget, your app doesn’t receive any timely alerts until additional background budget becomes available. The user can reset this budget by launching your app.

## Relationships

- **Inherits From**: [WKRefreshBackgroundTask](wkrefreshbackgroundtask.md)

- **Conforms To**: [CVarArg](../swift/cvararg.md), [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md), [CustomStringConvertible](../swift/customstringconvertible.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [NSObjectProtocol](../objectivec/nsobjectprotocol.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md)

## See Also

### Background tasks

- [Using background tasks](using-background-tasks.md) — Handle scheduled update tasks in the background, and respond to background system interactions including Siri intents and incoming Bluetooth messages.
- [Preparing to take your watchOS app’s snapshot](preparing-to-take-your-watchos-app-s-snapshot.md) — Provide a timely, accurate snapshot of your app by using snapshot background tasks.
- [WKApplicationRefreshBackgroundTask](wkapplicationrefreshbackgroundtask.md) — A task that updates your app’s state in the background.
- [WKURLSessionRefreshBackgroundTask](wkurlsessionrefreshbackgroundtask.md) — A task that responds to background URL sessions.
- [WKWatchConnectivityRefreshBackgroundTask](wkwatchconnectivityrefreshbackgroundtask.md) — A background task used to receive background updates from the Watch Connectivity framework.
- [WKIntentDidRunRefreshBackgroundTask](wkintentdidrunrefreshbackgroundtask.md) — A background task used to update your app after a SiriKit intent runs.
- [WKRelevantShortcutRefreshBackgroundTask](wkrelevantshortcutrefreshbackgroundtask.md) — A background task used to periodically donate relevant Siri shortcuts.
- [WKSnapshotRefreshBackgroundTask](wksnapshotrefreshbackgroundtask.md) — A background task used to update your app’s user interface in preparation for a snapshot.
- [WKRefreshBackgroundTask](wkrefreshbackgroundtask.md) — The abstract superclass for WatchKit’s background task classes.
