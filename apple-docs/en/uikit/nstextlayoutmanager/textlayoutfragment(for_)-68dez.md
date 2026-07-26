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
doc_path: '/documentation/uikit/nstextlayoutmanager/textlayoutfragment(for:)-68dez'
source_url: 'https://developer.apple.com/documentation/uikit/nstextlayoutmanager/textlayoutfragment(for:)-68dez'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/nstextlayoutmanager/textlayoutfragment%28for%3A%29-68dez.json'
content_hash: 'sha256:0d424222a17275c8'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [NSTextLayoutManager](../nstextlayoutmanager.md)

# textLayoutFragment(for:)

<sub>Instance Method</sub>

Returns the text layout fragment from the document at the specified location.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
func textLayoutFragment(for location: any NSTextLocation) -> NSTextLayoutFragment?
```

## Parameters

- `location` — The starting location.

## Return Value

An [NSTextLayoutFragment](../nstextlayoutfragment.md).

## See Also

### Causing layout generation

- [textViewportLayoutController](textviewportlayoutcontroller.md) — Returns text viewport layout controller associated with the layout manager’s text container.
- [- invalidateLayoutForRange:](<invalidatelayout(for_).md>) — Invalidates the layout information for specified text range.
- [- textLayoutFragmentForPosition:](<textlayoutfragment(for_)-4dhrx.md>) — Returns the text layout fragment at the position you specify in the text container.
- [- ensureLayoutForBounds:](<ensurelayout(for_)-6ptsj.md>) — Performs the layout for filling the bounds you specify inside the last text container.
- [- ensureLayoutForRange:](<ensurelayout(for_)-3duae.md>) — Performs the layout for specified text range.
- [- enumerateTextLayoutFragmentsFromLocation:options:usingBlock:](<enumeratetextlayoutfragments(from_options_using_).md>) — Enumerates the text layout fragments starting at the specified location.
- [SegmentType](segmenttype.md) — Values that describe the rendering of selection boundaries.
- [SegmentOptions](segmentoptions.md) — Values that describe where and how the framework extends segments of a selection.
