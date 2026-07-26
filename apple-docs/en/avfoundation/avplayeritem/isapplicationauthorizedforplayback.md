---
title: isApplicationAuthorizedForPlayback
framework: AVFoundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [Mac Catalyst 13.0+, macOS 10.7+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avplayeritem/isapplicationauthorizedforplayback
source_url: 'https://developer.apple.com/documentation/avfoundation/avplayeritem/isapplicationauthorizedforplayback'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avplayeritem/isapplicationauthorizedforplayback.json'
content_hash: 'sha256:7573df49f5ac79f4'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVPlayerItem](../avplayeritem.md)

# isApplicationAuthorizedForPlayback

<sub>Instance Property</sub>

A Boolean value that indicates whether the application can be used to play the content.

<sub>Mac Catalyst, macOS</sub>

```swift
var isApplicationAuthorizedForPlayback: Bool { get }
```

## Discussion

This property reports whether or not the calling application is authorized to play the content associated with the item.

Application authorization is independent of content authorization (see [contentAuthorizedForPlayback](iscontentauthorizedforplayback.md)) and that both must be granted in order for an application to be allowed to play protected content. Also, unlike content authorization, application authorization is not dependent on user credentials (that is, if `applicationAuthorizedForPlayback` is [false](../../swift/false.md), there are no means to obtain authorization).

This property is not key-value observable.

## See Also

### Managing playback authorization in macOS

- [contentAuthorizedForPlayback](iscontentauthorizedforplayback.md) — A Boolean value that indicates whether the content has been authorized by the user.
- [authorizationRequiredForPlayback](isauthorizationrequiredforplayback.md) — A Boolean value that indicates whether authorization is required to play the content.
- [- requestContentAuthorizationAsynchronouslyWithTimeoutInterval:completionHandler:](<requestcontentauthorizationasynchronously(withtimeoutinterval_completionhandler_).md>) — Presents the user the opportunity to authorize the content for playback.
- [contentAuthorizationRequestStatus](contentauthorizationrequeststatus.md) — The status of the most recent content authorization request.
- [AVContentAuthorizationStatus](../avcontentauthorizationstatus.md) — A value representing the status of a content authorization request.
- [- cancelContentAuthorizationRequest](<cancelcontentauthorizationrequest().md>) — Cancels the currently outstanding content authorization request.
