---
title: MTLFeatureSet
framework: Metal
symbol_kind: enum
role: symbol
role_heading: Enumeration
platforms: [iOS 8.0+（16.0 起废弃）, iPadOS 8.0+（16.0 起废弃）, Mac Catalyst 13.1+（16.0 起废弃）, macOS 10.11+（13.0 起废弃）, tvOS 9.0+（16.0 起废弃）, visionOS 1.0+（1.0 起废弃）]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: /documentation/metal/mtlfeatureset
source_url: 'https://developer.apple.com/documentation/metal/mtlfeatureset'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtlfeatureset.json'
content_hash: 'sha256:bc7e68ba423744b4'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Metal](../metal.md)

# MTLFeatureSet

<sub>Enumeration</sub>

The device feature sets that define specific platform, hardware, and software configurations.

> [!warning] Deprecated
> Use [MTLGPUFamily](mtlgpufamily.md) instead.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
enum MTLFeatureSet
```

## Overview

If your app is running on an operating system that supports the [- supportsFamily:](<mtldevice/supportsfamily(__).md>) method, use that method instead. See [Detecting GPU features and Metal software versions](detecting-gpu-features-and-metal-software-versions.md) for more information about [MTLGPUFamily](mtlgpufamily.md) — the replacement for this enumeration —  and the feature set tables. This type doesn’t define constants for GPU families introduced after iOS GPU family 5.

Metal feature sets define the feature availability, implementation limits, and pixel format capabilities for each device. The table shows the GPU families and their corresponding GPU hardware.

| GPU family | GPU hardware |
|---|---|
| iOS GPU family 1 | Apple A7 devices |
| iOS GPU family 2 ![](../../../attachments/67dc4b07a8d84366d4cc0e812eb40b4a/spacer.png) tvOS GPU family 1 | Apple A8 devices |
| iOS GPU family 3 ![](../../../attachments/67dc4b07a8d84366d4cc0e812eb40b4a/spacer.png) tvOS GPU family 2 | Apple A9 devices ![](../../../attachments/67dc4b07a8d84366d4cc0e812eb40b4a/spacer.png) Apple A10 devices |
| iOS GPU family 4 | Apple A11 devices |
| iOS GPU family 5 | Apple A12 devices |
| macOS GPU family 1 | iMac Pro models ![](../../../attachments/67dc4b07a8d84366d4cc0e812eb40b4a/spacer.png) iMac models from 2012 or later ![](../../../attachments/67dc4b07a8d84366d4cc0e812eb40b4a/spacer.png) MacBook models from 2015 or later ![](../../../attachments/67dc4b07a8d84366d4cc0e812eb40b4a/spacer.png) MacBook Pro models from 2012 or later ![](../../../attachments/67dc4b07a8d84366d4cc0e812eb40b4a/spacer.png) MacBook Air models from 2012 or later ![](../../../attachments/67dc4b07a8d84366d4cc0e812eb40b4a/spacer.png) Mac mini models from 2012 or later ![](../../../attachments/67dc4b07a8d84366d4cc0e812eb40b4a/spacer.png) Mac Pro models from late 2013 |
| macOS GPU family 2 | iMac models from 2015 or later ![](../../../attachments/67dc4b07a8d84366d4cc0e812eb40b4a/spacer.png) MacBook Pro models from 2016 or later ![](../../../attachments/67dc4b07a8d84366d4cc0e812eb40b4a/spacer.png) MacBook models from 2016 or later ![](../../../attachments/67dc4b07a8d84366d4cc0e812eb40b4a/spacer.png) iMac Pro models from 2017 or later |

For more information on Mac support for Metal, see [Mac computers that support Metal](https://support.apple.com/en-us/HT205073).

## Relationships

- **Conforms To**: [BitwiseCopyable](../swift/bitwisecopyable.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [RawRepresentable](../swift/rawrepresentable.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md)

## Topics

### iOS GPU family 5

- [MTLFeatureSet_iOS_GPUFamily5_v1](mtlfeatureset/ios_gpufamily5_v1.md) — The GPU family 5, version 1 feature set for iOS. _(deprecated)_

### iOS GPU family 4

- [MTLFeatureSet_iOS_GPUFamily4_v2](mtlfeatureset/ios_gpufamily4_v2.md) — The GPU family 4, version 2 feature set for iOS. _(deprecated)_
- [MTLFeatureSet_iOS_GPUFamily4_v1](mtlfeatureset/ios_gpufamily4_v1.md) — The GPU family 4, version 1 feature set for iOS. _(deprecated)_

### iOS GPU family 3

- [MTLFeatureSet_iOS_GPUFamily3_v4](mtlfeatureset/ios_gpufamily3_v4.md) — The GPU family 3, version 4 feature set for iOS. _(deprecated)_
- [MTLFeatureSet_iOS_GPUFamily3_v3](mtlfeatureset/ios_gpufamily3_v3.md) — The GPU family 3, version 3 feature set for iOS. _(deprecated)_
- [MTLFeatureSet_iOS_GPUFamily3_v2](mtlfeatureset/ios_gpufamily3_v2.md) — The GPU family 3, version 2 feature set for iOS. _(deprecated)_
- [MTLFeatureSet_iOS_GPUFamily3_v1](mtlfeatureset/ios_gpufamily3_v1.md) — The GPU family 3, version 1 feature set for iOS. _(deprecated)_

### iOS GPU family 2

- [MTLFeatureSet_iOS_GPUFamily2_v5](mtlfeatureset/ios_gpufamily2_v5.md) — The GPU family 2, version 5 feature set for iOS. _(deprecated)_
- [MTLFeatureSet_iOS_GPUFamily2_v4](mtlfeatureset/ios_gpufamily2_v4.md) — The GPU family 2, version 4 feature set for iOS. _(deprecated)_
- [MTLFeatureSet_iOS_GPUFamily2_v3](mtlfeatureset/ios_gpufamily2_v3.md) — The GPU family 2, version 3 feature set for iOS. _(deprecated)_
- [MTLFeatureSet_iOS_GPUFamily2_v2](mtlfeatureset/ios_gpufamily2_v2.md) — The GPU family 2, version 2 feature set for iOS. _(deprecated)_
- [MTLFeatureSet_iOS_GPUFamily2_v1](mtlfeatureset/ios_gpufamily2_v1.md) — The GPU family 2, version 1 feature set for iOS. _(deprecated)_

### iOS GPU family 1

- [MTLFeatureSet_iOS_GPUFamily1_v5](mtlfeatureset/ios_gpufamily1_v5.md) — The GPU family 1, version 5 feature set for iOS. _(deprecated)_
- [MTLFeatureSet_iOS_GPUFamily1_v4](mtlfeatureset/ios_gpufamily1_v4.md) — The GPU family 1, version 4 feature set for iOS. _(deprecated)_
- [MTLFeatureSet_iOS_GPUFamily1_v3](mtlfeatureset/ios_gpufamily1_v3.md) — The GPU family 1, version 3 feature set for iOS. _(deprecated)_
- [MTLFeatureSet_iOS_GPUFamily1_v2](mtlfeatureset/ios_gpufamily1_v2.md) — The GPU family 1, version 2 feature set for iOS. _(deprecated)_
- [MTLFeatureSet_iOS_GPUFamily1_v1](mtlfeatureset/ios_gpufamily1_v1.md) — The GPU family 1, version 1 feature set for iOS. _(deprecated)_

### tvOS GPU family 2

- [MTLFeatureSet_tvOS_GPUFamily2_v2](mtlfeatureset/tvos_gpufamily2_v2.md) — The GPU family 2, version 2 feature set for tvOS. _(deprecated)_
- [MTLFeatureSet_tvOS_GPUFamily2_v1](mtlfeatureset/tvos_gpufamily2_v1.md) — The GPU family 2, version 1 feature set for tvOS. _(deprecated)_

### tvOS GPU family 1

- [MTLFeatureSet_tvOS_GPUFamily1_v4](mtlfeatureset/tvos_gpufamily1_v4.md) — The GPU family 1, version 4 feature set for tvOS. _(deprecated)_
- [MTLFeatureSet_tvOS_GPUFamily1_v3](mtlfeatureset/tvos_gpufamily1_v3.md) — The GPU family 1, version 3 feature set for tvOS. _(deprecated)_
- [MTLFeatureSet_tvOS_GPUFamily1_v2](mtlfeatureset/tvos_gpufamily1_v2.md) — The GPU family 1, version 2 feature set for tvOS. _(deprecated)_
- [MTLFeatureSet_tvOS_GPUFamily1_v1](mtlfeatureset/tvos_gpufamily1_v1-swift.enum.case.md) — The GPU family 1, version 1 feature set for tvOS. _(deprecated)_

### macOS GPU family 2

- [MTLFeatureSet_macOS_GPUFamily2_v1](mtlfeatureset/macos_gpufamily2_v1.md) — The GPU family 2, version 1 feature set for macOS. _(deprecated)_

### macOS GPU family 1

- [MTLFeatureSet_macOS_GPUFamily1_v4](mtlfeatureset/macos_gpufamily1_v4.md) — The GPU family 1, version 4 feature set for macOS. _(deprecated)_
- [MTLFeatureSet_macOS_GPUFamily1_v3](mtlfeatureset/macos_gpufamily1_v3.md) — The GPU family 1, version 3 feature set for macOS. _(deprecated)_
- [MTLFeatureSet_macOS_GPUFamily1_v2](mtlfeatureset/macos_gpufamily1_v2.md) — The GPU family 1, version 2 feature set for macOS. _(deprecated)_
- [MTLFeatureSet_macOS_GPUFamily1_v1](mtlfeatureset/macos_gpufamily1_v1.md) — The GPU family 1, version 1 feature set for macOS. _(deprecated)_

### macOS tier 2

- [MTLFeatureSet_macOS_ReadWriteTextureTier2](mtlfeatureset/macos_readwritetexturetier2.md) — The read-write texture, tier 2 feature set for macOS. _(deprecated)_

### Initializers

- [init(rawValue:)](<mtlfeatureset/init(rawvalue_).md>) _(deprecated)_

### Type Properties

- [MTLFeatureSet_OSX_GPUFamily1_v1](mtlfeatureset/osx_gpufamily1_v1.md) _(deprecated)_
- [MTLFeatureSet_OSX_GPUFamily1_v2](mtlfeatureset/osx_gpufamily1_v2.md) _(deprecated)_
- [MTLFeatureSet_OSX_ReadWriteTextureTier2](mtlfeatureset/osx_readwritetexturetier2.md) _(deprecated)_
- [MTLFeatureSet_TVOS_GPUFamily1_v1](mtlfeatureset/tvos_gpufamily1_v1-swift.type.property.md) _(deprecated)_

## See Also

### Checking a GPU device’s feature support

- [- supportsFamily:](<mtldevice/supportsfamily(__).md>) — Returns a Boolean value that indicates whether the GPU device supports the feature set of a specific GPU family.
- [MTLGPUFamily](mtlgpufamily.md) — Represents the functionality for families of GPUs.
- [- supportsFeatureSet:](<mtldevice/supportsfeatureset(__).md>) — Returns a Boolean value that indicates whether the GPU device supports a specific feature set. _(deprecated)_
