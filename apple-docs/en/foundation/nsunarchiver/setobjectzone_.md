---
title: 'setObjectZone:'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [Mac Catalyst 13.1+（13.1 起废弃）, macOS 10.0+（10.13 起废弃）]
languages: [occ]
beta: false
deprecated: true
doc_path: '/documentation/foundation/nsunarchiver/setobjectzone:'
source_url: 'https://developer.apple.com/documentation/foundation/nsunarchiver/setobjectzone:'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsunarchiver/setobjectzone%3A.json'
content_hash: 'sha256:52d792200bc3adc0'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSUnarchiver](../nsunarchiver.md)

# setObjectZone:

<sub>Instance Method</sub>

Sets the memory zone used to allocate decoded objects.

<sub>Mac Catalyst, macOS</sub>

```objc
- (void) setObjectZone:(NSZone *) zone;
```

## Parameters

- `zone` — The memory zone used to allocate decoded objects.

## Discussion

If `zone` is `nil`, or if this method is never invoked, the default zone is used, as given by `NSDefaultMallocZone()`.

## See Also

### Managing an NSUnarchiver

- [atEnd](isatend.md) — A Boolean value that indicates whether the receiver has reached the end of the encoded data while decoding. _(deprecated)_
- [objectZone](objectzone-c.method.md) — Returns the memory zone used to allocate decoded objects. _(deprecated)_
- [systemVersion](systemversion-swift.property.md) — The system version number in effect when the archive was created. _(deprecated)_
