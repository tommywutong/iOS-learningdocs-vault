---
title: CGDisplayChangeSummaryFlags
framework: Core Graphics
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [Mac Catalyst, macOS]
languages: [swift, swift, swift, occ, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/coregraphics/cgdisplaychangesummaryflags
source_url: 'https://developer.apple.com/documentation/coregraphics/cgdisplaychangesummaryflags'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coregraphics/cgdisplaychangesummaryflags.json'
content_hash: 'sha256:4106e61dd0b98dba'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Graphics](../coregraphics.md)

# CGDisplayChangeSummaryFlags

<sub>Structure</sub>

The configuration parameters that are passed to a display reconfiguration callback function.

<sub>Mac Catalyst, macOS</sub>

```swift
struct CGDisplayChangeSummaryFlags
```

## Overview

For information about how these constants are used, see the callback [CGDisplayReconfigurationCallBack](cgdisplayreconfigurationcallback.md).

## Relationships

- **Conforms To**: [BitwiseCopyable](../swift/bitwisecopyable.md), [Equatable](../swift/equatable.md), [ExpressibleByArrayLiteral](../swift/expressiblebyarrayliteral.md), [OptionSet](../swift/optionset.md), [RawRepresentable](../swift/rawrepresentable.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md), [SetAlgebra](../swift/setalgebra.md)

## Topics

### Constants

- [kCGDisplayBeginConfigurationFlag](cgdisplaychangesummaryflags/beginconfigurationflag.md) — The display configuration is about to change.
- [kCGDisplayMovedFlag](cgdisplaychangesummaryflags/movedflag.md) — The location of the upper-left corner of the display in the global display coordinate space has changed.
- [kCGDisplaySetMainFlag](cgdisplaychangesummaryflags/setmainflag.md) — The display is now the main display.
- [kCGDisplaySetModeFlag](cgdisplaychangesummaryflags/setmodeflag.md) — The display mode has changed.
- [kCGDisplayAddFlag](cgdisplaychangesummaryflags/addflag.md) — The display has been added to the active display list.
- [kCGDisplayRemoveFlag](cgdisplaychangesummaryflags/removeflag.md) — The display has been removed from the active display list.
- [kCGDisplayEnabledFlag](cgdisplaychangesummaryflags/enabledflag.md) — The display has been enabled.
- [kCGDisplayDisabledFlag](cgdisplaychangesummaryflags/disabledflag.md) — The display has been disabled.
- [kCGDisplayMirrorFlag](cgdisplaychangesummaryflags/mirrorflag.md) — The display is now mirroring another display.
- [kCGDisplayUnMirrorFlag](cgdisplaychangesummaryflags/unmirrorflag.md) — The display is no longer mirroring another display.
- [kCGDisplayDesktopShapeChangedFlag](cgdisplaychangesummaryflags/desktopshapechangedflag.md)

### Initializers

- [init(rawValue:)](<cgdisplaychangesummaryflags/init(rawvalue_).md>)

## See Also

### Enumerations

- [CGCaptureOptions](cgcaptureoptions.md) — Configuration parameters that are used when capturing displays.
- [CGColorConversionInfoTransformType](cgcolorconversioninfotransformtype.md) — Constants describing how a color conversion uses color spaces.
- [CGColorRenderingIntent](cgcolorrenderingintent.md) — Handling options for colors that are not located within the destination color space of a graphics context.
- [CGConfigureOption](cgconfigureoption.md) — The scope of the changes in a display configuration transaction.
- [CGDisplayStreamFrameStatus](cgdisplaystreamframestatus.md) — Describes a frame update event.
- [CGDisplayStreamUpdateRectType](cgdisplaystreamupdaterecttype.md) — Use these constants to determine which rectangles your app is interested in.
- [CGError](cgerror.md) — A uniform type for result codes returned by functions in Core Graphics.
- [CGEventField](cgeventfield.md) — Constants used as keys to access specialized fields in low-level events.
- [CGEventFilterMask](cgeventfiltermask.md) — Specify masks for classes of low-level events that can be filtered during event suppression states.
- [CGEventFlags](cgeventflags.md) — Constants that indicate the modifier key state at the time an event is created, as well as other event-related states.
- [CGEventMouseSubtype](cgeventmousesubtype.md) — Constants used with the [kCGMouseEventSubtype](cgeventfield/mouseeventsubtype.md) event field.
- [CGEventSourceStateID](cgeventsourcestateid.md) — Constants that specify the possible source states of an event source.
- [CGEventSuppressionState](cgeventsuppressionstate.md) — Specify the event suppression states that can occur after posting an event.
- [CGEventTapLocation](cgeventtaplocation.md) — Constants that specify possible tapping points for events.
- [CGEventTapOptions](cgeventtapoptions.md) — Constants that specify whether a new event tap is an active filter or a passive listener.
