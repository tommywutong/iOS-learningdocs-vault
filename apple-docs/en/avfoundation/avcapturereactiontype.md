---
title: AVCaptureReactionType
framework: AVFoundation
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 17.0+, iPadOS 17.0+, Mac Catalyst 17.0+, macOS 14.0+, tvOS 17.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avcapturereactiontype
source_url: 'https://developer.apple.com/documentation/avfoundation/avcapturereactiontype'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avcapturereactiontype.json'
content_hash: 'sha256:7e76132471775067'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [AVFoundation](../avfoundation.md)

# AVCaptureReactionType

<sub>Structure</sub>

Constants that indicate the type of reaction that an effect can perform.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS</sub>

```swift
struct AVCaptureReactionType
```

## Relationships

- **Conforms To**: [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [RawRepresentable](../swift/rawrepresentable.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md)

## Topics

### Reaction types

- [AVCaptureReactionTypeBalloons](avcapturereactiontype/balloons.md) — A reaction that displays balloons rising through the scene.
- [AVCaptureReactionTypeConfetti](avcapturereactiontype/confetti.md) — A reaction that displays festive spots of color falling through the scene.
- [AVCaptureReactionTypeFireworks](avcapturereactiontype/fireworks.md) — A reaction that displays fireworks bursting in the background.
- [AVCaptureReactionTypeHeart](avcapturereactiontype/heart.md) — A reaction that displays one or more heart symbols.
- [AVCaptureReactionTypeLasers](avcapturereactiontype/lasers.md) — A reaction that displays a bright laser show projecting into the scene.
- [AVCaptureReactionTypeRain](avcapturereactiontype/rain.md) — A reaction that displays a dark and stormy night.
- [AVCaptureReactionTypeThumbsUp](avcapturereactiontype/thumbsup.md) — A reaction that displays a thumbs-up symbol.
- [AVCaptureReactionTypeThumbsDown](avcapturereactiontype/thumbsdown.md) — A reaction that displays a thumbs-down symbol.

### Accessing the system image name

- [AVCaptureReactionSystemImageNameForType](avcapturereactiontype/systemimagename.md) — Returns the name of a system image that displays the recommended iconography for a specified reaction type.

### Initializers

- [init(rawValue:)](<avcapturereactiontype/init(rawvalue_).md>) — Creates a reaction type with a string value.

## See Also

### Configuring the effect state

- [reactionType](avcapturereactioneffectstate/reactiontype.md) — The type of reaction.
- [startTime](avcapturereactioneffectstate/starttime.md) — The presentation time of the first frame where the system renders the effect.
- [endTime](avcapturereactioneffectstate/endtime.md) — The presentation time of the first frame following the end of a reaction effect.
