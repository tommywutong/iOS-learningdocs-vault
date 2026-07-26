---
title: 'getTasksWithCompletionHandler(_:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 7.0+, iPadOS 7.0+, Mac Catalyst 13.1+, macOS 10.9+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/urlsession/gettaskswithcompletionhandler(_:)'
source_url: 'https://developer.apple.com/documentation/foundation/urlsession/gettaskswithcompletionhandler(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/urlsession/gettaskswithcompletionhandler%28_%3A%29.json'
content_hash: 'sha256:dba2ed400354c337'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [URLSession](../urlsession.md)

# getTasksWithCompletionHandler(_:)

<sub>Instance Method</sub>

Asynchronously calls a completion callback with all data, upload, and download tasks in a session.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func getTasksWithCompletionHandler(_ completionHandler: @escaping @Sendable ([URLSessionDataTask], [URLSessionUploadTask], [URLSessionDownloadTask]) -> Void)
```

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var tasks: ([URLSessionDataTask], [URLSessionUploadTask], [URLSessionDownloadTask]) { get async }
```

## Parameters

- `completionHandler` — The completion handler to call with the list of tasks. This handler is executed on the delegate queue.

## Discussion

The arrays passed to the completion handler contain any tasks that you have created within the session, not including any tasks that have been invalidated after completing, failing, or being cancelled.

## See Also

### Managing the session

- [- finishTasksAndInvalidate](<finishtasksandinvalidate().md>) — Invalidates the session, allowing any outstanding tasks to finish.
- [- flushWithCompletionHandler:](<flush(completionhandler_).md>) — Flushes cookies and credentials to disk, clears transient caches, and ensures that future requests occur on a new TCP connection.
- [- getAllTasksWithCompletionHandler:](<getalltasks(completionhandler_).md>) — Asynchronously calls a completion callback with all tasks in a session
- [- invalidateAndCancel](<invalidateandcancel().md>) — Cancels all outstanding tasks and then invalidates the session.
- [- resetWithCompletionHandler:](<reset(completionhandler_).md>) — Empties all cookies, caches and credential stores, removes disk files, flushes in-progress downloads to disk, and ensures that future requests occur on a new socket.
- [sessionDescription](sessiondescription.md) — An app-defined descriptive label for the session.
