---
title: touchDragInside
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS, iPadOS, Mac Catalyst, tvOS, visionOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uicontrol/event/touchdraginside
source_url: 'https://developer.apple.com/documentation/uikit/uicontrol/event/touchdraginside'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uicontrol/event/touchdraginside.json'
content_hash: 'sha256:7135e5fe884f6bc4'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [UIKit](../../../uikit.md) · [UIControl](../../uicontrol.md) · [Event](../event.md)

# touchDragInside

<sub>Type Property</sub>

An event where a finger is dragged inside the bounds of the control.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
static var touchDragInside: UIControl.Event { get }
```

## See Also

### Constants

- [UIControlEventTouchDown](touchdown.md) — A touch-down event in the control.
- [UIControlEventTouchDownRepeat](touchdownrepeat.md) — A repeated touch-down event in the control; for this event the value of the UITouch `tapCount` method is greater than one.
- [UIControlEventTouchDragOutside](touchdragoutside.md) — An event where a finger is dragged just outside the bounds of the control.
- [UIControlEventTouchDragEnter](touchdragenter.md) — An event where a finger is dragged into the bounds of the control.
- [UIControlEventTouchDragExit](touchdragexit.md) — An event where a finger is dragged from within a control to outside its bounds.
- [UIControlEventTouchUpInside](touchupinside.md) — A touch-up event in the control where the finger is inside the bounds of the control.
- [UIControlEventTouchUpOutside](touchupoutside.md) — A touch-up event in the control where the finger is outside the bounds of the control.
- [UIControlEventTouchCancel](touchcancel.md) — A system event canceling the current touches for the control.
- [UIControlEventValueChanged](valuechanged.md) — A touch dragging or otherwise manipulating a control, causing it to emit a series of different values.
- [UIControlEventMenuActionTriggered](menuactiontriggered.md) — A menu action has triggered prior to the menu being presented.
- [UIControlEventPrimaryActionTriggered](primaryactiontriggered.md) — A semantic action triggered by buttons.
- [UIControlEventEditingDidBegin](editingdidbegin.md) — A touch initiating an editing session in a text field by entering its bounds.
- [UIControlEventEditingChanged](editingchanged.md) — A touch making an editing change in a text field.
- [UIControlEventEditingDidEnd](editingdidend.md) — A touch ending an editing session in a text field by leaving its bounds.
- [UIControlEventEditingDidEndOnExit](editingdidendonexit.md) — A touch ending an editing session in a text field.
