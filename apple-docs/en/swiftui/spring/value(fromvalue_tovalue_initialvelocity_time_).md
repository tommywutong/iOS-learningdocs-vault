---
title: 'value(fromValue:toValue:initialVelocity:time:)'
framework: SwiftUI
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 17.0+, iPadOS 17.0+, Mac Catalyst 17.0+, macOS 14.0+, tvOS 17.0+, visionOS 1.0+, watchOS 10.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/spring/value(fromvalue:tovalue:initialvelocity:time:)'
source_url: 'https://developer.apple.com/documentation/swiftui/spring/value(fromvalue:tovalue:initialvelocity:time:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/spring/value%28fromvalue%3Atovalue%3Ainitialvelocity%3Atime%3A%29.json'
content_hash: 'sha256:92dc60c70145fcff'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [Spring](../spring.md)

# value(fromValue:toValue:initialVelocity:time:)

<sub>Instance Method</sub>

Calculates the value of the spring at a given time for a starting and ending value for the spring to travel.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func value<V>(fromValue: V, toValue: V, initialVelocity: V, time: TimeInterval) -> V where V : Animatable
```

## See Also

### Getting spring state

- [value(target:initialVelocity:time:)](<value(target_initialvelocity_time_).md>) — Calculates the value of the spring at a given time given a target amount of change.
- [velocity(target:initialVelocity:time:)](<velocity(target_initialvelocity_time_).md>) — Calculates the velocity of the spring at a given time given a target amount of change.
- [velocity(fromValue:toValue:initialVelocity:time:)](<velocity(fromvalue_tovalue_initialvelocity_time_).md>) — Calculates the velocity of the spring at a given time given a starting and ending value for the spring to travel.
