---
title: CGDisplayStreamUpdateRectType
framework: Core Graphics
symbol_kind: enum
role: symbol
role_heading: Enumeration
platforms: [Mac Catalyst, macOS]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/coregraphics/cgdisplaystreamupdaterecttype
source_url: 'https://developer.apple.com/documentation/coregraphics/cgdisplaystreamupdaterecttype'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coregraphics/cgdisplaystreamupdaterecttype.json'
content_hash: 'sha256:0fe739c3608d9420'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Graphics](../coregraphics.md)

# CGDisplayStreamUpdateRectType

<sub>Enumeration</sub>

Use these constants to determine which rectangles your app is interested in.

<sub>Mac Catalyst, macOS</sub>

```swift
enum CGDisplayStreamUpdateRectType
```

## Relationships

- **Conforms To**: [BitwiseCopyable](../swift/bitwisecopyable.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [RawRepresentable](../swift/rawrepresentable.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md)

## Topics

### Constants

- [kCGDisplayStreamUpdateRefreshedRects](cgdisplaystreamupdaterecttype/refreshedrects.md) — The rectangles for the portions of the display that were redrawn.
- [kCGDisplayStreamUpdateMovedRects](cgdisplaystreamupdaterecttype/movedrects.md) — The rectangles for the portions of the display that were simply moved from one part of the display to another.
- [kCGDisplayStreamUpdateDirtyRects](cgdisplaystreamupdaterecttype/dirtyrects.md) — The union of both rectangles that were redrawn and rectangles that were moved.
- [kCGDisplayStreamUpdateReducedDirtyRects](cgdisplaystreamupdaterecttype/reduceddirtyrects.md) — The union is calculated and then simplified. This reduces the number of rectangles returned to your app, but it may report some pixels that were not actually changed.

### Initializers

- [init(rawValue:)](<cgdisplaystreamupdaterecttype/init(rawvalue_).md>)

## See Also

### Enumerations

- [CGCaptureOptions](cgcaptureoptions.md) — Configuration parameters that are used when capturing displays.
- [CGColorConversionInfoTransformType](cgcolorconversioninfotransformtype.md) — Constants describing how a color conversion uses color spaces.
- [CGColorRenderingIntent](cgcolorrenderingintent.md) — Handling options for colors that are not located within the destination color space of a graphics context.
- [CGConfigureOption](cgconfigureoption.md) — The scope of the changes in a display configuration transaction.
- [CGDisplayChangeSummaryFlags](cgdisplaychangesummaryflags.md) — The configuration parameters that are passed to a display reconfiguration callback function.
- [CGDisplayStreamFrameStatus](cgdisplaystreamframestatus.md) — Describes a frame update event.
- [CGError](cgerror.md) — A uniform type for result codes returned by functions in Core Graphics.
- [CGEventField](cgeventfield.md) — Constants used as keys to access specialized fields in low-level events.
- [CGEventFilterMask](cgeventfiltermask.md) — Specify masks for classes of low-level events that can be filtered during event suppression states.
- [CGEventFlags](cgeventflags.md) — Constants that indicate the modifier key state at the time an event is created, as well as other event-related states.
- [CGEventMouseSubtype](cgeventmousesubtype.md) — Constants used with the [kCGMouseEventSubtype](cgeventfield/mouseeventsubtype.md) event field.
- [CGEventSourceStateID](cgeventsourcestateid.md) — Constants that specify the possible source states of an event source.
- [CGEventSuppressionState](cgeventsuppressionstate.md) — Specify the event suppression states that can occur after posting an event.
- [CGEventTapLocation](cgeventtaplocation.md) — Constants that specify possible tapping points for events.
- [CGEventTapOptions](cgeventtapoptions.md) — Constants that specify whether a new event tap is an active filter or a passive listener.
