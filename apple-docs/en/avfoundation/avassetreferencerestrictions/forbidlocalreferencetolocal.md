---
title: forbidLocalReferenceToLocal
framework: AVFoundation
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avassetreferencerestrictions/forbidlocalreferencetolocal
source_url: 'https://developer.apple.com/documentation/avfoundation/avassetreferencerestrictions/forbidlocalreferencetolocal'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avassetreferencerestrictions/forbidlocalreferencetolocal.json'
content_hash: 'sha256:001088587fc7662c'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVAssetReferenceRestrictions](../avassetreferencerestrictions.md)

# forbidLocalReferenceToLocal

<sub>Type Property</sub>

A local asset shouldn’t follow references to local media data stored outside its container file.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
static var forbidLocalReferenceToLocal: AVAssetReferenceRestrictions { get }
```

## See Also

### Reference restrictions

- [AVAssetReferenceRestrictionForbidAll](forbidall.md) — The asset can only reference media stored within its container file.
- [AVAssetReferenceRestrictionForbidRemoteReferenceToLocal](forbidremotereferencetolocal.md) — A remote asset shouldn’t follow references to local media.
- [AVAssetReferenceRestrictionForbidLocalReferenceToRemote](forbidlocalreferencetoremote.md) — A local asset shouldn’t follow references to remote media.
- [AVAssetReferenceRestrictionForbidCrossSiteReference](forbidcrosssitereference.md) — A remote asset shouldn’t follow references to remote media data stored at a different host.
- [AVAssetReferenceRestrictionDefaultPolicy](defaultpolicy.md) — The asset should use the default reference restrictions policy.
