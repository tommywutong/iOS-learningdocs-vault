---
title: setMainFlag
framework: Core Graphics
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [Mac Catalyst, macOS]
languages: [swift, swift, swift, occ, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/coregraphics/cgdisplaychangesummaryflags/setmainflag
source_url: 'https://developer.apple.com/documentation/coregraphics/cgdisplaychangesummaryflags/setmainflag'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coregraphics/cgdisplaychangesummaryflags/setmainflag.json'
content_hash: 'sha256:a648c0c1a769de17'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Graphics](../../coregraphics.md) · [CGDisplayChangeSummaryFlags](../cgdisplaychangesummaryflags.md)

# setMainFlag

<sub>Type Property</sub>

The display is now the main display.

<sub>Mac Catalyst, macOS</sub>

```swift
static var setMainFlag: CGDisplayChangeSummaryFlags { get }
```

## See Also

### Constants

- [kCGDisplayBeginConfigurationFlag](beginconfigurationflag.md) — The display configuration is about to change.
- [kCGDisplayMovedFlag](movedflag.md) — The location of the upper-left corner of the display in the global display coordinate space has changed.
- [kCGDisplaySetModeFlag](setmodeflag.md) — The display mode has changed.
- [kCGDisplayAddFlag](addflag.md) — The display has been added to the active display list.
- [kCGDisplayRemoveFlag](removeflag.md) — The display has been removed from the active display list.
- [kCGDisplayEnabledFlag](enabledflag.md) — The display has been enabled.
- [kCGDisplayDisabledFlag](disabledflag.md) — The display has been disabled.
- [kCGDisplayMirrorFlag](mirrorflag.md) — The display is now mirroring another display.
- [kCGDisplayUnMirrorFlag](unmirrorflag.md) — The display is no longer mirroring another display.
- [kCGDisplayDesktopShapeChangedFlag](desktopshapechangedflag.md)
