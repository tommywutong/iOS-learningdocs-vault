---
title: optionIncludingWindow
framework: Core Graphics
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [Mac Catalyst, macOS]
languages: [swift, swift, swift, swift, occ, occ, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/coregraphics/cgwindowlistoption/optionincludingwindow
source_url: 'https://developer.apple.com/documentation/coregraphics/cgwindowlistoption/optionincludingwindow'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coregraphics/cgwindowlistoption/optionincludingwindow.json'
content_hash: 'sha256:e3a44cfba80e3bc0'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Graphics](../../coregraphics.md) · [CGWindowListOption](../cgwindowlistoption.md)

# optionIncludingWindow

<sub>Type Property</sub>

<sub>Mac Catalyst, macOS</sub>

```swift
static var optionIncludingWindow: CGWindowListOption { get }
```

## Discussion

Include the specified window (from the `relativeToWindow` parameter) in the returned list. You must combine this option with the [kCGWindowListOptionOnScreenAboveWindow](optiononscreenabovewindow.md) or [kCGWindowListOptionOnScreenBelowWindow](optiononscreenbelowwindow.md) option to retrieve meaningful results.

## See Also

### Type Properties

- [kCGWindowListExcludeDesktopElements](excludedesktopelements.md)
- [kCGWindowListOptionAll](optionall.md)
- [kCGWindowListOptionOnScreenAboveWindow](optiononscreenabovewindow.md)
- [kCGWindowListOptionOnScreenBelowWindow](optiononscreenbelowwindow.md)
- [kCGWindowListOptionOnScreenOnly](optiononscreenonly.md)
