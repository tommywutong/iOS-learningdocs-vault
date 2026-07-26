---
title: UISceneCollectionJoinBehavior.preferred
framework: UIKit
symbol_kind: case
role: symbol
role_heading: Case
platforms: [Mac Catalyst 14.0+]
languages: [swift, swift, swift, swift, swift, swift, swift, occ, occ, occ, occ, occ, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uiscenecollectionjoinbehavior/preferred
source_url: 'https://developer.apple.com/documentation/uikit/uiscenecollectionjoinbehavior/preferred'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiscenecollectionjoinbehavior/preferred.json'
content_hash: 'sha256:e6ca99e6635e5244'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UISceneCollectionJoinBehavior](../uiscenecollectionjoinbehavior.md)

# UISceneCollectionJoinBehavior.preferred

<sub>Case</sub>

A behavior that adds the new scene to the requesting scene’s collection and activate it, or attempts to join a compatible collection.

<sub>Mac Catalyst</sub>

```swift
case preferred
```

## Discussion

If [requestingScene](../uiscene/activationrequestoptions/requestingscene.md) is set, this behavior adds the new scene to its collection and activates it. Otherwise, the scene attempts to join a compatible collection.

## See Also

### Constants

- [UISceneCollectionJoinBehaviorAutomatic](automatic.md) — A behavior that uses the system preferences for joining collections.
- [UISceneCollectionJoinBehaviorPreferredWithoutActivating](preferredwithoutactivating.md) — A behavior that adds the new scene to the requesting scene’s collection without activating it, or attempts to join a compatible collection.
- [UISceneCollectionJoinBehaviorDisallowed](disallowed.md) — A behavior that creates a new collection for the new scene, ignoring system preferences.
