---
title: 'init(protectionSpace:proposedCredential:previousFailureCount:failureResponse:error:sender:)'
framework: Foundation
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.1+, macOS 10.2+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/urlauthenticationchallenge/init(protectionspace:proposedcredential:previousfailurecount:failureresponse:error:sender:)'
source_url: 'https://developer.apple.com/documentation/foundation/urlauthenticationchallenge/init(protectionspace:proposedcredential:previousfailurecount:failureresponse:error:sender:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/urlauthenticationchallenge/init%28protectionspace%3Aproposedcredential%3Apreviousfailurecount%3Afailureresponse%3Aerror%3Asender%3A%29.json'
content_hash: 'sha256:f36fbf42ea752470'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [URLAuthenticationChallenge](../urlauthenticationchallenge.md)

# init(protectionSpace:proposedCredential:previousFailureCount:failureResponse:error:sender:)

<sub>Initializer</sub>

Initializes an authentication challenge from parameters you provide.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
init(protectionSpace space: URLProtectionSpace, proposedCredential credential: URLCredential?, previousFailureCount: Int, failureResponse response: URLResponse?, error: (any Error)?, sender: any URLAuthenticationChallengeSender)
```

## Parameters

- `space` — The protection space for the authentication challenge. This provides additional information about the authentication request, such as the host, port, authentication realm, and so on.

- `credential` — The proposed credential, or `nil`.

- `previousFailureCount` — The total number of previous failures for this request, including failures for other protection spaces.

- `response` — An instance of [URLResponse](../urlresponse.md) containing the server response that caused you to generate an authentication challenge, or `nil` if no response object is applicable to the challenge.

- `error` — An `NS``Error` instance describing the authentication failure, or `nil` if it is not applicable to the challenge.

- `sender` — The object that initiated the authentication challenge (typically, the object that called this method).

## Return Value

A new authentication challenge object, with the given properties.

## Discussion

Most apps don’t create [URLAuthenticationChallenge](../urlauthenticationchallenge.md) instances themselves. Instead, they handle received challenges in the [- URLSession:task:didReceiveChallenge:completionHandler:](<../urlsessiontaskdelegate/urlsession(__task_didreceive_completionhandler_).md>) method of [URLSessionTaskDelegate](../urlsessiontaskdelegate.md).

However, you might need to create authentication challenge objects when adding support for custom networking protocols, as part of your custom [URLProtocol](../urlprotocol.md) subclasses.

## See Also

### Creating an authentication challenge instance

- [- initWithAuthenticationChallenge:sender:](<init(authenticationchallenge_sender_).md>) — Creates an authentication challenge from an existing challenge instance.
