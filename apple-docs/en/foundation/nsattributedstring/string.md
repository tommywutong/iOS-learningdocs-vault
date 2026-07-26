---
title: string
framework: Foundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 3.2+, iPadOS 3.2+, Mac Catalyst 13.1+, macOS 10.0+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/nsattributedstring/string
source_url: 'https://developer.apple.com/documentation/foundation/nsattributedstring/string'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsattributedstring/string.json'
content_hash: 'sha256:efa37dd8f1c0a3d9'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSAttributedString](../nsattributedstring.md)

# string

<sub>Instance Property</sub>

The character contents of the attributed string as a string.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var string: String { get }
```

## Discussion

Attachment characters are not removed from the value of this property.

For performance reasons, this property returns the current backing store of the attributed string object. If you want to maintain a snapshot of this as you manipulate the returned string, you should make a copy of the appropriate substring.

This primitive property must guarantee efficient access to an attributed string’s characters; subclasses should implement it to execute in O(1) time.

## See Also

### Getting the characters

- [length](length.md) — The length of the attributed string.
- [- attributedSubstringFromRange:](<attributedsubstring(from_).md>) — Returns an attributed string consisting of the characters and attributes within the specified range in the attributed string.
