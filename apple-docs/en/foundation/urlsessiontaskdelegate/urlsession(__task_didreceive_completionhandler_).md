---
title: 'urlSession(_:task:didReceive:completionHandler:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 7.0+, iPadOS 7.0+, Mac Catalyst 13.1+, macOS 10.9+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, swift, swift, occ, occ, occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/urlsessiontaskdelegate/urlsession(_:task:didreceive:completionhandler:)'
source_url: 'https://developer.apple.com/documentation/foundation/urlsessiontaskdelegate/urlsession(_:task:didreceive:completionhandler:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/urlsessiontaskdelegate/urlsession%28_%3Atask%3Adidreceive%3Acompletionhandler%3A%29.json'
content_hash: 'sha256:42afba691df70b65'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [URLSessionTaskDelegate](../urlsessiontaskdelegate.md)

# urlSession(_:task:didReceive:completionHandler:)

<sub>Instance Method</sub>

Requests credentials from the delegate in response to an authentication request from the remote server.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
optional func urlSession(_ session: URLSession, task: URLSessionTask, didReceive challenge: URLAuthenticationChallenge, completionHandler: @escaping @Sendable (URLSession.AuthChallengeDisposition, URLCredential?) -> Void)
```

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
optional func urlSession(_ session: URLSession, task: URLSessionTask, didReceive challenge: URLAuthenticationChallenge) async -> (URLSession.AuthChallengeDisposition, URLCredential?)
```

## Parameters

- `session` — The session containing the task whose request requires authentication.

- `task` — The task whose request requires authentication.

- `challenge` — An object that contains the request for authentication.

- `completionHandler` — A handler that your delegate method must call. Its parameters are: - `disposition`—One of several constants that describes how the challenge should be handled. - `credential`—The credential that should be used for authentication if disposition is `NSURLSessionAuthChallengeUseCredential`; otherwise, `NULL`.

## Discussion

This method handles task-level authentication challenges. The [URLSessionDelegate](../urlsessiondelegate.md) protocol also provides a session-level authentication delegate method. The method called depends on the type of authentication challenge:

- For session-level challenges—[NSURLAuthenticationMethodNTLM](../nsurlauthenticationmethodntlm.md), [NSURLAuthenticationMethodNegotiate](../nsurlauthenticationmethodnegotiate.md), [NSURLAuthenticationMethodClientCertificate](../nsurlauthenticationmethodclientcertificate.md), or [NSURLAuthenticationMethodServerTrust](../nsurlauthenticationmethodservertrust.md)—the `NSURLSession` object calls the session delegate’s [- URLSession:didReceiveChallenge:completionHandler:](<../urlsessiondelegate/urlsession(__didreceive_completionhandler_).md>) method. If your app does not provide a session delegate method, the `NSURLSession` object  calls the task delegate’s [- URLSession:task:didReceiveChallenge:completionHandler:](<urlsession(__task_didreceive_completionhandler_).md>) method to handle the challenge.
- For non-session-level challenges (all others), the [URLSession](../urlsession.md) object calls the session delegate’s [- URLSession:task:didReceiveChallenge:completionHandler:](<urlsession(__task_didreceive_completionhandler_).md>) method to handle the challenge. If your app provides a session delegate and you need to handle authentication, then you must either handle the authentication at the task level or provide a task-level handler that calls the per-session handler explicitly. The session delegate’s [- URLSession:didReceiveChallenge:completionHandler:](<../urlsessiondelegate/urlsession(__didreceive_completionhandler_).md>) method is _not_ called for non-session-level challenges.

## See Also

### Handling authentication challenges

- [AuthChallengeDisposition](../urlsession/authchallengedisposition.md) — Constants passed by session or task delegates to the provided continuation block in response to an authentication challenge.
