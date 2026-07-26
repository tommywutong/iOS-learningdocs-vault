---
title: CIDataMatrixCodeDescriptor.ECCVersion
framework: Core Image
symbol_kind: enum
role: symbol
role_heading: Enumeration
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/coreimage/cidatamatrixcodedescriptor/eccversion-swift.enum
source_url: 'https://developer.apple.com/documentation/coreimage/cidatamatrixcodedescriptor/eccversion-swift.enum'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coreimage/cidatamatrixcodedescriptor/eccversion-swift.enum.json'
content_hash: 'sha256:7bbaf3eea68950de'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Image](../../coreimage.md) · [CIDataMatrixCodeDescriptor](../cidatamatrixcodedescriptor.md)

# CIDataMatrixCodeDescriptor.ECCVersion

<sub>Enumeration</sub>

Constants indicating the Data Matrix code ECC version.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
enum ECCVersion
```

## Overview

ECC 000 - 140 symbols offer five levels of error correction using convolutional code error correction. Each successive level or error correction offers more protection for the message data but increases the size of the symbol required to carry a given message. See the ISO/IEC 16022:2006 spec for other modes.

ECC 200 symbols utilize Reed-Solomon error correction. The error correction capacity for any given Data Matrix symbol is fixed by the size (in rows and columns) of the symbol. See Table 7 of ISO/IEC 16022:2006(E) for more details.

## Relationships

- **Conforms To**: [BitwiseCopyable](../../swift/bitwisecopyable.md), [Equatable](../../swift/equatable.md), [Hashable](../../swift/hashable.md), [RawRepresentable](../../swift/rawrepresentable.md), [Sendable](../../swift/sendable.md), [SendableMetatype](../../swift/sendablemetatype.md)

## Topics

### Enumeration Cases

- [CIDataMatrixCodeECCVersion000](eccversion-swift.enum/v000.md) — Indicates error correction using convolutional code error correction with no data protection.
- [CIDataMatrixCodeECCVersion050](eccversion-swift.enum/v050.md) — Indicates 1/4 of the symbol is dedicated to convolutional code error correction.
- [CIDataMatrixCodeECCVersion080](eccversion-swift.enum/v080.md) — Indicates 1/3 of the symbol is dedicated to convolutional code error correction.
- [CIDataMatrixCodeECCVersion100](eccversion-swift.enum/v100.md) — Indicates 1/2 of the symbol is dedicated to convolutional code error correction.
- [CIDataMatrixCodeECCVersion140](eccversion-swift.enum/v140.md) — Indicates 3/4 of the symbol is dedicated to convolutional code error correction.
- [CIDataMatrixCodeECCVersion200](eccversion-swift.enum/v200.md) — Indicates error correction using Reed-Solomon error correction. Data protection overhead varies based on symbol size.

### Initializers

- [init(rawValue:)](<eccversion-swift.enum/init(rawvalue_).md>)
