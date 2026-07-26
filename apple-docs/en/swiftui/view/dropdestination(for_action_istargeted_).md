---
title: 'dropDestination(for:action:isTargeted:)'
framework: SwiftUI
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 16.0+（27.0 起废弃）, iPadOS 16.0+（27.0 起废弃）, Mac Catalyst 16.0+（27.0 起废弃）, macOS 13.0+（27.0 起废弃）, visionOS 1.0+]
languages: [swift]
beta: false
deprecated: true
doc_path: '/documentation/swiftui/view/dropdestination(for:action:istargeted:)'
source_url: 'https://developer.apple.com/documentation/swiftui/view/dropdestination(for:action:istargeted:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/view/dropdestination%28for%3Aaction%3Aistargeted%3A%29.json'
content_hash: 'sha256:121eda921750f988'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [View](../view.md)

# dropDestination(for:action:isTargeted:)

<sub>Instance Method</sub>

Defines the destination of a drag and drop operation that handles the dropped content with a closure that you specify.

> [!warning] Deprecated
> Use [dropDestination(for:isEnabled:action:)](<dropdestination(for_isenabled_action_).md>) with an `action` that takes a [DropSession](../dropsession.md) instead.

<sub>iOS, iPadOS, Mac Catalyst, macOS, visionOS</sub>

```swift
nonisolated func dropDestination<T>(for payloadType: T.Type = T.self, action: @escaping ([T], CGPoint) -> Bool, isTargeted: @escaping (Bool) -> Void = { _ in }) -> some View where T : Transferable

```

## Parameters

- `payloadType` — The expected type of the dropped models.

- `action` — A closure that takes the dropped content and responds appropriately. The first parameter to `action` contains the dropped items. The second parameter contains the drop location in this view’s coordinate space. Return `true` if the drop operation was successful; otherwise, return `false`.

- `isTargeted` — A closure that is called when a drag and drop operation enters or exits the drop target area. The received value is `true` when the cursor is inside the area, and `false` when the cursor is outside.

## Return Value

A view that provides a drop destination for a drag operation of the specified type.

## Discussion

The dropped content can be provided as binary data, file URLs, or file promises.

The drop destination is the same size and position as this view.

```swift
@State private var isDropTargeted = false

var body: some View {
    Color.pink
        .frame(width: 400, height: 400)
        .dropDestination(for: String.self) { receivedTitles, location in
            animateDrop(at: location)
            process(titles: receivedTitles)
        } isTargeted: {
            isDropTargeted = $0
        }
}

func process(titles: [String]) { ... }
func animateDrop(at: CGPoint) { ... }
```

## See Also

### Input and events modifiers

- [onChange(of:perform:)](<onchange(of_perform_).md>) — Adds an action to perform when the given value changes. _(deprecated)_
- [onTapGesture(count:coordinateSpace:perform:)](<ontapgesture(count_coordinatespace_perform_)-36x9h.md>) — Adds an action to perform when this view recognizes a tap gesture, and provides the action with the location of the interaction. _(deprecated)_
- [onLongPressGesture(minimumDuration:maximumDistance:pressing:perform:)](<onlongpressgesture(minimumduration_maximumdistance_pressing_perform_).md>) — Adds an action to perform when this view recognizes a long press gesture. _(deprecated)_
- [onLongPressGesture(minimumDuration:pressing:perform:)](<onlongpressgesture(minimumduration_pressing_perform_).md>) — Adds an action to perform when this view recognizes a long press gesture. _(deprecated)_
- [onPasteCommand(of:perform:)](<onpastecommand(of_perform_)-4f78f.md>) — Adds an action to perform in response to the system’s Paste command. _(deprecated)_
- [onPasteCommand(of:validator:perform:)](<onpastecommand(of_validator_perform_)-964k1.md>) — Adds an action to perform in response to the system’s Paste command with items that you validate. _(deprecated)_
- [onDrop(of:delegate:)](<ondrop(of_delegate_)-2vr9o.md>) — Defines the destination for a drag and drop operation with the same size and position as this view, with behavior controlled by the given delegate. _(deprecated)_
- [onDrop(of:isTargeted:perform:)](<ondrop(of_istargeted_perform_).md>) — Defines the destination of a drag-and-drop operation that handles the dropped content with a closure that you specify.
- [focusable(_:onFocusChange:)](<focusable(__onfocuschange_).md>) — Specifies if the view is focusable and, if so, adds an action to perform when the view comes into focus. _(deprecated)_
- [onContinuousHover(coordinateSpace:perform:)](<oncontinuoushover(coordinatespace_perform_)-8gyrl.md>) — Adds an action to perform when the pointer enters, moves within, and exits the view’s bounds. _(deprecated)_
