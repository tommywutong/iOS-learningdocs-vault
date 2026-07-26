---
title: AVAuthorizationStatus.notDetermined
framework: AVFoundation
symbol_kind: case
role: symbol
role_heading: Case
platforms: [iOS 7.0+, iPadOS 7.0+, Mac Catalyst 14.0+, macOS 10.14+, tvOS 17.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avauthorizationstatus/notdetermined
source_url: 'https://developer.apple.com/documentation/avfoundation/avauthorizationstatus/notdetermined'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avauthorizationstatus/notdetermined.json'
content_hash: 'sha256:46c2552fa1d49310'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVAuthorizationStatus](../avauthorizationstatus.md)

# AVAuthorizationStatus.notDetermined

<sub>Case</sub>

A status that indicates the user hasn’t yet granted or denied authorization.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
case notDetermined
```

## Discussion

This is the default status prior to user to granting or denying recording priviledge to the app. Call [+ requestAccessForMediaType:completionHandler:](<../avcapturedevice/requestaccess(for_completionhandler_).md>) to prompt the user for permission.

## See Also

### Status values

- [AVAuthorizationStatusRestricted](restricted.md) — A status that indicates the app isn’t permitted to use media capture devices.
- [AVAuthorizationStatusDenied](denied.md) — A status that indicates the user has explicitly denied an app permission to capture media.
- [AVAuthorizationStatusAuthorized](authorized.md) — A status that indicates the user has explicitly granted an app permission to capture media.
