---
title: 'init(payload:isCompact:rowCount:columnCount:)'
framework: Core Image
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 11.0+, iPadOS 11.0+, Mac Catalyst 13.1+, macOS 10.13+, tvOS 11.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/coreimage/cipdf417codedescriptor/init(payload:iscompact:rowcount:columncount:)'
source_url: 'https://developer.apple.com/documentation/coreimage/cipdf417codedescriptor/init(payload:iscompact:rowcount:columncount:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coreimage/cipdf417codedescriptor/init%28payload%3Aiscompact%3Arowcount%3Acolumncount%3A%29.json'
content_hash: 'sha256:3c52cf8b7f19732b'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Image](../../coreimage.md) · [CIPDF417CodeDescriptor](../cipdf417codedescriptor.md)

# init(payload:isCompact:rowCount:columnCount:)

<sub>Initializer</sub>

Initializes an PDF417 code descriptor for the given payload and parameters.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
init?(payload errorCorrectedPayload: Data, isCompact: Bool, rowCount: Int, columnCount: Int)
```

## Parameters

- `errorCorrectedPayload` — The data to encode in the PDF417 code symbol.

- `isCompact` — A Boolean indicating whether or not the PDF417 code is compact.

- `rowCount` — The number of rows in the PDF417 code, from 3 to 90.

- `columnCount` — The number of columns in the Aztec code, from 1 to 30.

## Return Value

An initialized [CIPDF417CodeDescriptor](../cipdf417codedescriptor.md) instance or `nil` if the parameters are invalid
