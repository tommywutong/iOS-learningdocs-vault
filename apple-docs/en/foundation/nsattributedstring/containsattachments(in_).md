---
title: 'containsAttachments(in:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 9.0+, iPadOS 9.0+, Mac Catalyst 13.1+, macOS 10.11+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/nsattributedstring/containsattachments(in:)'
source_url: 'https://developer.apple.com/documentation/foundation/nsattributedstring/containsattachments(in:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsattributedstring/containsattachments%28in%3A%29.json'
content_hash: 'sha256:7103b545200cd97b'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSAttributedString](../nsattributedstring.md)

# containsAttachments(in:)

<sub>Instance Method</sub>

Returns a Boolean value that indicates if the attributed string contains an attachment in the specified range.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func containsAttachments(in range: NSRange) -> Bool
```

## Parameters

- `range` — The range.

## Return Value

[true](../../swift/true.md) if the attributed string contains a property configured as [attachment](key/attachment.md) with [character](../../appkit/nstextattachment/character.md) in `range`; otherwise, [false](../../swift/false.md).

## See Also

### Getting metrics for the string

- [- size](<size().md>) — Returns the size necessary to draw the string.
- [- boundingRectWithSize:options:context:](<boundingrect(with_options_context_).md>) — Returns the bounding rectangle necessary to draw the string.
