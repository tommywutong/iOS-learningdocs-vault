---
title: URLSession
framework: Foundation
symbol_kind: class
role: symbol
role_heading: Class
platforms: [iOS 7.0+, iPadOS 7.0+, Mac Catalyst 13.1+, macOS 10.9+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/urlsession
source_url: 'https://developer.apple.com/documentation/foundation/urlsession'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/urlsession.json'
content_hash: 'sha256:cee884a7ed657445'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Foundation](../foundation.md)

# URLSession

<sub>Class</sub>

An object that coordinates a group of related, network data transfer tasks.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
class URLSession
```

## Overview

The [URLSession](urlsession.md) class and related classes provide an API for downloading data from and uploading data to endpoints indicated by URLs. Your app can also use this API to perform background downloads when your app isn’t running or, in iOS, while your app is suspended. You can use the related [URLSessionDelegate](urlsessiondelegate.md) and [URLSessionTaskDelegate](urlsessiontaskdelegate.md) to support authentication and receive events like redirection and task completion.

> [!note] Note
> The [URLSession](urlsession.md) API involves many different classes that work together in a fairly complex way which may not be obvious if you read the reference documentation by itself. Before using the API, read the overview in the [URL Loading System](url-loading-system.md) topic. The articles in the Essentials, Uploading, and Downloading sections offer examples of performing common tasks with [URLSession](urlsession.md).

Your app creates one or more [URLSession](urlsession.md) instances, each of which coordinates a group of related data-transfer tasks. For example, if you’re creating a web browser, your app might create one session per tab or window, or one session for interactive use and another for background downloads. Within each session, your app adds a series of tasks, each of which represents a request for a specific URL (following HTTP redirects, if necessary).

### Types of URL sessions

The tasks within a given URL session share a common session configuration object, which defines connection behavior, like the maximum number of simultaneous connections to make to a single host, whether connections can use the cellular network, and so on.

[URLSession](urlsession.md) has a singleton [sharedSession](urlsession/shared.md) session (which doesn’t have a configuration object) for basic requests. It’s not as customizable as sessions you create, but it serves as a good starting point if you have very limited requirements. You access this session by calling the shared class method. For other kinds of sessions, you create a [URLSession](urlsession.md) with one of three kinds of configurations:

- A default session behaves much like the shared session, but lets you configure it. You can also assign a delegate to the default session to obtain data incrementally.
- Ephemeral sessions are similar to shared sessions, but don’t write caches, cookies, or credentials to disk.
- Background sessions let you perform uploads and downloads of content in the background while your app isn’t running.

See Creating a session configuration object in the [URLSessionConfiguration](urlsessionconfiguration.md) class for details on creating each type of configuration.

### Types of URL session tasks

Within a session, you create tasks that optionally upload data to a server and then retrieve data from the server either as a file on disk or as one or more [NSData](nsdata.md) objects in memory. The [URLSession](urlsession.md) API provides four types of tasks:

- Data tasks send and receive data using [NSData](nsdata.md) objects. Data tasks are intended for short, often interactive requests to a server.
- Upload tasks are similar to data tasks, but they also send data (often in the form of a file), and support background uploads while the app isn’t running.
- Download tasks retrieve data in the form of a file, and support background downloads and uploads while the app isn’t running.
- WebSocket tasks exchange messages over TCP and TLS, using the WebSocket protocol defined in [RFC 6455](https://tools.ietf.org/html/rfc6455).

### Using a session delegate

Tasks in a session also share a common delegate object. You implement this delegate to provide and obtain information when various events occur, including when:

- Authentication fails.
- Data arrives from the server.
- Data becomes available for caching.

If you don’t need the features provided by a delegate, you can use this API without providing one by passing `nil` when you create a session.

> [!important] Important
> The session object keeps a strong reference to the delegate until your app exits or explicitly invalidates the session. If you don’t invalidate the session, your app leaks memory until the app terminates.

Each task you create with the session calls back to the session’s delegate, using the methods defined in [URLSessionTaskDelegate](urlsessiontaskdelegate.md). You can also intercept these callbacks before they reach the session delegate by populating a separate [delegate](urlsessiontask/delegate.md) that’s specific to the task.

### Asynchronicity and URL sessions

Like most networking APIs, the [URLSession](urlsession.md) API is highly asynchronous. It returns data to your app in one of three ways, depending on the methods you call:

- If you’re using Swift, you can use the methods marked with the `async` keyword to perform common tasks. For example, [data(from:delegate:)](<urlsession/data(from_delegate_).md>) fetches data, while [download(from:delegate:)](<urlsession/download(from_delegate_).md>) downloads files. Your call point uses the `await` keyword to suspend running until the transfer completes. You can also use the [bytes(from:delegate:)](<urlsession/bytes(from_delegate_).md>) method to receive data as an [AsyncSequence](../swift/asyncsequence.md). With this approach, you use the `for`-`await`-`in` syntax to iterate over the data as your app receives it. The [URL](url.md) type also offers covenience methods to fetch bytes or lines from the shared URL session.
- In Swift or Objective-C, you can provide a completion handler block, which runs when the transfer completes.
- In Swift or Objective-C, you can receive callbacks to a delegate method as the transfer progresses and immediately after it completes.

In addition to delivering this information to delegates, the [URLSession](urlsession.md) provides status and progress properties. Query these properties if you need to make programmatic decisions based on the current state of the task (with the caveat that its state can change at any time).

### Protocol support

The [URLSession](urlsession.md) class natively supports the `data`, `file`, `ftp`, `http`, and `https` URL schemes, with transparent support for proxy servers and SOCKS gateways, as configured in the user’s system preferences.

[URLSession](urlsession.md) supports the HTTP/1.1, HTTP/2, and HTTP/3 protocols. HTTP/2 support, as described by [RFC 7540](https://tools.ietf.org/html/rfc7540), requires a server that supports Application-Layer Protocol Negotiation (ALPN).

You can also add support for your own custom networking protocols and URL schemes (for your app’s private use) by subclassing [URLProtocol](urlprotocol.md).

### App Transport Security (ATS)

iOS 9.0 and macOS 10.11 and later use App Transport Security (ATS) for all HTTP connections made with [URLSession](urlsession.md). ATS requires that HTTP connections use HTTPS ([RFC 2818](https://tools.ietf.org/html/rfc2818)).

For more information, see [NSAppTransportSecurity](../bundleresources/information-property-list/nsapptransportsecurity.md).

### Foundation copying behavior

Session and task objects conform to the [NSCopying](nscopying.md) protocol as follows:

- When your app copies a session or task object, you get the same object back.
- When your app copies a configuration object, you get a new copy you can independently modify.

### Thread safety

The URL session API is thread-safe. You can freely create sessions and tasks in any thread context. When your delegate methods call the provided completion handlers, the work is automatically scheduled on the correct delegate queue.

## Relationships

- **Inherits From**: [NSObject](../objectivec/nsobject-swift.class.md)

- **Conforms To**: [CVarArg](../swift/cvararg.md), [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md), [CustomStringConvertible](../swift/customstringconvertible.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [NSObjectProtocol](../objectivec/nsobjectprotocol.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md)

## Topics

### Using the shared session

- [sharedSession](urlsession/shared.md) — The shared singleton session object.

### Creating a session

- [+ sessionWithConfiguration:](<urlsession/init(configuration_).md>) — Creates a session with the specified session configuration.
- [+ sessionWithConfiguration:delegate:delegateQueue:](<urlsession/init(configuration_delegate_delegatequeue_).md>) — Creates a session with the specified session configuration, delegate, and operation queue.
- [URLSessionConfiguration](urlsessionconfiguration.md) — A configuration object that defines behavior and policies for a URL session.
- [configuration](urlsession/configuration.md) — A copy of the configuration object for this session.

### Working with a delegate

- [delegate](urlsession/delegate.md) — The delegate assigned when this object was created.
- [URLSessionDelegate](urlsessiondelegate.md) — A protocol that defines methods that URL session instances call on their delegates to handle session-level events, like session life cycle changes.
- [URLSessionTaskDelegate](urlsessiontaskdelegate.md) — A protocol that defines methods that URL session instances call on their delegates to handle task-level events.
- [delegateQueue](urlsession/delegatequeue.md) — The operation queue provided when this object was created.

### Performing asynchronous transfers

- [bytes(for:delegate:)](<urlsession/bytes(for_delegate_).md>) — Retrieves the contents of a URL based on the specified URL request and delivers an asynchronous sequence of bytes.
- [bytes(from:delegate:)](<urlsession/bytes(from_delegate_).md>) — Retrieves the contents of a given URL and delivers an asynchronous sequence of bytes.
- [AsyncBytes](urlsession/asyncbytes.md) — An asynchronous sequence of bytes.
- [data(for:delegate:)](<urlsession/data(for_delegate_).md>) — Downloads the contents of a URL based on the specified URL request and delivers the data asynchronously.
- [data(from:delegate:)](<urlsession/data(from_delegate_).md>) — Retrieves the contents of a URL and delivers the data asynchronously.
- [data(for:)](<urlsession/data(for_).md>) — Convenience method to load data using a URLRequest, creates and resumes a URLSessionDataTask internally.
- [data(from:)](<urlsession/data(from_).md>) — Convenience method to load data using a URL, creates and resumes a URLSessionDataTask internally.
- [download(for:delegate:)](<urlsession/download(for_delegate_).md>) — Retrieves the contents of a URL based on the specified URL request and delivers the URL of the saved file asynchronously.
- [download(from:delegate:)](<urlsession/download(from_delegate_).md>) — Retrieves the contents of a URL and delivers the URL of the saved file asynchronously.
- [download(resumeFrom:delegate:)](<urlsession/download(resumefrom_delegate_).md>) — Resumes a previously-paused download and delivers the URL of the saved file asynchronously.
- [upload(for:from:delegate:)](<urlsession/upload(for_from_delegate_).md>) — Uploads data to a URL based on the specified URL request and delivers the result asynchronously.
- [upload(for:fromFile:delegate:)](<urlsession/upload(for_fromfile_delegate_).md>) — Uploads data to a URL and delivers the result asynchronously.
- [upload(for:from:)](<urlsession/upload(for_from_).md>) — Convenience method to upload data using a URLRequest, creates and resumes a URLSessionUploadTask internally.
- [upload(for:fromFile:)](<urlsession/upload(for_fromfile_).md>) — Convenience method to upload data using a URLRequest, creates and resumes a URLSessionUploadTask internally.
- [URLSessionTaskDelegate](urlsessiontaskdelegate.md) — A protocol that defines methods that URL session instances call on their delegates to handle task-level events.

### Adding data tasks to a session

- [- dataTaskWithURL:](<urlsession/datatask(with_)-10dy7.md>) — Creates a task that retrieves the contents of the specified URL.
- [- dataTaskWithURL:completionHandler:](<urlsession/datatask(with_completionhandler_)-52wk8.md>) — Creates a task that retrieves the contents of the specified URL, then calls a handler upon completion.
- [- dataTaskWithRequest:](<urlsession/datatask(with_)-7jpys.md>) — Creates a task that retrieves the contents of a URL based on the specified URL request object.
- [- dataTaskWithRequest:completionHandler:](<urlsession/datatask(with_completionhandler_)-e6xv.md>) — Creates a task that retrieves the contents of a URL based on the specified URL request object, and calls a handler upon completion.
- [URLSessionDataTask](urlsessiondatatask.md) — A URL session task that returns downloaded data directly to the app in memory.
- [URLSessionDataDelegate](urlsessiondatadelegate.md) — A protocol that defines methods that URL session instances call on their delegates to handle task-level events specific to data and upload tasks.

### Adding download tasks to a session

- [- downloadTaskWithURL:](<urlsession/downloadtask(with_)-1onj.md>) — Creates a download task that retrieves the contents of the specified URL and saves the results to a file.
- [- downloadTaskWithURL:completionHandler:](<urlsession/downloadtask(with_completionhandler_)-7cuje.md>) — Creates a download task that retrieves the contents of the specified URL, saves the results to a file, and calls a handler upon completion.
- [- downloadTaskWithRequest:](<urlsession/downloadtask(with_)-3fb7s.md>) — Creates a download task that retrieves the contents of a URL based on the specified URL request object and saves the results to a file.
- [- downloadTaskWithRequest:completionHandler:](<urlsession/downloadtask(with_completionhandler_)-4a84s.md>) — Creates a download task that retrieves the contents of a URL based on the specified URL request object, saves the results to a file, and calls a handler upon completion.
- [- downloadTaskWithResumeData:](<urlsession/downloadtask(withresumedata_).md>) — Creates a download task to resume a previously canceled or failed download.
- [- downloadTaskWithResumeData:completionHandler:](<urlsession/downloadtask(withresumedata_completionhandler_).md>) — Creates a download task to resume a previously canceled or failed download and calls a handler upon completion.
- [URLSessionDownloadTask](urlsessiondownloadtask.md) — A URL session task that stores downloaded data to a file.
- [URLSessionDownloadDelegate](urlsessiondownloaddelegate.md) — A protocol that defines methods that URL session instances call on their delegates to handle task-level events specific to download tasks.

### Adding upload tasks to a session

- [Building a resumable upload server with SwiftNIO](building-a-resumable-upload-server-with-swiftnio.md) — Support HTTP resumable upload protocol in SwiftNIO by translating resumable uploads to regular uploads.
- [- uploadTaskWithRequest:fromData:](<urlsession/uploadtask(with_from_).md>) — Creates a task that performs an HTTP request for the specified URL request object and uploads the provided data.
- [- uploadTaskWithRequest:fromData:completionHandler:](<urlsession/uploadtask(with_from_completionhandler_).md>) — Creates a task that performs an HTTP request for the specified URL request object, uploads the provided data, and calls a handler upon completion.
- [- uploadTaskWithRequest:fromFile:](<urlsession/uploadtask(with_fromfile_).md>) — Creates a task that performs an HTTP request for uploading the specified file.
- [- uploadTaskWithRequest:fromFile:completionHandler:](<urlsession/uploadtask(with_fromfile_completionhandler_).md>) — Creates a task that performs an HTTP request for uploading the specified file, then calls a handler upon completion.
- [- uploadTaskWithStreamedRequest:](<urlsession/uploadtask(withstreamedrequest_).md>) — Creates a task that performs an HTTP request for uploading data based on the specified URL request.
- [- uploadTaskWithResumeData:](<urlsession/uploadtask(withresumedata_).md>) — Creates an upload task from a resume data blob. Requires the server to support the latest resumable uploads Internet-Draft from the HTTP Working Group, found at https://datatracker.ietf.org/doc/draft-ietf-httpbis-resumable-upload/ If resuming from an upload file, the file must still exist and be unmodified. If the upload cannot be successfully resumed, URLSession:task:didCompleteWithError: will be called.
- [- uploadTaskWithResumeData:completionHandler:](<urlsession/uploadtask(withresumedata_completionhandler_).md>) — Creates a URLSessionUploadTask from a resume data blob. If resuming from an upload file, the file must still exist and be unmodified.
- [URLSessionUploadTask](urlsessionuploadtask.md) — A URL session task that uploads data to the network in a request body.
- [URLSessionDataDelegate](urlsessiondatadelegate.md) — A protocol that defines methods that URL session instances call on their delegates to handle task-level events specific to data and upload tasks.

### Adding stream tasks to a session

- [- streamTaskWithHostName:port:](<urlsession/streamtask(withhostname_port_).md>) — Creates a task that establishes a bidirectional TCP/IP connection to a specified hostname and port.
- [- streamTaskWithNetService:](<urlsession/streamtask(with_).md>) — Creates a task that establishes a bidirectional TCP/IP connection using a specified network service. _(deprecated)_
- [URLSessionStreamTask](urlsessionstreamtask.md) — A URL session task that is stream-based.
- [URLSessionStreamDelegate](urlsessionstreamdelegate.md) — A protocol that defines methods that URL session instances call on their delegates to handle task-level events specific to stream tasks.

### Adding WebSocket tasks to a session

- [- webSocketTaskWithURL:](<urlsession/websockettask(with_)-87ipz.md>) — Creates a WebSocket task for the provided URL.
- [- webSocketTaskWithRequest:](<urlsession/websockettask(with_)-mtks.md>) — Creates a WebSocket task for the provided URL request.
- [- webSocketTaskWithURL:protocols:](<urlsession/websockettask(with_protocols_).md>) — Creates a WebSocket task given a URL and an array of protocols.
- [URLSessionWebSocketTask](urlsessionwebsockettask.md) — A URL session task that communicates over the WebSockets protocol standard.
- [URLSessionWebSocketDelegate](urlsessionwebsocketdelegate.md) — A protocol that defines methods that URL session instances call on their delegates to handle task-level events specific to WebSocket tasks.

### Managing the session

- [- finishTasksAndInvalidate](<urlsession/finishtasksandinvalidate().md>) — Invalidates the session, allowing any outstanding tasks to finish.
- [- flushWithCompletionHandler:](<urlsession/flush(completionhandler_).md>) — Flushes cookies and credentials to disk, clears transient caches, and ensures that future requests occur on a new TCP connection.
- [- getTasksWithCompletionHandler:](<urlsession/gettaskswithcompletionhandler(__).md>) — Asynchronously calls a completion callback with all data, upload, and download tasks in a session.
- [- getAllTasksWithCompletionHandler:](<urlsession/getalltasks(completionhandler_).md>) — Asynchronously calls a completion callback with all tasks in a session
- [- invalidateAndCancel](<urlsession/invalidateandcancel().md>) — Cancels all outstanding tasks and then invalidates the session.
- [- resetWithCompletionHandler:](<urlsession/reset(completionhandler_).md>) — Empties all cookies, caches and credential stores, removes disk files, flushes in-progress downloads to disk, and ensures that future requests occur on a new socket.
- [sessionDescription](urlsession/sessiondescription.md) — An app-defined descriptive label for the session.

### Handling errors

- [URL session error dictionary keys](url-session-error-dictionary-keys.md) — Keys used in conjunction with error objects returned by URL sessions and tasks.
- [Background task cancellation](background-task-cancellation.md) — Constants that indicate why a background task was canceled.

### Performing tasks as a Combine Publisher

- [Processing URL session data task results with Combine](processing-url-session-data-task-results-with-combine.md) — Use a chain of asynchronous operators to receive and process data fetched from a URL.
- [dataTaskPublisher(for:)](<urlsession/datataskpublisher(for_)-61v3e.md>) — Returns a publisher that wraps a URL session data task for a given URL request.
- [dataTaskPublisher(for:)](<urlsession/datataskpublisher(for_)-5kiir.md>) — Returns a publisher that wraps a URL session data task for a given URL.
- [DataTaskPublisher](urlsession/datataskpublisher.md) — A publisher that delivers the results of performing URL session data tasks.

### Deprecated

- [+ new](<urlsession/new().md>) _(deprecated)_
- [- init](<urlsession/init().md>) _(deprecated)_

## See Also

### Essentials

- [Fetching website data into memory](fetching-website-data-into-memory.md) — Receive data directly into memory by creating a data task from a URL session.
- [Analyzing HTTP traffic with Instruments](analyzing-http-traffic-with-instruments.md) — Measure HTTP-based network performance and usage of your apps.
- [URLSessionTask](urlsessiontask.md) — A task, like downloading a specific resource, performed in a URL session.
