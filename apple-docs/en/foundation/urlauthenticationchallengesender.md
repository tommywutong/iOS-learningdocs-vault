---
title: URLAuthenticationChallengeSender
framework: Foundation
symbol_kind: protocol
role: symbol
role_heading: Protocol
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.1+, macOS 10.2+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/urlauthenticationchallengesender
source_url: 'https://developer.apple.com/documentation/foundation/urlauthenticationchallengesender'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/urlauthenticationchallengesender.json'
content_hash: 'sha256:237efc9ec693e8a1'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Foundation](../foundation.md)

# URLAuthenticationChallengeSender

<sub>Protocol</sub>

The `URLAuthenticationChallengeSender` protocol represents the interface that the sender of an authentication challenge must implement.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
protocol URLAuthenticationChallengeSender : NSObjectProtocol, Sendable
```

## Overview

The methods in the protocol are generally sent by a delegate in response to receiving a [- connection:didReceiveAuthenticationChallenge:](<nsurlconnectiondelegate/connection(__didreceive_).md>): or [- download:didReceiveAuthenticationChallenge:](<nsurldownloaddelegate/download(__didreceive_)-1pc0v.md>):. The different methods provide different ways of responding to authentication challenges.

> [!important] Important
> This protocol is _only_ for use with the legacy [NSURLConnection](nsurlconnection.md) and [NSURLDownload](nsurldownload.md) classes. It should not be used with [URLSession](urlsession.md)-based code, for which you respond to authentication challenges by passing [AuthChallengeDisposition](urlsession/authchallengedisposition.md) constants to the provided completion handler blocks.

## Relationships

- **Inherits From**: [NSObjectProtocol](../objectivec/nsobjectprotocol.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md)

## Topics

### Protocol Methods

- [- cancelAuthenticationChallenge:](<urlauthenticationchallengesender/cancel(__).md>) — Cancels a given authentication challenge.
- [- continueWithoutCredentialForAuthenticationChallenge:](<urlauthenticationchallengesender/continuewithoutcredential(for_).md>) — Attempt to continue downloading a request without providing a credential for a given challenge.
- [- useCredential:forAuthenticationChallenge:](<urlauthenticationchallengesender/use(__for_).md>) — Attempt to use a given credential for a given authentication challenge.
- [- performDefaultHandlingForAuthenticationChallenge:](<urlauthenticationchallengesender/performdefaulthandling(for_).md>) — Causes the system-provided default behavior to be used.
- [- rejectProtectionSpaceAndContinueWithChallenge:](<urlauthenticationchallengesender/rejectprotectionspaceandcontinue(with_).md>) — Rejects the currently supplied protection space.
