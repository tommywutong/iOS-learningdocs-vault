---
title: 'textForGuidedAccessRestriction(withIdentifier:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 7.0+, iPadOS 7.0+, Mac Catalyst 13.1+, tvOS, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uiguidedaccessrestrictiondelegate/textforguidedaccessrestriction(withidentifier:)'
source_url: 'https://developer.apple.com/documentation/uikit/uiguidedaccessrestrictiondelegate/textforguidedaccessrestriction(withidentifier:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiguidedaccessrestrictiondelegate/textforguidedaccessrestriction%28withidentifier%3A%29.json'
content_hash: 'sha256:7fcacc7eeadd63cc'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIGuidedAccessRestrictionDelegate](../uiguidedaccessrestrictiondelegate.md)

# textForGuidedAccessRestriction(withIdentifier:)

<sub>Instance Method</sub>

Provides a succinct description of the restriction for the specified identifier.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
func textForGuidedAccessRestriction(withIdentifier restrictionIdentifier: String) -> String?
```

## Parameters

- `restrictionIdentifier` — The identifer of the restriction the system is interested in.

## Return Value

A localized, human-readable string that succinctly describes the restriction for the provided identifier.

## See Also

### Identifying custom Guided Access restrictions

- [guidedAccessRestrictionIdentifiers](guidedaccessrestrictionidentifiers.md) — An array of strings identifying custom restrictions.
- [- detailTextForGuidedAccessRestrictionWithIdentifier:](<detailtextforguidedaccessrestriction(withidentifier_).md>) — Provides more detailed information about the restriction for the specified identifier.
