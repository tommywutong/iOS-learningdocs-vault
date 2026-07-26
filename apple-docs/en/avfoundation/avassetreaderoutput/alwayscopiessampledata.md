---
title: alwaysCopiesSampleData
framework: AVFoundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 5.0+（27.0 起废弃）, iPadOS 5.0+（27.0 起废弃）, Mac Catalyst 13.1+（27.0 起废弃）, macOS 10.8+（27.0 起废弃）, tvOS 9.0+（27.0 起废弃）, visionOS 1.0+（27.0 起废弃）]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: /documentation/avfoundation/avassetreaderoutput/alwayscopiessampledata
source_url: 'https://developer.apple.com/documentation/avfoundation/avassetreaderoutput/alwayscopiessampledata'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avassetreaderoutput/alwayscopiessampledata.json'
content_hash: 'sha256:f1f3f45c9b158817'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVAssetReaderOutput](../avassetreaderoutput.md)

# alwaysCopiesSampleData

<sub>Instance Property</sub>

A Boolean value that indicates whether the output vends copied sample data.

> [!warning] Deprecated
> It is not necessary to copy the sample data in order to make it safe to use the vended buffer

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
var alwaysCopiesSampleData: Bool { get set }
```

## Discussion

The default value is [true](../../swift/true.md), which indicates that the output always provides copies of sample data to your app. This is the appropriate property value if you intend to modify the sample data it returns.

You can disable the default behavior by setting the value to [false](../../swift/false.md), which causes the output to vend buffers that may not be copies. Your app can reference these buffers, but it can’t modify them because the result of modifying a shared buffer isn’t defined. If you don’t need to modify the sample data, disabling copying may lead to performance improvements.

## See Also

### Configuring reading

- [supportsRandomAccess](supportsrandomaccess.md) — A Boolean value that indicates whether the output supports reconfiguring the time ranges it reads. _(deprecated)_
- [- resetForReadingTimeRanges:](<reset(forreadingtimeranges_).md>) — Restarts reading with a new set of time ranges. _(deprecated)_
- [- markConfigurationAsFinal](<markconfigurationasfinal().md>) — Tells the output that it’s finished reconfiguring time ranges, and allows the asset reader to advance to a completed state. _(deprecated)_
