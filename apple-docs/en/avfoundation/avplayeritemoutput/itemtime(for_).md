---
title: 'itemTime(for:)'
framework: AVFoundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [macOS 10.8+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/avfoundation/avplayeritemoutput/itemtime(for:)'
source_url: 'https://developer.apple.com/documentation/avfoundation/avplayeritemoutput/itemtime(for:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avplayeritemoutput/itemtime%28for%3A%29.json'
content_hash: 'sha256:6adc14621dbe685f'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVPlayerItemOutput](../avplayeritemoutput.md)

# itemTime(for:)

<sub>Instance Method</sub>

Converts a Core Video timestamp to the item’s timebase.

<sub>macOS</sub>

```swift
func itemTime(for timestamp: CVTimeStamp) -> CMTime
```

## Parameters

- `timestamp` — A timestamp value provided by the Core Video framework.

## Return Value

The equivalent time in the item’s timebase.

## See Also

### Time conversion

- [- itemTimeForHostTime:](<itemtime(forhosttime_).md>) — Converts a host time, specified in seconds, to the item’s timebase.
- [- itemTimeForMachAbsoluteTime:](<itemtime(formachabsolutetime_).md>) — Converts a Mach host time to the item’s timebase.
