---
title: cancelContentAuthorizationRequest()
framework: AVFoundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [macOS 10.7+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avplayeritem/cancelcontentauthorizationrequest()
source_url: 'https://developer.apple.com/documentation/avfoundation/avplayeritem/cancelcontentauthorizationrequest()'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avplayeritem/cancelcontentauthorizationrequest%28%29.json'
content_hash: 'sha256:37a72217a1117265'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVPlayerItem](../avplayeritem.md)

# cancelContentAuthorizationRequest()

<sub>Instance Method</sub>

Cancels the currently outstanding content authorization request.

<sub>macOS</sub>

```swift
func cancelContentAuthorizationRequest()
```

## Discussion

Calling this method while a content authorization request is pending will cause that request to be cancelled and its completion handler to be invoked with a status of [AVContentAuthorizationCancelled](../avcontentauthorizationstatus/cancelled.md).

This method does not block.

## See Also

### Managing playback authorization in macOS

- [contentAuthorizedForPlayback](iscontentauthorizedforplayback.md) — A Boolean value that indicates whether the content has been authorized by the user.
- [authorizationRequiredForPlayback](isauthorizationrequiredforplayback.md) — A Boolean value that indicates whether authorization is required to play the content.
- [applicationAuthorizedForPlayback](isapplicationauthorizedforplayback.md) — A Boolean value that indicates whether the application can be used to play the content.
- [- requestContentAuthorizationAsynchronouslyWithTimeoutInterval:completionHandler:](<requestcontentauthorizationasynchronously(withtimeoutinterval_completionhandler_).md>) — Presents the user the opportunity to authorize the content for playback.
- [contentAuthorizationRequestStatus](contentauthorizationrequeststatus.md) — The status of the most recent content authorization request.
- [AVContentAuthorizationStatus](../avcontentauthorizationstatus.md) — A value representing the status of a content authorization request.
