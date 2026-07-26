---
title: Maps Entitlement
framework: Bundle Resources
symbol_kind: typealias
role: symbol
role_heading: Property List Key
platforms: [macOS 10.9+（10.11 起废弃）]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: /documentation/bundleresources/entitlements/com.apple.developer.maps
source_url: 'https://developer.apple.com/documentation/bundleresources/entitlements/com.apple.developer.maps'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/bundleresources/entitlements/com.apple.developer.maps.json'
content_hash: 'sha256:d1c1b2b61ad46637'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Bundle Resources](../../bundleresources.md) · [Entitlements](../entitlements.md)

# Maps Entitlement

<sub>Property List Key</sub>

A Boolean value that indicates whether the app may provide directions beyond what Maps supports, such as subway routes, hiking trails, and bike paths.

> [!warning] Deprecated
> Using Maps no longer requires an entitlement.

## Discussion

To add this entitlement to your app, enable the Maps capability in Xcode.

## See Also

### Deprecated entitlements

- [Inter-App Audio Entitlement](inter-app-audio.md) — A Boolean value that indicates whether the app may exchange audio with other Inter-App Audio-enabled apps. _(deprecated)_
- [All files entitlement](com.apple.security.files.all.md) — A Boolean value that indicates whether the app may have access to all files. _(deprecated)_
