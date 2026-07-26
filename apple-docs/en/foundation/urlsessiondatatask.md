---
title: URLSessionDataTask
framework: Foundation
symbol_kind: class
role: symbol
role_heading: Class
platforms: [iOS 7.0+, iPadOS 7.0+, Mac Catalyst 13.1+, macOS 10.9+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/urlsessiondatatask
source_url: 'https://developer.apple.com/documentation/foundation/urlsessiondatatask'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/urlsessiondatatask.json'
content_hash: 'sha256:56622af1d202aa5c'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Foundation](../foundation.md)

# URLSessionDataTask

<sub>Class</sub>

A URL session task that returns downloaded data directly to the app in memory.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
class URLSessionDataTask
```

## Overview

A [URLSessionDataTask](urlsessiondatatask.md) is a concrete subclass of [URLSessionTask](urlsessiontask.md). The methods in the [URLSessionDataTask](urlsessiondatatask.md) class are documented in [URLSessionTask](urlsessiontask.md).

A data task returns data directly to the app (in memory) as one or more `NSData` objects. When you use a data task:

- During upload of the body data (if your app provides any), the session periodically calls its delegate’s [- URLSession:task:didSendBodyData:totalBytesSent:totalBytesExpectedToSend:](<urlsessiontaskdelegate/urlsession(__task_didsendbodydata_totalbytessent_totalbytesexpectedtosend_).md>) method with status information.
- After receiving an initial response, the session calls its delegate’s [- URLSession:dataTask:didReceiveResponse:completionHandler:](<urlsessiondatadelegate/urlsession(__datatask_didreceive_completionhandler_).md>) method to let you examine the status code and headers, and optionally convert the data task into a download task.
- During the transfer, the session calls its delegate’s [- URLSession:dataTask:didReceiveData:](<urlsessiondatadelegate/urlsession(__datatask_didreceive_).md>) method to provide your app with the content as it arrives.
- Upon completion, the session calls its delegate’s [- URLSession:dataTask:willCacheResponse:completionHandler:](<urlsessiondatadelegate/urlsession(__datatask_willcacheresponse_completionhandler_).md>) method to let you determine whether the response should be cached.

For examples of using data tasks for fetching and uploading data, see [Fetching website data into memory](fetching-website-data-into-memory.md) and [Uploading data to a website](uploading-data-to-a-website.md).

## Relationships

- **Inherits From**: [URLSessionTask](urlsessiontask.md)

- **Inherited By**: [URLSessionUploadTask](urlsessionuploadtask.md)

- **Conforms To**: [CVarArg](../swift/cvararg.md), [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md), [CustomStringConvertible](../swift/customstringconvertible.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [NSCopying](nscopying.md), [NSObjectProtocol](../objectivec/nsobjectprotocol.md), [ProgressReporting](progressreporting.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md)

## Topics

### Initializers

- [- init](<urlsessiondatatask/init().md>) _(deprecated)_

### Type Methods

- [+ new](<urlsessiondatatask/new().md>) _(deprecated)_

## See Also

### Adding data tasks to a session

- [- dataTaskWithURL:](<urlsession/datatask(with_)-10dy7.md>) — Creates a task that retrieves the contents of the specified URL.
- [- dataTaskWithURL:completionHandler:](<urlsession/datatask(with_completionhandler_)-52wk8.md>) — Creates a task that retrieves the contents of the specified URL, then calls a handler upon completion.
- [- dataTaskWithRequest:](<urlsession/datatask(with_)-7jpys.md>) — Creates a task that retrieves the contents of a URL based on the specified URL request object.
- [- dataTaskWithRequest:completionHandler:](<urlsession/datatask(with_completionhandler_)-e6xv.md>) — Creates a task that retrieves the contents of a URL based on the specified URL request object, and calls a handler upon completion.
- [URLSessionDataDelegate](urlsessiondatadelegate.md) — A protocol that defines methods that URL session instances call on their delegates to handle task-level events specific to data and upload tasks.
