---
title: 'init(scheme:user:password:host:port:path:query:fragment:)'
framework: Foundation
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, macOS 13.0+, tvOS 16.0+, visionOS 1.0+, watchOS 9.0+]
languages: [swift, swift, swift, swift]
beta: false
deprecated: false
doc_path: '/documentation/foundation/url/parsestrategy/init(scheme:user:password:host:port:path:query:fragment:)'
source_url: 'https://developer.apple.com/documentation/foundation/url/parsestrategy/init(scheme:user:password:host:port:path:query:fragment:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/url/parsestrategy/init%28scheme%3Auser%3Apassword%3Ahost%3Aport%3Apath%3Aquery%3Afragment%3A%29.json'
content_hash: 'sha256:2642205d2a48b290'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [Foundation](../../../foundation.md) · [URL](../../url.md) · [ParseStrategy](../parsestrategy.md)

# init(scheme:user:password:host:port:path:query:fragment:)

<sub>Initializer</sub>

Creates a URL parse strategy with the specified component-parsing behaviors.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
init(scheme: URL.ParseStrategy.ComponentParseStrategy<String> = .required, user: URL.ParseStrategy.ComponentParseStrategy<String> = .optional, password: URL.ParseStrategy.ComponentParseStrategy<String> = .optional, host: URL.ParseStrategy.ComponentParseStrategy<String> = .required, port: URL.ParseStrategy.ComponentParseStrategy<Int> = .optional, path: URL.ParseStrategy.ComponentParseStrategy<String> = .optional, query: URL.ParseStrategy.ComponentParseStrategy<String> = .optional, fragment: URL.ParseStrategy.ComponentParseStrategy<String> = .optional)
```

## Parameters

- `scheme` — A strategy for parsing the scheme component.

- `user` — A strategy for parsing the user component.

- `password` — A strategy for parsing the password component.

- `host` — A strategy for parsing the host component.

- `port` — A strategy for parsing the port component.

- `path` — A strategy for parsing the path component.

- `query` — A strategy for parsing the query component.

- `fragment` — A strategy for parsing the fragment component.

## See Also

### Creating a URL parse strategy

- [ComponentParseStrategy](componentparsestrategy.md) — The strategy used to parse one component of a URL.
