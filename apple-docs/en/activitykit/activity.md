---
title: Activity
framework: ActivityKit
symbol_kind: class
role: symbol
role_heading: Class
platforms: [iOS 16.1+, iPadOS 16.1+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/activitykit/activity
source_url: 'https://developer.apple.com/documentation/activitykit/activity'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/activitykit/activity.json'
content_hash: 'sha256:d160da3c4f00dda1'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [ActivityKit](../activitykit.md)

# Activity

<sub>Class</sub>

The object you use to start, update, and end a Live Activity.

<sub>iOS, iPadOS, Mac Catalyst</sub>

```swift
class Activity<Attributes> where Attributes : ActivityAttributes
```

## Overview

The `Activity` object offers functionality to start, update, and end a Live Activity from within your app. You can update or end a Live Activity while your app is in the background, but you can only start a Live Activity while the app is in the foreground, unless you adopt [App Intents](../appintents.md) and start the Live Activity using a [LiveActivityIntent](../appintents/liveactivityintent.md).

Additionally, `Activity` offers functionality to observe changes to:

- The Live Activity
- The Live Activity’s state in its life cycle
- A person’s permission to start Live Activities
- The Live Activity’s push token if you configure it to receive updates through ActivityKit push notifications.

To observe these changes, use the asynchronous sequences the activity object offers; for example, use the [activityStateUpdates](activity/activitystateupdates-swift.property.md) sequence to observe changes to the state of a Live Activity.

## Relationships

- **Conforms To**: [Identifiable](../swift/identifiable.md)

## Topics

### Starting a Live Activity

- [request(attributes:content:pushType:)](<activity/request(attributes_content_pushtype_).md>) — Requests and starts a standard Live Activity.
- [request(attributes:content:pushType:style:)](<activity/request(attributes_content_pushtype_style_).md>) — Requests and starts a Live Activity.
- [request(attributes:content:pushType:style:alertConfiguration:start:)](<activity/request(attributes_content_pushtype_style_alertconfiguration_start_).md>) — Requests and schedules a Live Activity for a specific date.
- [request(attributes:content:pushType:style:alertConfiguration:startDate:)](<activity/request(attributes_content_pushtype_style_alertconfiguration_startdate_).md>) _(deprecated)_
- [attributes](activity/attributes.md) — A set of attributes that describe a Live Activity and its content.
- [ActivityAttributes](activityattributes.md) — The protocol you implement to describe the content of a Live Activity.
- [ActivityStyle](activitystyle.md)
- [content](activity/content.md) — The dynamic content of a Live Activity.
- [ActivityContent](activitycontent.md) — A structure that describes the state and configuration of a Live Activity.
- [ContentState](activity/contentstate-swift.typealias.md) — The type alias for the structure that describes the dynamic content of a Live Activity.
- [PushType](pushtype.md) — The structure that offers constants you use to configure a Live Activity to receive updates through ActivityKit push notifications.
- [ActivityAuthorizationError](activityauthorizationerror.md) — An error that indicates why the request to start a Live Activity failed.

### Updating a Live Activity

- [update(_:)](<activity/update(__).md>) — Updates the dynamic content of the Live Activity.
- [update(_:alertConfiguration:)](<activity/update(__alertconfiguration_).md>) — Updates the dynamic content of a Live Activity and alerts a person about the Live Activity update.
- [AlertConfiguration](alertconfiguration.md) — A structure you use to configure an alert that appears when you update your Live Activity.
- [update(_:alertConfiguration:timestamp:)](<activity/update(__alertconfiguration_timestamp_).md>) — Updates the dynamic content of a Live Activity and alerts a person about the Live Activity update.

### Ending a Live Activity

- [end(_:dismissalPolicy:)](<activity/end(__dismissalpolicy_).md>) — Ends an active Live Activity.
- [ActivityUIDismissalPolicy](activityuidismissalpolicy.md) — The structure that describes when the system should remove a Live Activity that ended.
- [end(_:dismissalPolicy:timestamp:)](<activity/end(__dismissalpolicy_timestamp_).md>) — Ends an active Live Activity.

### Observing Live Activity content changes

- [contentUpdates](activity/contentupdates-swift.property.md) — An asynchronous sequence you use to observe changes to the dynamic content of a Live Activity.
- [ContentUpdates](activity/contentupdates-swift.struct.md) — A structure that offers functionality to observe changes to the dynamic content of a Live Activity.

### Observing the Live Activity life cycle

- [activityState](activity/activitystate.md) — The current state of a Live Activity in its life cycle.
- [ActivityState](activitystate.md) — The enum that describes the state of a Live Activity in its life cycle.
- [activityStateUpdates](activity/activitystateupdates-swift.property.md) — An asynchronous sequence you use to observe activity state changes.
- [ActivityStateUpdates](activity/activitystateupdates-swift.struct.md) — A structure that offers functionality to observe state changes of a Live Activity.

### Using ActivityKit push notifications

- [pushToken](activity/pushtoken.md) — The token you use to send ActivityKit push notifications to a Live Activity.
- [pushTokenUpdates](activity/pushtokenupdates-swift.property.md) — An asynchronous sequence you use to observe changes to the push token of a Live Activity.
- [PushTokenUpdates](activity/pushtokenupdates-swift.struct.md) — A structure that offers functionality to observe changes to the push token of a Live Activity.
- [pushToStartToken](activity/pushtostarttoken.md) — The token you use to start a Live Activity with an ActivityKit push notification.
- [pushToStartTokenUpdates](activity/pushtostarttokenupdates.md) — An asynchronous sequence you use to observe changes to the token for starting a Live Activity with an ActivityKit push notification.

### Checking user authorization

- [ActivityAuthorizationInfo](activityauthorizationinfo.md) — An object with information about whether a person allowed your app to start Live Activities and permitted content updates with frequent ActivityKit push notifications.

### Accessing Live Activities

- [activities](activity/activities.md) — An array of your app’s current Live Activities.
- [activityUpdates](activity/activityupdates-swift.type.property.md) — An asynchronous sequence you use to observe changes to ongoing Live Activities and to asynchronously access a Live Activity when you start it.
- [ActivityUpdates](activity/activityupdates-swift.struct.md) — A structure that offers functionality to observe changes to a Live Activity.

### Identifying a Live Activity

- [id](activity/id.md) — A unique identifier for a Live Activity.
- [id](activity/id.md) — A unique identifier for a Live Activity.

### Deprecated

- [Deprecated symbols](deprecated-symbols.md) — Review unsupported symbols and their replacements.

## See Also

### Starting a Live Activity

- [Displaying live data with Live Activities](displaying-live-data-with-live-activities.md) — Display up-to-date data and offer quick interactions in the Dynamic Island, on the Lock Screen, in CarPlay, and on a paired Mac or Apple Watch.
- [Starting and updating Live Activities with ActivityKit push notifications](starting-and-updating-live-activities-with-activitykit-push-notifications.md) — Use ActivityKit to receive push tokens and to remotely start, update, and end your Live Activity with ActivityKit notifications.
- [Emoji Rangers: Supporting Live Activities, interactivity, and animations](../widgetkit/emoji-rangers-supporting-live-activities-interactivity-and-animations.md) — Offer Live Activities, controls, animate data updates, and add interactivity to widgets.
- [NSSupportsLiveActivities](../bundleresources/information-property-list/nssupportsliveactivities.md) — A Boolean value that indicates whether an app supports Live Activities.
- [NSSupportsLiveActivitiesFrequentUpdates](../bundleresources/information-property-list/nssupportsliveactivitiesfrequentupdates.md) — A Boolean value that indicates whether an app can update its Live Activities frequently.
