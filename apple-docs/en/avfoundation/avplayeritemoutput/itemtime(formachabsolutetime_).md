---
title: 'itemTime(forMachAbsoluteTime:)'
framework: AVFoundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 6.0+, iPadOS 6.0+, Mac Catalyst 13.1+, macOS 10.8+, tvOS 9.0+, visionOS 1.0+, watchOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/avfoundation/avplayeritemoutput/itemtime(formachabsolutetime:)'
source_url: 'https://developer.apple.com/documentation/avfoundation/avplayeritemoutput/itemtime(formachabsolutetime:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avplayeritemoutput/itemtime%28formachabsolutetime%3A%29.json'
content_hash: 'sha256:ea18335ed9cad2cd'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVPlayerItemOutput](../avplayeritemoutput.md)

# itemTime(forMachAbsoluteTime:)

<sub>Instance Method</sub>

Converts a Mach host time to the item’s timebase.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func itemTime(forMachAbsoluteTime machAbsoluteTime: Int64) -> CMTime
```

## Parameters

- `machAbsoluteTime` — The Mach host time to convert. You typically retrieve this value using the `mach_absolute_time` function.

## Return Value

The equivalent time in the item’s timebase.

## See Also

### Time conversion

- [- itemTimeForHostTime:](<itemtime(forhosttime_).md>) — Converts a host time, specified in seconds, to the item’s timebase.
- [- itemTimeForCVTimeStamp:](<itemtime(for_).md>) — Converts a Core Video timestamp to the item’s timebase.
