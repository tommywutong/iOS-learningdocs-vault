---
title: 'init(contentEditingInput:)'
framework: Photos
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.1+, macOS 10.11+, tvOS 10.0+, visionOS 1.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/photos/phcontenteditingoutput/init(contenteditinginput:)'
source_url: 'https://developer.apple.com/documentation/photos/phcontenteditingoutput/init(contenteditinginput:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/photos/phcontenteditingoutput/init%28contenteditinginput%3A%29.json'
content_hash: 'sha256:c173935c64f4329f'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Photos](../../photos.md) · [PHContentEditingOutput](../phcontenteditingoutput.md)

# init(contentEditingInput:)

<sub>Initializer</sub>

Creates an editing output from the specified editing input.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
init(contentEditingInput: PHContentEditingInput)
```

## Parameters

- `contentEditingInput` — An object providing information about the asset to be edited.

## Return Value

An initialized content editing output.

## Discussion

To complete the edit, use the [renderedContentURL](renderedcontenturl.md) property to provide the edited asset content. Then, use the [PHAssetChangeRequest](../phassetchangerequest.md) class or [PHContentEditingController](../../photosui/phcontenteditingcontroller.md) protocol to commit the edit to storage.
