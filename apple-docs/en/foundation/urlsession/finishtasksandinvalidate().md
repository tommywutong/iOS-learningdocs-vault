---
title: finishTasksAndInvalidate()
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 7.0+, iPadOS 7.0+, Mac Catalyst 13.1+, macOS 10.9+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/urlsession/finishtasksandinvalidate()
source_url: 'https://developer.apple.com/documentation/foundation/urlsession/finishtasksandinvalidate()'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/urlsession/finishtasksandinvalidate%28%29.json'
content_hash: 'sha256:373f77805aba71e0'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [URLSession](../urlsession.md)

# finishTasksAndInvalidate()

<sub>Instance Method</sub>

Invalidates the session, allowing any outstanding tasks to finish.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func finishTasksAndInvalidate()
```

## Discussion

This method returns immediately without waiting for tasks to finish. Once a session is invalidated, new tasks cannot be created in the session, but existing tasks continue until completion. After the last task finishes and the session makes the last delegate call related to those tasks, the session calls the [- URLSession:didBecomeInvalidWithError:](<../urlsessiondelegate/urlsession(__didbecomeinvalidwitherror_).md>) method on its delegate, then breaks references to the delegate and callback objects. After invalidation, session objects cannot be reused.

To cancel all outstanding tasks, call [- invalidateAndCancel](<invalidateandcancel().md>) instead.

> [!important] Important
> Calling this method on the session returned by the [sharedSession](shared.md) method has no effect.

## See Also

### Managing the session

- [- flushWithCompletionHandler:](<flush(completionhandler_).md>) — Flushes cookies and credentials to disk, clears transient caches, and ensures that future requests occur on a new TCP connection.
- [- getTasksWithCompletionHandler:](<gettaskswithcompletionhandler(__).md>) — Asynchronously calls a completion callback with all data, upload, and download tasks in a session.
- [- getAllTasksWithCompletionHandler:](<getalltasks(completionhandler_).md>) — Asynchronously calls a completion callback with all tasks in a session
- [- invalidateAndCancel](<invalidateandcancel().md>) — Cancels all outstanding tasks and then invalidates the session.
- [- resetWithCompletionHandler:](<reset(completionhandler_).md>) — Empties all cookies, caches and credential stores, removes disk files, flushes in-progress downloads to disk, and ensures that future requests occur on a new socket.
- [sessionDescription](sessiondescription.md) — An app-defined descriptive label for the session.
