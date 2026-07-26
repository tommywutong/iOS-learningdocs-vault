---
title: 'textLayoutFragment(for:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, tvOS 15.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/nstextlayoutmanager/textlayoutfragment(for:)-4dhrx'
source_url: 'https://developer.apple.com/documentation/uikit/nstextlayoutmanager/textlayoutfragment(for:)-4dhrx'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/nstextlayoutmanager/textlayoutfragment%28for%3A%29-4dhrx.json'
content_hash: 'sha256:0d5cd400b3eb2c3e'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [NSTextLayoutManager](../nstextlayoutmanager.md)

# textLayoutFragment(for:)

<sub>Instance Method</sub>

Returns the text layout fragment at the position you specify in the text container.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
func textLayoutFragment(for position: CGPoint) -> NSTextLayoutFragment?
```

## Parameters

- `position` — A [CGPoint](../../corefoundation/cgpoint.md) that describes the position in the coordinate system for the text container.

## Return Value

An [NSTextLayoutFragment](../nstextlayoutfragment.md).

## See Also

### Causing layout generation

- [textViewportLayoutController](textviewportlayoutcontroller.md) — Returns text viewport layout controller associated with the layout manager’s text container.
- [- invalidateLayoutForRange:](<invalidatelayout(for_).md>) — Invalidates the layout information for specified text range.
- [- textLayoutFragmentForLocation:](<textlayoutfragment(for_)-68dez.md>) — Returns the text layout fragment from the document at the specified location.
- [- ensureLayoutForBounds:](<ensurelayout(for_)-6ptsj.md>) — Performs the layout for filling the bounds you specify inside the last text container.
- [- ensureLayoutForRange:](<ensurelayout(for_)-3duae.md>) — Performs the layout for specified text range.
- [- enumerateTextLayoutFragmentsFromLocation:options:usingBlock:](<enumeratetextlayoutfragments(from_options_using_).md>) — Enumerates the text layout fragments starting at the specified location.
- [SegmentType](segmenttype.md) — Values that describe the rendering of selection boundaries.
- [SegmentOptions](segmentoptions.md) — Values that describe where and how the framework extends segments of a selection.
