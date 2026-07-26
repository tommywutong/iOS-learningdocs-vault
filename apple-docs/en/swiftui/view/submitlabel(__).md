---
title: 'submitLabel(_:)'
framework: SwiftUI
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, macOS 12.0+, tvOS 15.0+, visionOS 1.0+, watchOS 8.0+]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/view/submitlabel(_:)'
source_url: 'https://developer.apple.com/documentation/swiftui/view/submitlabel(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/view/submitlabel%28_%3A%29.json'
content_hash: 'sha256:ce4d47ebfa36f4f1'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [View](../view.md)

# submitLabel(_:)

<sub>Instance Method</sub>

Sets the submit label for this view.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
nonisolated func submitLabel(_ submitLabel: SubmitLabel) -> some View

```

## Parameters

- `submitLabel` — One of the cases specified in [SubmitLabel](../submitlabel.md).

## Discussion

```swift
Form {
    TextField("Username", $viewModel.username)
        .submitLabel(.continue)
    SecureField("Password", $viewModel.password)
        .submitLabel(.done)
}
```

## See Also

### Labeling a submission event

- [SubmitLabel](../submitlabel.md) — A semantic label describing the label of submission within a view hierarchy.
