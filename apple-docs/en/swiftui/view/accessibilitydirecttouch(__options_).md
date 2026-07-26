---
title: 'accessibilityDirectTouch(_:options:)'
framework: SwiftUI
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 17.0+, iPadOS 17.0+, Mac Catalyst 17.0+, macOS 14.0+, tvOS 17.0+, visionOS 1.0+, watchOS 10.0+]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/view/accessibilitydirecttouch(_:options:)'
source_url: 'https://developer.apple.com/documentation/swiftui/view/accessibilitydirecttouch(_:options:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/view/accessibilitydirecttouch%28_%3Aoptions%3A%29.json'
content_hash: 'sha256:69afbf234476e3a5'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [View](../view.md)

# accessibilityDirectTouch(_:options:)

<sub>Instance Method</sub>

Explicitly set whether this accessibility element is a direct touch area. Direct touch areas passthrough touch events to the app rather than being handled through an assistive technology, such as VoiceOver. The modifier accepts an optional `AccessibilityDirectTouchOptions` option set to customize the functionality of the direct touch area.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
nonisolated func accessibilityDirectTouch(_ isDirectTouchArea: Bool = true, options: AccessibilityDirectTouchOptions = []) -> ModifiedContent<Self, AccessibilityAttachmentModifier>
```

## Discussion

For example, this is how a direct touch area would allow a VoiceOver user to interact with a view with a `rotationEffect` controlled by a `RotationGesture`. The direct touch area would require a user to activate the area before using the direct touch area.

```swift
var body: some View {
    Rectangle()
        .frame(width: 200, height: 200, alignment: .center)
        .rotationEffect(angle)
        .gesture(rotation)
        .accessibilityDirectTouch(options: .requiresActivation)
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
- [accessibilityZoomAction(_:)](<accessibilityzoomaction(__).md>) — Adds an accessibility zoom action to the view. Actions allow assistive technologies, such as VoiceOver, to interact with the view by invoking the action.
- [AccessibilityDirectTouchOptions](../accessibilitydirecttouchoptions.md) — An option set that defines the functionality of a view’s direct touch area.
- [AccessibilityZoomGestureAction](../accessibilityzoomgestureaction.md) — Position and direction information of a zoom gesture that someone performs with an assistive technology like VoiceOver.
