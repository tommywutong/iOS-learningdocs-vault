---
title: 'loadResourceDataNotifyingClient:usingCache:'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [macOS 10.0+（10.4 起废弃）]
languages: [occ]
beta: false
deprecated: true
doc_path: '/documentation/foundation/nsurl/loadresourcedatanotifyingclient:usingcache:'
source_url: 'https://developer.apple.com/documentation/foundation/nsurl/loadresourcedatanotifyingclient:usingcache:'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsurl/loadresourcedatanotifyingclient%3Ausingcache%3A.json'
content_hash: 'sha256:b088afd0ffc7a9b8'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSURL](../nsurl.md)

# loadResourceDataNotifyingClient:usingCache:

<sub>Instance Method</sub>

Loads the receiver’s resource data in the background.

<sub>macOS</sub>

```objc
- (void) loadResourceDataNotifyingClient:(id) client usingCache:(BOOL) shouldUseCache;
```

## Parameters

- `client` — The client of the loading operation. `client` is notified of the receiver’s progress loading the resource data using the NSURLClient informal protocol. The NSURLClient messages are delivered on the current thread and require the run loop to be running.

- `shouldUseCache` — Whether the URL should use cached resource data from an already loaded URL that refers to the same resource. If `YES`, the cache is consulted when loading data. If `NO`, the data is always loaded directly, without consulting the cache.

## Discussion

A given NSURL object can perform only one background load at a time.

### Special Considerations

Use the [URLSession](../urlsession.md) or [NSURLConnection](../nsurlconnection.md) classes for loading content from remote URLs.

## See Also

### Deprecated

- [- initWithScheme:host:path:](<init(scheme_host_path_).md>) — Initializes a newly created NSURL with a specified scheme, host, and path. _(deprecated)_
- [URLHandleUsingCache:](urlhandleusingcache_.md) — Returns a URL handle to service the receiver. _(deprecated)_
- [resourceDataUsingCache:](resourcedatausingcache_.md) — Returns the receiver’s resource data, loading it if necessary. _(deprecated)_
- [setResourceData:](setresourcedata_.md) — Attempts to set the resource data for the receiver. _(deprecated)_
- [propertyForKey:](propertyforkey_.md) — Returns the specified property of the receiver’s resource. _(deprecated)_
- [setProperty:forKey:](setproperty_forkey_.md) — Changes the specified property of the receiver’s resource. _(deprecated)_
