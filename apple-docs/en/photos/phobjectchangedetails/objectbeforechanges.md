---
title: objectBeforeChanges
framework: Photos
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.1+, macOS 10.13+, tvOS 10.0+, visionOS 1.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/photos/phobjectchangedetails/objectbeforechanges
source_url: 'https://developer.apple.com/documentation/photos/phobjectchangedetails/objectbeforechanges'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/photos/phobjectchangedetails/objectbeforechanges.json'
content_hash: 'sha256:d46a1ba330726e73'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Photos](../../photos.md) · [PHObjectChangeDetails](../phobjectchangedetails.md)

# objectBeforeChanges

<sub>Instance Property</sub>

An object that reflects the original state of the asset or collection it represents.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
var objectBeforeChanges: ObjectType { get }
```

## Discussion

This property’s value is the same object you passed to the [changeDetailsForObject:](../phchange/changedetailsforobject_.md) to request change details.

## See Also

### Getting the Changed Object

- [objectAfterChanges](objectafterchanges.md) — An object that reflects the current state of the asset or collection it represents.
