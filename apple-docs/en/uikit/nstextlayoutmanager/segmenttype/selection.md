---
title: NSTextLayoutManager.SegmentType.selection
framework: UIKit
symbol_kind: case
role: symbol
role_heading: Case
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, tvOS 15.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/nstextlayoutmanager/segmenttype/selection
source_url: 'https://developer.apple.com/documentation/uikit/nstextlayoutmanager/segmenttype/selection'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/nstextlayoutmanager/segmenttype/selection.json'
content_hash: 'sha256:02738ef74aceb6d4'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [UIKit](../../../uikit.md) · [NSTextLayoutManager](../../nstextlayoutmanager.md) · [SegmentType](../segmenttype.md)

# NSTextLayoutManager.SegmentType.selection

<sub>Case</sub>

The segment behavior suitable for selection rendering.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
case selection
```

## Discussion

This segment type extends the last segment in a line fragment to the trailing edge if continuing to the next line.

## See Also

### Kinds of text selection segments

- [NSTextLayoutManagerSegmentTypeHighlight](highlight.md) — The segment behavior suitable for highlighting.
- [NSTextLayoutManagerSegmentTypeStandard](standard.md) — The standard segment, matching the typographic bounds of the range.
