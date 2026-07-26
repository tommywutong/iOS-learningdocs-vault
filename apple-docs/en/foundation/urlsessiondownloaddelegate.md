---
title: URLSessionDownloadDelegate
framework: Foundation
symbol_kind: protocol
role: symbol
role_heading: Protocol
platforms: [iOS 7.0+, iPadOS 7.0+, Mac Catalyst 13.1+, macOS 10.9+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/urlsessiondownloaddelegate
source_url: 'https://developer.apple.com/documentation/foundation/urlsessiondownloaddelegate'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/urlsessiondownloaddelegate.json'
content_hash: 'sha256:0288a1cddc5670bb'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Foundation](../foundation.md)

# URLSessionDownloadDelegate

<sub>Protocol</sub>

A protocol that defines methods that URL session instances call on their delegates to handle task-level events specific to download tasks.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
protocol URLSessionDownloadDelegate : URLSessionTaskDelegate
```

## Overview

In addition to the methods in this protocol, be sure to implement the methods in the [URLSessionTaskDelegate](urlsessiontaskdelegate.md) and [URLSessionDelegate](urlsessiondelegate.md) protocols to handle events common to all task types and session-level events, respectively.

> [!note] Note
> An [URLSession](urlsession.md) object need not have a delegate. If no delegate is assigned, a system-provided delegate is used, and you must provide a completion callback to obtain the data.

## Relationships

- **Inherits From**: [NSObjectProtocol](../objectivec/nsobjectprotocol.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md), [URLSessionDelegate](urlsessiondelegate.md), [URLSessionTaskDelegate](urlsessiontaskdelegate.md)

## Topics

### Handling download life cycle changes

- [- URLSession:downloadTask:didFinishDownloadingToURL:](<urlsessiondownloaddelegate/urlsession(__downloadtask_didfinishdownloadingto_).md>) — Tells the delegate that a download task has finished downloading.

### Resuming paused downloads

- [- URLSession:downloadTask:didResumeAtOffset:expectedTotalBytes:](<urlsessiondownloaddelegate/urlsession(__downloadtask_didresumeatoffset_expectedtotalbytes_).md>) — Tells the delegate that the download task has resumed downloading.

### Receiving progress updates

- [- URLSession:downloadTask:didWriteData:totalBytesWritten:totalBytesExpectedToWrite:](<urlsessiondownloaddelegate/urlsession(__downloadtask_didwritedata_totalbyteswritten_totalbytesexpectedtowrite_).md>) — Periodically informs the delegate about the download’s progress.

## See Also

### Adding download tasks to a session

- [- downloadTaskWithURL:](<urlsession/downloadtask(with_)-1onj.md>) — Creates a download task that retrieves the contents of the specified URL and saves the results to a file.
- [- downloadTaskWithURL:completionHandler:](<urlsession/downloadtask(with_completionhandler_)-7cuje.md>) — Creates a download task that retrieves the contents of the specified URL, saves the results to a file, and calls a handler upon completion.
- [- downloadTaskWithRequest:](<urlsession/downloadtask(with_)-3fb7s.md>) — Creates a download task that retrieves the contents of a URL based on the specified URL request object and saves the results to a file.
- [- downloadTaskWithRequest:completionHandler:](<urlsession/downloadtask(with_completionhandler_)-4a84s.md>) — Creates a download task that retrieves the contents of a URL based on the specified URL request object, saves the results to a file, and calls a handler upon completion.
- [- downloadTaskWithResumeData:](<urlsession/downloadtask(withresumedata_).md>) — Creates a download task to resume a previously canceled or failed download.
- [- downloadTaskWithResumeData:completionHandler:](<urlsession/downloadtask(withresumedata_completionhandler_).md>) — Creates a download task to resume a previously canceled or failed download and calls a handler upon completion.
- [URLSessionDownloadTask](urlsessiondownloadtask.md) — A URL session task that stores downloaded data to a file.
