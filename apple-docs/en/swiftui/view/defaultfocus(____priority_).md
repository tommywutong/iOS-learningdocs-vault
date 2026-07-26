---
title: 'defaultFocus(_:_:priority:)'
framework: SwiftUI
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 17.0+, iPadOS 17.0+, Mac Catalyst 17.0+, macOS 13.0+, tvOS 16.0+, visionOS 1.0+, watchOS 9.0+]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/view/defaultfocus(_:_:priority:)'
source_url: 'https://developer.apple.com/documentation/swiftui/view/defaultfocus(_:_:priority:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/view/defaultfocus%28_%3A_%3Apriority%3A%29.json'
content_hash: 'sha256:50df2058a16c2ec5'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [View](../view.md)

# defaultFocus(_:_:priority:)

<sub>Instance Method</sub>

Defines a region of the window in which default focus is evaluated by assigning a value to a given focus state binding.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
nonisolated func defaultFocus<V>(_ binding: FocusState<V>.Binding, _ value: V, priority: DefaultFocusEvaluationPriority = .automatic) -> some View where V : Hashable

```

## Parameters

- `binding` — A focus state binding to update when evaluating default focus in the modified view hierarchy.

- `value` — The value to set the binding to during evaluation.

- `priority` — An indication of how to prioritize the preferred default focus target when focus moves into the modified view hierarchy. The default value is `automatic`, which means the preference will be given priority when focus is being initialized or relocated programmatically, but not when responding to user-directed navigation commands.

## Return Value

The modified view.

## Discussion

By default, SwiftUI evaluates default focus when the window first appears, and when a focus state binding update moves focus automatically, but not when responding to user-driven navigation commands.

Clients can override the default behavior by specifying an evaluation priority of [userInitiated](../defaultfocusevaluationpriority/userinitiated.md), which causes SwiftUI to use the client’s preferred default focus in response to user-driven focus navigation as well as automatic changes.

In the following example, focus automatically goes to the second of the two text fields when the view is first presented in the window.

```swift
WindowGroup {
    VStack {
        TextField(...)
            .focused($focusedField, equals: .firstField)
        TextField(...)
            .focused($focusedField, equals: .secondField)
    }
    .defaultFocus($focusedField, .secondField)
}
```

## See Also

### Controlling default focus

- [prefersDefaultFocus(_:in:)](<prefersdefaultfocus(__in_).md>) — Indicates that the view should receive focus by default for a given namespace.
- [DefaultFocusEvaluationPriority](../defaultfocusevaluationpriority.md) — Prioritizations for default focus preferences when evaluating where to move focus in different circumstances.
