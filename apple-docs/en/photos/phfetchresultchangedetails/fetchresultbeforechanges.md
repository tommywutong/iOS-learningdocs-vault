---
title: fetchResultBeforeChanges
framework: Photos
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.1+, macOS 10.13+, tvOS 10.0+, visionOS 1.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/photos/phfetchresultchangedetails/fetchresultbeforechanges
source_url: 'https://developer.apple.com/documentation/photos/phfetchresultchangedetails/fetchresultbeforechanges'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/photos/phfetchresultchangedetails/fetchresultbeforechanges.json'
content_hash: 'sha256:caa954e5e5e756b3'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Photos](../../photos.md) · [PHFetchResultChangeDetails](../phfetchresultchangedetails.md)

# fetchResultBeforeChanges

<sub>Instance Property</sub>

The original fetch result, without recent changes.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
var fetchResultBeforeChanges: PHFetchResult<ObjectType> { get }
```

## Discussion

This property’s value is the same object you passed to the [changeDetails(for:)](<../phchange/changedetails(for_)-33a6n.md>) method to request change details.

## See Also

### Getting the Changed Fetch Result

- [fetchResultAfterChanges](fetchresultafterchanges.md) — The current fetch result, incorporating recent changes.
