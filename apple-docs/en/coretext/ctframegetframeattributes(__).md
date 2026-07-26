---
title: 'CTFrameGetFrameAttributes(_:)'
framework: Core Text
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS 3.2+, iPadOS 3.2+, Mac Catalyst 13.1+, macOS 10.5+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/coretext/ctframegetframeattributes(_:)'
source_url: 'https://developer.apple.com/documentation/coretext/ctframegetframeattributes(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coretext/ctframegetframeattributes%28_%3A%29.json'
content_hash: 'sha256:593da3b2ce3c2f26'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Text](../coretext.md)

# CTFrameGetFrameAttributes(_:)

<sub>Function</sub>

Returns the frame attributes used to create the frame.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func CTFrameGetFrameAttributes(_ frame: CTFrame) -> CFDictionary?
```

## Parameters

- `frame` — The frame whose attributes are returned.

## Return Value

A reference to a CFDictionary object containing the frame attributes that were used to create the frame, or, if the frame was created without any frame attributes, `NULL`.

## Discussion

You can create a frame with an attributes dictionary to control various aspects of the framing process. These attributes are different from the ones used to create an attributed string.

## See Also

### Getting Frame Data

- [CTFrameGetStringRange](<ctframegetstringrange(__).md>) — Returns the range of characters originally requested to fill the frame.
- [CTFrameGetVisibleStringRange](<ctframegetvisiblestringrange(__).md>) — Returns the range of characters that actually fit in the frame.
- [CTFrameGetPath](<ctframegetpath(__).md>) — Returns the path used to create the frame.
