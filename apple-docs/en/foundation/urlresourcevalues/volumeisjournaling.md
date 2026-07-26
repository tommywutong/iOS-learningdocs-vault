---
title: volumeIsJournaling
framework: Foundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 8.0+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/foundation/urlresourcevalues/volumeisjournaling
source_url: 'https://developer.apple.com/documentation/foundation/urlresourcevalues/volumeisjournaling'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/urlresourcevalues/volumeisjournaling.json'
content_hash: 'sha256:1e137ea4aa390b18'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [URLResourceValues](../urlresourcevalues.md)

# volumeIsJournaling

<sub>Instance Property</sub>

A Boolean value that indicates whether the volume is currently using a journal for speedy recovery after an unplanned restart.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var volumeIsJournaling: Bool? { get }
```

## See Also

### Volume status values

- [volumeIsAutomounted](volumeisautomounted.md) — A Boolean value that indicates whether the volume is automounted.
- [volumeIsBrowsable](volumeisbrowsable.md) — A Boolean value that indicates whether the volume is visible through the user interface.
- [volumeIsEjectable](volumeisejectable.md) — A Boolean value that indicates whether the volume’s media is ejectable from the drive mechanism under software control.
- [volumeIsEncrypted](volumeisencrypted.md) — A Boolean value that indicates whether the volume is encrypted.
- [volumeIsInternal](volumeisinternal.md) — A Boolean value that indicates whether the volume’s device is connected to an internal bus, or nil if not available.
- [volumeIsLocal](volumeislocal.md) — A Boolean value that indicates whether the volume is on a local device.
- [volumeIsReadOnly](volumeisreadonly.md) — A Boolean value that indicates whether the volume is read-only.
- [volumeIsRemovable](volumeisremovable.md) — A Boolean value that indicates whether the volume’s media is removable from the drive mechanism.
- [volumeIsRootFileSystem](volumeisrootfilesystem.md) — A Boolean value that indicates whether the volume is the root file system.
- [volumeTypeName](volumetypename.md) — The volume’s type name, as a string.
- [volumeSubtype](volumesubtype.md) — An integer value that indicates the file system subtype.
- [volumeMountFromLocation](volumemountfromlocation.md) — The file system device location, as a string.
