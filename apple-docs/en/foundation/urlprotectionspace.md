---
title: URLProtectionSpace
framework: Foundation
symbol_kind: class
role: symbol
role_heading: Class
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.1+, macOS 10.2+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/urlprotectionspace
source_url: 'https://developer.apple.com/documentation/foundation/urlprotectionspace'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/urlprotectionspace.json'
content_hash: 'sha256:f5c518bd204b24dd'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Foundation](../foundation.md)

# URLProtectionSpace

<sub>Class</sub>

A server or an area on a server, commonly referred to as a realm, that requires authentication.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
class URLProtectionSpace
```

## Overview

A protection space defines a series of matching constraints that determine which credential should be provided. For example, if a request provides your delegate with a [URLAuthenticationChallenge](urlauthenticationchallenge.md) object that requests a client username and password, your app should provide the correct username and password for the particular host, port, protocol, and realm, as specified in the challenge’s protection space.

> [!note] Note
> This class has no designated initializer; its `init` method always returns `nil`. You must initialize this class by calling one of the initialization methods described in Creating a protection space.

## Relationships

- **Inherits From**: [NSObject](../objectivec/nsobject-swift.class.md)

- **Conforms To**: [CVarArg](../swift/cvararg.md), [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md), [CustomStringConvertible](../swift/customstringconvertible.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [NSCoding](nscoding.md), [NSCopying](nscopying.md), [NSObjectProtocol](../objectivec/nsobjectprotocol.md), [NSSecureCoding](nssecurecoding.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md)

## Topics

### Creating a protection space

- [- initWithHost:port:protocol:realm:authenticationMethod:](<urlprotectionspace/init(host_port_protocol_realm_authenticationmethod_).md>) — Creates a protection space object from the given host, port, protocol, realm, and authentication method.
- [- initWithProxyHost:port:type:realm:authenticationMethod:](<urlprotectionspace/init(proxyhost_port_type_realm_authenticationmethod_).md>) — Creates a protection space object representing a proxy server.

### Getting protection space properties

- [authenticationMethod](urlprotectionspace/authenticationmethod.md) — The authentication method used by the receiver.
- [distinguishedNames](urlprotectionspace/distinguishednames.md) — The acceptable certificate-issuing authorities for client certificate authentication.
- [host](urlprotectionspace/host.md) — The receiver’s host.
- [port](urlprotectionspace/port.md) — The receiver’s port.
- [protocol](urlprotectionspace/protocol.md) — The receiver’s protocol.
- [proxyType](urlprotectionspace/proxytype.md) — The receiver’s proxy type.
- [realm](urlprotectionspace/realm.md) — The receiver’s authentication realm
- [receivesCredentialSecurely](urlprotectionspace/receivescredentialsecurely.md) — A Boolean value that indicates whether the credentials for the protection space can be sent securely.
- [serverTrust](urlprotectionspace/servertrust.md) — A representation of the server’s SSL transaction state.

### Identifying protection space properties

- [NSURLProtectionSpace protocol types](nsurlprotectionspace-protocol-types.md) — These constants describe the supported protocols for a protection space, as returned by [protocol](urlprotectionspace/protocol.md).
- [NSURLProtectionSpace proxy types](nsurlprotectionspace-proxy-types.md) — These constants describe the supported proxy types used in [- initWithProxyHost:port:type:realm:authenticationMethod:](<urlprotectionspace/init(proxyhost_port_type_realm_authenticationmethod_).md>) and returned by [proxyType](urlprotectionspace/proxytype.md).
- [NSURLProtectionSpace authentication method constants](nsurlprotectionspace-authentication-method-constants.md) — Constants describing known values of the [authenticationMethod](urlprotectionspace/authenticationmethod.md) property of a [URLProtectionSpace](urlprotectionspace.md).

### Initializers

- [init(coder:)](<urlprotectionspace/init(coder_).md>)

### Instance Methods

- [isProxy()](<urlprotectionspace/isproxy().md>)

## See Also

### Authentication and credentials

- [Handling an authentication challenge](handling-an-authentication-challenge.md) — Respond appropriately when a server demands authentication for a URL request.
- [URLAuthenticationChallenge](urlauthenticationchallenge.md) — A challenge from a server requiring authentication from the client.
- [URLCredential](urlcredential.md) — `A`n authentication credential consisting of information specific to the type of credential and the type of persistent storage to use, if any.
- [URLCredentialStorage](urlcredentialstorage.md) — The manager of a shared credentials cache.
