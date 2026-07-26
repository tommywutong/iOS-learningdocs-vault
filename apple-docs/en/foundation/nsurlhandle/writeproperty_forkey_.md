---
title: 'writeProperty:forKey:'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [macOS 10.0+（10.4 起废弃）]
languages: [occ]
beta: false
deprecated: true
doc_path: '/documentation/foundation/nsurlhandle/writeproperty:forkey:'
source_url: 'https://developer.apple.com/documentation/foundation/nsurlhandle/writeproperty:forkey:'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsurlhandle/writeproperty%3Aforkey%3A.json'
content_hash: 'sha256:078cb3acc9b36be6'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSURLHandle](../nsurlhandle.md)

# writeProperty:forKey:

<sub>Instance Method</sub>

Sets the property of the receiver’s resource for a specified key to the specified value.

> [!warning] Deprecated
> Use [NSURLConnection](../nsurlconnection.md) or [NSURLDownload](../nsurldownload.md) instead; see [URL Loading System](../url-loading-system.md).

<sub>Mac Catalyst, macOS</sub>

```objc
- (BOOL) writeProperty:(id) propertyValue forKey:(NSString *) propertyKey;
```

## Parameters

- `propertyValue` — The new value for the property.

- `propertyKey` — The key of the desired property.

## Return Value

[true](../../swift/true.md) if the modification was successful, [false](../../swift/false.md) otherwise.

## Discussion

Must be overridden by subclasses.

## See Also

### Setting and getting resource properties

- [propertyForKey:](propertyforkey_.md) — Returns the property for the specified key. _(deprecated)_
- [propertyForKeyIfAvailable:](propertyforkeyifavailable_.md) — Returns the property for the specified key only if the value is already available; that is, the client doesn’t need to do any work. _(deprecated)_
