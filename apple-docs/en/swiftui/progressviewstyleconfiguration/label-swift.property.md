---
title: label
framework: SwiftUI
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 14.0+, iPadOS 14.0+, Mac Catalyst 14.0+, macOS 11.0+, tvOS 14.0+, visionOS 1.0+, watchOS 7.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/progressviewstyleconfiguration/label-swift.property
source_url: 'https://developer.apple.com/documentation/swiftui/progressviewstyleconfiguration/label-swift.property'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/progressviewstyleconfiguration/label-swift.property.json'
content_hash: 'sha256:e3637b38a5b68cc4'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [ProgressViewStyleConfiguration](../progressviewstyleconfiguration.md)

# label

<sub>Instance Property</sub>

A view that describes the task represented by the progress view.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var label: ProgressViewStyleConfiguration.Label?
```

## Discussion

If `nil`, then the task is self-evident from the surrounding context, and the style does not need to provide any additional description.

If the progress view is defined using a `Progress` instance, then this label is equivalent to its `localizedDescription`.

## See Also

### Configuring the label

- [Label](label-swift.struct.md) — A type-erased label describing the task represented by the progress view.
