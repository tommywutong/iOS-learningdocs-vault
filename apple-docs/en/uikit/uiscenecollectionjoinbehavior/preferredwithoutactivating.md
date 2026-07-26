---
title: UISceneCollectionJoinBehavior.preferredWithoutActivating
framework: UIKit
symbol_kind: case
role: symbol
role_heading: Case
platforms: [Mac Catalyst 14.0+]
languages: [swift, swift, swift, swift, swift, swift, swift, occ, occ, occ, occ, occ, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uiscenecollectionjoinbehavior/preferredwithoutactivating
source_url: 'https://developer.apple.com/documentation/uikit/uiscenecollectionjoinbehavior/preferredwithoutactivating'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiscenecollectionjoinbehavior/preferredwithoutactivating.json'
content_hash: 'sha256:7846e33ec430808a'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UISceneCollectionJoinBehavior](../uiscenecollectionjoinbehavior.md)

# UISceneCollectionJoinBehavior.preferredWithoutActivating

<sub>Case</sub>

A behavior that adds the new scene to the requesting scene’s collection without activating it, or attempts to join a compatible collection.

<sub>Mac Catalyst</sub>

```swift
case preferredWithoutActivating
```

## Discussion

If [requestingScene](../uiscene/activationrequestoptions/requestingscene.md) is set, this behavior adds the new scene without deactivating the [requestingScene](../uiscene/activationrequestoptions/requestingscene.md). Otherwise, this behavior behaves the same as [UISceneCollectionJoinBehaviorPreferred](preferred.md). For example, in apps built with Mac Catalyst, you can use this behavior to open a link in a new tab in the background.

## See Also

### Constants

- [UISceneCollectionJoinBehaviorAutomatic](automatic.md) — A behavior that uses the system preferences for joining collections.
- [UISceneCollectionJoinBehaviorPreferred](preferred.md) — A behavior that adds the new scene to the requesting scene’s collection and activate it, or attempts to join a compatible collection.
- [UISceneCollectionJoinBehaviorDisallowed](disallowed.md) — A behavior that creates a new collection for the new scene, ignoring system preferences.
