---
title: 'subscript(dynamicMember:)'
framework: SwiftUI
symbol_kind: subscript
role: symbol
role_heading: Instance Subscript
platforms: [iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, macOS 13.0+, tvOS 16.0+, visionOS 1.0+, watchOS 9.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/presentationdetent/context/subscript(dynamicmember:)'
source_url: 'https://developer.apple.com/documentation/swiftui/presentationdetent/context/subscript(dynamicmember:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/presentationdetent/context/subscript%28dynamicmember%3A%29.json'
content_hash: 'sha256:dc652282ec03955c'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [SwiftUI](../../../swiftui.md) · [PresentationDetent](../../presentationdetent.md) · [Context](../context.md)

# subscript(dynamicMember:)

<sub>Instance Subscript</sub>

Returns the value specified by the keyPath from the environment.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
subscript<T>(dynamicMember keyPath: KeyPath<EnvironmentValues, T>) -> T { get }
```

## Overview

This uses the environment from where the sheet is shown, not the environment where the presentation modifier is applied.
