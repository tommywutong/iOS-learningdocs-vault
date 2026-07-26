---
title: 'init(_:symbolName:localizedIndexTitles:)'
framework: AVFoundation
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 18.0+, iPadOS 18.0+, Mac Catalyst 18.0+, macOS 15.0+, tvOS 18.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/avfoundation/avcaptureindexpicker/init(_:symbolname:localizedindextitles:)'
source_url: 'https://developer.apple.com/documentation/avfoundation/avcaptureindexpicker/init(_:symbolname:localizedindextitles:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avcaptureindexpicker/init%28_%3Asymbolname%3Alocalizedindextitles%3A%29.json'
content_hash: 'sha256:7f658465769c271a'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVCaptureIndexPicker](../avcaptureindexpicker.md)

# init(_:symbolName:localizedIndexTitles:)

<sub>Initializer</sub>

Creates an object to select an index from a set of values.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS</sub>

```swift
init(_ localizedTitle: String, symbolName: String, localizedIndexTitles: [String])
```

## Parameters

- `localizedTitle` — A localized title that describes the control’s action.

- `symbolName` — The name of an SF Symbol that represents the control.

- `localizedIndexTitles` — The titles to use for each index. The array must not be empty.

## Discussion

Create a picker with this initializer when you already have an array containing a title for each picked value.

## See Also

### Creating an index picker

- [- initWithLocalizedTitle:symbolName:numberOfIndexes:](<init(__symbolname_numberofindexes_).md>) — Creates a control to pick a value from the specified number of indexes.
- [- initWithLocalizedTitle:symbolName:numberOfIndexes:localizedTitleTransform:](<init(__symbolname_numberofindexes_localizedtitletransform_).md>) — Creates a control to pick a value from the specified number of indices.
