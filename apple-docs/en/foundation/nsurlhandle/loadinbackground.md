---
title: loadInBackground
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [macOS 10.0+（10.4 起废弃）]
languages: [occ]
beta: false
deprecated: true
doc_path: /documentation/foundation/nsurlhandle/loadinbackground
source_url: 'https://developer.apple.com/documentation/foundation/nsurlhandle/loadinbackground'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsurlhandle/loadinbackground.json'
content_hash: 'sha256:66297e3445068275'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSURLHandle](../nsurlhandle.md)

# loadInBackground

<sub>Instance Method</sub>

Loads the receiver’s data in the background.

> [!warning] Deprecated
> Use [NSURLConnection](../nsurlconnection.md) or [NSURLDownload](../nsurldownload.md) instead; see [URL Loading System](../url-loading-system.md).

<sub>Mac Catalyst, macOS</sub>

```objc
- (void) loadInBackground;
```

## Discussion

Each subclass determines its own loading policy. Clients should not assume that multiple background loads can proceed simultaneously. For example, a subclass may maintain only one thread for background loading, so only one background loading operation can be in progress at a time. If multiple background loads are requested, the later requests will wait in a queue until earlier requests are handled.

## See Also

### Loading resource data

- [availableResourceData](availableresourcedata.md) — Immediately returns the currently available resource data managed by the URL handle. _(deprecated)_
- [backgroundLoadDidFailWithReason:](backgroundloaddidfailwithreason_.md) — Called when a background load fails. _(deprecated)_
- [beginLoadInBackground](beginloadinbackground.md) — Called when a background load begins. _(deprecated)_
- [cancelLoadInBackground](cancelloadinbackground.md) — Called to cancel a load currently in progress. _(deprecated)_
- [didLoadBytes:loadComplete:](didloadbytes_loadcomplete_.md) — Appends new data to the receiver’s resource data. _(deprecated)_
- [endLoadInBackground](endloadinbackground.md) — Halts any background loading. _(deprecated)_
- [expectedResourceDataSize](expectedresourcedatasize.md) — Returns the expected length of the resource data if it is provided by the server. _(deprecated)_
- [failureReason](failurereason.md) — Returns a string describing the reason a load failed. _(deprecated)_
- [flushCachedData](flushcacheddata.md) — Flushes any cached data for the URL served by this URL handle. _(deprecated)_
- [loadInForeground](loadinforeground.md) — Loads the receiver’s data synchronously. _(deprecated)_
- [resourceData](resourcedata.md) — Returns the resource data managed by the receiver, loading it if necessary. _(deprecated)_
- [status](status-c.method.md) — Returns the status of the receiver. _(deprecated)_
- [Status](status-swift.enum.md) — These following constants are defined by `NSURLHandle` and are returned by [status](status-c.method.md).
