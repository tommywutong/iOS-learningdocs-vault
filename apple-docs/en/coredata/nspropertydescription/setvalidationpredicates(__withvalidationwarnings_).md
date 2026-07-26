---
title: 'setValidationPredicates(_:withValidationWarnings:)'
framework: Core Data
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 3.0+, iPadOS 3.0+, Mac Catalyst 13.1+, macOS 10.4+, tvOS, visionOS 1.0+, watchOS 2.0+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: '/documentation/coredata/nspropertydescription/setvalidationpredicates(_:withvalidationwarnings:)'
source_url: 'https://developer.apple.com/documentation/coredata/nspropertydescription/setvalidationpredicates(_:withvalidationwarnings:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coredata/nspropertydescription/setvalidationpredicates%28_%3Awithvalidationwarnings%3A%29.json'
content_hash: 'sha256:6a2d658654403cb0'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Data](../../coredata.md) · [NSPropertyDescription](../nspropertydescription.md)

# setValidationPredicates(_:withValidationWarnings:)

<sub>Instance Method</sub>

Sets the validation predicates and warnings of the receiver.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func setValidationPredicates(_ validationPredicates: [NSPredicate]?, withValidationWarnings validationWarnings: [String]?)
```

## Parameters

- `validationPredicates` — An array containing the validation predicates for the receiver.

- `validationWarnings` — An array containing the validation warnings for the receiver.

## Discussion

The `validationPredicates` and `validationWarnings` arrays should contain the same number of elements, and corresponding elements should appear at the same index in each array.

Instead of implementing individual validation methods, you can use this method to provide a list of predicates that are evaluated against the managed objects and a list of corresponding error messages (which can be localized).

### Special Considerations

This method raises an exception if the receiver’s model has been used by an object graph manager.

## See Also

### Supporting Validation

- [validationPredicates](validationpredicates.md) — The validation predicates of the receiver.
- [validationWarnings](validationwarnings.md) — The error strings associated with the receiver’s validation predicates.
