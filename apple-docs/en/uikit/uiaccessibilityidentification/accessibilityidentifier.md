---
title: accessibilityIdentifier
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 5.0+, iPadOS 5.0+, Mac Catalyst 13.1+, tvOS, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uiaccessibilityidentification/accessibilityidentifier
source_url: 'https://developer.apple.com/documentation/uikit/uiaccessibilityidentification/accessibilityidentifier'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiaccessibilityidentification/accessibilityidentifier.json'
content_hash: 'sha256:cd844630f2e07408'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIAccessibilityIdentification](../uiaccessibilityidentification.md)

# accessibilityIdentifier

<sub>Instance Property</sub>

A string that identifies the element.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
@MainActor var accessibilityIdentifier: String? { get set }
```

## Discussion

An identifier can be used to uniquely identify an element in the scripts you write using the UI Automation interfaces. Using an identifier allows you to avoid inappropriately setting or accessing an element’s accessibility label.
