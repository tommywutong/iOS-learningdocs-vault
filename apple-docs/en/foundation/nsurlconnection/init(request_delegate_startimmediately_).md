---
title: 'init(request:delegate:startImmediately:)'
framework: Foundation
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 2.0+（9.0 起废弃）, iPadOS 2.0+（9.0 起废弃）, Mac Catalyst 13.1+（13.1 起废弃）, macOS 10.5+（10.11 起废弃）, tvOS 9.0+（9.0 起废弃）, visionOS 1.0+（1.0 起废弃）]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: '/documentation/foundation/nsurlconnection/init(request:delegate:startimmediately:)'
source_url: 'https://developer.apple.com/documentation/foundation/nsurlconnection/init(request:delegate:startimmediately:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsurlconnection/init%28request%3Adelegate%3Astartimmediately%3A%29.json'
content_hash: 'sha256:c26ca538e826c041'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSURLConnection](../nsurlconnection.md)

# init(request:delegate:startImmediately:)

<sub>Initializer</sub>

Returns an initialized URL connection and begins to load the data for the URL request, if specified.

> [!warning] Deprecated
> Use NSURLSession (see NSURLSession.h)

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
init?(request: URLRequest, delegate: Any?, startImmediately: Bool)
```

## Parameters

- `request` — The URL request to load. The `request` object is deep-copied as part of the initialization process. Changes made to `request` after this method returns do not affect the request that is used for the loading process.

- `delegate` — The delegate object for the connection. The connection calls methods on this delegate as the load progresses.

- `startImmediately` — [true](../../swift/true.md) if the connection should begin loading data immediately, otherwise [false](../../swift/false.md). If you pass [false](../../swift/false.md), the connection is not scheduled with a run loop. You can then schedule the connection in the run loop and mode of your choice by calling [- scheduleInRunLoop:forMode:](<schedule(in_formode_).md>).

## Return Value

The URL connection for the URL request. Returns `nil` if a connection can’t be initialized.

## Discussion

During the download the connection maintains a strong reference to the `delegate`. It releases that strong reference when the connection finishes loading, fails, or is canceled.

## See Also

### Loading Data Asynchronously

- [- initWithRequest:delegate:](<init(request_delegate_).md>) — Returns an initialized URL connection and begins to load the data for the URL request. _(deprecated)_
- [+ sendAsynchronousRequest:queue:completionHandler:](<sendasynchronousrequest(__queue_completionhandler_).md>) — Loads the data for a URL request and executes a handler block on an operation queue when the request completes or fails. _(deprecated)_
- [- start](<start().md>) — Causes the connection to begin loading data, if it has not already.
