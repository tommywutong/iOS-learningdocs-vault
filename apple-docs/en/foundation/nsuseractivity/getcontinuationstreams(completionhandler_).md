---
title: 'getContinuationStreams(completionHandler:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.1+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/nsuseractivity/getcontinuationstreams(completionhandler:)'
source_url: 'https://developer.apple.com/documentation/foundation/nsuseractivity/getcontinuationstreams(completionhandler:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsuseractivity/getcontinuationstreams%28completionhandler%3A%29.json'
content_hash: 'sha256:a0051e856fd8dd8e'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSUserActivity](../nsuseractivity.md)

# getContinuationStreams(completionHandler:)

<sub>Instance Method</sub>

Requests streams back to the originating app.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func getContinuationStreams(completionHandler: @escaping @Sendable (InputStream?, OutputStream?, (any Error)?) -> Void)
```

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func continuationStreams() async throws -> (InputStream, OutputStream)
```

## Parameters

- `completionHandler` — The completion handler block that returns streams. The block takes three arguments: - **`inputStream`** — The stream from which the continuing app can read data written by the originating app. - **`outputStream`** — The stream to which the continuing app writes data to be read by the originating app. - **`error`** — If successful, `nil`; if not successful, an [NSError](../nserror.md) object that encapsulates the reason why the streams could not be created.

## Discussion

When an app is launched for a continuation event, it can request streams back to the originating app. Streams can be successfully retrieved only from the [NSUserActivity](../nsuseractivity.md) object in the [NSApplication](../../appkit/nsapplication.md) or [UIApplication](../../uikit/uiapplication.md) delegate that is called for a continuation event. The streams are provided by the completion handler in an unopened state, and the delegate should open them immediately to start communicating with the continuing side.

Continuation streams are an optional feature of Handoff, and most user activities do not need them for successful continuation. When streams are needed, a simple request from the continuing app accompanied by a response from the originating app is enough for most continuation events.

## See Also

### Working with continuation streams

- [supportsContinuationStreams](supportscontinuationstreams.md) — A Boolean value that determines whether the continuing app can request streams to be opened back to the originating app.
