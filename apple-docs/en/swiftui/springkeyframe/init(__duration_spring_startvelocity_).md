---
title: 'init(_:duration:spring:startVelocity:)'
framework: SwiftUI
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 17.0+, iPadOS 17.0+, Mac Catalyst 17.0+, macOS 14.0+, tvOS 17.0+, visionOS 1.0+, watchOS 10.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/springkeyframe/init(_:duration:spring:startvelocity:)'
source_url: 'https://developer.apple.com/documentation/swiftui/springkeyframe/init(_:duration:spring:startvelocity:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/springkeyframe/init%28_%3Aduration%3Aspring%3Astartvelocity%3A%29.json'
content_hash: 'sha256:f5675b20c69c6b68'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [SpringKeyframe](../springkeyframe.md)

# init(_:duration:spring:startVelocity:)

<sub>Initializer</sub>

Creates a new keyframe using the given value and timestamp.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
init(_ to: Value, duration: TimeInterval? = nil, spring: Spring = Spring(), startVelocity: Value? = nil)
```

## Parameters

- `to` — The value of the keyframe.

- `duration` — The duration of the segment defined by this keyframe, or nil to use the settling duration of the spring.

- `spring` — The spring that defines the shape of the segment befire this keyframe

- `startVelocity` — The velocity of the value at the start of the segment, or `nil` to automatically compute the velocity to maintain smooth motion.
