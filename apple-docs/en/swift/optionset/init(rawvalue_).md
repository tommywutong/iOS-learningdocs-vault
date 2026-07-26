---
title: 'init(rawValue:)'
framework: Swift
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.0+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swift/optionset/init(rawvalue:)'
source_url: 'https://developer.apple.com/documentation/swift/optionset/init(rawvalue:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/optionset/init%28rawvalue%3A%29.json'
content_hash: 'sha256:766410e3931ebd14'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [OptionSet](../optionset.md)

# init(rawValue:)

<sub>Initializer</sub>

Creates a new option set from the given raw value.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
init(rawValue: Self.RawValue)
```

## Parameters

- `rawValue` — The raw value of the option set to create. Each bit of `rawValue` potentially represents an element of the option set, though raw values may include bits that are not defined as distinct values of the `OptionSet` type.

## Discussion

This initializer always succeeds, even if the value passed as `rawValue` exceeds the static properties declared as part of the option set. This example creates an instance of `ShippingOptions` with a raw value beyond the highest element, with a bit mask that effectively contains all the declared static members.

```swift
let extraOptions = ShippingOptions(rawValue: 255)
print(extraOptions.isStrictSuperset(of: .all))
// Prints "true"
```
