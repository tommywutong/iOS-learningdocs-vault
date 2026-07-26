---
title: 'getAllTasks(completionHandler:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 9.0+, iPadOS 9.0+, Mac Catalyst 13.1+, macOS 10.11+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/urlsession/getalltasks(completionhandler:)'
source_url: 'https://developer.apple.com/documentation/foundation/urlsession/getalltasks(completionhandler:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/urlsession/getalltasks%28completionhandler%3A%29.json'
content_hash: 'sha256:ad83cfe1f554096f'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [URLSession](../urlsession.md)

# getAllTasks(completionHandler:)

<sub>Instance Method</sub>

Asynchronously calls a completion callback with all tasks in a session

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func getAllTasks(completionHandler: @escaping @Sendable ([URLSessionTask]) -> Void)
```

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var allTasks: [URLSessionTask] { get async }
```

## Parameters

- `completionHandler` — The completion handler to call with the list of tasks.

## See Also

### Managing the session

- [- finishTasksAndInvalidate](<finishtasksandinvalidate().md>) — Invalidates the session, allowing any outstanding tasks to finish.
- [- flushWithCompletionHandler:](<flush(completionhandler_).md>) — Flushes cookies and credentials to disk, clears transient caches, and ensures that future requests occur on a new TCP connection.
- [- getTasksWithCompletionHandler:](<gettaskswithcompletionhandler(__).md>) — Asynchronously calls a completion callback with all data, upload, and download tasks in a session.
- [- invalidateAndCancel](<invalidateandcancel().md>) — Cancels all outstanding tasks and then invalidates the session.
- [- resetWithCompletionHandler:](<reset(completionhandler_).md>) — Empties all cookies, caches and credential stores, removes disk files, flushes in-progress downloads to disk, and ensures that future requests occur on a new socket.
- [sessionDescription](sessiondescription.md) — An app-defined descriptive label for the session.
