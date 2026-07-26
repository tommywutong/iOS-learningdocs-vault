---
title: 'CTFrameGetStringRange(_:)'
framework: Core Text
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS 3.2+, iPadOS 3.2+, Mac Catalyst 13.1+, macOS 10.5+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/coretext/ctframegetstringrange(_:)'
source_url: 'https://developer.apple.com/documentation/coretext/ctframegetstringrange(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coretext/ctframegetstringrange%28_%3A%29.json'
content_hash: 'sha256:19ef198d8fb8ba8e'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Text](../coretext.md)

# CTFrameGetStringRange(_:)

<sub>Function</sub>

Returns the range of characters originally requested to fill the frame.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func CTFrameGetStringRange(_ frame: CTFrame) -> CFRange
```

## Parameters

- `frame` — The frame whose character range is returned.

## Return Value

A `CFRange` structure containing the backing store range of characters that were originally requested to fill the frame, or, if the function call is not successful, an empty range.

## See Also

### Getting Frame Data

- [CTFrameGetVisibleStringRange](<ctframegetvisiblestringrange(__).md>) — Returns the range of characters that actually fit in the frame.
- [CTFrameGetPath](<ctframegetpath(__).md>) — Returns the path used to create the frame.
- [CTFrameGetFrameAttributes](<ctframegetframeattributes(__).md>) — Returns the frame attributes used to create the frame.
