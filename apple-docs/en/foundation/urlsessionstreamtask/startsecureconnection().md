---
title: startSecureConnection()
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 9.0+, iPadOS 9.0+, Mac Catalyst 13.1+, macOS 10.11+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/urlsessionstreamtask/startsecureconnection()
source_url: 'https://developer.apple.com/documentation/foundation/urlsessionstreamtask/startsecureconnection()'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/urlsessionstreamtask/startsecureconnection%28%29.json'
content_hash: 'sha256:b3bc6244f16bd1cf'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [URLSessionStreamTask](../urlsessionstreamtask.md)

# startSecureConnection()

<sub>Instance Method</sub>

Completes any enqueued reads and writes, and establishes a secure connection.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func startSecureConnection()
```

## Discussion

Authentication callbacks are sent to the session’s delegate using the [- URLSession:task:didReceiveChallenge:completionHandler:](<../urlsessiontaskdelegate/urlsession(__task_didreceive_completionhandler_).md>) method.

## See Also

### Starting and stopping secure connections

- [- stopSecureConnection](<stopsecureconnection().md>) — Completes any enqueued reads and writes, and closes the secure connection. _(deprecated)_
