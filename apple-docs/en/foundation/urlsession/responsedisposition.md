---
title: URLSession.ResponseDisposition
framework: Foundation
symbol_kind: enum
role: symbol
role_heading: Enumeration
platforms: [iOS 7.0+, iPadOS 7.0+, Mac Catalyst 13.1+, macOS 10.9+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/urlsession/responsedisposition
source_url: 'https://developer.apple.com/documentation/foundation/urlsession/responsedisposition'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/urlsession/responsedisposition.json'
content_hash: 'sha256:e3569953ea0ddf44'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [URLSession](../urlsession.md)

# URLSession.ResponseDisposition

<sub>Enumeration</sub>

Constants indicating how a data or upload session should proceed after receiving the initial headers.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
enum ResponseDisposition
```

## Overview

When a data or upload task first receives a response, it calls the  [- URLSession:dataTask:didReceiveResponse:completionHandler:](<../urlsessiondatadelegate/urlsession(__datatask_didreceive_completionhandler_).md>) method of [URLSessionDataDelegate](../urlsessiondatadelegate.md). Implement this method to inspect the received [URLResponse](../urlresponse.md) and then call the provided completion handler. The first parameter to the completion handler is of this type, a disposition that tells the task how to proceed.

## Relationships

- **Conforms To**: [BitwiseCopyable](../../swift/bitwisecopyable.md), [Equatable](../../swift/equatable.md), [Hashable](../../swift/hashable.md), [RawRepresentable](../../swift/rawrepresentable.md), [Sendable](../../swift/sendable.md), [SendableMetatype](../../swift/sendablemetatype.md)

## Topics

### Task dispositions

- [NSURLSessionResponseCancel](responsedisposition/cancel.md) — Cancel the load.
- [NSURLSessionResponseAllow](responsedisposition/allow.md) — Allow the load operation to continue.
- [NSURLSessionResponseBecomeDownload](responsedisposition/becomedownload.md) — Convert the response for this request to use a [URLSessionDownloadTask](../urlsessiondownloadtask.md).
- [NSURLSessionResponseBecomeStream](responsedisposition/becomestream.md) — Convert the response for this request to use a [URLSessionStreamTask](../urlsessionstreamtask.md).

### Initializers

- [init(rawValue:)](<responsedisposition/init(rawvalue_).md>)

## See Also

### Handling task life cycle changes

- [- URLSession:dataTask:didReceiveResponse:completionHandler:](<../urlsessiondatadelegate/urlsession(__datatask_didreceive_completionhandler_).md>) — Tells the delegate that the data task received the initial reply (headers) from the server.
- [- URLSession:dataTask:didBecomeDownloadTask:](<../urlsessiondatadelegate/urlsession(__datatask_didbecome_)-60op5.md>) — Tells the delegate that the data task was changed to a download task.
- [- URLSession:dataTask:didBecomeStreamTask:](<../urlsessiondatadelegate/urlsession(__datatask_didbecome_)-7nqzu.md>) — Tells the delegate that the data task was changed to a stream task.
