---
title: forbidRemoteReferenceToLocal
framework: AVFoundation
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avassetreferencerestrictions/forbidremotereferencetolocal
source_url: 'https://developer.apple.com/documentation/avfoundation/avassetreferencerestrictions/forbidremotereferencetolocal'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avassetreferencerestrictions/forbidremotereferencetolocal.json'
content_hash: 'sha256:833e40e663fd983b'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVAssetReferenceRestrictions](../avassetreferencerestrictions.md)

# forbidRemoteReferenceToLocal

<sub>Type Property</sub>

A remote asset shouldn’t follow references to local media.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
static var forbidRemoteReferenceToLocal: AVAssetReferenceRestrictions { get }
```

## See Also

### Reference restrictions

- [AVAssetReferenceRestrictionForbidAll](forbidall.md) — The asset can only reference media stored within its container file.
- [AVAssetReferenceRestrictionForbidLocalReferenceToRemote](forbidlocalreferencetoremote.md) — A local asset shouldn’t follow references to remote media.
- [AVAssetReferenceRestrictionForbidCrossSiteReference](forbidcrosssitereference.md) — A remote asset shouldn’t follow references to remote media data stored at a different host.
- [AVAssetReferenceRestrictionForbidLocalReferenceToLocal](forbidlocalreferencetolocal.md) — A local asset shouldn’t follow references to local media data stored outside its container file.
- [AVAssetReferenceRestrictionDefaultPolicy](defaultpolicy.md) — The asset should use the default reference restrictions policy.
