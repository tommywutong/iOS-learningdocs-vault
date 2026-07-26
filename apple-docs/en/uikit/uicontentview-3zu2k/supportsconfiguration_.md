---
title: 'supportsConfiguration:'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, tvOS 16.0+, visionOS 1.0+]
languages: [occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uicontentview-3zu2k/supportsconfiguration:'
source_url: 'https://developer.apple.com/documentation/uikit/uicontentview-3zu2k/supportsconfiguration:'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uicontentview-3zu2k/supportsconfiguration%3A.json'
content_hash: 'sha256:29cf99d883b90a57'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIContentView](../uicontentview-3zu2k.md)

# supportsConfiguration:

<sub>Instance Method</sub>

Determines whether the view is compatible with the provided configuration.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS</sub>

```objc
- (BOOL) supportsConfiguration:(id<UIContentConfiguration>) configuration;
```

## Parameters

- `configuration` — The new configuration to test for compatibility.

## Return Value

[true](../../swift/true.md) if the view supports this configuration being set to its [configuration](configuration.md) property and is capable of updating itself for the configuration; otherwise, [false](../../swift/false.md).

## Discussion

The default implementation assumes the view is compatible with configuration classes that match the class of the view’s existing configuration.
