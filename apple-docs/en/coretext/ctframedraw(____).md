---
title: 'CTFrameDraw(_:_:)'
framework: Core Text
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS 3.2+, iPadOS 3.2+, Mac Catalyst 13.1+, macOS 10.5+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/coretext/ctframedraw(_:_:)'
source_url: 'https://developer.apple.com/documentation/coretext/ctframedraw(_:_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coretext/ctframedraw%28_%3A_%3A%29.json'
content_hash: 'sha256:61c47a0ce6f129ac'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Text](../coretext.md)

# CTFrameDraw(_:_:)

<sub>Function</sub>

Draws an entire frame into a context.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func CTFrameDraw(_ frame: CTFrame, _ context: CGContext)
```

## Parameters

- `frame` — The frame to draw.

- `context` — The context in which to draw the frame.

## Discussion

If both the frame and the context are valid, the frame is drawn in the context. This call can leave the context in any state and does not flush it after the draw operation.
