---
title: 'step(byPresentationTime:wasPinned:)'
framework: AVFoundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, macOS 10.10+, tvOS 16.0+, visionOS 1.0+, watchOS 9.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/avfoundation/avsamplecursor/step(bypresentationtime:waspinned:)'
source_url: 'https://developer.apple.com/documentation/avfoundation/avsamplecursor/step(bypresentationtime:waspinned:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avsamplecursor/step%28bypresentationtime%3Awaspinned%3A%29.json'
content_hash: 'sha256:ba56a3d2af890f11'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVSampleCursor](../avsamplecursor.md)

# step(byPresentationTime:wasPinned:)

<sub>Instance Method</sub>

Moves the cursor by a given delta time on the presentation timeline.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func step(byPresentationTime deltaPresentationTime: CMTime, wasPinned outWasPinned: UnsafeMutablePointer<ObjCBool>?) -> CMTime
```

## Parameters

- `deltaPresentationTime` — The amount of time to move in the presentation timeline.

- `outWasPinned` — The system sets the value of this pointer to [true](../../swift/true.md) if the cursor reaches the beginning or the end of the sample sequence before it reaches the requested time. You may specify `nil` if you’re not interested in this information.

## Return Value

The amount of time the cursor was moved along the presentation timeline. Because sample cursors snap to sample boundaries when stepped, this value may not be equal to the specified time delta even if the cursor was not pinned.

## See Also

### Navigating samples

- [- stepByDecodeTime:wasPinned:](<step(bydecodetime_waspinned_).md>) — Moves the cursor by a given delta time on the decode timeline.
- [- stepInDecodeOrderByCount:](<stepindecodeorder(bycount_).md>) — Moves the cursor a given number of samples in decode order.
- [- stepInPresentationOrderByCount:](<stepinpresentationorder(bycount_).md>) — Moves the cursor a given number of samples in presentation order.
