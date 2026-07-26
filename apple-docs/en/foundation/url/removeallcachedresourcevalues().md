---
title: removeAllCachedResourceValues()
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 8.0+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/foundation/url/removeallcachedresourcevalues()
source_url: 'https://developer.apple.com/documentation/foundation/url/removeallcachedresourcevalues()'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/url/removeallcachedresourcevalues%28%29.json'
content_hash: 'sha256:c0446b11694f64cb'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [URL](../url.md)

# removeAllCachedResourceValues()

<sub>Instance Method</sub>

Removes all cached resource values and all temporary resource values from the URL object.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
mutating func removeAllCachedResourceValues()
```

## Discussion

This method is currently applicable only to URLs for file system resources.

## See Also

### Accessing resource values

- [resourceValues(forKeys:)](<resourcevalues(forkeys_).md>) — Returns a collection of resource values identified by the given resource keys.
- [setResourceValues(_:)](<setresourcevalues(__).md>) — Sets the resource value identified by a given resource key.
- [removeCachedResourceValue(forKey:)](<removecachedresourcevalue(forkey_).md>) — Removes the cached resource value identified by a given resource value key from the URL object.
- [setTemporaryResourceValue(_:forKey:)](<settemporaryresourcevalue(__forkey_).md>) — Sets a temporary resource value on the URL object.
- [URLResourceKey](../urlresourcekey.md) — Keys that apply to file system URLs.
- [URLResourceValues](../urlresourcevalues.md) — The properties that the file system resources support.
