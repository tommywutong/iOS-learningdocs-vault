---
title: body
framework: SwiftUI
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.0+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/view/body-8kl5o
source_url: 'https://developer.apple.com/documentation/swiftui/view/body-8kl5o'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/view/body-8kl5o.json'
content_hash: 'sha256:09d3d5255f8965bc'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [View](../view.md)

# body

<sub>Instance Property</sub>

The content and behavior of the view.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
@ContentBuilder @MainActor @preconcurrency var body: Self.Body { get }
```

## Discussion

When you implement a custom view, you must implement a computed `body` property to provide the content for your view. Return a view that’s composed of built-in views that SwiftUI provides, plus other composite views that you’ve already defined:

```swift
struct MyView: View {
    var body: some View {
        Text("Hello, World!")
    }
}
```

For more information about composing views and a view hierarchy, see [Declaring a custom view](../declaring-a-custom-view.md).

## Default Implementations

### NSViewControllerRepresentable Implementations

- [body](../nsviewcontrollerrepresentable/body.md) — Declares the content and behavior of this view.

### NSViewRepresentable Implementations

- [body](../nsviewrepresentable/body.md) — Declares the content and behavior of this view.

### UIViewControllerRepresentable Implementations

- [body](../uiviewcontrollerrepresentable/body.md) — Declares the content and behavior of this view.

### UIViewRepresentable Implementations

- [body](../uiviewrepresentable/body.md) — Declares the content and behavior of this view.

### View Implementations

- [body](body-44706.md)

### WKInterfaceObjectRepresentable Implementations

- [body](../wkinterfaceobjectrepresentable/body.md) — Declares the content and behavior of this view.

## See Also

### Implementing a custom view

- [Body](body-swift.associatedtype.md) — The type of view representing the body of this view.
- [modifier(_:)](<modifier(__).md>) — Applies a modifier to a view and returns a new view.
- [Previews in Xcode](../previews-in-xcode.md) — Generate dynamic, interactive previews of your custom views.
