---
title: 'matchedTransitionSource(id:in:configuration:)'
framework: SwiftUI
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 18.0+, iPadOS 18.0+, Mac Catalyst 18.0+, macOS 15.0+, tvOS 18.0+, visionOS 2.0+, watchOS 11.0+]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/view/matchedtransitionsource(id:in:configuration:)'
source_url: 'https://developer.apple.com/documentation/swiftui/view/matchedtransitionsource(id:in:configuration:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/view/matchedtransitionsource%28id%3Ain%3Aconfiguration%3A%29.json'
content_hash: 'sha256:15b93e4b254947bc'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [View](../view.md)

# matchedTransitionSource(id:in:configuration:)

<sub>Instance Method</sub>

Identifies this view as the source of a navigation transition, such as a zoom transition.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
nonisolated func matchedTransitionSource(id: some Hashable, in namespace: Namespace.ID, configuration: (EmptyMatchedTransitionSourceConfiguration) -> some MatchedTransitionSourceConfiguration) -> some View

```

## Parameters

- `id` — The identifier, often derived from the identifier of the data being displayed by the view.

- `namespace` — The namespace in which defines the `id`. New namespaces are created by adding an [Namespace](../namespace.md) variable to a [View](../view.md) type and reading its value in the view’s body method.

- `configuration` — A closure that you can use to apply styling to the source.

## Discussion

The appearance of the source can be configured using the `configuration` trailing closure. Any modifiers applied will be smoothly interpolated when a zoom transition originates from this matched transition source.

```swift
MyView()
    .matchedTransitionSource(id: someID, in: someNamespace) { source in
        source
            .cornerRadius(8.0)
    }
```

## See Also

### Defining matched transitions

- [matchedTransitionSource(id:in:)](<matchedtransitionsource(id_in_).md>) — Identifies this view as the source of a navigation transition, such as a zoom transition.
- [MatchedTransitionSourceConfiguration](../matchedtransitionsourceconfiguration.md) — A configuration that defines the appearance of a matched transition source.
- [EmptyMatchedTransitionSourceConfiguration](../emptymatchedtransitionsourceconfiguration.md) — An unstyled matched transition source configuration.
