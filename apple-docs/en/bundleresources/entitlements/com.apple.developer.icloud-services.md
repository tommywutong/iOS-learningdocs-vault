---
title: iCloud Services Entitlement
framework: Bundle Resources
symbol_kind: typealias
role: symbol
role_heading: Property List Key
platforms: [iOS 3.0+, iPadOS 3.0+, macOS 10.7+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/bundleresources/entitlements/com.apple.developer.icloud-services
source_url: 'https://developer.apple.com/documentation/bundleresources/entitlements/com.apple.developer.icloud-services'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/bundleresources/entitlements/com.apple.developer.icloud-services.json'
content_hash: 'sha256:065f4600de4b5228'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Bundle Resources](../../bundleresources.md) · [Entitlements](../entitlements.md)

# iCloud Services Entitlement

<sub>Property List Key</sub>

The iCloud services used by the app.

## Discussion

To add this entitlement to your app, enable the iCloud capability and the iCloud Documents or CloudKit service in Xcode.

The value `CloudKit-Anonymous` is only available to App Clips, but App Clips can’t use the values `CloudDocuments` or `CloudKit`. For more information on using CloudKit in your App Clip, see [Sharing data between your App Clip and your full app](../../appclip/sharing-data-between-your-app-clip-and-your-full-app.md).

## See Also

### iCloud

- [com.apple.developer.icloud-container-development-container-identifiers](com.apple.developer.icloud-container-development-container-identifiers.md) — The container identifiers for the iCloud development environment.
- [com.apple.developer.icloud-container-environment](com.apple.developer.icloud-container-environment.md) — The development or production environment to use for the iCloud containers.
- [iCloud Container Identifiers Entitlement](com.apple.developer.icloud-container-identifiers.md) — The container identifiers for the iCloud production environment.
- [iCloud Key-Value Store Entitlement](com.apple.developer.ubiquity-kvstore-identifier.md) — The container identifier to use for iCloud key-value storage.
