---
title: NSFeatureUnsupportedError
framework: Foundation
symbol_kind: case
role: symbol
role_heading: Enumeration Case
platforms: [iOS 6.0+, iPadOS 6.0+, Mac Catalyst 13.1+, macOS 10.8+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/nsfeatureunsupportederror-c.enum.case
source_url: 'https://developer.apple.com/documentation/foundation/nsfeatureunsupportederror-c.enum.case'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsfeatureunsupportederror-c.enum.case.json'
content_hash: 'sha256:b4fdeb71b4b363ce'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Foundation](../foundation.md)

# NSFeatureUnsupportedError

<sub>Enumeration Case</sub>

The feature isn’t supported, because the file system lacks the feature, or required libraries are missing, or other similar reasons.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```objc
NSFeatureUnsupportedError
```

## Discussion

For example, some volumes may not support a Trash folder, so these methods will report failure by returning [false](../swift/false.md) or `nil` and an [NSError](nserror.md) with [NSFeatureUnsupportedError](nsfeatureunsupportederror-swift.var.md).

## See Also

### Miscellaneous Errors

- [NSKeyValueValidationError](nskeyvaluevalidationerror-c.enum.case.md) — A key-value coding validation error.
