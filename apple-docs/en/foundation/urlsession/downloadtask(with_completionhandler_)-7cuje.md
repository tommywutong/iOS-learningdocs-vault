---
title: 'downloadTask(with:completionHandler:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.0+, macOS 10.0+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/urlsession/downloadtask(with:completionhandler:)-7cuje'
source_url: 'https://developer.apple.com/documentation/foundation/urlsession/downloadtask(with:completionhandler:)-7cuje'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/urlsession/downloadtask%28with%3Acompletionhandler%3A%29-7cuje.json'
content_hash: 'sha256:e569a67d84fe3f4f'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [URLSession](../urlsession.md)

# downloadTask(with:completionHandler:)

<sub>Instance Method</sub>

Creates a download task that retrieves the contents of the specified URL, saves the results to a file, and calls a handler upon completion.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func downloadTask(with url: URL, completionHandler: @escaping @Sendable (URL?, URLResponse?, (any Error)?) -> Void) -> URLSessionDownloadTask
```

## Parameters

- `url` — The URL to download.

- `completionHandler` — The completion handler to call when the load request is complete. This handler is executed on the delegate queue. If you pass `nil`, only the session delegate methods are called when the task completes, making this method equivalent to the [- downloadTaskWithURL:](<downloadtask(with_)-1onj.md>) method. This completion handler takes the following parameters: - **`location`** — The location of a temporary file where the server’s response is stored. You must move this file or open it for reading before your completion handler returns. Otherwise, the file is deleted, and the data is lost. - **`response`** — An object that provides response metadata, such as HTTP headers and status code. If you are making an HTTP or HTTPS request, the returned object is actually an [HTTPURLResponse](../httpurlresponse.md) object. - **`error`** — An error object that indicates why the request failed, or `nil` if the request was successful.

## Return Value

The new session download task.

## Discussion

By using the completion handler, the task bypasses calls to delegate methods for response and data delivery, and instead provides any resulting [NSData](https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/PropertyLists/OldStylePlists/OldStylePLists.html#//apple_ref/doc/uid/20001012-47169), [URLResponse](../urlresponse.md), and [NSError](../nserror.md) objects inside the completion handler. Delegate methods for handling authentication challenges, however, are still called.

You should pass a `nil` completion handler _only_ when creating tasks in sessions whose delegates include a [- URLSession:downloadTask:didFinishDownloadingToURL:](<../urlsessiondownloaddelegate/urlsession(__downloadtask_didfinishdownloadingto_).md>) method.

After you create the task, you must start it by calling its [- resume](<../urlsessiontask/resume().md>) method.

If the request completes successfully, the `location` parameter of the completion handler block contains the location of the temporary file, and the `error` parameter is `nil`. If the request fails, the `location` parameter is `nil` and the `error` parameter contain information about the failure. If a response from the server is received, regardless of whether the request completes successfully or fails, the `response` parameter contains that information.

## See Also

### Adding download tasks to a session

- [- downloadTaskWithURL:](<downloadtask(with_)-1onj.md>) — Creates a download task that retrieves the contents of the specified URL and saves the results to a file.
- [- downloadTaskWithRequest:](<downloadtask(with_)-3fb7s.md>) — Creates a download task that retrieves the contents of a URL based on the specified URL request object and saves the results to a file.
- [- downloadTaskWithRequest:completionHandler:](<downloadtask(with_completionhandler_)-4a84s.md>) — Creates a download task that retrieves the contents of a URL based on the specified URL request object, saves the results to a file, and calls a handler upon completion.
- [- downloadTaskWithResumeData:](<downloadtask(withresumedata_).md>) — Creates a download task to resume a previously canceled or failed download.
- [- downloadTaskWithResumeData:completionHandler:](<downloadtask(withresumedata_completionhandler_).md>) — Creates a download task to resume a previously canceled or failed download and calls a handler upon completion.
- [URLSessionDownloadTask](../urlsessiondownloadtask.md) — A URL session task that stores downloaded data to a file.
- [URLSessionDownloadDelegate](../urlsessiondownloaddelegate.md) — A protocol that defines methods that URL session instances call on their delegates to handle task-level events specific to download tasks.
