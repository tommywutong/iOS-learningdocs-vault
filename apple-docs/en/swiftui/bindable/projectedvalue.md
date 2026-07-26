---
title: projectedValue
framework: SwiftUI
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 17.0+, iPadOS 17.0+, Mac Catalyst 17.0+, macOS 14.0+, tvOS 17.0+, visionOS 1.0+, watchOS 10.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/bindable/projectedvalue
source_url: 'https://developer.apple.com/documentation/swiftui/bindable/projectedvalue'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/bindable/projectedvalue.json'
content_hash: 'sha256:5290510f99d2c69e'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [Bindable](../bindable.md)

# projectedValue

<sub>Instance Property</sub>

The bindable wrapper for the object that creates bindings to its properties using dynamic member lookup.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var projectedValue: Bindable<Value> { get }
```

## See Also

### Getting the value

- [wrappedValue](wrappedvalue.md) — The wrapped object.
- [subscript(dynamicMember:)](<subscript(dynamicmember_).md>) — Returns a binding to the value of a given key path.
