---
title: 'stepInPresentationOrder(byCount:)'
framework: AVFoundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, macOS 10.10+, tvOS 16.0+, visionOS 1.0+, watchOS 9.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/avfoundation/avsamplecursor/stepinpresentationorder(bycount:)'
source_url: 'https://developer.apple.com/documentation/avfoundation/avsamplecursor/stepinpresentationorder(bycount:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avsamplecursor/stepinpresentationorder%28bycount%3A%29.json'
content_hash: 'sha256:36b1ca7d146d84fd'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVSampleCursor](../avsamplecursor.md)

# stepInPresentationOrder(byCount:)

<sub>Instance Method</sub>

Moves the cursor a given number of samples in presentation order.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func stepInPresentationOrder(byCount stepCount: Int64) -> Int64
```

## Parameters

- `stepCount` — The number of samples to move across. If positive, step forward this many samples. If negative, step backward this many samples.

## Return Value

The number of samples the cursor traversed. If the cursor reaches the beginning or the end of the sample sequence before the requested number of samples was traversed, the absolute value of the result will be less than the absolute value of the specified step count.

## See Also

### Navigating samples

- [- stepByDecodeTime:wasPinned:](<step(bydecodetime_waspinned_).md>) — Moves the cursor by a given delta time on the decode timeline.
- [- stepByPresentationTime:wasPinned:](<step(bypresentationtime_waspinned_).md>) — Moves the cursor by a given delta time on the presentation timeline.
- [- stepInDecodeOrderByCount:](<stepindecodeorder(bycount_).md>) — Moves the cursor a given number of samples in decode order.
