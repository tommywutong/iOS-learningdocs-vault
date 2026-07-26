---
title: parentFocusEnvironment
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 12.0+, iPadOS 12.0+, Mac Catalyst 13.1+, tvOS 12.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uifocusenvironment/parentfocusenvironment
source_url: 'https://developer.apple.com/documentation/uikit/uifocusenvironment/parentfocusenvironment'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uifocusenvironment/parentfocusenvironment.json'
content_hash: 'sha256:9fa9fbe27018618d'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIFocusEnvironment](../uifocusenvironment.md)

# parentFocusEnvironment

<sub>Instance Property</sub>

The parent focus environment for this environment.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
weak var parentFocusEnvironment: (any UIFocusEnvironment)? { get }
```

## Discussion

The value of this property is `nil` when no parent container exists.

## See Also

### Checking the ancestry of the environment

- [focusItemContainer](focusitemcontainer.md) — The container for the child focus items in this focus environment.
