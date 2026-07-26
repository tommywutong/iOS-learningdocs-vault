---
title: 'scheme(_:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, macOS 13.0+, tvOS 16.0+, visionOS 1.0+, watchOS 9.0+]
languages: [swift, swift, swift]
beta: false
deprecated: false
doc_path: '/documentation/foundation/url/formatstyle/scheme(_:)'
source_url: 'https://developer.apple.com/documentation/foundation/url/formatstyle/scheme(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/url/formatstyle/scheme%28_%3A%29.json'
content_hash: 'sha256:336dcc955700d397'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [Foundation](../../../foundation.md) · [URL](../../url.md) · [FormatStyle](../formatstyle.md)

# scheme(_:)

<sub>Instance Method</sub>

Modifies a format style to display a URL’s scheme component in accordance with the provided option.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func scheme(_ strategy: URL.FormatStyle.ComponentDisplayOption = .always) -> URL.FormatStyle
```

## Parameters

- `strategy` — A component display option that indicates when, if ever, to display the scheme.

## Return Value

A modified [FormatStyle](../formatstyle.md) that incorporates the specified behavior.

## See Also

### Customizing style behavior

- [user(_:)](<user(__).md>) — Modifies a format style to display a URL’s user component in accordance with the provided option.
- [password(_:)](<password(__).md>) — Modifies a format style to display a URL’s password component in accordance with the provided option.
- [host(_:)](<host(__).md>) — Modifies a format style to display a URL’s host component in accordance with the provided option.
- [HostDisplayOption](hostdisplayoption.md) — A type that indicates whether a formatted URL should include the host component.
- [port(_:)](<port(__).md>) — Modifies a format style to display a URL’s port component in accordance with the provided option.
- [path(_:)](<path(__).md>) — Modifies a format style to display a URL’s path component in accordance with the provided option.
- [query(_:)](<query(__).md>) — Modifies a format style to display a URL’s query component in accordance with the provided option.
- [fragment(_:)](<fragment(__).md>) — Modifies a format style to display a URL’s fragment component in accordance with the provided option.
- [ComponentDisplayOption](componentdisplayoption.md) — A type that indicates whether a formatted URL should include a component.
