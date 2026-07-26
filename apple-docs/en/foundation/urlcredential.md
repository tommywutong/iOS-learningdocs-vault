---
title: URLCredential
framework: Foundation
symbol_kind: class
role: symbol
role_heading: Class
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.1+, macOS 10.2+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/urlcredential
source_url: 'https://developer.apple.com/documentation/foundation/urlcredential'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/urlcredential.json'
content_hash: 'sha256:99f0977a740f7a13'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Foundation](../foundation.md)

# URLCredential

<sub>Class</sub>

`A`n authentication credential consisting of information specific to the type of credential and the type of persistent storage to use, if any.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
class URLCredential
```

## Overview

The URL Loading System supports password-based user credentials, certificate-based user credentials, and certificate-based server credentials.

When you create a credential, you can specify it for a single request, persist it temporarily (until your app quits), or persist it permanently. Permanent persistence can be local persistence in the keychain, or synchronized persistence across the user’s devices, based on their Apple ID.

> [!note] Note
> Permanent storage of credentials is only available for password-based credentials. TLS credentials are never stored permanently by [URLCredentialStorage](urlcredentialstorage.md). In general, use for-session persistence for TLS credentials.

## Relationships

- **Inherits From**: [NSObject](../objectivec/nsobject-swift.class.md)

- **Conforms To**: [CVarArg](../swift/cvararg.md), [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md), [CustomStringConvertible](../swift/customstringconvertible.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [NSCoding](nscoding.md), [NSCopying](nscopying.md), [NSObjectProtocol](../objectivec/nsobjectprotocol.md), [NSSecureCoding](nssecurecoding.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md)

## Topics

### Creating a credential

- [init(forTrust:)](<urlcredential/init(fortrust_).md>) — Creates a URL credential instance for server trust authentication with a given accepted trust.
- [- initWithIdentity:certificates:persistence:](<urlcredential/init(identity_certificates_persistence_).md>) — Creates a URL credential instance for resolving a client certificate authentication challenge.
- [- initWithTrust:](<urlcredential/init(trust_).md>) — Creates a URL credential instance for server trust authentication, initialized with a accepted trust.
- [- initWithUser:password:persistence:](<urlcredential/init(user_password_persistence_).md>) — Creates a URL credential instance initialized with a given user name and password, using a given persistence setting.
- [Persistence](urlcredential/persistence-swift.enum.md) — Constants that specify how long the credential will be kept.

### Getting credential properties

- [user](urlcredential/user.md) — The credential’s user name.
- [certificates](urlcredential/certificates.md) — The intermediate certificates of the credential, if it is a client certificate credential.
- [hasPassword](urlcredential/haspassword.md) — A Boolean value that indicates whether the credential has a password.
- [password](urlcredential/password.md) — The credential’s password.
- [identity](urlcredential/identity.md) — The identity of this credential if it is a client certificate credential.
- [persistence](urlcredential/persistence-swift.property.md) — The credential’s persistence setting.
- [Persistence](urlcredential/persistence-swift.enum.md) — Constants that specify how long the credential will be kept.

### Initializers

- [init(coder:)](<urlcredential/init(coder_).md>)

### Default Implementations

- [NSURLCredential Implementations](urlcredential/nsurlcredential-implementations.md)

## See Also

### Authentication and credentials

- [Handling an authentication challenge](handling-an-authentication-challenge.md) — Respond appropriately when a server demands authentication for a URL request.
- [URLAuthenticationChallenge](urlauthenticationchallenge.md) — A challenge from a server requiring authentication from the client.
- [URLCredentialStorage](urlcredentialstorage.md) — The manager of a shared credentials cache.
- [URLProtectionSpace](urlprotectionspace.md) — A server or an area on a server, commonly referred to as a realm, that requires authentication.
