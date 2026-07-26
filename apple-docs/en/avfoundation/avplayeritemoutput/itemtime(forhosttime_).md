---
title: 'itemTime(forHostTime:)'
framework: AVFoundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 6.0+, iPadOS 6.0+, Mac Catalyst 13.1+, macOS 10.8+, tvOS 9.0+, visionOS 1.0+, watchOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/avfoundation/avplayeritemoutput/itemtime(forhosttime:)'
source_url: 'https://developer.apple.com/documentation/avfoundation/avplayeritemoutput/itemtime(forhosttime:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avplayeritemoutput/itemtime%28forhosttime%3A%29.json'
content_hash: 'sha256:f4f9c8e487b2c69b'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVPlayerItemOutput](../avplayeritemoutput.md)

# itemTime(forHostTime:)

<sub>Instance Method</sub>

Converts a host time, specified in seconds, to the item’s timebase.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func itemTime(forHostTime hostTimeInSeconds: CFTimeInterval) -> CMTime
```

## Parameters

- `hostTimeInSeconds` — A host time value, specified in seconds. For example, you might specify the time value returned by the [CACurrentMediaTime()](<../../quartzcore/cacurrentmediatime().md>) function or the timestamp from a [CADisplayLink](../../quartzcore/cadisplaylink.md) object for this parameter.

## Return Value

The equivalent time in the item’s timebase.

## Discussion

The timestamp associated with a [CADisplayLink](../../quartzcore/cadisplaylink.md) object represents the time of the most recent screen refresh, which is usually a time in the past. If you want to find the time associated with the next screen refresh, you need to increment the timestamp by the value in the display link’s `duration` property.

## See Also

### Time conversion

- [- itemTimeForMachAbsoluteTime:](<itemtime(formachabsolutetime_).md>) — Converts a Mach host time to the item’s timebase.
- [- itemTimeForCVTimeStamp:](<itemtime(for_).md>) — Converts a Core Video timestamp to the item’s timebase.
