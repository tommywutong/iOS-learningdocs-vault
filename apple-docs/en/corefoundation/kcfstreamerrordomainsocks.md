---
title: kCFStreamErrorDomainSOCKS
framework: Core Foundation
symbol_kind: var
role: symbol
role_heading: Global Variable
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.1+, macOS 10.0+, tvOS, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/corefoundation/kcfstreamerrordomainsocks
source_url: 'https://developer.apple.com/documentation/corefoundation/kcfstreamerrordomainsocks'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/corefoundation/kcfstreamerrordomainsocks.json'
content_hash: 'sha256:ac80412e9cc1d44b'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Foundation](../corefoundation.md)

# kCFStreamErrorDomainSOCKS

<sub>Global Variable</sub>

The error code is a SOCKS proxy error.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
let kCFStreamErrorDomainSOCKS: Int32
```

## See Also

### Constants

- [kCFStreamErrorDomainNetDB](../cfnetwork/kcfstreamerrordomainnetdb.md) — The error code is an error code defined in `netdb.h`.
- [kCFStreamErrorDomainNetServices](../cfnetwork/kcfstreamerrordomainnetservices.md) — The error code is a `CFNetService` error code. For details, see the [`CFNetServicesError`](doc://com.apple.cfnetwork/documentation/CFNetwork/CFNetServicesError) enumeration.
- [kCFStreamErrorDomainMach](../cfnetwork/kcfstreamerrordomainmach.md) — The error code is a Mach error code defined in `mach/error.h`.
- [kCFStreamErrorDomainFTP](../cfnetwork/kcfstreamerrordomainftp.md) — The error code is an FTP error code.
- [kCFStreamErrorDomainHTTP](../cfnetwork/kcfstreamerrordomainhttp.md) — The error code is an HTTP error code.
- [kCFStreamErrorDomainSystemConfiguration](../cfnetwork/kcfstreamerrordomainsystemconfiguration.md) — The error code is a system configuration error code as defined in `System/ConfigurationSystemConfiguration.h`.
- [kCFStreamErrorDomainWinSock](../cfnetwork/kcfstreamerrordomainwinsock.md) — When running CFNetwork code on Windows, this domain returns error codes associated with the underlying TCP/IP stack. You should also note that non-networking errors such as `ENOMEM` are delivered through the POSIX domain. See the header `winsock2.h` for relevant error codes.
- [kCFStreamErrorDomainSSL](kcfstreamerrordomainssl.md) — The error code is an SSL error code as defined in `Security/SecureTransport.h`.
