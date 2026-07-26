---
title: URLSessionDataDelegate
framework: Foundation
symbol_kind: protocol
role: symbol
role_heading: Protocol
platforms: [iOS 7.0+, iPadOS 7.0+, Mac Catalyst 13.1+, macOS 10.9+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/urlsessiondatadelegate
source_url: 'https://developer.apple.com/documentation/foundation/urlsessiondatadelegate'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/urlsessiondatadelegate.json'
content_hash: 'sha256:83cd45ddeb295d7c'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Foundation](../foundation.md)

# URLSessionDataDelegate

<sub>Protocol</sub>

A protocol that defines methods that URL session instances call on their delegates to handle task-level events specific to data and upload tasks.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
protocol URLSessionDataDelegate : URLSessionTaskDelegate
```

## Overview

Your session delegate should also implement the methods in the [URLSessionTaskDelegate](urlsessiontaskdelegate.md) protocol to handle task-level events that are common to all task types, and methods in the [URLSessionDelegate](urlsessiondelegate.md) protocol to handle session-level events.

> [!note] Note
> A [URLSession](urlsession.md) object need not have a delegate. If no delegate is assigned, when you create tasks in that session, you must provide a completion handler block to obtain the data.
>
> Completion handler blocks are primarily intended as an alternative to using a custom delegate. If you create a task using a method that takes a completion handler block, the delegate methods for response and data delivery are not called.

## Relationships

- **Inherits From**: [NSObjectProtocol](../objectivec/nsobjectprotocol.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md), [URLSessionDelegate](urlsessiondelegate.md), [URLSessionTaskDelegate](urlsessiontaskdelegate.md)

## Topics

### Handling task life cycle changes

- [- URLSession:dataTask:didReceiveResponse:completionHandler:](<urlsessiondatadelegate/urlsession(__datatask_didreceive_completionhandler_).md>) — Tells the delegate that the data task received the initial reply (headers) from the server.
- [ResponseDisposition](urlsession/responsedisposition.md) — Constants indicating how a data or upload session should proceed after receiving the initial headers.
- [- URLSession:dataTask:didBecomeDownloadTask:](<urlsessiondatadelegate/urlsession(__datatask_didbecome_)-60op5.md>) — Tells the delegate that the data task was changed to a download task.
- [- URLSession:dataTask:didBecomeStreamTask:](<urlsessiondatadelegate/urlsession(__datatask_didbecome_)-7nqzu.md>) — Tells the delegate that the data task was changed to a stream task.

### Receiving data

- [- URLSession:dataTask:didReceiveData:](<urlsessiondatadelegate/urlsession(__datatask_didreceive_).md>) — Tells the delegate that the data task has received some of the expected data.

### Handling caching

- [- URLSession:dataTask:willCacheResponse:completionHandler:](<urlsessiondatadelegate/urlsession(__datatask_willcacheresponse_completionhandler_).md>) — Asks the delegate whether the data (or upload) task should store the response in the cache.

## See Also

### Adding data tasks to a session

- [- dataTaskWithURL:](<urlsession/datatask(with_)-10dy7.md>) — Creates a task that retrieves the contents of the specified URL.
- [- dataTaskWithURL:completionHandler:](<urlsession/datatask(with_completionhandler_)-52wk8.md>) — Creates a task that retrieves the contents of the specified URL, then calls a handler upon completion.
- [- dataTaskWithRequest:](<urlsession/datatask(with_)-7jpys.md>) — Creates a task that retrieves the contents of a URL based on the specified URL request object.
- [- dataTaskWithRequest:completionHandler:](<urlsession/datatask(with_completionhandler_)-e6xv.md>) — Creates a task that retrieves the contents of a URL based on the specified URL request object, and calls a handler upon completion.
- [URLSessionDataTask](urlsessiondatatask.md) — A URL session task that returns downloaded data directly to the app in memory.
