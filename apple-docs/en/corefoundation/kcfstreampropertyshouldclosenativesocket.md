---
title: kCFStreamPropertyShouldCloseNativeSocket
framework: Core Foundation
symbol_kind: var
role: symbol
role_heading: Global Variable
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.1+, macOS 10.2+, tvOS, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/corefoundation/kcfstreampropertyshouldclosenativesocket
source_url: 'https://developer.apple.com/documentation/corefoundation/kcfstreampropertyshouldclosenativesocket'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/corefoundation/kcfstreampropertyshouldclosenativesocket.json'
content_hash: 'sha256:0af8e68e7be158e4'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Foundation](../corefoundation.md)

# kCFStreamPropertyShouldCloseNativeSocket

<sub>Global Variable</sub>

Should Close Native Socket property key.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
let kCFStreamPropertyShouldCloseNativeSocket: CFString
```

## Discussion

If set to `kCFBooleanTrue`, the stream will close and release the underlying native socket when the stream is released. If set to `kCFBooleanFalse`, the stream will not close and release the underlying native socket when the stream is released. If a stream is created with a native socket, the default value of this property is `kCFBooleanFalse`. This property is only available for socket streams. It can be set by calling [CFReadStreamSetProperty](<cfreadstreamsetproperty(______).md>) and [CFWriteStreamSetProperty](<cfwritestreamsetproperty(______).md>), and it can be copied by [CFReadStreamCopyProperty](<cfreadstreamcopyproperty(____).md>) and [CFWriteStreamCopyProperty](<cfwritestreamcopyproperty(____).md>).

## See Also

### Constants

- [kCFStreamPropertyAppendToFile](cfstreampropertykey/appendtofile.md) — Value is a `CFBoolean` value that indicates whether to append the written data to a file, if it already exists, rather than to replace its contents.
- [kCFStreamPropertyDataWritten](cfstreampropertykey/datawritten.md) — Value is a `CFData` object that contains all the bytes written to a writable memory stream. You cannot modify this value.
- [kCFStreamPropertyFileCurrentOffset](cfstreampropertykey/filecurrentoffset.md) — Value is a `CFNumber` object containing the current file offset.
- [kCFStreamPropertySocketNativeHandle](cfstreampropertykey/socketnativehandle.md) — Value is a `CFData` object that contains the native handle for a socket stream—of type [CFSocketNativeHandle](cfsocketnativehandle.md)—to which the socket stream is connected.
- [kCFStreamPropertySocketRemoteHostName](cfstreampropertykey/socketremotehostname.md) — Value is a `CFString` object containing the name of the host to which the socket stream is connected or `NULL` if unknown.
- [kCFStreamPropertySocketRemotePortNumber](cfstreampropertykey/socketremoteportnumber.md) — Value is a `CFNumber` object containing the remote port number to which the socket stream is connected or `NULL` if unknown.
- [kCFStreamPropertySocketSecurityLevel](kcfstreampropertysocketsecuritylevel.md) — Socket Security Level property key.
- [kCFStreamPropertySSLPeerCertificates](../cfnetwork/kcfstreampropertysslpeercertificates.md) — SSL Peer Certificates property key for copy operations, which return a `CFArray` object containing `SecCertificateRef` objects. _(deprecated)_
- [kCFStreamPropertySSLPeerTrust](../cfnetwork/kcfstreampropertysslpeertrust.md) — SSL Peer Trust property key for copy operations, which return a `SecTrustRef` object containing the result of the SSL handshake.
- [kCFStreamPropertySSLSettings](../cfnetwork/kcfstreampropertysslsettings.md) — SSL Settings property key for set operations.
- [kCFStreamPropertySSLContext](../cfnetwork/kcfstreampropertysslcontext.md)
- [kCFStreamPropertySOCKSProxy](kcfstreampropertysocksproxy.md) — SOCKS proxy property key.
- [kCFStreamPropertyProxyLocalBypass](../cfnetwork/kcfstreampropertyproxylocalbypass.md) — Proxy Local Bypass property key.
- [kCFStreamPropertySocketRemoteHost](../cfnetwork/kcfstreampropertysocketremotehost.md) — The key’s value is a `CFHostRef` for the remote host if it is known. If not, its value is `NULL`.
- [kCFStreamPropertySocketRemoteNetService](../cfnetwork/kcfstreampropertysocketremotenetservice.md) — The key’s value is a `CFNetServiceRef` for the remote network service if it is known. If not, its value is `NULL`.
