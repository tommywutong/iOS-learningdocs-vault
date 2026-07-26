---
title: 'flush(completionHandler:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 7.0+, iPadOS 7.0+, Mac Catalyst 13.1+, macOS 10.9+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/urlsession/flush(completionhandler:)'
source_url: 'https://developer.apple.com/documentation/foundation/urlsession/flush(completionhandler:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/urlsession/flush%28completionhandler%3A%29.json'
content_hash: 'sha256:0e2cea816ba17d90'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [URLSession](../urlsession.md)

# flush(completionHandler:)

<sub>Instance Method</sub>

Flushes cookies and credentials to disk, clears transient caches, and ensures that future requests occur on a new TCP connection.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func flush(completionHandler: @escaping @Sendable () -> Void)
```

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func flush() async
```

## Parameters

- `completionHandler` — The completion handler to call when the flush operation is complete. This handler is executed on the delegate queue.

## See Also

### Managing the session

- [- finishTasksAndInvalidate](<finishtasksandinvalidate().md>) — Invalidates the session, allowing any outstanding tasks to finish.
- [- getTasksWithCompletionHandler:](<gettaskswithcompletionhandler(__).md>) — Asynchronously calls a completion callback with all data, upload, and download tasks in a session.
- [- getAllTasksWithCompletionHandler:](<getalltasks(completionhandler_).md>) — Asynchronously calls a completion callback with all tasks in a session
- [- invalidateAndCancel](<invalidateandcancel().md>) — Cancels all outstanding tasks and then invalidates the session.
- [- resetWithCompletionHandler:](<reset(completionhandler_).md>) — Empties all cookies, caches and credential stores, removes disk files, flushes in-progress downloads to disk, and ensures that future requests occur on a new socket.
- [sessionDescription](sessiondescription.md) — An app-defined descriptive label for the session.
