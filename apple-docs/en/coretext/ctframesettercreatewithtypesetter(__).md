---
title: 'CTFramesetterCreateWithTypesetter(_:)'
framework: Core Text
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS 12.0+, iPadOS 12.0+, Mac Catalyst 13.1+, macOS 10.14+, tvOS 12.0+, visionOS 1.0+, watchOS 5.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/coretext/ctframesettercreatewithtypesetter(_:)'
source_url: 'https://developer.apple.com/documentation/coretext/ctframesettercreatewithtypesetter(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coretext/ctframesettercreatewithtypesetter%28_%3A%29.json'
content_hash: 'sha256:0047722466c87c0f'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Text](../coretext.md)

# CTFramesetterCreateWithTypesetter(_:)

<sub>Function</sub>

Creates a framesetter directly from a typesetter.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func CTFramesetterCreateWithTypesetter(_ typesetter: CTTypesetter) -> CTFramesetter
```

## Parameters

- `typesetter` — The typesetter that the framesetter uses to lay out text.

## Return Value

This function returns a reference to a `CTFramesetter` object.

## Discussion

Each framesetter uses a typesetter internally to perform line breaking and other contextual analysis according to the characters in a string. This function allows the framesetter to use a typesetter that the system constructs using specific options.

## See Also

### Creating a Framesetter

- [CTFramesetterCreateWithAttributedString](<ctframesettercreatewithattributedstring(__).md>) — Creates an immutable framesetter object from an attributed string.
