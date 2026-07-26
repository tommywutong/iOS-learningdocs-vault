---
title: 'enumerateTextLayoutFragments(from:options:using:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, tvOS 15.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/nstextlayoutmanager/enumeratetextlayoutfragments(from:options:using:)'
source_url: 'https://developer.apple.com/documentation/uikit/nstextlayoutmanager/enumeratetextlayoutfragments(from:options:using:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/nstextlayoutmanager/enumeratetextlayoutfragments%28from%3Aoptions%3Ausing%3A%29.json'
content_hash: 'sha256:49b982861ac725aa'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [NSTextLayoutManager](../nstextlayoutmanager.md)

# enumerateTextLayoutFragments(from:options:using:)

<sub>Instance Method</sub>

Enumerates the text layout fragments starting at the specified location.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
func enumerateTextLayoutFragments(from location: (any NSTextLocation)?, options: NSTextLayoutFragment.EnumerationOptions = [], using block: (NSTextLayoutFragment) -> Bool) -> (any NSTextLocation)?
```

## Parameters

- `location` — The location where youstart the enumeration.

- `options` — One or more of the available [EnumerationOptions](../nstextlayoutfragment/enumerationoptions.md).

- `block` — A closure you provide that determines if the enumeration finishes early.

## Return Value

An [NSTextLocation](../nstextlocation.md), or `nil`.

## Discussion

If `textLocation` is `nil`, the method starts at `self.textContentManager.documentRange.location`.The method uses `self.documentRange.endLocation` for reverse enumeration. When enumerating backward, it starts with the fragment preceding the one containing `textLocation`. If the method enumerates at least one fragment, it returns the edge of the enumerated range.

The enumerated range might not match the range of the last element returned; it enumerates the elements in the sequence, but it can skip a range. For example, it can limit the maximum number of text elements the method enumerates for a single invocation or hide some elements from the layout.

Returning `false` from `block` breaks out of the enumeration.

## See Also

### Causing layout generation

- [textViewportLayoutController](textviewportlayoutcontroller.md) — Returns text viewport layout controller associated with the layout manager’s text container.
- [- invalidateLayoutForRange:](<invalidatelayout(for_).md>) — Invalidates the layout information for specified text range.
- [- textLayoutFragmentForLocation:](<textlayoutfragment(for_)-68dez.md>) — Returns the text layout fragment from the document at the specified location.
- [- textLayoutFragmentForPosition:](<textlayoutfragment(for_)-4dhrx.md>) — Returns the text layout fragment at the position you specify in the text container.
- [- ensureLayoutForBounds:](<ensurelayout(for_)-6ptsj.md>) — Performs the layout for filling the bounds you specify inside the last text container.
- [- ensureLayoutForRange:](<ensurelayout(for_)-3duae.md>) — Performs the layout for specified text range.
- [SegmentType](segmenttype.md) — Values that describe the rendering of selection boundaries.
- [SegmentOptions](segmentoptions.md) — Values that describe where and how the framework extends segments of a selection.
