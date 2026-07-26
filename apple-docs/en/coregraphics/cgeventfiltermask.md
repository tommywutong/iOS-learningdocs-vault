---
title: CGEventFilterMask
framework: Core Graphics
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [Mac Catalyst, macOS]
languages: [swift, swift, swift, occ, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/coregraphics/cgeventfiltermask
source_url: 'https://developer.apple.com/documentation/coregraphics/cgeventfiltermask'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coregraphics/cgeventfiltermask.json'
content_hash: 'sha256:68de0a177d5f2aee'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Graphics](../coregraphics.md)

# CGEventFilterMask

<sub>Structure</sub>

Specify masks for classes of low-level events that can be filtered during event suppression states.

<sub>Mac Catalyst, macOS</sub>

```swift
struct CGEventFilterMask
```

## Relationships

- **Conforms To**: [BitwiseCopyable](../swift/bitwisecopyable.md), [Equatable](../swift/equatable.md), [ExpressibleByArrayLiteral](../swift/expressiblebyarrayliteral.md), [OptionSet](../swift/optionset.md), [RawRepresentable](../swift/rawrepresentable.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md), [SetAlgebra](../swift/setalgebra.md)

## Topics

### Initializers

- [init(rawValue:)](<cgeventfiltermask/init(rawvalue_).md>)

### Type Properties

- [kCGEventFilterMaskPermitLocalKeyboardEvents](cgeventfiltermask/permitlocalkeyboardevents.md)
- [kCGEventFilterMaskPermitLocalMouseEvents](cgeventfiltermask/permitlocalmouseevents.md)
- [kCGEventFilterMaskPermitSystemDefinedEvents](cgeventfiltermask/permitsystemdefinedevents.md)

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
- [CGEventFlags](cgeventflags.md) — Constants that indicate the modifier key state at the time an event is created, as well as other event-related states.
- [CGEventMouseSubtype](cgeventmousesubtype.md) — Constants used with the [kCGMouseEventSubtype](cgeventfield/mouseeventsubtype.md) event field.
- [CGEventSourceStateID](cgeventsourcestateid.md) — Constants that specify the possible source states of an event source.
- [CGEventSuppressionState](cgeventsuppressionstate.md) — Specify the event suppression states that can occur after posting an event.
- [CGEventTapLocation](cgeventtaplocation.md) — Constants that specify possible tapping points for events.
- [CGEventTapOptions](cgeventtapoptions.md) — Constants that specify whether a new event tap is an active filter or a passive listener.
