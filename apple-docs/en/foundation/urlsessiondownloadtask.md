---
title: URLSessionDownloadTask
framework: Foundation
symbol_kind: class
role: symbol
role_heading: Class
platforms: [iOS 7.0+, iPadOS 7.0+, Mac Catalyst 13.1+, macOS 10.9+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/urlsessiondownloadtask
source_url: 'https://developer.apple.com/documentation/foundation/urlsessiondownloadtask'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/urlsessiondownloadtask.json'
content_hash: 'sha256:5d751fa8be07f187'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Foundation](../foundation.md)

# URLSessionDownloadTask

<sub>Class</sub>

A URL session task that stores downloaded data to a file.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
class URLSessionDownloadTask
```

## Overview

An [URLSessionDownloadTask](urlsessiondownloadtask.md) is a concrete subclass of [URLSessionTask](urlsessiontask.md), which provides most of the methods for this class.

Download tasks directly write the server’s response data to a temporary file, providing your app with progress updates as data arrives from the server. When you use download tasks in background sessions, these downloads continue even when your app is in the suspended state or otherwise not running.

You can pause (cancel) download tasks and resume them later (assuming the server supports doing so). You can also resume downloads that failed because of network connectivity problems.

### Download delegate behavior

When you use a download task, your delegate receives several callbacks unique to download scenarios.

- During download, the session periodically calls the delegate’s [- URLSession:downloadTask:didWriteData:totalBytesWritten:totalBytesExpectedToWrite:](<urlsessiondownloaddelegate/urlsession(__downloadtask_didwritedata_totalbyteswritten_totalbytesexpectedtowrite_).md>) method with status information.
- Upon successful completion, the session calls the delegate’s [- URLSession:downloadTask:didFinishDownloadingToURL:](<urlsessiondownloaddelegate/urlsession(__downloadtask_didfinishdownloadingto_).md>) method or completion handler. In that method, you must either open the file for reading or move it to a permanent location in your app’s sandbox container directory.
- Upon unsuccessful completion, the session calls the delegate’s [- URLSession:task:didCompleteWithError:](<urlsessiontaskdelegate/urlsession(__task_didcompletewitherror_).md>) method or completion handler. The only errors your delegate receives through the `error` parameter are client-side errors, such as being unable to resolve the hostname or connect to the host. To check for server-side errors, inspect the [response](urlsessiontask/response.md) property of the `task` parameter received by this callback.

## Relationships

- **Inherits From**: [URLSessionTask](urlsessiontask.md)

- **Conforms To**: [CVarArg](../swift/cvararg.md), [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md), [CustomStringConvertible](../swift/customstringconvertible.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [NSCopying](nscopying.md), [NSObjectProtocol](../objectivec/nsobjectprotocol.md), [ProgressReporting](progressreporting.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md)

## Topics

### Canceling a download

- [- cancelByProducingResumeData:](<urlsessiondownloadtask/cancel(byproducingresumedata_).md>) — Cancels a download and calls a callback with resume data for later use.

### Creating download tasks

- [- init](<urlsessiondownloadtask/init().md>) — Initializes a download task. _(deprecated)_
- [+ new](<urlsessiondownloadtask/new().md>) — Creates and initializes a download task. _(deprecated)_

## See Also

### Adding download tasks to a session

- [- downloadTaskWithURL:](<urlsession/downloadtask(with_)-1onj.md>) — Creates a download task that retrieves the contents of the specified URL and saves the results to a file.
- [- downloadTaskWithURL:completionHandler:](<urlsession/downloadtask(with_completionhandler_)-7cuje.md>) — Creates a download task that retrieves the contents of the specified URL, saves the results to a file, and calls a handler upon completion.
- [- downloadTaskWithRequest:](<urlsession/downloadtask(with_)-3fb7s.md>) — Creates a download task that retrieves the contents of a URL based on the specified URL request object and saves the results to a file.
- [- downloadTaskWithRequest:completionHandler:](<urlsession/downloadtask(with_completionhandler_)-4a84s.md>) — Creates a download task that retrieves the contents of a URL based on the specified URL request object, saves the results to a file, and calls a handler upon completion.
- [- downloadTaskWithResumeData:](<urlsession/downloadtask(withresumedata_).md>) — Creates a download task to resume a previously canceled or failed download.
- [- downloadTaskWithResumeData:completionHandler:](<urlsession/downloadtask(withresumedata_completionhandler_).md>) — Creates a download task to resume a previously canceled or failed download and calls a handler upon completion.
- [URLSessionDownloadDelegate](urlsessiondownloaddelegate.md) — A protocol that defines methods that URL session instances call on their delegates to handle task-level events specific to download tasks.
