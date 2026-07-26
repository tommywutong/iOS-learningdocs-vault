---
title: isUserAuthenticationEnabled
framework: SwiftUI
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 18.0+, iPadOS 18.0+, Mac Catalyst 18.0+, macOS 15.0+, tvOS 18.0+, visionOS 2.0+, watchOS 11.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/environmentvalues/isuserauthenticationenabled
source_url: 'https://developer.apple.com/documentation/swiftui/environmentvalues/isuserauthenticationenabled'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/environmentvalues/isuserauthenticationenabled.json'
content_hash: 'sha256:5ced20821ce0bd7a'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [EnvironmentValues](../environmentvalues.md)

# isUserAuthenticationEnabled

<sub>Instance Property</sub>

The current system user authentication enablement status.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var isUserAuthenticationEnabled: Bool { get }
```

## Discussion

Use this value to determine whether the system will issue additional device-owner authentication challenges before revealing this piece of user interface from under a system-installed shield.

Your app can respond to changes in this value to take appropriate action, like installing or uninstalling a bespoke UI shield for sensitive content.
