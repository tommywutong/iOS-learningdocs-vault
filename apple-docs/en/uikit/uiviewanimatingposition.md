---
title: UIViewAnimatingPosition
framework: UIKit
symbol_kind: enum
role: symbol
role_heading: Enumeration
platforms: [iOS 10.0+, iPadOS 10.0+, Mac Catalyst 13.1+, tvOS 10.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uiviewanimatingposition
source_url: 'https://developer.apple.com/documentation/uikit/uiviewanimatingposition'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiviewanimatingposition.json'
content_hash: 'sha256:7d55a18098282f50'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [UIKit](../uikit.md)

# UIViewAnimatingPosition

<sub>Enumeration</sub>

Constants indicating positions within the animation.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
enum UIViewAnimatingPosition
```

## Relationships

- **Conforms To**: [BitwiseCopyable](../swift/bitwisecopyable.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [RawRepresentable](../swift/rawrepresentable.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md)

## Topics

### Constants

- [UIViewAnimatingPositionEnd](uiviewanimatingposition/end.md) — The end point of the animation. Use this constant when you want the final values for any animatable properties—that is, you want to refer to the values you specified in your animation blocks.
- [UIViewAnimatingPositionStart](uiviewanimatingposition/start.md) — The beginning of the animation. Use this constant when you want the starting values for any animatable properties—that is, the values of the properties before you applied any animations.
- [UIViewAnimatingPositionCurrent](uiviewanimatingposition/current.md) — The current position. Use this constant when you want the most recent value set by an animator object.

### Initializers

- [init(rawValue:)](<uiviewanimatingposition/init(rawvalue_).md>)

## See Also

### Constants

- [UIViewAnimatingState](uiviewanimatingstate.md) — Constants indicating the current state of the animation.
