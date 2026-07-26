---
title: disabled
framework: SwiftUI
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, macOS 13.0+, tvOS 16.0+, visionOS 1.0+, watchOS 9.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/toolbarcustomizationbehavior/disabled
source_url: 'https://developer.apple.com/documentation/swiftui/toolbarcustomizationbehavior/disabled'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/toolbarcustomizationbehavior/disabled.json'
content_hash: 'sha256:ae5212b28caab614'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [ToolbarCustomizationBehavior](../toolbarcustomizationbehavior.md)

# disabled

<sub>Type Property</sub>

The disabled customization behavior.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
static var disabled: ToolbarCustomizationBehavior { get }
```

## Discussion

Items with this behavior may not be removed or moved by the user. They will be placed before other customizatable items. Use this behavior for the most important items that users need for the app to do common functionality.

## See Also

### Getting customization behaviors

- [default](default.md) — The default customization behavior.
- [reorderable](reorderable.md) — The reorderable customization behavior.
