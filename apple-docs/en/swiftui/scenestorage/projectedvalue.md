---
title: projectedValue
framework: SwiftUI
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 14.0+, iPadOS 14.0+, Mac Catalyst 14.0+, macOS 11.0+, tvOS 14.0+, visionOS 1.0+, watchOS 7.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/scenestorage/projectedvalue
source_url: 'https://developer.apple.com/documentation/swiftui/scenestorage/projectedvalue'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/scenestorage/projectedvalue.json'
content_hash: 'sha256:a7263e38e60fb648'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [SceneStorage](../scenestorage.md)

# projectedValue

<sub>Instance Property</sub>

A binding to the state value.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var projectedValue: Binding<Value> { get }
```

## Discussion

This works identically to `State.projectedValue`.

> [!info] See Also
> State.projectedValue

## See Also

### Getting the value

- [wrappedValue](wrappedvalue.md) — The underlying value referenced by the state variable.
