---
title: 'init(activityItems:applicationActivities:)'
framework: UIKit
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 6.0+, iPadOS 6.0+, Mac Catalyst 13.1+, visionOS 1.0+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uiactivityviewcontroller/init(activityitems:applicationactivities:)'
source_url: 'https://developer.apple.com/documentation/uikit/uiactivityviewcontroller/init(activityitems:applicationactivities:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiactivityviewcontroller/init%28activityitems%3Aapplicationactivities%3A%29.json'
content_hash: 'sha256:ba594b02a5518762'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIActivityViewController](../uiactivityviewcontroller.md)

# init(activityItems:applicationActivities:)

<sub>Initializer</sub>

Initializes a new activity view controller object that acts on the specified data.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
init(activityItems: [Any], applicationActivities: [UIActivity]?)
```

## Parameters

- `activityItems` — The array of data objects on which to perform the activity. The type of objects in the array is variable and dependent on the data your application manages. For example, the data might consist of one or more string or image objects representing the currently selected content. Instead of actual data objects, the objects in this array can be objects that adopt the [UIActivityItemSource](../uiactivityitemsource.md) protocol, such as [UIActivityItemProvider](../uiactivityitemprovider.md) objects. Source and provider objects act as proxies for the corresponding data in situations where you do not want to provide that data until it is needed. Note that you should not reuse an activity view controller object that includes a [UIActivityItemProvider](../uiactivityitemprovider.md) object in its `activityItems` array. This array must not be `nil` and must contain at least one object.

- `applicationActivities` — An array of [UIActivity](../uiactivity.md) objects representing the custom services that your application supports. This parameter may be `nil`.

## Return Value

The activity view controller to present.

## Discussion

It is your responsibility to present and dismiss the view controller using the appropriate means for the given device idiom. On iPad, you must present the view controller in a popover. On other devices, you must present it modally.

## See Also

### Initializing the activity view controller

- [- initWithActivityItemsConfiguration:](<init(activityitemsconfiguration_).md>) — Initializes a new activity view controller object that acts on the specified configuration.
- [UIActivityItemsConfiguration](../uiactivityitemsconfiguration.md) — A configuration that allows a responder to export data through a variety of interactions.
- [UIActivityItemsConfigurationReading](../uiactivityitemsconfigurationreading.md) — A set of methods adopted by an object so that the object can act as an activity items configuration.
