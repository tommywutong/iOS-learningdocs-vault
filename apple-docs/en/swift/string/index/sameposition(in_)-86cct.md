---
title: 'samePosition(in:)'
framework: Swift
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.0+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, swift, swift, swift]
beta: false
deprecated: false
doc_path: '/documentation/swift/string/index/sameposition(in:)-86cct'
source_url: 'https://developer.apple.com/documentation/swift/string/index/sameposition(in:)-86cct'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/string/index/sameposition%28in%3A%29-86cct.json'
content_hash: 'sha256:c7a1e9e979afa599'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [Swift](../../../swift.md) · [String](../../string.md) · [Index](../index.md)

# samePosition(in:)

<sub>Instance Method</sub>

Returns the position in the given UTF-16 view that corresponds exactly to this index.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func samePosition(in utf16: String.UTF16View) -> String.UTF16View.Index?
```

## Parameters

- `utf16` — The view to use for the index conversion. This index must be a valid index of at least one view of the string shared by `utf16`.

## Return Value

The position in `utf16` that corresponds exactly to this index. If this index does not have an exact corresponding position in `utf16`, this method returns `nil`. For example, an attempt to convert the position of a UTF-8 continuation byte returns `nil`.

## Discussion

The index must be a valid index of `String(utf16)`.

This example first finds the position of the character `"é"` and then uses this method find the same position in the string’s `utf16` view.

```swift
let cafe = "Café"
if let i = cafe.firstIndex(of: "é") {
    let j = i.samePosition(in: cafe.utf16)!
    print(cafe.utf16[j])
}
// Prints "233"
```
