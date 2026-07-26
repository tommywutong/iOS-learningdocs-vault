---
title: 'submitScope(_:)'
framework: SwiftUI
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, macOS 12.0+, tvOS 15.0+, visionOS 1.0+, watchOS 8.0+]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/view/submitscope(_:)'
source_url: 'https://developer.apple.com/documentation/swiftui/view/submitscope(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/view/submitscope%28_%3A%29.json'
content_hash: 'sha256:511e7777622219db'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [View](../view.md)

# submitScope(_:)

<sub>Instance Method</sub>

Prevents submission triggers originating from this view to invoke a submission action configured by a submission modifier higher up in the view hierarchy.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
nonisolated func submitScope(_ isBlocking: Bool = true) -> some View

```

## Parameters

- `isBlocking` — A Boolean that indicates whether this scope is actively blocking submission triggers from reaching higher submission actions.

## Discussion

Use this modifier when you want to avoid specific views from initiating a submission action configured by the [onSubmit(of:_:)](<onsubmit(of___).md>) modifier. In the example below, the tag field doesn’t trigger the submission of the form:

```swift
Form {
    TextField("Username", text: $viewModel.userName)
    SecureField("Password", text: $viewModel.password)

    TextField("Tags", text: $viewModel.tags)
        .submitScope()
}
.onSubmit {
    guard viewModel.validate() else { return }
    viewModel.login()
}
```

## See Also

### Responding to submission events

- [onSubmit(of:_:)](<onsubmit(of___).md>) — Adds an action to perform when the user submits a value to this view.
- [SubmitTriggers](../submittriggers.md) — A type that defines various triggers that result in the firing of a submission action.
