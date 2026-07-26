---
title: 'accessibilityZoomAction(_:)'
framework: SwiftUI
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, macOS 13.0+, tvOS 16.0+, visionOS 1.0+, watchOS 9.0+]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/view/accessibilityzoomaction(_:)'
source_url: 'https://developer.apple.com/documentation/swiftui/view/accessibilityzoomaction(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/view/accessibilityzoomaction%28_%3A%29.json'
content_hash: 'sha256:a6997e7ed642b96a'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [View](../view.md)

# accessibilityZoomAction(_:)

<sub>Instance Method</sub>

Adds an accessibility zoom action to the view. Actions allow assistive technologies, such as VoiceOver, to interact with the view by invoking the action.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
nonisolated func accessibilityZoomAction(_ handler: @escaping (AccessibilityZoomGestureAction) -> Void) -> ModifiedContent<Self, AccessibilityAttachmentModifier>
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

## See Also

### Making gestures accessible

- [accessibilityActivationPoint(_:)](<accessibilityactivationpoint(__).md>) — The activation point for an element is the location assistive technologies use to initiate gestures.
- [accessibilityActivationPoint(_:isEnabled:)](<accessibilityactivationpoint(__isenabled_).md>) — The activation point for an element is the location assistive technologies use to initiate gestures.
- [accessibilityDragPoint(_:description:)](<accessibilitydragpoint(__description_).md>) — The point an assistive technology should use to begin a drag interaction.
- [accessibilityDragPoint(_:description:isEnabled:)](<accessibilitydragpoint(__description_isenabled_).md>) — The point an assistive technology should use to begin a drag interaction.
- [accessibilityDropPoint(_:description:)](<accessibilitydroppoint(__description_).md>) — The point an assistive technology should use to end a drag interaction.
- [accessibilityDropPoint(_:description:isEnabled:)](<accessibilitydroppoint(__description_isenabled_).md>) — The point an assistive technology should use to end a drag interaction.
- [accessibilityDirectTouch(_:options:)](<accessibilitydirecttouch(__options_).md>) — Explicitly set whether this accessibility element is a direct touch area. Direct touch areas passthrough touch events to the app rather than being handled through an assistive technology, such as VoiceOver. The modifier accepts an optional `AccessibilityDirectTouchOptions` option set to customize the functionality of the direct touch area.
- [AccessibilityDirectTouchOptions](../accessibilitydirecttouchoptions.md) — An option set that defines the functionality of a view’s direct touch area.
- [AccessibilityZoomGestureAction](../accessibilityzoomgestureaction.md) — Position and direction information of a zoom gesture that someone performs with an assistive technology like VoiceOver.
