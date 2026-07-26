---
title: setModeFlag
framework: Core Graphics
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [Mac Catalyst, macOS]
languages: [swift, swift, swift, occ, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/coregraphics/cgdisplaychangesummaryflags/setmodeflag
source_url: 'https://developer.apple.com/documentation/coregraphics/cgdisplaychangesummaryflags/setmodeflag'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coregraphics/cgdisplaychangesummaryflags/setmodeflag.json'
content_hash: 'sha256:7e055a67d445d2c1'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Graphics](../../coregraphics.md) · [CGDisplayChangeSummaryFlags](../cgdisplaychangesummaryflags.md)

# setModeFlag

<sub>Type Property</sub>

The display mode has changed.

<sub>Mac Catalyst, macOS</sub>

```swift
static var setModeFlag: CGDisplayChangeSummaryFlags { get }
```

## See Also

### Constants

- [kCGDisplayBeginConfigurationFlag](beginconfigurationflag.md) — The display configuration is about to change.
- [kCGDisplayMovedFlag](movedflag.md) — The location of the upper-left corner of the display in the global display coordinate space has changed.
- [kCGDisplaySetMainFlag](setmainflag.md) — The display is now the main display.
- [kCGDisplayAddFlag](addflag.md) — The display has been added to the active display list.
- [kCGDisplayRemoveFlag](removeflag.md) — The display has been removed from the active display list.
- [kCGDisplayEnabledFlag](enabledflag.md) — The display has been enabled.
- [kCGDisplayDisabledFlag](disabledflag.md) — The display has been disabled.
- [kCGDisplayMirrorFlag](mirrorflag.md) — The display is now mirroring another display.
- [kCGDisplayUnMirrorFlag](unmirrorflag.md) — The display is no longer mirroring another display.
- [kCGDisplayDesktopShapeChangedFlag](desktopshapechangedflag.md)
