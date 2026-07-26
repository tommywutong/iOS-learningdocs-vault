---
title: 'init(scheme:user:password:host:port:path:query:fragment:)'
framework: Foundation
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, macOS 13.0+, tvOS 16.0+, visionOS 1.0+, watchOS 9.0+]
languages: [swift, swift, swift]
beta: false
deprecated: false
doc_path: '/documentation/foundation/url/formatstyle/init(scheme:user:password:host:port:path:query:fragment:)'
source_url: 'https://developer.apple.com/documentation/foundation/url/formatstyle/init(scheme:user:password:host:port:path:query:fragment:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/url/formatstyle/init%28scheme%3Auser%3Apassword%3Ahost%3Aport%3Apath%3Aquery%3Afragment%3A%29.json'
content_hash: 'sha256:d5454a8614025d15'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [Foundation](../../../foundation.md) · [URL](../../url.md) · [FormatStyle](../formatstyle.md)

# init(scheme:user:password:host:port:path:query:fragment:)

<sub>Initializer</sub>

Creates a URL format style with the given display options.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
init(scheme: URL.FormatStyle.ComponentDisplayOption = .always, user: URL.FormatStyle.ComponentDisplayOption = .never, password: URL.FormatStyle.ComponentDisplayOption = .never, host: URL.FormatStyle.HostDisplayOption = .always, port: URL.FormatStyle.ComponentDisplayOption = .omitIfHTTPFamily, path: URL.FormatStyle.ComponentDisplayOption = .always, query: URL.FormatStyle.ComponentDisplayOption = .never, fragment: URL.FormatStyle.ComponentDisplayOption = .never)
```

## Parameters

- `scheme` — An option to control display of the URL scheme component.

- `user` — An option to control display of the URL user component.

- `password` — An option to control display of the URL password component.

- `host` — An option to control display of the URL host component.

- `port` — An option to control display of the URL port component.

- `path` — An option to control display of the URL path component.

- `query` — An option to control display of the URL query component.

- `fragment` — An option to control display of the URL fragment component.

## Discussion

Explicitly create a URL format style in situations where you want to format multiple URLs with the same style configuration. For one-time use, call [formatted()](<../formatted().md>) for a default style, or create a style with [url](../../formatstyle/url.md) and customize it with the modifiers in Customizing style behavior.

## See Also

### Creating a URL format style

- [ComponentDisplayOption](componentdisplayoption.md) — A type that indicates whether a formatted URL should include a component.
- [HostDisplayOption](hostdisplayoption.md) — A type that indicates whether a formatted URL should include the host component.
