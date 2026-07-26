---
title: 'guidedAccessRestriction(withIdentifier:didChange:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 7.0+, iPadOS 7.0+, Mac Catalyst 13.1+, tvOS, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uiguidedaccessrestrictiondelegate/guidedaccessrestriction(withidentifier:didchange:)'
source_url: 'https://developer.apple.com/documentation/uikit/uiguidedaccessrestrictiondelegate/guidedaccessrestriction(withidentifier:didchange:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiguidedaccessrestrictiondelegate/guidedaccessrestriction%28withidentifier%3Adidchange%3A%29.json'
content_hash: 'sha256:834a845e04ade7e7'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIGuidedAccessRestrictionDelegate](../uiguidedaccessrestrictiondelegate.md)

# guidedAccessRestriction(withIdentifier:didChange:)

<sub>Instance Method</sub>

Tells the delegate that the restriction associated with the identifier has changed state.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
func guidedAccessRestriction(withIdentifier restrictionIdentifier: String, didChange newRestrictionState: UIAccessibility.GuidedAccessRestrictionState)
```

## Parameters

- `restrictionIdentifier` — The identifier of the restriction whose state has changed.

- `newRestrictionState` — The new state for the restriction.

## Discussion

Your app should adjust its behavior to allow or deny the operation controlled by the specified restriction each time it receives this message.

## See Also

### Implementing restrictions

- [GuidedAccessRestrictionState](../uiaccessibility/guidedaccessrestrictionstate.md) — Constants that describe the state of a restriction, either allow or deny.
