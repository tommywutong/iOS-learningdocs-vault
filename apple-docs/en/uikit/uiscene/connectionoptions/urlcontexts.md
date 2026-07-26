---
title: urlContexts
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.1+, tvOS 13.0+, visionOS 1.0+]
languages: [swift, swift, swift, swift, swift, swift, occ, occ, occ, occ, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uiscene/connectionoptions/urlcontexts
source_url: 'https://developer.apple.com/documentation/uikit/uiscene/connectionoptions/urlcontexts'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiscene/connectionoptions/urlcontexts.json'
content_hash: 'sha256:3db9146f701489ff'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [UIKit](../../../uikit.md) · [UIScene](../../uiscene.md) · [ConnectionOptions](../connectionoptions.md)

# urlContexts

<sub>Instance Property</sub>

The URLs to open, along with metadata specifying how to open them.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
var urlContexts: Set<UIOpenURLContext> { get }
```

## Discussion

An empty set indicates that there are no URLs to open.
