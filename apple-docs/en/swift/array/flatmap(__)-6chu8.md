---
title: 'flatMap(_:)'
framework: Swift
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.0+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+, Swift（4.1 起废弃）]
languages: [swift, swift, swift, swift]
beta: false
deprecated: true
doc_path: '/documentation/swift/array/flatmap(_:)-6chu8'
source_url: 'https://developer.apple.com/documentation/swift/array/flatmap(_:)-6chu8'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/array/flatmap%28_%3A%29-6chu8.json'
content_hash: 'sha256:dd5a3f130c4b5c19'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [Array](../array.md)

# flatMap(_:)

<sub>Instance Method</sub>

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func flatMap<ElementOfResult>(_ transform: (Self.Element) throws -> ElementOfResult?) rethrows -> [ElementOfResult]
```

## See Also

### Transforming an Array

- [flatMap(_:)](<flatmap(__)-i3mr.md>) — Returns an array containing the concatenated results of calling the given transformation with each element of this sequence.
- [compactMap(_:)](<compactmap(__).md>) — Returns an array containing the non-`nil` results of calling the given transformation with each element of this sequence.
- [reduce(_:_:)](<reduce(____).md>) — Returns the result of combining the elements of the sequence using the given closure.
- [reduce(into:_:)](<reduce(into___).md>) — Returns the result of combining the elements of the sequence using the given closure.
- [lazy](lazy.md) — A sequence containing the same elements as this sequence, but on which some operations, such as `map` and `filter`, are implemented lazily.
