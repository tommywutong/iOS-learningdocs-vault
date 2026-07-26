---
title: beginConfigurationFlag
framework: Core Graphics
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [Mac Catalyst, macOS]
languages: [swift, swift, swift, occ, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/coregraphics/cgdisplaychangesummaryflags/beginconfigurationflag
source_url: 'https://developer.apple.com/documentation/coregraphics/cgdisplaychangesummaryflags/beginconfigurationflag'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coregraphics/cgdisplaychangesummaryflags/beginconfigurationflag.json'
content_hash: 'sha256:162196f22be8844d'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Graphics](../../coregraphics.md) · [CGDisplayChangeSummaryFlags](../cgdisplaychangesummaryflags.md)

# beginConfigurationFlag

<sub>Type Property</sub>

The display configuration is about to change.

<sub>Mac Catalyst, macOS</sub>

```swift
static var beginConfigurationFlag: CGDisplayChangeSummaryFlags { get }
```

## See Also

### Constants

- [kCGDisplayMovedFlag](movedflag.md) — The location of the upper-left corner of the display in the global display coordinate space has changed.
- [kCGDisplaySetMainFlag](setmainflag.md) — The display is now the main display.
- [kCGDisplaySetModeFlag](setmodeflag.md) — The display mode has changed.
- [kCGDisplayAddFlag](addflag.md) — The display has been added to the active display list.
- [kCGDisplayRemoveFlag](removeflag.md) — The display has been removed from the active display list.
- [kCGDisplayEnabledFlag](enabledflag.md) — The display has been enabled.
- [kCGDisplayDisabledFlag](disabledflag.md) — The display has been disabled.
- [kCGDisplayMirrorFlag](mirrorflag.md) — The display is now mirroring another display.
- [kCGDisplayUnMirrorFlag](unmirrorflag.md) — The display is no longer mirroring another display.
- [kCGDisplayDesktopShapeChangedFlag](desktopshapechangedflag.md)
