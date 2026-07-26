---
title: 'setProperty:forKey:'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [macOS 10.0+（10.4 起废弃）]
languages: [occ]
beta: false
deprecated: true
doc_path: '/documentation/foundation/nsurl/setproperty:forkey:'
source_url: 'https://developer.apple.com/documentation/foundation/nsurl/setproperty:forkey:'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsurl/setproperty%3Aforkey%3A.json'
content_hash: 'sha256:4a9c0413e93d3e32'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSURL](../nsurl.md)

# setProperty:forKey:

<sub>Instance Method</sub>

Changes the specified property of the receiver’s resource.

<sub>macOS</sub>

```objc
- (BOOL) setProperty:(id) property forKey:(NSString *) propertyKey;
```

## Parameters

- `property` — The new value of the property of the receiver’s resource.

- `propertyKey` — The key of the desired property.

## Return Value

Returns [true](../../swift/true.md) if the modification was successful, [false](../../swift/false.md) otherwise.

## See Also

### Deprecated

- [- initWithScheme:host:path:](<init(scheme_host_path_).md>) — Initializes a newly created NSURL with a specified scheme, host, and path. _(deprecated)_
- [URLHandleUsingCache:](urlhandleusingcache_.md) — Returns a URL handle to service the receiver. _(deprecated)_
- [loadResourceDataNotifyingClient:usingCache:](loadresourcedatanotifyingclient_usingcache_.md) — Loads the receiver’s resource data in the background. _(deprecated)_
- [resourceDataUsingCache:](resourcedatausingcache_.md) — Returns the receiver’s resource data, loading it if necessary. _(deprecated)_
- [setResourceData:](setresourcedata_.md) — Attempts to set the resource data for the receiver. _(deprecated)_
- [propertyForKey:](propertyforkey_.md) — Returns the specified property of the receiver’s resource. _(deprecated)_
