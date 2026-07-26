---
title: Keys for Items Accessed in JavaScript Code
framework: Foundation
symbol_kind: article
role: collectionGroup
role_heading: API Collection
platforms: []
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/keys-for-items-accessed-in-javascript-code
source_url: 'https://developer.apple.com/documentation/foundation/keys-for-items-accessed-in-javascript-code'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/keys-for-items-accessed-in-javascript-code.json'
content_hash: 'sha256:07de97cfb42c88fb'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Foundation](../foundation.md) · [App Extension Support](app-extension-support.md) · [NSItemProvider](nsitemprovider.md)

# Keys for Items Accessed in JavaScript Code

<sub>API Collection</sub>

Keys in property list items that the system recieves from or sends to JavaScript code.

## Topics

### Constants

- [NSExtensionJavaScriptPreprocessingResultsKey](nsextensionjavascriptpreprocessingresultskey.md) — A key whose value is an item of type `kUTTypePropertyList`. The item contains an `NSDictionary` that contains the object returned by the JavaScript code to its completion function.
- [NSExtensionJavaScriptFinalizeArgumentKey](nsextensionjavascriptfinalizeargumentkey.md) — A key whose value is an item of type `kUTTypePropertyList`. The item contains an `NSDictionary` that contains the arguments to be passed to a JavaScript finalize method.

## See Also

### Constants

- [CompletionHandler](nsitemprovider/completionhandler.md) — A block that receives the item provider’s data.
- [LoadHandler](nsitemprovider/loadhandler.md) — A block that loads the item provider’s data and coerces it to the specified type.
- [Options Dictionary Key](options-dictionary-key.md) — Keys indicating options to use when generating the item provider’s data.
- [NSItemProviderErrorDomain](nsitemprovider/errordomain.md) — The error domain associated with the item provider.
- [NSItemProviderFileOptions](nsitemproviderfileoptions.md) — Data-access specifications that declare how to handle items.
- [NSItemProviderReading](nsitemproviderreading.md) — The protocol for implementing a class to allow an item provider to create an instance of the class.
- [NSItemProviderWriting](nsitemproviderwriting.md) — The protocol for implementing a class to allow an item provider to retrieve data from an instance of the class.
- [NSItemProviderRepresentationVisibility](nsitemproviderrepresentationvisibility.md) — Specifications that control which categories of processes can see an item.
- [ErrorCode](nsitemprovider/errorcode.md) — The error codes that describe problems with consuming data from an item provider.
