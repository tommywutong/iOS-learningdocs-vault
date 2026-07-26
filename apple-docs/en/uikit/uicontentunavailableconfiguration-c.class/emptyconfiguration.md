---
title: emptyConfiguration
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [iOS 17.0+, iPadOS 17.0+, Mac Catalyst 17.0+, tvOS 17.0+, visionOS 1.0+]
languages: [occ, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uicontentunavailableconfiguration-c.class/emptyconfiguration
source_url: 'https://developer.apple.com/documentation/uikit/uicontentunavailableconfiguration-c.class/emptyconfiguration'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uicontentunavailableconfiguration-c.class/emptyconfiguration.json'
content_hash: 'sha256:1d61de120397b078'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIContentUnavailableConfiguration](../uicontentunavailableconfiguration-c.class.md)

# emptyConfiguration

<sub>Type Method</sub>

Creates a configuration ready to customize.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS</sub>

```objc
+ (instancetype) emptyConfiguration;
```

## Return Value

A new configuration.

## Discussion

Use this method to create a new configuration to customize. This is useful if your empty content doesn’t fit the uses covered by configurations available with [searchConfiguration](searchconfiguration.md) or [loadingConfiguration](loadingconfiguration.md).
