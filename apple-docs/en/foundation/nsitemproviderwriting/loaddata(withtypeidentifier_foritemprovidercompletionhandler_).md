---
title: 'loadData(withTypeIdentifier:forItemProviderCompletionHandler:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 11.0+, iPadOS 11.0+, Mac Catalyst 13.1+, macOS 10.13+, tvOS 11.0+, visionOS 1.0+, watchOS 4.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/nsitemproviderwriting/loaddata(withtypeidentifier:foritemprovidercompletionhandler:)'
source_url: 'https://developer.apple.com/documentation/foundation/nsitemproviderwriting/loaddata(withtypeidentifier:foritemprovidercompletionhandler:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsitemproviderwriting/loaddata%28withtypeidentifier%3Aforitemprovidercompletionhandler%3A%29.json'
content_hash: 'sha256:41822792504d513c'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSItemProviderWriting](../nsitemproviderwriting.md)

# loadData(withTypeIdentifier:forItemProviderCompletionHandler:)

<sub>Instance Method</sub>

Loads data of a particular type, identified by the given UTI.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func loadData(withTypeIdentifier typeIdentifier: String, forItemProviderCompletionHandler completionHandler: @escaping @Sendable (Data?, (any Error)?) -> Void) -> Progress?
```

## Parameters

- `typeIdentifier` — The uniform type identifier (UTI) identifying the type of data to load.

- `completionHandler` — The handler that’s called after the data is loaded.

## Return Value

The progress of the data load process.

## Discussion

When the system calls this method, the `typeIdentifier` parameter is set to one of the elements in the `writableTypeIdentifiersForItemProvider` array.
