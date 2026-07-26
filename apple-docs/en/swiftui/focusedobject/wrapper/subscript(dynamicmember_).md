---
title: 'subscript(dynamicMember:)'
framework: SwiftUI
symbol_kind: subscript
role: symbol
role_heading: Instance Subscript
platforms: [iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, macOS 13.0+, tvOS 16.0+, visionOS 1.0+, watchOS 9.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/focusedobject/wrapper/subscript(dynamicmember:)'
source_url: 'https://developer.apple.com/documentation/swiftui/focusedobject/wrapper/subscript(dynamicmember:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/focusedobject/wrapper/subscript%28dynamicmember%3A%29.json'
content_hash: 'sha256:264dc0d28bffb743'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [SwiftUI](../../../swiftui.md) · [FocusedObject](../../focusedobject.md) · [Wrapper](../wrapper.md)

# subscript(dynamicMember:)

<sub>Instance Subscript</sub>

Returns a binding to the value of a given key path.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
@MainActor @preconcurrency subscript<T>(dynamicMember keyPath: ReferenceWritableKeyPath<ObjectType, T>) -> Binding<T> { get }
```

## Parameters

- `keyPath` — A key path to a specific value on the wrapped object.

## Return Value

A new binding.
