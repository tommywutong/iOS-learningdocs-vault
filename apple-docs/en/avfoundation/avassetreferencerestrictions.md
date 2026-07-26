---
title: AVAssetReferenceRestrictions
framework: AVFoundation
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avassetreferencerestrictions
source_url: 'https://developer.apple.com/documentation/avfoundation/avassetreferencerestrictions'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avassetreferencerestrictions.json'
content_hash: 'sha256:9460a544a996fd0c'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [AVFoundation](../avfoundation.md)

# AVAssetReferenceRestrictions

<sub>Structure</sub>

Restrictions to use when resolving references to external media data.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
struct AVAssetReferenceRestrictions
```

## Relationships

- **Conforms To**: [BitwiseCopyable](../swift/bitwisecopyable.md), [Equatable](../swift/equatable.md), [ExpressibleByArrayLiteral](../swift/expressiblebyarrayliteral.md), [OptionSet](../swift/optionset.md), [RawRepresentable](../swift/rawrepresentable.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md), [SetAlgebra](../swift/setalgebra.md)

## Topics

### Reference restrictions

- [AVAssetReferenceRestrictionForbidAll](avassetreferencerestrictions/forbidall.md) — The asset can only reference media stored within its container file.
- [AVAssetReferenceRestrictionForbidRemoteReferenceToLocal](avassetreferencerestrictions/forbidremotereferencetolocal.md) — A remote asset shouldn’t follow references to local media.
- [AVAssetReferenceRestrictionForbidLocalReferenceToRemote](avassetreferencerestrictions/forbidlocalreferencetoremote.md) — A local asset shouldn’t follow references to remote media.
- [AVAssetReferenceRestrictionForbidCrossSiteReference](avassetreferencerestrictions/forbidcrosssitereference.md) — A remote asset shouldn’t follow references to remote media data stored at a different host.
- [AVAssetReferenceRestrictionForbidLocalReferenceToLocal](avassetreferencerestrictions/forbidlocalreferencetolocal.md) — A local asset shouldn’t follow references to local media data stored outside its container file.
- [AVAssetReferenceRestrictionDefaultPolicy](avassetreferencerestrictions/defaultpolicy.md) — The asset should use the default reference restrictions policy.

### Initializers

- [init(rawValue:)](<avassetreferencerestrictions/init(rawvalue_).md>) — Creates reference restrictions with an integer value.

## See Also

### Retrieving reference restrictions

- [referenceRestrictions](avasset/referencerestrictions.md) — The restrictions that an asset places on how it resolves references to external media.
