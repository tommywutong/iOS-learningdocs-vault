---
title: CFXMLParserStatusCode
framework: Core Foundation
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [macOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/corefoundation/cfxmlparserstatuscode
source_url: 'https://developer.apple.com/documentation/corefoundation/cfxmlparserstatuscode'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/corefoundation/cfxmlparserstatuscode.json'
content_hash: 'sha256:2c0bacd698c79b62'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Foundation](../corefoundation.md)

# CFXMLParserStatusCode

<sub>Structure</sub>

The various status and error flags that can be returned by the parser.

<sub>macOS</sub>

```swift
struct CFXMLParserStatusCode
```

## Overview

Parser status is determined by calling the [CFXMLParserGetStatusCode](cfxmlparsergetstatuscode.md) function. The parser reports errors to your application by invoking the [CFXMLParserHandleErrorCallBack](cfxmlparserhandleerrorcallback.md) function.

## Relationships

- **Conforms To**: [BitwiseCopyable](../swift/bitwisecopyable.md), [Equatable](../swift/equatable.md), [ExpressibleByArrayLiteral](../swift/expressiblebyarrayliteral.md), [OptionSet](../swift/optionset.md), [RawRepresentable](../swift/rawrepresentable.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md), [SetAlgebra](../swift/setalgebra.md)

## Topics

### Constants

- [kCFXMLStatusParseNotBegun](cfxmlparserstatuscode/statusparsenotbegun.md) — Indicates the parser has not begun.
- [kCFXMLStatusParseInProgress](cfxmlparserstatuscode/statusparseinprogress.md) — Indicates the parser is in progress.
- [kCFXMLErrorUnexpectedEOF](cfxmlparserstatuscode/errorunexpectedeof.md) — Indicates an unexpected EOF occurred.
- [kCFXMLErrorUnknownEncoding](cfxmlparserstatuscode/errorunknownencoding.md) — Indicates an unknown encoding error.
- [kCFXMLErrorEncodingConversionFailure](cfxmlparserstatuscode/errorencodingconversionfailure.md) — Indicates an encoding conversion error.
- [kCFXMLErrorMalformedProcessingInstruction](cfxmlparserstatuscode/errormalformedprocessinginstruction.md) — Indicates a malformed processing instruction.
- [kCFXMLErrorMalformedDTD](cfxmlparserstatuscode/errormalformeddtd.md) — Indicates a malformed DTD.
- [kCFXMLErrorMalformedName](cfxmlparserstatuscode/errormalformedname.md) — Indicates a malformed name.
- [kCFXMLErrorMalformedCDSect](cfxmlparserstatuscode/errormalformedcdsect.md) — Indicates a malformed CDATA section.
- [kCFXMLErrorMalformedCloseTag](cfxmlparserstatuscode/errormalformedclosetag.md) — Indicates a malformed close tag.
- [kCFXMLErrorMalformedStartTag](cfxmlparserstatuscode/errormalformedstarttag.md) — Indicates a malformed start tag.
- [kCFXMLErrorMalformedDocument](cfxmlparserstatuscode/errormalformeddocument.md) — Indicates a malformed document.
- [kCFXMLErrorElementlessDocument](cfxmlparserstatuscode/errorelementlessdocument.md) — Indicates a document containing no elements.
- [kCFXMLErrorMalformedComment](cfxmlparserstatuscode/errormalformedcomment.md) — Indicates a malformed comment.
- [kCFXMLErrorMalformedCharacterReference](cfxmlparserstatuscode/errormalformedcharacterreference.md) — Indicates a malformed character reference.
- [kCFXMLErrorMalformedParsedCharacterData](cfxmlparserstatuscode/errormalformedparsedcharacterdata.md) — Indicates malformed character data.
- [kCFXMLErrorNoData](cfxmlparserstatuscode/errornodata.md) — Indicates a no data error.

### Initializers

- [init(rawValue:)](<cfxmlparserstatuscode/init(rawvalue_).md>)

## See Also

### Constants

- [CFXMLParserOptions](cfxmlparseroptions.md) — Options you can use to control the parser’s treatment of an XML document.
