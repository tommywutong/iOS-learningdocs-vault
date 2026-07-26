---
title: CGEventFlags
framework: Core Graphics
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [Mac Catalyst, macOS]
languages: [swift, swift, swift, occ, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/coregraphics/cgeventflags
source_url: 'https://developer.apple.com/documentation/coregraphics/cgeventflags'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coregraphics/cgeventflags.json'
content_hash: 'sha256:5caf73fe345bab17'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Graphics](../coregraphics.md)

# CGEventFlags

<sub>Structure</sub>

Constants that indicate the modifier key state at the time an event is created, as well as other event-related states.

<sub>Mac Catalyst, macOS</sub>

```swift
struct CGEventFlags
```

## Overview

These constants specify masks for the bits in an event flags bit mask. Event flags indicate the modifier key state at the time an event is created, as well as other event-related states. Event flags are used in accessor functions such as [CGEventGetFlags](cgevent/flags.md), [CGEventSetFlags](cgeventsetflags.md), and [CGEventSourceFlagsState](<cgeventsource/flagsstate(__).md>).

## Relationships

- **Conforms To**: [BitwiseCopyable](../swift/bitwisecopyable.md), [Equatable](../swift/equatable.md), [ExpressibleByArrayLiteral](../swift/expressiblebyarrayliteral.md), [OptionSet](../swift/optionset.md), [RawRepresentable](../swift/rawrepresentable.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md), [SetAlgebra](../swift/setalgebra.md)

## Topics

### Constants

- [kCGEventFlagMaskAlphaShift](cgeventflags/maskalphashift.md) — Indicates that the Caps Lock key is down for a keyboard, mouse, or flag-changed event.
- [kCGEventFlagMaskShift](cgeventflags/maskshift.md) — Indicates that the Shift key is down for a keyboard, mouse, or flag-changed event.
- [kCGEventFlagMaskControl](cgeventflags/maskcontrol.md) — Indicates that the Control key is down for a keyboard, mouse, or flag-changed event.
- [kCGEventFlagMaskAlternate](cgeventflags/maskalternate.md) — Indicates that the Alt or Option key is down for a keyboard, mouse, or flag-changed event.
- [kCGEventFlagMaskCommand](cgeventflags/maskcommand.md) — Indicates that the Command key is down for a keyboard, mouse, or flag-changed event.
- [kCGEventFlagMaskHelp](cgeventflags/maskhelp.md) — Indicates that the Help modifier key is down for a keyboard, mouse, or flag-changed event. This key is not present on most keyboards, and is different than the Help key found in the same row as Home and Page Up.
- [kCGEventFlagMaskSecondaryFn](cgeventflags/masksecondaryfn.md) — Indicates that the Fn (Function) key is down for a keyboard, mouse, or flag-changed event. This key is found primarily on laptop keyboards.
- [kCGEventFlagMaskNumericPad](cgeventflags/masknumericpad.md) — Identifies key events from the numeric keypad area on extended keyboards.
- [kCGEventFlagMaskNonCoalesced](cgeventflags/masknoncoalesced.md) — Indicates that mouse and pen movement events are not being coalesced.

### Initializers

- [init(rawValue:)](<cgeventflags/init(rawvalue_).md>)

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
- [CGEventMouseSubtype](cgeventmousesubtype.md) — Constants used with the [kCGMouseEventSubtype](cgeventfield/mouseeventsubtype.md) event field.
- [CGEventSourceStateID](cgeventsourcestateid.md) — Constants that specify the possible source states of an event source.
- [CGEventSuppressionState](cgeventsuppressionstate.md) — Specify the event suppression states that can occur after posting an event.
- [CGEventTapLocation](cgeventtaplocation.md) — Constants that specify possible tapping points for events.
- [CGEventTapOptions](cgeventtapoptions.md) — Constants that specify whether a new event tap is an active filter or a passive listener.
