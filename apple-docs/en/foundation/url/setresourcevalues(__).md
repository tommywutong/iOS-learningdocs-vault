---
title: 'setResourceValues(_:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 8.0+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/foundation/url/setresourcevalues(_:)'
source_url: 'https://developer.apple.com/documentation/foundation/url/setresourcevalues(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/url/setresourcevalues%28_%3A%29.json'
content_hash: 'sha256:cf5e7c1361a70090'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [URL](../url.md)

# setResourceValues(_:)

<sub>Instance Method</sub>

Sets the resource value identified by a given resource key.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
mutating func setResourceValues(_ values: URLResourceValues) throws
```

## Discussion

This method writes the new resource values out to the backing store. Attempts to set a read-only resource property or to set a resource property not supported by the resource are ignored and are not considered errors. This method is currently applicable only to URLs for file system resources.

`URLResourceValues` keeps track of which of its properties have been set. Those values are the ones used by this function to determine which properties to write.

## See Also

### Accessing resource values

- [resourceValues(forKeys:)](<resourcevalues(forkeys_).md>) — Returns a collection of resource values identified by the given resource keys.
- [removeCachedResourceValue(forKey:)](<removecachedresourcevalue(forkey_).md>) — Removes the cached resource value identified by a given resource value key from the URL object.
- [removeAllCachedResourceValues()](<removeallcachedresourcevalues().md>) — Removes all cached resource values and all temporary resource values from the URL object.
- [setTemporaryResourceValue(_:forKey:)](<settemporaryresourcevalue(__forkey_).md>) — Sets a temporary resource value on the URL object.
- [URLResourceKey](../urlresourcekey.md) — Keys that apply to file system URLs.
- [URLResourceValues](../urlresourcevalues.md) — The properties that the file system resources support.
