---
title: contentMarginsDisabled()
framework: SwiftUI
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, macOS 12.0+, visionOS 26.0+, watchOS 9.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/widgetconfiguration/contentmarginsdisabled()
source_url: 'https://developer.apple.com/documentation/swiftui/widgetconfiguration/contentmarginsdisabled()'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/widgetconfiguration/contentmarginsdisabled%28%29.json'
content_hash: 'sha256:9e95fbd194ba672f'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [WidgetConfiguration](../widgetconfiguration.md)

# contentMarginsDisabled()

<sub>Instance Method</sub>

Disable default content margins.

<sub>iOS, iPadOS, Mac Catalyst, macOS, visionOS, watchOS</sub>

```swift
@MainActor @preconcurrency func contentMarginsDisabled() -> some WidgetConfiguration

```

## Return Value

A modified widget configuration that doesn’t use default content margins.

## Discussion

When you disable content margins for a widget, the system doesn’t automatically add margins around the widget’s content, and you are responsible for specifying margins and padding around your widget content for each context. To specify custom margins, use [widgetContentMargins](../environmentvalues/widgetcontentmargins.md) in combination with [padding(_:)](<../view/padding(__).md>) to selectively or partially apply the default content margins.

This modifier has no effect on operation system versions prior to iOS 17, watchOS 10, or macOS 14.

## See Also

### Setting the appearance

- [supportedFamilies(_:)](<supportedfamilies(__).md>) — Sets the sizes that a widget supports.
- [disfavoredLocations(_:for:)](<disfavoredlocations(__for_).md>) — Sets the disfavored locations for a widget.
- [containerBackgroundRemovable(_:)](<containerbackgroundremovable(__).md>) — A modifier that marks the background of a widget as removable.
