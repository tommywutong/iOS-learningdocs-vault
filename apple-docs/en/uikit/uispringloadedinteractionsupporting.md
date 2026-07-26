---
title: UISpringLoadedInteractionSupporting
framework: UIKit
symbol_kind: protocol
role: symbol
role_heading: Protocol
platforms: [iOS 11.0+, iPadOS 11.0+, Mac Catalyst 13.1+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uispringloadedinteractionsupporting
source_url: 'https://developer.apple.com/documentation/uikit/uispringloadedinteractionsupporting'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uispringloadedinteractionsupporting.json'
content_hash: 'sha256:52b6c974e484b9af'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [UIKit](../uikit.md)

# UISpringLoadedInteractionSupporting

<sub>Protocol</sub>

The interface that determines if an object supports a spring-loaded interaction for drag and drop activities.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
@MainActor protocol UISpringLoadedInteractionSupporting : NSObjectProtocol
```

## Relationships

- **Inherits From**: [NSObjectProtocol](../objectivec/nsobjectprotocol.md)

- **Conforming Types**: [UIAlertController](uialertcontroller.md), [UIBarButtonItem](uibarbuttonitem.md), [UIButton](uibutton.md), [UICollectionView](uicollectionview.md), [UISearchTab](uisearchtab.md), [UISegmentedControl](uisegmentedcontrol.md), [UITab](uitab.md), [UITabBar](uitabbar.md), [UITabBarItem](uitabbaritem.md), [UITabGroup](uitabgroup.md), [UITableView](uitableview.md)

## Topics

### Checking the spring-loaded interaction status

- [springLoaded](uispringloadedinteractionsupporting/isspringloaded.md) — A Boolean value that specifies whether the object is participating in spring-loaded interaction for a drag and drop activity.

## See Also

### Spring-loaded interactions

- [UISpringLoadedInteractionBehavior](uispringloadedinteractionbehavior.md) — The interface for specifying the behavior of a spring-loaded interaction.
- [UISpringLoadedInteraction](uispringloadedinteraction.md) — An interaction object for configuring and controlling spring-loaded, user-driven navigation during a drag activity.
- [UISpringLoadedInteractionContext](uispringloadedinteractioncontext.md) — The interface an object implements to provide information about a spring-loaded interaction.
- [UISpringLoadedInteractionEffect](uispringloadedinteractioneffect.md) — The interface for providing visual styling to a spring-loaded interaction based on the interaction state.
