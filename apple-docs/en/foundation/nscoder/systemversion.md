---
title: systemVersion
framework: Foundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.0+, macOS 10.0+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/nscoder/systemversion
source_url: 'https://developer.apple.com/documentation/foundation/nscoder/systemversion'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nscoder/systemversion.json'
content_hash: 'sha256:268c1cc26039165c'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSCoder](../nscoder.md)

# systemVersion

<sub>Instance Property</sub>

The system version in effect for the archive.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var systemVersion: UInt32 { get }
```

## Discussion

During encoding, the current version. During decoding, the version that was in effect when the data was encoded.

Subclasses that implement decoding must override this property to return the system version of the data being decoded.

## See Also

### Getting Version Information

- [- versionForClassName:](<version(forclassname_).md>) — This method is present for historical reasons and is not used with keyed archivers.
