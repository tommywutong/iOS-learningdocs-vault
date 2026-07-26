---
title: 'completePath(into:caseSensitive:matchesInto:filterTypes:)'
framework: Swift
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 8.0+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: '/documentation/swift/stringprotocol/completepath(into:casesensitive:matchesinto:filtertypes:)'
source_url: 'https://developer.apple.com/documentation/swift/stringprotocol/completepath(into:casesensitive:matchesinto:filtertypes:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/stringprotocol/completepath%28into%3Acasesensitive%3Amatchesinto%3Afiltertypes%3A%29.json'
content_hash: 'sha256:49e3522747b07d8a'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [StringProtocol](../stringprotocol.md)

# completePath(into:caseSensitive:matchesInto:filterTypes:)

<sub>Instance Method</sub>

Interprets the string as a path in the file system and attempts to perform filename completion, returning a numeric value that indicates whether a match was possible, and by reference the longest path that matches the string.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func completePath(into outputName: UnsafeMutablePointer<String>? = nil, caseSensitive: Bool, matchesInto outputArray: UnsafeMutablePointer<[String]>? = nil, filterTypes: [String]? = nil) -> Int
```

## Return Value

The actual number of matching paths.
