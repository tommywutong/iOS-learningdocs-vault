---
title: 'host(_:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, macOS 13.0+, tvOS 16.0+, visionOS 1.0+, watchOS 9.0+]
languages: [swift, swift, swift, swift]
beta: false
deprecated: false
doc_path: '/documentation/foundation/url/parsestrategy/host(_:)'
source_url: 'https://developer.apple.com/documentation/foundation/url/parsestrategy/host(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/url/parsestrategy/host%28_%3A%29.json'
content_hash: 'sha256:886dee0fc5fe8fd8'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [Foundation](../../../foundation.md) · [URL](../../url.md) · [ParseStrategy](../parsestrategy.md)

# host(_:)

<sub>Instance Method</sub>

Modifies a parse strategy to parse a URL’s host component in accordance with the provided behavior.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func host(_ strategy: URL.ParseStrategy.ComponentParseStrategy<String> = .required) -> URL.ParseStrategy
```

## Parameters

- `strategy` — A strategy for parsing the host component.

## Return Value

A modified [ParseStrategy](../parsestrategy.md) that incorporates the specified behavior.

## See Also

### Customizing strategy behavior

- [scheme(_:)](<scheme(__).md>) — Modifies a parse strategy to parse a URL’s scheme component in accordance with the provided behavior.
- [user(_:)](<user(__).md>) — Modifies a parse strategy to parse a URL’s user component in accordance with the provided behavior.
- [password(_:)](<password(__).md>) — Modifies a parse strategy to parse a URL’s password component in accordance with the provided behavior.
- [port(_:)](<port(__).md>) — Modifies a parse strategy to parse a URL’s port component in accordance with the provided behavior.
- [path(_:)](<path(__).md>) — Modifies a parse strategy to parse a URL’s path component in accordance with the provided behavior.
- [query(_:)](<query(__).md>) — Modifies a parse strategy to parse a URL’s query component in accordance with the provided behavior.
- [fragment(_:)](<fragment(__).md>) — Modifies a parse strategy to parse a URL’s fragment component in accordance with the provided behavior.
- [ComponentParseStrategy](componentparsestrategy.md) — The strategy used to parse one component of a URL.
