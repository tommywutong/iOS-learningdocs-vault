---
title: MTLGPUFamily
framework: Metal
symbol_kind: enum
role: symbol
role_heading: Enumeration
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.1+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/metal/mtlgpufamily
source_url: 'https://developer.apple.com/documentation/metal/mtlgpufamily'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtlgpufamily.json'
content_hash: 'sha256:399dbda748ba6fb4'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Metal](../metal.md)

# MTLGPUFamily

<sub>Enumeration</sub>

Represents the functionality for families of GPUs.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
enum MTLGPUFamily
```

## Overview

Check whether a GPU supports the features of a specific family by calling the [- supportsFamily:](<mtldevice/supportsfamily(__).md>) method of a GPU’s [MTLDevice](mtldevice.md) instance.

## Relationships

- **Conforms To**: [BitwiseCopyable](../swift/bitwisecopyable.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [RawRepresentable](../swift/rawrepresentable.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md)

## Topics

### Checking for Metal family GPU support

- [MTLGPUFamilyMetal4](mtlgpufamily/metal4.md)
- [MTLGPUFamilyMetal3](mtlgpufamily/metal3.md) — Represents the Metal 3 features.

### Checking for Apple family GPU support

- [MTLGPUFamilyApple9](mtlgpufamily/apple9.md) — Represents the Apple family 9 GPU features that correspond to the Apple A17, M3, and M4 GPUs.
- [MTLGPUFamilyApple8](mtlgpufamily/apple8.md) — Represents the Apple family 8 GPU features that correspond to the Apple A15, A16, and M2 GPUs.
- [MTLGPUFamilyApple7](mtlgpufamily/apple7.md) — Represents the Apple family 7 GPU features that correspond to the Apple A14 and M1 GPUs.
- [MTLGPUFamilyApple6](mtlgpufamily/apple6.md) — Represents the Apple family 6 GPU features that correspond to the Apple A13 GPUs.
- [MTLGPUFamilyApple5](mtlgpufamily/apple5.md) — Represents the Apple family 5 GPU features that correspond to the Apple A12 GPUs.
- [MTLGPUFamilyApple4](mtlgpufamily/apple4.md) — Represents the Apple family 4 GPU features that correspond to the Apple A11 GPUs.
- [MTLGPUFamilyApple3](mtlgpufamily/apple3.md) — Represents the Apple family 3 GPU features that correspond to the Apple A9 and A10 GPUs.
- [MTLGPUFamilyApple2](mtlgpufamily/apple2.md) — Represents the Apple family 2 GPU features that correspond to the Apple A8 GPUs.
- [MTLGPUFamilyApple1](mtlgpufamily/apple1.md) — Represents the Apple family 1 GPU features that correspond to the Apple A7 GPUs.

### Checking for common GPU support

- [MTLGPUFamilyCommon3](mtlgpufamily/common3.md) — Represents the Common family 3 GPU features. _(deprecated)_
- [MTLGPUFamilyCommon2](mtlgpufamily/common2.md) — Represents the Common family 2 GPU features. _(deprecated)_
- [MTLGPUFamilyCommon1](mtlgpufamily/common1.md) — Represents the Common family 1 GPU features. _(deprecated)_

### Checking for macOS family GPU support

- [MTLGPUFamilyMac2](mtlgpufamily/mac2.md) — Represents the Mac family 2 GPU features. _(deprecated)_
- [MTLGPUFamilyMac1](mtlgpufamily/mac1.md) — Represents the Mac family 1 GPU features. _(deprecated)_

### Checking for Mac Catalyst family GPU support

- [MTLGPUFamilyMacCatalyst2](mtlgpufamily/maccatalyst2.md) — Represents a family 2 Mac GPU when running an app you built with Mac Catalyst. _(deprecated)_
- [MTLGPUFamilyMacCatalyst1](mtlgpufamily/maccatalyst1.md) — Represents a family 1 Mac GPU when running an app you built with Mac Catalyst. _(deprecated)_

### Swift support

- [init(rawValue:)](<mtlgpufamily/init(rawvalue_).md>) — Creates a GPU family instance from a raw value.

### Enumeration Cases

- [MTLGPUFamilyApple10](mtlgpufamily/apple10.md)

## See Also

### Checking a GPU device’s feature support

- [- supportsFamily:](<mtldevice/supportsfamily(__).md>) — Returns a Boolean value that indicates whether the GPU device supports the feature set of a specific GPU family.
- [- supportsFeatureSet:](<mtldevice/supportsfeatureset(__).md>) — Returns a Boolean value that indicates whether the GPU device supports a specific feature set. _(deprecated)_
- [MTLFeatureSet](mtlfeatureset.md) — The device feature sets that define specific platform, hardware, and software configurations. _(deprecated)_
