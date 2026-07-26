---
title: 'init(base:separator:)'
framework: Swift
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.0+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swift/joinedsequence/iterator/init(base:separator:)'
source_url: 'https://developer.apple.com/documentation/swift/joinedsequence/iterator/init(base:separator:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/joinedsequence/iterator/init%28base%3Aseparator%3A%29.json'
content_hash: 'sha256:e6a704035b64e7df'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [Swift](../../../swift.md) · [JoinedSequence](../../joinedsequence.md) · [Iterator](../iterator.md)

# init(base:separator:)

<sub>Initializer</sub>

Creates an iterator that presents the elements of `base` sequences concatenated using `separator`.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
init<Separator>(base: Base.Iterator, separator: Separator) where Separator : Sequence, Separator.Element == Base.Element.Element
```

## Discussion

> [!abstract] Complexity
> O(`separator.count`).
