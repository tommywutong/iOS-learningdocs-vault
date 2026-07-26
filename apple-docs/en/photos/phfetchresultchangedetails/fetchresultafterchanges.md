---
title: fetchResultAfterChanges
framework: Photos
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.1+, macOS 10.13+, tvOS 10.0+, visionOS 1.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/photos/phfetchresultchangedetails/fetchresultafterchanges
source_url: 'https://developer.apple.com/documentation/photos/phfetchresultchangedetails/fetchresultafterchanges'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/photos/phfetchresultchangedetails/fetchresultafterchanges.json'
content_hash: 'sha256:343e1b97dc22cd99'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Photos](../../photos.md) · [PHFetchResultChangeDetails](../phfetchresultchangedetails.md)

# fetchResultAfterChanges

<sub>Instance Property</sub>

The current fetch result, incorporating recent changes.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
var fetchResultAfterChanges: PHFetchResult<ObjectType> { get }
```

## Discussion

You can use this object to inspect the current state of the fetched objects even if the [hasIncrementalChanges](hasincrementalchanges.md) property’s value is `false`. Using this fetch result is equivalent to performing once more the same fetch that returned the original fetch result.

## See Also

### Getting the Changed Fetch Result

- [fetchResultBeforeChanges](fetchresultbeforechanges.md) — The original fetch result, without recent changes.
