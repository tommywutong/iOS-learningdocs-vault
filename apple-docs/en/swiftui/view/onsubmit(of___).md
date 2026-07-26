---
title: 'onSubmit(of:_:)'
framework: SwiftUI
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, macOS 12.0+, tvOS 15.0+, visionOS 1.0+, watchOS 8.0+]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/view/onsubmit(of:_:)'
source_url: 'https://developer.apple.com/documentation/swiftui/view/onsubmit(of:_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/view/onsubmit%28of%3A_%3A%29.json'
content_hash: 'sha256:d0c9d65ee3e73bb7'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [View](../view.md)

# onSubmit(of:_:)

<sub>Instance Method</sub>

Adds an action to perform when the user submits a value to this view.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
nonisolated func onSubmit(of triggers: SubmitTriggers = .text, _ action: @escaping () -> Void) -> some View

```

## Parameters

- `triggers` — The triggers that should invoke the provided action.

- `action` — The action to perform on submission of a value.

## Discussion

Different views may have different triggers for the provided action. A [TextField](../textfield.md), or [SecureField](../securefield.md) will trigger this action when the user hits the hardware or software return key. This modifier may also bind this action to a default action keyboard shortcut. You may set this action on an individual view or an entire view hierarchy.

```swift
TextField("Username", text: $username)
    .onSubmit {
        guard viewModel.validate() else { return }
        viewModel.login()
    }
```

You can use the [submitScope(_:)](<submitscope(__).md>) modifier to stop a submit trigger from a control from propagating higher up in the view hierarchy to higher `View.onSubmit(of:_:)` modifiers.

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

You can use different submit triggers to filter the types of triggers that should invoke the provided submission action. For example, you may provide a value of [search](../submittriggers/search.md) to only hear submission triggers that originate from search fields vended by searchable modifiers.

```swift
@StateObject private var viewModel = ViewModel()

NavigationView {
    SidebarView()
    DetailView()
}
.searchable(
    text: $viewModel.searchText,
    placement: .sidebar
) {
    SuggestionsView()
}
.onSubmit(of: .search) {
    viewModel.submitCurrentSearchQuery()
}
```

## See Also

### Responding to submission events

- [submitScope(_:)](<submitscope(__).md>) — Prevents submission triggers originating from this view to invoke a submission action configured by a submission modifier higher up in the view hierarchy.
- [SubmitTriggers](../submittriggers.md) — A type that defines various triggers that result in the firing of a submission action.
