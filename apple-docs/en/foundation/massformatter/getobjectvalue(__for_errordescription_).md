---
title: 'getObjectValue(_:for:errorDescription:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.1+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/massformatter/getobjectvalue(_:for:errordescription:)'
source_url: 'https://developer.apple.com/documentation/foundation/massformatter/getobjectvalue(_:for:errordescription:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/massformatter/getobjectvalue%28_%3Afor%3Aerrordescription%3A%29.json'
content_hash: 'sha256:7470b32d4ae8084e'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [MassFormatter](../massformatter.md)

# getObjectValue(_:for:errorDescription:)

<sub>Instance Method</sub>

This method is not supported for the `NSMassFormatter` class.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func getObjectValue(_ obj: AutoreleasingUnsafeMutablePointer<AnyObject?>?, for string: String, errorDescription error: AutoreleasingUnsafeMutablePointer<NSString?>?) -> Bool
```

## Parameters

- `obj` — An output parameter. If overridden, this parameter should contain the object created from the provided string.

- `string` — A string representation of the object.

- `error` — An output parameter. If overridden, this parameter should contain a description of any errors that occur. If you do not want to receive error messages, set this parameter to `NULL`.

## Return Value

[true](../../swift/true.md) if the conversion from string was successful; otherwise, [false](../../swift/false.md).

## Discussion

You can override this method in a subclass. For more information, see [Formatter](../formatter.md).

## See Also

### Related Documentation

- [- getObjectValue:forString:errorDescription:](<../formatter/getobjectvalue(__for_errordescription_).md>) — The default implementation of this method raises an exception.

### Formatting Mass Strings

- [forPersonMassUse](isforpersonmassuse.md) — A Boolean value that indicates whether the resulting string represents a person’s mass.
- [numberFormatter](numberformatter.md) — The number formatter used to format the numbers in a mass strings.
- [- stringFromKilograms:](<string(fromkilograms_).md>) — Returns a mass string for the provided value.
- [- stringFromValue:unit:](<string(fromvalue_unit_).md>) — Returns a properly formatted mass string for the given value and unit.
- [- unitStringFromKilograms:usedUnit:](<unitstring(fromkilograms_usedunit_).md>) — Returns the unit string for the provided value.
- [- unitStringFromValue:unit:](<unitstring(fromvalue_unit_).md>) — Returns the unit string based on the provided value and unit.
- [unitStyle](unitstyle.md) — The unit style used by this formatter.
