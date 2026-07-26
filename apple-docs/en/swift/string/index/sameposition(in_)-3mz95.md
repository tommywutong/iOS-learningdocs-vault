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
doc_path: '/documentation/swift/string/index/sameposition(in:)-3mz95'
source_url: 'https://developer.apple.com/documentation/swift/string/index/sameposition(in:)-3mz95'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/string/index/sameposition%28in%3A%29-3mz95.json'
content_hash: 'sha256:c49a330973bbe0d9'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [Swift](../../../swift.md) · [String](../../string.md) · [Index](../index.md)

# samePosition(in:)

<sub>Instance Method</sub>

Returns the position in the given UTF-8 view that corresponds exactly to this index.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func samePosition(in utf8: String.UTF8View) -> String.UTF8View.Index?
```

## Parameters

- `utf8` — The view to use for the index conversion. This index must be a valid index of at least one view of the string shared by `utf8`.

## Return Value

The position in `utf8` that corresponds exactly to this index. If this index does not have an exact corresponding position in `utf8`, this method returns `nil`. For example, an attempt to convert the position of a UTF-16 trailing surrogate returns `nil`.

## Discussion

This example first finds the position of the character `"é"`, and then uses this method find the same position in the string’s `utf8` view.

```swift
let cafe = "Café"
if let i = cafe.firstIndex(of: "é") {
    let j = i.samePosition(in: cafe.utf8)!
    print(Array(cafe.utf8[j...]))
}
// Prints "[195, 169]"
```
