---
title: 'applyingTransform(_:reverse:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 9.0+, iPadOS 9.0+, Mac Catalyst 13.1+, macOS 10.11+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ, occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/nsstring/applyingtransform(_:reverse:)'
source_url: 'https://developer.apple.com/documentation/foundation/nsstring/applyingtransform(_:reverse:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsstring/applyingtransform%28_%3Areverse%3A%29.json'
content_hash: 'sha256:b64f0f719460ed1d'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSString](../nsstring.md)

# applyingTransform(_:reverse:)

<sub>Instance Method</sub>

Returns a new string by applying a specified transform to the string.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func applyingTransform(_ transform: StringTransform, reverse: Bool) -> String?
```

## Discussion

You can use this method to, for example, transliterate text from one script to another, strip diacritics or combining marks, and get the unicode names of characters.

> [!note] Note
> The constants defined by the [StringTransform](../stringtransform.md) type offer a subset of the functionality provided by the underlying ICU transform functionality. To apply an ICU transform defined in the [ICU User Guide](http://userguide.icu-project.org/transforms/general) that doesn’t have a corresponding [StringTransform](../stringtransform.md) constant, create an instance of  [NSMutableString](../nsmutablestring.md) and call the [- applyTransform:reverse:range:updatedRange:](<../nsmutablestring/applytransform(__reverse_range_updatedrange_).md>) method instead.

.

## See Also

### Related Documentation

- [- applyTransform:reverse:range:updatedRange:](<../nsmutablestring/applytransform(__reverse_range_updatedrange_).md>) — Transliterates the receiver by applying a specified ICU string transform.

### Transforming Strings

- [StringTransform](../stringtransform.md) — Constants representing an ICU string transform.
