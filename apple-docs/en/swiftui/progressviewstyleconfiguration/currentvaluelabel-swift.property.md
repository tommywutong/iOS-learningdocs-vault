---
title: currentValueLabel
framework: SwiftUI
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 14.0+, iPadOS 14.0+, Mac Catalyst 14.0+, macOS 11.0+, tvOS 14.0+, visionOS 1.0+, watchOS 7.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/progressviewstyleconfiguration/currentvaluelabel-swift.property
source_url: 'https://developer.apple.com/documentation/swiftui/progressviewstyleconfiguration/currentvaluelabel-swift.property'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/progressviewstyleconfiguration/currentvaluelabel-swift.property.json'
content_hash: 'sha256:c494bb2772289e3f'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [ProgressViewStyleConfiguration](../progressviewstyleconfiguration.md)

# currentValueLabel

<sub>Instance Property</sub>

A view that describes the current value of a progress view.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var currentValueLabel: ProgressViewStyleConfiguration.CurrentValueLabel?
```

## Discussion

If `nil`, then the value of the progress view is either self-evident from the surrounding context or unknown, and the style does not need to provide any additional description.

If the progress view is defined using a `Progress` instance, then this label is equivalent to its `localizedAdditionalDescription`.

## See Also

### Configuring the current value label

- [CurrentValueLabel](currentvaluelabel-swift.struct.md) — A type-erased label that describes the current value of a progress view.
