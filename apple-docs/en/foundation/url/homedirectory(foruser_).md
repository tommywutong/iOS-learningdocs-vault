---
title: 'homeDirectory(forUser:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, macOS 13.0+, tvOS 16.0+, visionOS 1.0+, watchOS 9.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/foundation/url/homedirectory(foruser:)'
source_url: 'https://developer.apple.com/documentation/foundation/url/homedirectory(foruser:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/url/homedirectory%28foruser%3A%29.json'
content_hash: 'sha256:80a81556177cfdcb'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [URL](../url.md)

# homeDirectory(forUser:)

<sub>Type Method</sub>

Returns the home directory for the specified user.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
static func homeDirectory(forUser user: String) -> URL?
```

## Parameters

- `user` — The system user name for a given user.

## Return Value

The home directory for the specified user.

## See Also

### Accessing home and user directories

- [currentDirectory()](<currentdirectory().md>) — Returns the working directory of the current process.
- [homeDirectory](homedirectory.md) — The home directory for the current user.
