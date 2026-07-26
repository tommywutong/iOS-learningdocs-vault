---
title: NSURLErrorBackgroundSessionWasDisconnected
framework: Foundation
symbol_kind: var
role: symbol
role_heading: Global Variable
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.1+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/foundation/nsurlerrorbackgroundsessionwasdisconnected-swift.var
source_url: 'https://developer.apple.com/documentation/foundation/nsurlerrorbackgroundsessionwasdisconnected-swift.var'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsurlerrorbackgroundsessionwasdisconnected-swift.var.json'
content_hash: 'sha256:24f25bff39681494'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Foundation](../foundation.md)

# NSURLErrorBackgroundSessionWasDisconnected

<sub>Global Variable</sub>

The app is suspended or exits while a background data task is processing.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var NSURLErrorBackgroundSessionWasDisconnected: Int { get }
```

## Discussion

If your app has created a background data task and the app is then suspended, the task will fail with this error code. To prevent this, when you receive the response, convert the data task to a download task.

## See Also

### URL Errors

- [NSURLErrorAppTransportSecurityRequiresSecureConnection](nsurlerrorapptransportsecurityrequiressecureconnection-swift.var.md) — App Transport Security disallowed a connection because there is no secure network connection.
- [NSURLErrorBackgroundSessionInUseByAnotherProcess](nsurlerrorbackgroundsessioninusebyanotherprocess-swift.var.md) — An app or app extension attempted to connect to a background session that is already connected to a process.
- [NSURLErrorBackgroundSessionRequiresSharedContainer](nsurlerrorbackgroundsessionrequiressharedcontainer-swift.var.md) — The shared container identifier of the URL session configuration is needed but hasn’t been set.
- [NSURLErrorBadServerResponse](nsurlerrorbadserverresponse-swift.var.md) — The URL Loading System received bad data from the server.
- [NSURLErrorBadURL](nsurlerrorbadurl-swift.var.md) — A malformed URL prevented a URL request from being initiated.
- [NSURLErrorCallIsActive](nsurlerrorcallisactive-swift.var.md) — A connection was attempted while a phone call was active on a network that doesn’t support simultaneous phone and data communication, such as EDGE or GPRS.
- [NSURLErrorCancelled](nsurlerrorcancelled-swift.var.md) — An asynchronous load has been canceled.
- [NSURLErrorCannotCloseFile](nsurlerrorcannotclosefile-swift.var.md) — A download task couldn’t close the downloaded file on disk.
- [NSURLErrorCannotConnectToHost](nsurlerrorcannotconnecttohost-swift.var.md) — An attempt to connect to a host failed.
- [NSURLErrorCannotCreateFile](nsurlerrorcannotcreatefile-swift.var.md) — A download task couldn’t create the downloaded file on disk because of an I/O failure.
- [NSURLErrorCannotDecodeContentData](nsurlerrorcannotdecodecontentdata-swift.var.md) — Content data received during a connection request had an unknown content encoding.
- [NSURLErrorCannotDecodeRawData](nsurlerrorcannotdecoderawdata-swift.var.md) — Content data received during a connection request couldn’t be decoded for a known content encoding.
- [NSURLErrorCannotFindHost](nsurlerrorcannotfindhost-swift.var.md) — The host name for a URL couldn’t be resolved.
- [NSURLErrorCannotLoadFromNetwork](nsurlerrorcannotloadfromnetwork-swift.var.md) — A specific request to load an item only from the cache couldn’t be satisfied.
- [NSURLErrorCannotMoveFile](nsurlerrorcannotmovefile-swift.var.md) — A downloaded file on disk couldn’t be moved.
