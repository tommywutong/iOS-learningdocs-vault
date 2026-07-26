---
title: 'uploadTask(with:from:completionHandler:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.0+, macOS 10.0+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/urlsession/uploadtask(with:from:completionhandler:)'
source_url: 'https://developer.apple.com/documentation/foundation/urlsession/uploadtask(with:from:completionhandler:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/urlsession/uploadtask%28with%3Afrom%3Acompletionhandler%3A%29.json'
content_hash: 'sha256:d3950e9d481eb9e7'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [URLSession](../urlsession.md)

# uploadTask(with:from:completionHandler:)

<sub>Instance Method</sub>

Creates a task that performs an HTTP request for the specified URL request object, uploads the provided data, and calls a handler upon completion.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func uploadTask(with request: URLRequest, from bodyData: Data?, completionHandler: @escaping @Sendable (Data?, URLResponse?, (any Error)?) -> Void) -> URLSessionUploadTask
```

## Parameters

- `request` — A URL request object that provides the URL, cache policy, request type, and so on. The body stream and body data in this request object are ignored.

- `bodyData` — The body data for the request.

- `completionHandler` — The completion handler to call when the load request is complete. This handler is executed on the delegate queue. If you pass `nil`, only the session delegate methods are called when the task completes, making this method equivalent to the [- uploadTaskWithRequest:fromData:](<uploadtask(with_from_).md>) method. This completion handler takes the following parameters: - **`data`** — The data returned by the server. - **`response`** — An object that provides response metadata, such as HTTP headers and status code. If you are making an HTTP or HTTPS request, the returned object is actually an [HTTPURLResponse](../httpurlresponse.md) object. - **`error`** — An error object that indicates why the request failed, or `nil` if the request was successful.

## Return Value

The new session upload task.

## Discussion

An HTTP upload request is any request that contains a request body, such as a `POST` or `PUT` request. Upload tasks require you to create a request object so that you can provide metadata for the upload, like HTTP request headers.

Unlike [- uploadTaskWithRequest:fromData:](<uploadtask(with_from_).md>), this method returns the response body after it has been received in full, and does not require you to write a custom delegate to obtain the response body.

By using a completion handler, the task bypasses calls to delegate methods for response and data delivery, and instead provides any resulting data, response, or error inside the completion handler. Delegate methods for handling authentication challenges, however, are still called.

Typically you pass a `nil` completion handler only when creating tasks in sessions whose delegates include a [- URLSession:dataTask:didReceiveData:](<../urlsessiondatadelegate/urlsession(__datatask_didreceive_).md>) method. However, if you do not need the response data, use key-value observing to watch for changes to the task’s status to determine when it completes.

After you create the task, you must start it by calling its [- resume](<../urlsessiontask/resume().md>) method.

If the request completes successfully, the `data` parameter of the completion handler block contains the resource data, and the `error` parameter is `nil`. If the request fails, the `data` parameter is `nil,` and the `error` parameter contains information about the failure. If a response from the server is received, regardless of whether the request completes successfully or fails, the `response` parameter contains that information.

## See Also

### Adding upload tasks to a session

- [Building a resumable upload server with SwiftNIO](../building-a-resumable-upload-server-with-swiftnio.md) — Support HTTP resumable upload protocol in SwiftNIO by translating resumable uploads to regular uploads.
- [- uploadTaskWithRequest:fromData:](<uploadtask(with_from_).md>) — Creates a task that performs an HTTP request for the specified URL request object and uploads the provided data.
- [- uploadTaskWithRequest:fromFile:](<uploadtask(with_fromfile_).md>) — Creates a task that performs an HTTP request for uploading the specified file.
- [- uploadTaskWithRequest:fromFile:completionHandler:](<uploadtask(with_fromfile_completionhandler_).md>) — Creates a task that performs an HTTP request for uploading the specified file, then calls a handler upon completion.
- [- uploadTaskWithStreamedRequest:](<uploadtask(withstreamedrequest_).md>) — Creates a task that performs an HTTP request for uploading data based on the specified URL request.
- [- uploadTaskWithResumeData:](<uploadtask(withresumedata_).md>) — Creates an upload task from a resume data blob. Requires the server to support the latest resumable uploads Internet-Draft from the HTTP Working Group, found at https://datatracker.ietf.org/doc/draft-ietf-httpbis-resumable-upload/ If resuming from an upload file, the file must still exist and be unmodified. If the upload cannot be successfully resumed, URLSession:task:didCompleteWithError: will be called.
- [- uploadTaskWithResumeData:completionHandler:](<uploadtask(withresumedata_completionhandler_).md>) — Creates a URLSessionUploadTask from a resume data blob. If resuming from an upload file, the file must still exist and be unmodified.
- [URLSessionUploadTask](../urlsessionuploadtask.md) — A URL session task that uploads data to the network in a request body.
- [URLSessionDataDelegate](../urlsessiondatadelegate.md) — A protocol that defines methods that URL session instances call on their delegates to handle task-level events specific to data and upload tasks.
