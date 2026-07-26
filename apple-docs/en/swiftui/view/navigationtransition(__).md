---
title: 'navigationTransition(_:)'
framework: SwiftUI
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 18.0+, iPadOS 18.0+, Mac Catalyst 18.0+, macOS 15.0+, tvOS 18.0+, visionOS 2.0+, watchOS 11.0+]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/view/navigationtransition(_:)'
source_url: 'https://developer.apple.com/documentation/swiftui/view/navigationtransition(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/view/navigationtransition%28_%3A%29.json'
content_hash: 'sha256:7d9a4623de11f292'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [View](../view.md)

# navigationTransition(_:)

<sub>Instance Method</sub>

Sets the navigation transition style for this view.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
nonisolated func navigationTransition(_ style: some NavigationTransition) -> some View

```

## Discussion

Add this modifier to a view that appears within a [NavigationStack](../navigationstack.md) or a sheet, outside of any containers such as [VStack](../vstack.md).

```swift
struct ContentView: View {
    @Namespace private var namespace
    var body: some View {
        NavigationStack {
            NavigationLink {
                DetailView()
                    .navigationTransition(.zoom(sourceID: "world", in: namespace))
            } label: {
                Image(systemName: "globe")
                    .matchedTransitionSource(id: "world", in: namespace)
            }
        }
    }
}
```

## See Also

### Defining navigation transitions

- [NavigationTransition](../navigationtransition.md) — A type that defines the transition to use when navigating to a view.
- [AnyNavigationTransition](../anynavigationtransition.md) — A type-erasing navigation transition that allows for providing any navigation transition value dynamically. _(beta)_
- [CrossFadeNavigationTransition](../crossfadenavigationtransition.md) — A navigation transition that cross-fades between the appearing view and the disappearing view. _(beta)_
