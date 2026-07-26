---
title: contentSelectionViewController
framework: AVKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [visionOS 2.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/avkit/avmultiviewmanager/contentselectionviewcontroller
source_url: 'https://developer.apple.com/documentation/avkit/avmultiviewmanager/contentselectionviewcontroller'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avkit/avmultiviewmanager/contentselectionviewcontroller.json'
content_hash: 'sha256:97c5d46e40e83262'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVKit](../../avkit.md) · [AVMultiviewManager](../avmultiviewmanager.md)

# contentSelectionViewController

<sub>Instance Property</sub>

A view controller that presents a user interface to select additional video content to display.

<sub>visionOS</sub>

```swift
@MainActor final var contentSelectionViewController: AVContentSelectionViewController? { get set }
```

## Discussion

Implement this property to add custom user interface elements. The primary role of this interface is to provide a way for users to add additional videos.

## See Also

### Providing additional UI

- [AVContentSelectionViewController](../avcontentselectionviewcontroller.md) — A view controller for providing additional UI to the multiview experience.
