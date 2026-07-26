---
title: 'CTFrameGetLines(_:)'
framework: Core Text
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS 3.2+, iPadOS 3.2+, Mac Catalyst 13.1+, macOS 10.5+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/coretext/ctframegetlines(_:)'
source_url: 'https://developer.apple.com/documentation/coretext/ctframegetlines(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coretext/ctframegetlines%28_%3A%29.json'
content_hash: 'sha256:338f2ead62dc355c'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Text](../coretext.md)

# CTFrameGetLines(_:)

<sub>Function</sub>

Returns an array of lines stored in the frame.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func CTFrameGetLines(_ frame: CTFrame) -> CFArray
```

## Parameters

- `frame` — The frame whose line array is returned.

## Return Value

A CFArray object containing the CTLine objects that make up the frame, or, if there are no lines in the frame, an array with no elements.

## See Also

### Getting Lines

- [CTFrameGetLineOrigins](<ctframegetlineorigins(______).md>) — Copies a range of line origins for a frame.
