---
title: 'disfavoredLocations(_:for:)'
framework: SwiftUI
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 17.0+, iPadOS 17.0+, Mac Catalyst 17.0+, watchOS 26.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/widgetconfiguration/disfavoredlocations(_:for:)'
source_url: 'https://developer.apple.com/documentation/swiftui/widgetconfiguration/disfavoredlocations(_:for:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/widgetconfiguration/disfavoredlocations%28_%3Afor%3A%29.json'
content_hash: 'sha256:73556c69f7e6c726'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [WidgetConfiguration](../widgetconfiguration.md)

# disfavoredLocations(_:for:)

<sub>Instance Method</sub>

Sets the disfavored locations for a widget.

<sub>iOS, iPadOS, Mac Catalyst, watchOS</sub>

```swift
@MainActor @preconcurrency func disfavoredLocations(_ locations: [WidgetLocation], for families: [WidgetFamily]) -> some WidgetConfiguration

```

## Parameters

- `locations` — An array of disfavored locations for a widget.

- `families` — The families you want to mark as disfavored in the given locations.

## Discussion

A widget can appear in different contexts on different platforms. For example, a small system widget appears by default on the Home Screen and in Today View on iPhone, on the iPad Lock Screen, and so on. This gives more people opportunity to view data and functionality that your widget provides. However, some widgets may not work well in a location. For example, a widget that heavily relies on high-resolution photos and background colors for its functionality may not work well on the Lock Screen, where the system applies a vibrant treatment to the widget. To tell the system that the widget gallery should show a widget in the “Other” section of the widget gallery for a specific context, use the `.disfavoredLocations` modifier.

The following code snippet tells the system to show the small system family widget in the “Other” section of the widget gallery for the disfavored `WidgetLocation/lockScreen` and `WidgetLocation/homeScreen` locations.

```swift
lockScreenOnlyConfig
    .disfavoredLocations([.lockScreen, .homeScreen], for: [.systemSmall])
```

You can use subsequent calls to `disfavoredLocations(_:families:)` to join them and set disfavored locations for different families:

```swift
widgetConfig
    .disfavoredLocations([.lockScreen, .homeScreen], for: [.systemSmall])
    .disfavoredLocations([.homescreen], for: [.systemMedium])
```

## See Also

### Setting the appearance

- [supportedFamilies(_:)](<supportedfamilies(__).md>) — Sets the sizes that a widget supports.
- [contentMarginsDisabled()](<contentmarginsdisabled().md>) — Disable default content margins.
- [containerBackgroundRemovable(_:)](<containerbackgroundremovable(__).md>) — A modifier that marks the background of a widget as removable.
