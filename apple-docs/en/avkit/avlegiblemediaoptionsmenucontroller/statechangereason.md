---
title: AVLegibleMediaOptionsMenuController.StateChangeReason
framework: AVKit
symbol_kind: enum
role: symbol
role_heading: Enumeration
platforms: [iOS 26.4+, iPadOS 26.4+, Mac Catalyst 26.4+, macOS 26.4+, visionOS 26.4+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avkit/avlegiblemediaoptionsmenucontroller/statechangereason
source_url: 'https://developer.apple.com/documentation/avkit/avlegiblemediaoptionsmenucontroller/statechangereason'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avkit/avlegiblemediaoptionsmenucontroller/statechangereason.json'
content_hash: 'sha256:5f3a1ce2a98af83b'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVKit](../../avkit.md) · [AVLegibleMediaOptionsMenuController](../avlegiblemediaoptionsmenucontroller.md)

# AVLegibleMediaOptionsMenuController.StateChangeReason

<sub>Enumeration</sub>

<sub>iOS, iPadOS, Mac Catalyst, macOS, visionOS</sub>

```swift
enum StateChangeReason
```

## Overview

```
		An enum set, describing the different reasons for changing the menu state.
```

```
		Describes a non specified menu state change reason.
```

```
		Describes a menu state change reason due language mismatch.
```

## Relationships

- **Conforms To**: [BitwiseCopyable](../../swift/bitwisecopyable.md), [Equatable](../../swift/equatable.md), [Hashable](../../swift/hashable.md), [RawRepresentable](../../swift/rawrepresentable.md), [Sendable](../../swift/sendable.md), [SendableMetatype](../../swift/sendablemetatype.md)

## Topics

### Creating a reason

- [init(rawValue:)](<statechangereason/init(rawvalue_).md>)

### Reasons

- [AVLegibleMediaOptionsMenuStateChangeReasonNone](statechangereason/none.md)
- [AVLegibleMediaOptionsMenuStateChangeReasonLanguageMismatch](statechangereason/languagemismatch.md)

## See Also

### Managing the menu

- [- menuWithContents:](<menu(contents_).md>)
- [menuState](menustate.md)
- [MenuContents](menucontents.md)
- [AVLegibleMediaOptionsMenuState](../avlegiblemediaoptionsmenustate.md)
