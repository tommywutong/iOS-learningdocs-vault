---
title: AnimationCompletionCriteria
framework: SwiftUI
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 17.0+, iPadOS 17.0+, Mac Catalyst 17.0+, macOS 14.0+, tvOS 17.0+, visionOS 1.0+, watchOS 10.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/animationcompletioncriteria
source_url: 'https://developer.apple.com/documentation/swiftui/animationcompletioncriteria'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/animationcompletioncriteria.json'
content_hash: 'sha256:ef568fa2d269659b'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [SwiftUI](../swiftui.md)

# AnimationCompletionCriteria

<sub>Structure</sub>

The criteria that determines when an animation is considered finished.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
struct AnimationCompletionCriteria
```

## Relationships

- **Conforms To**: [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md)

## Topics

### Getting the completion criteria

- [logicallyComplete](animationcompletioncriteria/logicallycomplete.md) — The animation has logically completed, but may still be in its long tail.
- [removed](animationcompletioncriteria/removed.md) — The entire animation is finished and will now be removed.

## See Also

### Adding state-based animation to an action

- [withAnimation(_:_:)](<withanimation(____).md>) — Returns the result of recomputing the view’s body with the provided animation.
- [withAnimation(_:completionCriteria:_:completion:)](<withanimation(__completioncriteria___completion_).md>) — Returns the result of recomputing the view’s body with the provided animation, and runs the completion when all animations are complete.
- [Animation](animation.md) — The way a view changes over time to create a smooth visual transition from one state to another.
