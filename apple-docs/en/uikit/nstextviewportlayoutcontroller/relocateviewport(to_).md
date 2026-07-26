---
title: 'relocateViewport(to:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, tvOS 15.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/nstextviewportlayoutcontroller/relocateviewport(to:)'
source_url: 'https://developer.apple.com/documentation/uikit/nstextviewportlayoutcontroller/relocateviewport(to:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/nstextviewportlayoutcontroller/relocateviewport%28to%3A%29.json'
content_hash: 'sha256:8410dbc3191b6a7a'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [NSTextViewportLayoutController](../nstextviewportlayoutcontroller.md)

# relocateViewport(to:)

<sub>Instance Method</sub>

Relocates the viewport to the location you specify.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
func relocateViewport(to textLocation: any NSTextLocation) -> CGFloat
```

## Parameters

- `textLocation` — An `NSTextLocation`.

## See Also

### Accessing the viewport characteristics

- [viewportBounds](viewportbounds.md) — Returns the visible bounds of the view, plus the overdraw area.
- [viewportRange](viewportrange.md) — Returns the text range of the current viewport layout.
- [- adjustViewportByVerticalOffset:](<adjustviewport(byverticaloffset_).md>) — Adjusts the viewport rect by the specified offset if needed.
- [- layoutViewport](<layoutviewport().md>) — Performs layout in the viewport.
