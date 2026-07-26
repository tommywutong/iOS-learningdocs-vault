---
title: wrappedValue
framework: SwiftUI
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 14.0+, iPadOS 14.0+, Mac Catalyst 14.0+, macOS 11.0+, tvOS 14.0+, visionOS 1.0+, watchOS 7.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/focusedvalue/wrappedvalue
source_url: 'https://developer.apple.com/documentation/swiftui/focusedvalue/wrappedvalue'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/focusedvalue/wrappedvalue.json'
content_hash: 'sha256:d032782054779108'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [FocusedValue](../focusedvalue.md)

# wrappedValue

<sub>Instance Property</sub>

The value for the focus key given the current scope and state of the focused view hierarchy.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var wrappedValue: Value? { get }
```

## Discussion

Returns `nil` when nothing in the focused view hierarchy exports a value.
