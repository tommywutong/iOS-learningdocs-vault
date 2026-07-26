---
title: appTransportSecurityRequiresSecureConnection
framework: Foundation
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 9.0+, iPadOS 9.0+, Mac Catalyst 9.0+, macOS 10.11+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/foundation/urlerror/code/apptransportsecurityrequiressecureconnection
source_url: 'https://developer.apple.com/documentation/foundation/urlerror/code/apptransportsecurityrequiressecureconnection'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/urlerror/code/apptransportsecurityrequiressecureconnection.json'
content_hash: 'sha256:a4b4bf3a8c2069e5'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [Foundation](../../../foundation.md) · [URLError](../../urlerror.md) · [Code](../code.md)

# appTransportSecurityRequiresSecureConnection

<sub>Type Property</sub>

App Transport Security disallowed a connection because there is no secure network connection.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
static var appTransportSecurityRequiresSecureConnection: URLError.Code { get }
```

## Discussion

Starting in iOS 9.0 and macOS v10.11, App Transport Security (ATS) is enabled by default for connections created by URLSession. ATS requires the use of best practice secure protocols in HTTPS. For more information on ATS, see [NSAppTransportSecurity](https://developer.apple.com/library/archive/documentation/General/Reference/InfoPlistKeyReference/Articles/CocoaKeys.html#//apple_ref/doc/plist/info/NSAppTransportSecurity) in  [Information Property List Key Reference](https://developer.apple.com/library/archive/documentation/General/Reference/InfoPlistKeyReference/Introduction/Introduction.html#//apple_ref/doc/uid/TP40009247).

## See Also

### Error codes

- [backgroundSessionInUseByAnotherProcess](backgroundsessioninusebyanotherprocess.md) — An app or app extension attempted to connect to a background session that is already connected to a process.
- [backgroundSessionRequiresSharedContainer](backgroundsessionrequiressharedcontainer.md) — The shared container identifier of the URL session configuration is needed but has not been set.
- [backgroundSessionWasDisconnected](backgroundsessionwasdisconnected.md) — The app is suspended or exits while a background data task is processing.
- [badServerResponse](badserverresponse.md) — The URL Loading system received bad data from the server.
- [badURL](badurl.md) — A malformed URL prevented a URL request from being initiated.
- [callIsActive](callisactive.md) — A connection was attempted while a phone call is active on a network that does not support simultaneous phone and data communication (EDGE or GPRS).
- [cancelled](cancelled.md) — An asynchronous load has been canceled.
- [cannotCloseFile](cannotclosefile.md) — A download task couldn’t close the downloaded file on disk.
- [cannotConnectToHost](cannotconnecttohost.md) — An attempt to connect to a host failed.
- [cannotCreateFile](cannotcreatefile.md) — A download task couldn’t create the downloaded file on disk because of an I/O failure.
- [cannotDecodeContentData](cannotdecodecontentdata.md) — Content data received during a connection request had an unknown content encoding.
- [cannotDecodeRawData](cannotdecoderawdata.md) — Content data received during a connection request could not be decoded for a known content encoding.
- [cannotFindHost](cannotfindhost.md) — The host name for a URL could not be resolved.
- [cannotLoadFromNetwork](cannotloadfromnetwork.md) — A request to load an item only from the cache could not be satisfied.
- [cannotMoveFile](cannotmovefile.md) — A download task was unable to move a downloaded file on disk.
