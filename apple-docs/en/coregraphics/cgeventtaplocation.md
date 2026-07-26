---
title: CGEventTapLocation
framework: Core Graphics
symbol_kind: enum
role: symbol
role_heading: Enumeration
platforms: [Mac Catalyst, macOS]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/coregraphics/cgeventtaplocation
source_url: 'https://developer.apple.com/documentation/coregraphics/cgeventtaplocation'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coregraphics/cgeventtaplocation.json'
content_hash: 'sha256:1651b2c824121776'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Graphics](../coregraphics.md)

# CGEventTapLocation

<sub>Enumeration</sub>

Constants that specify possible tapping points for events.

<sub>Mac Catalyst, macOS</sub>

```swift
enum CGEventTapLocation
```

## Overview

In addition to the three tapping points described above, an event tap may also be placed where annotated events are delivered to a specific application. For more information, see the function [CGEventTapCreateForPSN](<cgevent/tapcreateforpsn(processserialnumber_place_options_eventsofinterest_callback_userinfo_).md>).

## Relationships

- **Conforms To**: [BitwiseCopyable](../swift/bitwisecopyable.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [RawRepresentable](../swift/rawrepresentable.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md)

## Topics

### Constants

- [kCGHIDEventTap](cgeventtaplocation/cghideventtap.md) — Specifies that an event tap is placed at the point where HID system events enter the window server.
- [kCGSessionEventTap](cgeventtaplocation/cgsessioneventtap.md) — Specifies that an event tap is placed at the point where HID system and remote control events enter a login session.
- [kCGAnnotatedSessionEventTap](cgeventtaplocation/cgannotatedsessioneventtap.md) — Specifies that an event tap is placed at the point where session events have been annotated to flow to an application.

### Initializers

- [init(rawValue:)](<cgeventtaplocation/init(rawvalue_).md>)

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
- [CGEventTapOptions](cgeventtapoptions.md) — Constants that specify whether a new event tap is an active filter or a passive listener.
