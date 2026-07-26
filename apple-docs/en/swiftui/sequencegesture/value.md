---
title: SequenceGesture.Value
framework: SwiftUI
symbol_kind: enum
role: symbol
role_heading: Enumeration
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.0+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/sequencegesture/value
source_url: 'https://developer.apple.com/documentation/swiftui/sequencegesture/value'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/sequencegesture/value.json'
content_hash: 'sha256:cfa07b2825a718f4'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [SequenceGesture](../sequencegesture.md)

# SequenceGesture.Value

<sub>Enumeration</sub>

The value of a sequence gesture that helps to detect whether the first gesture succeeded, so the second gesture can start.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
@frozen enum Value
```

## Relationships

- **Conforms To**: [Equatable](../../swift/equatable.md), [Sendable](../../swift/sendable.md), [SendableMetatype](../../swift/sendablemetatype.md)

## Topics

### Getting gesture values

- [SequenceGesture.Value.first(_:)](<value/first(__).md>) — The first gesture hasn’t ended.
- [SequenceGesture.Value.second(_:_:)](<value/second(____).md>) — The first gesture has ended.
