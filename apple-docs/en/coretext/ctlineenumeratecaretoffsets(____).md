---
title: 'CTLineEnumerateCaretOffsets(_:_:)'
framework: Core Text
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS 9.0+, iPadOS 9.0+, Mac Catalyst 13.1+, macOS 10.11+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/coretext/ctlineenumeratecaretoffsets(_:_:)'
source_url: 'https://developer.apple.com/documentation/coretext/ctlineenumeratecaretoffsets(_:_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coretext/ctlineenumeratecaretoffsets%28_%3A_%3A%29.json'
content_hash: 'sha256:3f6526e8973a3f24'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Text](../coretext.md)

# CTLineEnumerateCaretOffsets(_:_:)

<sub>Function</sub>

Enumerates caret offsets for characters in a line.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func CTLineEnumerateCaretOffsets(_ line: CTLine, _ block: @escaping (Double, CFIndex, Bool, UnsafeMutablePointer<Bool>) -> Void)
```

## Parameters

- `line` — The line to enumerate.

- `block` — The block to invoke once for each logical caret edge in the line, in left-to-right visual order. The block’s `offset` parameter is relative to the line origin. The block’s `leadingEdge` parameter specifies logical order.

## See Also

### Getting Line Positioning

- [CTLineGetStringIndexForPosition](<ctlinegetstringindexforposition(____).md>) — Performs hit testing.
- [CTLineGetOffsetForStringIndex](<ctlinegetoffsetforstringindex(______).md>) — Determines the graphical offset or offsets for a string index.
