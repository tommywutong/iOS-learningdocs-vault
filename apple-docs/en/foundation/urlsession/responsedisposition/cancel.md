---
title: URLSession.ResponseDisposition.cancel
framework: Foundation
symbol_kind: case
role: symbol
role_heading: Case
platforms: [iOS 7.0+, iPadOS 7.0+, Mac Catalyst 13.1+, macOS 10.9+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/urlsession/responsedisposition/cancel
source_url: 'https://developer.apple.com/documentation/foundation/urlsession/responsedisposition/cancel'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/urlsession/responsedisposition/cancel.json'
content_hash: 'sha256:18beb961eb03f1a8'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [Foundation](../../../foundation.md) · [URLSession](../../urlsession.md) · [ResponseDisposition](../responsedisposition.md)

# URLSession.ResponseDisposition.cancel

<sub>Case</sub>

Cancel the load.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
case cancel
```

## Discussion

Using this disposition is equivalent to calling [- cancel](<../../urlsessiontask/cancel().md>) on the task.

## See Also

### Task dispositions

- [NSURLSessionResponseAllow](allow.md) — Allow the load operation to continue.
- [NSURLSessionResponseBecomeDownload](becomedownload.md) — Convert the response for this request to use a [URLSessionDownloadTask](../../urlsessiondownloadtask.md).
- [NSURLSessionResponseBecomeStream](becomestream.md) — Convert the response for this request to use a [URLSessionStreamTask](../../urlsessionstreamtask.md).
