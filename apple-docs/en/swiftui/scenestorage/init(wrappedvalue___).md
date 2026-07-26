---
title: 'init(wrappedValue:_:)'
framework: SwiftUI
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 14.0+, iPadOS 14.0+, Mac Catalyst 14.0+, macOS 11.0+, tvOS 14.0+, visionOS 1.0+, watchOS 7.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/scenestorage/init(wrappedvalue:_:)'
source_url: 'https://developer.apple.com/documentation/swiftui/scenestorage/init(wrappedvalue:_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/scenestorage/init%28wrappedvalue%3A_%3A%29.json'
content_hash: 'sha256:99ecf3c7f165576c'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [SceneStorage](../scenestorage.md)

# init(wrappedValue:_:)

<sub>Initializer</sub>

Creates a property that can save and restore an integer, transforming it to a `RawRepresentable` data type.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
init(wrappedValue: Value, _ key: String) where Value : RawRepresentable, Value.RawValue == Int
```

## Parameters

- `wrappedValue` — The default value if an integer value is not available for the given key.

- `key` — A key used to save and restore the value.

## Discussion

A common usage is with enumerations:

```swift
enum MyEnum: Int {
    case a
    case b
    case c
}
struct MyView: View {
    @SceneStorage("MyEnumValue") private var value = MyEnum.a
    var body: some View { ... }
}
```

## See Also

### Storing a value

- [init(_:)](<init(__).md>) — Creates a property that can save and restore an Optional boolean.
