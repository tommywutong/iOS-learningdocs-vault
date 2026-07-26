---
title: currentDate()
framework: AVFoundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avplayeritem/currentdate()
source_url: 'https://developer.apple.com/documentation/avfoundation/avplayeritem/currentdate()'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avplayeritem/currentdate%28%29.json'
content_hash: 'sha256:98c02a50925b8626'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVPlayerItem](../avplayeritem.md)

# currentDate()

<sub>Instance Method</sub>

Returns the current time of the item as a date.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
nonisolated func currentDate() -> Date?
```

## Return Value

The current time of the item as a date, or `nil` if there isn’t a mapped date for the item.

## Discussion

The system calculates this value from the `EXT-X-PROGRAM-DATE-TIME` tag.

## See Also

### Accessing timing information

- [- currentTime](<currenttime().md>) — Returns the current time of the item.
- [duration](duration.md) — The duration of the item.
- [timebase](timebase.md) — The timebase information for the item.
