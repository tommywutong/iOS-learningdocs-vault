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
doc_path: '/documentation/swift/joinedsequence/init(base:separator:)'
source_url: 'https://developer.apple.com/documentation/swift/joinedsequence/init(base:separator:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/joinedsequence/init%28base%3Aseparator%3A%29.json'
content_hash: 'sha256:9ef42daa863650ae'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [JoinedSequence](../joinedsequence.md)

# init(base:separator:)

<sub>Initializer</sub>

Creates an iterator that presents the elements of the sequences traversed by `base`, concatenated using `separator`.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
init<Separator>(base: Base, separator: Separator) where Separator : Sequence, Separator.Element == Base.Element.Element
```

## Discussion

> [!abstract] Complexity
> O(`separator.count`).
