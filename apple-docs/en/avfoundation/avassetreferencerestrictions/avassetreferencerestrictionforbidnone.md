---
title: AVAssetReferenceRestrictionForbidNone
framework: AVFoundation
symbol_kind: case
role: symbol
role_heading: Enumeration Case
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS]
languages: [occ, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avassetreferencerestrictions/avassetreferencerestrictionforbidnone
source_url: 'https://developer.apple.com/documentation/avfoundation/avassetreferencerestrictions/avassetreferencerestrictionforbidnone'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avassetreferencerestrictions/avassetreferencerestrictionforbidnone.json'
content_hash: 'sha256:8b50f749107f32ec'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVAssetReferenceRestrictions](../avassetreferencerestrictions.md)

# AVAssetReferenceRestrictionForbidNone

<sub>Enumeration Case</sub>

The asset should follow all media references.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```objc
AVAssetReferenceRestrictionForbidNone
```

## See Also

### Reference restrictions

- [AVAssetReferenceRestrictionForbidAll](forbidall.md) — The asset can only reference media stored within its container file.
- [AVAssetReferenceRestrictionForbidRemoteReferenceToLocal](forbidremotereferencetolocal.md) — A remote asset shouldn’t follow references to local media.
- [AVAssetReferenceRestrictionForbidLocalReferenceToRemote](forbidlocalreferencetoremote.md) — A local asset shouldn’t follow references to remote media.
- [AVAssetReferenceRestrictionForbidCrossSiteReference](forbidcrosssitereference.md) — A remote asset shouldn’t follow references to remote media data stored at a different host.
- [AVAssetReferenceRestrictionForbidLocalReferenceToLocal](forbidlocalreferencetolocal.md) — A local asset shouldn’t follow references to local media data stored outside its container file.
- [AVAssetReferenceRestrictionDefaultPolicy](defaultpolicy.md) — The asset should use the default reference restrictions policy.
