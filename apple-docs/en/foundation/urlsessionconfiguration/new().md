---
title: new()
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [iOS 7.0+（13.0 起废弃）, iPadOS 7.0+（13.0 起废弃）, Mac Catalyst 13.1+（13.1 起废弃）, macOS 10.9+（10.15 起废弃）, tvOS 9.0+（13.0 起废弃）, visionOS 1.0+（1.0 起废弃）, watchOS 2.0+（6.0 起废弃）]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: /documentation/foundation/urlsessionconfiguration/new()
source_url: 'https://developer.apple.com/documentation/foundation/urlsessionconfiguration/new()'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/urlsessionconfiguration/new%28%29.json'
content_hash: 'sha256:5bbafe846a386da1'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [URLSessionConfiguration](../urlsessionconfiguration.md)

# new()

<sub>Type Method</sub>

Creates an empty session configuration.

> [!warning] Deprecated
> Use [defaultSessionConfiguration](default.md) or other class methods to create instances.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
class func new() -> Self
```

## See Also

### Creating a session configuration object

- [defaultSessionConfiguration](default.md) — A default session configuration object.
- [ephemeralSessionConfiguration](ephemeral.md) — A session configuration that uses no persistent storage for caches, cookies, or credentials.
- [+ backgroundSessionConfigurationWithIdentifier:](<background(withidentifier_).md>) — Creates a session configuration object that allows HTTP and HTTPS uploads or downloads to be performed in the background.
- [- init](<init().md>) — Creates an empty session configuration. _(deprecated)_
