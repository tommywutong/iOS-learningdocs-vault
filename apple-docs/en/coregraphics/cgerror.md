---
title: CGError
framework: Core Graphics
symbol_kind: enum
role: symbol
role_heading: Enumeration
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/coregraphics/cgerror
source_url: 'https://developer.apple.com/documentation/coregraphics/cgerror'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coregraphics/cgerror.json'
content_hash: 'sha256:f2b9a20c09fc04b0'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Graphics](../coregraphics.md)

# CGError

<sub>Enumeration</sub>

A uniform type for result codes returned by functions in Core Graphics.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
enum CGError
```

## Relationships

- **Conforms To**: [BitwiseCopyable](../swift/bitwisecopyable.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [RawRepresentable](../swift/rawrepresentable.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md)

## Topics

### Constants

- [kCGErrorCannotComplete](cgerror/cannotcomplete.md) — The requested operation is inappropriate for the parameters passed in, or the current system state.
- [kCGErrorFailure](cgerror/failure.md) — A general failure occurred.
- [kCGErrorIllegalArgument](cgerror/illegalargument.md) — One or more of the parameters passed to a function are invalid. Check for `NULL` pointers.
- [kCGErrorInvalidConnection](cgerror/invalidconnection.md) — The parameter representing a connection to the window server is invalid.
- [kCGErrorInvalidContext](cgerror/invalidcontext.md) — The `CPSProcessSerNum` or context identifier parameter is not valid.
- [kCGErrorInvalidOperation](cgerror/invalidoperation.md) — The requested operation is not valid for the parameters passed in, or the current system state.
- [kCGErrorNoneAvailable](cgerror/noneavailable.md) — The requested operation could not be completed as the indicated resources were not found.
- [kCGErrorNotImplemented](cgerror/notimplemented.md) — Return value from obsolete function stubs present for binary compatibility, but not typically called.
- [kCGErrorRangeCheck](cgerror/rangecheck.md) — A parameter passed in has a value that is inappropriate, or which does not map to a useful operation or value.
- [kCGErrorSuccess](cgerror/success.md) — The requested operation was completed successfully.
- [kCGErrorTypeCheck](cgerror/typecheck.md) — A data type or token was encountered that did not match the expected type or token.

### Initializers

- [init(rawValue:)](<cgerror/init(rawvalue_).md>)

## See Also

### Related Documentation

- [Quartz 2D Programming Guide](https://developer.apple.com/library/archive/documentation/GraphicsImaging/Conceptual/drawingwithquartz2d/Introduction/Introduction.html#//apple_ref/doc/uid/TP30001066)

### Enumerations

- [CGCaptureOptions](cgcaptureoptions.md) — Configuration parameters that are used when capturing displays.
- [CGColorConversionInfoTransformType](cgcolorconversioninfotransformtype.md) — Constants describing how a color conversion uses color spaces.
- [CGColorRenderingIntent](cgcolorrenderingintent.md) — Handling options for colors that are not located within the destination color space of a graphics context.
- [CGConfigureOption](cgconfigureoption.md) — The scope of the changes in a display configuration transaction.
- [CGDisplayChangeSummaryFlags](cgdisplaychangesummaryflags.md) — The configuration parameters that are passed to a display reconfiguration callback function.
- [CGDisplayStreamFrameStatus](cgdisplaystreamframestatus.md) — Describes a frame update event.
- [CGDisplayStreamUpdateRectType](cgdisplaystreamupdaterecttype.md) — Use these constants to determine which rectangles your app is interested in.
- [CGEventField](cgeventfield.md) — Constants used as keys to access specialized fields in low-level events.
- [CGEventFilterMask](cgeventfiltermask.md) — Specify masks for classes of low-level events that can be filtered during event suppression states.
- [CGEventFlags](cgeventflags.md) — Constants that indicate the modifier key state at the time an event is created, as well as other event-related states.
- [CGEventMouseSubtype](cgeventmousesubtype.md) — Constants used with the [kCGMouseEventSubtype](cgeventfield/mouseeventsubtype.md) event field.
- [CGEventSourceStateID](cgeventsourcestateid.md) — Constants that specify the possible source states of an event source.
- [CGEventSuppressionState](cgeventsuppressionstate.md) — Specify the event suppression states that can occur after posting an event.
- [CGEventTapLocation](cgeventtaplocation.md) — Constants that specify possible tapping points for events.
- [CGEventTapOptions](cgeventtapoptions.md) — Constants that specify whether a new event tap is an active filter or a passive listener.
