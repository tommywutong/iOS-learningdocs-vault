---
title: UITransitionContextViewKey
framework: UIKit
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS, iPadOS, Mac Catalyst, tvOS, visionOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uitransitioncontextviewkey
source_url: 'https://developer.apple.com/documentation/uikit/uitransitioncontextviewkey'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uitransitioncontextviewkey.json'
content_hash: 'sha256:663ae35877caf8f2'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [UIKit](../uikit.md)

# UITransitionContextViewKey

<sub>Structure</sub>

The keys you use to identify the views involved in a transition.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
struct UITransitionContextViewKey
```

## Relationships

- **Conforms To**: [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [RawRepresentable](../swift/rawrepresentable.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md)

## Topics

### Keys

- [UITransitionContextFromViewKey](uitransitioncontextviewkey/from.md) — A key that identifies the view shown at the beginning of the transition, or at the end of a canceled transition.
- [UITransitionContextToViewKey](uitransitioncontextviewkey/to.md) — A key that identifies the view shown at the end of a completed transition.

### Initializers

- [init(rawValue:)](<uitransitioncontextviewkey/init(rawvalue_).md>) — Creates a key to identify the views in a transition.

## See Also

### Constants

- [UITransitionContextViewControllerKey](uitransitioncontextviewcontrollerkey.md) — The keys you use to identify the view controllers involved in a transition.
