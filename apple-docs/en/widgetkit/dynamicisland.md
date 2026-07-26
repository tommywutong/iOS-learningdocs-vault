---
title: DynamicIsland
framework: WidgetKit
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 16.1+, iPadOS 16.1+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/widgetkit/dynamicisland
source_url: 'https://developer.apple.com/documentation/widgetkit/dynamicisland'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/widgetkit/dynamicisland.json'
content_hash: 'sha256:7d84d73ac10d1583'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [WidgetKit](../widgetkit.md)

# DynamicIsland

<sub>Structure</sub>

The layout and configuration for a Live Activity that appears in the Dynamic Island.

<sub>iOS, iPadOS, Mac Catalyst</sub>

```swift
struct DynamicIsland
```

## Topics

### Creating the view for the Dynamic Island

- [init(expanded:compactLeading:compactTrailing:minimal:)](<dynamicisland/init(expanded_compactleading_compacttrailing_minimal_).md>) — Creates a configuration object with views that appear in the Dynamic Island.
- [DynamicIslandExpandedRegion](dynamicislandexpandedregion.md) — A structure that defines and positions the content of an expanded Live Activity in the Dynamic Island.

### Deep linking

- [widgetURL(_:)](<dynamicisland/widgeturl(__).md>) — Sets the URL that opens the corresponding app of a Live Activity when a user taps on the Live Activity.

### Setting a tint color

- [keylineTint(_:)](<dynamicisland/keylinetint(__).md>) — Applies a subtle tint color to the surrounding border of a Live Activity that appears in the Dynamic Island.

### Specifying content margins

- [contentMargins(_:_:for:)](<dynamicisland/contentmargins(____for_).md>) — Overrides default content margins for the provided content modes in the Dynamic Island.
- [DynamicIslandMode](dynamicislandmode.md) — A structure that offers values that describe the content mode for a Live Activity.

## See Also

### Live Activity setup

- [Displaying live data with Live Activities](../activitykit/displaying-live-data-with-live-activities.md) — Display up-to-date data and offer quick interactions in the Dynamic Island, on the Lock Screen, in CarPlay, and on a paired Mac or Apple Watch.
- [ActivityKit](../activitykit.md) — Share live updates from your app as Live Activities on iPhone, iPad, Apple Watch, and the Mac.
- [Creating a widget extension](creating-a-widget-extension.md) — Display your app’s content in a convenient, informative widget on various devices.
- [Emoji Rangers: Supporting Live Activities, interactivity, and animations](emoji-rangers-supporting-live-activities-interactivity-and-animations.md) — Offer Live Activities, controls, animate data updates, and add interactivity to widgets.
- [ActivityConfiguration](activityconfiguration.md) — An object that describes the content of a Live Activity.
- [NSUserActivityTypeLiveActivity](nsuseractivitytypeliveactivity.md) — A string that the system passes to the app on launch from a Live Activity that doesn’t provide a URL.
- [ActivityPreviewViewKind](activitypreviewviewkind.md) — Values that represent Live Activity presentations for use in Xcode previews.
- [ActivityFamily](activityfamily.md) — A family that defines the Live Activity’s size.
