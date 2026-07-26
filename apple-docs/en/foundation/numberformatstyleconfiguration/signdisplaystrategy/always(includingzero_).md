---
title: 'always(includingZero:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, macOS 12.0+, tvOS 15.0+, visionOS 1.0+, watchOS 8.0+]
languages: [swift, swift, swift, swift, swift, swift, swift, swift, swift, swift, swift, swift, swift, swift, swift, swift, swift, swift, swift, swift]
beta: false
deprecated: false
doc_path: '/documentation/foundation/numberformatstyleconfiguration/signdisplaystrategy/always(includingzero:)'
source_url: 'https://developer.apple.com/documentation/foundation/numberformatstyleconfiguration/signdisplaystrategy/always(includingzero:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/numberformatstyleconfiguration/signdisplaystrategy/always%28includingzero%3A%29.json'
content_hash: 'sha256:48b6e75ae7a1ab77'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [Foundation](../../../foundation.md) · [NumberFormatStyleConfiguration](../../numberformatstyleconfiguration.md) · [SignDisplayStrategy](../signdisplaystrategy.md)

# always(includingZero:)

<sub>Type Method</sub>

A strategy to always display sign symbols.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
static func always(includingZero: Bool = true) -> NumberFormatStyleConfiguration.SignDisplayStrategy
```

## Parameters

- `includingZero` — A Boolean value that determines whether the format style should apply sign characters to zero values. Defaults to `true`.

## Return Value

A strategy to always display sign symbols, with the given behavior for zero values.

## See Also

### Sign display strategies

- [automatic](automatic.md) — A strategy to automatically configure locale-appropriate sign display behavior.
- [never](never.md) — A strategy to never display sign symbols.
