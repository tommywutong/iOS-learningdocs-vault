---
title: 'write(to:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 11.0+, iPadOS 11.0+, Mac Catalyst 13.1+, macOS 10.13+, tvOS 11.0+, visionOS 1.0+, watchOS 4.0+]
languages: [swift, occ, occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/nsdictionary/write(to:)'
source_url: 'https://developer.apple.com/documentation/foundation/nsdictionary/write(to:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsdictionary/write%28to%3A%29.json'
content_hash: 'sha256:55d2f660da22c83f'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSDictionary](../nsdictionary.md)

# write(to:)

<sub>Instance Method</sub>

Writes a property list representation of the contents of the dictionary to a given URL.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func write(to url: URL) throws
```

## Parameters

- `url` — The URL to which to write the dictionary.

## Discussion

This method recursively validates that all the contained objects are property list objects (instances of [NSData](../nsdata.md), [NSDate](../nsdate.md), [NSNumber](../nsnumber.md), [NSString](../nsstring.md), [NSArray](../nsarray.md), or [NSDictionary](../nsdictionary.md)) before writing out the file. The method throws an error if all the objects are not property list objects, because the resulting output wouldn’t be a valid property list.

If the dictionary’s contents are all property list objects, you can use the location written by this method to initialize a new dictionary with the instance method `NSDictionary/init(contentsOfURL:)-4pv16`.

If you need greater control over the property list representation, use [PropertyListSerialization](../propertylistserialization.md) instead.

For more information about property lists, see [Property List Programming Guide](https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/PropertyLists/Introduction/Introduction.html#//apple_ref/doc/uid/10000048i).

## See Also

### Storing Dictionaries

- [- writeToURL:atomically:](<write(to_atomically_).md>) — Writes a property list representation of the contents of the dictionary to a given URL. _(deprecated)_
- [- writeToFile:atomically:](<write(tofile_atomically_).md>) — Writes a property list representation of the contents of the dictionary to a given path. _(deprecated)_
