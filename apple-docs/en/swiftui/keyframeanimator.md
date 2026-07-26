---
title: KeyframeAnimator
framework: SwiftUI
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 17.0+, iPadOS 17.0+, Mac Catalyst 17.0+, macOS 14.0+, tvOS 17.0+, visionOS 1.0+, watchOS 10.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/keyframeanimator
source_url: 'https://developer.apple.com/documentation/swiftui/keyframeanimator'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/keyframeanimator.json'
content_hash: 'sha256:9ed3aca63f662781'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [SwiftUI](../swiftui.md)

# KeyframeAnimator

<sub>Structure</sub>

A container that animates its content with keyframes.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
nonisolated struct KeyframeAnimator<Value, KeyframePath, Content> where Value == KeyframePath.Value, KeyframePath : Keyframes, Content : View
```

## Overview

The `content` closure updates every frame while animating, so avoid performing any expensive operations directly within `content`.

## Relationships

- **Conforms To**: [View](view.md)

## Topics

### Creating a phase animator

- [init(initialValue:repeating:content:keyframes:)](<keyframeanimator/init(initialvalue_repeating_content_keyframes_).md>) — Loops the given keyframes continuously, updating the view using the modifiers you apply in `body`.
- [init(initialValue:trigger:content:keyframes:)](<keyframeanimator/init(initialvalue_trigger_content_keyframes_).md>) — Plays the given keyframes when the given trigger value changes, updating the view using the modifiers you apply in `body`.

## See Also

### Creating keyframe-based animation

- [keyframeAnimator(initialValue:repeating:content:keyframes:)](<view/keyframeanimator(initialvalue_repeating_content_keyframes_).md>) — Loops the given keyframes continuously, updating the view using the modifiers you apply in `body`.
- [keyframeAnimator(initialValue:trigger:content:keyframes:)](<view/keyframeanimator(initialvalue_trigger_content_keyframes_).md>) — Plays the given keyframes when the given trigger value changes, updating the view using the modifiers you apply in `body`.
- [Keyframes](keyframes.md) — A type that defines changes to a value over time.
- [KeyframeTimeline](keyframetimeline.md) — A description of how a value changes over time, modeled using keyframes.
- [KeyframeTrack](keyframetrack.md) — A sequence of keyframes animating a single property of a root type.
- [KeyframeTrackContentBuilder](keyframetrackcontentbuilder.md) — The builder that creates keyframe track content from the keyframes that you define within a closure.
- [KeyframesBuilder](keyframesbuilder.md) — A builder that combines keyframe content values into a single value.
- [KeyframeTrackContent](keyframetrackcontent.md) — A group of keyframes that define an interpolation curve of an animatable value.
- [CubicKeyframe](cubickeyframe.md) — A keyframe that uses a cubic curve to smoothly interpolate between values.
- [LinearKeyframe](linearkeyframe.md) — A keyframe that uses simple linear interpolation.
- [MoveKeyframe](movekeyframe.md) — A keyframe that immediately moves to the given value without interpolating.
- [SpringKeyframe](springkeyframe.md) — A keyframe that uses a spring function to interpolate to the given value.
