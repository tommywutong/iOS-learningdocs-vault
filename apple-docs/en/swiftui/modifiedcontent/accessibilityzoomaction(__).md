---
title: 'accessibilityZoomAction(_:)'
framework: SwiftUI
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, macOS 13.0+, tvOS 16.0+, visionOS 1.0+, watchOS 9.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/modifiedcontent/accessibilityzoomaction(_:)'
source_url: 'https://developer.apple.com/documentation/swiftui/modifiedcontent/accessibilityzoomaction(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/modifiedcontent/accessibilityzoomaction%28_%3A%29.json'
content_hash: 'sha256:acba7e5aafe2e97c'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [ModifiedContent](../modifiedcontent.md)

# accessibilityZoomAction(_:)

<sub>Instance Method</sub>

Adds an accessibility zoom action to the view. Actions allow assistive technologies, such as VoiceOver, to interact with the view by invoking the action.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
nonisolated func accessibilityZoomAction(_ handler: @escaping (AccessibilityZoomGestureAction) -> Void) -> ModifiedContent<Content, Modifier>
```

## Discussion

For example, this is how a zoom action is used to transform the scale of a shape which has a `MagnificationGesture`.

```swift
var body: some View {
    Circle()
        .scaleEffect(magnifyBy)
        .gesture(magnification)
        .accessibilityLabel("Circle Magnifier")
        .accessibilityZoomAction { action in
            switch action.direction {
            case .zoomIn:
                magnifyBy += 0.5
            case .zoomOut:
                 magnifyBy -= 0.5
            }
        }
}
```
