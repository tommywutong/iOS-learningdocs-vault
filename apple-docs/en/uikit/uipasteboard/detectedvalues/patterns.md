---
title: patterns
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, visionOS]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/uikit/uipasteboard/detectedvalues/patterns
source_url: 'https://developer.apple.com/documentation/uikit/uipasteboard/detectedvalues/patterns'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uipasteboard/detectedvalues/patterns.json'
content_hash: 'sha256:4a974d78f977c435'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [UIKit](../../../uikit.md) · [UIPasteboard](../../uipasteboard.md) · [DetectedValues](../detectedvalues.md)

# patterns

<sub>Instance Property</sub>

A set of key paths that represent patterns that the data detection system identifies.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
var patterns: Set<PartialKeyPath<UIPasteboard.DetectedValues>> { get }
```

## See Also

### Detected patterns

- [probableWebSearch](probablewebsearch.md) — A string that the data detection system identifies as a probable web search item.
- [probableWebURL](probableweburl.md) — A string that the data detection system identifies as a probable web URL.
