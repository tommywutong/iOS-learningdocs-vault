---
title: viewportBounds
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, tvOS 15.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/nstextviewportlayoutcontroller/viewportbounds
source_url: 'https://developer.apple.com/documentation/uikit/nstextviewportlayoutcontroller/viewportbounds'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/nstextviewportlayoutcontroller/viewportbounds.json'
content_hash: 'sha256:882f91f77ab08e4b'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [NSTextViewportLayoutController](../nstextviewportlayoutcontroller.md)

# viewportBounds

<sub>Instance Property</sub>

Returns the visible bounds of the view, plus the overdraw area.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
var viewportBounds: CGRect { get }
```

## See Also

### Accessing the viewport characteristics

- [viewportRange](viewportrange.md) — Returns the text range of the current viewport layout.
- [- adjustViewportByVerticalOffset:](<adjustviewport(byverticaloffset_).md>) — Adjusts the viewport rect by the specified offset if needed.
- [- layoutViewport](<layoutviewport().md>) — Performs layout in the viewport.
- [- relocateViewportToTextLocation:](<relocateviewport(to_).md>) — Relocates the viewport to the location you specify.
