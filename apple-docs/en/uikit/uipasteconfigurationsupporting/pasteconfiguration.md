---
title: pasteConfiguration
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 11.0+, iPadOS 11.0+, Mac Catalyst 13.1+, visionOS 1.0+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uipasteconfigurationsupporting/pasteconfiguration
source_url: 'https://developer.apple.com/documentation/uikit/uipasteconfigurationsupporting/pasteconfiguration'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uipasteconfigurationsupporting/pasteconfiguration.json'
content_hash: 'sha256:55ab8c595fdd4e0a'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIPasteConfigurationSupporting](../uipasteconfigurationsupporting.md)

# pasteConfiguration

<sub>Instance Property</sub>

The paste configuration associated with the responder object.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
@NSCopying var pasteConfiguration: UIPasteConfiguration? { get set }
```

## Discussion

If the responder object doesn’t have a paste configuration, `nil` is returned.
