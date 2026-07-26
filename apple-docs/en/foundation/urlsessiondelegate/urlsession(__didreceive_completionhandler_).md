---
title: 'urlSession(_:didReceive:completionHandler:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 7.0+, iPadOS 7.0+, Mac Catalyst 13.1+, macOS 10.9+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/urlsessiondelegate/urlsession(_:didreceive:completionhandler:)'
source_url: 'https://developer.apple.com/documentation/foundation/urlsessiondelegate/urlsession(_:didreceive:completionhandler:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/urlsessiondelegate/urlsession%28_%3Adidreceive%3Acompletionhandler%3A%29.json'
content_hash: 'sha256:9fe40988b854a64f'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [URLSessionDelegate](../urlsessiondelegate.md)

# urlSession(_:didReceive:completionHandler:)

<sub>Instance Method</sub>

Requests credentials from the delegate in response to a session-level authentication request from the remote server.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
optional func urlSession(_ session: URLSession, didReceive challenge: URLAuthenticationChallenge, completionHandler: @escaping @Sendable (URLSession.AuthChallengeDisposition, URLCredential?) -> Void)
```

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
optional func urlSession(_ session: URLSession, didReceive challenge: URLAuthenticationChallenge) async -> (URLSession.AuthChallengeDisposition, URLCredential?)
```

## Parameters

- `session` — The session containing the task that requested authentication.

- `challenge` — An object that contains the request for authentication.

- `completionHandler` — A handler that your delegate method must call. This completion handler takes the following parameters:: - `disposition`—One of several constants that describes how the challenge should be handled. - `credential`—The credential that should be used for authentication if disposition is `NSURLSessionAuthChallengeUseCredential`, otherwise `NULL`.

## Discussion

This method is called in two situations:

- When a remote server asks for client certificates or Windows NT LAN Manager (NTLM) authentication, to allow your app to provide appropriate credentials
- When a session first establishes a connection to a remote server that uses SSL or TLS, to allow your app to verify the server’s certificate chain

If you do not implement this method, the session calls its delegate’s [- URLSession:task:didReceiveChallenge:completionHandler:](<../urlsessiontaskdelegate/urlsession(__task_didreceive_completionhandler_).md>) method instead.

> [!note] Note
> This method handles _only_ the [NSURLAuthenticationMethodNTLM](../nsurlauthenticationmethodntlm.md), [NSURLAuthenticationMethodNegotiate](../nsurlauthenticationmethodnegotiate.md), [NSURLAuthenticationMethodClientCertificate](../nsurlauthenticationmethodclientcertificate.md), and [NSURLAuthenticationMethodServerTrust](../nsurlauthenticationmethodservertrust.md) authentication types. For all other authentication schemes, the session calls _only_ the [- URLSession:task:didReceiveChallenge:completionHandler:](<../urlsessiontaskdelegate/urlsession(__task_didreceive_completionhandler_).md>) method.

## See Also

### Handling authentication challenges

- [AuthChallengeDisposition](../urlsession/authchallengedisposition.md) — Constants passed by session or task delegates to the provided continuation block in response to an authentication challenge.
