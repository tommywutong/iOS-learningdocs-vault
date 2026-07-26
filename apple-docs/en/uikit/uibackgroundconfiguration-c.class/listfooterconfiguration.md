---
title: listFooterConfiguration
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [iOS 18.0+, iPadOS 18.0+, Mac Catalyst 18.0+, tvOS 18.0+, visionOS 2.0+]
languages: [occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uibackgroundconfiguration-c.class/listfooterconfiguration
source_url: 'https://developer.apple.com/documentation/uikit/uibackgroundconfiguration-c.class/listfooterconfiguration'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uibackgroundconfiguration-c.class/listfooterconfiguration.json'
content_hash: 'sha256:d18b9f5de786a872'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIBackgroundConfiguration](../uibackgroundconfiguration-c.class.md)

# listFooterConfiguration

<sub>Type Method</sub>

Represents a generic footer background configuration that automatically adopts the style of a containing list when updated for a new configuration state, by reading the `listEnvironment` trait from the state’s trait collection. Defaults to the background configuration for a footer in a plain-style list.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS</sub>

```objc
+ (instancetype) listFooterConfiguration;
```
