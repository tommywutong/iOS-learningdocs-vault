---
title: containsFragments
framework: AVFoundation
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, macOS 12.0+, tvOS 15.0+, visionOS 1.0+]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avpartialasyncproperty/containsfragments
source_url: 'https://developer.apple.com/documentation/avfoundation/avpartialasyncproperty/containsfragments'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avpartialasyncproperty/containsfragments.json'
content_hash: 'sha256:64ce848800b8b7cf'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVPartialAsyncProperty](../avpartialasyncproperty.md)

# containsFragments

<sub>Type Property</sub>

A Boolean value that indicates whether at least one movie fragment extends the asset.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
static var containsFragments: AVAsyncProperty<Root, Bool> { get }
```

## Discussion

Use the [load(_:isolation:)](<../avasynchronouskeyvalueloading/load(__isolation_).md>) method to retrieve the property value.

For QuickTime movie files and MPEG-4 files, the value of this property is [true](../../swift/true.md) if [canContainFragments](../avasset/cancontainfragments.md) is [true](../../swift/true.md) and at least one `moof` box is present after the `moov` box.

## See Also

### Loading fragment support

- [canContainFragments](cancontainfragments.md) — A Boolean value that indicates whether you can extend the asset by fragments.
- [overallDurationHint](overalldurationhint.md) — A hint to the total duration of fragments that currently exist or may exist in the future.
