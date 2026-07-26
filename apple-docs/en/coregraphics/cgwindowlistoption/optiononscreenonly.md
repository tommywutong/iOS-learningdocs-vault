---
title: optionOnScreenOnly
framework: Core Graphics
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [Mac Catalyst, macOS]
languages: [swift, swift, swift, swift, occ, occ, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/coregraphics/cgwindowlistoption/optiononscreenonly
source_url: 'https://developer.apple.com/documentation/coregraphics/cgwindowlistoption/optiononscreenonly'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coregraphics/cgwindowlistoption/optiononscreenonly.json'
content_hash: 'sha256:cbc5c602b33a1fdb'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Graphics](../../coregraphics.md) · [CGWindowListOption](../cgwindowlistoption.md)

# optionOnScreenOnly

<sub>Type Property</sub>

<sub>Mac Catalyst, macOS</sub>

```swift
static var optionOnScreenOnly: CGWindowListOption { get }
```

## Discussion

List all windows that are currently onscreen. Windows are returned in order from front to back. When retrieving a list with this option, the `relativeToWindow` parameter should be set to [kCGNullWindowID](../kcgnullwindowid.md).

## See Also

### Type Properties

- [kCGWindowListExcludeDesktopElements](excludedesktopelements.md)
- [kCGWindowListOptionAll](optionall.md)
- [kCGWindowListOptionIncludingWindow](optionincludingwindow.md)
- [kCGWindowListOptionOnScreenAboveWindow](optiononscreenabovewindow.md)
- [kCGWindowListOptionOnScreenBelowWindow](optiononscreenbelowwindow.md)
