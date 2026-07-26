---
title: AVAuthorizationStatus.restricted
framework: AVFoundation
symbol_kind: case
role: symbol
role_heading: Case
platforms: [iOS 7.0+, iPadOS 7.0+, Mac Catalyst 14.0+, macOS 10.14+, tvOS 17.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avauthorizationstatus/restricted
source_url: 'https://developer.apple.com/documentation/avfoundation/avauthorizationstatus/restricted'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avauthorizationstatus/restricted.json'
content_hash: 'sha256:91ef949e45ccefef'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVAuthorizationStatus](../avauthorizationstatus.md)

# AVAuthorizationStatus.restricted

<sub>Case</sub>

A status that indicates the app isn’t permitted to use media capture devices.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
case restricted
```

## Discussion

This status occurs when a user can’t change the authorization status, possibly due to the system imposing restrictions like parental controls.

## See Also

### Status values

- [AVAuthorizationStatusNotDetermined](notdetermined.md) — A status that indicates the user hasn’t yet granted or denied authorization.
- [AVAuthorizationStatusDenied](denied.md) — A status that indicates the user has explicitly denied an app permission to capture media.
- [AVAuthorizationStatusAuthorized](authorized.md) — A status that indicates the user has explicitly granted an app permission to capture media.
