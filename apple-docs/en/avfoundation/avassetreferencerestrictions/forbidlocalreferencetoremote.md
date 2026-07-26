---
title: forbidLocalReferenceToRemote
framework: AVFoundation
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avassetreferencerestrictions/forbidlocalreferencetoremote
source_url: 'https://developer.apple.com/documentation/avfoundation/avassetreferencerestrictions/forbidlocalreferencetoremote'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avassetreferencerestrictions/forbidlocalreferencetoremote.json'
content_hash: 'sha256:8f9cc8d47f23fa26'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVAssetReferenceRestrictions](../avassetreferencerestrictions.md)

# forbidLocalReferenceToRemote

<sub>Type Property</sub>

A local asset shouldn’t follow references to remote media.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
static var forbidLocalReferenceToRemote: AVAssetReferenceRestrictions { get }
```

## See Also

### Reference restrictions

- [AVAssetReferenceRestrictionForbidAll](forbidall.md) — The asset can only reference media stored within its container file.
- [AVAssetReferenceRestrictionForbidRemoteReferenceToLocal](forbidremotereferencetolocal.md) — A remote asset shouldn’t follow references to local media.
- [AVAssetReferenceRestrictionForbidCrossSiteReference](forbidcrosssitereference.md) — A remote asset shouldn’t follow references to remote media data stored at a different host.
- [AVAssetReferenceRestrictionForbidLocalReferenceToLocal](forbidlocalreferencetolocal.md) — A local asset shouldn’t follow references to local media data stored outside its container file.
- [AVAssetReferenceRestrictionDefaultPolicy](defaultpolicy.md) — The asset should use the default reference restrictions policy.
