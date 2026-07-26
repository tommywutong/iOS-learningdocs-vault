---
title: 'accessibilityActivationPoint(_:isEnabled:)'
framework: SwiftUI
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 18.0+, iPadOS 18.0+, Mac Catalyst 18.0+, macOS 15.0+, tvOS 18.0+, visionOS 2.0+, watchOS 11.0+]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/view/accessibilityactivationpoint(_:isenabled:)'
source_url: 'https://developer.apple.com/documentation/swiftui/view/accessibilityactivationpoint(_:isenabled:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/view/accessibilityactivationpoint%28_%3Aisenabled%3A%29.json'
content_hash: 'sha256:685dc4023481d6ae'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [View](../view.md)

# accessibilityActivationPoint(_:isEnabled:)

<sub>Instance Method</sub>

The activation point for an element is the location assistive technologies use to initiate gestures.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
nonisolated func accessibilityActivationPoint(_ activationPoint: CGPoint, isEnabled: Bool) -> ModifiedContent<Self, AccessibilityAttachmentModifier>
```

## Parameters

- `activationPoint` — The accessibility activation point to apply.

- `isEnabled` — If true the accessibility activation point is applied; otherwise the accessibility activation point is unchanged.

## Discussion

Use this modifier to ensure that the activation point for a small element remains accurate even if you present a larger version of the element to VoiceOver.

If an activation point is not provided, an activation point will be derived from one of the accessibility elements decedents or from the center of the accessibility frame.

## See Also

### Making gestures accessible

- [accessibilityActivationPoint(_:)](<accessibilityactivationpoint(__).md>) — The activation point for an element is the location assistive technologies use to initiate gestures.
- [accessibilityDragPoint(_:description:)](<accessibilitydragpoint(__description_).md>) — The point an assistive technology should use to begin a drag interaction.
- [accessibilityDragPoint(_:description:isEnabled:)](<accessibilitydragpoint(__description_isenabled_).md>) — The point an assistive technology should use to begin a drag interaction.
- [accessibilityDropPoint(_:description:)](<accessibilitydroppoint(__description_).md>) — The point an assistive technology should use to end a drag interaction.
- [accessibilityDropPoint(_:description:isEnabled:)](<accessibilitydroppoint(__description_isenabled_).md>) — The point an assistive technology should use to end a drag interaction.
- [accessibilityDirectTouch(_:options:)](<accessibilitydirecttouch(__options_).md>) — Explicitly set whether this accessibility element is a direct touch area. Direct touch areas passthrough touch events to the app rather than being handled through an assistive technology, such as VoiceOver. The modifier accepts an optional `AccessibilityDirectTouchOptions` option set to customize the functionality of the direct touch area.
- [accessibilityZoomAction(_:)](<accessibilityzoomaction(__).md>) — Adds an accessibility zoom action to the view. Actions allow assistive technologies, such as VoiceOver, to interact with the view by invoking the action.
- [AccessibilityDirectTouchOptions](../accessibilitydirecttouchoptions.md) — An option set that defines the functionality of a view’s direct touch area.
- [AccessibilityZoomGestureAction](../accessibilityzoomgestureaction.md) — Position and direction information of a zoom gesture that someone performs with an assistive technology like VoiceOver.
