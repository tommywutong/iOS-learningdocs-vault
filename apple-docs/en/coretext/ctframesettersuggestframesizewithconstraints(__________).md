---
title: 'CTFramesetterSuggestFrameSizeWithConstraints(_:_:_:_:_:)'
framework: Core Text
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS 3.2+, iPadOS 3.2+, Mac Catalyst 13.1+, macOS 10.5+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/coretext/ctframesettersuggestframesizewithconstraints(_:_:_:_:_:)'
source_url: 'https://developer.apple.com/documentation/coretext/ctframesettersuggestframesizewithconstraints(_:_:_:_:_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coretext/ctframesettersuggestframesizewithconstraints%28_%3A_%3A_%3A_%3A_%3A%29.json'
content_hash: 'sha256:e6b6c61d355bdbe3'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Text](../coretext.md)

# CTFramesetterSuggestFrameSizeWithConstraints(_:_:_:_:_:)

<sub>Function</sub>

Determines the frame size needed for a string range.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func CTFramesetterSuggestFrameSizeWithConstraints(_ framesetter: CTFramesetter, _ stringRange: CFRange, _ frameAttributes: CFDictionary?, _ constraints: CGSize, _ fitRange: UnsafeMutablePointer<CFRange>?) -> CGSize
```

## Parameters

- `framesetter` — The framesetter used for measuring the frame size.

- `stringRange` — The string range to which the frame size applies. The string range is a range over the string used to create the framesetter. If the length portion of the range is set to `0`, then the framesetter continues to add lines until it runs out of text or space.

- `frameAttributes` — Additional attributes that control the frame filling process, or `NULL` if there are no such attributes.

- `constraints` — The width and height to which the frame size is constrained. A value of [CGFLOAT_MAX](../corefoundation/cgfloat_max.md) for either dimension indicates that it should be treated as unconstrained.

- `fitRange` — On return, contains the range of the string that actually fit in the constrained size.

## Return Value

The actual dimensions for the given string range and constraints.

## Discussion

This function can be used to determine how much space is needed to display a string, optionally by constraining the space along either dimension.
