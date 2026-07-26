---
title: textViewportLayoutController
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, tvOS 15.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/nstextlayoutmanager/textviewportlayoutcontroller
source_url: 'https://developer.apple.com/documentation/uikit/nstextlayoutmanager/textviewportlayoutcontroller'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/nstextlayoutmanager/textviewportlayoutcontroller.json'
content_hash: 'sha256:b33a08f70e4ddb5e'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [NSTextLayoutManager](../nstextlayoutmanager.md)

# textViewportLayoutController

<sub>Instance Property</sub>

Returns text viewport layout controller associated with the layout manager’s text container.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
var textViewportLayoutController: NSTextViewportLayoutController { get }
```

## See Also

### Causing layout generation

- [- invalidateLayoutForRange:](<invalidatelayout(for_).md>) — Invalidates the layout information for specified text range.
- [- textLayoutFragmentForLocation:](<textlayoutfragment(for_)-68dez.md>) — Returns the text layout fragment from the document at the specified location.
- [- textLayoutFragmentForPosition:](<textlayoutfragment(for_)-4dhrx.md>) — Returns the text layout fragment at the position you specify in the text container.
- [- ensureLayoutForBounds:](<ensurelayout(for_)-6ptsj.md>) — Performs the layout for filling the bounds you specify inside the last text container.
- [- ensureLayoutForRange:](<ensurelayout(for_)-3duae.md>) — Performs the layout for specified text range.
- [- enumerateTextLayoutFragmentsFromLocation:options:usingBlock:](<enumeratetextlayoutfragments(from_options_using_).md>) — Enumerates the text layout fragments starting at the specified location.
- [SegmentType](segmenttype.md) — Values that describe the rendering of selection boundaries.
- [SegmentOptions](segmentoptions.md) — Values that describe where and how the framework extends segments of a selection.
