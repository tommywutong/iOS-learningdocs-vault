---
title: old
framework: Foundation
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.0+, macOS 10.0+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/nskeyvalueobservingoptions/old
source_url: 'https://developer.apple.com/documentation/foundation/nskeyvalueobservingoptions/old'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nskeyvalueobservingoptions/old.json'
content_hash: 'sha256:35df9271b23e0e8f'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSKeyValueObservingOptions](../nskeyvalueobservingoptions.md)

# old

<sub>Type Property</sub>

Indicates that the change dictionary should contain the old attribute value, if applicable.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
static var old: NSKeyValueObservingOptions { get }
```

## See Also

### Constants

- [NSKeyValueObservingOptionNew](new.md) — Indicates that the change dictionary should provide the new attribute value, if applicable.
- [NSKeyValueObservingOptionInitial](initial.md) — If specified, a notification should be sent to the observer immediately, before the observer registration method even returns.
- [NSKeyValueObservingOptionPrior](prior.md) — Whether separate notifications should be sent to the observer before and after each change, instead of a single notification after the change.
