---
title: Error Dictionary Keys
framework: Core Foundation
symbol_kind: article
role: collectionGroup
role_heading: API Collection
platforms: []
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/corefoundation/error-dictionary-keys
source_url: 'https://developer.apple.com/documentation/corefoundation/error-dictionary-keys'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/corefoundation/error-dictionary-keys.json'
content_hash: 'sha256:c7e1326420add80f'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Foundation](../corefoundation.md) · [CFXMLTree](cfxmltree.md)

# Error Dictionary Keys

<sub>API Collection</sub>

The keys used in an error dictionary returned by some functions to provide more information about XML parse errors.

## Overview

These keys are used in the error dictionary returned by the [CFXMLTreeCreateFromDataWithError](cfxmltreecreatefromdatawitherror.md) function.

## Topics

### Constants

- [kCFXMLTreeErrorDescription](kcfxmltreeerrordescription.md) — Dictionary key whose value is a CFString containing a readable description of the error.
- [kCFXMLTreeErrorLineNumber](kcfxmltreeerrorlinenumber.md) — Dictionary key whose value is a CFNumber containing the line number where the error was detected. This may not be the line number where the actual XML error is located.
- [kCFXMLTreeErrorLocation](kcfxmltreeerrorlocation.md) — Dictionary key whose value is a CFNumber containing the byte location where the error was detected.
- [kCFXMLTreeErrorStatusCode](kcfxmltreeerrorstatuscode.md) — Dictionary key whose value is a CFNumber containing the error status code. See [CFXMLParser](cfxmlparser.md) for possible status code values.
