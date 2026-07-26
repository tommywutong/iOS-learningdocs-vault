---
title: 'readData(ofMinLength:maxLength:timeout:completionHandler:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 9.0+, iPadOS 9.0+, Mac Catalyst 13.1+, macOS 10.11+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/urlsessionstreamtask/readdata(ofminlength:maxlength:timeout:completionhandler:)'
source_url: 'https://developer.apple.com/documentation/foundation/urlsessionstreamtask/readdata(ofminlength:maxlength:timeout:completionhandler:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/urlsessionstreamtask/readdata%28ofminlength%3Amaxlength%3Atimeout%3Acompletionhandler%3A%29.json'
content_hash: 'sha256:f87efbe381e89f02'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [URLSessionStreamTask](../urlsessionstreamtask.md)

# readData(ofMinLength:maxLength:timeout:completionHandler:)

<sub>Instance Method</sub>

Asynchronously reads a number of bytes from the stream, and calls a handler upon completion.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func readData(ofMinLength minBytes: Int, maxLength maxBytes: Int, timeout: TimeInterval, completionHandler: @escaping @Sendable (Data?, Bool, (any Error)?) -> Void)
```

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func readData(ofMinLength minBytes: Int, maxLength maxBytes: Int, timeout: TimeInterval) async throws -> (Data?, Bool)
```

## Parameters

- `minBytes` — The minimum number of bytes to read.

- `maxBytes` — The maximum number of bytes to read.

- `timeout` — A timeout for reading bytes. If the read is not completed within the specified interval, the read is canceled and the `completionHandler` is called with an error. Pass `0` to prevent a read from timing out.

- `completionHandler` — The completion handler to call when all bytes are read, or an error occurs. This handler is executed on the delegate queue. This completion handler takes the following parameters: - **`data`** — The data read from the stream. - **`atEOF`** — Whether or not the stream reached end-of-file (EOF), such that no more data can be read. - **`error`** — An error object that indicates why the read failed, or `nil` if the read was successful.

## See Also

### Reading and writing data

- [- writeData:timeout:completionHandler:](<write(__timeout_completionhandler_).md>) — Asynchronously writes the specified data to the stream, and calls a handler upon completion.
