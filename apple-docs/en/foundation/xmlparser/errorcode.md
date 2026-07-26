---
title: XMLParser.ErrorCode
framework: Foundation
symbol_kind: enum
role: symbol
role_heading: Enumeration
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.0+, macOS 10.0+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/xmlparser/errorcode
source_url: 'https://developer.apple.com/documentation/foundation/xmlparser/errorcode'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/xmlparser/errorcode.json'
content_hash: 'sha256:f01654d04a525f3c'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [XMLParser](../xmlparser.md)

# XMLParser.ErrorCode

<sub>Enumeration</sub>

The following error codes are defined by `NSXMLParser`. For error codes not listed here, see the `<libxml/xmlerror.h>` header file.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
enum ErrorCode
```

## Relationships

- **Conforms To**: [BitwiseCopyable](../../swift/bitwisecopyable.md), [Equatable](../../swift/equatable.md), [Hashable](../../swift/hashable.md), [RawRepresentable](../../swift/rawrepresentable.md), [Sendable](../../swift/sendable.md), [SendableMetatype](../../swift/sendablemetatype.md)

## Topics

### Constants

- [NSXMLParserInternalError](errorcode/internalerror.md) — The parser object encountered an internal error.
- [NSXMLParserOutOfMemoryError](errorcode/outofmemoryerror.md) — The parser object ran out of memory.
- [NSXMLParserDocumentStartError](errorcode/documentstarterror.md) — The parser object is unable to start parsing.
- [NSXMLParserEmptyDocumentError](errorcode/emptydocumenterror.md) — The document is empty.
- [NSXMLParserPrematureDocumentEndError](errorcode/prematuredocumentenderror.md) — The document ended unexpectedly.
- [NSXMLParserInvalidHexCharacterRefError](errorcode/invalidhexcharacterreferror.md) — Invalid hexadecimal character reference encountered.
- [NSXMLParserInvalidDecimalCharacterRefError](errorcode/invaliddecimalcharacterreferror.md) — Invalid decimal character reference encountered.
- [NSXMLParserInvalidCharacterRefError](errorcode/invalidcharacterreferror.md) — Invalid character reference encountered.
- [NSXMLParserInvalidCharacterError](errorcode/invalidcharactererror.md) — Invalid character encountered.
- [NSXMLParserCharacterRefAtEOFError](errorcode/characterrefateoferror.md) — Target of character reference cannot be found.
- [NSXMLParserCharacterRefInPrologError](errorcode/characterrefinprologerror.md) — Invalid character found in the prolog.
- [NSXMLParserCharacterRefInEpilogError](errorcode/characterrefinepilogerror.md) — Invalid character found in the epilog.
- [NSXMLParserCharacterRefInDTDError](errorcode/characterrefindtderror.md) — Invalid character encountered in the DTD.
- [NSXMLParserEntityRefAtEOFError](errorcode/entityrefateoferror.md) — Target of entity reference is not found.
- [NSXMLParserEntityRefInPrologError](errorcode/entityrefinprologerror.md) — Invalid entity reference found in the prolog.
- [NSXMLParserEntityRefInEpilogError](errorcode/entityrefinepilogerror.md) — Invalid entity reference found in the epilog.
- [NSXMLParserEntityRefInDTDError](errorcode/entityrefindtderror.md) — Invalid entity reference found in the DTD.
- [NSXMLParserParsedEntityRefAtEOFError](errorcode/parsedentityrefateoferror.md) — Target of parsed entity reference is not found.
- [NSXMLParserParsedEntityRefInPrologError](errorcode/parsedentityrefinprologerror.md) — Target of parsed entity reference is not found in prolog.
- [NSXMLParserParsedEntityRefInEpilogError](errorcode/parsedentityrefinepilogerror.md) — Target of parsed entity reference is not found in epilog.
- [NSXMLParserParsedEntityRefInInternalSubsetError](errorcode/parsedentityrefininternalsubseterror.md) — Target of parsed entity reference is not found in internal subset.
- [NSXMLParserEntityReferenceWithoutNameError](errorcode/entityreferencewithoutnameerror.md) — Entity reference is without name.
- [NSXMLParserEntityReferenceMissingSemiError](errorcode/entityreferencemissingsemierror.md) — Entity reference is missing semicolon.
- [NSXMLParserParsedEntityRefNoNameError](errorcode/parsedentityrefnonameerror.md) — Parsed entity reference is without an entity name.
- [NSXMLParserParsedEntityRefMissingSemiError](errorcode/parsedentityrefmissingsemierror.md) — Parsed entity reference is missing semicolon.
- [NSXMLParserUndeclaredEntityError](errorcode/undeclaredentityerror.md) — Entity is not declared.
- [NSXMLParserUnparsedEntityError](errorcode/unparsedentityerror.md) — Cannot parse entity.
- [NSXMLParserEntityIsExternalError](errorcode/entityisexternalerror.md) — Cannot parse external entity.
- [NSXMLParserEntityIsParameterError](errorcode/entityisparametererror.md) — Entity is a parameter.
- [NSXMLParserUnknownEncodingError](errorcode/unknownencodingerror.md) — Document encoding is unknown.
- [NSXMLParserEncodingNotSupportedError](errorcode/encodingnotsupportederror.md) — Document encoding is not supported.
- [NSXMLParserStringNotStartedError](errorcode/stringnotstartederror.md) — String is not started.
- [NSXMLParserStringNotClosedError](errorcode/stringnotclosederror.md) — String is not closed.
- [NSXMLParserNamespaceDeclarationError](errorcode/namespacedeclarationerror.md) — Invalid namespace declaration encountered.
- [NSXMLParserEntityNotStartedError](errorcode/entitynotstartederror.md) — Entity is not started.
- [NSXMLParserEntityNotFinishedError](errorcode/entitynotfinishederror.md) — Entity is not finished.
- [NSXMLParserLessThanSymbolInAttributeError](errorcode/lessthansymbolinattributeerror.md) — Angle bracket is used in attribute.
- [NSXMLParserAttributeNotStartedError](errorcode/attributenotstartederror.md) — Attribute is not started.
- [NSXMLParserAttributeNotFinishedError](errorcode/attributenotfinishederror.md) — Attribute is not finished.
- [NSXMLParserAttributeHasNoValueError](errorcode/attributehasnovalueerror.md) — Attribute doesn’t contain a value.
- [NSXMLParserAttributeRedefinedError](errorcode/attributeredefinederror.md) — Attribute is redefined.
- [NSXMLParserLiteralNotStartedError](errorcode/literalnotstartederror.md) — Literal is not started.
- [NSXMLParserLiteralNotFinishedError](errorcode/literalnotfinishederror.md) — Literal is not finished.
- [NSXMLParserCommentNotFinishedError](errorcode/commentnotfinishederror.md) — Comment is not finished.
- [NSXMLParserProcessingInstructionNotStartedError](errorcode/processinginstructionnotstartederror.md) — Processing instruction is not started.
- [NSXMLParserProcessingInstructionNotFinishedError](errorcode/processinginstructionnotfinishederror.md) — Processing instruction is not finished.
- [NSXMLParserNotationNotStartedError](errorcode/notationnotstartederror.md) — Notation is not started.
- [NSXMLParserNotationNotFinishedError](errorcode/notationnotfinishederror.md) — Notation is not finished.
- [NSXMLParserAttributeListNotStartedError](errorcode/attributelistnotstartederror.md) — Attribute list is not started.
- [NSXMLParserAttributeListNotFinishedError](errorcode/attributelistnotfinishederror.md) — Attribute list is not finished.
- [NSXMLParserMixedContentDeclNotStartedError](errorcode/mixedcontentdeclnotstartederror.md) — Mixed content declaration is not started.
- [NSXMLParserMixedContentDeclNotFinishedError](errorcode/mixedcontentdeclnotfinishederror.md) — Mixed content declaration is not finished.
- [NSXMLParserElementContentDeclNotStartedError](errorcode/elementcontentdeclnotstartederror.md) — Element content declaration is not started.
- [NSXMLParserElementContentDeclNotFinishedError](errorcode/elementcontentdeclnotfinishederror.md) — Element content declaration is not finished.
- [NSXMLParserXMLDeclNotStartedError](errorcode/xmldeclnotstartederror.md) — XML declaration is not started.
- [NSXMLParserXMLDeclNotFinishedError](errorcode/xmldeclnotfinishederror.md) — XML declaration is not finished.
- [NSXMLParserConditionalSectionNotStartedError](errorcode/conditionalsectionnotstartederror.md) — Conditional section is not started.
- [NSXMLParserConditionalSectionNotFinishedError](errorcode/conditionalsectionnotfinishederror.md) — Conditional section is not finished.
- [NSXMLParserExternalSubsetNotFinishedError](errorcode/externalsubsetnotfinishederror.md) — External subset is not finished.
- [NSXMLParserDOCTYPEDeclNotFinishedError](errorcode/doctypedeclnotfinishederror.md) — Document type declaration is not finished.
- [NSXMLParserMisplacedCDATAEndStringError](errorcode/misplacedcdataendstringerror.md) — Misplaced CDATA end string.
- [NSXMLParserCDATANotFinishedError](errorcode/cdatanotfinishederror.md) — CDATA block is not finished.
- [NSXMLParserMisplacedXMLDeclarationError](errorcode/misplacedxmldeclarationerror.md) — Misplaced XML declaration.
- [NSXMLParserSpaceRequiredError](errorcode/spacerequirederror.md) — Space is required.
- [NSXMLParserSeparatorRequiredError](errorcode/separatorrequirederror.md) — Separator is required.
- [NSXMLParserNMTOKENRequiredError](errorcode/nmtokenrequirederror.md) — Name token is required.
- [NSXMLParserNAMERequiredError](errorcode/namerequirederror.md) — Name is required.
- [NSXMLParserPCDATARequiredError](errorcode/pcdatarequirederror.md) — CDATA is required.
- [NSXMLParserURIRequiredError](errorcode/urirequirederror.md) — URI is required.
- [NSXMLParserPublicIdentifierRequiredError](errorcode/publicidentifierrequirederror.md) — Public identifier is required.
- [NSXMLParserLTRequiredError](errorcode/ltrequirederror.md) — Left angle bracket is required.
- [NSXMLParserGTRequiredError](errorcode/gtrequirederror.md) — Right angle bracket is required.
- [NSXMLParserLTSlashRequiredError](errorcode/ltslashrequirederror.md) — Left angle bracket slash is required.
- [NSXMLParserEqualExpectedError](errorcode/equalexpectederror.md) — Equal sign expected.
- [NSXMLParserTagNameMismatchError](errorcode/tagnamemismatcherror.md) — Tag name mismatch.
- [NSXMLParserUnfinishedTagError](errorcode/unfinishedtagerror.md) — Unfinished tag found.
- [NSXMLParserStandaloneValueError](errorcode/standalonevalueerror.md) — Standalone value found.
- [NSXMLParserInvalidEncodingNameError](errorcode/invalidencodingnameerror.md) — Invalid encoding name found.
- [NSXMLParserCommentContainsDoubleHyphenError](errorcode/commentcontainsdoublehyphenerror.md) — Comment contains double hyphen.
- [NSXMLParserInvalidEncodingError](errorcode/invalidencodingerror.md) — Invalid encoding.
- [NSXMLParserExternalStandaloneEntityError](errorcode/externalstandaloneentityerror.md) — External standalone entity.
- [NSXMLParserInvalidConditionalSectionError](errorcode/invalidconditionalsectionerror.md) — Invalid conditional section.
- [NSXMLParserEntityValueRequiredError](errorcode/entityvaluerequirederror.md) — Entity value is required.
- [NSXMLParserNotWellBalancedError](errorcode/notwellbalancederror.md) — Document is not well balanced.
- [NSXMLParserExtraContentError](errorcode/extracontenterror.md) — Error in content found.
- [NSXMLParserInvalidCharacterInEntityError](errorcode/invalidcharacterinentityerror.md) — Invalid character in entity found.
- [NSXMLParserParsedEntityRefInInternalError](errorcode/parsedentityrefininternalerror.md) — Internal error in parsed entity reference found.
- [NSXMLParserEntityRefLoopError](errorcode/entityreflooperror.md) — Entity reference loop encountered.
- [NSXMLParserEntityBoundaryError](errorcode/entityboundaryerror.md) — Entity boundary error.
- [NSXMLParserInvalidURIError](errorcode/invalidurierror.md) — Invalid URI specified.
- [NSXMLParserURIFragmentError](errorcode/urifragmenterror.md) — URI fragment.
- [NSXMLParserNoDTDError](errorcode/nodtderror.md) — Missing DTD.
- [NSXMLParserDelegateAbortedParseError](errorcode/delegateabortedparseerror.md) — Delegate aborted parse.

### Initializers

- [init(rawValue:)](<errorcode/init(rawvalue_).md>)

## See Also

### Constants

- [ExternalEntityResolvingPolicy](externalentityresolvingpolicy-swift.enum.md) — Defines the external entity resolving policy used by an `NSXMLParser` instance.
- [NSXMLParserErrorDomain](errordomain.md) — Indicates an error in XML parsing.
