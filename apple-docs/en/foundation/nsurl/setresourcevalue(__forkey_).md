---
title: 'setResourceValue(_:forKey:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 4.0+, iPadOS 4.0+, Mac Catalyst 13.1+, macOS 10.6+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/nsurl/setresourcevalue(_:forkey:)'
source_url: 'https://developer.apple.com/documentation/foundation/nsurl/setresourcevalue(_:forkey:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsurl/setresourcevalue%28_%3Aforkey%3A%29.json'
content_hash: 'sha256:dda8afe34a9b28f2'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSURL](../nsurl.md)

# setResourceValue(_:forKey:)

<sub>Instance Method</sub>

Sets the URL’s resource property for a given key to a given value.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func setResourceValue(_ value: Any?, forKey key: URLResourceKey) throws
```

## Parameters

- `value` — The value for the resource property defined by `key`.

- `key` — The name of one of the URL’s resource properties.

## Discussion

This method synchronously writes the new resource value out to disk. Attempts to set a read-only resource property or to set a resource property that is not supported by the resource are ignored and are not considered errors.

If an error occurs, this method returns [false](../../swift/false.md) and populates the object pointer referenced by `error` with additional information.

> [!note] Note
> This method applies only to URLs for file system resources.

> [!note] Handling Errors in Swift
> In Swift, this method returns `Void` and is marked with the `throws` keyword to indicate that it throws an error in cases of failure.
>
> You call this method in a `try` expression and handle any errors in the `catch` clauses of a `do` statement, as described in [Error Handling](https://docs.swift.org/swift-book/LanguageGuide/ErrorHandling.html) in [The Swift Programming Language](https://docs.swift.org/swift-book/) and `About Imported Cocoa Error Parameters`.

## See Also

### Accessing Resource Values

- [- resourceValuesForKeys:error:](<resourcevalues(forkeys_).md>) — Returns the resource values for the properties identified by specified array of keys.
- [- getResourceValue:forKey:error:](<getresourcevalue(__forkey_).md>) — Returns the value of the resource property for the specified key.
- [- setResourceValues:error:](<setresourcevalues(__).md>) — Sets the URL’s resource properties for a given set of keys to a given set of values.
- [- removeAllCachedResourceValues](<removeallcachedresourcevalues().md>) — Removes all cached resource values and temporary resource values from the URL object.
- [- removeCachedResourceValueForKey:](<removecachedresourcevalue(forkey_).md>) — Removes the cached resource value identified by a given key from the URL object.
- [- setTemporaryResourceValue:forKey:](<settemporaryresourcevalue(__forkey_).md>) — Sets a temporary resource value on the URL object.
- [URLResourceKey](../urlresourcekey.md) — Keys that apply to file system URLs.
