---
title: CGImageByteOrderInfo
framework: Core Graphics
symbol_kind: enum
role: symbol
role_heading: Enumeration
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.1+, macOS 10.0+, tvOS, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/coregraphics/cgimagebyteorderinfo
source_url: 'https://developer.apple.com/documentation/coregraphics/cgimagebyteorderinfo'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coregraphics/cgimagebyteorderinfo.json'
content_hash: 'sha256:7e49fb6a26a8c644'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Graphics](../coregraphics.md)

# CGImageByteOrderInfo

<sub>Enumeration</sub>

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
enum CGImageByteOrderInfo
```

## Relationships

- **Conforms To**: [BitwiseCopyable](../swift/bitwisecopyable.md), [CaseIterable](../swift/caseiterable.md), [Copyable](../swift/copyable.md), [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md), [Equatable](../swift/equatable.md), [Escapable](../swift/escapable.md), [Hashable](../swift/hashable.md), [RawRepresentable](../swift/rawrepresentable.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md)

## Topics

### Constants

- [kCGImageByteOrder16Big](cgimagebyteorderinfo/order16big.md)
- [kCGImageByteOrder16Little](cgimagebyteorderinfo/order16little.md)
- [kCGImageByteOrder32Big](cgimagebyteorderinfo/order32big.md)
- [kCGImageByteOrder32Little](cgimagebyteorderinfo/order32little.md)
- [kCGImageByteOrderMask](cgimagebyteorderinfo/ordermask.md) _(deprecated)_
- [kCGImageByteOrderDefault](cgimagebyteorderinfo/orderdefault.md)

### Initializers

- [init(rawValue:)](<cgimagebyteorderinfo/init(rawvalue_).md>)

### Type Properties

- [kCGImageByteOrder16Host](cgimagebyteorderinfo/order16host.md)
- [kCGImageByteOrder32Host](cgimagebyteorderinfo/order32host.md)

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
