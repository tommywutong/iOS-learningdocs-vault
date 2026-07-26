---
title: start()
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.1+, macOS 10.5+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/nsurlconnection/start()
source_url: 'https://developer.apple.com/documentation/foundation/nsurlconnection/start()'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsurlconnection/start%28%29.json'
content_hash: 'sha256:58992e96a24069b2'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSURLConnection](../nsurlconnection.md)

# start()

<sub>Instance Method</sub>

Causes the connection to begin loading data, if it has not already.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func start()
```

## Discussion

Calling this method is necessary only if you create a connection with the [- initWithRequest:delegate:startImmediately:](<init(request_delegate_startimmediately_).md>) method and provide [false](../../swift/false.md) for the `startImmediately` parameter. If you don’t schedule the connection in a run loop or an operation queue before calling this method, the connection is scheduled in the current run loop in the default mode.

## See Also

### Loading Data Asynchronously

- [- initWithRequest:delegate:](<init(request_delegate_).md>) — Returns an initialized URL connection and begins to load the data for the URL request. _(deprecated)_
- [- initWithRequest:delegate:startImmediately:](<init(request_delegate_startimmediately_).md>) — Returns an initialized URL connection and begins to load the data for the URL request, if specified. _(deprecated)_
- [+ sendAsynchronousRequest:queue:completionHandler:](<sendasynchronousrequest(__queue_completionhandler_).md>) — Loads the data for a URL request and executes a handler block on an operation queue when the request completes or fails. _(deprecated)_
