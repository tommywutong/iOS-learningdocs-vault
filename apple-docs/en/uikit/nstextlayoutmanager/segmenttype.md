---
title: NSTextLayoutManager.SegmentType
framework: UIKit
symbol_kind: enum
role: symbol
role_heading: Enumeration
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, tvOS 15.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/nstextlayoutmanager/segmenttype
source_url: 'https://developer.apple.com/documentation/uikit/nstextlayoutmanager/segmenttype'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/nstextlayoutmanager/segmenttype.json'
content_hash: 'sha256:eedbf626596bfd7f'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [NSTextLayoutManager](../nstextlayoutmanager.md)

# NSTextLayoutManager.SegmentType

<sub>Enumeration</sub>

Values that describe the rendering of selection boundaries.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
enum SegmentType
```

## Relationships

- **Conforms To**: [BitwiseCopyable](../../swift/bitwisecopyable.md), [Equatable](../../swift/equatable.md), [Hashable](../../swift/hashable.md), [RawRepresentable](../../swift/rawrepresentable.md), [Sendable](../../swift/sendable.md), [SendableMetatype](../../swift/sendablemetatype.md)

## Topics

### Kinds of text selection segments

- [NSTextLayoutManagerSegmentTypeHighlight](segmenttype/highlight.md) — The segment behavior suitable for highlighting.
- [NSTextLayoutManagerSegmentTypeSelection](segmenttype/selection.md) — The segment behavior suitable for selection rendering.
- [NSTextLayoutManagerSegmentTypeStandard](segmenttype/standard.md) — The standard segment, matching the typographic bounds of the range.

### Initializers

- [init(rawValue:)](<segmenttype/init(rawvalue_).md>)

## See Also

### Causing layout generation

- [textViewportLayoutController](textviewportlayoutcontroller.md) — Returns text viewport layout controller associated with the layout manager’s text container.
- [- invalidateLayoutForRange:](<invalidatelayout(for_).md>) — Invalidates the layout information for specified text range.
- [- textLayoutFragmentForLocation:](<textlayoutfragment(for_)-68dez.md>) — Returns the text layout fragment from the document at the specified location.
- [- textLayoutFragmentForPosition:](<textlayoutfragment(for_)-4dhrx.md>) — Returns the text layout fragment at the position you specify in the text container.
- [- ensureLayoutForBounds:](<ensurelayout(for_)-6ptsj.md>) — Performs the layout for filling the bounds you specify inside the last text container.
- [- ensureLayoutForRange:](<ensurelayout(for_)-3duae.md>) — Performs the layout for specified text range.
- [- enumerateTextLayoutFragmentsFromLocation:options:usingBlock:](<enumeratetextlayoutfragments(from_options_using_).md>) — Enumerates the text layout fragments starting at the specified location.
- [SegmentOptions](segmentoptions.md) — Values that describe where and how the framework extends segments of a selection.
