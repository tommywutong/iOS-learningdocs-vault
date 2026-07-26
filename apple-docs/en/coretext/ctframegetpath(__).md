---
title: 'CTFrameGetPath(_:)'
framework: Core Text
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS 3.2+, iPadOS 3.2+, Mac Catalyst 13.1+, macOS 10.5+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/coretext/ctframegetpath(_:)'
source_url: 'https://developer.apple.com/documentation/coretext/ctframegetpath(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coretext/ctframegetpath%28_%3A%29.json'
content_hash: 'sha256:f18151d85fd96fd2'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Text](../coretext.md)

# CTFrameGetPath(_:)

<sub>Function</sub>

Returns the path used to create the frame.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func CTFrameGetPath(_ frame: CTFrame) -> CGPath
```

## Parameters

- `frame` — The frame whose path is returned.

## See Also

### Getting Frame Data

- [CTFrameGetStringRange](<ctframegetstringrange(__).md>) — Returns the range of characters originally requested to fill the frame.
- [CTFrameGetVisibleStringRange](<ctframegetvisiblestringrange(__).md>) — Returns the range of characters that actually fit in the frame.
- [CTFrameGetFrameAttributes](<ctframegetframeattributes(__).md>) — Returns the frame attributes used to create the frame.
