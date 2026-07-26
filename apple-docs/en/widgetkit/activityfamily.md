---
title: ActivityFamily
framework: WidgetKit
symbol_kind: enum
role: symbol
role_heading: Enumeration
platforms: [iOS 18.0+, iPadOS 18.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/widgetkit/activityfamily
source_url: 'https://developer.apple.com/documentation/widgetkit/activityfamily'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/widgetkit/activityfamily.json'
content_hash: 'sha256:f793e94cbbe58372'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [WidgetKit](../widgetkit.md)

# ActivityFamily

<sub>Enumeration</sub>

A family that defines the Live Activity’s size.

<sub>iOS, iPadOS, Mac Catalyst</sub>

```swift
enum ActivityFamily
```

## Overview

Live Activities support one or more sizes, giving you the flexibility to configure them for different devices. A Live Activity renders for a specific family, depending on both the device and the location in which it’s displayed.

A Live Activity initiated on one device can be sent to a remote device that renders the Live Activity at a different family size. For example, if your Live Activity is running on an iOS or iPadOS device, it natively renders with an [ActivityFamily.medium](activityfamily/medium.md) family. If you want to opt in to customize the rendering for a Live Activity for the watchOS Smart Stack, use the [ActivityFamily.small](activityfamily/small.md) family modifier.

When you define your Live Activity’s configuration, specify the sizes your Live Activity supports using the [supplementalActivityFamilies(_:)](<../swiftui/widgetconfiguration/supplementalactivityfamilies(__).md>) property modifier.

When you render the content of the Live Activity, use [activityFamily](../swiftui/environmentvalues/activityfamily.md) to read the current family and lay out your content appropriately. The code below uses [supplementalActivityFamilies(_:)](<../swiftui/widgetconfiguration/supplementalactivityfamilies(__).md>) to specify the size of the Live Activity for devices on iOS and watchOS.

```swift
// A RideSharingActivity that supports the watchOS Smart Stack and the iOS Lock Screen.
struct RideSharingActivity: Widget {
   var body: some WidgetConfiguration {
       ActivityConfiguration(for: RideAttributes.self) { context in
           RideSharingView(context: context)
       } dynamicIsland: { context in
           DynamicIsland {
               DynamicIslandExpandedRegion(.bottom) {
                   RideShareDetails()
               }
           } compactLeading: {
               AppLogo()
           } compactTrailing: {
               ETAView()
           } minimal: {
               ETAView()
           }
       }
       .supplementalActivityFamilies([.small, .medium])
   }
}
```

## Relationships

- **Conforms To**: [Copyable](../swift/copyable.md), [CustomStringConvertible](../swift/customstringconvertible.md), [Decodable](../swift/decodable.md), [Encodable](../swift/encodable.md), [Equatable](../swift/equatable.md), [Escapable](../swift/escapable.md), [Hashable](../swift/hashable.md), [RawRepresentable](../swift/rawrepresentable.md)

## Topics

### Accessing system families

- [ActivityFamily.small](activityfamily/small.md) — A size family of a Live Activity on watchOS.
- [ActivityFamily.medium](activityfamily/medium.md) — A size family of a Live Activity on iOS and macOS.

### Environment keys

- [SupportedActivityFamiliesEnvironmentKey](supportedactivityfamiliesenvironmentkey.md) — An environment key for the size of a rendered Live Activity.

## See Also

### Live Activity setup

- [Displaying live data with Live Activities](../activitykit/displaying-live-data-with-live-activities.md) — Display up-to-date data and offer quick interactions in the Dynamic Island, on the Lock Screen, in CarPlay, and on a paired Mac or Apple Watch.
- [ActivityKit](../activitykit.md) — Share live updates from your app as Live Activities on iPhone, iPad, Apple Watch, and the Mac.
- [Creating a widget extension](creating-a-widget-extension.md) — Display your app’s content in a convenient, informative widget on various devices.
- [Emoji Rangers: Supporting Live Activities, interactivity, and animations](emoji-rangers-supporting-live-activities-interactivity-and-animations.md) — Offer Live Activities, controls, animate data updates, and add interactivity to widgets.
- [ActivityConfiguration](activityconfiguration.md) — An object that describes the content of a Live Activity.
- [DynamicIsland](dynamicisland.md) — The layout and configuration for a Live Activity that appears in the Dynamic Island.
- [NSUserActivityTypeLiveActivity](nsuseractivitytypeliveactivity.md) — A string that the system passes to the app on launch from a Live Activity that doesn’t provide a URL.
- [ActivityPreviewViewKind](activitypreviewviewkind.md) — Values that represent Live Activity presentations for use in Xcode previews.
