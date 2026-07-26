---
title: CGWindowImageOption
framework: Core Graphics
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [Mac Catalyst, macOS]
languages: [swift, swift, swift, occ, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/coregraphics/cgwindowimageoption
source_url: 'https://developer.apple.com/documentation/coregraphics/cgwindowimageoption'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coregraphics/cgwindowimageoption.json'
content_hash: 'sha256:0431b5b6e03c8ee1'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Graphics](../coregraphics.md)

# CGWindowImageOption

<sub>Structure</sub>

The data type to use to specify the type of image to be generated for a window.

<sub>Mac Catalyst, macOS</sub>

```swift
struct CGWindowImageOption
```

## Overview

This type is used in conjunction with the constants described in [Window Image Types](window-image-types.md).

## Relationships

- **Conforms To**: [BitwiseCopyable](../swift/bitwisecopyable.md), [Equatable](../swift/equatable.md), [ExpressibleByArrayLiteral](../swift/expressiblebyarrayliteral.md), [OptionSet](../swift/optionset.md), [RawRepresentable](../swift/rawrepresentable.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md), [SetAlgebra](../swift/setalgebra.md)

## Topics

### Initializers

- [init(rawValue:)](<cgwindowimageoption/init(rawvalue_).md>)

### Type Properties

- [kCGWindowImageBestResolution](cgwindowimageoption/bestresolution.md) — When capturing the window, return the best image resolution. The returned image size may be different than the screen size.
- [kCGWindowImageBoundsIgnoreFraming](cgwindowimageoption/boundsignoreframing.md)
- [kCGWindowImageNominalResolution](cgwindowimageoption/nominalresolution.md) — When capturing the window, return the nominal image resolution. The returned image size is the same as the screen size.
- [kCGWindowImageOnlyShadows](cgwindowimageoption/onlyshadows.md)
- [kCGWindowImageShouldBeOpaque](cgwindowimageoption/shouldbeopaque.md)

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
