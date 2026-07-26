---
title: optionOnScreenBelowWindow
framework: Core Graphics
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [Mac Catalyst, macOS]
languages: [swift, swift, swift, swift, occ, occ, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/coregraphics/cgwindowlistoption/optiononscreenbelowwindow
source_url: 'https://developer.apple.com/documentation/coregraphics/cgwindowlistoption/optiononscreenbelowwindow'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coregraphics/cgwindowlistoption/optiononscreenbelowwindow.json'
content_hash: 'sha256:62008da80501313a'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Graphics](../../coregraphics.md) · [CGWindowListOption](../cgwindowlistoption.md)

# optionOnScreenBelowWindow

<sub>Type Property</sub>

<sub>Mac Catalyst, macOS</sub>

```swift
static var optionOnScreenBelowWindow: CGWindowListOption { get }
```

## Discussion

List all windows that are currently onscreen and in behind the window specified in the `relativeToWindow` parameter. Windows are returned in order from front to back.

## See Also

### Type Properties

- [kCGWindowListExcludeDesktopElements](excludedesktopelements.md)
- [kCGWindowListOptionAll](optionall.md)
- [kCGWindowListOptionIncludingWindow](optionincludingwindow.md)
- [kCGWindowListOptionOnScreenAboveWindow](optiononscreenabovewindow.md)
- [kCGWindowListOptionOnScreenOnly](optiononscreenonly.md)
