---
title: 'CTTypesetterCreateLine(_:_:)'
framework: Core Text
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS 3.2+, iPadOS 3.2+, Mac Catalyst 13.1+, macOS 10.5+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/coretext/cttypesettercreateline(_:_:)'
source_url: 'https://developer.apple.com/documentation/coretext/cttypesettercreateline(_:_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coretext/cttypesettercreateline%28_%3A_%3A%29.json'
content_hash: 'sha256:f13943fecd5f8185'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Text](../coretext.md)

# CTTypesetterCreateLine(_:_:)

<sub>Function</sub>

Creates an immutable line from the typesetter.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func CTTypesetterCreateLine(_ typesetter: CTTypesetter, _ stringRange: CFRange) -> CTLine
```

## Parameters

- `typesetter` — The typesetter that creates the line. This parameter is required and cannot be set to `NULL`.

- `stringRange` — The string range on which the line is based. If the length portion of range is set to `0`, then the typesetter continues to add glyphs to the line until it runs out of characters in the string. The location and length of the range must be within the bounds of the string, or the call will fail.

## Return Value

A reference to a CTLine object if the call was successful; otherwise, `NULL`.

## Discussion

The resultant line consists of glyphs in the correct visual order, ready to draw. This function is equivalent to [CTTypesetterCreateLineWithOffset](<cttypesettercreatelinewithoffset(______).md>) with an offset of 0.0.

## See Also

### Creating Lines

- [CTTypesetterCreateLineWithOffset](<cttypesettercreatelinewithoffset(______).md>) — Creates an immutable line from the typesetter at a specified line offset.
