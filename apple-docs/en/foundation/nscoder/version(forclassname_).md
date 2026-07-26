---
title: 'version(forClassName:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.0+, macOS 10.0+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/nscoder/version(forclassname:)'
source_url: 'https://developer.apple.com/documentation/foundation/nscoder/version(forclassname:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nscoder/version%28forclassname%3A%29.json'
content_hash: 'sha256:681d6e7f121c4610'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSCoder](../nscoder.md)

# version(forClassName:)

<sub>Instance Method</sub>

This method is present for historical reasons and is not used with keyed archivers.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func version(forClassName className: String) -> Int
```

## Return Value

The version in effect for the class named `className` or `NSNotFound` if no class named `className` exists.

## Discussion

The version number does apply not to `NSKeyedArchiver`/`NSKeyedUnarchiver`.  A keyed archiver does not encode class version numbers.

## See Also

### Getting Version Information

- [systemVersion](systemversion.md) — The system version in effect for the archive.
