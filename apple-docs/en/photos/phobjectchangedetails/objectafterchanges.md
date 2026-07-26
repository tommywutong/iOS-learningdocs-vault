---
title: objectAfterChanges
framework: Photos
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.1+, macOS 10.13+, tvOS 10.0+, visionOS 1.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/photos/phobjectchangedetails/objectafterchanges
source_url: 'https://developer.apple.com/documentation/photos/phobjectchangedetails/objectafterchanges'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/photos/phobjectchangedetails/objectafterchanges.json'
content_hash: 'sha256:abca5043cfe6bd12'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Photos](../../photos.md) · [PHObjectChangeDetails](../phobjectchangedetails.md)

# objectAfterChanges

<sub>Instance Property</sub>

An object that reflects the current state of the asset or collection it represents.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
var objectAfterChanges: ObjectType? { get }
```

## Discussion

Read this object’s properties to retrieve updated metadata for the asset or collection. Using this object is equivalent to repeating the same fetch that returned the original object.

## See Also

### Getting the Changed Object

- [objectBeforeChanges](objectbeforechanges.md) — An object that reflects the original state of the asset or collection it represents.
