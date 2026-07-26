---
title: CGEventField
framework: Core Graphics
symbol_kind: enum
role: symbol
role_heading: Enumeration
platforms: [Mac Catalyst, macOS]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/coregraphics/cgeventfield
source_url: 'https://developer.apple.com/documentation/coregraphics/cgeventfield'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coregraphics/cgeventfield.json'
content_hash: 'sha256:74594863483c87a0'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Graphics](../coregraphics.md)

# CGEventField

<sub>Enumeration</sub>

Constants used as keys to access specialized fields in low-level events.

<sub>Mac Catalyst, macOS</sub>

```swift
enum CGEventField
```

## Overview

These constants are used as keys to access certain specialized event fields when using low-level accessor functions such as [CGEventGetIntegerValueField](<cgevent/getintegervaluefield(__).md>), [CGEventSetIntegerValueField](<cgevent/setintegervaluefield(__value_).md>), [CGEventGetDoubleValueField](<cgevent/getdoublevaluefield(__).md>), and [CGEventSetDoubleValueField](<cgevent/setdoublevaluefield(__value_).md>).

## Relationships

- **Conforms To**: [BitwiseCopyable](../swift/bitwisecopyable.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [RawRepresentable](../swift/rawrepresentable.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md)

## Topics

### Constants

- [kCGMouseEventNumber](cgeventfield/mouseeventnumber.md) — Key to access an integer field that contains the mouse button event number. Matching mouse-down and mouse-up events will have the same event number.
- [kCGMouseEventClickState](cgeventfield/mouseeventclickstate.md) — Key to access an integer field that contains the mouse button click state. A click state of 1 represents a single click. A click state of 2 represents a double-click. A click state of 3 represents a triple-click.
- [kCGMouseEventPressure](cgeventfield/mouseeventpressure.md) — Key to access a double field that contains the mouse button pressure. The pressure value may range from 0 to 1, with 0 representing the mouse being up. This value is commonly set by tablet pens mimicking a mouse.
- [kCGMouseEventButtonNumber](cgeventfield/mouseeventbuttonnumber.md) — Key to access an integer field that contains the mouse button number. For information about the possible values, see [CGMouseButton](cgmousebutton.md).
- [kCGMouseEventDeltaX](cgeventfield/mouseeventdeltax.md) — Key to access an integer field that contains the horizontal mouse delta since the last mouse movement event.
- [kCGMouseEventDeltaY](cgeventfield/mouseeventdeltay.md) — Key to access an integer field that contains the vertical mouse delta since the last mouse movement event.
- [kCGMouseEventInstantMouser](cgeventfield/mouseeventinstantmouser.md) — Key to access an integer field. The value is non-zero if the event should be ignored by the Inkwell subsystem.
- [kCGMouseEventSubtype](cgeventfield/mouseeventsubtype.md) — Key to access an integer field that encodes the mouse event subtype as a `kCFNumberIntType`.
- [kCGKeyboardEventAutorepeat](cgeventfield/keyboardeventautorepeat.md) — Key to access an integer field, non-zero when this is an autorepeat of a key-down, and zero otherwise.
- [kCGKeyboardEventKeycode](cgeventfield/keyboardeventkeycode.md) — Key to access an integer field that contains the virtual keycode of the key-down or key-up event.
- [kCGKeyboardEventKeyboardType](cgeventfield/keyboardeventkeyboardtype.md) — Key to access an integer field that contains the keyboard type identifier.
- [kCGScrollWheelEventDeltaAxis1](cgeventfield/scrollwheeleventdeltaaxis1.md) — Key to access an integer field that contains scrolling data. This field typically contains the change in vertical position since the last scrolling event from a Mighty Mouse scroller or a single-wheel mouse scroller.
- [kCGScrollWheelEventDeltaAxis2](cgeventfield/scrollwheeleventdeltaaxis2.md) — Key to access an integer field that contains scrolling data. This field typically contains the change in horizontal position since the last scrolling event from a Mighty Mouse scroller.
- [kCGScrollWheelEventDeltaAxis3](cgeventfield/scrollwheeleventdeltaaxis3.md) — This field is not used.
- [kCGScrollWheelEventFixedPtDeltaAxis1](cgeventfield/scrollwheeleventfixedptdeltaaxis1.md) — Key to access a field that contains scrolling data. The scrolling data represents a line-based or pixel-based change in vertical position since the last scrolling event from a Mighty Mouse scroller or a single-wheel mouse scroller. The scrolling data uses a fixed-point 16.16 signed integer format. For example, if the field contains a value of 1.0, the integer 0x00010000 is returned by `CGEventGetIntegerValueField`. If this key is passed to `CGEventGetDoubleValueField`, the fixed-point value is converted to a double value.
- [kCGScrollWheelEventFixedPtDeltaAxis2](cgeventfield/scrollwheeleventfixedptdeltaaxis2.md) — Key to access a field that contains scrolling data. The scrolling data represents a line-based or pixel-based change in horizontal position since the last scrolling event from a Mighty Mouse scroller. The scrolling data uses a fixed-point 16.16 signed integer format. For example, if the field contains a value of 1.0, the integer 0x00010000 is returned by `CGEventGetIntegerValueField`. If this key is passed to `CGEventGetDoubleValueField`, the fixed-point value is converted to a double value.
- [kCGScrollWheelEventFixedPtDeltaAxis3](cgeventfield/scrollwheeleventfixedptdeltaaxis3.md) — This field is not used.
- [kCGScrollWheelEventPointDeltaAxis1](cgeventfield/scrollwheeleventpointdeltaaxis1.md) — Key to access an integer field that contains pixel-based scrolling data. The scrolling data represents the change in vertical position since the last scrolling event from a Mighty Mouse scroller or a single-wheel mouse scroller.
- [kCGScrollWheelEventPointDeltaAxis2](cgeventfield/scrollwheeleventpointdeltaaxis2.md) — Key to access an integer field that contains pixel-based scrolling data. The scrolling data represents the change in horizontal position since the last scrolling event from a Mighty Mouse scroller.
- [kCGScrollWheelEventPointDeltaAxis3](cgeventfield/scrollwheeleventpointdeltaaxis3.md) — This field is not used.
- [kCGScrollWheelEventInstantMouser](cgeventfield/scrollwheeleventinstantmouser.md) — Key to access an integer field that indicates whether the event should be ignored by the Inkwell subsystem. If the value is non-zero, the event should be ignored.
- [kCGTabletEventPointX](cgeventfield/tableteventpointx.md) — Key to access an integer field that contains the absolute X coordinate in tablet space at full tablet resolution.
- [kCGTabletEventPointY](cgeventfield/tableteventpointy.md) — Key to access an integer field that contains the absolute Y coordinate in tablet space at full tablet resolution.
- [kCGTabletEventPointZ](cgeventfield/tableteventpointz.md) — Key to access an integer field that contains the absolute Z coordinate in tablet space at full tablet resolution.
- [kCGTabletEventPointButtons](cgeventfield/tableteventpointbuttons.md) — Key to access an integer field that contains the tablet button state. Bit 0 is the first button, and a set bit represents a closed or pressed button. Up to 16 buttons are supported.
- [kCGTabletEventPointPressure](cgeventfield/tableteventpointpressure.md) — Key to access a double field that contains the tablet pen pressure. A value of 0.0 represents no pressure, and 1.0 represents maximum pressure.
- [kCGTabletEventTiltX](cgeventfield/tableteventtiltx.md) — Key to access a double field that contains the horizontal tablet pen tilt. A value of 0.0 represents no tilt, and 1.0 represents maximum tilt.
- [kCGTabletEventTiltY](cgeventfield/tableteventtilty.md) — Key to access a double field that contains the vertical tablet pen tilt. A value of 0.0 represents no tilt, and 1.0 represents maximum tilt.
- [kCGTabletEventRotation](cgeventfield/tableteventrotation.md) — Key to access a double field that contains the tablet pen rotation.
- [kCGTabletEventTangentialPressure](cgeventfield/tableteventtangentialpressure.md) — Key to access a double field that contains the tangential pressure on the device. A value of 0.0 represents no pressure, and 1.0 represents maximum pressure.
- [kCGTabletEventDeviceID](cgeventfield/tableteventdeviceid.md) — Key to access an integer field that contains the system-assigned unique device ID.
- [kCGTabletEventVendor1](cgeventfield/tableteventvendor1.md) — Key to access an integer field that contains a vendor-specified value.
- [kCGTabletEventVendor2](cgeventfield/tableteventvendor2.md) — Key to access an integer field that contains a vendor-specified value.
- [kCGTabletEventVendor3](cgeventfield/tableteventvendor3.md) — Key to access an integer field that contains a vendor-specified value.
- [kCGTabletProximityEventVendorID](cgeventfield/tabletproximityeventvendorid.md) — Key to access an integer field that contains the vendor-defined ID, typically the USB vendor ID.
- [kCGTabletProximityEventTabletID](cgeventfield/tabletproximityeventtabletid.md) — Key to access an integer field that contains the vendor-defined tablet ID, typically the USB product ID.
- [kCGTabletProximityEventPointerID](cgeventfield/tabletproximityeventpointerid.md) — Key to access an integer field that contains the vendor-defined ID of the pointing device.
- [kCGTabletProximityEventDeviceID](cgeventfield/tabletproximityeventdeviceid.md) — Key to access an integer field that contains the system-assigned device ID.
- [kCGTabletProximityEventSystemTabletID](cgeventfield/tabletproximityeventsystemtabletid.md) — Key to access an integer field that contains the system-assigned unique tablet ID.
- [kCGTabletProximityEventVendorPointerType](cgeventfield/tabletproximityeventvendorpointertype.md) — Key to access an integer field that contains the vendor-assigned pointer type.
- [kCGTabletProximityEventVendorPointerSerialNumber](cgeventfield/tabletproximityeventvendorpointerserialnumber.md) — Key to access an integer field that contains the vendor-defined pointer serial number.
- [kCGTabletProximityEventVendorUniqueID](cgeventfield/tabletproximityeventvendoruniqueid.md) — Key to access an integer field that contains the vendor-defined unique ID.
- [kCGTabletProximityEventCapabilityMask](cgeventfield/tabletproximityeventcapabilitymask.md) — Key to access an integer field that contains the device capabilities mask.
- [kCGTabletProximityEventPointerType](cgeventfield/tabletproximityeventpointertype.md) — Key to access an integer field that contains the pointer type.
- [kCGTabletProximityEventEnterProximity](cgeventfield/tabletproximityevententerproximity.md) — Key to access an integer field that indicates whether the pen is in proximity to the tablet. The value is non-zero if the pen is in proximity to the tablet and zero when leaving the tablet.
- [kCGEventTargetProcessSerialNumber](cgeventfield/eventtargetprocessserialnumber.md) — Key to access a field that contains the event target process serial number. The value is a 64-bit long word.
- [kCGEventTargetUnixProcessID](cgeventfield/eventtargetunixprocessid.md) — Key to access a field that contains the event target Unix process ID.
- [kCGEventSourceUnixProcessID](cgeventfield/eventsourceunixprocessid.md) — Key to access a field that contains the event source Unix process ID.
- [kCGEventSourceUserData](cgeventfield/eventsourceuserdata.md) — Key to access a field that contains the event source user-supplied data, up to 64 bits.
- [kCGEventSourceUserID](cgeventfield/eventsourceuserid.md) — Key to access a field that contains the event source Unix effective UID.
- [kCGEventSourceGroupID](cgeventfield/eventsourcegroupid.md) — Key to access a field that contains the event source Unix effective GID.
- [kCGEventSourceStateID](cgeventfield/eventsourcestateid.md) — Key to access a field that contains the event source state ID used to create this event.
- [kCGScrollWheelEventIsContinuous](cgeventfield/scrollwheeleventiscontinuous.md) — Key to access an integer field that indicates whether a scrolling event contains continuous, pixel-based scrolling data. The value is non-zero when the scrolling data is pixel-based and zero when the scrolling data is line-based.
- [kCGMouseEventWindowUnderMousePointer](cgeventfield/mouseeventwindowundermousepointer.md)
- [kCGMouseEventWindowUnderMousePointerThatCanHandleThisEvent](cgeventfield/mouseeventwindowundermousepointerthatcanhandlethisevent.md)
- [kCGScrollWheelEventMomentumPhase](cgeventfield/scrollwheeleventmomentumphase.md)
- [kCGScrollWheelEventScrollCount](cgeventfield/scrollwheeleventscrollcount.md)
- [kCGScrollWheelEventScrollPhase](cgeventfield/scrollwheeleventscrollphase.md)

### Enumeration Cases

- [kCGMouseEventWindowUnderMousePointer](cgeventfield/mouseeventwindowundermousepointer.md)
- [kCGMouseEventWindowUnderMousePointerThatCanHandleThisEvent](cgeventfield/mouseeventwindowundermousepointerthatcanhandlethisevent.md)
- [kCGScrollWheelEventMomentumPhase](cgeventfield/scrollwheeleventmomentumphase.md)
- [kCGScrollWheelEventScrollCount](cgeventfield/scrollwheeleventscrollcount.md)
- [kCGScrollWheelEventScrollPhase](cgeventfield/scrollwheeleventscrollphase.md)
- [kCGEventUnacceleratedPointerMovementX](cgeventfield/eventunacceleratedpointermovementx.md)
- [kCGEventUnacceleratedPointerMovementY](cgeventfield/eventunacceleratedpointermovementy.md)
- [kCGScrollWheelEventAcceleratedDeltaAxis1](cgeventfield/scrollwheeleventaccelerateddeltaaxis1.md)
- [kCGScrollWheelEventAcceleratedDeltaAxis2](cgeventfield/scrollwheeleventaccelerateddeltaaxis2.md)
- [kCGScrollWheelEventMomentumOptionPhase](cgeventfield/scrollwheeleventmomentumoptionphase.md)
- [kCGScrollWheelEventRawDeltaAxis1](cgeventfield/scrollwheeleventrawdeltaaxis1.md)
- [kCGScrollWheelEventRawDeltaAxis2](cgeventfield/scrollwheeleventrawdeltaaxis2.md)

### Initializers

- [init(rawValue:)](<cgeventfield/init(rawvalue_).md>)

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
- [CGEventFilterMask](cgeventfiltermask.md) — Specify masks for classes of low-level events that can be filtered during event suppression states.
- [CGEventFlags](cgeventflags.md) — Constants that indicate the modifier key state at the time an event is created, as well as other event-related states.
- [CGEventMouseSubtype](cgeventmousesubtype.md) — Constants used with the [kCGMouseEventSubtype](cgeventfield/mouseeventsubtype.md) event field.
- [CGEventSourceStateID](cgeventsourcestateid.md) — Constants that specify the possible source states of an event source.
- [CGEventSuppressionState](cgeventsuppressionstate.md) — Specify the event suppression states that can occur after posting an event.
- [CGEventTapLocation](cgeventtaplocation.md) — Constants that specify possible tapping points for events.
- [CGEventTapOptions](cgeventtapoptions.md) — Constants that specify whether a new event tap is an active filter or a passive listener.
