---
title: 'resourceValues(forKeys:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 8.0+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/foundation/url/resourcevalues(forkeys:)'
source_url: 'https://developer.apple.com/documentation/foundation/url/resourcevalues(forkeys:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/url/resourcevalues%28forkeys%3A%29.json'
content_hash: 'sha256:0dd5d5531ff7ac13'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [URL](../url.md)

# resourceValues(forKeys:)

<sub>Instance Method</sub>

Returns a collection of resource values identified by the given resource keys.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func resourceValues(forKeys keys: Set<URLResourceKey>) throws -> URLResourceValues
```

## Parameters

- `keys` — A set of URL resource keys indicating the values to retrieve.

## Return Value

A [URLResourceValues](../urlresourcevalues.md) instance, containing the retrieved values.

## Discussion

This method first checks if the URL instance already caches the specified resource values. If so, it returns the cached resource values to the caller. If not, then this method synchronously obtains the resource values from the backing store, adds them to the URL object’s cache, and returns a populated [URLResourceValues](../urlresourcevalues.md) instance. This method only populates [URLResourceValues](../urlresourcevalues.md) members corresponding to the contents of the `keys` parameter.

The type of the returned resource value varies by resource property; for details, see the documentation for the [URLResourceKey](../urlresourcekey.md) you want to access.

If there’s no available value for a given key in `keys`, the returned [URLResourceValues](../urlresourcevalues.md) contains `nil` for the corresponding item. If this method fails to determine a value’s availability or retrieve its value, the method throws an error.

When you call this method from the main thread, the URL removes cached resource values the next time the thread’s run loop runs, except those added as temporary properties. You can explicitly remove cached resource values with [removeCachedResourceValue(forKey:)](<removecachedresourcevalue(forkey_).md>) and [removeAllCachedResourceValues()](<removeallcachedresourcevalues().md>).

> [!note] Note
> This method is currently applicable only to URLs for file system resources.

## See Also

### Accessing resource values

- [setResourceValues(_:)](<setresourcevalues(__).md>) — Sets the resource value identified by a given resource key.
- [removeCachedResourceValue(forKey:)](<removecachedresourcevalue(forkey_).md>) — Removes the cached resource value identified by a given resource value key from the URL object.
- [removeAllCachedResourceValues()](<removeallcachedresourcevalues().md>) — Removes all cached resource values and all temporary resource values from the URL object.
- [setTemporaryResourceValue(_:forKey:)](<settemporaryresourcevalue(__forkey_).md>) — Sets a temporary resource value on the URL object.
- [URLResourceKey](../urlresourcekey.md) — Keys that apply to file system URLs.
- [URLResourceValues](../urlresourcevalues.md) — The properties that the file system resources support.
