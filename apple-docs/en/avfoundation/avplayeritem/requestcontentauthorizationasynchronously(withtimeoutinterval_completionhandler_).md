---
title: 'requestContentAuthorizationAsynchronously(withTimeoutInterval:completionHandler:)'
framework: AVFoundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [macOS 10.7+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/avfoundation/avplayeritem/requestcontentauthorizationasynchronously(withtimeoutinterval:completionhandler:)'
source_url: 'https://developer.apple.com/documentation/avfoundation/avplayeritem/requestcontentauthorizationasynchronously(withtimeoutinterval:completionhandler:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avplayeritem/requestcontentauthorizationasynchronously%28withtimeoutinterval%3Acompletionhandler%3A%29.json'
content_hash: 'sha256:ddaa10f2abcf0e23'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVPlayerItem](../avplayeritem.md)

# requestContentAuthorizationAsynchronously(withTimeoutInterval:completionHandler:)

<sub>Instance Method</sub>

Presents the user the opportunity to authorize the content for playback.

<sub>macOS</sub>

```swift
func requestContentAuthorizationAsynchronously(withTimeoutInterval timeoutInterval: TimeInterval, completionHandler handler: @escaping @Sendable () -> Void)
```

<sub>macOS</sub>

```swift
func requestContentAuthorization(withTimeoutInterval timeoutInterval: TimeInterval) async
```

## Parameters

- `timeoutInterval` — The maximum amount of time in seconds to wait for the user to authorize the content before calling the handler block with a timeout result.

- `handler` — The block to be called upon completion.

## Discussion

Calling this method will present the user with the opportunity to authorize the content (for example, by launching iTunes and prompting the user to enter their Apple ID and password).

When the user has taken action (or the timeout has elapsed), the completion handler is invoked. You determine the status of the authorization attempt by checking the value of the [contentAuthorizationRequestStatus](contentauthorizationrequeststatus.md) property.

Even if the status indicates a completed authorization, the content may still not be authorized (for example, if the user authorizes an Apple ID other than that associated with the content).  You should re-check the value of [contentAuthorizationRequestStatus](contentauthorizationrequeststatus.md) to verify whether the content has actually been authorized before continuing.  It is not necessary to call this method if the value of [contentAuthorizationRequestStatus](contentauthorizationrequeststatus.md) is already true.

## See Also

### Managing playback authorization in macOS

- [contentAuthorizedForPlayback](iscontentauthorizedforplayback.md) — A Boolean value that indicates whether the content has been authorized by the user.
- [authorizationRequiredForPlayback](isauthorizationrequiredforplayback.md) — A Boolean value that indicates whether authorization is required to play the content.
- [applicationAuthorizedForPlayback](isapplicationauthorizedforplayback.md) — A Boolean value that indicates whether the application can be used to play the content.
- [contentAuthorizationRequestStatus](contentauthorizationrequeststatus.md) — The status of the most recent content authorization request.
- [AVContentAuthorizationStatus](../avcontentauthorizationstatus.md) — A value representing the status of a content authorization request.
- [- cancelContentAuthorizationRequest](<cancelcontentauthorizationrequest().md>) — Cancels the currently outstanding content authorization request.
