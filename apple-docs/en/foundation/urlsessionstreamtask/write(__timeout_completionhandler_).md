---
title: 'write(_:timeout:completionHandler:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 9.0+, iPadOS 9.0+, Mac Catalyst 13.1+, macOS 10.11+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/urlsessionstreamtask/write(_:timeout:completionhandler:)'
source_url: 'https://developer.apple.com/documentation/foundation/urlsessionstreamtask/write(_:timeout:completionhandler:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/urlsessionstreamtask/write%28_%3Atimeout%3Acompletionhandler%3A%29.json'
content_hash: 'sha256:2c91e038fc92aca9'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [URLSessionStreamTask](../urlsessionstreamtask.md)

# write(_:timeout:completionHandler:)

<sub>Instance Method</sub>

Asynchronously writes the specified data to the stream, and calls a handler upon completion.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func write(_ data: Data, timeout: TimeInterval, completionHandler: @escaping @Sendable ((any Error)?) -> Void)
```

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func write(_ data: Data, timeout: TimeInterval) async throws
```

## Parameters

- `data` — The data to be written.

- `timeout` — A timeout for writing bytes. If the write is not completed within the specified interval, the write is canceled and the `completionHandler` is called with an error. Pass `0` to prevent a write from timing out.

- `completionHandler` — The completion handler to call when all bytes are written, or an error occurs. This handler is executed on the delegate queue. This completion handler takes the following parameter: - **`error`** — An error object that indicates why the write failed, or `nil` if the write was successful.

## Discussion

There is no guarantee that the remote side of the stream has received all of the written bytes at the time that `completionHandler` is called, only that all of the data has been written to the kernel.

## See Also

### Reading and writing data

- [- readDataOfMinLength:maxLength:timeout:completionHandler:](<readdata(ofminlength_maxlength_timeout_completionhandler_).md>) — Asynchronously reads a number of bytes from the stream, and calls a handler upon completion.
