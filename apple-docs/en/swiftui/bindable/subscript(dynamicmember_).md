---
title: 'subscript(dynamicMember:)'
framework: SwiftUI
symbol_kind: subscript
role: symbol
role_heading: Instance Subscript
platforms: [iOS 17.0+, iPadOS 17.0+, Mac Catalyst 17.0+, macOS 14.0+, tvOS 17.0+, visionOS 1.0+, watchOS 10.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/bindable/subscript(dynamicmember:)'
source_url: 'https://developer.apple.com/documentation/swiftui/bindable/subscript(dynamicmember:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/bindable/subscript%28dynamicmember%3A%29.json'
content_hash: 'sha256:51ebd5134a0144db'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [Bindable](../bindable.md)

# subscript(dynamicMember:)

<sub>Instance Subscript</sub>

Returns a binding to the value of a given key path.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
subscript<Subject>(dynamicMember keyPath: ReferenceWritableKeyPath<Value, Subject>) -> Binding<Subject> { get }
```

## See Also

### Getting the value

- [wrappedValue](wrappedvalue.md) — The wrapped object.
- [projectedValue](projectedvalue.md) — The bindable wrapper for the object that creates bindings to its properties using dynamic member lookup.
