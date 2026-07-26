---
title: 'append(contentsOf:)'
framework: Swift
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.0+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, swift, swift, swift]
beta: false
deprecated: false
doc_path: '/documentation/swift/string/append(contentsof:)-7est5'
source_url: 'https://developer.apple.com/documentation/swift/string/append(contentsof:)-7est5'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/string/append%28contentsof%3A%29-7est5.json'
content_hash: 'sha256:b9f20451c5093b2f'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [String](../string.md)

# append(contentsOf:)

<sub>Instance Method</sub>

Appends the characters in the given sequence to the string.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
mutating func append<S>(contentsOf newElements: S) where S : Sequence, S.Element == Character
```

## Parameters

- `newElements` — A sequence of characters.

## See Also

### Appending Strings and Characters

- [append(_:)](<append(__)-4xa8f.md>) — Appends the given string to this string.
- [append(_:)](<append(__)-4xi3j.md>) — Appends the given character to the string.
- [append(contentsOf:)](<append(contentsof_)-oxek.md>)
- [append(contentsOf:)](<append(contentsof_)-9vb4t.md>)
- [append(contentsOf:)](<append(contentsof_)-9foms.md>) — Adds the elements of a sequence or collection to the end of this collection.
- [reserveCapacity(_:)](<reservecapacity(__).md>) — Reserves enough space in the string’s underlying storage to store the specified number of ASCII characters.
- [+(_:_:)](<+(____).md>)
- [+=(_:_:)](<+=(____).md>)
- [+(_:_:)](<+(____)-6h59y.md>) — Creates a new collection by concatenating the elements of a sequence and a collection.
- [+(_:_:)](<+(____)-n329.md>) — Creates a new collection by concatenating the elements of a collection and a sequence.
- [+(_:_:)](<+(____)-9fm57.md>) — Creates a new collection by concatenating the elements of two collections.
- [+=(_:_:)](<+=(____)-676gx.md>) — Appends the elements of a sequence to a range-replaceable collection.
