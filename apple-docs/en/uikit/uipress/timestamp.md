---
title: timestamp
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 9.0+, iPadOS 9.0+, Mac Catalyst 13.1+, tvOS 9.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uipress/timestamp
source_url: 'https://developer.apple.com/documentation/uikit/uipress/timestamp'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uipress/timestamp.json'
content_hash: 'sha256:a5690b427e924df7'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIPress](../uipress.md)

# timestamp

<sub>Instance Property</sub>

The time when the press occurred or when it was last mutated.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
var timestamp: TimeInterval { get }
```

## Discussion

The value of this property is the time, in seconds, from system startup to the time in which the touch either originated or was last changed. You can store and compare the initial value of this attribute to subsequent timestamp values of a [UIPress](../uipress.md) instance to determine the duration of the press and, if it’s being swiped, the speed of movement. For a definition of the time-since-boot value, see the description of the [ProcessInfo](../../foundation/processinfo.md) class’s [systemUptime](../../foundation/processinfo/systemuptime.md) method.

## See Also

### Getting press attributes

- [key](key.md) — The key pressed or released on a physical keyboard.
- [type](type.md) — The type of the specified press.
- [phase](phase-swift.property.md) — The current press phase of the object.
