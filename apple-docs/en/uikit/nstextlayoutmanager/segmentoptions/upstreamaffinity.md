---
title: upstreamAffinity
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, tvOS 15.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/nstextlayoutmanager/segmentoptions/upstreamaffinity
source_url: 'https://developer.apple.com/documentation/uikit/nstextlayoutmanager/segmentoptions/upstreamaffinity'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/nstextlayoutmanager/segmentoptions/upstreamaffinity.json'
content_hash: 'sha256:454e3f3714ae568a'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [UIKit](../../../uikit.md) · [NSTextLayoutManager](../../nstextlayoutmanager.md) · [SegmentOptions](../segmentoptions.md)

# upstreamAffinity

<sub>Type Property</sub>

Returns the value that causes the framework to the place the segment based on the upstream affinity for an empty range.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
static var upstreamAffinity: NSTextLayoutManager.SegmentOptions { get }
```

## See Also

### Getting segment options

- [NSTextLayoutManagerSegmentOptionsHeadSegmentExtended](headsegmentextended.md) — Returns the value that causes the framework to extend the segment to the tail edge.
- [NSTextLayoutManagerSegmentOptionsMiddleFragmentsExcluded](middlefragmentsexcluded.md) — Returns the value that causes the framework to enumerate segments in only the first and last line fragments.
- [NSTextLayoutManagerSegmentOptionsRangeNotRequired](rangenotrequired.md) — Returns the value that causes the framework enumerate text segment rectangles, but avoids preparing a range object.
- [NSTextLayoutManagerSegmentOptionsTailSegmentExtended](tailsegmentextended.md) — Returns the value that causes the framework to extend the segment to the tail edge.
