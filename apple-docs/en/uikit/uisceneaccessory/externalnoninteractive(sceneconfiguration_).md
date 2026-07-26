---
title: 'externalNonInteractive(sceneConfiguration:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [iOS 27.0+ beta, iPadOS 27.0+ beta]
languages: [swift, swift, swift, swift, swift, swift, occ, occ, occ, occ, occ, occ]
beta: true
deprecated: false
doc_path: '/documentation/uikit/uisceneaccessory/externalnoninteractive(sceneconfiguration:)'
source_url: 'https://developer.apple.com/documentation/uikit/uisceneaccessory/externalnoninteractive(sceneconfiguration:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uisceneaccessory/externalnoninteractive%28sceneconfiguration%3A%29.json'
content_hash: 'sha256:37af0f1621edf0d9'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UISceneAccessory](../uisceneaccessory.md)

# externalNonInteractive(sceneConfiguration:)

<sub>Type Method</sub>

Creates a new scene accessory configuration for presenting non-interactive content on an external display.

<sub>iOS, iPadOS, Mac Catalyst</sub>

```swift
class func externalNonInteractive(sceneConfiguration: UISceneConfiguration) -> Self
```

## Parameters

- `sceneConfiguration` — A scene configuration value with delegate type defined for it.

## Discussion

When the display connects, the scene accessory’s content may be presented on it.
