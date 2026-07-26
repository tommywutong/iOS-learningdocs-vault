---
title: 'URL.ParseStrategy.ComponentParseStrategy.defaultValue(_:)'
framework: Foundation
symbol_kind: case
role: symbol
role_heading: Case
platforms: [iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, macOS 13.0+, tvOS 16.0+, visionOS 1.0+, watchOS 9.0+]
languages: [swift, swift, swift, swift, swift, swift, swift, swift]
beta: false
deprecated: false
doc_path: '/documentation/foundation/url/parsestrategy/componentparsestrategy/defaultvalue(_:)'
source_url: 'https://developer.apple.com/documentation/foundation/url/parsestrategy/componentparsestrategy/defaultvalue(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/url/parsestrategy/componentparsestrategy/defaultvalue%28_%3A%29.json'
content_hash: 'sha256:87bf38e152ab0f79'
translated: false
---

> Navigation: [Technologies](../../../../technologies.md) · [Foundation](../../../../foundation.md) · [URL](../../../url.md) · [ParseStrategy](../../parsestrategy.md) · [ComponentParseStrategy](../componentparsestrategy.md)

# URL.ParseStrategy.ComponentParseStrategy.defaultValue(_:)

<sub>Case</sub>

A strategy that provides a default value for a component if it’s absent in the source string.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
case defaultValue(Component)
```

## Parameters

- `Component` — A value to use in the parsed URL if the component is absent in the source string.

## See Also

### Component parse strategies

- [URL.ParseStrategy.ComponentParseStrategy.required](required.md) — A strategy that requires the presence of the associated component for parsing to succeed.
- [URL.ParseStrategy.ComponentParseStrategy.optional](optional.md) — A strategy that treats the presence of the associated component as optional.
