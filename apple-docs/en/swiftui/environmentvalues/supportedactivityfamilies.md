---
title: supportedActivityFamilies
framework: SwiftUI
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 18.0+, iPadOS 18.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/environmentvalues/supportedactivityfamilies
source_url: 'https://developer.apple.com/documentation/swiftui/environmentvalues/supportedactivityfamilies'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/environmentvalues/supportedactivityfamilies.json'
content_hash: 'sha256:4e37192fb62979e2'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [EnvironmentValues](../environmentvalues.md)

# supportedActivityFamilies

<sub>Instance Property</sub>

An environment value that that indicates potential rendered family for a Live Activity.

<sub>iOS, iPadOS, Mac Catalyst</sub>

```swift
var supportedActivityFamilies: Set<ActivityFamily> { get set }
```

## Discussion

To detect the currently rendered activity family size, use the [activityFamily](activityfamily.md) environment variable. The `supportedActivityFamilies` environment value might only be useful if your make you make your Live Activity views available in a Swift package.
