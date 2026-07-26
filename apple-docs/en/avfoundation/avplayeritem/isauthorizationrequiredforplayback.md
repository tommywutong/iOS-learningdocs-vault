---
title: isAuthorizationRequiredForPlayback
framework: AVFoundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [Mac Catalyst 13.0+, macOS 10.7+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avplayeritem/isauthorizationrequiredforplayback
source_url: 'https://developer.apple.com/documentation/avfoundation/avplayeritem/isauthorizationrequiredforplayback'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avplayeritem/isauthorizationrequiredforplayback.json'
content_hash: 'sha256:c3b0ad097852afae'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVPlayerItem](../avplayeritem.md)

# isAuthorizationRequiredForPlayback

<sub>Instance Property</sub>

A Boolean value that indicates whether authorization is required to play the content.

<sub>Mac Catalyst, macOS</sub>

```swift
var isAuthorizationRequiredForPlayback: Bool { get }
```

## Discussion

This property reports whether authorization is required for the item’s content to be played. If it does not require authorization, then none of the other authorization-related  methods or properties apply (though they will return sensible values where possible).

This property is not key-value observable.

## See Also

### Managing playback authorization in macOS

- [contentAuthorizedForPlayback](iscontentauthorizedforplayback.md) — A Boolean value that indicates whether the content has been authorized by the user.
- [applicationAuthorizedForPlayback](isapplicationauthorizedforplayback.md) — A Boolean value that indicates whether the application can be used to play the content.
- [- requestContentAuthorizationAsynchronouslyWithTimeoutInterval:completionHandler:](<requestcontentauthorizationasynchronously(withtimeoutinterval_completionhandler_).md>) — Presents the user the opportunity to authorize the content for playback.
- [contentAuthorizationRequestStatus](contentauthorizationrequeststatus.md) — The status of the most recent content authorization request.
- [AVContentAuthorizationStatus](../avcontentauthorizationstatus.md) — A value representing the status of a content authorization request.
- [- cancelContentAuthorizationRequest](<cancelcontentauthorizationrequest().md>) — Cancels the currently outstanding content authorization request.
