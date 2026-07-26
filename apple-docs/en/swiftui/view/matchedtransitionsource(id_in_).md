---
title: 'matchedTransitionSource(id:in:)'
framework: SwiftUI
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 18.0+, iPadOS 18.0+, Mac Catalyst 18.0+, macOS 15.0+, tvOS 18.0+, visionOS 2.0+, watchOS 11.0+]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/view/matchedtransitionsource(id:in:)'
source_url: 'https://developer.apple.com/documentation/swiftui/view/matchedtransitionsource(id:in:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/view/matchedtransitionsource%28id%3Ain%3A%29.json'
content_hash: 'sha256:fbf04c64271e8693'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [View](../view.md)

# matchedTransitionSource(id:in:)

<sub>Instance Method</sub>

Identifies this view as the source of a navigation transition, such as a zoom transition.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
nonisolated func matchedTransitionSource(id: some Hashable, in namespace: Namespace.ID) -> some View

```

## Parameters

- `id` — The identifier, often derived from the identifier of the data being displayed by the view.

- `namespace` — The namespace in which defines the `id`. New namespaces are created by adding an [Namespace](../namespace.md) variable to a [View](../view.md) type and reading its value in the view’s body method.

## See Also

### Defining matched transitions

- [matchedTransitionSource(id:in:configuration:)](<matchedtransitionsource(id_in_configuration_).md>) — Identifies this view as the source of a navigation transition, such as a zoom transition.
- [MatchedTransitionSourceConfiguration](../matchedtransitionsourceconfiguration.md) — A configuration that defines the appearance of a matched transition source.
- [EmptyMatchedTransitionSourceConfiguration](../emptymatchedtransitionsourceconfiguration.md) — An unstyled matched transition source configuration.
