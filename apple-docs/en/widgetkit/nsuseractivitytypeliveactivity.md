---
title: NSUserActivityTypeLiveActivity
framework: WidgetKit
symbol_kind: var
role: symbol
role_heading: Global Variable
platforms: [iOS, iPadOS, Mac Catalyst, macOS, visionOS, watchOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/widgetkit/nsuseractivitytypeliveactivity
source_url: 'https://developer.apple.com/documentation/widgetkit/nsuseractivitytypeliveactivity'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/widgetkit/nsuseractivitytypeliveactivity.json'
content_hash: 'sha256:ebc3dcd21d903e76'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [WidgetKit](../widgetkit.md)

# NSUserActivityTypeLiveActivity

<sub>Global Variable</sub>

A string that the system passes to the app on launch from a Live Activity that doesn’t provide a URL.

<sub>iOS, iPadOS, Mac Catalyst, macOS, visionOS, watchOS</sub>

```swift
let NSUserActivityTypeLiveActivity: String
```

## Discussion

In many cases, you use  [widgetURL(_:)](<../swiftui/view/widgeturl(__).md>) to allow users to tap a Live Activity and open a screen in the app with functionality that best fits the Live Activity. If you don’t use the `widgetURL(_:)` modifier to provide a URL, the system launches your app and passes `NSUserActivityTypeLiveActivity` as the [activityType](../foundation/nsuseractivity/activitytype.md) of [NSUserActivity](../foundation/nsuseractivity.md) upon launch. Check for this value on launch to open a screen in your app that fits the context of the active Live Activity.

## See Also

### Live Activity setup

- [Displaying live data with Live Activities](../activitykit/displaying-live-data-with-live-activities.md) — Display up-to-date data and offer quick interactions in the Dynamic Island, on the Lock Screen, in CarPlay, and on a paired Mac or Apple Watch.
- [ActivityKit](../activitykit.md) — Share live updates from your app as Live Activities on iPhone, iPad, Apple Watch, and the Mac.
- [Creating a widget extension](creating-a-widget-extension.md) — Display your app’s content in a convenient, informative widget on various devices.
- [Emoji Rangers: Supporting Live Activities, interactivity, and animations](emoji-rangers-supporting-live-activities-interactivity-and-animations.md) — Offer Live Activities, controls, animate data updates, and add interactivity to widgets.
- [ActivityConfiguration](activityconfiguration.md) — An object that describes the content of a Live Activity.
- [DynamicIsland](dynamicisland.md) — The layout and configuration for a Live Activity that appears in the Dynamic Island.
- [ActivityPreviewViewKind](activitypreviewviewkind.md) — Values that represent Live Activity presentations for use in Xcode previews.
- [ActivityFamily](activityfamily.md) — A family that defines the Live Activity’s size.
