---
title: 'init(_:duration:startVelocity:endVelocity:)'
framework: SwiftUI
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 17.0+, iPadOS 17.0+, Mac Catalyst 17.0+, macOS 14.0+, tvOS 17.0+, visionOS 1.0+, watchOS 10.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/cubickeyframe/init(_:duration:startvelocity:endvelocity:)'
source_url: 'https://developer.apple.com/documentation/swiftui/cubickeyframe/init(_:duration:startvelocity:endvelocity:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/cubickeyframe/init%28_%3Aduration%3Astartvelocity%3Aendvelocity%3A%29.json'
content_hash: 'sha256:a55c89de8fd96e29'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [CubicKeyframe](../cubickeyframe.md)

# init(_:duration:startVelocity:endVelocity:)

<sub>Initializer</sub>

Creates a new keyframe using the given value and timestamp.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
init(_ to: Value, duration: TimeInterval, startVelocity: Value? = nil, endVelocity: Value? = nil)
```

## Parameters

- `to` — The value of the keyframe.

- `duration` — The duration of the segment defined by this keyframe.

- `startVelocity` — The velocity of the value at the beginning of the segment, or `nil` to automatically compute the velocity to maintain smooth motion.

- `endVelocity` — The velocity of the value at the end of the segment, or `nil` to automatically compute the velocity to maintain smooth motion.
