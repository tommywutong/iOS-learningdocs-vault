---
title: authorizationStatus
framework: SwiftUI
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [visionOS 26.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/surfacesnappinginfo/authorizationstatus-swift.type.property
source_url: 'https://developer.apple.com/documentation/swiftui/surfacesnappinginfo/authorizationstatus-swift.type.property'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/surfacesnappinginfo/authorizationstatus-swift.type.property.json'
content_hash: 'sha256:7c3720ae3b61c42d'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [SurfaceSnappingInfo](../surfacesnappinginfo.md)

# authorizationStatus

<sub>Type Property</sub>

A value that represents whether the user has authorized providing more detailed information about the surface scenes are snapped to. To request this detailed surface information, in your `Info.plist` file, set `UIWantsDetailedSurfaceInfo` to `YES` and set `NSWorldSensingUsageDescription` to provide a description of why your app is requesting this information.

<sub>visionOS</sub>

```swift
static var authorizationStatus: SurfaceSnappingInfo.AuthorizationStatus { get }
```
