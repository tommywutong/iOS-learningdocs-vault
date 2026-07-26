---
title: footerConfiguration
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [iOS 18.0+, iPadOS 18.0+, Mac Catalyst 18.0+, tvOS 18.0+, visionOS 2.0+]
languages: [occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uilistcontentconfiguration-c.class/footerconfiguration
source_url: 'https://developer.apple.com/documentation/uikit/uilistcontentconfiguration-c.class/footerconfiguration'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uilistcontentconfiguration-c.class/footerconfiguration.json'
content_hash: 'sha256:0ab9ced04f4f0af1'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIListContentConfiguration](../uilistcontentconfiguration-c.class.md)

# footerConfiguration

<sub>Type Method</sub>

Represents a generic footer configuration that automatically adopts the style of a containing list when updating for a new configuration state, by reading the `listEnvironment` trait from the state’s trait collection. Defaults to the footer configuration for a plain-style list.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS</sub>

```objc
+ (instancetype) footerConfiguration;
```
