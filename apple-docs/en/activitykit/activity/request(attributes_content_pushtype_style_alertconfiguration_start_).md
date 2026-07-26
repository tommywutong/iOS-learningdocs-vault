---
title: 'request(attributes:content:pushType:style:alertConfiguration:start:)'
framework: ActivityKit
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [iOS 26.0+, iPadOS 26.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/activitykit/activity/request(attributes:content:pushtype:style:alertconfiguration:start:)'
source_url: 'https://developer.apple.com/documentation/activitykit/activity/request(attributes:content:pushtype:style:alertconfiguration:start:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/activitykit/activity/request%28attributes%3Acontent%3Apushtype%3Astyle%3Aalertconfiguration%3Astart%3A%29.json'
content_hash: 'sha256:1e4e44499d2ca3d3'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [ActivityKit](../../activitykit.md) · [Activity](../activity.md)

# request(attributes:content:pushType:style:alertConfiguration:start:)

<sub>Type Method</sub>

Requests and schedules a Live Activity for a specific date.

<sub>iOS, iPadOS, Mac Catalyst</sub>

```swift
static func request(attributes: Attributes, content: ActivityContent<Activity<Attributes>.ContentState>, pushType: PushType? = nil, style: ActivityStyle, alertConfiguration: AlertConfiguration, start: Date) throws -> Activity<Attributes>
```

## Parameters

- `attributes` — A set of attributes that describe the Live Activity and its static content.

- `content` — A structure that describes the dynamic content of the Live Activity that changes over time.

- `pushType` — A value that indicates whether the Live Activity receives updates to its dynamic content with ActivityKit push notifications. Pass `nil` to start a Live Activity that only receives updates from the app with the [update(_:)](<update(__).md>) function. To start a Live Activity that receives updates to its dynamic content with ActivityKit push notifications in addition to the [update(_:)](<update(__).md>) function, pass [token](../pushtype/token.md) to this parameter.

- `style` — A flag that indicates whether the Live Activity uses standard or transient behavior. For most apps, passing [ActivityStyle.standard](../activitystyle/standard.md) is the best choice. It starts a standard Live Activity that continues until the app, a push notification, or a person ends it, or until it exceeds the maximum duration for Live Activities. By passing [ActivityStyle.transient](../activitystyle/transient.md), you start a Live Activity that appears in the extended presentation in the Dynamic Island but ends automatically when a person automatically locks the device, collapses the extended presentation, leaves the app, or performs other tasks outside the Dynamic Island.

- `alertConfiguration` — The alert configuration you use to configure how the system notifies a person about the updated content of the Live Activity.

- `start` — The date to schedule the start of your Live Activity; for example, for an upcoming sports game. You must provide an `alertConfiguration` to let people know that your app started a Live Activity. The [ActivityState](../activitystate.md) for a scheduled but not yet started Live Activity is [ActivityState.pending](../activitystate/pending.md).

## Return Value

The object that represents the Live Activity you started.

## Discussion

Use this function to request and start a Live Activity from your app while it’s in the foreground. Note that you can’t do this while your app is in the background, unless you adopt [App Intents](../../appintents.md) and start the Live Activity using a [LiveActivityIntent](../../appintents/liveactivityintent.md).

The system starts the Live Activity at the specified date, even if the app is in the background. Note that you must provide an [AlertConfiguration](../alertconfiguration.md). This makes sure that the system notifies people when your app starts the Live Activity.

> [!note] Note
> The system limits the number of simultaneous ongoing Live Activities. Scheduled Live Activities count towards this limit.

If your Live Activity displays image assets, the system requires them to use a resolution that’s smaller or equal to the size of the Live Activity presentation for a device. If you use an image asset that’s larger than the size of the Live Activity presentation, the system may fail to start the Live Activity. For information about the sizes of Live Activity presentations, see [Human Interface Guidelines \> Live Activities](https://developer.apple.com/design/human-interface-guidelines/components/system-experiences/live-activities).

For additional information on starting a Live Activity, see [Displaying live data with Live Activities](../displaying-live-data-with-live-activities.md).

> [!danger] Throws
> [ActivityAuthorizationError](../activityauthorizationerror.md) if the app can’t start a new Live Activity. For example, [ActivityAuthorizationError.denied](../activityauthorizationerror/denied.md) indicates that the person deactivated Live Activities for the app.

## See Also

### Starting a Live Activity

- [request(attributes:content:pushType:)](<request(attributes_content_pushtype_).md>) — Requests and starts a standard Live Activity.
- [request(attributes:content:pushType:style:)](<request(attributes_content_pushtype_style_).md>) — Requests and starts a Live Activity.
- [request(attributes:content:pushType:style:alertConfiguration:startDate:)](<request(attributes_content_pushtype_style_alertconfiguration_startdate_).md>) _(deprecated)_
- [attributes](attributes.md) — A set of attributes that describe a Live Activity and its content.
- [ActivityAttributes](../activityattributes.md) — The protocol you implement to describe the content of a Live Activity.
- [ActivityStyle](../activitystyle.md)
- [content](content.md) — The dynamic content of a Live Activity.
- [ActivityContent](../activitycontent.md) — A structure that describes the state and configuration of a Live Activity.
- [ContentState](contentstate-swift.typealias.md) — The type alias for the structure that describes the dynamic content of a Live Activity.
- [PushType](../pushtype.md) — The structure that offers constants you use to configure a Live Activity to receive updates through ActivityKit push notifications.
- [ActivityAuthorizationError](../activityauthorizationerror.md) — An error that indicates why the request to start a Live Activity failed.
