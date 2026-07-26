---
title: 'init(_:)'
framework: SwiftUI
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 14.0+, iPadOS 14.0+, Mac Catalyst 14.0+, macOS 11.0+, tvOS 14.0+, visionOS 1.0+, watchOS 7.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/focusedvalue/init(_:)'
source_url: 'https://developer.apple.com/documentation/swiftui/focusedvalue/init(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/focusedvalue/init%28_%3A%29.json'
content_hash: 'sha256:368a6e2dfe7bd4f5'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [FocusedValue](../focusedvalue.md)

# init(_:)

<sub>Initializer</sub>

A new property wrapper for the given key path.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
init(_ keyPath: KeyPath<FocusedValues, Value?>)
```

## Parameters

- `keyPath` — The key path for the focus value to read.

## Discussion

The value of the property wrapper is updated dynamically as focus changes and different published values go in and out of scope.
