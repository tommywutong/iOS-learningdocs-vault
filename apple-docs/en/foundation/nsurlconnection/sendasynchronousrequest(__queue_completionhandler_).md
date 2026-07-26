---
title: 'sendAsynchronousRequest(_:queue:completionHandler:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [iOS 5.0+（9.0 起废弃）, iPadOS 5.0+（9.0 起废弃）, Mac Catalyst 13.1+（13.1 起废弃）, macOS 10.7+（10.11 起废弃）, tvOS 9.0+（9.0 起废弃）, visionOS 1.0+（1.0 起废弃）]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: '/documentation/foundation/nsurlconnection/sendasynchronousrequest(_:queue:completionhandler:)'
source_url: 'https://developer.apple.com/documentation/foundation/nsurlconnection/sendasynchronousrequest(_:queue:completionhandler:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsurlconnection/sendasynchronousrequest%28_%3Aqueue%3Acompletionhandler%3A%29.json'
content_hash: 'sha256:222a001c2c06ed0e'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSURLConnection](../nsurlconnection.md)

# sendAsynchronousRequest(_:queue:completionHandler:)

<sub>Type Method</sub>

Loads the data for a URL request and executes a handler block on an operation queue when the request completes or fails.

> [!warning] Deprecated
> Use [NSURLSession dataTaskWithRequest:completionHandler:] (see NSURLSession.h

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
class func sendAsynchronousRequest(_ request: URLRequest, queue: OperationQueue, completionHandler handler: @escaping @Sendable (URLResponse?, Data?, (any Error)?) -> Void)
```

<sub>Mac Catalyst, visionOS</sub>

```swift
class func sendAsynchronousRequest(_ request: URLRequest, queue: OperationQueue) async throws -> (URLResponse, Data)
```

## Parameters

- `request` — The URL request to load. The `request` object is deep-copied as part of the initialization process. Changes made to `request` after this method returns do not affect the request that is used for the loading process.

- `queue` — The operation queue to which the handler block is dispatched when the request completes or failed.

- `handler` — The handler block to execute.

## Discussion

If the request completes successfully, the `data` parameter of the handler block contains the resource data, and the `error` parameter is `nil`.  If the request fails, the `data` parameter is `nil` and the error parameter contain information about the failure.

If authentication is required in order to download the request, the required credentials must be specified as part of the URL. If authentication fails, or credentials are missing, the connection will attempt to continue without credentials. If the request finishes with a `401 Unauthorized` status code, the `response` parameter is `nil`, the `data` parameter contains the resource data, and the `error` parameter is an `NSError` with the [NSURLErrorUserCancelledAuthentication](../nsurlerrorusercancelledauthentication-swift.var.md) code in the [NSURLErrorDomain](../nsurlerrordomain.md) error domain.

## See Also

### Loading Data Asynchronously

- [- initWithRequest:delegate:](<init(request_delegate_).md>) — Returns an initialized URL connection and begins to load the data for the URL request. _(deprecated)_
- [- initWithRequest:delegate:startImmediately:](<init(request_delegate_startimmediately_).md>) — Returns an initialized URL connection and begins to load the data for the URL request, if specified. _(deprecated)_
- [- start](<start().md>) — Causes the connection to begin loading data, if it has not already.
