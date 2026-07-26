---
title: 'searchScopes(_:scopes:)'
framework: SwiftUI
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, macOS 13.0+, tvOS 16.4+, visionOS 1.0+]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/view/searchscopes(_:scopes:)'
source_url: 'https://developer.apple.com/documentation/swiftui/view/searchscopes(_:scopes:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/view/searchscopes%28_%3Ascopes%3A%29.json'
content_hash: 'sha256:0eb88caff7710968'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [View](../view.md)

# searchScopes(_:scopes:)

<sub>Instance Method</sub>

Configures the search scopes for this view.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
nonisolated func searchScopes<V, S>(_ scope: Binding<V>, @ContentBuilder scopes: () -> S) -> some View where V : Hashable, S : View

```

## Parameters

- `scope` — The active scope of the search field.

- `scopes` — A content builder that represents the scoping options SwiftUI uses to populate a [Picker](../picker.md).

## Discussion

To enable people to narrow the scope of their searches, you can create a type that represents the possible scopes, and then create a state variable to hold the current selection. For example, you can scope the product search to just fruits or just vegetables:

```swift
enum ProductScope {
    case fruit
    case vegetable
}

@State private var scope: ProductScope = .fruit
```

Provide a binding to the scope, as well as a view that represents each scope:

```swift
ProductList()
    .searchable(text: $text, tokens: $tokens) { token in
        switch token {
        case .apple: Text("Apple")
        case .pear: Text("Pear")
        case .banana: Text("Banana")
        }
    }
    .searchScopes($scope) {
        Text("Fruit").tag(ProductScope.fruit)
        Text("Vegetable").tag(ProductScope.vegetable)
    }
```

SwiftUI uses this binding and view to add a [Picker](../picker.md) with the search field. In iOS, iPadOS, macOS, and tvOS, the picker appears below the search field when search is active. To ensure that the picker operates correctly, match the type of the scope binding with the type of each view’s tag. Then modify your search to account for the current value of the `scope` state property.

For more information about using searchable modifiers, see [Adding a search interface to your app](../adding-a-search-interface-to-your-app.md).

## See Also

### Limiting search scope

- [Scoping a search operation](../scoping-a-search-operation.md) — Divide the search space into a few broad categories.
- [searchScopes(_:activation:_:)](<searchscopes(__activation___).md>) — Configures the search scopes for this view with the specified activation strategy.
- [SearchScopeActivation](../searchscopeactivation.md) — The ways that searchable modifiers can show or hide search scopes.
