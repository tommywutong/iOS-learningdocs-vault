---
title: stopSecureConnection()
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 7.0+（13.0 起废弃）, iPadOS 7.0+（13.0 起废弃）, Mac Catalyst 13.1+（13.1 起废弃）, macOS 10.9+（10.15 起废弃）, tvOS 9.0+（13.0 起废弃）, visionOS 1.0+（1.0 起废弃）, watchOS 2.0+（6.0 起废弃）]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: /documentation/foundation/urlsessionstreamtask/stopsecureconnection()
source_url: 'https://developer.apple.com/documentation/foundation/urlsessionstreamtask/stopsecureconnection()'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/urlsessionstreamtask/stopsecureconnection%28%29.json'
content_hash: 'sha256:112b791ff2ce4ec8'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [URLSessionStreamTask](../urlsessionstreamtask.md)

# stopSecureConnection()

<sub>Instance Method</sub>

Completes any enqueued reads and writes, and closes the secure connection.

> [!warning] Deprecated
> TLS cannot be disabled once it is enabled

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func stopSecureConnection()
```

## See Also

### Starting and stopping secure connections

- [- startSecureConnection](<startsecureconnection().md>) — Completes any enqueued reads and writes, and establishes a secure connection.
