---
title: 'onGeometryChange(for:of:action:)'
framework: SwiftUI
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, macOS 13.0+, tvOS 16.0+, visionOS 1.0+, watchOS 9.0+]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/view/ongeometrychange(for:of:action:)'
source_url: 'https://developer.apple.com/documentation/swiftui/view/ongeometrychange(for:of:action:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/view/ongeometrychange%28for%3Aof%3Aaction%3A%29.json'
content_hash: 'sha256:65013f5be6a06c34'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [View](../view.md)

# onGeometryChange(for:of:action:)

<sub>Instance Method</sub>

Adds an action to be performed when a value, created from a geometry proxy, changes.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
@export(implementation) @preconcurrency nonisolated func onGeometryChange<T>(for type: T.Type, of transform: @escaping @Sendable (GeometryProxy) -> T, action: @escaping (T) -> Void) -> some View where T : Equatable, T : Sendable

```

## Parameters

- `type` — The type of value transformed from a [GeometryProxy](../geometryproxy.md).

- `transform` — A closure that transforms a [GeometryProxy](../geometryproxy.md) to your type.

- `action` — A closure to run when the transformed data changes. - **newValue** — The new value that failed the comparison check.

## Discussion

The geometry of a view can change frequently, especially if the view is contained within a [ScrollView](../scrollview.md) and that scroll view is scrolling.

You should avoid updating large parts of your app whenever the scroll geometry changes. To aid in this, you provide two closures to this modifier:

- transform: This converts a value of [GeometryProxy](../geometryproxy.md) to your own data type.
- action: This provides the data type you created in `of` and is called whenever the data type changes.

For example, you can use this modifier to know how much of a view is visible on screen. In the following example, the data type you convert to is a `Bool` and the action is called whenever the `Bool` changes.

```swift
ScrollView(.horizontal) {
    LazyHStack {
         ForEach(videos) { video in
             VideoView(video)
         }
     }
 }

struct VideoView: View {
    var video: VideoModel

    var body: some View {
        VideoPlayer(video)
            .onGeometryChange(for: Bool.self) { proxy in
                let frame = proxy.frame(in: .scrollView)
                let bounds = proxy.bounds(of: .scrollView) ?? .zero
                let intersection = frame.intersection(
                    CGRect(origin: .zero, size: bounds.size))
                let visibleHeight = intersection.size.height
                return (visibleHeight / frame.size.height) > 0.75
            } action: { isVisible in
                video.updateAutoplayingState(
                    isVisible: isVisible)
            }
    }
}
```

For easily responding to geometry changes of a scroll view, see the [onScrollGeometryChange(for:of:action:)](<onscrollgeometrychange(for_of_action_).md>) modifier.
