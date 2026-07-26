---
title: 'navigationDestination(isPresented:destination:)'
framework: SwiftUI
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, macOS 13.0+, tvOS 16.0+, visionOS 1.0+, watchOS 9.0+]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/view/navigationdestination(ispresented:destination:)'
source_url: 'https://developer.apple.com/documentation/swiftui/view/navigationdestination(ispresented:destination:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/view/navigationdestination%28ispresented%3Adestination%3A%29.json'
content_hash: 'sha256:b43c6ed210f7df1b'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [View](../view.md)

# navigationDestination(isPresented:destination:)

<sub>Instance Method</sub>

Associates a destination view with a binding that can be used to push the view onto a [NavigationStack](../navigationstack.md).

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
nonisolated func navigationDestination<V>(isPresented: Binding<Bool>, @ContentBuilder destination: () -> V) -> some View where V : View

```

## Parameters

- `isPresented` — A binding to a Boolean value that indicates whether `destination` is currently presented.

- `destination` — A view to present.

## Discussion

In general, favor binding a path to a navigation stack for programmatic navigation. Add this view modifier to a view inside a [NavigationStack](../navigationstack.md) to programmatically push a single view onto the stack. This is useful for building components that can push an associated view. For example, you can present a `ColorDetail` view for a particular color:

```swift
@State private var showDetails = false
var favoriteColor: Color

NavigationStack {
    VStack {
        Circle()
            .fill(favoriteColor)
        Button("Show details") {
            showDetails = true
        }
    }
    .navigationDestination(isPresented: $showDetails) {
        ColorDetail(color: favoriteColor)
    }
    .navigationTitle("My Favorite Color")
}
```

Do not put a navigation destination modifier inside a “lazy” container, like [List](../list.md) or [LazyVStack](../lazyvstack.md). These containers create child views only when needed to render on screen. Add the navigation destination modifier outside these containers so that the navigation stack can always see the destination.

## See Also

### Stacking views in one column

- [NavigationStack](../navigationstack.md) — A view that displays a root view and enables you to present additional views over the root view.
- [NavigationPath](../navigationpath.md) — A type-erased list of data representing the content of a navigation stack.
- [navigationDestination(for:destination:)](<navigationdestination(for_destination_).md>) — Associates a destination view with a presented data type for use within a navigation stack.
- [navigationDestination(item:destination:)](<navigationdestination(item_destination_).md>) — Associates a destination view with a bound value for use within a navigation stack or navigation split view
