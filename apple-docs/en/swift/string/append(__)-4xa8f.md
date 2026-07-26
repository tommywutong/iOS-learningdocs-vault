---
title: 'append(_:)'
framework: Swift
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.0+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: '/documentation/swift/string/append(_:)-4xa8f'
source_url: 'https://developer.apple.com/documentation/swift/string/append(_:)-4xa8f'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/string/append%28_%3A%29-4xa8f.json'
content_hash: 'sha256:19663fd2dfdf3fc1'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [String](../string.md)

# append(_:)

<sub>Instance Method</sub>

Appends the given string to this string.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
mutating func append(_ other: String)
```

## Parameters

- `other` — Another string.

## Discussion

The following example builds a customized greeting by using the `append(_:)` method:

```swift
var greeting = "Hello, "
if let name = getUserName() {
    greeting.append(name)
} else {
    greeting.append("friend")
}
print(greeting)
// Prints "Hello, friend"
```

## See Also

### Appending Strings and Characters

- [append(_:)](<append(__)-4xi3j.md>) — Appends the given character to the string.
- [append(contentsOf:)](<append(contentsof_)-oxek.md>)
- [append(contentsOf:)](<append(contentsof_)-9vb4t.md>)
- [append(contentsOf:)](<append(contentsof_)-7est5.md>) — Appends the characters in the given sequence to the string.
- [append(contentsOf:)](<append(contentsof_)-9foms.md>) — Adds the elements of a sequence or collection to the end of this collection.
- [reserveCapacity(_:)](<reservecapacity(__).md>) — Reserves enough space in the string’s underlying storage to store the specified number of ASCII characters.
- [+(_:_:)](<+(____).md>)
- [+=(_:_:)](<+=(____).md>)
- [+(_:_:)](<+(____)-6h59y.md>) — Creates a new collection by concatenating the elements of a sequence and a collection.
- [+(_:_:)](<+(____)-n329.md>) — Creates a new collection by concatenating the elements of a collection and a sequence.
- [+(_:_:)](<+(____)-9fm57.md>) — Creates a new collection by concatenating the elements of two collections.
- [+=(_:_:)](<+=(____)-676gx.md>) — Appends the elements of a sequence to a range-replaceable collection.
