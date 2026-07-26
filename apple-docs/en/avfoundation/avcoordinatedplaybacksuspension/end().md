---
title: end()
framework: AVFoundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, macOS 12.0+, tvOS 15.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avcoordinatedplaybacksuspension/end()
source_url: 'https://developer.apple.com/documentation/avfoundation/avcoordinatedplaybacksuspension/end()'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avcoordinatedplaybacksuspension/end%28%29.json'
content_hash: 'sha256:b9f3423e2a66daa2'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVCoordinatedPlaybackSuspension](../avcoordinatedplaybacksuspension.md)

# end()

<sub>Instance Method</sub>

Ends a suspension.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
func end()
```

## Discussion

If this is the last suspension, the coordinator adjusts the timing of its playback object to match the group.

To end a suspension and simultaneously propose a new playback time to the group, call the [- endProposingNewTime:](<end(proposingnewtime_).md>) method.

## See Also

### Ending a suspension

- [- endProposingNewTime:](<end(proposingnewtime_).md>) — Ends a suspension and proposes a new playback time to the group.
