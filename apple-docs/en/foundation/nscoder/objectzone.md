---
title: objectZone
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.0+, macOS 10.0+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/nscoder/objectzone
source_url: 'https://developer.apple.com/documentation/foundation/nscoder/objectzone'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nscoder/objectzone.json'
content_hash: 'sha256:e085357096a6f36e'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSCoder](../nscoder.md)

# objectZone

<sub>Instance Method</sub>

This method is present for historical reasons and has no effect.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```objc
- (NSZone *) objectZone;
```

## Discussion

`NSCoder`’s implementation returns the default memory zone, as given by `NSDefaultMallocZone()`.

## See Also

### Managing Zones

- [setObjectZone:](setobjectzone_.md) — This method is present for historical reasons and has no effect.
