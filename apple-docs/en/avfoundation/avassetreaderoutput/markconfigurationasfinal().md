---
title: markConfigurationAsFinal()
framework: AVFoundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 8.0+（27.0 起废弃）, iPadOS 8.0+（27.0 起废弃）, Mac Catalyst 13.1+（27.0 起废弃）, macOS 10.10+（27.0 起废弃）, tvOS 9.0+（27.0 起废弃）, visionOS 1.0+（27.0 起废弃）]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: /documentation/avfoundation/avassetreaderoutput/markconfigurationasfinal()
source_url: 'https://developer.apple.com/documentation/avfoundation/avassetreaderoutput/markconfigurationasfinal()'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avassetreaderoutput/markconfigurationasfinal%28%29.json'
content_hash: 'sha256:22f84183893c6246'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVAssetReaderOutput](../avassetreaderoutput.md)

# markConfigurationAsFinal()

<sub>Instance Method</sub>

Tells the output that it’s finished reconfiguring time ranges, and allows the asset reader to advance to a completed state.

> [!warning] Deprecated
> Use RandomAccessController.markConfigurationAsFinal() instead

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
func markConfigurationAsFinal()
```

## Discussion

When the value of the [supportsRandomAccess](supportsrandomaccess.md) property is [true](../../swift/true.md), the asset reader doesn’t advance to an [AVAssetReaderStatusCompleted](../avassetreader/status-swift.enum/completed.md) state until you call this method.

After you call this method, you can’t make further calls to the [- resetForReadingTimeRanges:](<reset(forreadingtimeranges_).md>) method.

When the destination of the output’s media data is an [AVAssetWriterInput](../avassetwriterinput.md) that you configure for multi-pass encoding, an appropriate time to call this method is after the asset writer input indicates that it doesn’t require performing additional passes.

## See Also

### Configuring reading

- [alwaysCopiesSampleData](alwayscopiessampledata.md) — A Boolean value that indicates whether the output vends copied sample data. _(deprecated)_
- [supportsRandomAccess](supportsrandomaccess.md) — A Boolean value that indicates whether the output supports reconfiguring the time ranges it reads. _(deprecated)_
- [- resetForReadingTimeRanges:](<reset(forreadingtimeranges_).md>) — Restarts reading with a new set of time ranges. _(deprecated)_
