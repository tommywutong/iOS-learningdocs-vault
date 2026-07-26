---
title: 'exclusively(before:)'
framework: SwiftUI
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.0+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/gesture/exclusively(before:)'
source_url: 'https://developer.apple.com/documentation/swiftui/gesture/exclusively(before:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/gesture/exclusively%28before%3A%29.json'
content_hash: 'sha256:17711a9f33521f90'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [Gesture](../gesture.md)

# exclusively(before:)

<sub>Instance Method</sub>

Combines two gestures exclusively to create a new gesture where only one gesture succeeds, giving precedence to the first gesture.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
nonisolated func exclusively<Other>(before other: Other) -> ExclusiveGesture<Self, Other> where Other : Gesture
```

## Parameters

- `other` — A gesture you combine with your gesture, to create a new, combined gesture.

## Return Value

A gesture that’s the result of combining two gestures where only one of them can succeed. SwiftUI gives precedence to the first gesture.

## See Also

### Composing gestures

- [simultaneously(with:)](<simultaneously(with_).md>) — Combines a gesture with another gesture to create a new gesture that recognizes both gestures at the same time.
- [sequenced(before:)](<sequenced(before_).md>) — Sequences a gesture with another one to create a new gesture, which results in the second gesture only receiving events after the first gesture succeeds.
