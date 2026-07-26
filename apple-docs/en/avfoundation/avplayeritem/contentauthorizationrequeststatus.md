---
title: contentAuthorizationRequestStatus
framework: AVFoundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [macOS 10.7+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avplayeritem/contentauthorizationrequeststatus
source_url: 'https://developer.apple.com/documentation/avfoundation/avplayeritem/contentauthorizationrequeststatus'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avplayeritem/contentauthorizationrequeststatus.json'
content_hash: 'sha256:86eb1ee4e71caee2'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVPlayerItem](../avplayeritem.md)

# contentAuthorizationRequestStatus

<sub>Instance Property</sub>

The status of the most recent content authorization request.

<sub>macOS</sub>

```swift
var contentAuthorizationRequestStatus: AVContentAuthorizationStatus { get }
```

## Discussion

This property reports the authorization status as determined by the most recent call to [- requestContentAuthorizationAsynchronouslyWithTimeoutInterval:completionHandler:](<requestcontentauthorizationasynchronously(withtimeoutinterval_completionhandler_).md>).

The value will be [AVContentAuthorizationUnknown](../avcontentauthorizationstatus/unknown.md) before the first call and between the time a request call is made and just prior to the completion handler being executed (thus it is safe to query this property from the completion handler).

This value is not key-value observable.

## See Also

### Managing playback authorization in macOS

- [contentAuthorizedForPlayback](iscontentauthorizedforplayback.md) — A Boolean value that indicates whether the content has been authorized by the user.
- [authorizationRequiredForPlayback](isauthorizationrequiredforplayback.md) — A Boolean value that indicates whether authorization is required to play the content.
- [applicationAuthorizedForPlayback](isapplicationauthorizedforplayback.md) — A Boolean value that indicates whether the application can be used to play the content.
- [- requestContentAuthorizationAsynchronouslyWithTimeoutInterval:completionHandler:](<requestcontentauthorizationasynchronously(withtimeoutinterval_completionhandler_).md>) — Presents the user the opportunity to authorize the content for playback.
- [AVContentAuthorizationStatus](../avcontentauthorizationstatus.md) — A value representing the status of a content authorization request.
- [- cancelContentAuthorizationRequest](<cancelcontentauthorizationrequest().md>) — Cancels the currently outstanding content authorization request.
