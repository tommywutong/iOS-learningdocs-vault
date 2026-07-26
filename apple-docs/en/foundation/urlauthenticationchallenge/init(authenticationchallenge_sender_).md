---
title: 'init(authenticationChallenge:sender:)'
framework: Foundation
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.1+, macOS 10.2+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/urlauthenticationchallenge/init(authenticationchallenge:sender:)'
source_url: 'https://developer.apple.com/documentation/foundation/urlauthenticationchallenge/init(authenticationchallenge:sender:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/urlauthenticationchallenge/init%28authenticationchallenge%3Asender%3A%29.json'
content_hash: 'sha256:40ad791047027ff5'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [URLAuthenticationChallenge](../urlauthenticationchallenge.md)

# init(authenticationChallenge:sender:)

<sub>Initializer</sub>

Creates an authentication challenge from an existing challenge instance.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
init(authenticationChallenge challenge: URLAuthenticationChallenge, sender: any URLAuthenticationChallengeSender)
```

## Parameters

- `challenge` — The challenge that you want to copy. Usually, this is a challenge received by an existing [URLProtocol](../urlprotocol.md) subclass that you are subclassing.

- `sender` — The sender that you want to use for the new object. Typically, the sender is the instance of your custom [URLProtocol](../urlprotocol.md) subclass that called this method.

## Return Value

A new authentication challenge object, based on an existing challenge.

## Discussion

Most apps don’t create [URLAuthenticationChallenge](../urlauthenticationchallenge.md) instances themselves. Instead, they handle received challenges in the [- URLSession:task:didReceiveChallenge:completionHandler:](<../urlsessiontaskdelegate/urlsession(__task_didreceive_completionhandler_).md>) method of [URLSessionTaskDelegate](../urlsessiontaskdelegate.md).

However, you might need to create authentication challenge objects when adding support for custom networking protocols, as part of a custom [URLProtocol](../urlprotocol.md) subclass. When you subclass an existing [URLProtocol](../urlprotocol.md) subclass, this initializer lets you modify challenges issued by the existing class so that your subclass receives any responses to those challenges.

## See Also

### Creating an authentication challenge instance

- [- initWithProtectionSpace:proposedCredential:previousFailureCount:failureResponse:error:sender:](<init(protectionspace_proposedcredential_previousfailurecount_failureresponse_error_sender_).md>) — Initializes an authentication challenge from parameters you provide.
