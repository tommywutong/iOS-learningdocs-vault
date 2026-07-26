---
title: 'init(_:within:)'
framework: Swift
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.0+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, swift, swift, swift]
beta: false
deprecated: false
doc_path: '/documentation/swift/string/index/init(_:within:)-7e1rw'
source_url: 'https://developer.apple.com/documentation/swift/string/index/init(_:within:)-7e1rw'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/string/index/init%28_%3Awithin%3A%29-7e1rw.json'
content_hash: 'sha256:a99ebec3111f18ee'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [Swift](../../../swift.md) · [String](../../string.md) · [Index](../index.md)

# init(_:within:)

<sub>Initializer</sub>

Creates an index in the given Unicode scalars view that corresponds exactly to the specified `UTF16View` position.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
init?(_ sourcePosition: String.Index, within unicodeScalars: String.UnicodeScalarView)
```

## Parameters

- `sourcePosition` — A position in the `utf16` view of a string. `utf16Index` must be an element of `String(unicodeScalars).utf16.indices`.

- `unicodeScalars` — The `UnicodeScalarView` in which to find the new position.

## Discussion

The following example finds the position of a space in a string’s `utf16` view and then converts that position to an index in the string’s `unicodeScalars` view:

```swift
let cafe = "Café 🍵"

let utf16Index = cafe.utf16.firstIndex(of: 32)!
let scalarIndex = String.Index(utf16Index, within: cafe.unicodeScalars)!

print(String(cafe.unicodeScalars[..<scalarIndex]))
// Prints "Café"
```

If the index passed as `sourcePosition` doesn’t have an exact corresponding position in `unicodeScalars`, the result of the initializer is `nil`. For example, an attempt to convert the position of the trailing surrogate of a UTF-16 surrogate pair results in `nil`.
