---
title: 'copy(with:)'
framework: AVFoundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 4.0+, iPadOS 4.0+, Mac Catalyst 13.1+, macOS 10.7+, tvOS 9.0+, visionOS 1.0+, watchOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/avfoundation/avplayeritem/copy(with:)'
source_url: 'https://developer.apple.com/documentation/avfoundation/avplayeritem/copy(with:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avplayeritem/copy%28with%3A%29.json'
content_hash: 'sha256:31bed233ea185487'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVPlayerItem](../avplayeritem.md)

# copy(with:)

<sub>Instance Method</sub>

Creates a copy of the object with the specified zone.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
nonisolated func copy(with zone: NSZone? = nil) -> Any
```

## Parameters

- `zone` — The system ignores this parameter.

## Return Value

A copy of the original asset instance.

## See Also

### Copying an player item

- [- copy](<copy().md>) — Creates a copy of the object.
