---
title: 'propertyForKey:'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [macOS 10.0+（10.4 起废弃）]
languages: [occ]
beta: false
deprecated: true
doc_path: '/documentation/foundation/nsurl/propertyforkey:'
source_url: 'https://developer.apple.com/documentation/foundation/nsurl/propertyforkey:'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsurl/propertyforkey%3A.json'
content_hash: 'sha256:f7dc445bf834a70b'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSURL](../nsurl.md)

# propertyForKey:

<sub>Instance Method</sub>

Returns the specified property of the receiver’s resource.

<sub>macOS</sub>

```objc
- (id) propertyForKey:(NSString *) propertyKey;
```

## Parameters

- `propertyKey` — The key of the desired property.

## Return Value

The value of the property of the receiver’s resource for the provided key. Returns `nil` if there is no such key.

## See Also

### Deprecated

- [- initWithScheme:host:path:](<init(scheme_host_path_).md>) — Initializes a newly created NSURL with a specified scheme, host, and path. _(deprecated)_
- [URLHandleUsingCache:](urlhandleusingcache_.md) — Returns a URL handle to service the receiver. _(deprecated)_
- [loadResourceDataNotifyingClient:usingCache:](loadresourcedatanotifyingclient_usingcache_.md) — Loads the receiver’s resource data in the background. _(deprecated)_
- [resourceDataUsingCache:](resourcedatausingcache_.md) — Returns the receiver’s resource data, loading it if necessary. _(deprecated)_
- [setResourceData:](setresourcedata_.md) — Attempts to set the resource data for the receiver. _(deprecated)_
- [setProperty:forKey:](setproperty_forkey_.md) — Changes the specified property of the receiver’s resource. _(deprecated)_
