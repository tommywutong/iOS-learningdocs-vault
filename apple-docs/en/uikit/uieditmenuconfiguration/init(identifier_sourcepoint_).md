---
title: 'init(identifier:sourcePoint:)'
framework: UIKit
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, visionOS]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uieditmenuconfiguration/init(identifier:sourcepoint:)'
source_url: 'https://developer.apple.com/documentation/uikit/uieditmenuconfiguration/init(identifier:sourcepoint:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uieditmenuconfiguration/init%28identifier%3Asourcepoint%3A%29.json'
content_hash: 'sha256:052726bdf1eb640d'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIEditMenuConfiguration](../uieditmenuconfiguration.md)

# init(identifier:sourcePoint:)

<sub>Initializer</sub>

Initializes a new configuration with the source location you specify.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
@MainActor @preconcurrency convenience init(identifier: AnyHashable?, sourcePoint: CGPoint)
```

## Parameters

- `identifier` — The unique identifier for this configuration object.

- `sourcePoint` — The source location of the interaction.
