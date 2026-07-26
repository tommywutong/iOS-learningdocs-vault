---
title: UISceneCollectionJoinBehavior
framework: UIKit
symbol_kind: enum
role: symbol
role_heading: Enumeration
platforms: [Mac Catalyst 14.0+]
languages: [swift, swift, swift, swift, swift, swift, swift, occ, occ, occ, occ, occ, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uiscenecollectionjoinbehavior
source_url: 'https://developer.apple.com/documentation/uikit/uiscenecollectionjoinbehavior'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiscenecollectionjoinbehavior.json'
content_hash: 'sha256:2c8175fe3e958dd9'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [UIKit](../uikit.md)

# UISceneCollectionJoinBehavior

<sub>Enumeration</sub>

A set of behaviors that specify how a new scene joins a scene collection.

<sub>Mac Catalyst</sub>

```swift
enum UISceneCollectionJoinBehavior
```

## Relationships

- **Conforms To**: [BitwiseCopyable](../swift/bitwisecopyable.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [RawRepresentable](../swift/rawrepresentable.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md)

## Topics

### Constants

- [UISceneCollectionJoinBehaviorAutomatic](uiscenecollectionjoinbehavior/automatic.md) — A behavior that uses the system preferences for joining collections.
- [UISceneCollectionJoinBehaviorPreferred](uiscenecollectionjoinbehavior/preferred.md) — A behavior that adds the new scene to the requesting scene’s collection and activate it, or attempts to join a compatible collection.
- [UISceneCollectionJoinBehaviorPreferredWithoutActivating](uiscenecollectionjoinbehavior/preferredwithoutactivating.md) — A behavior that adds the new scene to the requesting scene’s collection without activating it, or attempts to join a compatible collection.
- [UISceneCollectionJoinBehaviorDisallowed](uiscenecollectionjoinbehavior/disallowed.md) — A behavior that creates a new collection for the new scene, ignoring system preferences.

### Initializers

- [init(rawValue:)](<uiscenecollectionjoinbehavior/init(rawvalue_).md>)

## See Also

### Specifying collection join behavior

- [collectionJoinBehavior](uiscene/activationrequestoptions/collectionjoinbehavior.md) — The behavior that specifies how a new scene joins a scene collection.
