---
title: containsAttachments
framework: Foundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [macOS 10.0+]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: /documentation/foundation/nsattributedstring/containsattachments
source_url: 'https://developer.apple.com/documentation/foundation/nsattributedstring/containsattachments'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsattributedstring/containsattachments.json'
content_hash: 'sha256:34cac70ddf1ca962'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSAttributedString](../nsattributedstring.md)

# containsAttachments

<sub>Instance Property</sub>

A Boolean value that indicates whether the attribute string contains any attachment attributes.

> [!warning] Deprecated
> Use [- containsAttachmentsInRange:](<containsattachments(in_).md>) instead.

<sub>macOS</sub>

```swift
var containsAttachments: Bool { get }
```

## Return Value

YES if the attributed string contains any attachment attributes, otherwise NO.

## Discussion

This method checks only for attachment attributes, not for `NSAttachmentCharacter`.
