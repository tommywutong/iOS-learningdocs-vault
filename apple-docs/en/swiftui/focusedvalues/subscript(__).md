---
title: 'subscript(_:)'
framework: SwiftUI
symbol_kind: subscript
role: symbol
role_heading: Instance Subscript
platforms: [iOS 14.0+, iPadOS 14.0+, Mac Catalyst 14.0+, macOS 11.0+, tvOS 14.0+, visionOS 1.0+, watchOS 7.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/focusedvalues/subscript(_:)'
source_url: 'https://developer.apple.com/documentation/swiftui/focusedvalues/subscript(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/focusedvalues/subscript%28_%3A%29.json'
content_hash: 'sha256:8a7b82c82562de68'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [FocusedValues](../focusedvalues.md)

# subscript(_:)

<sub>Instance Subscript</sub>

Reads and writes values associated with a given focused value key.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
subscript<Key>(key: Key.Type) -> Key.Value? where Key : FocusedValueKey { get set }
```

## Overview

Use this subscript to get or set a focused value for a custom [FocusedValueKey](../focusedvaluekey.md). In most cases, you’ll use the `Entry` macro to create focused value properties, which automatically generates the appropriate key and uses this subscript internally:

```swift
extension FocusedValues {
    @Entry var myCustomValue: MyType?
}
```
