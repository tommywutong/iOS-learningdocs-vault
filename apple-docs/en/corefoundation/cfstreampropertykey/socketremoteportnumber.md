---
title: socketRemotePortNumber
framework: Core Foundation
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/corefoundation/cfstreampropertykey/socketremoteportnumber
source_url: 'https://developer.apple.com/documentation/corefoundation/cfstreampropertykey/socketremoteportnumber'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/corefoundation/cfstreampropertykey/socketremoteportnumber.json'
content_hash: 'sha256:b589cf822543b33d'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Foundation](../../corefoundation.md) · [CFStreamPropertyKey](../cfstreampropertykey.md)

# socketRemotePortNumber

<sub>Type Property</sub>

Value is a `CFNumber` object containing the remote port number to which the socket stream is connected or `NULL` if unknown.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
static let socketRemotePortNumber: CFStreamPropertyKey!
```

## Discussion

You cannot modify this value. You can read this value at any time.]

## See Also

### Constants

- [kCFStreamPropertyAppendToFile](appendtofile.md) — Value is a `CFBoolean` value that indicates whether to append the written data to a file, if it already exists, rather than to replace its contents.
- [kCFStreamPropertyDataWritten](datawritten.md) — Value is a `CFData` object that contains all the bytes written to a writable memory stream. You cannot modify this value.
- [kCFStreamPropertyFileCurrentOffset](filecurrentoffset.md) — Value is a `CFNumber` object containing the current file offset.
- [kCFStreamPropertySocketNativeHandle](socketnativehandle.md) — Value is a `CFData` object that contains the native handle for a socket stream—of type [CFSocketNativeHandle](../cfsocketnativehandle.md)—to which the socket stream is connected.
- [kCFStreamPropertySocketRemoteHostName](socketremotehostname.md) — Value is a `CFString` object containing the name of the host to which the socket stream is connected or `NULL` if unknown.
- [kCFStreamPropertyShouldCloseNativeSocket](../kcfstreampropertyshouldclosenativesocket.md) — Should Close Native Socket property key.
- [kCFStreamPropertySocketSecurityLevel](../kcfstreampropertysocketsecuritylevel.md) — Socket Security Level property key.
- [kCFStreamPropertySSLPeerCertificates](../../cfnetwork/kcfstreampropertysslpeercertificates.md) — SSL Peer Certificates property key for copy operations, which return a `CFArray` object containing `SecCertificateRef` objects. _(deprecated)_
- [kCFStreamPropertySSLPeerTrust](../../cfnetwork/kcfstreampropertysslpeertrust.md) — SSL Peer Trust property key for copy operations, which return a `SecTrustRef` object containing the result of the SSL handshake.
- [kCFStreamPropertySSLSettings](../../cfnetwork/kcfstreampropertysslsettings.md) — SSL Settings property key for set operations.
- [kCFStreamPropertySSLContext](../../cfnetwork/kcfstreampropertysslcontext.md)
- [kCFStreamPropertySOCKSProxy](../kcfstreampropertysocksproxy.md) — SOCKS proxy property key.
- [kCFStreamPropertyProxyLocalBypass](../../cfnetwork/kcfstreampropertyproxylocalbypass.md) — Proxy Local Bypass property key.
- [kCFStreamPropertySocketRemoteHost](../../cfnetwork/kcfstreampropertysocketremotehost.md) — The key’s value is a `CFHostRef` for the remote host if it is known. If not, its value is `NULL`.
- [kCFStreamPropertySocketRemoteNetService](../../cfnetwork/kcfstreampropertysocketremotenetservice.md) — The key’s value is a `CFNetServiceRef` for the remote network service if it is known. If not, its value is `NULL`.
