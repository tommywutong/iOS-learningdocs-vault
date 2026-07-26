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
doc_path: '/documentation/swiftui/focusedbinding/init(_:)'
source_url: 'https://developer.apple.com/documentation/swiftui/focusedbinding/init(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/focusedbinding/init%28_%3A%29.json'
content_hash: 'sha256:254ff594f481987b'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [FocusedBinding](../focusedbinding.md)

# init(_:)

<sub>Initializer</sub>

A new property wrapper for the given key path.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
init(_ keyPath: KeyPath<FocusedValues, Binding<Value>?>)
```

## Parameters

- `keyPath` — The key path for the focus value to read.

## Discussion

The value of the property wrapper is updated dynamically as focus changes and different published bindings go in and out of scope.
