---
title: queryTimestampFrequency()
framework: Metal
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 26.0+, iPadOS 26.0+, Mac Catalyst 26.0+, macOS 26.0+, tvOS 26.0+, visionOS 26.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/metal/mtldevice/querytimestampfrequency()
source_url: 'https://developer.apple.com/documentation/metal/mtldevice/querytimestampfrequency()'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtldevice/querytimestampfrequency%28%29.json'
content_hash: 'sha256:83f7f840cfb0b7bf'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTLDevice](../mtldevice.md)

# queryTimestampFrequency()

<sub>Instance Method</sub>

Queries the frequency of the GPU timestamp in ticks per second.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
func queryTimestampFrequency() -> UInt64
```

## Return Value

The frequency of the GPU timestamp in ticks per second.
