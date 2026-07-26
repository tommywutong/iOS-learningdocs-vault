---
title: Processing queued notifications
framework: UIKit
symbol_kind: article
role: article
role_heading: Article
platforms: []
languages: [swift, swift, swift, occ, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/processing-queued-notifications
source_url: 'https://developer.apple.com/documentation/uikit/processing-queued-notifications'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/processing-queued-notifications.json'
content_hash: 'sha256:ee2c50293411f934'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [UIKit](../uikit.md) · [App and environment](app-and-environment.md) · [Scenes](scenes.md) · [Preparing your UI to run in the foreground](preparing-your-ui-to-run-in-the-foreground.md)

# Processing queued notifications

<sub>Article</sub>

Respond to notifications when coming out of the suspended state.

## Overview

When settings or device conditions change, the system generates notifications so that apps can respond accordingly. These notifications are delivered immediately to apps that are running, but their delivery is delayed for apps that are suspended. For a suspended app, pending notifications are delivered as soon after the app begins running again (either in the foreground or in the background).

The following table lists the notifications that apps can receive after they start running again. You must explicitly add an observer to these notifications to receive them. The system coalesces multiple related notifications so that the app receives only one notification with the net changes.

| Event | Notifications |
|---|---|
| The user changed your app’s preferences | [didChangeNotification](../foundation/userdefaults/didchangenotification.md) |
| The current language or locale settings changed | [currentLocaleDidChangeNotification](../foundation/nslocale/currentlocaledidchangenotification.md) |
| The screen mode of a display changes | [UIScreenModeDidChangeNotification](uiscreen/modedidchangenotification.md) |
| An external display is connected or disconnected | [UIScreenDidConnectNotification](uiscreen/didconnectnotification.md) ![](../../../attachments/67dc4b07a8d84366d4cc0e812eb40b4a/spacer.png) [UIScreenDidDisconnectNotification](uiscreen/diddisconnectnotification.md) |
| An accessory is connected or disconnected | [EAAccessoryDidConnect](../foundation/nsnotification/name-swift.struct/eaaccessorydidconnect.md) (Swift) or [EAAccessoryDidConnectNotification](../externalaccessory/eaaccessorydidconnectnotification.md) (Objective-C) ![](../../../attachments/67dc4b07a8d84366d4cc0e812eb40b4a/spacer.png) [EAAccessoryDidDisconnect](../foundation/nsnotification/name-swift.struct/eaaccessorydiddisconnect.md) (Swift) or [EAAccessoryDidDisconnectNotification](../externalaccessory/eaaccessorydiddisconnectnotification.md) (Objective-C) |
| The status of the user’s iCloud account changed | [NSUbiquityIdentityDidChange](../foundation/nsnotification/name-swift.struct/nsubiquityidentitydidchange.md) |
| The device orientation changed | [UIDeviceOrientationDidChangeNotification](uidevice/orientationdidchangenotification.md) ![](../../../attachments/67dc4b07a8d84366d4cc0e812eb40b4a/spacer.png) (UIKit automatically updates the interface orientation of your view controllers when appropriate.) |
| There was a significant time change | [UIApplicationSignificantTimeChangeNotification](uiapplication/significanttimechangenotification.md) |
| The battery level or battery state changed | [UIDeviceBatteryLevelDidChangeNotification](uidevice/batteryleveldidchangenotification.md) ![](../../../attachments/67dc4b07a8d84366d4cc0e812eb40b4a/spacer.png) [UIDeviceBatteryStateDidChangeNotification](uidevice/batterystatedidchangenotification.md) |
| The device’s proximity to the user changed | [UIDeviceProximityStateDidChangeNotification](uidevice/proximitystatedidchangenotification.md) |

When a suspended app starts running again, the system delivers any queued notifications on the app’s main thread before it delivers any touch events or user input. Handle all notifications as quickly as possible.
