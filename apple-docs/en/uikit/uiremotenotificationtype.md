---
title: UIRemoteNotificationType
framework: UIKit
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 3.0+（8.0 起废弃）, iPadOS 3.0+（8.0 起废弃）, Mac Catalyst 13.1+（13.1 起废弃）]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: /documentation/uikit/uiremotenotificationtype
source_url: 'https://developer.apple.com/documentation/uikit/uiremotenotificationtype'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiremotenotificationtype.json'
content_hash: 'sha256:ffa145070bfed478'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [UIKit](../uikit.md)

# UIRemoteNotificationType

<sub>Structure</sub>

Constants indicating the types of notifications the app may display to the user.

> [!warning] Deprecated
> Use [UNAuthorizationOptions](../usernotifications/unauthorizationoptions.md) for user notifications and [- registerForRemoteNotifications](<uiapplication/registerforremotenotifications().md>) for receiving remote notifications instead.

<sub>iOS, iPadOS, Mac Catalyst</sub>

```swift
struct UIRemoteNotificationType
```

## Overview

One or more of the values in the `UIRemoteNotificationType` bit mask are passed to iOS as the argument of the [- registerForRemoteNotificationTypes:](<uiapplication/registerforremotenotifications(matching_).md>) method. Thereafter, iOS filters notifications for the app based on these values. You can always get the current notification types by calling the [- enabledRemoteNotificationTypes](<uiapplication/enabledremotenotificationtypes().md>) method.

## Relationships

- **Conforms To**: [BitwiseCopyable](../swift/bitwisecopyable.md), [Equatable](../swift/equatable.md), [ExpressibleByArrayLiteral](../swift/expressiblebyarrayliteral.md), [OptionSet](../swift/optionset.md), [RawRepresentable](../swift/rawrepresentable.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md), [SetAlgebra](../swift/setalgebra.md)

## Topics

### Constants

- [UIRemoteNotificationTypeBadge](uiremotenotificationtype/badge.md) — The app accepts notifications that badge the app icon. _(deprecated)_
- [UIRemoteNotificationTypeSound](uiremotenotificationtype/sound.md) — The app accepts alert sounds as notifications. _(deprecated)_
- [UIRemoteNotificationTypeAlert](uiremotenotificationtype/alert.md) — The app accepts alert messages as notifications. _(deprecated)_
- [UIRemoteNotificationTypeNewsstandContentAvailability](uiremotenotificationtype/newsstandcontentavailability.md) — The app accepts notifications that start the downloading of issue assets for Newsstand apps. _(deprecated)_

### Initializers

- [init(rawValue:)](<uiremotenotificationtype/init(rawvalue_).md>) _(deprecated)_

## See Also

### Deprecated methods

- [- requestSceneSessionActivation:userActivity:options:errorHandler:](<uiapplication/requestscenesessionactivation(__useractivity_options_errorhandler_).md>) — Asks the system to activate an existing scene, or create a new scene and associate it with your app. _(deprecated)_
- [- beginIgnoringInteractionEvents](<uiapplication/beginignoringinteractionevents().md>) — Tells the receiver to suspend the handling of touch-related events. _(deprecated)_
- [- endIgnoringInteractionEvents](<uiapplication/endignoringinteractionevents().md>) — Tells the receiver to resume the handling of touch-related events. _(deprecated)_
- [- setMinimumBackgroundFetchInterval:](<uiapplication/setminimumbackgroundfetchinterval(__).md>) — Specifies the minimum amount of time that must elapse between background fetch operations. _(deprecated)_
- [- scheduleLocalNotification:](<uiapplication/schedulelocalnotification(__).md>) — Schedules a local notification for delivery at its encapsulated date and time. _(deprecated)_
- [- presentLocalNotificationNow:](<uiapplication/presentlocalnotificationnow(__).md>) — Presents a local notification immediately. _(deprecated)_
- [- cancelLocalNotification:](<uiapplication/cancellocalnotification(__).md>) — Cancels the delivery of the specified scheduled local notification. _(deprecated)_
- [- cancelAllLocalNotifications](<uiapplication/cancelalllocalnotifications().md>) — Cancels the delivery of all scheduled local notifications. _(deprecated)_
- [- setKeepAliveTimeout:handler:](<uiapplication/setkeepalivetimeout(__handler_).md>) — Configures a periodic handler for VoIP apps in older versions of iOS. _(deprecated)_
- [UIMinimumKeepAliveTimeout](uiminimumkeepalivetimeout.md) — The minimum amount of time (measured in seconds) an app may run a critical background task in the background. _(deprecated)_
- [- clearKeepAliveTimeout](<uiapplication/clearkeepalivetimeout().md>) — Removes a previously installed periodic handler block. _(deprecated)_
- [- setStatusBarHidden:withAnimation:](<uiapplication/setstatusbarhidden(__with_).md>) — Hides or shows the status bar, optionally animating the transition. _(deprecated)_
- [- setStatusBarStyle:animated:](<uiapplication/setstatusbarstyle(__animated_).md>) — Sets the style of the status bar, optionally animating the transition to the new style. _(deprecated)_
- [- setStatusBarOrientation:animated:](<uiapplication/setstatusbarorientation(__animated_).md>) — Sets the app’s status bar to the specified orientation, optionally animating the transition. _(deprecated)_
- [- registerUserNotificationSettings:](<uiapplication/registerusernotificationsettings(__).md>) — Registers your preferred options for notifying the user. _(deprecated)_
