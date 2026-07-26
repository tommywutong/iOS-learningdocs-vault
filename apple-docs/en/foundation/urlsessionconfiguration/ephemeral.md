---
title: ephemeral
framework: Foundation
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 7.0+, iPadOS 7.0+, Mac Catalyst 13.1+, macOS 10.9+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/urlsessionconfiguration/ephemeral
source_url: 'https://developer.apple.com/documentation/foundation/urlsessionconfiguration/ephemeral'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/urlsessionconfiguration/ephemeral.json'
content_hash: 'sha256:6f3c79491b0c77ea'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [URLSessionConfiguration](../urlsessionconfiguration.md)

# ephemeral

<sub>Type Property</sub>

A session configuration that uses no persistent storage for caches, cookies, or credentials.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
class var ephemeral: URLSessionConfiguration { get }
```

## Discussion

An ephemeral session configuration object is similar to a default session configuration (see [defaultSessionConfiguration](default.md)), except that the corresponding session object doesn’t store caches, credential stores, or any session-related data to disk. Instead, session-related data is stored in RAM. The only time an ephemeral session writes data to disk is when you tell it to write the contents of a URL to a file.

> [!note] Note
> It is possible to customize a default session configuration object to obtain the same behavior (or any portion thereof) provided by an ephemeral session configuration object, but the use of this method is more convenient.

### Privacy and performance considerations

The main advantage to using ephemeral sessions is privacy. By not writing potentially sensitive data to disk, you make it less likely that the data will be intercepted and used later. For this reason, ephemeral sessions are ideal for private browsing modes in web browsers and other similar situations.

Because an ephemeral session doesn’t write cached data to disk, the size of the cache is limited by available RAM. This limitation means that previously fetched resources are less likely to be in the cache (and are guaranteed to not be there if the user quits and relaunches your app). This behavior may reduce perceived performance, depending on your app.

When your app invalidates the session, all ephemeral session data is purged automatically. Additionally, in iOS, the in-memory cache isn’t purged automatically when your app is suspended but may be purged when your app is terminated or when the system experiences memory pressure.

## See Also

### Related Documentation

- [discretionary](isdiscretionary.md) — A Boolean value that determines whether background tasks can be scheduled at the discretion of the system for optimal performance.

### Creating a session configuration object

- [defaultSessionConfiguration](default.md) — A default session configuration object.
- [+ backgroundSessionConfigurationWithIdentifier:](<background(withidentifier_).md>) — Creates a session configuration object that allows HTTP and HTTPS uploads or downloads to be performed in the background.
- [- init](<init().md>) — Creates an empty session configuration. _(deprecated)_
- [+ new](<new().md>) — Creates an empty session configuration. _(deprecated)_
