---
title: 'removeCachedResourceValue(forKey:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 8.0+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/foundation/url/removecachedresourcevalue(forkey:)'
source_url: 'https://developer.apple.com/documentation/foundation/url/removecachedresourcevalue(forkey:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/url/removecachedresourcevalue%28forkey%3A%29.json'
content_hash: 'sha256:849df3b03239a6ac'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [URL](../url.md)

# removeCachedResourceValue(forKey:)

<sub>Instance Method</sub>

Removes the cached resource value identified by a given resource value key from the URL object.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
mutating func removeCachedResourceValue(forKey key: URLResourceKey)
```

## Discussion

Removing a cached resource value may remove other cached resource values because some resource values are cached as a set of values, and because some resource values depend on other resource values (temporary resource values have no dependencies). This method is currently applicable only to URLs for file system resources.

## See Also

### Accessing resource values

- [resourceValues(forKeys:)](<resourcevalues(forkeys_).md>) — Returns a collection of resource values identified by the given resource keys.
- [setResourceValues(_:)](<setresourcevalues(__).md>) — Sets the resource value identified by a given resource key.
- [removeAllCachedResourceValues()](<removeallcachedresourcevalues().md>) — Removes all cached resource values and all temporary resource values from the URL object.
- [setTemporaryResourceValue(_:forKey:)](<settemporaryresourcevalue(__forkey_).md>) — Sets a temporary resource value on the URL object.
- [URLResourceKey](../urlresourcekey.md) — Keys that apply to file system URLs.
- [URLResourceValues](../urlresourcevalues.md) — The properties that the file system resources support.
