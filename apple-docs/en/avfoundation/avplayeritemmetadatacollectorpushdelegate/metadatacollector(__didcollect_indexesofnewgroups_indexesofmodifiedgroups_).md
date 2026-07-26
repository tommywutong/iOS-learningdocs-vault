---
title: 'metadataCollector(_:didCollect:indexesOfNewGroups:indexesOfModifiedGroups:)'
framework: AVFoundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 9.3+, iPadOS 9.3+, Mac Catalyst 13.1+, macOS 10.11.3+, tvOS 9.2+, visionOS 1.0+, watchOS 2.3+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/avfoundation/avplayeritemmetadatacollectorpushdelegate/metadatacollector(_:didcollect:indexesofnewgroups:indexesofmodifiedgroups:)'
source_url: 'https://developer.apple.com/documentation/avfoundation/avplayeritemmetadatacollectorpushdelegate/metadatacollector(_:didcollect:indexesofnewgroups:indexesofmodifiedgroups:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avplayeritemmetadatacollectorpushdelegate/metadatacollector%28_%3Adidcollect%3Aindexesofnewgroups%3Aindexesofmodifiedgroups%3A%29.json'
content_hash: 'sha256:484a4353e10545ff'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVPlayerItemMetadataCollectorPushDelegate](../avplayeritemmetadatacollectorpushdelegate.md)

# metadataCollector(_:didCollect:indexesOfNewGroups:indexesOfModifiedGroups:)

<sub>Instance Method</sub>

Tells the delegate the collected metadata group information has changed and needs to be updated.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func metadataCollector(_ metadataCollector: AVPlayerItemMetadataCollector, didCollect metadataGroups: sending [AVDateRangeMetadataGroup], indexesOfNewGroups: IndexSet, indexesOfModifiedGroups: IndexSet)
```

## Parameters

- `metadataCollector` — The [AVPlayerItemMetadataCollector](../avplayeritemmetadatacollector.md) on which this delegate is set.

- `metadataGroups` — The complete array of all metadata groups meeting the criteria of the output.

- `indexesOfNewGroups` — The indexes of the `metadataGroups` added since the last delegate invocation of this method.

- `indexesOfModifiedGroups` — The indexes of the `metadataGroups` modified since the last delegate invocation of this method.

## Discussion

This method is called when additions or modifications are made to the array of collected metadata groups. The initial invocation will have `indexesOfNewGroup` referring to every index in `metadataGroups`. Subsequent invocations may not contain all previously collected metadata groups if they no longer refer to a region in the player item’s [seekableTimeRanges](../avplayeritem/seekabletimeranges.md).
