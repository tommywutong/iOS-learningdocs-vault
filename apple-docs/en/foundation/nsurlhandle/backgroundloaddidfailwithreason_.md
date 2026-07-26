---
title: 'backgroundLoadDidFailWithReason:'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [macOS 10.0+（10.4 起废弃）]
languages: [occ]
beta: false
deprecated: true
doc_path: '/documentation/foundation/nsurlhandle/backgroundloaddidfailwithreason:'
source_url: 'https://developer.apple.com/documentation/foundation/nsurlhandle/backgroundloaddidfailwithreason:'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsurlhandle/backgroundloaddidfailwithreason%3A.json'
content_hash: 'sha256:8e3e8f1fd3710291'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSURLHandle](../nsurlhandle.md)

# backgroundLoadDidFailWithReason:

<sub>Instance Method</sub>

Called when a background load fails.

> [!warning] Deprecated
> Use [NSURLConnection](../nsurlconnection.md) or [NSURLDownload](../nsurldownload.md) instead; see [URL Loading System](../url-loading-system.md).

<sub>Mac Catalyst, macOS</sub>

```objc
- (void) backgroundLoadDidFailWithReason:(NSString *) reason;
```

## Parameters

- `reason` — The status message indicating why the background load failed.

## Discussion

This method is provided mainly for subclasses that wish to take some action before passing along the failure notification to the URL client. This method should invoke `super`’s implementation before returning.

## See Also

### Loading resource data

- [availableResourceData](availableresourcedata.md) — Immediately returns the currently available resource data managed by the URL handle. _(deprecated)_
- [beginLoadInBackground](beginloadinbackground.md) — Called when a background load begins. _(deprecated)_
- [cancelLoadInBackground](cancelloadinbackground.md) — Called to cancel a load currently in progress. _(deprecated)_
- [didLoadBytes:loadComplete:](didloadbytes_loadcomplete_.md) — Appends new data to the receiver’s resource data. _(deprecated)_
- [endLoadInBackground](endloadinbackground.md) — Halts any background loading. _(deprecated)_
- [expectedResourceDataSize](expectedresourcedatasize.md) — Returns the expected length of the resource data if it is provided by the server. _(deprecated)_
- [failureReason](failurereason.md) — Returns a string describing the reason a load failed. _(deprecated)_
- [flushCachedData](flushcacheddata.md) — Flushes any cached data for the URL served by this URL handle. _(deprecated)_
- [loadInBackground](loadinbackground.md) — Loads the receiver’s data in the background. _(deprecated)_
- [loadInForeground](loadinforeground.md) — Loads the receiver’s data synchronously. _(deprecated)_
- [resourceData](resourcedata.md) — Returns the resource data managed by the receiver, loading it if necessary. _(deprecated)_
- [status](status-c.method.md) — Returns the status of the receiver. _(deprecated)_
- [Status](status-swift.enum.md) — These following constants are defined by `NSURLHandle` and are returned by [status](status-c.method.md).
