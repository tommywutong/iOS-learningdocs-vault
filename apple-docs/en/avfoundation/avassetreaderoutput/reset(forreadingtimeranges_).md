---
title: 'reset(forReadingTimeRanges:)'
framework: AVFoundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 8.0+（27.0 起废弃）, iPadOS 8.0+（27.0 起废弃）, Mac Catalyst 13.1+（27.0 起废弃）, macOS 10.10+（27.0 起废弃）, tvOS 9.0+（27.0 起废弃）, visionOS 1.0+（27.0 起废弃）]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: '/documentation/avfoundation/avassetreaderoutput/reset(forreadingtimeranges:)'
source_url: 'https://developer.apple.com/documentation/avfoundation/avassetreaderoutput/reset(forreadingtimeranges:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avassetreaderoutput/reset%28forreadingtimeranges%3A%29.json'
content_hash: 'sha256:26cba333a15d162d'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVAssetReaderOutput](../avassetreaderoutput.md)

# reset(forReadingTimeRanges:)

<sub>Instance Method</sub>

Restarts reading with a new set of time ranges.

> [!warning] Deprecated
> Use RandomAccessController.resetForReading(timeRanges:) instead

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
func reset(forReadingTimeRanges timeRanges: [NSValue])
```

## Parameters

- `timeRanges` — An array of [NSValue](../../foundation/nsvalue.md) objects, each representing a single [CMTimeRange](../../coremedia/cmtimerange.md) structure.

## Discussion

You may only call this method if the value of the [supportsRandomAccess](supportsrandomaccess.md) property is [true](../../swift/true.md). You can’t call it after invoking [- markConfigurationAsFinal](<markconfigurationasfinal().md>).

A typical time to call this method is when performing multi-pass encoding using an instance of [AVAssetWriter](../avassetwriter.md). In this case, call the [- copyNextSampleBuffer](<copynextsamplebuffer().md>) method until it returns `nil`, and then ask the asset writer’s input for a set of time ranges to reencode. You pass the time ranges to this method to prepare the output for the next pass.

The time ranges that you set here override the value of the asset reader’s [timeRange](../avassetreader/timerange.md) property. If the start times of the time range in the array don’t strictly increase, or if two or more time ranges in the array overlap, the system throws an exception. It’s an error to include a time range with a nonnumeric start time or duration, unless the duration is [positiveInfinity](../../coremedia/cmtime/positiveinfinity.md).

If you call this method while the asset reader is in an [AVAssetReaderStatusFailed](../avassetreader/status-swift.enum/failed.md) or [AVAssetReaderStatusCancelled](../avassetreader/status-swift.enum/cancelled.md) state, its [status](../avassetreader/status-swift.property.md) property value doesn’t change, and the result of the next call to [- copyNextSampleBuffer](<copynextsamplebuffer().md>) is `nil`.

If you call this method while there’s still media data to read, the system throws an exception. You can only call it after the asset reader starts reading.

## See Also

### Configuring reading

- [alwaysCopiesSampleData](alwayscopiessampledata.md) — A Boolean value that indicates whether the output vends copied sample data. _(deprecated)_
- [supportsRandomAccess](supportsrandomaccess.md) — A Boolean value that indicates whether the output supports reconfiguring the time ranges it reads. _(deprecated)_
- [- markConfigurationAsFinal](<markconfigurationasfinal().md>) — Tells the output that it’s finished reconfiguring time ranges, and allows the asset reader to advance to a completed state. _(deprecated)_
