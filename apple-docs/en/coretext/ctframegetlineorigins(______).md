---
title: 'CTFrameGetLineOrigins(_:_:_:)'
framework: Core Text
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS 3.2+, iPadOS 3.2+, Mac Catalyst 13.1+, macOS 10.5+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/coretext/ctframegetlineorigins(_:_:_:)'
source_url: 'https://developer.apple.com/documentation/coretext/ctframegetlineorigins(_:_:_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coretext/ctframegetlineorigins%28_%3A_%3A_%3A%29.json'
content_hash: 'sha256:17288f1dcb5a8f1e'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Text](../coretext.md)

# CTFrameGetLineOrigins(_:_:_:)

<sub>Function</sub>

Copies a range of line origins for a frame.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func CTFrameGetLineOrigins(_ frame: CTFrame, _ range: CFRange, _ origins: UnsafeMutablePointer<CGPoint>)
```

## Parameters

- `frame` — The frame whose line origin array is copied.

- `range` — The range of line origins you wish to copy. If the length of the range is 0, then the copy operation continues from the start index of the range to the last line origin.

- `origins` — The buffer to which the origins are copied. The buffer must have at least as many elements as specified by range’s length. Each [CGPoint](../corefoundation/cgpoint.md) in this array is the origin of the corresponding line in the array of lines returned by [CTFrameGetLines](<ctframegetlines(__).md>) relative to the origin of the path’s bounding box, which can be obtained from `CGPathGetPathBoundingBox`.

## Discussion

This function copies a range of [CGPoint](../corefoundation/cgpoint.md) structures into the `origins` buffer. The maximum number of line origins this function will copy into the `origins` buffer is the count of the array of lines (the length of the `range` parameter).

### Special Considerations

In versions of macOS prior to 10.7 and versions of iOS prior to 4.2, this function may function unpredictably if the frame is not rectangular.

## See Also

### Getting Lines

- [CTFrameGetLines](<ctframegetlines(__).md>) — Returns an array of lines stored in the frame.
