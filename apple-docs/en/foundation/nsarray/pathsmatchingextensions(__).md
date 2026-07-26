---
title: 'pathsMatchingExtensions(_:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.0+, macOS 10.0+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ, occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/nsarray/pathsmatchingextensions(_:)'
source_url: 'https://developer.apple.com/documentation/foundation/nsarray/pathsmatchingextensions(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsarray/pathsmatchingextensions%28_%3A%29.json'
content_hash: 'sha256:6cf3e4f45d877b09'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSArray](../nsarray.md)

# pathsMatchingExtensions(_:)

<sub>Instance Method</sub>

Returns an array containing all the pathname elements in the receiving array that have filename extensions from a given array.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func pathsMatchingExtensions(_ filterTypes: [String]) -> [String]
```

## Parameters

- `filterTypes` — An array of `NSString` objects containing filename extensions. The extensions should not include the dot (”.”) character.

## Return Value

An array containing all the pathname elements in the receiving array that have filename extensions from the `filterTypes` array.
