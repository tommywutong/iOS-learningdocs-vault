---
title: allowEvaluation()
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 7.0+, iPadOS 7.0+, Mac Catalyst 13.1+, macOS 10.9+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/nssortdescriptor/allowevaluation()
source_url: 'https://developer.apple.com/documentation/foundation/nssortdescriptor/allowevaluation()'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nssortdescriptor/allowevaluation%28%29.json'
content_hash: 'sha256:2940240729b74f02'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSSortDescriptor](../nssortdescriptor.md)

# allowEvaluation()

<sub>Instance Method</sub>

Forces a securely decoded sort descriptor to allow evaluation.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func allowEvaluation()
```

## Discussion

When securely decoding [NSSortDescriptor](../nssortdescriptor.md) objects that are encoded using [NSSecureCoding](../nssecurecoding.md), evaluation is disabled because it is potentially unsafe to evaluate descriptors you get out of an archive.

Before you enable evaluation, you should validate key paths, selectors, and related properties to ensure no erroneous or malicious code will be executed. Once you’ve preflighted the sort descriptor, you can enable the sort descriptor for evaluation by calling [- allowEvaluation](<allowevaluation().md>).

## See Also

### Using Sort Descriptors

- [- compareObject:toObject:](<compare(__to_).md>) — Returns a comparison result value that indicates the sort order of two objects.
- [reversedSortDescriptor](reversedsortdescriptor.md) — Returns a sort descriptor that reverses the sort order.
