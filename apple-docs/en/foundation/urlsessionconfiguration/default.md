---
title: default
framework: Foundation
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 7.0+, iPadOS 7.0+, Mac Catalyst 13.1+, macOS 10.9+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/urlsessionconfiguration/default
source_url: 'https://developer.apple.com/documentation/foundation/urlsessionconfiguration/default'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/urlsessionconfiguration/default.json'
content_hash: 'sha256:36ad1be676d1f437'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [URLSessionConfiguration](../urlsessionconfiguration.md)

# default

<sub>Type Property</sub>

A default session configuration object.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
class var `default`: URLSessionConfiguration { get }
```

## Discussion

The default session configuration uses a persistent disk-based cache (except when the result is downloaded to a file) and stores credentials in the user’s keychain. It also stores cookies (by default) in the same shared cookie store as the [NSURLConnection](../nsurlconnection.md) and [NSURLDownload](../nsurldownload.md) classes.

> [!note] Note
> If you’re porting code based on the [NSURLConnection](../nsurlconnection.md) class, use this method to obtain an initial configuration object and then customize that object as needed.

Modifying the returned session configuration object does _not_ affect any configuration objects returned by future calls to this method, and does not change the default behavior for existing sessions. It is therefore always safe to use the returned object as a starting point for additional customization.

## See Also

### Related Documentation

- [Fetching website data into memory](../fetching-website-data-into-memory.md) — Receive data directly into memory by creating a data task from a URL session.

### Creating a session configuration object

- [ephemeralSessionConfiguration](ephemeral.md) — A session configuration that uses no persistent storage for caches, cookies, or credentials.
- [+ backgroundSessionConfigurationWithIdentifier:](<background(withidentifier_).md>) — Creates a session configuration object that allows HTTP and HTTPS uploads or downloads to be performed in the background.
- [- init](<init().md>) — Creates an empty session configuration. _(deprecated)_
- [+ new](<new().md>) — Creates an empty session configuration. _(deprecated)_
