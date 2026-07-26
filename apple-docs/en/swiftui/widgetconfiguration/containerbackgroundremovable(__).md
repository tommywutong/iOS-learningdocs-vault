---
title: 'containerBackgroundRemovable(_:)'
framework: SwiftUI
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, macOS 12.0+, visionOS 26.0+, watchOS 9.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/widgetconfiguration/containerbackgroundremovable(_:)'
source_url: 'https://developer.apple.com/documentation/swiftui/widgetconfiguration/containerbackgroundremovable(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/widgetconfiguration/containerbackgroundremovable%28_%3A%29.json'
content_hash: 'sha256:c18347be9b347ad8'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [WidgetConfiguration](../widgetconfiguration.md)

# containerBackgroundRemovable(_:)

<sub>Instance Method</sub>

A modifier that marks the background of a widget as removable.

<sub>iOS, iPadOS, Mac Catalyst, macOS, visionOS, watchOS</sub>

```swift
@MainActor @preconcurrency func containerBackgroundRemovable(_ isRemovable: Bool = true) -> some WidgetConfiguration

```

## Parameters

- `isRemovable` — If `true`, the widget supports removal of the container background in contexts that prefer no backgrounds. If `false`, the system doesn’t remove the background.

## Return Value

A modified widget configuration.

## Discussion

In most cases, mark the background container of a widget as removable to allow people to place the widget in as many contexts as possible. If you mark the background as nonremovable, the widget becomes ineligible in various contexts that require a removable background. For example, a small widget without a removable background doesn’t appear in the widget gallery on the iPad Lock Screen.

If you mark a background as nonremovable, the system always displays the background container of the widget. Note that the background may render differently; for example, it can appear faded or desaturated.

This modifier has no effect on operation system versions prior to iOS 17, watchOS 10, or macOS 14.

## See Also

### Setting the appearance

- [supportedFamilies(_:)](<supportedfamilies(__).md>) — Sets the sizes that a widget supports.
- [contentMarginsDisabled()](<contentmarginsdisabled().md>) — Disable default content margins.
- [disfavoredLocations(_:for:)](<disfavoredlocations(__for_).md>) — Sets the disfavored locations for a widget.
