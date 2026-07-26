---
title: 'setTemporaryResourceValue(_:forKey:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 7.0+, iPadOS 7.0+, Mac Catalyst 13.1+, macOS 10.9+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/nsurl/settemporaryresourcevalue(_:forkey:)'
source_url: 'https://developer.apple.com/documentation/foundation/nsurl/settemporaryresourcevalue(_:forkey:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsurl/settemporaryresourcevalue%28_%3Aforkey%3A%29.json'
content_hash: 'sha256:4bf9d679f1b1fc8d'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSURL](../nsurl.md)

# setTemporaryResourceValue(_:forKey:)

<sub>Instance Method</sub>

Sets a temporary resource value on the URL object.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func setTemporaryResourceValue(_ value: (any Sendable)?, forKey key: URLResourceKey)
```

## Parameters

- `value` — The value to store.

- `key` — The key where the value should be stored. This key must be unique and must not conflict with any system-defined keys. Reverse-domain-name notation is recommended.

## Discussion

Your app can use a temporary resource value to temporarily store a value for an app-defined resource value key in memory without modifying the actual resource that the URL represents. Once set, you can copy the temporary resource value from the URL object just as you would copy system-defined keys—by calling [- getResourceValue:forKey:error:](<getresourcevalue(__forkey_).md>) or [- resourceValuesForKeys:error:](<resourcevalues(forkeys_).md>).

Your app can remove a temporary resource value from the URL object by calling [- removeCachedResourceValueForKey:](<removecachedresourcevalue(forkey_).md>) or [- removeAllCachedResourceValues](<removeallcachedresourcevalues().md>) (to remove all temporary values).

This method is applicable only to URLs for file system resources.

## See Also

### Accessing Resource Values

- [- resourceValuesForKeys:error:](<resourcevalues(forkeys_).md>) — Returns the resource values for the properties identified by specified array of keys.
- [- getResourceValue:forKey:error:](<getresourcevalue(__forkey_).md>) — Returns the value of the resource property for the specified key.
- [- setResourceValue:forKey:error:](<setresourcevalue(__forkey_).md>) — Sets the URL’s resource property for a given key to a given value.
- [- setResourceValues:error:](<setresourcevalues(__).md>) — Sets the URL’s resource properties for a given set of keys to a given set of values.
- [- removeAllCachedResourceValues](<removeallcachedresourcevalues().md>) — Removes all cached resource values and temporary resource values from the URL object.
- [- removeCachedResourceValueForKey:](<removecachedresourcevalue(forkey_).md>) — Removes the cached resource value identified by a given key from the URL object.
- [URLResourceKey](../urlresourcekey.md) — Keys that apply to file system URLs.
