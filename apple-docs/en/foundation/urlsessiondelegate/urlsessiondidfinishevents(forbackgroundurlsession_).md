---
title: 'urlSessionDidFinishEvents(forBackgroundURLSession:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 7.0+, iPadOS 7.0+, Mac Catalyst 13.1+, macOS 11.0+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/urlsessiondelegate/urlsessiondidfinishevents(forbackgroundurlsession:)'
source_url: 'https://developer.apple.com/documentation/foundation/urlsessiondelegate/urlsessiondidfinishevents(forbackgroundurlsession:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/urlsessiondelegate/urlsessiondidfinishevents%28forbackgroundurlsession%3A%29.json'
content_hash: 'sha256:de203b6888737eef'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [URLSessionDelegate](../urlsessiondelegate.md)

# urlSessionDidFinishEvents(forBackgroundURLSession:)

<sub>Instance Method</sub>

Tells the delegate that all messages enqueued for a session have been delivered.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
optional func urlSessionDidFinishEvents(forBackgroundURLSession session: URLSession)
```

## Parameters

- `session` — The session that no longer has any outstanding requests.

## Discussion

In iOS, when a background transfer completes or requires credentials, if your app is no longer running, your app is automatically relaunched in the background, and the app’s `UIApplicationDelegate` is sent an [application(_:handleEventsForBackgroundURLSession:completionHandler:)](<../../uikit/uiapplicationdelegate/application(__handleeventsforbackgroundurlsession_completionhandler_).md>) message. This call contains the identifier of the session that caused your app to be launched. You should then store that completion handler before creating a background configuration object with the same identifier, and creating a session with that configuration. The newly created session is automatically reassociated with ongoing background activity.

When your app later receives a [- URLSessionDidFinishEventsForBackgroundURLSession:](<urlsessiondidfinishevents(forbackgroundurlsession_).md>) message, this indicates that all messages previously enqueued for this session have been delivered, and that it is now safe to invoke the previously stored completion handler or to begin any internal updates that may result in invoking the completion handler.

> [!important] Important
> Because the provided completion handler is part of UIKit, you must call it on your main thread.

## See Also

### Handling session life cycle changes

- [- URLSession:didBecomeInvalidWithError:](<urlsession(__didbecomeinvalidwitherror_).md>) — Tells the URL session that the session has been invalidated.
