---
title: Mirror.Children
framework: Swift
symbol_kind: typealias
role: symbol
role_heading: Type Alias
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.0+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swift/mirror/children-swift.typealias
source_url: 'https://developer.apple.com/documentation/swift/mirror/children-swift.typealias'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/mirror/children-swift.typealias.json'
content_hash: 'sha256:08eb2f20f28022a2'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [Mirror](../mirror.md)

# Mirror.Children

<sub>Type Alias</sub>

The type used to represent substructure.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
typealias Children = AnyCollection<Mirror.Child>
```

## Discussion

When working with a mirror that reflects a bidirectional or random access collection, you may find it useful to “upgrade” instances of this type to `AnyBidirectionalCollection` or `AnyRandomAccessCollection`. For example, to display the last twenty children of a mirror if they can be accessed efficiently, you write the following code:

```swift
if let b = AnyBidirectionalCollection(someMirror.children) {
    for element in b.suffix(20) {
        print(element)
    }
}
```
