---
title: NSTextLayoutManager.SegmentOptions
framework: UIKit
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, tvOS 15.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/nstextlayoutmanager/segmentoptions
source_url: 'https://developer.apple.com/documentation/uikit/nstextlayoutmanager/segmentoptions'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/nstextlayoutmanager/segmentoptions.json'
content_hash: 'sha256:2e53aa07587dd3c7'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [NSTextLayoutManager](../nstextlayoutmanager.md)

# NSTextLayoutManager.SegmentOptions

<sub>Structure</sub>

Values that describe where and how the framework extends segments of a selection.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
struct SegmentOptions
```

## Relationships

- **Conforms To**: [BitwiseCopyable](../../swift/bitwisecopyable.md), [Equatable](../../swift/equatable.md), [ExpressibleByArrayLiteral](../../swift/expressiblebyarrayliteral.md), [OptionSet](../../swift/optionset.md), [RawRepresentable](../../swift/rawrepresentable.md), [Sendable](../../swift/sendable.md), [SendableMetatype](../../swift/sendablemetatype.md), [SetAlgebra](../../swift/setalgebra.md)

## Topics

### Creating segment options

- [init(rawValue:)](<segmentoptions/init(rawvalue_).md>) — Cceates a new segment option using the value you provide.

### Getting segment options

- [NSTextLayoutManagerSegmentOptionsHeadSegmentExtended](segmentoptions/headsegmentextended.md) — Returns the value that causes the framework to extend the segment to the tail edge.
- [NSTextLayoutManagerSegmentOptionsMiddleFragmentsExcluded](segmentoptions/middlefragmentsexcluded.md) — Returns the value that causes the framework to enumerate segments in only the first and last line fragments.
- [NSTextLayoutManagerSegmentOptionsRangeNotRequired](segmentoptions/rangenotrequired.md) — Returns the value that causes the framework enumerate text segment rectangles, but avoids preparing a range object.
- [NSTextLayoutManagerSegmentOptionsTailSegmentExtended](segmentoptions/tailsegmentextended.md) — Returns the value that causes the framework to extend the segment to the tail edge.
- [NSTextLayoutManagerSegmentOptionsUpstreamAffinity](segmentoptions/upstreamaffinity.md) — Returns the value that causes the framework to the place the segment based on the upstream affinity for an empty range.

## See Also

### Causing layout generation

- [textViewportLayoutController](textviewportlayoutcontroller.md) — Returns text viewport layout controller associated with the layout manager’s text container.
- [- invalidateLayoutForRange:](<invalidatelayout(for_).md>) — Invalidates the layout information for specified text range.
- [- textLayoutFragmentForLocation:](<textlayoutfragment(for_)-68dez.md>) — Returns the text layout fragment from the document at the specified location.
- [- textLayoutFragmentForPosition:](<textlayoutfragment(for_)-4dhrx.md>) — Returns the text layout fragment at the position you specify in the text container.
- [- ensureLayoutForBounds:](<ensurelayout(for_)-6ptsj.md>) — Performs the layout for filling the bounds you specify inside the last text container.
- [- ensureLayoutForRange:](<ensurelayout(for_)-3duae.md>) — Performs the layout for specified text range.
- [- enumerateTextLayoutFragmentsFromLocation:options:usingBlock:](<enumeratetextlayoutfragments(from_options_using_).md>) — Enumerates the text layout fragments starting at the specified location.
- [SegmentType](segmenttype.md) — Values that describe the rendering of selection boundaries.
