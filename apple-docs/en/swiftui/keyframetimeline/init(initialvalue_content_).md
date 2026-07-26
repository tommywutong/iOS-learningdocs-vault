---
title: 'init(initialValue:content:)'
framework: SwiftUI
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 17.0+, iPadOS 17.0+, Mac Catalyst 17.0+, macOS 14.0+, tvOS 17.0+, visionOS 1.0+, watchOS 10.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/keyframetimeline/init(initialvalue:content:)'
source_url: 'https://developer.apple.com/documentation/swiftui/keyframetimeline/init(initialvalue:content:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/keyframetimeline/init%28initialvalue%3Acontent%3A%29.json'
content_hash: 'sha256:5ba9267935619499'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [KeyframeTimeline](../keyframetimeline.md)

# init(initialValue:content:)

<sub>Initializer</sub>

Creates a new instance using the initial value and content that you provide.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
init(initialValue: Value, @KeyframesBuilder<Value> content: () -> some Keyframes<Value>)
```
