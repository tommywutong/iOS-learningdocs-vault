---
title: characters
framework: Swift
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.0+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: /documentation/swift/string/characters
source_url: 'https://developer.apple.com/documentation/swift/string/characters'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/string/characters.json'
content_hash: 'sha256:06fa222d7168d658'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [String](../string.md)

# characters

<sub>Instance Property</sub>

A view of the string’s contents as a collection of characters.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var characters: String { get set }
```

## Discussion

Previous versions of Swift provided this view since String itself was not a collection. String is now a collection of characters, so this type is now just an alias for String.
