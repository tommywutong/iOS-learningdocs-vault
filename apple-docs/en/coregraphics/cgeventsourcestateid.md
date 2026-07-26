---
title: CGEventSourceStateID
framework: Core Graphics
symbol_kind: enum
role: symbol
role_heading: Enumeration
platforms: [Mac Catalyst, macOS]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/coregraphics/cgeventsourcestateid
source_url: 'https://developer.apple.com/documentation/coregraphics/cgeventsourcestateid'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coregraphics/cgeventsourcestateid.json'
content_hash: 'sha256:a45b9c6f4651a9f2'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Graphics](../coregraphics.md)

# CGEventSourceStateID

<sub>Enumeration</sub>

Constants that specify the possible source states of an event source.

<sub>Mac Catalyst, macOS</sub>

```swift
enum CGEventSourceStateID
```

## Overview

A source state refers to a global event state table. These tables contain accumulated information on modifier flag state, keyboard key state, mouse button state, and related internal parameters placed in effect by posting events with associated sources.

Two pre-existing event state tables are defined:

- The `kCGEventSourceStateCombinedSessionState` table reflects the combined state of all event sources posting to the current user login session. If your program is posting events from within a login session, you should use this source state when you create an event source.
- The `kCGEventSourceStateHIDSystemState` table reflects the combined state of all hardware event sources posting from the HID system. If your program is a daemon or a user space device driver interpreting hardware state and generating events, you should use this source state when you create an event source.

Specialized applications such as remote control programs may want to generate and track event source state independent of other processes. These programs should use the `kCGEventSourceStatePrivate` value in creating their event source. An independent state table and unique source state ID (`CGEventSourceStateID`) are created to track the event source’s state. This independent state table is owned by the creating event source and released with it.

## Relationships

- **Conforms To**: [BitwiseCopyable](../swift/bitwisecopyable.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [RawRepresentable](../swift/rawrepresentable.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md)

## Topics

### Constants

- [kCGEventSourceStatePrivate](cgeventsourcestateid/privatestate.md) — Specifies that an event source should use a private event state table.
- [kCGEventSourceStateCombinedSessionState](cgeventsourcestateid/combinedsessionstate.md) — Specifies that an event source should use the event state table that reflects the combined state of all event sources posting to the current user login session.
- [kCGEventSourceStateHIDSystemState](cgeventsourcestateid/hidsystemstate.md) — Specifies that an event source should use the event state table that reflects the combined state of all hardware event sources posting from the HID system.

### Initializers

- [init(rawValue:)](<cgeventsourcestateid/init(rawvalue_).md>)

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
- [CGEventSuppressionState](cgeventsuppressionstate.md) — Specify the event suppression states that can occur after posting an event.
- [CGEventTapLocation](cgeventtaplocation.md) — Constants that specify possible tapping points for events.
- [CGEventTapOptions](cgeventtapoptions.md) — Constants that specify whether a new event tap is an active filter or a passive listener.
