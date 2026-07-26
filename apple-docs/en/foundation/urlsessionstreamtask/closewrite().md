---
title: closeWrite()
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 9.0+, iPadOS 9.0+, Mac Catalyst 13.1+, macOS 10.11+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/urlsessionstreamtask/closewrite()
source_url: 'https://developer.apple.com/documentation/foundation/urlsessionstreamtask/closewrite()'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/urlsessionstreamtask/closewrite%28%29.json'
content_hash: 'sha256:14e8571836e83a9f'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [URLSessionStreamTask](../urlsessionstreamtask.md)

# closeWrite()

<sub>Instance Method</sub>

Completes any enqueued reads and writes, and then closes the write side of the underlying socket.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func closeWrite()
```

## Discussion

You may continue to read data using the [- readDataOfMinLength:maxLength:timeout:completionHandler:](<readdata(ofminlength_maxlength_timeout_completionhandler_).md>) method after calling this method. Any calls to [- writeData:timeout:completionHandler:](<write(__timeout_completionhandler_).md>) after calling this method will result in an error.

Because the server may continue to write bytes to the client, it is recommended that you continue reading until the stream reaches end-of-file (EOF).

## See Also

### Closing read and write sockets

- [- closeRead](<closeread().md>) — Completes any enqueued reads and writes, and then closes the read side of the underlying socket.
