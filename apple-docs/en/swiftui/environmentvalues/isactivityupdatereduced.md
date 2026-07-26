---
title: isActivityUpdateReduced
framework: SwiftUI
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 18.0+, iPadOS 18.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/environmentvalues/isactivityupdatereduced
source_url: 'https://developer.apple.com/documentation/swiftui/environmentvalues/isactivityupdatereduced'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/environmentvalues/isactivityupdatereduced.json'
content_hash: 'sha256:58dfd2137734fe8c'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [EnvironmentValues](../environmentvalues.md)

# isActivityUpdateReduced

<sub>Instance Property</sub>

A Boolean value that indicates whether the Live Activity update synchronization rate is reduced.

<sub>iOS, iPadOS, Mac Catalyst</sub>

```swift
var isActivityUpdateReduced: Bool { get set }
```

## Discussion

When rendering an activity on a remote device such as Apple Watch, content updates may sometimes be limited to only alerting updates, depending on system conditions. When a Live Activity is visible and the system synchronizes only alerting updates with a remote device, the value of `isActivityUpdateReduced` is `true`.

For example, `isActivityUpdateReduced` may be `true` for Live Activities on an Apple Watch that’s out of range of the paired iPhone.
