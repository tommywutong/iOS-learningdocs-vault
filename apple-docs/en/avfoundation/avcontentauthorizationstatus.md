---
title: AVContentAuthorizationStatus
framework: AVFoundation
symbol_kind: enum
role: symbol
role_heading: Enumeration
platforms: [macOS 10.7+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avcontentauthorizationstatus
source_url: 'https://developer.apple.com/documentation/avfoundation/avcontentauthorizationstatus'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avcontentauthorizationstatus.json'
content_hash: 'sha256:0fd557329383d3b2'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [AVFoundation](../avfoundation.md)

# AVContentAuthorizationStatus

<sub>Enumeration</sub>

A value representing the status of a content authorization request.

<sub>macOS</sub>

```swift
enum AVContentAuthorizationStatus
```

## Overview

Even if authorization is completed by the user, there is no guarantee that the content will then be authorized. You should re-check whether the content is authorized before proceeding.

## Relationships

- **Conforms To**: [BitwiseCopyable](../swift/bitwisecopyable.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [RawRepresentable](../swift/rawrepresentable.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md)

## Topics

### Content authorization statuses

- [AVContentAuthorizationUnknown](avcontentauthorizationstatus/unknown.md) — The content authorization content request hasn’t completed.
- [AVContentAuthorizationCompleted](avcontentauthorizationstatus/completed.md) — The last completed call to request content authorization completed.
- [AVContentAuthorizationCancelled](avcontentauthorizationstatus/cancelled.md) — The last call to request content authorization was cancelled by the user.
- [AVContentAuthorizationTimedOut](avcontentauthorizationstatus/timedout.md) — The last call to request content authorization was cancelled because the timeout interval was reached.
- [AVContentAuthorizationBusy](avcontentauthorizationstatus/busy.md) — The last call to request content authorization couldn’t be completed because another asset is currently attempting authorization.
- [AVContentAuthorizationNotAvailable](avcontentauthorizationstatus/notavailable.md) — The last call to request content authorization couldn’t be completed because there was no known mechanism by which to attempt authorization.
- [AVContentAuthorizationNotPossible](avcontentauthorizationstatus/notpossible.md) — The last call to request content authorization couldn’t be completed in a non-recoverable way.

### Initializers

- [init(rawValue:)](<avcontentauthorizationstatus/init(rawvalue_).md>)

## See Also

### Managing playback authorization in macOS

- [contentAuthorizedForPlayback](avplayeritem/iscontentauthorizedforplayback.md) — A Boolean value that indicates whether the content has been authorized by the user.
- [authorizationRequiredForPlayback](avplayeritem/isauthorizationrequiredforplayback.md) — A Boolean value that indicates whether authorization is required to play the content.
- [applicationAuthorizedForPlayback](avplayeritem/isapplicationauthorizedforplayback.md) — A Boolean value that indicates whether the application can be used to play the content.
- [- requestContentAuthorizationAsynchronouslyWithTimeoutInterval:completionHandler:](<avplayeritem/requestcontentauthorizationasynchronously(withtimeoutinterval_completionhandler_).md>) — Presents the user the opportunity to authorize the content for playback.
- [contentAuthorizationRequestStatus](avplayeritem/contentauthorizationrequeststatus.md) — The status of the most recent content authorization request.
- [- cancelContentAuthorizationRequest](<avplayeritem/cancelcontentauthorizationrequest().md>) — Cancels the currently outstanding content authorization request.
