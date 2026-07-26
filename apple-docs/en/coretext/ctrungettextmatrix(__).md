---
title: 'CTRunGetTextMatrix(_:)'
framework: Core Text
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS 3.2+, iPadOS 3.2+, Mac Catalyst 13.1+, macOS 10.5+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/coretext/ctrungettextmatrix(_:)'
source_url: 'https://developer.apple.com/documentation/coretext/ctrungettextmatrix(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coretext/ctrungettextmatrix%28_%3A%29.json'
content_hash: 'sha256:ec2f1f611413252c'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Text](../coretext.md)

# CTRunGetTextMatrix(_:)

<sub>Function</sub>

Returns the text matrix needed to draw this run.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func CTRunGetTextMatrix(_ run: CTRun) -> CGAffineTransform
```

## Parameters

- `run` — The run object from which to get the text matrix.

## Return Value

A [CGAffineTransform](../corefoundation/cgaffinetransform.md) structure.

## Discussion

To properly draw the glyphs in a run, the fields `tx` and `ty` of the [CGAffineTransform](../corefoundation/cgaffinetransform.md) returned by this function should be set to the current text position.

## See Also

### Drawing the Glyph Run

- [CTRunDraw](<ctrundraw(______).md>) — Draws a complete run or part of one.
