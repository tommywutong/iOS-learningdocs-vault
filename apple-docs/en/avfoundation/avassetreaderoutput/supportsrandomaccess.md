---
title: supportsRandomAccess
framework: AVFoundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 8.0+（27.0 起废弃）, iPadOS 8.0+（27.0 起废弃）, Mac Catalyst 13.1+（27.0 起废弃）, macOS 10.10+（27.0 起废弃）, tvOS 9.0+（27.0 起废弃）, visionOS 1.0+（27.0 起废弃）]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: /documentation/avfoundation/avassetreaderoutput/supportsrandomaccess
source_url: 'https://developer.apple.com/documentation/avfoundation/avassetreaderoutput/supportsrandomaccess'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avassetreaderoutput/supportsrandomaccess.json'
content_hash: 'sha256:efef7d580e67b23a'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVAssetReaderOutput](../avassetreaderoutput.md)

# supportsRandomAccess

<sub>Instance Property</sub>

A Boolean value that indicates whether the output supports reconfiguring the time ranges it reads.

> [!warning] Deprecated
> Use AVAssetReader.outputProviderWithRandomAccess(for:) instead

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
var supportsRandomAccess: Bool { get set }
```

## Discussion

The default value is [false](../../swift/false.md), which means you can’t reconfigure the output after reading begins. This setting may result in more efficient reading, particularly when you’re using multiple asset reader outputs.

A value of [true](../../swift/true.md) indicates that you can reconfigure the output’s time ranges after reading begins by calling the [- resetForReadingTimeRanges:](<reset(forreadingtimeranges_).md>) method. This setting also prevents the asset reader from progressing to a completed state until you call the [- markConfigurationAsFinal](<markconfigurationasfinal().md>) method.

You can’t set this value after you call [- startReading](<../avassetreader/startreading().md>) on the asset reader.

## See Also

### Configuring reading

- [alwaysCopiesSampleData](alwayscopiessampledata.md) — A Boolean value that indicates whether the output vends copied sample data. _(deprecated)_
- [- resetForReadingTimeRanges:](<reset(forreadingtimeranges_).md>) — Restarts reading with a new set of time ranges. _(deprecated)_
- [- markConfigurationAsFinal](<markconfigurationasfinal().md>) — Tells the output that it’s finished reconfiguring time ranges, and allows the asset reader to advance to a completed state. _(deprecated)_
