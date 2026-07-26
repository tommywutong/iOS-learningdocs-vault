---
title: 'url(forKey:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 4.0+, iPadOS 4.0+, Mac Catalyst 13.1+, macOS 10.6+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/userdefaults/url(forkey:)'
source_url: 'https://developer.apple.com/documentation/foundation/userdefaults/url(forkey:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/userdefaults/url%28forkey%3A%29.json'
content_hash: 'sha256:7eb1b25ee69e4651'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [UserDefaults](../userdefaults.md)

# url(forKey:)

<sub>Instance Method</sub>

Returns the URL associated with the specified key.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func url(forKey defaultName: String) -> URL?
```

## Parameters

- `defaultName` — The key to retrieve from the defaults database.

## Return Value

The URL associated with `defaultName`, or `nil` if the key isn’t present in the defaults database.

## Discussion

This method uses the data for the specified key to create and return a URL type. If the key is present but the method can’t use it to create a URL, this method returns `nil`. If a file URL contains a tilde (~) character in its path, this method replaces the tilde with an expanded path. If you saved a bookmark URL for the key previously, use the [URLByResolvingBookmarkData:options:relativeToURL:bookmarkDataIsStale:error:](../nsurl/urlbyresolvingbookmarkdata_options_relativetourl_bookmarkdataisstale_error_.md) method to resolve the bookmark data and retrieve an equivalent file URL.

## See Also

### Getting the value of a key

- [- boolForKey:](<bool(forkey_).md>) — Returns the Boolean value associated with the specified key.
- [- integerForKey:](<integer(forkey_).md>) — Returns the integer value associated with the specified key.
- [- floatForKey:](<float(forkey_).md>) — Returns the floating-point value associated with the specified key.
- [- doubleForKey:](<double(forkey_).md>) — Returns the double value associated with the specified key.
- [- stringForKey:](<string(forkey_).md>) — Returns the string associated with the specified key.
- [- stringArrayForKey:](<stringarray(forkey_).md>) — Returns the array of strings associated with the specified key.
- [- dataForKey:](<data(forkey_).md>) — Returns the data object associated with the specified key.
- [- objectForKey:](<object(forkey_).md>) — Returns the object associated with the specified key.
- [- arrayForKey:](<array(forkey_).md>) — Returns the array associated with the specified key.
- [- dictionaryForKey:](<dictionary(forkey_).md>) — Returns the dictionary object associated with the specified key.
- [- dictionaryRepresentation](<dictionaryrepresentation().md>) — Returns a dictionary with the union of all key-value pairs found from all domains.
