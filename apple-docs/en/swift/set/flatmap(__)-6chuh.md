---
title: 'flatMap(_:)'
framework: Swift
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.0+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+, Swift（4.1 起废弃）]
languages: [swift, swift]
beta: false
deprecated: true
doc_path: '/documentation/swift/set/flatmap(_:)-6chuh'
source_url: 'https://developer.apple.com/documentation/swift/set/flatmap(_:)-6chuh'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/set/flatmap%28_%3A%29-6chuh.json'
content_hash: 'sha256:ca1e31eb19a2eb68'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [Set](../set.md)

# flatMap(_:)

<sub>Instance Method</sub>

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func flatMap<ElementOfResult>(_ transform: (Self.Element) throws -> ElementOfResult?) rethrows -> [ElementOfResult]
```

## See Also

### Transforming a Set

- [compactMap(_:)](<compactmap(__).md>) — Returns an array containing the non-`nil` results of calling the given transformation with each element of this sequence.
- [flatMap(_:)](<flatmap(__)-i3my.md>) — Returns an array containing the concatenated results of calling the given transformation with each element of this sequence.
- [reduce(_:_:)](<reduce(____).md>) — Returns the result of combining the elements of the sequence using the given closure.
- [reduce(into:_:)](<reduce(into___).md>) — Returns the result of combining the elements of the sequence using the given closure.
- [sorted()](<sorted().md>) — Returns the elements of the sequence, sorted.
- [sorted(by:)](<sorted(by_).md>) — Returns the elements of the sequence, sorted using the given predicate as the comparison between elements.
- [shuffled()](<shuffled().md>) — Returns the elements of the sequence, shuffled.
- [shuffled(using:)](<shuffled(using_).md>) — Returns the elements of the sequence, shuffled using the given generator as a source for randomness.
- [lazy](lazy.md) — A sequence containing the same elements as this sequence, but on which some operations, such as `map` and `filter`, are implemented lazily.
