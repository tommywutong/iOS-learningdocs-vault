---
title: AVSampleBufferRequest.Mode.opportunistic
framework: AVFoundation
symbol_kind: case
role: symbol
role_heading: Case
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avsamplebufferrequest/mode-swift.enum/opportunistic
source_url: 'https://developer.apple.com/documentation/avfoundation/avsamplebufferrequest/mode-swift.enum/opportunistic'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avsamplebufferrequest/mode-swift.enum/opportunistic.json'
content_hash: 'sha256:66238553270a6a08'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [AVFoundation](../../../avfoundation.md) · [AVSampleBufferRequest](../../avsamplebufferrequest.md) · [Mode](../mode-swift.enum.md)

# AVSampleBufferRequest.Mode.opportunistic

<sub>Case</sub>

A mode that indicates that opportunistic sample buffer creation requests load data as soon as possible.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
case opportunistic
```

## Discussion

In situations with multiple competing requests, a sample buffer generator may defer an opportunistic request in favor of another immediate request, or a scheduled requests with a presentation time close to the timebase time.

> [!important] Important
> The system may postpone an opportunistic request indefinitely. Don’t use this mode for time-sensitive processing.

## See Also

### Mode scheduling

- [AVSampleBufferRequestModeImmediate](immediate.md) — A mode that indicates that sample buffer creation requests load data as soon as possible.
- [AVSampleBufferRequestModeScheduled](scheduled.md) — A mode that indicates that sample buffer creation requests load data according to a scheduled deadline.
