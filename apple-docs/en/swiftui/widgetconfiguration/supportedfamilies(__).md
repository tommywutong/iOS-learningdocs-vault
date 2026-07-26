---
title: 'supportedFamilies(_:)'
framework: SwiftUI
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 14.0+, iPadOS 14.0+, Mac Catalyst 14.0+, macOS 11.0+, visionOS 26.0+, watchOS 9.0+]
languages: [swift, swift, swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/widgetconfiguration/supportedfamilies(_:)'
source_url: 'https://developer.apple.com/documentation/swiftui/widgetconfiguration/supportedfamilies(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/widgetconfiguration/supportedfamilies%28_%3A%29.json'
content_hash: 'sha256:cdb97eb7bbe8306f'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [WidgetConfiguration](../widgetconfiguration.md)

# supportedFamilies(_:)

<sub>Instance Method</sub>

Sets the sizes that a widget supports.

<sub>iOS, iPadOS, Mac Catalyst, macOS, visionOS, watchOS</sub>

```swift
@MainActor @preconcurrency func supportedFamilies(_ families: [WidgetFamily]) -> some WidgetConfiguration

```

## Parameters

- `families` — The set of sizes the widget supports.

## Return Value

A widget configuration that supports the sizes you specify.

## See Also

### Setting the appearance

- [contentMarginsDisabled()](<contentmarginsdisabled().md>) — Disable default content margins.
- [disfavoredLocations(_:for:)](<disfavoredlocations(__for_).md>) — Sets the disfavored locations for a widget.
- [containerBackgroundRemovable(_:)](<containerbackgroundremovable(__).md>) — A modifier that marks the background of a widget as removable.
