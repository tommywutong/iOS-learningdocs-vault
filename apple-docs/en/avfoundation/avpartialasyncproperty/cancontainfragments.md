---
title: canContainFragments
framework: AVFoundation
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, macOS 12.0+, tvOS 15.0+, visionOS 1.0+]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avpartialasyncproperty/cancontainfragments
source_url: 'https://developer.apple.com/documentation/avfoundation/avpartialasyncproperty/cancontainfragments'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avpartialasyncproperty/cancontainfragments.json'
content_hash: 'sha256:60fd3f8f0536a94b'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVPartialAsyncProperty](../avpartialasyncproperty.md)

# canContainFragments

<sub>Type Property</sub>

A Boolean value that indicates whether you can extend the asset by fragments.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
static var canContainFragments: AVAsyncProperty<Root, Bool> { get }
```

## Discussion

Use the [load(_:isolation:)](<../avasynchronouskeyvalueloading/load(__isolation_).md>) method to retrieve the property value.

For QuickTime movie files and MPEG-4 files, the value is [true](../../swift/true.md) if an `mvex` box is present in the `moov` box. For those types, the `mvex` box signals the possible presence of later `moof` boxes.

## See Also

### Loading fragment support

- [containsFragments](containsfragments.md) — A Boolean value that indicates whether at least one movie fragment extends the asset.
- [overallDurationHint](overalldurationhint.md) — A hint to the total duration of fragments that currently exist or may exist in the future.
