---
title: 'uploadTask(withResumeData:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 17.0+, iPadOS 17.0+, Mac Catalyst 17.0+, macOS 14.0+, tvOS 17.0+, visionOS 1.0+, watchOS 10.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/urlsession/uploadtask(withresumedata:)'
source_url: 'https://developer.apple.com/documentation/foundation/urlsession/uploadtask(withresumedata:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/urlsession/uploadtask%28withresumedata%3A%29.json'
content_hash: 'sha256:f615e5325453c9b0'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [URLSession](../urlsession.md)

# uploadTask(withResumeData:)

<sub>Instance Method</sub>

Creates an upload task from a resume data blob. Requires the server to support the latest resumable uploads Internet-Draft from the HTTP Working Group, found at https://datatracker.ietf.org/doc/draft-ietf-httpbis-resumable-upload/ If resuming from an upload file, the file must still exist and be unmodified. If the upload cannot be successfully resumed, URLSession:task:didCompleteWithError: will be called.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func uploadTask(withResumeData resumeData: Data) -> URLSessionUploadTask
```

## Parameters

- `resumeData` — Resume data blob from an incomplete upload, such as data returned by the cancelByProducingResumeData: method.

## Return Value

A new session upload task, or nil if the resumeData is invalid.

## See Also

### Adding upload tasks to a session

- [Building a resumable upload server with SwiftNIO](../building-a-resumable-upload-server-with-swiftnio.md) — Support HTTP resumable upload protocol in SwiftNIO by translating resumable uploads to regular uploads.
- [- uploadTaskWithRequest:fromData:](<uploadtask(with_from_).md>) — Creates a task that performs an HTTP request for the specified URL request object and uploads the provided data.
- [- uploadTaskWithRequest:fromData:completionHandler:](<uploadtask(with_from_completionhandler_).md>) — Creates a task that performs an HTTP request for the specified URL request object, uploads the provided data, and calls a handler upon completion.
- [- uploadTaskWithRequest:fromFile:](<uploadtask(with_fromfile_).md>) — Creates a task that performs an HTTP request for uploading the specified file.
- [- uploadTaskWithRequest:fromFile:completionHandler:](<uploadtask(with_fromfile_completionhandler_).md>) — Creates a task that performs an HTTP request for uploading the specified file, then calls a handler upon completion.
- [- uploadTaskWithStreamedRequest:](<uploadtask(withstreamedrequest_).md>) — Creates a task that performs an HTTP request for uploading data based on the specified URL request.
- [- uploadTaskWithResumeData:completionHandler:](<uploadtask(withresumedata_completionhandler_).md>) — Creates a URLSessionUploadTask from a resume data blob. If resuming from an upload file, the file must still exist and be unmodified.
- [URLSessionUploadTask](../urlsessionuploadtask.md) — A URL session task that uploads data to the network in a request body.
- [URLSessionDataDelegate](../urlsessiondatadelegate.md) — A protocol that defines methods that URL session instances call on their delegates to handle task-level events specific to data and upload tasks.
