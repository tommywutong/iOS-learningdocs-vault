---
title: 'CTLineCreateJustifiedLine(_:_:_:)'
framework: Core Text
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS 3.2+, iPadOS 3.2+, Mac Catalyst 13.1+, macOS 10.5+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/coretext/ctlinecreatejustifiedline(_:_:_:)'
source_url: 'https://developer.apple.com/documentation/coretext/ctlinecreatejustifiedline(_:_:_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coretext/ctlinecreatejustifiedline%28_%3A_%3A_%3A%29.json'
content_hash: 'sha256:e20b585a56827732'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Text](../coretext.md)

# CTLineCreateJustifiedLine(_:_:_:)

<sub>Function</sub>

Creates a justified line from an existing line.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func CTLineCreateJustifiedLine(_ line: CTLine, _ justificationFactor: CGFloat, _ justificationWidth: Double) -> CTLine?
```

## Parameters

- `line` — The line from which to create a justified line.

- `justificationFactor` — Full or partial justification. When set to `1.0` or greater, full justification is performed. If this parameter is set to less than `1.0`, varying degrees of partial justification are performed. If it is set to `0` or less, no justification is performed.

- `justificationWidth` — The width to which the resultant line is justified. If `justificationWidth` is less than the actual width of the line, then negative justification is performed (that is, glyphs are squeezed together).

## Return Value

A reference to a justified CTLine object if the call was successful; otherwise, `NULL`.

## See Also

### Creating Lines

- [CTLineCreateWithAttributedString](<ctlinecreatewithattributedstring(__).md>) — Creates a single immutable line object from an attributed string.
- [CTLineCreateTruncatedLine](<ctlinecreatetruncatedline(________).md>) — Creates a truncated line from an existing line.
