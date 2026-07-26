---
title: 'CTFramesetterCreateWithAttributedString(_:)'
framework: Core Text
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS 3.2+, iPadOS 3.2+, Mac Catalyst 13.1+, macOS 10.5+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/coretext/ctframesettercreatewithattributedstring(_:)'
source_url: 'https://developer.apple.com/documentation/coretext/ctframesettercreatewithattributedstring(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coretext/ctframesettercreatewithattributedstring%28_%3A%29.json'
content_hash: 'sha256:cf967119c22d752c'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Text](../coretext.md)

# CTFramesetterCreateWithAttributedString(_:)

<sub>Function</sub>

Creates an immutable framesetter object from an attributed string.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func CTFramesetterCreateWithAttributedString(_ attrString: CFAttributedString) -> CTFramesetter
```

## Parameters

- `attrString` — The attributed string for constructing the framesetter object.

## Return Value

A reference to a framesetter object if the call is successful; otherwise, `NULL`.

## Discussion

Use the framesetter object to create and fill text frames with the [CTFramesetterCreateFrame](<ctframesettercreateframe(________).md>) call.

> [!note] Note
> By default, the text system doesn’t typeset text that requires an unreasonable amount of effort. To create a framesetter that supports typesetting text regardless of the amount of effort necessary, create a [CTTypesetter](cttypesetter.md) with the [kCTTypesetterOptionAllowUnboundedLayout](kcttypesetteroptionallowunboundedlayout.md) option set to [kCFBooleanTrue](../corefoundation/kcfbooleantrue.md), then use [CTFramesetterCreateWithTypesetter](<ctframesettercreatewithtypesetter(__).md>) instead.

## See Also

### Creating a Framesetter

- [CTFramesetterCreateWithTypesetter](<ctframesettercreatewithtypesetter(__).md>) — Creates a framesetter directly from a typesetter.
