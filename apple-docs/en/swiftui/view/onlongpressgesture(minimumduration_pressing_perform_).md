---
title: 'onLongPressGesture(minimumDuration:pressing:perform:)'
framework: SwiftUI
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [tvOS 14.0+（27.0 起废弃）]
languages: [swift]
beta: false
deprecated: true
doc_path: '/documentation/swiftui/view/onlongpressgesture(minimumduration:pressing:perform:)'
source_url: 'https://developer.apple.com/documentation/swiftui/view/onlongpressgesture(minimumduration:pressing:perform:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/view/onlongpressgesture%28minimumduration%3Apressing%3Aperform%3A%29.json'
content_hash: 'sha256:0bf9d26dfbe312dc'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [View](../view.md)

# onLongPressGesture(minimumDuration:pressing:perform:)

<sub>Instance Method</sub>

Adds an action to perform when this view recognizes a long press gesture.

> [!warning] Deprecated
> Use [onLongPressGesture(minimumDuration:perform:onPressingChanged:)](<onlongpressgesture(minimumduration_perform_onpressingchanged_).md>) instead.

<sub>tvOS</sub>

```swift
nonisolated func onLongPressGesture(minimumDuration: Double = 0.5, pressing: ((Bool) -> Void)? = nil, perform action: @escaping () -> Void) -> some View

```

## See Also

### Input and events modifiers

- [dropDestination(for:action:isTargeted:)](<dropdestination(for_action_istargeted_).md>) — Defines the destination of a drag and drop operation that handles the dropped content with a closure that you specify. _(deprecated)_
- [onChange(of:perform:)](<onchange(of_perform_).md>) — Adds an action to perform when the given value changes. _(deprecated)_
- [onTapGesture(count:coordinateSpace:perform:)](<ontapgesture(count_coordinatespace_perform_)-36x9h.md>) — Adds an action to perform when this view recognizes a tap gesture, and provides the action with the location of the interaction. _(deprecated)_
- [onLongPressGesture(minimumDuration:maximumDistance:pressing:perform:)](<onlongpressgesture(minimumduration_maximumdistance_pressing_perform_).md>) — Adds an action to perform when this view recognizes a long press gesture. _(deprecated)_
- [onPasteCommand(of:perform:)](<onpastecommand(of_perform_)-4f78f.md>) — Adds an action to perform in response to the system’s Paste command. _(deprecated)_
- [onPasteCommand(of:validator:perform:)](<onpastecommand(of_validator_perform_)-964k1.md>) — Adds an action to perform in response to the system’s Paste command with items that you validate. _(deprecated)_
- [onDrop(of:delegate:)](<ondrop(of_delegate_)-2vr9o.md>) — Defines the destination for a drag and drop operation with the same size and position as this view, with behavior controlled by the given delegate. _(deprecated)_
- [onDrop(of:isTargeted:perform:)](<ondrop(of_istargeted_perform_).md>) — Defines the destination of a drag-and-drop operation that handles the dropped content with a closure that you specify.
- [focusable(_:onFocusChange:)](<focusable(__onfocuschange_).md>) — Specifies if the view is focusable and, if so, adds an action to perform when the view comes into focus. _(deprecated)_
- [onContinuousHover(coordinateSpace:perform:)](<oncontinuoushover(coordinatespace_perform_)-8gyrl.md>) — Adds an action to perform when the pointer enters, moves within, and exits the view’s bounds. _(deprecated)_
