---
title: 'getResourceValue(_:forKey:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 4.0+, iPadOS 4.0+, Mac Catalyst 13.1+, macOS 10.6+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/nsurl/getresourcevalue(_:forkey:)'
source_url: 'https://developer.apple.com/documentation/foundation/nsurl/getresourcevalue(_:forkey:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsurl/getresourcevalue%28_%3Aforkey%3A%29.json'
content_hash: 'sha256:d79795b2a7a5f015'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSURL](../nsurl.md)

# getResourceValue(_:forKey:)

<sub>Instance Method</sub>

Returns the value of the resource property for the specified key.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func getResourceValue(_ value: AutoreleasingUnsafeMutablePointer<AnyObject?>, forKey key: URLResourceKey) throws
```

## Parameters

- `value` — The location where the value for the resource property identified by `key` should be stored.

- `key` — The name of one of the URL’s resource properties.

## Discussion

This method first checks if the URL object already caches the resource value. If so, it returns the cached resource value to the caller. If not, then this method synchronously obtains the resource value from the backing store, adds the resource value to the URL object’s cache, and returns the resource value to the caller.

The type of the returned resource value varies by resource property; for details, see the documentation for the key you want to access.

If this method returns [true](../../swift/true.md) and the value is populated with `nil`, it means that the resource property is not available for the specified resource, and that no errors occurred when determining that the resource property was unavailable.

If this method returns [false](../../swift/false.md), an error occurred. The object pointer referenced by `error` is populated with additional information.

> [!note] Note
> This method applies only to URLs that represent file system resources.

> [!note] Handling Errors in Swift
> In Swift, this method returns `Void` and is marked with the `throws` keyword to indicate that it throws an error in cases of failure.
>
> You call this method in a `try` expression and handle any errors in the `catch` clauses of a `do` statement, as described in [Error Handling](https://docs.swift.org/swift-book/LanguageGuide/ErrorHandling.html) in [The Swift Programming Language](https://docs.swift.org/swift-book/) and `About Imported Cocoa Error Parameters`.

## See Also

### Accessing Resource Values

- [- resourceValuesForKeys:error:](<resourcevalues(forkeys_).md>) — Returns the resource values for the properties identified by specified array of keys.
- [- setResourceValue:forKey:error:](<setresourcevalue(__forkey_).md>) — Sets the URL’s resource property for a given key to a given value.
- [- setResourceValues:error:](<setresourcevalues(__).md>) — Sets the URL’s resource properties for a given set of keys to a given set of values.
- [- removeAllCachedResourceValues](<removeallcachedresourcevalues().md>) — Removes all cached resource values and temporary resource values from the URL object.
- [- removeCachedResourceValueForKey:](<removecachedresourcevalue(forkey_).md>) — Removes the cached resource value identified by a given key from the URL object.
- [- setTemporaryResourceValue:forKey:](<settemporaryresourcevalue(__forkey_).md>) — Sets a temporary resource value on the URL object.
- [URLResourceKey](../urlresourcekey.md) — Keys that apply to file system URLs.
