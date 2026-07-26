---
title: 'applyTransform(_:reverse:range:updatedRange:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 9.0+, iPadOS 9.0+, Mac Catalyst 13.1+, macOS 10.11+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ, occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/nsmutablestring/applytransform(_:reverse:range:updatedrange:)'
source_url: 'https://developer.apple.com/documentation/foundation/nsmutablestring/applytransform(_:reverse:range:updatedrange:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsmutablestring/applytransform%28_%3Areverse%3Arange%3Aupdatedrange%3A%29.json'
content_hash: 'sha256:c777d5b9f84461a0'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSMutableString](../nsmutablestring.md)

# applyTransform(_:reverse:range:updatedRange:)

<sub>Instance Method</sub>

Transliterates the receiver by applying a specified ICU string transform.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func applyTransform(_ transform: StringTransform, reverse: Bool, range: NSRange, updatedRange resultingRange: NSRangePointer?) -> Bool
```

## Parameters

- `transform` — The transformation to apply. For a list of possible values, see [String Transformations](../string-transformations.md). If the specified transform does not exist, the receiver is not modified, and this method returns [false](../../swift/false.md).

- `reverse` — Whether an inverse transform should be used. If the specified transform does not have an inverse, the receiver is not modified, and this method returns [false](../../swift/false.md).

- `range` — The range of the string to transform. `range` must not exceed the bounds of the receiver. > [!important] Important > Raises an `NSRangeException` if any part of `aRange` lies beyond the end of the string.

- `resultingRange` — If the transform was successfully applied, upon return contains the range of the transformed string.

## Return Value

[true](../../swift/true.md) if the transform was successfully applied. Otherwise, [false](../../swift/false.md).

## Discussion

In addition to the provided transformation constants, you may use any valid ICU transform ID as defined in the [ICU User Guide](http://userguide.icu-project.org/transforms/general). However, arbitrary ICU transform rules are not supported.

## See Also

### Modifying a String

- [- appendString:](<append(__).md>) — Adds to the end of the receiver the characters of a given string.
- [- deleteCharactersInRange:](<deletecharacters(in_).md>) — Removes from the receiver the characters in a given range.
- [- insertString:atIndex:](<insert(__at_).md>) — Inserts into the receiver the characters of a given string at a given location.
- [- replaceCharactersInRange:withString:](<replacecharacters(in_with_).md>) — Replaces the characters from `range` with those in `aString`.
- [- replaceOccurrencesOfString:withString:options:range:](<replaceoccurrences(of_with_options_range_).md>) — Replaces all occurrences of a given string in a given range with another given string, returning the number of replacements.
- [- setString:](<setstring(__).md>) — Replaces the characters of the receiver with those in a given string.
