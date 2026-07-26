---
title: 'resourceDataUsingCache:'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [macOS 10.0+（10.4 起废弃）]
languages: [occ]
beta: false
deprecated: true
doc_path: '/documentation/foundation/nsurl/resourcedatausingcache:'
source_url: 'https://developer.apple.com/documentation/foundation/nsurl/resourcedatausingcache:'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsurl/resourcedatausingcache%3A.json'
content_hash: 'sha256:a20f04002a1730f8'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSURL](../nsurl.md)

# resourceDataUsingCache:

<sub>Instance Method</sub>

Returns the receiver’s resource data, loading it if necessary.

<sub>macOS</sub>

```objc
- (NSData *) resourceDataUsingCache:(BOOL) shouldUseCache;
```

## Parameters

- `shouldUseCache` — Whether the URL should use cached resource data from an already loaded URL that refers to the same resource. If `YES`, the cache is consulted when loading data. If `NO`, the data is always loaded directly, without consulting the cache.

## Return Value

The receiver’s resource data.

## Discussion

If the receiver has not already loaded its resource data, it will attempt to load it as a blocking operation.

In OS X v10.4, this method requests that the data be sent with gzip compression, however it does not automatically decompress the data if the server complies with this request. Data is automatically decompressed in macOS 10.5 and later.

### Special Considerations

Use the [URLSession](../urlsession.md) or [NSURLConnection](../nsurlconnection.md) classes for loading content from remote URLs.

## See Also

### Deprecated

- [- initWithScheme:host:path:](<init(scheme_host_path_).md>) — Initializes a newly created NSURL with a specified scheme, host, and path. _(deprecated)_
- [URLHandleUsingCache:](urlhandleusingcache_.md) — Returns a URL handle to service the receiver. _(deprecated)_
- [loadResourceDataNotifyingClient:usingCache:](loadresourcedatanotifyingclient_usingcache_.md) — Loads the receiver’s resource data in the background. _(deprecated)_
- [setResourceData:](setresourcedata_.md) — Attempts to set the resource data for the receiver. _(deprecated)_
- [propertyForKey:](propertyforkey_.md) — Returns the specified property of the receiver’s resource. _(deprecated)_
- [setProperty:forKey:](setproperty_forkey_.md) — Changes the specified property of the receiver’s resource. _(deprecated)_
