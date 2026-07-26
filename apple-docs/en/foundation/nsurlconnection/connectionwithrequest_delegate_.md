---
title: 'connectionWithRequest:delegate:'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [iOS 2.0+（9.0 起废弃）, iPadOS 2.0+（9.0 起废弃）, Mac Catalyst 13.1+（13.1 起废弃）, macOS 10.3+（10.11 起废弃）, tvOS 9.0+（9.0 起废弃）, visionOS 1.0+（1.0 起废弃）]
languages: [occ]
beta: false
deprecated: true
doc_path: '/documentation/foundation/nsurlconnection/connectionwithrequest:delegate:'
source_url: 'https://developer.apple.com/documentation/foundation/nsurlconnection/connectionwithrequest:delegate:'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsurlconnection/connectionwithrequest%3Adelegate%3A.json'
content_hash: 'sha256:bd2c60ccb3e4804a'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSURLConnection](../nsurlconnection.md)

# connectionWithRequest:delegate:

<sub>Type Method</sub>

Creates and returns an initialized URL connection and begins to load the data for the URL request.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```objc
+ (NSURLConnection *) connectionWithRequest:(NSURLRequest *) request delegate:(id) delegate;
```

## Parameters

- `request` — The URL request to load. The `request` object is deep-copied as part of the initialization process. Changes made to `request` after this method returns do not affect the request that is used for the loading process.

- `delegate` — The delegate object for the connection. The connection calls methods on this delegate as the load progresses. Delegate methods are called on the same thread that called this method. For the connection to work correctly, the calling thread’s run loop must be operating in the default run loop mode.

## Return Value

The URL connection for the URL request. Returns `nil` if a connection can’t be created.

## Discussion

During the download the connection maintains a strong reference to the `delegate`. It releases that strong reference when the connection finishes loading, fails, or is canceled.

## See Also

### Loading Data Asynchronously

- [- initWithRequest:delegate:](<init(request_delegate_).md>) — Returns an initialized URL connection and begins to load the data for the URL request. _(deprecated)_
- [- initWithRequest:delegate:startImmediately:](<init(request_delegate_startimmediately_).md>) — Returns an initialized URL connection and begins to load the data for the URL request, if specified. _(deprecated)_
- [+ sendAsynchronousRequest:queue:completionHandler:](<sendasynchronousrequest(__queue_completionhandler_).md>) — Loads the data for a URL request and executes a handler block on an operation queue when the request completes or fails. _(deprecated)_
- [- start](<start().md>) — Causes the connection to begin loading data, if it has not already.
