---
title: 'guidedAccessRestrictionState(forIdentifier:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [iOS 7.0+, iPadOS 7.0+, Mac Catalyst 13.1+, tvOS, visionOS 1.0+]
languages: [swift, swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uiaccessibility/guidedaccessrestrictionstate(foridentifier:)'
source_url: 'https://developer.apple.com/documentation/uikit/uiaccessibility/guidedaccessrestrictionstate(foridentifier:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiaccessibility/guidedaccessrestrictionstate%28foridentifier%3A%29.json'
content_hash: 'sha256:c0526e24e1166f94'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIAccessibility](../uiaccessibility.md)

# guidedAccessRestrictionState(forIdentifier:)

<sub>Type Method</sub>

Returns the restriction state for the specified guided access restriction.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
@MainActor static func guidedAccessRestrictionState(forIdentifier restrictionIdentifier: String) -> UIAccessibility.GuidedAccessRestrictionState
```

## Parameters

- `restrictionIdentifier` — The string that uniquely identifies the guided access restriction.

## Return Value

The current state of the guided access restriction. The initial state of all restrictions is [UIGuidedAccessRestrictionStateAllow](guidedaccessrestrictionstate/allow.md).

## See Also

### Guided Access

- [UIGuidedAccessRestrictionDelegate](../uiguidedaccessrestrictiondelegate.md) — A set of methods you use to add custom restrictions for the Guided Access feature in iOS.
