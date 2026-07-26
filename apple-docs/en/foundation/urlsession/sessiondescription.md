---
title: sessionDescription
framework: Foundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 7.0+, iPadOS 7.0+, Mac Catalyst 13.1+, macOS 10.9+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/urlsession/sessiondescription
source_url: 'https://developer.apple.com/documentation/foundation/urlsession/sessiondescription'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/urlsession/sessiondescription.json'
content_hash: 'sha256:4774ba5995944dbd'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [URLSession](../urlsession.md)

# sessionDescription

<sub>Instance Property</sub>

An app-defined descriptive label for the session.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var sessionDescription: String? { get set }
```

## Discussion

This property contains a human-readable string that you can use for debugging purposes. This value may be `nil` and defaults to `nil`. The value is ignored by the session.

## See Also

### Managing the session

- [- finishTasksAndInvalidate](<finishtasksandinvalidate().md>) — Invalidates the session, allowing any outstanding tasks to finish.
- [- flushWithCompletionHandler:](<flush(completionhandler_).md>) — Flushes cookies and credentials to disk, clears transient caches, and ensures that future requests occur on a new TCP connection.
- [- getTasksWithCompletionHandler:](<gettaskswithcompletionhandler(__).md>) — Asynchronously calls a completion callback with all data, upload, and download tasks in a session.
- [- getAllTasksWithCompletionHandler:](<getalltasks(completionhandler_).md>) — Asynchronously calls a completion callback with all tasks in a session
- [- invalidateAndCancel](<invalidateandcancel().md>) — Cancels all outstanding tasks and then invalidates the session.
- [- resetWithCompletionHandler:](<reset(completionhandler_).md>) — Empties all cookies, caches and credential stores, removes disk files, flushes in-progress downloads to disk, and ensures that future requests occur on a new socket.
