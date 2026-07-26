---
title: CGEventMouseSubtype
framework: Core Graphics
symbol_kind: enum
role: symbol
role_heading: Enumeration
platforms: [Mac Catalyst, macOS]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/coregraphics/cgeventmousesubtype
source_url: 'https://developer.apple.com/documentation/coregraphics/cgeventmousesubtype'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coregraphics/cgeventmousesubtype.json'
content_hash: 'sha256:533e4ab0a28e78d8'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Graphics](../coregraphics.md)

# CGEventMouseSubtype

<sub>Enumeration</sub>

Constants used with the [kCGMouseEventSubtype](cgeventfield/mouseeventsubtype.md) event field.

<sub>Mac Catalyst, macOS</sub>

```swift
enum CGEventMouseSubtype
```

## Overview

Tablets may generate specially annotated mouse events that contain values associated with the [kCGMouseEventSubtype](cgeventfield/mouseeventsubtype.md) event field. To learn how to set these values, see the function [CGEventSetIntegerValueField](<cgevent/setintegervaluefield(__value_).md>).

## Relationships

- **Conforms To**: [BitwiseCopyable](../swift/bitwisecopyable.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [RawRepresentable](../swift/rawrepresentable.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md)

## Topics

### Constants

- [kCGEventMouseSubtypeDefault](cgeventmousesubtype/defaulttype.md) — Specifies that the event is an ordinary mouse event, and does not contain additional tablet device information.
- [kCGEventMouseSubtypeTabletPoint](cgeventmousesubtype/tabletpoint.md) — Specifies that the mouse event originated from a tablet device, and that the various `kCGTabletEvent` field selectors may be used to obtain tablet-specific data from the mouse event.
- [kCGEventMouseSubtypeTabletProximity](cgeventmousesubtype/tabletproximity.md)

### Initializers

- [init(rawValue:)](<cgeventmousesubtype/init(rawvalue_).md>)

## See Also

### Enumerations

- [CGCaptureOptions](cgcaptureoptions.md) — Configuration parameters that are used when capturing displays.
- [CGColorConversionInfoTransformType](cgcolorconversioninfotransformtype.md) — Constants describing how a color conversion uses color spaces.
- [CGColorRenderingIntent](cgcolorrenderingintent.md) — Handling options for colors that are not located within the destination color space of a graphics context.
- [CGConfigureOption](cgconfigureoption.md) — The scope of the changes in a display configuration transaction.
- [CGDisplayChangeSummaryFlags](cgdisplaychangesummaryflags.md) — The configuration parameters that are passed to a display reconfiguration callback function.
- [CGDisplayStreamFrameStatus](cgdisplaystreamframestatus.md) — Describes a frame update event.
- [CGDisplayStreamUpdateRectType](cgdisplaystreamupdaterecttype.md) — Use these constants to determine which rectangles your app is interested in.
- [CGError](cgerror.md) — A uniform type for result codes returned by functions in Core Graphics.
- [CGEventField](cgeventfield.md) — Constants used as keys to access specialized fields in low-level events.
- [CGEventFilterMask](cgeventfiltermask.md) — Specify masks for classes of low-level events that can be filtered during event suppression states.
- [CGEventFlags](cgeventflags.md) — Constants that indicate the modifier key state at the time an event is created, as well as other event-related states.
- [CGEventSourceStateID](cgeventsourcestateid.md) — Constants that specify the possible source states of an event source.
- [CGEventSuppressionState](cgeventsuppressionstate.md) — Specify the event suppression states that can occur after posting an event.
- [CGEventTapLocation](cgeventtaplocation.md) — Constants that specify possible tapping points for events.
- [CGEventTapOptions](cgeventtapoptions.md) — Constants that specify whether a new event tap is an active filter or a passive listener.
