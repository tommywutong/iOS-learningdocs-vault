---
title: NSCharacterEncodingDocumentOption
framework: UIKit
symbol_kind: var
role: symbol
role_heading: Global Variable
platforms: [iOS 6.0+, iPadOS 6.0+, Mac Catalyst 13.1+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/nscharacterencodingdocumentoption
source_url: 'https://developer.apple.com/documentation/uikit/nscharacterencodingdocumentoption'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/nscharacterencodingdocumentoption.json'
content_hash: 'sha256:9fe2abd0ca15bf0f'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [UIKit](../uikit.md)

# NSCharacterEncodingDocumentOption

<sub>Global Variable</sub>

The string encoding.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS</sub>

```objc
extern NSAttributedStringDocumentReadingOptionKey const NSCharacterEncodingDocumentOption;
```

## Overview

For plain text documents; [NSNumber](../foundation/nsnumber.md) containing the unsigned int [NSStringEncoding](../foundation/nsstringencoding.md) to override any encoding specified in an HTML document. The previous string constant was `@"CharacterEncoding"`.

## See Also

### Getting the document options

- [NSDefaultAttributesDocumentOption](nsdefaultattributesdocumentoption.md)
- [NSDocumentTypeDocumentOption](nsdocumenttypedocumentoption.md) — The document type.
