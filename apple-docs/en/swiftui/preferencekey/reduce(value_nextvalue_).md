---
title: 'reduce(value:nextValue:)'
framework: SwiftUI
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.0+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/preferencekey/reduce(value:nextvalue:)'
source_url: 'https://developer.apple.com/documentation/swiftui/preferencekey/reduce(value:nextvalue:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/preferencekey/reduce%28value%3Anextvalue%3A%29.json'
content_hash: 'sha256:9608ea2afca25e27'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [PreferenceKey](../preferencekey.md)

# reduce(value:nextValue:)

<sub>Type Method</sub>

Combines a sequence of values by modifying the previously-accumulated value with the result of a closure that provides the next value.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
static func reduce(value: inout Self.Value, nextValue: () -> Self.Value)
```

## Parameters

- `value` — The value accumulated through previous calls to this method. The implementation should modify this value.

- `nextValue` — A closure that returns the next value in the sequence.

## Discussion

This method receives its values in view-tree order. Conceptually, this combines the preference value from one tree with that of its next sibling.
