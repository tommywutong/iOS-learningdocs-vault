---
title: overallDurationHint
framework: AVFoundation
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, macOS 12.0+, tvOS 15.0+, visionOS 1.0+, watchOS 8.0+]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avpartialasyncproperty/overalldurationhint
source_url: 'https://developer.apple.com/documentation/avfoundation/avpartialasyncproperty/overalldurationhint'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avpartialasyncproperty/overalldurationhint.json'
content_hash: 'sha256:c5b7a3bc7db504bc'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVPartialAsyncProperty](../avpartialasyncproperty.md)

# overallDurationHint

<sub>Type Property</sub>

A hint to the total duration of fragments that currently exist or may exist in the future.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
static var overallDurationHint: AVAsyncProperty<Root, CMTime> { get }
```

## Discussion

Use the [load(_:isolation:)](<../avasynchronouskeyvalueloading/load(__isolation_).md>) method to retrieve the property value.

For QuickTime movie files and MPEG-4 files, the system obtains the value of this property from the `mehd` box of the `mvex` box, if present. If no total fragment duration hint is available, the value of this property is [invalid](../../coremedia/cmtime/invalid.md).

## See Also

### Loading fragment support

- [canContainFragments](cancontainfragments.md) — A Boolean value that indicates whether you can extend the asset by fragments.
- [containsFragments](containsfragments.md) — A Boolean value that indicates whether at least one movie fragment extends the asset.
