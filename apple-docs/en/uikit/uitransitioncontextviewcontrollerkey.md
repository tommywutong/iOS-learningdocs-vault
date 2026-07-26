---
title: UITransitionContextViewControllerKey
framework: UIKit
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS, iPadOS, Mac Catalyst, tvOS, visionOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uitransitioncontextviewcontrollerkey
source_url: 'https://developer.apple.com/documentation/uikit/uitransitioncontextviewcontrollerkey'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uitransitioncontextviewcontrollerkey.json'
content_hash: 'sha256:194a5d598f619a7c'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [UIKit](../uikit.md)

# UITransitionContextViewControllerKey

<sub>Structure</sub>

The keys you use to identify the view controllers involved in a transition.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
struct UITransitionContextViewControllerKey
```

## Relationships

- **Conforms To**: [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [RawRepresentable](../swift/rawrepresentable.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md)

## Topics

### Keys

- [UITransitionContextFromViewControllerKey](uitransitioncontextviewcontrollerkey/from.md) — A key that identifies the view controller that’s visible at the beginning of the transition, or at the end of a canceled transition.
- [UITransitionContextToViewControllerKey](uitransitioncontextviewcontrollerkey/to.md) — A key that identifies the view controller that’s visible at the end of a completed transition.

### Initializers

- [init(rawValue:)](<uitransitioncontextviewcontrollerkey/init(rawvalue_).md>) — Creates a key to identify the view controllers in a transition.

## See Also

### Constants

- [UITransitionContextViewKey](uitransitioncontextviewkey.md) — The keys you use to identify the views involved in a transition.
