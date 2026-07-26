---
title: 'init(_:symbolName:numberOfIndexes:)'
framework: AVFoundation
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 18.0+, iPadOS 18.0+, Mac Catalyst 18.0+, macOS 15.0+, tvOS 18.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/avfoundation/avcaptureindexpicker/init(_:symbolname:numberofindexes:)'
source_url: 'https://developer.apple.com/documentation/avfoundation/avcaptureindexpicker/init(_:symbolname:numberofindexes:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avcaptureindexpicker/init%28_%3Asymbolname%3Anumberofindexes%3A%29.json'
content_hash: 'sha256:5de0c8a7f45bd4c9'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVCaptureIndexPicker](../avcaptureindexpicker.md)

# init(_:symbolName:numberOfIndexes:)

<sub>Initializer</sub>

Creates a control to pick a value from the specified number of indexes.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS</sub>

```swift
init(_ localizedTitle: String, symbolName: String, numberOfIndexes: Int)
```

## Parameters

- `localizedTitle` — A localized title that describes the picker’s action.

- `symbolName` — The name of the symbol from the SF Symbols library to use to represent this control.

- `numberOfIndexes` — The number of indexes to pick between. This value must be greater than `0`.

## Discussion

Create a picker with this initializer when the control’s values don’t require titles.

## See Also

### Creating an index picker

- [- initWithLocalizedTitle:symbolName:numberOfIndexes:localizedTitleTransform:](<init(__symbolname_numberofindexes_localizedtitletransform_).md>) — Creates a control to pick a value from the specified number of indices.
- [- initWithLocalizedTitle:symbolName:localizedIndexTitles:](<init(__symbolname_localizedindextitles_).md>) — Creates an object to select an index from a set of values.
