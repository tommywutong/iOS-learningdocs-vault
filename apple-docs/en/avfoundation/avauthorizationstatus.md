---
title: AVAuthorizationStatus
framework: AVFoundation
symbol_kind: enum
role: symbol
role_heading: Enumeration
platforms: [iOS 7.0+, iPadOS 7.0+, Mac Catalyst 14.0+, macOS 10.14+, tvOS 17.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avauthorizationstatus
source_url: 'https://developer.apple.com/documentation/avfoundation/avauthorizationstatus'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avauthorizationstatus.json'
content_hash: 'sha256:67ccc68ebae2afbc'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [AVFoundation](../avfoundation.md)

# AVAuthorizationStatus

<sub>Enumeration</sub>

Constants that indicate the status of an app’s authorization to capture media.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
enum AVAuthorizationStatus
```

## Overview

Call [+ authorizationStatusForMediaType:](<avcapturedevice/authorizationstatus(for_).md>) to determine the app’s current permission to capture media.

## Relationships

- **Conforms To**: [BitwiseCopyable](../swift/bitwisecopyable.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [RawRepresentable](../swift/rawrepresentable.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md)

## Topics

### Status values

- [AVAuthorizationStatusNotDetermined](avauthorizationstatus/notdetermined.md) — A status that indicates the user hasn’t yet granted or denied authorization.
- [AVAuthorizationStatusRestricted](avauthorizationstatus/restricted.md) — A status that indicates the app isn’t permitted to use media capture devices.
- [AVAuthorizationStatusDenied](avauthorizationstatus/denied.md) — A status that indicates the user has explicitly denied an app permission to capture media.
- [AVAuthorizationStatusAuthorized](avauthorizationstatus/authorized.md) — A status that indicates the user has explicitly granted an app permission to capture media.

### Initializers

- [init(rawValue:)](<avauthorizationstatus/init(rawvalue_).md>)

## See Also

### Authorizing device access

- [+ requestAccessForMediaType:completionHandler:](<avcapturedevice/requestaccess(for_completionhandler_).md>) — Requests the user’s permission to allow the app to capture media of a particular type.
- [+ authorizationStatusForMediaType:](<avcapturedevice/authorizationstatus(for_).md>) — Returns an authorization status that indicates whether the user grants the app permission to capture media of a particular type.
