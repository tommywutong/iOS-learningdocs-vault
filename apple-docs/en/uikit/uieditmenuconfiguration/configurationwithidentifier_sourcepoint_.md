---
title: 'configurationWithIdentifier:sourcePoint:'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, visionOS 1.0+]
languages: [occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uieditmenuconfiguration/configurationwithidentifier:sourcepoint:'
source_url: 'https://developer.apple.com/documentation/uikit/uieditmenuconfiguration/configurationwithidentifier:sourcepoint:'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uieditmenuconfiguration/configurationwithidentifier%3Asourcepoint%3A.json'
content_hash: 'sha256:48689a28954d9e59'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIEditMenuConfiguration](../uieditmenuconfiguration.md)

# configurationWithIdentifier:sourcePoint:

<sub>Type Method</sub>

Creates a new configuration with the source location you specify.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS</sub>

```objc
+ (instancetype) configurationWithIdentifier:(id<NSCopying>) identifier sourcePoint:(CGPoint) sourcePoint;
```

## Parameters

- `identifier` — The unique identifier for this configuration object.

- `sourcePoint` — The source location of the interaction.
