---
title: CGEventSuppressionState
framework: Core Graphics
symbol_kind: enum
role: symbol
role_heading: Enumeration
platforms: [Mac Catalyst, macOS]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/coregraphics/cgeventsuppressionstate
source_url: 'https://developer.apple.com/documentation/coregraphics/cgeventsuppressionstate'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coregraphics/cgeventsuppressionstate.json'
content_hash: 'sha256:482dbbdcfe00127c'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Graphics](../coregraphics.md)

# CGEventSuppressionState

<sub>Enumeration</sub>

Specify the event suppression states that can occur after posting an event.

<sub>Mac Catalyst, macOS</sub>

```swift
enum CGEventSuppressionState
```

## Overview

These constants specify the types of event suppression intervals during which an event filter is applied after posting an event.

## Relationships

- **Conforms To**: [BitwiseCopyable](../swift/bitwisecopyable.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [RawRepresentable](../swift/rawrepresentable.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md)

## Topics

### Constants

- [kCGEventSuppressionStateSuppressionInterval](cgeventsuppressionstate/eventsuppressionstatesuppressioninterval.md) — Specifies that certain local hardware events may be suppressed for a short interval after posting an event.
- [kCGEventSuppressionStateRemoteMouseDrag](cgeventsuppressionstate/eventsuppressionstateremotemousedrag.md) — Specifies that certain local hardware events may be suppressed during a mouse drag operation (mouse movement with the left or only mouse button down).
- [kCGNumberOfEventSuppressionStates](cgeventsuppressionstate/numberofeventsuppressionstates.md)

### Enumeration Cases

- [kCGNumberOfEventSuppressionStates](cgeventsuppressionstate/numberofeventsuppressionstates.md)

### Initializers

- [init(rawValue:)](<cgeventsuppressionstate/init(rawvalue_).md>)

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
- [CGEventTapLocation](cgeventtaplocation.md) — Constants that specify possible tapping points for events.
- [CGEventTapOptions](cgeventtapoptions.md) — Constants that specify whether a new event tap is an active filter or a passive listener.
