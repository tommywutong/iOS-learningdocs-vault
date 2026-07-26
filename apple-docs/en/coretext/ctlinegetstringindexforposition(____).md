---
title: 'CTLineGetStringIndexForPosition(_:_:)'
framework: Core Text
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS 3.2+, iPadOS 3.2+, Mac Catalyst 13.1+, macOS 10.5+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/coretext/ctlinegetstringindexforposition(_:_:)'
source_url: 'https://developer.apple.com/documentation/coretext/ctlinegetstringindexforposition(_:_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coretext/ctlinegetstringindexforposition%28_%3A_%3A%29.json'
content_hash: 'sha256:0f9671bb7d655d56'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Text](../coretext.md)

# CTLineGetStringIndexForPosition(_:_:)

<sub>Function</sub>

Performs hit testing.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func CTLineGetStringIndexForPosition(_ line: CTLine, _ position: CGPoint) -> CFIndex
```

## Parameters

- `line` — The line being examined.

- `position` — The location of the mouse click relative to the line’s origin.

## Return Value

The string index for the position, or if the line does not support string access, [kCFNotFound](../corefoundation/kcfnotfound.md). Relative to the line’s string range, this value can be no less than the first string index and no greater than the last string index plus 1.

## Discussion

This function can be used to determine the string index for a mouse click or other event. This string index corresponds to the character before which the next character should be inserted. This determination is made by analyzing the string from which a typesetter was created and the corresponding glyphs as embodied by a particular line.

## See Also

### Getting Line Positioning

- [CTLineGetOffsetForStringIndex](<ctlinegetoffsetforstringindex(______).md>) — Determines the graphical offset or offsets for a string index.
- [CTLineEnumerateCaretOffsets](<ctlineenumeratecaretoffsets(____).md>) — Enumerates caret offsets for characters in a line.
