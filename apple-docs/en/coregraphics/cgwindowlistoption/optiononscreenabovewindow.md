---
title: optionOnScreenAboveWindow
framework: Core Graphics
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [Mac Catalyst, macOS]
languages: [swift, swift, swift, swift, occ, occ, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/coregraphics/cgwindowlistoption/optiononscreenabovewindow
source_url: 'https://developer.apple.com/documentation/coregraphics/cgwindowlistoption/optiononscreenabovewindow'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coregraphics/cgwindowlistoption/optiononscreenabovewindow.json'
content_hash: 'sha256:b130a0e9d9b71f48'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Graphics](../../coregraphics.md) · [CGWindowListOption](../cgwindowlistoption.md)

# optionOnScreenAboveWindow

<sub>Type Property</sub>

<sub>Mac Catalyst, macOS</sub>

```swift
static var optionOnScreenAboveWindow: CGWindowListOption { get }
```

## Discussion

List all windows that are currently onscreen and in front of the window specified in the `relativeToWindow` parameter. Windows are returned in order from front to back.

## See Also

### Type Properties

- [kCGWindowListExcludeDesktopElements](excludedesktopelements.md)
- [kCGWindowListOptionAll](optionall.md)
- [kCGWindowListOptionIncludingWindow](optionincludingwindow.md)
- [kCGWindowListOptionOnScreenBelowWindow](optiononscreenbelowwindow.md)
- [kCGWindowListOptionOnScreenOnly](optiononscreenonly.md)
