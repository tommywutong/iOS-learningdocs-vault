---
title: URLAuthenticationChallenge
framework: Foundation
symbol_kind: class
role: symbol
role_heading: Class
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.1+, macOS 10.2+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/urlauthenticationchallenge
source_url: 'https://developer.apple.com/documentation/foundation/urlauthenticationchallenge'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/urlauthenticationchallenge.json'
content_hash: 'sha256:715d16a1f72a6dbc'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Foundation](../foundation.md)

# URLAuthenticationChallenge

<sub>Class</sub>

A challenge from a server requiring authentication from the client.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
class URLAuthenticationChallenge
```

## Overview

Your app receives authentication challenges in various [URLSession](urlsession.md), [NSURLConnection](nsurlconnection.md), and [NSURLDownload](nsurldownload.md) delegate methods, such as [- URLSession:task:didReceiveChallenge:completionHandler:](<urlsessiontaskdelegate/urlsession(__task_didreceive_completionhandler_).md>). These objects provide the information you’ll need when deciding how to handle a server’s request for authentication.

At the core of that authentication challenge is a _protection space_ that defines the type of authentication being requested, the host and port number, the networking protocol, and (where applicable) the authentication realm (a group of related URLs on the same server that share a single set of credentials).

## Relationships

- **Inherits From**: [NSObject](../objectivec/nsobject-swift.class.md)

- **Conforms To**: [CVarArg](../swift/cvararg.md), [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md), [CustomStringConvertible](../swift/customstringconvertible.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [NSCoding](nscoding.md), [NSObjectProtocol](../objectivec/nsobjectprotocol.md), [NSSecureCoding](nssecurecoding.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md)

## Topics

### Creating an authentication challenge instance

- [- initWithAuthenticationChallenge:sender:](<urlauthenticationchallenge/init(authenticationchallenge_sender_).md>) — Creates an authentication challenge from an existing challenge instance.
- [- initWithProtectionSpace:proposedCredential:previousFailureCount:failureResponse:error:sender:](<urlauthenticationchallenge/init(protectionspace_proposedcredential_previousfailurecount_failureresponse_error_sender_).md>) — Initializes an authentication challenge from parameters you provide.

### Inspecting the authentication challenge

- [protectionSpace](urlauthenticationchallenge/protectionspace.md) — The receiver’s protection space.

### Getting properties of previous authentication attempts

- [failureResponse](urlauthenticationchallenge/failureresponse.md) — The URL response object representing the last authentication failure.
- [previousFailureCount](urlauthenticationchallenge/previousfailurecount.md) — The receiver’s count of failed authentication attempts.
- [proposedCredential](urlauthenticationchallenge/proposedcredential.md) — The proposed credential for this challenge.

### Getting authentication errors

- [error](urlauthenticationchallenge/error.md) — The error object representing the last authentication failure.

### Legacy

- [sender](urlauthenticationchallenge/sender.md) — The sender of the challenge.

### Initializers

- [init(coder:)](<urlauthenticationchallenge/init(coder_).md>)

## See Also

### Authentication and credentials

- [Handling an authentication challenge](handling-an-authentication-challenge.md) — Respond appropriately when a server demands authentication for a URL request.
- [URLCredential](urlcredential.md) — `A`n authentication credential consisting of information specific to the type of credential and the type of persistent storage to use, if any.
- [URLCredentialStorage](urlcredentialstorage.md) — The manager of a shared credentials cache.
- [URLProtectionSpace](urlprotectionspace.md) — A server or an area on a server, commonly referred to as a realm, that requires authentication.
