---
title: selectedIndex
framework: AVFoundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 18.0+, iPadOS 18.0+, Mac Catalyst 18.0+, macOS 15.0+, tvOS 18.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avcaptureindexpicker/selectedindex
source_url: 'https://developer.apple.com/documentation/avfoundation/avcaptureindexpicker/selectedindex'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avcaptureindexpicker/selectedindex.json'
content_hash: 'sha256:4af245d47bdcff7e'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVCaptureIndexPicker](../avcaptureindexpicker.md)

# selectedIndex

<sub>Instance Property</sub>

The currently selected index.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS</sub>

```swift
var selectedIndex: Int { get set }
```

## Discussion

The default value is `0`. You can only set a value that’s greater than or equal to `0` and less than [numberOfIndexes](numberofindexes.md).

> [!important] Important
> Only modify the selected index from the same dispatch queue that you specified in the control’s [setActionQueue:action:](../avcaptureslider/setactionqueue_action_.md) method.

## See Also

### Accessing the control value

- [numberOfIndexes](numberofindexes.md) — The number of index values the control provides.
