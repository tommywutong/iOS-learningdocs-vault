---
title: url
framework: Foundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 5.0+, iPadOS 5.0+, Mac Catalyst 13.1+, macOS 10.7+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, swift, swift, occ, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/nsfileversion/url
source_url: 'https://developer.apple.com/documentation/foundation/nsfileversion/url'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsfileversion/url.json'
content_hash: 'sha256:be043ef15ea43e07'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSFileVersion](../nsfileversion.md)

# url

<sub>Instance Property</sub>

The URL identifying the location of the file associated with the file version object.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var url: URL { get }
```

## Discussion

The URL identifies the location of the file associated with this version. If this version of the file has been deleted, the value in this property is `nil`.

Do not display any part of this URL to the user. The location of file versions is managed by the system and should not be exposed to the user. If you want to present the name of a file version, use the [localizedName](localizedname.md) property.

## See Also

### Accessing the Version Information

- [localizedName](localizedname.md) — The string containing the user-presentable name of the file version.
- [localizedNameOfSavingComputer](localizednameofsavingcomputer.md) — The user-presentable name of the computer on which the revision was saved.
- [modificationDate](modificationdate.md) — The modification date of the version.
- [persistentIdentifier](persistentidentifier.md) — The identifier for this version of the file.
- [discardable](isdiscardable.md) — A Boolean value that specifies whether the system can delete the associated file at some future time.
