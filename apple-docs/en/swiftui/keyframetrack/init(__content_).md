---
title: 'init(_:content:)'
framework: SwiftUI
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 17.0+, iPadOS 17.0+, Mac Catalyst 17.0+, macOS 14.0+, tvOS 17.0+, visionOS 1.0+, watchOS 10.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/keyframetrack/init(_:content:)'
source_url: 'https://developer.apple.com/documentation/swiftui/keyframetrack/init(_:content:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/keyframetrack/init%28_%3Acontent%3A%29.json'
content_hash: 'sha256:452ee4352bb6d8e3'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [KeyframeTrack](../keyframetrack.md)

# init(_:content:)

<sub>Initializer</sub>

Creates an instance that animates the property of the root value at the given key path.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
init(_ keyPath: WritableKeyPath<Root, Value>, @KeyframeTrackContentBuilder<Value> content: () -> Content)
```

## Parameters

- `keyPath` — The property to animate.

## See Also

### Creating a keyframe track

- [init(content:)](<init(content_).md>) — Creates an instance that animates the entire value from the root of the key path.
