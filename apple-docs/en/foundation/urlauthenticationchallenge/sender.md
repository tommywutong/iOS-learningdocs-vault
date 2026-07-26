---
title: sender
framework: Foundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.1+, macOS 10.2+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/urlauthenticationchallenge/sender
source_url: 'https://developer.apple.com/documentation/foundation/urlauthenticationchallenge/sender'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/urlauthenticationchallenge/sender.json'
content_hash: 'sha256:eb44ecd97821de0b'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [URLAuthenticationChallenge](../urlauthenticationchallenge.md)

# sender

<sub>Instance Property</sub>

The sender of the challenge.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var sender: (any URLAuthenticationChallengeSender)? { get }
```

## Discussion

If you are using the [URLSession](../urlsession.md) API, this value is purely informational, because you _must_ respond to authentication challenges in your [URLSessionDelegate](../urlsessiondelegate.md) or [URLSessionTaskDelegate](../urlsessiontaskdelegate.md) implementations, by passing [AuthChallengeDisposition](../urlsession/authchallengedisposition.md) constants to the provided completion handler blocks.

However, if you are using the legacy `NSURLConnection` or `NSURLDownload` API, you use this object directly in your authentication handler delegate method. With these APIs, after you finish processing the authentication challenge, you respond by calling methods defined in the [URLAuthenticationChallengeSender](../urlauthenticationchallengesender.md) protocol on this sender.

> [!warning] Warning
> Do not call methods directly on this object if you are using the [URLSession](../urlsession.md) API.
