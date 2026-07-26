---
title: 'init(configuration:delegate:delegateQueue:)'
framework: Foundation
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 7.0+, iPadOS 7.0+, Mac Catalyst 13.1+, macOS 10.9+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/urlsession/init(configuration:delegate:delegatequeue:)'
source_url: 'https://developer.apple.com/documentation/foundation/urlsession/init(configuration:delegate:delegatequeue:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/urlsession/init%28configuration%3Adelegate%3Adelegatequeue%3A%29.json'
content_hash: 'sha256:c77509965296f41c'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [URLSession](../urlsession.md)

# init(configuration:delegate:delegateQueue:)

<sub>Initializer</sub>

Creates a session with the specified session configuration, delegate, and operation queue.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
init(configuration: URLSessionConfiguration, delegate: (any URLSessionDelegate)?, delegateQueue queue: OperationQueue?)
```

## Parameters

- `configuration` — A configuration object that specifies certain behaviors, such as caching policies, timeouts, proxies, pipelining, TLS versions to support, cookie policies, and credential storage. See [URLSessionConfiguration](../urlsessionconfiguration.md) for more information.

- `delegate` — A session delegate object that handles requests for authentication and other session-related events. This delegate object is responsible for handling authentication challenges, for making caching decisions, and for handling other session-related events. If `nil`, the class should be used only with methods that take completion handlers. > [!important] Important > The session object keeps a strong reference to the delegate until your app exits or explicitly invalidates the session. If you do not invalidate the session by calling the [- invalidateAndCancel](<invalidateandcancel().md>) or [- finishTasksAndInvalidate](<finishtasksandinvalidate().md>) method, your app leaks memory until it exits.

- `queue` — An operation queue for scheduling the delegate calls and completion handlers. The queue should be a serial queue, in order to ensure the correct ordering of callbacks. If `nil`, the session creates a serial operation queue for performing all delegate method calls and completion handler calls.

## See Also

### Creating a session

- [+ sessionWithConfiguration:](<init(configuration_).md>) — Creates a session with the specified session configuration.
- [URLSessionConfiguration](../urlsessionconfiguration.md) — A configuration object that defines behavior and policies for a URL session.
- [configuration](configuration.md) — A copy of the configuration object for this session.
