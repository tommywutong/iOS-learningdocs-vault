---
title: 'init(items:start:end:)'
framework: AVFoundation
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 9.0+, iPadOS 9.0+, Mac Catalyst 13.1+, macOS 10.11+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/avfoundation/avdaterangemetadatagroup/init(items:start:end:)'
source_url: 'https://developer.apple.com/documentation/avfoundation/avdaterangemetadatagroup/init(items:start:end:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avdaterangemetadatagroup/init%28items%3Astart%3Aend%3A%29.json'
content_hash: 'sha256:72fa622357314fd6'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVDateRangeMetadataGroup](../avdaterangemetadatagroup.md)

# init(items:start:end:)

<sub>Initializer</sub>

Initializes an instance of `AVDateRangeMetadataGroup` with a collection of metadata items.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
init(items: [AVMetadataItem], start startDate: Date, end endDate: Date?)
```

## Parameters

- `items` — The array of [AVMetadataItem](../avmetadataitem.md) instances to associate with this group.

- `startDate` — The starting date for the group of metadata items.

- `endDate` — The ending date for the group of metadata items.

## Return Value

A new instance of `AVDateRangeMetadataGroup`.

## Discussion

Creates a new instance of `AVDateRangeMetadataGroup` with the specified collection of metadata items. The `startDate` and `endDate` arguments define the effective time range on the timeline to which the metadata applies.
