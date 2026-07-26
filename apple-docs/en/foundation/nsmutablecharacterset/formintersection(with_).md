---
title: 'formIntersection(with:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.0+, macOS 10.0+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/nsmutablecharacterset/formintersection(with:)'
source_url: 'https://developer.apple.com/documentation/foundation/nsmutablecharacterset/formintersection(with:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsmutablecharacterset/formintersection%28with%3A%29.json'
content_hash: 'sha256:5162eb8a09ffa272'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSMutableCharacterSet](../nsmutablecharacterset.md)

# formIntersection(with:)

<sub>Instance Method</sub>

Modifies the receiver so it contains only characters that exist in both the receiver and another set.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func formIntersection(with otherSet: CharacterSet)
```

## Parameters

- `otherSet` — The character set with which to perform the intersection.

## See Also

### Combining Character Sets

- [- formUnionWithCharacterSet:](<formunion(with_).md>) — Modifies the receiver so it contains all characters that exist in either the receiver or another set.
