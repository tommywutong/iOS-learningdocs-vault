---
title: 'URLHandleUsingCache:'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [macOS 10.0+（10.4 起废弃）]
languages: [occ]
beta: false
deprecated: true
doc_path: '/documentation/foundation/nsurl/urlhandleusingcache:'
source_url: 'https://developer.apple.com/documentation/foundation/nsurl/urlhandleusingcache:'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsurl/urlhandleusingcache%3A.json'
content_hash: 'sha256:62c5b28e8ce30598'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSURL](../nsurl.md)

# URLHandleUsingCache:

<sub>Instance Method</sub>

Returns a URL handle to service the receiver.

<sub>macOS</sub>

```objc
- (NSURLHandle *) URLHandleUsingCache:(BOOL) shouldUseCache;
```

## Parameters

- `shouldUseCache` — Whether to use a cached URL handle. If `shouldUseCache` is [true](../../swift/true.md), the cache is searched for a URL handle that has serviced the receiver or another identical URL. If `shouldUseCache` is [false](../../swift/false.md), a newly instantiated handle is returned, even if an equivalent URL has been loaded.

## Return Value

A URL handle to service the receiver.

## Discussion

Sophisticated clients use the URL handle directly for additional control.

### Special Considerations

Use the [URLSession](../urlsession.md) or [NSURLConnection](../nsurlconnection.md) classes for loading content from remote URLs.

## See Also

### Related Documentation

- [cachedHandleForURL:](../nsurlhandle/cachedhandleforurl_.md) — Returns the URL handle from the cache that has serviced the specified URL or another identical URL. _(deprecated)_

### Deprecated

- [- initWithScheme:host:path:](<init(scheme_host_path_).md>) — Initializes a newly created NSURL with a specified scheme, host, and path. _(deprecated)_
- [loadResourceDataNotifyingClient:usingCache:](loadresourcedatanotifyingclient_usingcache_.md) — Loads the receiver’s resource data in the background. _(deprecated)_
- [resourceDataUsingCache:](resourcedatausingcache_.md) — Returns the receiver’s resource data, loading it if necessary. _(deprecated)_
- [setResourceData:](setresourcedata_.md) — Attempts to set the resource data for the receiver. _(deprecated)_
- [propertyForKey:](propertyforkey_.md) — Returns the specified property of the receiver’s resource. _(deprecated)_
- [setProperty:forKey:](setproperty_forkey_.md) — Changes the specified property of the receiver’s resource. _(deprecated)_
