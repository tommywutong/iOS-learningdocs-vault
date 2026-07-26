---
title: 'sendSynchronousRequest(_:returning:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [iOS 2.0+（9.0 起废弃）, iPadOS 2.0+（9.0 起废弃）, Mac Catalyst 13.1+（13.1 起废弃）, macOS 10.3+（10.11 起废弃）, tvOS 9.0+（9.0 起废弃）, visionOS 1.0+（1.0 起废弃）]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: '/documentation/foundation/nsurlconnection/sendsynchronousrequest(_:returning:)'
source_url: 'https://developer.apple.com/documentation/foundation/nsurlconnection/sendsynchronousrequest(_:returning:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsurlconnection/sendsynchronousrequest%28_%3Areturning%3A%29.json'
content_hash: 'sha256:ef7bb3fa654d9f00'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSURLConnection](../nsurlconnection.md)

# sendSynchronousRequest(_:returning:)

<sub>Type Method</sub>

Performs a synchronous load of the specified URL request.

> [!warning] Deprecated
> Use [NSURLSession dataTaskWithRequest:completionHandler:] (see NSURLSession.h

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
class func sendSynchronousRequest(_ request: URLRequest, returning response: AutoreleasingUnsafeMutablePointer<URLResponse?>?) throws -> Data
```

## Parameters

- `request` — The URL request to load. The `request` object is deep-copied as part of the initialization process. Changes made to `request` after this method returns do not affect the request that is used for the loading process.

- `response` — Out parameter for the URL response returned by the server.

## Return Value

The downloaded data for the URL request. Returns `nil` if a connection could not be created or if the download fails.

## Discussion

A synchronous load is built on top of the asynchronous loading code made available by the class. The calling thread is blocked while the asynchronous loading system performs the URL load on a thread spawned specifically for this load request. No special threading or run loop configuration is necessary in the calling thread in order to perform a synchronous load.

> [!important] Important
> Because this call can potentially take several minutes to complete (particularly when using a cellular network in iOS), you should never call this function from the main thread of your application. Doing so may cause a `0x8badf00d` exception with the main thread at `mach_msg_trap`. The solution is to migrate to URL loading using [URLSession](../urlsession.md).

If authentication is required in order to download the request, the required credentials must be specified as part of the URL. If authentication fails, or credentials are missing, the connection will attempt to continue without credentials.

> [!note] Handling Errors in Swift
> In Swift, this method returns a nonoptional result and is marked with the `throws` keyword to indicate that it throws an error in cases of failure.
>
> You call this method in a `try` expression and handle any errors in the `catch` clauses of a `do` statement, as described in [Error Handling](https://docs.swift.org/swift-book/LanguageGuide/ErrorHandling.html) in [The Swift Programming Language](https://docs.swift.org/swift-book/) and `About Imported Cocoa Error Parameters`.
