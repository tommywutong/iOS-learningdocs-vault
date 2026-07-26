---
title: validateForDelete()
framework: Core Data
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 3.0+, iPadOS 3.0+, Mac Catalyst 13.1+, macOS 10.4+, tvOS, visionOS 1.0+, watchOS 2.0+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/coredata/nsmanagedobject/validatefordelete()
source_url: 'https://developer.apple.com/documentation/coredata/nsmanagedobject/validatefordelete()'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coredata/nsmanagedobject/validatefordelete%28%29.json'
content_hash: 'sha256:9518423414e4da31'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Data](../../coredata.md) · [NSManagedObject](../nsmanagedobject.md)

# validateForDelete()

<sub>Instance Method</sub>

Determines whether the managed object can be deleted in its current state.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func validateForDelete() throws
```

## Discussion

An object cannot be deleted if it has a relationship has a “deny” delete rule and that relationship has a destination object.

`NSManagedObject`‘s implementation sends the receiver’s entity description a message which performs basic checking based on the presence or absence of values.

> [!important] Important
> Subclasses should invoke super’s implementation before performing their own validation, and should combine any error returned by super’s implementation with their own (see Managed Object Validation).

## See Also

### Managing Data Validation

- [- validateValue:forKey:error:](<validatevalue(__forkey_).md>) — Validates a property value for a given key.
- [- validateForInsert:](<validateforinsert().md>) — Determines whether the managed object can be inserted in its current state.
- [- validateForUpdate:](<validateforupdate().md>) — Determines whether the managed object’s current state is valid.
- [Validation error codes](../1535452-validation-error-codes.md) — Error codes relating to the validation of managed objects.
- [NSValidationKeyErrorKey](../nsvalidationkeyerrorkey.md) — The error key for the attribute that failed to validate.
- [NSValidationObjectErrorKey](../nsvalidationobjecterrorkey.md) — The error key for the object that failed to validate.
- [NSValidationPredicateErrorKey](../nsvalidationpredicateerrorkey.md) — The error key for the predicate that failed to validate.
- [NSValidationValueErrorKey](../nsvalidationvalueerrorkey.md) — The error key for the value that failed to validate.
