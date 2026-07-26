---
title: CGEventField.eventSourceUserData
framework: Core Graphics
symbol_kind: case
role: symbol
role_heading: Case
platforms: [Mac Catalyst, macOS]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/coregraphics/cgeventfield/eventsourceuserdata
source_url: 'https://developer.apple.com/documentation/coregraphics/cgeventfield/eventsourceuserdata'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coregraphics/cgeventfield/eventsourceuserdata.json'
content_hash: 'sha256:4a2ca222c476d18b'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Graphics](../../coregraphics.md) · [CGEventField](../cgeventfield.md)

# CGEventField.eventSourceUserData

<sub>Case</sub>

Key to access a field that contains the event source user-supplied data, up to 64 bits.

<sub>Mac Catalyst, macOS</sub>

```swift
case eventSourceUserData
```

## See Also

### Constants

- [kCGMouseEventNumber](mouseeventnumber.md) — Key to access an integer field that contains the mouse button event number. Matching mouse-down and mouse-up events will have the same event number.
- [kCGMouseEventClickState](mouseeventclickstate.md) — Key to access an integer field that contains the mouse button click state. A click state of 1 represents a single click. A click state of 2 represents a double-click. A click state of 3 represents a triple-click.
- [kCGMouseEventPressure](mouseeventpressure.md) — Key to access a double field that contains the mouse button pressure. The pressure value may range from 0 to 1, with 0 representing the mouse being up. This value is commonly set by tablet pens mimicking a mouse.
- [kCGMouseEventButtonNumber](mouseeventbuttonnumber.md) — Key to access an integer field that contains the mouse button number. For information about the possible values, see [CGMouseButton](../cgmousebutton.md).
- [kCGMouseEventDeltaX](mouseeventdeltax.md) — Key to access an integer field that contains the horizontal mouse delta since the last mouse movement event.
- [kCGMouseEventDeltaY](mouseeventdeltay.md) — Key to access an integer field that contains the vertical mouse delta since the last mouse movement event.
- [kCGMouseEventInstantMouser](mouseeventinstantmouser.md) — Key to access an integer field. The value is non-zero if the event should be ignored by the Inkwell subsystem.
- [kCGMouseEventSubtype](mouseeventsubtype.md) — Key to access an integer field that encodes the mouse event subtype as a `kCFNumberIntType`.
- [kCGKeyboardEventAutorepeat](keyboardeventautorepeat.md) — Key to access an integer field, non-zero when this is an autorepeat of a key-down, and zero otherwise.
- [kCGKeyboardEventKeycode](keyboardeventkeycode.md) — Key to access an integer field that contains the virtual keycode of the key-down or key-up event.
- [kCGKeyboardEventKeyboardType](keyboardeventkeyboardtype.md) — Key to access an integer field that contains the keyboard type identifier.
- [kCGScrollWheelEventDeltaAxis1](scrollwheeleventdeltaaxis1.md) — Key to access an integer field that contains scrolling data. This field typically contains the change in vertical position since the last scrolling event from a Mighty Mouse scroller or a single-wheel mouse scroller.
- [kCGScrollWheelEventDeltaAxis2](scrollwheeleventdeltaaxis2.md) — Key to access an integer field that contains scrolling data. This field typically contains the change in horizontal position since the last scrolling event from a Mighty Mouse scroller.
- [kCGScrollWheelEventDeltaAxis3](scrollwheeleventdeltaaxis3.md) — This field is not used.
- [kCGScrollWheelEventFixedPtDeltaAxis1](scrollwheeleventfixedptdeltaaxis1.md) — Key to access a field that contains scrolling data. The scrolling data represents a line-based or pixel-based change in vertical position since the last scrolling event from a Mighty Mouse scroller or a single-wheel mouse scroller. The scrolling data uses a fixed-point 16.16 signed integer format. For example, if the field contains a value of 1.0, the integer 0x00010000 is returned by `CGEventGetIntegerValueField`. If this key is passed to `CGEventGetDoubleValueField`, the fixed-point value is converted to a double value.
