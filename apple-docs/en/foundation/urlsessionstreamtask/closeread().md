---
title: closeRead()
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 9.0+, iPadOS 9.0+, Mac Catalyst 13.1+, macOS 10.11+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/urlsessionstreamtask/closeread()
source_url: 'https://developer.apple.com/documentation/foundation/urlsessionstreamtask/closeread()'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/urlsessionstreamtask/closeread%28%29.json'
content_hash: 'sha256:a84af1b7250a91fe'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [URLSessionStreamTask](../urlsessionstreamtask.md)

# closeRead()

<sub>Instance Method</sub>

Completes any enqueued reads and writes, and then closes the read side of the underlying socket.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func closeRead()
```

## Discussion

You may continue to write data using the [- writeData:timeout:completionHandler:](<write(__timeout_completionhandler_).md>) method after calling this method. Any calls to [- readDataOfMinLength:maxLength:timeout:completionHandler:](<readdata(ofminlength_maxlength_timeout_completionhandler_).md>) after calling this method will result in an error.

## See Also

### Closing read and write sockets

- [- closeWrite](<closewrite().md>) — Completes any enqueued reads and writes, and then closes the write side of the underlying socket.
