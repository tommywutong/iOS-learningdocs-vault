---
title: 'init(_:)'
framework: Swift
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.0+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: '/documentation/swift/string/init(_:)-1ywfq'
source_url: 'https://developer.apple.com/documentation/swift/string/init(_:)-1ywfq'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/string/init%28_%3A%29-1ywfq.json'
content_hash: 'sha256:11892563fcffdf75'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [String](../string.md)

# init(_:)

<sub>Initializer</sub>

Creates an instance from the description of a given `LosslessStringConvertible` instance.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
init<T>(_ value: T) where T : LosslessStringConvertible
```

## See Also

### Converting Other Types to Strings

- [init(describing:)](<init(describing_)-588wb.md>) — Creates a string representing the given value.
- [init(describing:)](<init(describing_)-hsqw.md>) — Creates a string representing the given value.
- [init(describing:)](<init(describing_)-6ttci.md>) — Creates a string representing the given value.
- [init(describing:)](<init(describing_)-67ncf.md>) — Creates a string representing the given value.
- [init(reflecting:)](<init(reflecting_).md>) — Creates a string with a detailed representation of the given value, suitable for debugging.
