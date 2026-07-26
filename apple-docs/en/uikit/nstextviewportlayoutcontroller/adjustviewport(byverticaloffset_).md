---
title: 'adjustViewport(byVerticalOffset:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, tvOS 15.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/nstextviewportlayoutcontroller/adjustviewport(byverticaloffset:)'
source_url: 'https://developer.apple.com/documentation/uikit/nstextviewportlayoutcontroller/adjustviewport(byverticaloffset:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/nstextviewportlayoutcontroller/adjustviewport%28byverticaloffset%3A%29.json'
content_hash: 'sha256:6db94c6f171f6bea'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [NSTextViewportLayoutController](../nstextviewportlayoutcontroller.md)

# adjustViewport(byVerticalOffset:)

<sub>Instance Method</sub>

Adjusts the viewport rect by the specified offset if needed.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
func adjustViewport(byVerticalOffset verticalOffset: CGFloat)
```

## Parameters

- `verticalOffset` — A `CGFloat` that represents the offset amount to apply to the viewport.

## See Also

### Accessing the viewport characteristics

- [viewportBounds](viewportbounds.md) — Returns the visible bounds of the view, plus the overdraw area.
- [viewportRange](viewportrange.md) — Returns the text range of the current viewport layout.
- [- layoutViewport](<layoutviewport().md>) — Performs layout in the viewport.
- [- relocateViewportToTextLocation:](<relocateviewport(to_).md>) — Relocates the viewport to the location you specify.
