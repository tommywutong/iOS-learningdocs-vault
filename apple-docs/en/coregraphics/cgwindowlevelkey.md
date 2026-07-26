---
title: CGWindowLevelKey
framework: Core Graphics
symbol_kind: enum
role: symbol
role_heading: Enumeration
platforms: [Mac Catalyst, macOS]
languages: [swift, swift, swift, swift, occ, occ, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/coregraphics/cgwindowlevelkey
source_url: 'https://developer.apple.com/documentation/coregraphics/cgwindowlevelkey'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coregraphics/cgwindowlevelkey.json'
content_hash: 'sha256:4f53211c95509001'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Graphics](../coregraphics.md)

# CGWindowLevelKey

<sub>Enumeration</sub>

Keys that represent the standard window levels in macOS. Quartz includes these keys to support application frameworks like Cocoa. Applications do not need to use them directly.

<sub>Mac Catalyst, macOS</sub>

```swift
enum CGWindowLevelKey
```

## Relationships

- **Conforms To**: [BitwiseCopyable](../swift/bitwisecopyable.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [RawRepresentable](../swift/rawrepresentable.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md)

## Topics

### Constants

- [kCGBaseWindowLevelKey](cgwindowlevelkey/basewindow.md)
- [kCGMinimumWindowLevelKey](cgwindowlevelkey/minimumwindow.md)
- [kCGDesktopWindowLevelKey](cgwindowlevelkey/desktopwindow.md)
- [kCGBackstopMenuLevelKey](cgwindowlevelkey/backstopmenu.md)
- [kCGNormalWindowLevelKey](cgwindowlevelkey/normalwindow.md)
- [kCGFloatingWindowLevelKey](cgwindowlevelkey/floatingwindow.md)
- [kCGTornOffMenuWindowLevelKey](cgwindowlevelkey/tornoffmenuwindow.md)
- [kCGDockWindowLevelKey](cgwindowlevelkey/dockwindow.md)
- [kCGMainMenuWindowLevelKey](cgwindowlevelkey/mainmenuwindow.md)
- [kCGStatusWindowLevelKey](cgwindowlevelkey/statuswindow.md)
- [kCGModalPanelWindowLevelKey](cgwindowlevelkey/modalpanelwindow.md)
- [kCGPopUpMenuWindowLevelKey](cgwindowlevelkey/popupmenuwindow.md)
- [kCGDraggingWindowLevelKey](cgwindowlevelkey/draggingwindow.md)
- [kCGScreenSaverWindowLevelKey](cgwindowlevelkey/screensaverwindow.md)
- [kCGMaximumWindowLevelKey](cgwindowlevelkey/maximumwindow.md)
- [kCGOverlayWindowLevelKey](cgwindowlevelkey/overlaywindow.md)
- [kCGHelpWindowLevelKey](cgwindowlevelkey/helpwindow.md)
- [kCGUtilityWindowLevelKey](cgwindowlevelkey/utilitywindow.md)
- [kCGDesktopIconWindowLevelKey](cgwindowlevelkey/desktopiconwindow.md)
- [kCGCursorWindowLevelKey](cgwindowlevelkey/cursorwindow.md)
- [kCGAssistiveTechHighWindowLevelKey](cgwindowlevelkey/assistivetechhighwindow.md)
- [kCGNumberOfWindowLevelKeys](cgwindowlevelkey/numberofwindowlevelkeys.md)

### Initializers

- [init(rawValue:)](<cgwindowlevelkey/init(rawvalue_).md>)

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
