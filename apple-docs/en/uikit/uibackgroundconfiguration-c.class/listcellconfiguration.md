---
title: listCellConfiguration
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [iOS 18.0+, iPadOS 18.0+, Mac Catalyst 18.0+, tvOS 18.0+, visionOS 2.0+]
languages: [occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uibackgroundconfiguration-c.class/listcellconfiguration
source_url: 'https://developer.apple.com/documentation/uikit/uibackgroundconfiguration-c.class/listcellconfiguration'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uibackgroundconfiguration-c.class/listcellconfiguration.json'
content_hash: 'sha256:fb1443da42fa2f7f'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIBackgroundConfiguration](../uibackgroundconfiguration-c.class.md)

# listCellConfiguration

<sub>Type Method</sub>

Represents a generic cell background configuration that automatically adopts the style of a containing list when updated for a new configuration state, by reading the `listEnvironment` trait from the state’s trait collection. Defaults to the background configuration for a cell in a plain-style list.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS</sub>

```objc
+ (instancetype) listCellConfiguration;
```
