---
title: update()
framework: SwiftUI
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.0+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/dynamicproperty/update()
source_url: 'https://developer.apple.com/documentation/swiftui/dynamicproperty/update()'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/dynamicproperty/update%28%29.json'
content_hash: 'sha256:d211fb62b818489c'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [DynamicProperty](../dynamicproperty.md)

# update()

<sub>Instance Method</sub>

Updates the underlying value of the stored value.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
mutating func update()
```

## Discussion

SwiftUI calls this function before rendering a view’s [body](../view/body-8kl5o.md) to ensure the view has the most recent value.

## Default Implementations

### DynamicProperty Implementations

- [update()](<update()-9fxv4.md>) — Updates the underlying value of the stored value.
