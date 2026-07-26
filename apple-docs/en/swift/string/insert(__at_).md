---
title: 'insert(_:at:)'
framework: Swift
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.0+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, swift, swift, swift]
beta: false
deprecated: false
doc_path: '/documentation/swift/string/insert(_:at:)'
source_url: 'https://developer.apple.com/documentation/swift/string/insert(_:at:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/string/insert%28_%3Aat%3A%29.json'
content_hash: 'sha256:9cae5f32720e8f76'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [String](../string.md)

# insert(_:at:)

<sub>Instance Method</sub>

Inserts a new character at the specified position.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
mutating func insert(_ newElement: Character, at i: String.Index)
```

## Parameters

- `newElement` — The new character to insert into the string.

- `i` — A valid index of the string. If `i` is equal to the string’s end index, this methods appends `newElement` to the string.

## Discussion

Calling this method invalidates any existing indices for use with this string.

> [!abstract] Complexity
> O(_n_), where _n_ is the length of the string.

## See Also

### Inserting Characters

- [insert(_:at:)](<insert(__at_)-88yqh.md>) — Inserts a new element into the collection at the specified position.
- [insert(contentsOf:at:)](<insert(contentsof_at_)-rdu9.md>) — Inserts the elements of a sequence into the collection at the specified position.
- [insert(contentsOf:at:)](<insert(contentsof_at_).md>) — Inserts a collection of characters at the specified position.
