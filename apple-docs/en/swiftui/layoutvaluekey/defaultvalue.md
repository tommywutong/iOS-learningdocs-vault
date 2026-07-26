---
title: defaultValue
framework: SwiftUI
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, macOS 13.0+, tvOS 16.0+, visionOS 1.0+, watchOS 9.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/layoutvaluekey/defaultvalue
source_url: 'https://developer.apple.com/documentation/swiftui/layoutvaluekey/defaultvalue'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/layoutvaluekey/defaultvalue.json'
content_hash: 'sha256:0f56b3dc8ad9de96'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [LayoutValueKey](../layoutvaluekey.md)

# defaultValue

<sub>Type Property</sub>

The default value of the key.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
static var defaultValue: Self.Value { get }
```

## Discussion

Implement the `defaultValue` property for a type that conforms to the [LayoutValueKey](../layoutvaluekey.md) protocol. For example, you can create a `Flexibility` layout value that defaults to `nil`:

```swift
private struct Flexibility: LayoutValueKey {
    static let defaultValue: CGFloat? = nil
}
```

The type that you declare for the `defaultValue` sets the layout key’s [Value](value.md) associated type. The Swift compiler infers the key’s associated type in the above example as an optional [CGFloat](../../corefoundation/cgfloat-swift.struct.md).

Any view that you don’t explicitly set a value for uses the default value. Override the default value for a view using the [layoutValue(key:value:)](<../view/layoutvalue(key_value_).md>) modifier.

## See Also

### Providing a default value

- [Value](value.md) — The type of the key’s value.
