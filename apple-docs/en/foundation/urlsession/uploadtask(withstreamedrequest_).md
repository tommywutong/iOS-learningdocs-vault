---
title: 'uploadTask(withStreamedRequest:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 7.0+, iPadOS 7.0+, Mac Catalyst 13.1+, macOS 10.9+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/urlsession/uploadtask(withstreamedrequest:)'
source_url: 'https://developer.apple.com/documentation/foundation/urlsession/uploadtask(withstreamedrequest:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/urlsession/uploadtask%28withstreamedrequest%3A%29.json'
content_hash: 'sha256:01258259588508b5'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [URLSession](../urlsession.md)

# uploadTask(withStreamedRequest:)

<sub>Instance Method</sub>

Creates a task that performs an HTTP request for uploading data based on the specified URL request.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func uploadTask(withStreamedRequest request: URLRequest) -> URLSessionUploadTask
```

## Parameters

- `request` — A URL request object that provides the URL, cache policy, request type, and so on. The body stream and body data in this request object are ignored, and the session calls its delegate’s [- URLSession:task:needNewBodyStream:](<../urlsessiontaskdelegate/urlsession(__task_neednewbodystream_).md>) method to provide the body data.

## Return Value

The new session upload task.

## Discussion

An HTTP upload request is any request that contains a request body, such as a `POST` or `PUT` request. Upload tasks require you to provide a request object so that you can provide metadata for the upload, such as HTTP request headers.

After you create the task, you must start it by calling its [- resume](<../urlsessiontask/resume().md>) method. The task calls methods on the session’s delegate to provide you with the upload’s progress, response metadata, response data, and so on. The session’s delegate must have a [- URLSession:task:needNewBodyStream:](<../urlsessiontaskdelegate/urlsession(__task_neednewbodystream_).md>) method that provides the body data to upload.

## See Also

### Adding upload tasks to a session

- [Building a resumable upload server with SwiftNIO](../building-a-resumable-upload-server-with-swiftnio.md) — Support HTTP resumable upload protocol in SwiftNIO by translating resumable uploads to regular uploads.
- [- uploadTaskWithRequest:fromData:](<uploadtask(with_from_).md>) — Creates a task that performs an HTTP request for the specified URL request object and uploads the provided data.
- [- uploadTaskWithRequest:fromData:completionHandler:](<uploadtask(with_from_completionhandler_).md>) — Creates a task that performs an HTTP request for the specified URL request object, uploads the provided data, and calls a handler upon completion.
- [- uploadTaskWithRequest:fromFile:](<uploadtask(with_fromfile_).md>) — Creates a task that performs an HTTP request for uploading the specified file.
- [- uploadTaskWithRequest:fromFile:completionHandler:](<uploadtask(with_fromfile_completionhandler_).md>) — Creates a task that performs an HTTP request for uploading the specified file, then calls a handler upon completion.
- [- uploadTaskWithResumeData:](<uploadtask(withresumedata_).md>) — Creates an upload task from a resume data blob. Requires the server to support the latest resumable uploads Internet-Draft from the HTTP Working Group, found at https://datatracker.ietf.org/doc/draft-ietf-httpbis-resumable-upload/ If resuming from an upload file, the file must still exist and be unmodified. If the upload cannot be successfully resumed, URLSession:task:didCompleteWithError: will be called.
- [- uploadTaskWithResumeData:completionHandler:](<uploadtask(withresumedata_completionhandler_).md>) — Creates a URLSessionUploadTask from a resume data blob. If resuming from an upload file, the file must still exist and be unmodified.
- [URLSessionUploadTask](../urlsessionuploadtask.md) — A URL session task that uploads data to the network in a request body.
- [URLSessionDataDelegate](../urlsessiondatadelegate.md) — A protocol that defines methods that URL session instances call on their delegates to handle task-level events specific to data and upload tasks.
