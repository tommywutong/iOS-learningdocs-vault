---
title: URLSessionUploadTask
framework: Foundation
symbol_kind: class
role: symbol
role_heading: Class
platforms: [iOS 7.0+, iPadOS 7.0+, Mac Catalyst 13.1+, macOS 10.9+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/urlsessionuploadtask
source_url: 'https://developer.apple.com/documentation/foundation/urlsessionuploadtask'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/urlsessionuploadtask.json'
content_hash: 'sha256:6720ab7053e3f63f'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Foundation](../foundation.md)

# URLSessionUploadTask

<sub>Class</sub>

A URL session task that uploads data to the network in a request body.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
class URLSessionUploadTask
```

## Overview

The [URLSessionUploadTask](urlsessionuploadtask.md) class is a subclass of [URLSessionDataTask](urlsessiondatatask.md), which in turn is a concrete subclass of [URLSessionTask](urlsessiontask.md). The methods associated with the [URLSessionUploadTask](urlsessionuploadtask.md) class are documented in [URLSessionTask](urlsessiontask.md).

Upload tasks are used for making HTTP requests that require a request body (such as `POST` or `PUT`). They behave similarly to data tasks, but you create them by calling different methods on the session that are designed to make it easier to provide the content to upload. As with data tasks, if the server provides a response, upload tasks return that response as one or more `NSData` objects in memory.

> [!note] Note
> Unlike data tasks, you can use upload tasks to upload content in the background.

When you create an upload task, you provide a [URLRequest](urlrequest.md) instance that contains any additional headers that you might need to send alongside the upload, such as the content type, content disposition, and so on. In iOS, when you create an upload task for a file in a background session, the system copies that file to a temporary location and streams data from there.

While the upload is in progress, the task calls the session delegate’s [- URLSession:task:didSendBodyData:totalBytesSent:totalBytesExpectedToSend:](<urlsessiontaskdelegate/urlsession(__task_didsendbodydata_totalbytessent_totalbytesexpectedtosend_).md>) method periodically to provide you with status information.

When the upload phase of the request finishes, the task behaves like a data task, calling methods on the session delegate to provide you with the server’s response—headers, status code, content data, and so on.

## Relationships

- **Inherits From**: [URLSessionDataTask](urlsessiondatatask.md)

- **Conforms To**: [CVarArg](../swift/cvararg.md), [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md), [CustomStringConvertible](../swift/customstringconvertible.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [NSCopying](nscopying.md), [NSObjectProtocol](../objectivec/nsobjectprotocol.md), [ProgressReporting](progressreporting.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md)

## Topics

### Initializers

- [- init](<urlsessionuploadtask/init().md>) _(deprecated)_

### Instance Methods

- [- cancelByProducingResumeData:](<urlsessionuploadtask/cancel(byproducingresumedata_).md>) — Cancels an upload and calls the completion handler with resume data for later use. resumeData will be nil if the server does not support the latest resumable uploads Internet-Draft from the HTTP Working Group, found at https://datatracker.ietf.org/doc/draft-ietf-httpbis-resumable-upload/

### Type Methods

- [+ new](<urlsessionuploadtask/new().md>) _(deprecated)_

## See Also

### Adding upload tasks to a session

- [Building a resumable upload server with SwiftNIO](building-a-resumable-upload-server-with-swiftnio.md) — Support HTTP resumable upload protocol in SwiftNIO by translating resumable uploads to regular uploads.
- [- uploadTaskWithRequest:fromData:](<urlsession/uploadtask(with_from_).md>) — Creates a task that performs an HTTP request for the specified URL request object and uploads the provided data.
- [- uploadTaskWithRequest:fromData:completionHandler:](<urlsession/uploadtask(with_from_completionhandler_).md>) — Creates a task that performs an HTTP request for the specified URL request object, uploads the provided data, and calls a handler upon completion.
- [- uploadTaskWithRequest:fromFile:](<urlsession/uploadtask(with_fromfile_).md>) — Creates a task that performs an HTTP request for uploading the specified file.
- [- uploadTaskWithRequest:fromFile:completionHandler:](<urlsession/uploadtask(with_fromfile_completionhandler_).md>) — Creates a task that performs an HTTP request for uploading the specified file, then calls a handler upon completion.
- [- uploadTaskWithStreamedRequest:](<urlsession/uploadtask(withstreamedrequest_).md>) — Creates a task that performs an HTTP request for uploading data based on the specified URL request.
- [- uploadTaskWithResumeData:](<urlsession/uploadtask(withresumedata_).md>) — Creates an upload task from a resume data blob. Requires the server to support the latest resumable uploads Internet-Draft from the HTTP Working Group, found at https://datatracker.ietf.org/doc/draft-ietf-httpbis-resumable-upload/ If resuming from an upload file, the file must still exist and be unmodified. If the upload cannot be successfully resumed, URLSession:task:didCompleteWithError: will be called.
- [- uploadTaskWithResumeData:completionHandler:](<urlsession/uploadtask(withresumedata_completionhandler_).md>) — Creates a URLSessionUploadTask from a resume data blob. If resuming from an upload file, the file must still exist and be unmodified.
- [URLSessionDataDelegate](urlsessiondatadelegate.md) — A protocol that defines methods that URL session instances call on their delegates to handle task-level events specific to data and upload tasks.
