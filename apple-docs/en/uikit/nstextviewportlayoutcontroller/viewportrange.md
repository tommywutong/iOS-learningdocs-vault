---
title: viewportRange
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, tvOS 15.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/nstextviewportlayoutcontroller/viewportrange
source_url: 'https://developer.apple.com/documentation/uikit/nstextviewportlayoutcontroller/viewportrange'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/nstextviewportlayoutcontroller/viewportrange.json'
content_hash: 'sha256:95ada4cddedcd0ac'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [NSTextViewportLayoutController](../nstextviewportlayoutcontroller.md)

# viewportRange

<sub>Instance Property</sub>

Returns the text range of the current viewport layout.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
var viewportRange: NSTextRange? { get }
```

## See Also

### Accessing the viewport characteristics

- [viewportBounds](viewportbounds.md) — Returns the visible bounds of the view, plus the overdraw area.
- [- adjustViewportByVerticalOffset:](<adjustviewport(byverticaloffset_).md>) — Adjusts the viewport rect by the specified offset if needed.
- [- layoutViewport](<layoutviewport().md>) — Performs layout in the viewport.
- [- relocateViewportToTextLocation:](<relocateviewport(to_).md>) — Relocates the viewport to the location you specify.
