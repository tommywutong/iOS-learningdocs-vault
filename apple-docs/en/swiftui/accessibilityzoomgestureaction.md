---
title: AccessibilityZoomGestureAction
framework: SwiftUI
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, macOS 13.0+, tvOS 16.0+, visionOS 1.0+, watchOS 9.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/accessibilityzoomgestureaction
source_url: 'https://developer.apple.com/documentation/swiftui/accessibilityzoomgestureaction'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/accessibilityzoomgestureaction.json'
content_hash: 'sha256:c042fe1aa5e8515f'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [SwiftUI](../swiftui.md)

# AccessibilityZoomGestureAction

<sub>Structure</sub>

Position and direction information of a zoom gesture that someone performs with an assistive technology like VoiceOver.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
struct AccessibilityZoomGestureAction
```

## Topics

### Getting the action’s direction

- [direction](accessibilityzoomgestureaction/direction-swift.property.md) — The zoom gesture’s direction.
- [Direction](accessibilityzoomgestureaction/direction-swift.enum.md) — A direction that matches the movement of a zoom gesture performed by an assistive technology, such as a swipe up and down in Voiceover’s zoom rotor.

### Getting location information

- [location](accessibilityzoomgestureaction/location.md) — The zoom gesture’s activation point, normalized to the accessibility element’s frame.
- [point](accessibilityzoomgestureaction/point.md) — The zoom gesture’s activation point within the window’s coordinate space.

## See Also

### Making gestures accessible

- [accessibilityActivationPoint(_:)](<view/accessibilityactivationpoint(__).md>) — The activation point for an element is the location assistive technologies use to initiate gestures.
- [accessibilityActivationPoint(_:isEnabled:)](<view/accessibilityactivationpoint(__isenabled_).md>) — The activation point for an element is the location assistive technologies use to initiate gestures.
- [accessibilityDragPoint(_:description:)](<view/accessibilitydragpoint(__description_).md>) — The point an assistive technology should use to begin a drag interaction.
- [accessibilityDragPoint(_:description:isEnabled:)](<view/accessibilitydragpoint(__description_isenabled_).md>) — The point an assistive technology should use to begin a drag interaction.
- [accessibilityDropPoint(_:description:)](<view/accessibilitydroppoint(__description_).md>) — The point an assistive technology should use to end a drag interaction.
- [accessibilityDropPoint(_:description:isEnabled:)](<view/accessibilitydroppoint(__description_isenabled_).md>) — The point an assistive technology should use to end a drag interaction.
- [accessibilityDirectTouch(_:options:)](<view/accessibilitydirecttouch(__options_).md>) — Explicitly set whether this accessibility element is a direct touch area. Direct touch areas passthrough touch events to the app rather than being handled through an assistive technology, such as VoiceOver. The modifier accepts an optional `AccessibilityDirectTouchOptions` option set to customize the functionality of the direct touch area.
- [accessibilityZoomAction(_:)](<view/accessibilityzoomaction(__).md>) — Adds an accessibility zoom action to the view. Actions allow assistive technologies, such as VoiceOver, to interact with the view by invoking the action.
- [AccessibilityDirectTouchOptions](accessibilitydirecttouchoptions.md) — An option set that defines the functionality of a view’s direct touch area.
