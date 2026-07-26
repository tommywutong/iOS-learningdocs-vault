---
title: 'end(proposingNewTime:)'
framework: AVFoundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, macOS 12.0+, tvOS 15.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/avfoundation/avcoordinatedplaybacksuspension/end(proposingnewtime:)'
source_url: 'https://developer.apple.com/documentation/avfoundation/avcoordinatedplaybacksuspension/end(proposingnewtime:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avcoordinatedplaybacksuspension/end%28proposingnewtime%3A%29.json'
content_hash: 'sha256:dc083c5496a488b6'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVCoordinatedPlaybackSuspension](../avcoordinatedplaybacksuspension.md)

# end(proposingNewTime:)

<sub>Instance Method</sub>

Ends a suspension and proposes a new playback time to the group.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
func end(proposingNewTime time: CMTime)
```

## Parameters

- `time` — The proposed playback time. Passing a nonnumeric time results in the same behavior as calling the [- end](<end().md>) method.

## Discussion

If this is the last suspension, the coordinator proposes a new time to the group without changing the group’s playback rate. If it isn’t, the coordinator only proposes the new time after all other suspensions end.

A suspension that ends after this one ends can override the proposed time. Similarly, playback commands from the group that arrive after this suspension ends, override a pending proposal.

## See Also

### Ending a suspension

- [- end](<end().md>) — Ends a suspension.
