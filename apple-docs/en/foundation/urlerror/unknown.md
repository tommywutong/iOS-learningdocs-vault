---
title: unknown
framework: Foundation
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 8.0+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/foundation/urlerror/unknown
source_url: 'https://developer.apple.com/documentation/foundation/urlerror/unknown'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/urlerror/unknown.json'
content_hash: 'sha256:a8e1001c838e6571'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [URLError](../urlerror.md)

# unknown

<sub>Type Property</sub>

The URL Loading System encountered an error that it can’t interpret.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
static var unknown: URLError.Code { get }
```

## Discussion

This can occur when an error originates from a lower level framework or library. Whenever this error code is received, it is a bug, and should be reported to Apple.

## See Also

### Error codes

- [appTransportSecurityRequiresSecureConnection](apptransportsecurityrequiressecureconnection.md) — App Transport Security disallowed a connection because there is no secure network connection.
- [backgroundSessionInUseByAnotherProcess](backgroundsessioninusebyanotherprocess.md) — An app or app extension attempted to connect to a background session that is already connected to a process.
- [backgroundSessionRequiresSharedContainer](backgroundsessionrequiressharedcontainer.md) — The shared container identifier of the URL session configuration is needed but hasn’t been set.
- [backgroundSessionWasDisconnected](backgroundsessionwasdisconnected.md) — The app is suspended or exits while a background data task is processing.
- [badServerResponse](badserverresponse.md) — The URL Loading System received bad data from the server.
- [badURL](badurl.md) — A malformed URL prevented a URL request from being initiated.
- [callIsActive](callisactive.md) — A connection was attempted while a phone call is active on a network that doesn’t support simultaneous phone and data communication, such as EDGE or GPRS.
- [cancelled](cancelled.md) — An asynchronous load has been canceled.
- [cannotCloseFile](cannotclosefile.md) — A download task couldn’t close the downloaded file on disk.
- [cannotConnectToHost](cannotconnecttohost.md) — An attempt to connect to a host failed.
- [cannotCreateFile](cannotcreatefile.md) — A download task couldn’t create the downloaded file on disk because of an I/O failure.
- [cannotDecodeContentData](cannotdecodecontentdata.md) — Content data received during a connection request had an unknown content encoding.
- [cannotDecodeRawData](cannotdecoderawdata.md) — Content data received during a connection request couldn’t be decoded for a known content encoding.
- [cannotFindHost](cannotfindhost.md) — The host name for a URL couldn’t be resolved.
- [cannotLoadFromNetwork](cannotloadfromnetwork.md) — A request to load an item only from the cache could not be satisfied.
