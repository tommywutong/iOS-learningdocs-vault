---
title: CGScreenUpdateMoveDelta
framework: Core Graphics
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [Mac Catalyst, macOS]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/coregraphics/cgscreenupdatemovedelta
source_url: 'https://developer.apple.com/documentation/coregraphics/cgscreenupdatemovedelta'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coregraphics/cgscreenupdatemovedelta.json'
content_hash: 'sha256:3b0fabca77d74753'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Graphics](../coregraphics.md)

# CGScreenUpdateMoveDelta

<sub>Structure</sub>

The distance, in pixel units, that an onscreen region moves.

<sub>Mac Catalyst, macOS</sub>

```swift
struct CGScreenUpdateMoveDelta
```

## Overview

Move operation notifications are restricted to changes that move a region by an integer number of pixels. The fields `dX` and `dY` describe the direction of movement:

- Positive values of `dX` indicate movement to the right.
- Negative values of `dX` indicate movement to the left.
- Positive values of `dY` indicate movement downward.
- Negative values of `dY` indicate movement upward.

## Relationships

- **Conforms To**: [BitwiseCopyable](../swift/bitwisecopyable.md), [Sendable](../swift/sendable.md)

## Topics

### Initializers

- [init()](<cgscreenupdatemovedelta/init().md>)
- [init(dX:dY:)](<cgscreenupdatemovedelta/init(dx_dy_).md>)

### Instance Properties

- [dX](cgscreenupdatemovedelta/dx.md)
- [dY](cgscreenupdatemovedelta/dy.md)

## See Also

### Structures

- [CGPSConverter](cgpsconverter.md) — An opaque data type used to convert PostScript data to PDF data.
- [CGCaptureOptions](cgcaptureoptions.md) — Configuration parameters that are used when capturing displays.
- [CGConfigureOption](cgconfigureoption.md) — The scope of the changes in a display configuration transaction.
- [CGDeviceColor](cgdevicecolor.md)
- [CGDisplayChangeSummaryFlags](cgdisplaychangesummaryflags.md) — The configuration parameters that are passed to a display reconfiguration callback function.
- [CGEventFilterMask](cgeventfiltermask.md) — Specify masks for classes of low-level events that can be filtered during event suppression states.
- [CGEventFlags](cgeventflags.md) — Constants that indicate the modifier key state at the time an event is created, as well as other event-related states.
- [CGEventTapInformation](cgeventtapinformation.md) — Defines the structure used to report information about event taps.
- [CGScreenUpdateOperation](cgscreenupdateoperation.md) — Types of screen-update operations.
- [CGWindowImageOption](cgwindowimageoption.md) — The data type to use to specify the type of image to be generated for a window.
- [CGWindowListOption](cgwindowlistoption.md) — The data type used to specify the options for gathering a list of windows.
- [CGColorBufferFormat](cgcolorbufferformat.md)
- [CGColorDataFormat](cgcolordataformat.md)
- [CGPDFAccessPermissions](cgpdfaccesspermissions.md)
- [CGPSConverterCallbacks](cgpsconvertercallbacks.md) — A structure for holding the callbacks provided when you create a PostScript converter object.
