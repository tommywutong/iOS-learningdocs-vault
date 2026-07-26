---
title: isContentAuthorizedForPlayback
framework: AVFoundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [Mac Catalyst 13.0+, macOS 10.7+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avplayeritem/iscontentauthorizedforplayback
source_url: 'https://developer.apple.com/documentation/avfoundation/avplayeritem/iscontentauthorizedforplayback'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avplayeritem/iscontentauthorizedforplayback.json'
content_hash: 'sha256:a26142e8a1915810'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVPlayerItem](../avplayeritem.md)

# isContentAuthorizedForPlayback

<sub>Instance Property</sub>

A Boolean value that indicates whether the content has been authorized by the user.

<sub>Mac Catalyst, macOS</sub>

```swift
var isContentAuthorizedForPlayback: Bool { get }
```

## Discussion

This property reports whether the user has provided the necessary credentials to the system in order for the content to be decrypted for playback.

Content authorization is independent of application authorization (see [applicationAuthorizedForPlayback](isapplicationauthorizedforplayback.md)) and that both must be granted in order for an application to be allowed to play protected content.

This property is not key-value observable.

## See Also

### Managing playback authorization in macOS

- [authorizationRequiredForPlayback](isauthorizationrequiredforplayback.md) — A Boolean value that indicates whether authorization is required to play the content.
- [applicationAuthorizedForPlayback](isapplicationauthorizedforplayback.md) — A Boolean value that indicates whether the application can be used to play the content.
- [- requestContentAuthorizationAsynchronouslyWithTimeoutInterval:completionHandler:](<requestcontentauthorizationasynchronously(withtimeoutinterval_completionhandler_).md>) — Presents the user the opportunity to authorize the content for playback.
- [contentAuthorizationRequestStatus](contentauthorizationrequeststatus.md) — The status of the most recent content authorization request.
- [AVContentAuthorizationStatus](../avcontentauthorizationstatus.md) — A value representing the status of a content authorization request.
- [- cancelContentAuthorizationRequest](<cancelcontentauthorizationrequest().md>) — Cancels the currently outstanding content authorization request.
