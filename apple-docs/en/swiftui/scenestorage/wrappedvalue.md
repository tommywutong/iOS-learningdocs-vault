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
doc_path: /documentation/swiftui/scenestorage/wrappedvalue
source_url: 'https://developer.apple.com/documentation/swiftui/scenestorage/wrappedvalue'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/scenestorage/wrappedvalue.json'
content_hash: 'sha256:c908218f1c9edcad'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [SceneStorage](../scenestorage.md)

# wrappedValue

<sub>Instance Property</sub>

The underlying value referenced by the state variable.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var wrappedValue: Value { get nonmutating set }
```

## Discussion

This works identically to `State.wrappedValue`.

> [!info] See Also
> State.wrappedValue

## See Also

### Getting the value

- [projectedValue](projectedvalue.md) — A binding to the state value.
