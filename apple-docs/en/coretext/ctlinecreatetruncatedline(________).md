---
title: 'CTLineCreateTruncatedLine(_:_:_:_:)'
framework: Core Text
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS 3.2+, iPadOS 3.2+, Mac Catalyst 13.1+, macOS 10.5+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/coretext/ctlinecreatetruncatedline(_:_:_:_:)'
source_url: 'https://developer.apple.com/documentation/coretext/ctlinecreatetruncatedline(_:_:_:_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coretext/ctlinecreatetruncatedline%28_%3A_%3A_%3A_%3A%29.json'
content_hash: 'sha256:e0afc67005ef56cb'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Text](../coretext.md)

# CTLineCreateTruncatedLine(_:_:_:_:)

<sub>Function</sub>

Creates a truncated line from an existing line.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func CTLineCreateTruncatedLine(_ line: CTLine, _ width: Double, _ truncationType: CTLineTruncationType, _ truncationToken: CTLine?) -> CTLine?
```

## Parameters

- `line` — The line from which to create a truncated line.

- `width` — The width at which truncation begins. The line is truncated if its width is greater than the width passed in this parameter.

- `truncationType` — The type of truncation to perform if needed. See [CTLineTruncationType](ctlinetruncationtype.md) for possible values.

- `truncationToken` — This token is added at the point where truncation took place, to indicate that the line was truncated. Usually, the truncation token is the ellipsis character (`U+2026`). If this parameter is set to `NULL`, then no truncation token is used and the line is simply cut off.

## Return Value

A reference to a truncated CTLine object if the call was successful; otherwise, `NULL`.

## Discussion

The line specified in `truncationToken` should have a width less than the width specified by the `width` parameter. If the width of the line specified in `truncationToken` is greater than `width` and truncation is needed, the function returns `NULL`.

## See Also

### Creating Lines

- [CTLineCreateWithAttributedString](<ctlinecreatewithattributedstring(__).md>) — Creates a single immutable line object from an attributed string.
- [CTLineCreateJustifiedLine](<ctlinecreatejustifiedline(______).md>) — Creates a justified line from an existing line.
