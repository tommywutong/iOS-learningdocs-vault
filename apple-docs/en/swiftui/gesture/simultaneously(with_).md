---
title: 'simultaneously(with:)'
framework: SwiftUI
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.0+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/gesture/simultaneously(with:)'
source_url: 'https://developer.apple.com/documentation/swiftui/gesture/simultaneously(with:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/gesture/simultaneously%28with%3A%29.json'
content_hash: 'sha256:1994df1d7a88d464'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [Gesture](../gesture.md)

# simultaneously(with:)

<sub>Instance Method</sub>

Combines a gesture with another gesture to create a new gesture that recognizes both gestures at the same time.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
nonisolated func simultaneously<Other>(with other: Other) -> SimultaneousGesture<Self, Other> where Other : Gesture
```

## Parameters

- `other` — A gesture that you want to combine with your gesture to create a new, combined gesture.

## Return Value

A gesture with two simultaneous gestures.

## See Also

### Composing gestures

- [sequenced(before:)](<sequenced(before_).md>) — Sequences a gesture with another one to create a new gesture, which results in the second gesture only receiving events after the first gesture succeeds.
- [exclusively(before:)](<exclusively(before_).md>) — Combines two gestures exclusively to create a new gesture where only one gesture succeeds, giving precedence to the first gesture.
