---
title: CGScreenUpdateOperation
framework: Core Graphics
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [Mac Catalyst, macOS]
languages: [swift, swift, swift, occ, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/coregraphics/cgscreenupdateoperation
source_url: 'https://developer.apple.com/documentation/coregraphics/cgscreenupdateoperation'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coregraphics/cgscreenupdateoperation.json'
content_hash: 'sha256:71049d46e0fe7f74'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Graphics](../coregraphics.md)

# CGScreenUpdateOperation

<sub>Structure</sub>

Types of screen-update operations.

<sub>Mac Catalyst, macOS</sub>

```swift
struct CGScreenUpdateOperation
```

## Overview

For information about how these constants are used, see the function [CGWaitForScreenUpdateRects](<cgwaitforscreenupdaterects(__________).md>).

## Relationships

- **Conforms To**: [BitwiseCopyable](../swift/bitwisecopyable.md), [Equatable](../swift/equatable.md), [ExpressibleByArrayLiteral](../swift/expressiblebyarrayliteral.md), [OptionSet](../swift/optionset.md), [RawRepresentable](../swift/rawrepresentable.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md), [SetAlgebra](../swift/setalgebra.md)

## Topics

### Constants

- [kCGScreenUpdateOperationRefresh](cgscreenupdateoperation/refresh.md) — A screen-refresh operation.
- [kCGScreenUpdateOperationMove](cgscreenupdateoperation/move.md) — A screen-move operation.
- [kCGScreenUpdateOperationReducedDirtyRectangleCount](cgscreenupdateoperation/reduceddirtyrectanglecount.md)

### Initializers

- [init(rawValue:)](<cgscreenupdateoperation/init(rawvalue_).md>)

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
- [CGEventMouseSubtype](cgeventmousesubtype.md) — Constants used with the [kCGMouseEventSubtype](cgeventfield/mouseeventsubtype.md) event field.
- [CGEventSourceStateID](cgeventsourcestateid.md) — Constants that specify the possible source states of an event source.
- [CGEventSuppressionState](cgeventsuppressionstate.md) — Specify the event suppression states that can occur after posting an event.
- [CGEventTapLocation](cgeventtaplocation.md) — Constants that specify possible tapping points for events.
