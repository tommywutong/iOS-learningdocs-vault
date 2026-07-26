---
title: 'setResourceData:'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [macOS 10.0+（10.4 起废弃）]
languages: [occ]
beta: false
deprecated: true
doc_path: '/documentation/foundation/nsurl/setresourcedata:'
source_url: 'https://developer.apple.com/documentation/foundation/nsurl/setresourcedata:'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsurl/setresourcedata%3A.json'
content_hash: 'sha256:6529080c6a4756d5'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSURL](../nsurl.md)

# setResourceData:

<sub>Instance Method</sub>

Attempts to set the resource data for the receiver.

<sub>macOS</sub>

```objc
- (BOOL) setResourceData:(NSData *) data;
```

## Parameters

- `data` — The data to set for the URL.

## Return Value

Returns [true](../../swift/true.md) if successful, [false](../../swift/false.md) otherwise.

## Discussion

In the case of a file URL, setting the data involves writing `data` to the specified file.

## See Also

### Deprecated

- [- initWithScheme:host:path:](<init(scheme_host_path_).md>) — Initializes a newly created NSURL with a specified scheme, host, and path. _(deprecated)_
- [URLHandleUsingCache:](urlhandleusingcache_.md) — Returns a URL handle to service the receiver. _(deprecated)_
- [loadResourceDataNotifyingClient:usingCache:](loadresourcedatanotifyingclient_usingcache_.md) — Loads the receiver’s resource data in the background. _(deprecated)_
- [resourceDataUsingCache:](resourcedatausingcache_.md) — Returns the receiver’s resource data, loading it if necessary. _(deprecated)_
- [propertyForKey:](propertyforkey_.md) — Returns the specified property of the receiver’s resource. _(deprecated)_
- [setProperty:forKey:](setproperty_forkey_.md) — Changes the specified property of the receiver’s resource. _(deprecated)_
