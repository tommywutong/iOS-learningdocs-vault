---
title: 'propertyForKeyIfAvailable:'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [macOS 10.0+（10.4 起废弃）]
languages: [occ]
beta: false
deprecated: true
doc_path: '/documentation/foundation/nsurlhandle/propertyforkeyifavailable:'
source_url: 'https://developer.apple.com/documentation/foundation/nsurlhandle/propertyforkeyifavailable:'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsurlhandle/propertyforkeyifavailable%3A.json'
content_hash: 'sha256:38bca98c10bed242'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSURLHandle](../nsurlhandle.md)

# propertyForKeyIfAvailable:

<sub>Instance Method</sub>

Returns the property for the specified key only if the value is already available; that is, the client doesn’t need to do any work.

> [!warning] Deprecated
> Use [NSURLConnection](../nsurlconnection.md) or [NSURLDownload](../nsurldownload.md) instead; see [URL Loading System](../url-loading-system.md).

<sub>Mac Catalyst, macOS</sub>

```objc
- (id) propertyForKeyIfAvailable:(NSString *) propertyKey;
```

## Parameters

- `propertyKey` — The key of the desired property.

## Return Value

The value associated with `propertyKey`. Returns `nil` if there is no such key or if the client would have to do work to fetch the property.

## See Also

### Setting and getting resource properties

- [propertyForKey:](propertyforkey_.md) — Returns the property for the specified key. _(deprecated)_
- [writeProperty:forKey:](writeproperty_forkey_.md) — Sets the property of the receiver’s resource for a specified key to the specified value. _(deprecated)_
