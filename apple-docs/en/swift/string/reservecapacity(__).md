---
title: 'reserveCapacity(_:)'
framework: Swift
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.0+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, swift, swift, swift]
beta: false
deprecated: false
doc_path: '/documentation/swift/string/reservecapacity(_:)'
source_url: 'https://developer.apple.com/documentation/swift/string/reservecapacity(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/string/reservecapacity%28_%3A%29.json'
content_hash: 'sha256:edc91ed593ca98f1'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [String](../string.md)

# reserveCapacity(_:)

<sub>Instance Method</sub>

Reserves enough space in the string’s underlying storage to store the specified number of ASCII characters.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
mutating func reserveCapacity(_ n: Int)
```

## Parameters

- `n` — The minimum number of ASCII character’s worth of storage to allocate.

## Discussion

Because each character in a string can require more than a single ASCII character’s worth of storage, additional allocation may be necessary when adding characters to a string after a call to `reserveCapacity(_:)`.

> [!abstract] Complexity
> O(_n_)

## See Also

### Appending Strings and Characters

- [append(_:)](<append(__)-4xa8f.md>) — Appends the given string to this string.
- [append(_:)](<append(__)-4xi3j.md>) — Appends the given character to the string.
- [append(contentsOf:)](<append(contentsof_)-oxek.md>)
- [append(contentsOf:)](<append(contentsof_)-9vb4t.md>)
- [append(contentsOf:)](<append(contentsof_)-7est5.md>) — Appends the characters in the given sequence to the string.
- [append(contentsOf:)](<append(contentsof_)-9foms.md>) — Adds the elements of a sequence or collection to the end of this collection.
- [+(_:_:)](<+(____).md>)
- [+=(_:_:)](<+=(____).md>)
- [+(_:_:)](<+(____)-6h59y.md>) — Creates a new collection by concatenating the elements of a sequence and a collection.
- [+(_:_:)](<+(____)-n329.md>) — Creates a new collection by concatenating the elements of a collection and a sequence.
- [+(_:_:)](<+(____)-9fm57.md>) — Creates a new collection by concatenating the elements of two collections.
- [+=(_:_:)](<+=(____)-676gx.md>) — Appends the elements of a sequence to a range-replaceable collection.
