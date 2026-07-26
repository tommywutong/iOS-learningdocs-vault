---
title: 'removeCachedResourceValue(forKey:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 7.0+, iPadOS 7.0+, Mac Catalyst 13.1+, macOS 10.9+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/nsurl/removecachedresourcevalue(forkey:)'
source_url: 'https://developer.apple.com/documentation/foundation/nsurl/removecachedresourcevalue(forkey:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsurl/removecachedresourcevalue%28forkey%3A%29.json'
content_hash: 'sha256:04bec91e83107af0'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSURL](../nsurl.md)

# removeCachedResourceValue(forKey:)

<sub>Instance Method</sub>

Removes the cached resource value identified by a given key from the URL object.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func removeCachedResourceValue(forKey key: URLResourceKey)
```

## Parameters

- `key` — The resource value key whose cached values you want to remove.

## Discussion

Removing a cached resource value may remove other cached resource values because some resource values are cached as a set of values, and because some resource values depend on other resource values. (Temporary resource values have no dependencies.)

This method is currently applicable only to URLs for file system resources.

> [!note] Note
> The caching behavior of the `NSURL` and `CFURL` APIs differ. For `NSURL`, all cached values (not temporary values) are automatically removed after each pass through the run loop. You only need to call the [- removeCachedResourceValueForKey:](<removecachedresourcevalue(forkey_).md>) method when you want to clear the cache within a single execution of the run loop. The `CFURL` functions, on the other hand, do not automatically clear cached resource values. The client has complete control over the cache lifetimes, and you must use [CFURLClearResourcePropertyCacheForKey(_:_:)](<../../corefoundation/cfurlclearresourcepropertycacheforkey(____).md>) or [CFURLClearResourcePropertyCache(_:)](<../../corefoundation/cfurlclearresourcepropertycache(__).md>) to clear cached resource values.

## See Also

### Accessing Resource Values

- [- resourceValuesForKeys:error:](<resourcevalues(forkeys_).md>) — Returns the resource values for the properties identified by specified array of keys.
- [- getResourceValue:forKey:error:](<getresourcevalue(__forkey_).md>) — Returns the value of the resource property for the specified key.
- [- setResourceValue:forKey:error:](<setresourcevalue(__forkey_).md>) — Sets the URL’s resource property for a given key to a given value.
- [- setResourceValues:error:](<setresourcevalues(__).md>) — Sets the URL’s resource properties for a given set of keys to a given set of values.
- [- removeAllCachedResourceValues](<removeallcachedresourcevalues().md>) — Removes all cached resource values and temporary resource values from the URL object.
- [- setTemporaryResourceValue:forKey:](<settemporaryresourcevalue(__forkey_).md>) — Sets a temporary resource value on the URL object.
- [URLResourceKey](../urlresourcekey.md) — Keys that apply to file system URLs.
