---
title: objectZone
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [Mac Catalyst 13.1+（13.1 起废弃）, macOS 10.0+（10.13 起废弃）]
languages: [occ]
beta: false
deprecated: true
doc_path: /documentation/foundation/nsunarchiver/objectzone-c.method
source_url: 'https://developer.apple.com/documentation/foundation/nsunarchiver/objectzone-c.method'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsunarchiver/objectzone-c.method.json'
content_hash: 'sha256:dd04e621614c0bd5'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSUnarchiver](../nsunarchiver.md)

# objectZone

<sub>Instance Method</sub>

Returns the memory zone used to allocate decoded objects.

<sub>Mac Catalyst, macOS</sub>

```objc
- (NSZone *) objectZone;
```

## Return Value

The memory zone used to allocate decoded objects.

## See Also

### Managing an NSUnarchiver

- [atEnd](isatend.md) — A Boolean value that indicates whether the receiver has reached the end of the encoded data while decoding. _(deprecated)_
- [setObjectZone:](setobjectzone_.md) — Sets the memory zone used to allocate decoded objects. _(deprecated)_
- [systemVersion](systemversion-swift.property.md) — The system version number in effect when the archive was created. _(deprecated)_
