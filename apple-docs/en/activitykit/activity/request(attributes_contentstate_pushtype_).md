---
title: 'request(attributes:contentState:pushType:)'
framework: ActivityKit
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [iOS 16.1+（16.2 起废弃）, iPadOS 16.1+（16.2 起废弃）]
languages: [swift]
beta: false
deprecated: true
doc_path: '/documentation/activitykit/activity/request(attributes:contentstate:pushtype:)'
source_url: 'https://developer.apple.com/documentation/activitykit/activity/request(attributes:contentstate:pushtype:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/activitykit/activity/request%28attributes%3Acontentstate%3Apushtype%3A%29.json'
content_hash: 'sha256:7f6245c8eba8440e'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [ActivityKit](../../activitykit.md) · [Activity](../activity.md)

# request(attributes:contentState:pushType:)

<sub>Type Method</sub>

Requests and starts a Live Activity.

> [!warning] Deprecated
> Use request(attributes:content:pushType:) instead

<sub>iOS, iPadOS, Mac Catalyst</sub>

```swift
static func request(attributes: Attributes, contentState: Activity<Attributes>.ContentState, pushType: PushType? = nil) throws -> Activity<Attributes>
```

## Parameters

- `attributes` — A set of attributes that describe the Live Activity and its static content.

- `contentState` — A structure that describes the dynamic content of the Live Activity that changes over time.

- `pushType` — A value that indicates whether the Live Activity receives updates to its dynamic content with ActivityKit push notifications. Pass `nil` to start a Live Activity that only receives updates from the app with the [update(_:)](<update(__).md>) function. To start a Live Activity that receives updates to its dynamic content with ActivityKit push notifications in addition to the [update(_:)](<update(__).md>) function, pass [token](../pushtype/token.md) to this parameter.

## Return Value

The object that represents the started Live Activity.

## Discussion

Use this function to request and start a Live Activity from your app while it’s in the foreground. Note that you can’t do this while your app is in the background, unless you adopt [App Intents](../../appintents.md) and start the Live Activity using a [LiveActivityIntent](../../appintents/liveactivityintent.md).

If your Live Activity displays image assets, the system requires them to use a resolution that’s smaller or equal to the size of the Live Activity presentation for a device. If you use an image asset that’s larger than the size of the Live Activity presentation, the system may fail to start the Live Activity. For information about the sizes of Live Activity presentations, see [Human Interface Guidelines \> Live Activities](https://developer.apple.com/design/human-interface-guidelines/components/system-experiences/live-activities).

For additional information on starting a Live Activity, see [Displaying live data with Live Activities](../displaying-live-data-with-live-activities.md).

> [!danger] Throws
> [ActivityAuthorizationError](../activityauthorizationerror.md) if the app can’t start a new Live Activity. For example, [ActivityAuthorizationError.denied](../activityauthorizationerror/denied.md) indicates that a person deactivated Live Activities for the app.

## See Also

### Deprecated

- [update(using:)](<update(using_).md>) — Updates the dynamic content of the Live Activity. _(deprecated)_
- [update(using:alertConfiguration:)](<update(using_alertconfiguration_).md>) — Updates the dynamic content of a Live Activity and alerts a person about the Live Activity update. _(deprecated)_
- [end(using:dismissalPolicy:)](<end(using_dismissalpolicy_).md>) — Ends an active Live Activity. _(deprecated)_
- [contentState](contentstate-swift.property.md) — The dynamic content of a Live Activity. _(deprecated)_
- [contentStateUpdates](contentstateupdates-swift.property.md) — An asynchronous sequence you use to observe changes to the dynamic content of a Live Activity. _(deprecated)_
- [ContentStateUpdates](contentstateupdates-swift.struct.md) — A structure that offers functionality to observe changes to the dynamic content of a Live Activity. _(deprecated)_
