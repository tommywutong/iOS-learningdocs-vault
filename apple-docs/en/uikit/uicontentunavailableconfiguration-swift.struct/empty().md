---
title: empty()
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [iOS 17.0+, iPadOS 17.0+, Mac Catalyst 17.0+, tvOS 17.0+, visionOS]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: /documentation/uikit/uicontentunavailableconfiguration-swift.struct/empty()
source_url: 'https://developer.apple.com/documentation/uikit/uicontentunavailableconfiguration-swift.struct/empty()'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uicontentunavailableconfiguration-swift.struct/empty%28%29.json'
content_hash: 'sha256:6ae4792e62817771'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIContentUnavailableConfiguration](../uicontentunavailableconfiguration-swift.struct.md)

# empty()

<sub>Type Method</sub>

Creates the default configuration for unavailable content.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
static func empty() -> UIContentUnavailableConfiguration
```

## Return Value

A new configuration.

## Discussion

Use this method to create a new configuration to customize. This is useful if your empty content doesn’t fit the uses covered by configurations available with [search()](<search().md>) or [loading()](<loading().md>).
