---
title: optionAll
framework: Core Graphics
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [Mac Catalyst, macOS]
languages: [swift, swift, swift, swift, occ, occ, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/coregraphics/cgwindowlistoption/optionall
source_url: 'https://developer.apple.com/documentation/coregraphics/cgwindowlistoption/optionall'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coregraphics/cgwindowlistoption/optionall.json'
content_hash: 'sha256:cf65eacf2306b3b8'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Graphics](../../coregraphics.md) · [CGWindowListOption](../cgwindowlistoption.md)

# optionAll

<sub>Type Property</sub>

<sub>Mac Catalyst, macOS</sub>

```swift
static var optionAll: CGWindowListOption { get }
```

## Discussion

List all windows, including both onscreen and offscreen windows. When retrieving a list with this option, the `relativeToWindow` parameter should be set to [kCGNullWindowID](../kcgnullwindowid.md).

## See Also

### Type Properties

- [kCGWindowListExcludeDesktopElements](excludedesktopelements.md)
- [kCGWindowListOptionIncludingWindow](optionincludingwindow.md)
- [kCGWindowListOptionOnScreenAboveWindow](optiononscreenabovewindow.md)
- [kCGWindowListOptionOnScreenBelowWindow](optiononscreenbelowwindow.md)
- [kCGWindowListOptionOnScreenOnly](optiononscreenonly.md)
