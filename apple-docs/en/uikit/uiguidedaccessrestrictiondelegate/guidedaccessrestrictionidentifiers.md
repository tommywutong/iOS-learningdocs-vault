---
title: guidedAccessRestrictionIdentifiers
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 7.0+, iPadOS 7.0+, Mac Catalyst 13.1+, tvOS, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uiguidedaccessrestrictiondelegate/guidedaccessrestrictionidentifiers
source_url: 'https://developer.apple.com/documentation/uikit/uiguidedaccessrestrictiondelegate/guidedaccessrestrictionidentifiers'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiguidedaccessrestrictiondelegate/guidedaccessrestrictionidentifiers.json'
content_hash: 'sha256:b5dba51f773d7418'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIGuidedAccessRestrictionDelegate](../uiguidedaccessrestrictiondelegate.md)

# guidedAccessRestrictionIdentifiers

<sub>Instance Property</sub>

An array of strings identifying custom restrictions.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
var guidedAccessRestrictionIdentifiers: [String]? { get }
```

## Return Value

An array of NSString objects, each of which represents a custom restriction.

## Discussion

Your delegate must implement this method and return an array with an identifier string for each custom guided access restriction you wish to provide in your app.

## See Also

### Identifying custom Guided Access restrictions

- [- textForGuidedAccessRestrictionWithIdentifier:](<textforguidedaccessrestriction(withidentifier_).md>) — Provides a succinct description of the restriction for the specified identifier.
- [- detailTextForGuidedAccessRestrictionWithIdentifier:](<detailtextforguidedaccessrestriction(withidentifier_).md>) — Provides more detailed information about the restriction for the specified identifier.
