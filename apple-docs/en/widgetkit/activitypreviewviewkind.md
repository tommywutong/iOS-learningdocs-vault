---
title: ActivityPreviewViewKind
framework: WidgetKit
symbol_kind: enum
role: symbol
role_heading: Enumeration
platforms: [iOS 16.2+, iPadOS 16.2+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/widgetkit/activitypreviewviewkind
source_url: 'https://developer.apple.com/documentation/widgetkit/activitypreviewviewkind'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/widgetkit/activitypreviewviewkind.json'
content_hash: 'sha256:d739d729f9d3c37d'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [WidgetKit](../widgetkit.md)

# ActivityPreviewViewKind

<sub>Enumeration</sub>

Values that represent Live Activity presentations for use in Xcode previews.

<sub>iOS, iPadOS, Mac Catalyst</sub>

```swift
@preconcurrency enum ActivityPreviewViewKind
```

## Relationships

- **Conforms To**: [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md)

## Topics

### Live Activity preview types

- [ActivityPreviewViewKind.content](activitypreviewviewkind/content.md) — The Live Activity presentation that appears on the Lock Screen and as a banner on devices that don’t support the Dynamic Island.
- [ActivityPreviewViewKind.dynamicIsland(_:)](<activitypreviewviewkind/dynamicisland(__).md>) — The Live Activity presentation that appears in the Dynamic Island.
- [DynamicIslandPreviewViewState](activitypreviewviewkind/dynamicislandpreviewviewstate.md) — Values that represent the different presentations of a Live Activity in the Dynamic Island for use in Xcode previews.

## See Also

### Live Activity setup

- [Displaying live data with Live Activities](../activitykit/displaying-live-data-with-live-activities.md) — Display up-to-date data and offer quick interactions in the Dynamic Island, on the Lock Screen, in CarPlay, and on a paired Mac or Apple Watch.
- [ActivityKit](../activitykit.md) — Share live updates from your app as Live Activities on iPhone, iPad, Apple Watch, and the Mac.
- [Creating a widget extension](creating-a-widget-extension.md) — Display your app’s content in a convenient, informative widget on various devices.
- [Emoji Rangers: Supporting Live Activities, interactivity, and animations](emoji-rangers-supporting-live-activities-interactivity-and-animations.md) — Offer Live Activities, controls, animate data updates, and add interactivity to widgets.
- [ActivityConfiguration](activityconfiguration.md) — An object that describes the content of a Live Activity.
- [DynamicIsland](dynamicisland.md) — The layout and configuration for a Live Activity that appears in the Dynamic Island.
- [NSUserActivityTypeLiveActivity](nsuseractivitytypeliveactivity.md) — A string that the system passes to the app on launch from a Live Activity that doesn’t provide a URL.
- [ActivityFamily](activityfamily.md) — A family that defines the Live Activity’s size.
