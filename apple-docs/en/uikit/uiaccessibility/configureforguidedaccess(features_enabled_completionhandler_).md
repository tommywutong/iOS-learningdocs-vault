---
title: 'configureForGuidedAccess(features:enabled:completionHandler:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [iOS 12.2+, iPadOS 12.2+, Mac Catalyst 13.1+, visionOS 1.0+]
languages: [swift, swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uiaccessibility/configureforguidedaccess(features:enabled:completionhandler:)'
source_url: 'https://developer.apple.com/documentation/uikit/uiaccessibility/configureforguidedaccess(features:enabled:completionhandler:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiaccessibility/configureforguidedaccess%28features%3Aenabled%3Acompletionhandler%3A%29.json'
content_hash: 'sha256:b9bbd4a484ca991c'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIAccessibility](../uiaccessibility.md)

# configureForGuidedAccess(features:enabled:completionHandler:)

<sub>Type Method</sub>

Enables or disables the specified accessibility features while using Guided Access.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
@MainActor static func configureForGuidedAccess(features: UIGuidedAccessAccessibilityFeature, enabled: Bool, completionHandler completion: @escaping (Bool, (any Error)?) -> Void)
```

## See Also

### Guided Access

- [UIGuidedAccessAccessibilityFeature](../uiguidedaccessaccessibilityfeature.md) — Constants that describe accessibility features for Guided Access.
- [Code](guidedaccesserror/code.md) — Error codes for Guided Access.
