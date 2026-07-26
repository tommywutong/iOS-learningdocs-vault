---
title: 'saveOptions(_:shouldShowUTType:)'
framework: Objective-C Runtime
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [macOS 10.6+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/objectivec/nsobject-swift.class/saveoptions(_:shouldshowuttype:)'
source_url: 'https://developer.apple.com/documentation/objectivec/nsobject-swift.class/saveoptions(_:shouldshowuttype:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/objectivec/nsobject-swift.class/saveoptions%28_%3Ashouldshowuttype%3A%29.json'
content_hash: 'sha256:0e97f28718b39b66'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Objective-C Runtime](../../objectivec.md) · [NSObject](../nsobject-swift.class.md)

# saveOptions(_:shouldShowUTType:)

<sub>Instance Method</sub>

Called to determine if the specified uniform type identifier should be shown in the save panel.

<sub>macOS</sub>

```swift
func saveOptions(_ saveOptions: IKSaveOptions!, shouldShowUTType utType: String!) -> Bool
```

## Parameters

- `saveOptions` — The `IKSaveOptions` instance that called the delegate.

- `utType` — The uniform type identifier to test.

## Return Value

[YES](../yes.md) if the specified type should be shown in the save options, otherwise [NO](../no.md).
