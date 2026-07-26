---
title: delegate
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 10.0+, iPadOS 10.0+, Mac Catalyst 13.1+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uipreviewinteraction/delegate
source_url: 'https://developer.apple.com/documentation/uikit/uipreviewinteraction/delegate'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uipreviewinteraction/delegate.json'
content_hash: 'sha256:fb495acf0c086031'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIPreviewInteraction](../uipreviewinteraction.md)

# delegate

<sub>Instance Property</sub>

An object that acts as the delegate of the preview interaction.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
weak var delegate: (any UIPreviewInteractionDelegate)? { get set }
```

## Discussion

The preview interaction informs the delegate of state and progress changes throughout the 3D Touch process. Create an object that conforms to the [UIPreviewInteractionDelegate](../uipreviewinteractiondelegate.md) protocol and assign it to this property.

## See Also

### Preparing preview interactions

- [UIPreviewInteractionDelegate](../uipreviewinteractiondelegate.md) — A set of methods for communicating the progress of a preview interaction.
