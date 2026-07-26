---
title: 'sequenced(before:)'
framework: SwiftUI
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.0+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/gesture/sequenced(before:)'
source_url: 'https://developer.apple.com/documentation/swiftui/gesture/sequenced(before:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/gesture/sequenced%28before%3A%29.json'
content_hash: 'sha256:3a93ff74ef57d901'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [Gesture](../gesture.md)

# sequenced(before:)

<sub>Instance Method</sub>

Sequences a gesture with another one to create a new gesture, which results in the second gesture only receiving events after the first gesture succeeds.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
@MainActor @preconcurrency func sequenced<Other>(before other: Other) -> SequenceGesture<Self, Other> where Other : Gesture
```

## Parameters

- `other` — A gesture you want to combine with another gesture to create a new, sequenced gesture.

## Return Value

A gesture that’s a sequence of two gestures.

## See Also

### Composing gestures

- [simultaneously(with:)](<simultaneously(with_).md>) — Combines a gesture with another gesture to create a new gesture that recognizes both gestures at the same time.
- [exclusively(before:)](<exclusively(before_).md>) — Combines two gestures exclusively to create a new gesture where only one gesture succeeds, giving precedence to the first gesture.
