---
title: KeyframeTrackContentBuilder
framework: SwiftUI
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 17.0+, iPadOS 17.0+, Mac Catalyst 17.0+, macOS 14.0+, tvOS 17.0+, visionOS 1.0+, watchOS 10.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/keyframetrackcontentbuilder
source_url: 'https://developer.apple.com/documentation/swiftui/keyframetrackcontentbuilder'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/keyframetrackcontentbuilder.json'
content_hash: 'sha256:14a0d59e70d38abd'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [SwiftUI](../swiftui.md)

# KeyframeTrackContentBuilder

<sub>Structure</sub>

The builder that creates keyframe track content from the keyframes that you define within a closure.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
@resultBuilder struct KeyframeTrackContentBuilder<Value> where Value : Animatable
```

## Topics

### Building keyframe track content

- [buildArray(_:)](<keyframetrackcontentbuilder/buildarray(__).md>)
- [buildBlock()](<keyframetrackcontentbuilder/buildblock().md>)
- [buildEither(first:)](<keyframetrackcontentbuilder/buildeither(first_).md>)
- [buildEither(second:)](<keyframetrackcontentbuilder/buildeither(second_).md>)
- [buildExpression(_:)](<keyframetrackcontentbuilder/buildexpression(__).md>)
- [buildPartialBlock(accumulated:next:)](<keyframetrackcontentbuilder/buildpartialblock(accumulated_next_).md>)
- [buildPartialBlock(first:)](<keyframetrackcontentbuilder/buildpartialblock(first_).md>)
- [Conditional](keyframetrackcontentbuilder/conditional.md) — A conditional result from the result builder.

## See Also

### Creating keyframe-based animation

- [keyframeAnimator(initialValue:repeating:content:keyframes:)](<view/keyframeanimator(initialvalue_repeating_content_keyframes_).md>) — Loops the given keyframes continuously, updating the view using the modifiers you apply in `body`.
- [keyframeAnimator(initialValue:trigger:content:keyframes:)](<view/keyframeanimator(initialvalue_trigger_content_keyframes_).md>) — Plays the given keyframes when the given trigger value changes, updating the view using the modifiers you apply in `body`.
- [KeyframeAnimator](keyframeanimator.md) — A container that animates its content with keyframes.
- [Keyframes](keyframes.md) — A type that defines changes to a value over time.
- [KeyframeTimeline](keyframetimeline.md) — A description of how a value changes over time, modeled using keyframes.
- [KeyframeTrack](keyframetrack.md) — A sequence of keyframes animating a single property of a root type.
- [KeyframesBuilder](keyframesbuilder.md) — A builder that combines keyframe content values into a single value.
- [KeyframeTrackContent](keyframetrackcontent.md) — A group of keyframes that define an interpolation curve of an animatable value.
- [CubicKeyframe](cubickeyframe.md) — A keyframe that uses a cubic curve to smoothly interpolate between values.
- [LinearKeyframe](linearkeyframe.md) — A keyframe that uses simple linear interpolation.
- [MoveKeyframe](movekeyframe.md) — A keyframe that immediately moves to the given value without interpolating.
- [SpringKeyframe](springkeyframe.md) — A keyframe that uses a spring function to interpolate to the given value.
