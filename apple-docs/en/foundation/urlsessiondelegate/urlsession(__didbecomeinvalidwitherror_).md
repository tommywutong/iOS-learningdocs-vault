---
title: 'urlSession(_:didBecomeInvalidWithError:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 7.0+, iPadOS 7.0+, Mac Catalyst 13.1+, macOS 10.9+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/urlsessiondelegate/urlsession(_:didbecomeinvalidwitherror:)'
source_url: 'https://developer.apple.com/documentation/foundation/urlsessiondelegate/urlsession(_:didbecomeinvalidwitherror:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/urlsessiondelegate/urlsession%28_%3Adidbecomeinvalidwitherror%3A%29.json'
content_hash: 'sha256:77ee4d6b1b05cdb4'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [URLSessionDelegate](../urlsessiondelegate.md)

# urlSession(_:didBecomeInvalidWithError:)

<sub>Instance Method</sub>

Tells the URL session that the session has been invalidated.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
optional func urlSession(_ session: URLSession, didBecomeInvalidWithError error: (any Error)?)
```

## Parameters

- `session` — The session object that was invalidated.

- `error` — The error that caused invalidation, or `nil` if the invalidation was explicit.

## Discussion

If you invalidate a session by calling its [- finishTasksAndInvalidate](<../urlsession/finishtasksandinvalidate().md>) method, the session waits until after the final task in the session finishes or fails before calling this delegate method. If you call the [- invalidateAndCancel](<../urlsession/invalidateandcancel().md>) method, the session calls this delegate method immediately.

## See Also

### Handling session life cycle changes

- [- URLSessionDidFinishEventsForBackgroundURLSession:](<urlsessiondidfinishevents(forbackgroundurlsession_).md>) — Tells the delegate that all messages enqueued for a session have been delivered.
