---
title: 'init(request:delegate:)'
framework: Foundation
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 2.0+（9.0 起废弃）, iPadOS 2.0+（9.0 起废弃）, Mac Catalyst 13.1+（13.1 起废弃）, macOS 10.3+（10.11 起废弃）, tvOS 9.0+（9.0 起废弃）, visionOS 1.0+（1.0 起废弃）]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: '/documentation/foundation/nsurlconnection/init(request:delegate:)'
source_url: 'https://developer.apple.com/documentation/foundation/nsurlconnection/init(request:delegate:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsurlconnection/init%28request%3Adelegate%3A%29.json'
content_hash: 'sha256:902ae9bd7ffe6955'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSURLConnection](../nsurlconnection.md)

# init(request:delegate:)

<sub>Initializer</sub>

Returns an initialized URL connection and begins to load the data for the URL request.

> [!warning] Deprecated
> Use NSURLSession (see NSURLSession.h)

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
init?(request: URLRequest, delegate: Any?)
```

## Parameters

- `request` — The URL request to load. The `request` object is deep-copied as part of the initialization process. Changes made to `request` after this method returns do not affect the request that is used for the loading process.

- `delegate` — The delegate object for the connection. The connection calls methods on this delegate as the load progresses. Delegate methods are called on the same thread that called this method. By default, for the connection to work correctly, the calling thread’s run loop must be operating in the default run loop mode. See [- scheduleInRunLoop:forMode:](<schedule(in_formode_).md>) to change the run loop and mode.

## Return Value

The URL connection for the URL request. Returns `nil` if a connection can’t be initialized.

## Discussion

This is equivalent to calling [- initWithRequest:delegate:startImmediately:](<init(request_delegate_startimmediately_).md>) and passing [true](../../swift/true.md) for `startImmediately`.

### Special Considerations

During the download the connection maintains a strong reference to the `delegate`. It releases that strong reference when the connection finishes loading, fails, or is canceled.

## See Also

### Loading Data Asynchronously

- [- initWithRequest:delegate:startImmediately:](<init(request_delegate_startimmediately_).md>) — Returns an initialized URL connection and begins to load the data for the URL request, if specified. _(deprecated)_
- [+ sendAsynchronousRequest:queue:completionHandler:](<sendasynchronousrequest(__queue_completionhandler_).md>) — Loads the data for a URL request and executes a handler block on an operation queue when the request completes or fails. _(deprecated)_
- [- start](<start().md>) — Causes the connection to begin loading data, if it has not already.
