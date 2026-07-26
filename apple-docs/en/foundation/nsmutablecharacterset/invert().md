---
title: invert()
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.0+, macOS 10.0+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/nsmutablecharacterset/invert()
source_url: 'https://developer.apple.com/documentation/foundation/nsmutablecharacterset/invert()'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsmutablecharacterset/invert%28%29.json'
content_hash: 'sha256:d6eb1c6458ec6d40'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSMutableCharacterSet](../nsmutablecharacterset.md)

# invert()

<sub>Instance Method</sub>

Replaces all the characters in the receiver with all the characters it didn’t previously contain.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func invert()
```

## Discussion

Inverting a mutable character set, whether by [- invert](<invert().md>) or by [invertedSet](../nscharacterset/inverted.md), is much less efficient than inverting an immutable character set with [invertedSet](../nscharacterset/inverted.md).

## See Also

### Related Documentation

- [invertedSet](../nscharacterset/inverted.md) — A character set containing only characters that don’t exist in the receiver.
