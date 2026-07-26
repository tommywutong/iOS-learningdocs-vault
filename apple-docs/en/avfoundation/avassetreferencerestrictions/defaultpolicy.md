---
title: defaultPolicy
framework: AVFoundation
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avassetreferencerestrictions/defaultpolicy
source_url: 'https://developer.apple.com/documentation/avfoundation/avassetreferencerestrictions/defaultpolicy'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avassetreferencerestrictions/defaultpolicy.json'
content_hash: 'sha256:126f05c01228bee6'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVAssetReferenceRestrictions](../avassetreferencerestrictions.md)

# defaultPolicy

<sub>Type Property</sub>

The asset should use the default reference restrictions policy.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
static var defaultPolicy: AVAssetReferenceRestrictions { get }
```

## Discussion

The default policy is [AVAssetReferenceRestrictionForbidLocalReferenceToRemote](forbidlocalreferencetoremote.md).

## See Also

### Reference restrictions

- [AVAssetReferenceRestrictionForbidAll](forbidall.md) — The asset can only reference media stored within its container file.
- [AVAssetReferenceRestrictionForbidRemoteReferenceToLocal](forbidremotereferencetolocal.md) — A remote asset shouldn’t follow references to local media.
- [AVAssetReferenceRestrictionForbidLocalReferenceToRemote](forbidlocalreferencetoremote.md) — A local asset shouldn’t follow references to remote media.
- [AVAssetReferenceRestrictionForbidCrossSiteReference](forbidcrosssitereference.md) — A remote asset shouldn’t follow references to remote media data stored at a different host.
- [AVAssetReferenceRestrictionForbidLocalReferenceToLocal](forbidlocalreferencetolocal.md) — A local asset shouldn’t follow references to local media data stored outside its container file.
