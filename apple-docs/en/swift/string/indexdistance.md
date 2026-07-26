---
title: String.IndexDistance
framework: Swift
symbol_kind: typealias
role: symbol
role_heading: Type Alias
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.0+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, swift]
beta: false
deprecated: true
doc_path: /documentation/swift/string/indexdistance
source_url: 'https://developer.apple.com/documentation/swift/string/indexdistance'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/string/indexdistance.json'
content_hash: 'sha256:a9fc3482975daa3a'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [String](../string.md)

# String.IndexDistance

<sub>Type Alias</sub>

A type that represents the number of steps between two `String.Index` values, where one value is reachable from the other.

> [!warning] Deprecated
> All index distances are now of type Int

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
typealias IndexDistance = Int
```

## Discussion

In Swift, _reachability_ refers to the ability to produce one value from the other through zero or more applications of `index(after:)`.
