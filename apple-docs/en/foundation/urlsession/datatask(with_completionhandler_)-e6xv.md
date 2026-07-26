---
title: 'dataTask(with:completionHandler:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.0+, macOS 10.0+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/urlsession/datatask(with:completionhandler:)-e6xv'
source_url: 'https://developer.apple.com/documentation/foundation/urlsession/datatask(with:completionhandler:)-e6xv'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/urlsession/datatask%28with%3Acompletionhandler%3A%29-e6xv.json'
content_hash: 'sha256:1e34a0b35f26b949'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [URLSession](../urlsession.md)

# dataTask(with:completionHandler:)

<sub>Instance Method</sub>

Creates a task that retrieves the contents of a URL based on the specified URL request object, and calls a handler upon completion.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func dataTask(with request: URLRequest, completionHandler: @escaping @Sendable (Data?, URLResponse?, (any Error)?) -> Void) -> URLSessionDataTask
```

## Parameters

- `request` — A URL request object that provides the URL, cache policy, request type, body data or body stream, and so on.

- `completionHandler` — The completion handler to call when the load request is complete. This handler is executed on the delegate queue. If you pass `nil`, only the session delegate methods are called when the task completes, making this method equivalent to the [- dataTaskWithRequest:](<datatask(with_)-7jpys.md>) method. This completion handler takes the following parameters: - **`data`** — The data returned by the server. - **`response`** — An object that provides response metadata, such as HTTP headers and status code. If you are making an HTTP or HTTPS request, the returned object is actually an [HTTPURLResponse](../httpurlresponse.md) object. - **`error`** — An error object that indicates why the request failed, or `nil` if the request was successful.

## Return Value

The new session data task.

## Discussion

By creating a task based on a request object, you can tune various aspects of the task’s behavior, including the cache policy and timeout interval.

By using the completion handler, the task bypasses calls to delegate methods for response and data delivery, and instead provides any resulting [NSData](../nsdata.md), [URLResponse](../urlresponse.md), and [NSError](../nserror.md) objects inside the completion handler. Delegate methods for handling authentication challenges, however, are still called.

You should pass a `nil` completion handler _only_ when creating tasks in sessions whose delegates include a [- URLSession:dataTask:didReceiveData:](<../urlsessiondatadelegate/urlsession(__datatask_didreceive_).md>) method.

After you create the task, you must start it by calling its [- resume](<../urlsessiontask/resume().md>) method.

If the request completes successfully, the `data` parameter of the completion handler block contains the resource data, and the `error` parameter is `nil`. If the request fails, the `data` parameter is `nil` and the `error` parameter contain information about the failure. If a response from the server is received, regardless of whether the request completes successfully or fails, the `response` parameter contains that information.

## See Also

### Adding data tasks to a session

- [- dataTaskWithURL:](<datatask(with_)-10dy7.md>) — Creates a task that retrieves the contents of the specified URL.
- [- dataTaskWithURL:completionHandler:](<datatask(with_completionhandler_)-52wk8.md>) — Creates a task that retrieves the contents of the specified URL, then calls a handler upon completion.
- [- dataTaskWithRequest:](<datatask(with_)-7jpys.md>) — Creates a task that retrieves the contents of a URL based on the specified URL request object.
- [URLSessionDataTask](../urlsessiondatatask.md) — A URL session task that returns downloaded data directly to the app in memory.
- [URLSessionDataDelegate](../urlsessiondatadelegate.md) — A protocol that defines methods that URL session instances call on their delegates to handle task-level events specific to data and upload tasks.
