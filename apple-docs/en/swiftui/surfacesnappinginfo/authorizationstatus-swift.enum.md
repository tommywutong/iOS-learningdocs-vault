---
title: SurfaceSnappingInfo.AuthorizationStatus
framework: SwiftUI
symbol_kind: enum
role: symbol
role_heading: Enumeration
platforms: [visionOS 26.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/surfacesnappinginfo/authorizationstatus-swift.enum
source_url: 'https://developer.apple.com/documentation/swiftui/surfacesnappinginfo/authorizationstatus-swift.enum'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/surfacesnappinginfo/authorizationstatus-swift.enum.json'
content_hash: 'sha256:d6fa25cd74835875'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [SurfaceSnappingInfo](../surfacesnappinginfo.md)

# SurfaceSnappingInfo.AuthorizationStatus

<sub>Enumeration</sub>

A type representing whether the user has granted permissions to provide more detailed information about the surface a scene is snapped to.

<sub>visionOS</sub>

```swift
enum AuthorizationStatus
```

## Overview

To provide `ARKit/SurfaceClassification` data, the user must allow the app to access information about their surroundings. To request this data, set `UIWantsDetailedSurfaceInfo` to `YES` and set `NSWorldSensingUsageDescription` to provide a description of why your app is requesting this information. These values are set in your app’s `Info.plist` file.

## Relationships

- **Conforms To**: [Equatable](../../swift/equatable.md), [Hashable](../../swift/hashable.md), [Sendable](../../swift/sendable.md), [SendableMetatype](../../swift/sendablemetatype.md)

## Topics

### Enumeration Cases

- [SurfaceSnappingInfo.AuthorizationStatus.authorized](authorizationstatus-swift.enum/authorized.md) — The user has authorized sharing information about their surroundings.
- [SurfaceSnappingInfo.AuthorizationStatus.denied](authorizationstatus-swift.enum/denied.md) — The user denied providing access to information about their surroundings.
- [SurfaceSnappingInfo.AuthorizationStatus.notDetermined](authorizationstatus-swift.enum/notdetermined.md) — The user has not yet authorized or denied providing information about their surroundings. Set `UIWantsDetailedSurfaceInfo` to `YES` in your `Info.plist` to request information about the user’s surroundings when they first snap a scene from your app.
- [SurfaceSnappingInfo.AuthorizationStatus.restricted](authorizationstatus-swift.enum/restricted.md) — The user is unable to grant authorization to share detailed information about their surroundings.
