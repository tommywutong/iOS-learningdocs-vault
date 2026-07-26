---
title: 'userActivity(_:didReceive:outputStream:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.1+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 3.0+]
languages: [swift, swift, swift, swift, occ, occ, occ, occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/nsuseractivitydelegate/useractivity(_:didreceive:outputstream:)'
source_url: 'https://developer.apple.com/documentation/foundation/nsuseractivitydelegate/useractivity(_:didreceive:outputstream:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsuseractivitydelegate/useractivity%28_%3Adidreceive%3Aoutputstream%3A%29.json'
content_hash: 'sha256:b956b6f543826a4e'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSUserActivityDelegate](../nsuseractivitydelegate.md)

# userActivity(_:didReceive:outputStream:)

<sub>Instance Method</sub>

Notifies the user activity delegate that an input and output streams are available to open.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
optional func userActivity(_ userActivity: NSUserActivity, didReceive inputStream: InputStream, outputStream: OutputStream)
```

## Parameters

- `userActivity` — The user activity that is continuing on another device. This user activity’s [supportsContinuationStreams](../nsuseractivity/supportscontinuationstreams.md) property must be [true](../../swift/true.md).

- `inputStream` — The stream from which the originating app can read data written from the continuing app.

- `outputStream` — The stream to which the originating app writes data to be read by the continuing app.

## Discussion

If [supportsContinuationStreams](../nsuseractivity/supportscontinuationstreams.md) is [true](../../swift/true.md), the continuing app can request streams back to the originating app. This delegate callback is received with the streams from the continuing side. The streams are provided in an unopened state, and the delegate should open them immediately to start communicating with the continuing side.

Continuation streams are an optional feature of Handoff, and most user activities do not need them for successful continuation. When streams are needed, a simple request from the continuing app accompanied by a response from the originating app is enough for most continuation events.

## See Also

### Related Documentation

- [Handoff Programming Guide](https://developer.apple.com/library/archive/documentation/UserExperience/Conceptual/Handoff/HandoffFundamentals/HandoffFundamentals.html#//apple_ref/doc/uid/TP40014338)
