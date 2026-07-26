---
title: 'urlSession(_:task:willPerformHTTPRedirection:newRequest:completionHandler:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 7.0+, iPadOS 7.0+, Mac Catalyst 13.1+, macOS 10.9+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, swift, swift, occ, occ, occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/urlsessiontaskdelegate/urlsession(_:task:willperformhttpredirection:newrequest:completionhandler:)'
source_url: 'https://developer.apple.com/documentation/foundation/urlsessiontaskdelegate/urlsession(_:task:willperformhttpredirection:newrequest:completionhandler:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/urlsessiontaskdelegate/urlsession%28_%3Atask%3Awillperformhttpredirection%3Anewrequest%3Acompletionhandler%3A%29.json'
content_hash: 'sha256:491989c8d39f09fb'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [URLSessionTaskDelegate](../urlsessiontaskdelegate.md)

# urlSession(_:task:willPerformHTTPRedirection:newRequest:completionHandler:)

<sub>Instance Method</sub>

Tells the delegate that the remote server requested an HTTP redirect.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
optional func urlSession(_ session: URLSession, task: URLSessionTask, willPerformHTTPRedirection response: HTTPURLResponse, newRequest request: URLRequest, completionHandler: @escaping @Sendable (URLRequest?) -> Void)
```

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
optional func urlSession(_ session: URLSession, task: URLSessionTask, willPerformHTTPRedirection response: HTTPURLResponse, newRequest request: URLRequest) async -> URLRequest?
```

## Parameters

- `session` — The session containing the task whose request resulted in a redirect.

- `task` — The task whose request resulted in a redirect.

- `response` — An object containing the server’s response to the original request.

- `request` — A URL request object filled out with the new location.

- `completionHandler` — A block that your handler should call with either the value of the `request` parameter, a modified URL request object, or `NULL` to refuse the redirect and return the body of the redirect response.

## Discussion

This method is called _only_ for tasks in default and ephemeral sessions. Tasks in background sessions automatically follow redirects.
