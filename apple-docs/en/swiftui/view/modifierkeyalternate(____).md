---
title: 'modifierKeyAlternate(_:_:)'
framework: SwiftUI
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [macOS 15.0+]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/view/modifierkeyalternate(_:_:)'
source_url: 'https://developer.apple.com/documentation/swiftui/view/modifierkeyalternate(_:_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/view/modifierkeyalternate%28_%3A_%3A%29.json'
content_hash: 'sha256:212f98d9c78a856f'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [View](../view.md)

# modifierKeyAlternate(_:_:)

<sub>Instance Method</sub>

Builds a view to use in place of the modified view when the user presses the modifier key(s) indicated by the given set.

<sub>macOS</sub>

```swift
nonisolated func modifierKeyAlternate<V>(_ modifiers: EventModifiers, @ContentBuilder _ alternate: () -> V) -> some View where V : View

```

## Parameters

- `modifiers` — The modifier keys to associate with the alternate view. While all these keys are held, SwiftUI will replace the modified view with this alternate one.

- `alternate` — A content builder for constructing the modified view’s alternate when matching modifier keys are pressed.

## Return Value

A modified view with an alternate view to use while specific modifier keys are held down.

## Discussion

```swift
Button("Go Forward", ...)
    .modifierKeyAlternate(.option) {
        Button("Go to Page…", ...)
    }
```

In menu style contexts, modifier key alternates become alternate menu items. If the modified view has a keyboard shortcut, it will be used as the basis for the alternate view’s shortcut.

```swift
// File > Save
Button("Save", ...) // ⌘ S
    .keyboardShortcut("s")
    .modifierKeyAlternate(.option) {
        Button("Save All", ...) // ⌥⌘ S
    }
```

To use a different keyboard shortcut for the alternate view, add one explicitly in the content builder. SwiftUI will use your explicit shortcut instead of its own inferred one.

```swift
Button("Go Forward", ...) // ⌘ →
    .keyboardShortcut(.rightArrow)
    .modifierKeyAlternate(.control) {
        Button("Go To Page…", ...) // ⌃ →
            .keyboardShortcut(.rightArrow, modifiers: .control)
    }
```

A view can have multiple modifier key alternates, provided their associated modifier keys are different. When multiple alternates match the currently-held keys, the most specific match prevails.

```swift
Button("Save", ...) // ⌘ S
    .keyboardShortcut("s")
    .modifierKeyAlternate(.option) {
        Button("Save All", ...) // ⌥⌘ S
    }
    .modifierKeyAlternate([.option, .shift]) {
        Button("Save a Copy…", ...) // ⇧⌥⌘ S
    }
```

## See Also

### Responding to modifier keys

- [onModifierKeysChanged(mask:initial:_:)](<onmodifierkeyschanged(mask_initial___).md>) — Performs an action whenever the user presses or releases a hardware modifier key.
