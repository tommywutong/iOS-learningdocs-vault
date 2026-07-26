---
title: 'CTFrameGetVisibleStringRange(_:)'
framework: Core Text
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS 3.2+, iPadOS 3.2+, Mac Catalyst 13.1+, macOS 10.5+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/coretext/ctframegetvisiblestringrange(_:)'
source_url: 'https://developer.apple.com/documentation/coretext/ctframegetvisiblestringrange(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coretext/ctframegetvisiblestringrange%28_%3A%29.json'
content_hash: 'sha256:59b88875a05a962d'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Text](../coretext.md)

# CTFrameGetVisibleStringRange(_:)

<sub>Function</sub>

Returns the range of characters that actually fit in the frame.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func CTFrameGetVisibleStringRange(_ frame: CTFrame) -> CFRange
```

## Parameters

- `frame` — The frame whose visible character range is returned.

## Return Value

A `CFRange` structure containing the backing store range of characters that fit into the frame, or if the function call is not successful or no characters fit in the frame, an empty range.

## Discussion

This function can be used to cascade frames, because it returns the range of characters that can be seen in the frame. The next frame would start where this frame ends.

## See Also

### Getting Frame Data

- [CTFrameGetStringRange](<ctframegetstringrange(__).md>) — Returns the range of characters originally requested to fill the frame.
- [CTFrameGetPath](<ctframegetpath(__).md>) — Returns the path used to create the frame.
- [CTFrameGetFrameAttributes](<ctframegetframeattributes(__).md>) — Returns the frame attributes used to create the frame.
