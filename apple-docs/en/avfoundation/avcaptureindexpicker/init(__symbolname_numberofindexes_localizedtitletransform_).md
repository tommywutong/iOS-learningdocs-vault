---
title: 'init(_:symbolName:numberOfIndexes:localizedTitleTransform:)'
framework: AVFoundation
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 18.0+, iPadOS 18.0+, Mac Catalyst 18.0+, macOS 15.0+, tvOS 18.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/avfoundation/avcaptureindexpicker/init(_:symbolname:numberofindexes:localizedtitletransform:)'
source_url: 'https://developer.apple.com/documentation/avfoundation/avcaptureindexpicker/init(_:symbolname:numberofindexes:localizedtitletransform:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avcaptureindexpicker/init%28_%3Asymbolname%3Anumberofindexes%3Alocalizedtitletransform%3A%29.json'
content_hash: 'sha256:59c70631f47b9ce9'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVCaptureIndexPicker](../avcaptureindexpicker.md)

# init(_:symbolName:numberOfIndexes:localizedTitleTransform:)

<sub>Initializer</sub>

Creates a control to pick a value from the specified number of indices.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS</sub>

```swift
init(_ localizedTitle: String, symbolName: String, numberOfIndexes: Int, localizedTitleTransform: (Int) -> String)
```

## Parameters

- `localizedTitle` — A localized title that describes the picker’s action.

- `symbolName` — The name of the symbol from the SF Symbols library to use to represent this control.

- `numberOfIndexes` — The number of indexes to pick between. This value must be greater than `0`.

- `localizedTitleTransform` — A transformation from index to localized title.

## Discussion

Create a picker with this initializer if your app requires specifying a title for each value lazily.

## See Also

### Creating an index picker

- [- initWithLocalizedTitle:symbolName:numberOfIndexes:](<init(__symbolname_numberofindexes_).md>) — Creates a control to pick a value from the specified number of indexes.
- [- initWithLocalizedTitle:symbolName:localizedIndexTitles:](<init(__symbolname_localizedindextitles_).md>) — Creates an object to select an index from a set of values.
