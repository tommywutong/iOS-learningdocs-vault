---
title: invalidateAndCancel()
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 7.0+, iPadOS 7.0+, Mac Catalyst 13.1+, macOS 10.9+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/urlsession/invalidateandcancel()
source_url: 'https://developer.apple.com/documentation/foundation/urlsession/invalidateandcancel()'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/urlsession/invalidateandcancel%28%29.json'
content_hash: 'sha256:fbb71114736cd50d'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [URLSession](../urlsession.md)

# invalidateAndCancel()

<sub>Instance Method</sub>

Cancels all outstanding tasks and then invalidates the session.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func invalidateAndCancel()
```

## Discussion

Once invalidated, references to the delegate and callback objects are broken. After invalidation, session objects cannot be reused.

To allow outstanding tasks to run until completion, call [- finishTasksAndInvalidate](<finishtasksandinvalidate().md>) instead.

> [!important] Important
> Calling this method on the session returned by the [sharedSession](shared.md) method has no effect.

## See Also

### Managing the session

- [- finishTasksAndInvalidate](<finishtasksandinvalidate().md>) — Invalidates the session, allowing any outstanding tasks to finish.
- [- flushWithCompletionHandler:](<flush(completionhandler_).md>) — Flushes cookies and credentials to disk, clears transient caches, and ensures that future requests occur on a new TCP connection.
- [- getTasksWithCompletionHandler:](<gettaskswithcompletionhandler(__).md>) — Asynchronously calls a completion callback with all data, upload, and download tasks in a session.
- [- getAllTasksWithCompletionHandler:](<getalltasks(completionhandler_).md>) — Asynchronously calls a completion callback with all tasks in a session
- [- resetWithCompletionHandler:](<reset(completionhandler_).md>) — Empties all cookies, caches and credential stores, removes disk files, flushes in-progress downloads to disk, and ensures that future requests occur on a new socket.
- [sessionDescription](sessiondescription.md) — An app-defined descriptive label for the session.
