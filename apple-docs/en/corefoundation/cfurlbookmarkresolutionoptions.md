---
title: CFURLBookmarkResolutionOptions
framework: Core Foundation
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 4.0+, iPadOS 4.0+, Mac Catalyst 13.1+, macOS 10.6+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/corefoundation/cfurlbookmarkresolutionoptions
source_url: 'https://developer.apple.com/documentation/corefoundation/cfurlbookmarkresolutionoptions'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/corefoundation/cfurlbookmarkresolutionoptions.json'
content_hash: 'sha256:f46949ef5685b46b'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Foundation](../corefoundation.md)

# CFURLBookmarkResolutionOptions

<sub>Structure</sub>

Type for bookmark data resolution options.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
struct CFURLBookmarkResolutionOptions
```

## Overview

See [Bookmark Data Resolution Options](bookmark-data-resolution-options.md) for possible values.

## Relationships

- **Conforms To**: [BitwiseCopyable](../swift/bitwisecopyable.md), [Equatable](../swift/equatable.md), [ExpressibleByArrayLiteral](../swift/expressiblebyarrayliteral.md), [OptionSet](../swift/optionset.md), [RawRepresentable](../swift/rawrepresentable.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md), [SetAlgebra](../swift/setalgebra.md)

## Topics

### Initializers

- [init(rawValue:)](<cfurlbookmarkresolutionoptions/init(rawvalue_).md>)

### Type Properties

- [kCFBookmarkResolutionWithoutMountingMask](cfurlbookmarkresolutionoptions/cfbookmarkresolutionwithoutmountingmask.md) — Specifies that no volume should be mounted during resolution of the bookmark data.
- [kCFBookmarkResolutionWithoutUIMask](cfurlbookmarkresolutionoptions/cfbookmarkresolutionwithoutuimask.md) — Specifies that no UI feedback accompany resolution of the bookmark data.
- [kCFURLBookmarkResolutionWithSecurityScope](cfurlbookmarkresolutionoptions/cfurlbookmarkresolutionwithsecurityscope.md) — Specifies that the security scope, applied to the bookmark when it was created, should be used during resolution of the bookmark data.
- [kCFURLBookmarkResolutionWithoutImplicitStartAccessing](cfurlbookmarkresolutionoptions/cfurlbookmarkresolutionwithoutimplicitstartaccessing.md)
- [kCFURLBookmarkResolutionWithoutMountingMask](cfurlbookmarkresolutionoptions/cfurlbookmarkresolutionwithoutmountingmask.md)
- [kCFURLBookmarkResolutionWithoutUIMask](cfurlbookmarkresolutionoptions/cfurlbookmarkresolutionwithoutuimask.md)

## See Also

### Bookmark Data Types

- [CFURLBookmarkCreationOptions](cfurlbookmarkcreationoptions.md) — Type for bookmark data creation options.
- [CFURLBookmarkFileCreationOptions](cfurlbookmarkfilecreationoptions.md) — Type for bookmark file creation options.
