---
title: 'CTLineGetOffsetForStringIndex(_:_:_:)'
framework: Core Text
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS 3.2+, iPadOS 3.2+, Mac Catalyst 13.1+, macOS 10.5+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/coretext/ctlinegetoffsetforstringindex(_:_:_:)'
source_url: 'https://developer.apple.com/documentation/coretext/ctlinegetoffsetforstringindex(_:_:_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coretext/ctlinegetoffsetforstringindex%28_%3A_%3A_%3A%29.json'
content_hash: 'sha256:942dfe3cee638e56'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Text](../coretext.md)

# CTLineGetOffsetForStringIndex(_:_:_:)

<sub>Function</sub>

Determines the graphical offset or offsets for a string index.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func CTLineGetOffsetForStringIndex(_ line: CTLine, _ charIndex: CFIndex, _ secondaryOffset: UnsafeMutablePointer<CGFloat>?) -> CGFloat
```

## Parameters

- `line` — The line from which the offset is requested.

- `charIndex` — The string index corresponding to the desired position.

- `secondaryOffset` — On output, the secondary offset along the baseline for `charIndex`. When a single caret is sufficient for a string index, this value will be the same as the primary offset, which is the return value of this function. May be `NULL`.

## Return Value

The primary offset along the baseline for `charIndex`, or `0.0` if the line does not support string access.

## Discussion

This function returns the graphical offset or offsets corresponding to a string index, suitable for movement between adjacent lines or for drawing a custom caret. For moving between adjacent lines, the primary offset can be adjusted for any relative indentation of the two lines; a [CGPoint](../corefoundation/cgpoint.md) constructed with the adjusted offset for its `x` value and `0.0` for its `y` value is suitable for passing to [CTLineGetStringIndexForPosition](<ctlinegetstringindexforposition(____).md>). For drawing a custom caret, the returned primary offset corresponds to the portion of the caret that represents the visual insertion location for a character whose direction matches the line’s writing direction.

## See Also

### Getting Line Positioning

- [CTLineGetStringIndexForPosition](<ctlinegetstringindexforposition(____).md>) — Performs hit testing.
- [CTLineEnumerateCaretOffsets](<ctlineenumeratecaretoffsets(____).md>) — Enumerates caret offsets for characters in a line.
