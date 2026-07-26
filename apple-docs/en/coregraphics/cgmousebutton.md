---
title: CGMouseButton
framework: Core Graphics
symbol_kind: enum
role: symbol
role_heading: Enumeration
platforms: [Mac Catalyst, macOS]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/coregraphics/cgmousebutton
source_url: 'https://developer.apple.com/documentation/coregraphics/cgmousebutton'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coregraphics/cgmousebutton.json'
content_hash: 'sha256:e56c30f149ca955e'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Graphics](../coregraphics.md)

# CGMouseButton

<sub>Enumeration</sub>

Constants that specify buttons on a one, two, or three-button mouse.

<sub>Mac Catalyst, macOS</sub>

```swift
enum CGMouseButton
```

## Overview

Quartz supports up to 32 mouse buttons. The first three buttons are specified using these three constants. Additional buttons are specified in USB order using the integers 3 to 31.

These constants are used:

- In the function [CGEventCreateMouseEvent](<cgevent/init(mouseeventsource_mousetype_mousecursorposition_mousebutton_).md>) to specify the button that’s changing state.
- In the function [CGEventSourceButtonState](<cgeventsource/buttonstate(__button_).md>) to specify the button that’s being tested.
- To specify the value of the `kCGMouseEventButtonNumber` event field when modifying an event.

## Relationships

- **Conforms To**: [BitwiseCopyable](../swift/bitwisecopyable.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [RawRepresentable](../swift/rawrepresentable.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md)

## Topics

### Constants

- [kCGMouseButtonLeft](cgmousebutton/left.md)
- [kCGMouseButtonRight](cgmousebutton/right.md)
- [kCGMouseButtonCenter](cgmousebutton/center.md)

### Initializers

- [init(rawValue:)](<cgmousebutton/init(rawvalue_).md>)

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
