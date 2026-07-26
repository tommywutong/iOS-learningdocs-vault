---
title: Foundation Data Types
framework: Foundation
symbol_kind: article
role: collectionGroup
role_heading: API Collection
platforms: []
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/foundation-data-types
source_url: 'https://developer.apple.com/documentation/foundation/foundation-data-types'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/foundation-data-types.json'
content_hash: 'sha256:8fbbbc7fc83b98d9'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Foundation](../foundation.md)

# Foundation Data Types

<sub>API Collection</sub>

This document describes the data types and constants found in the Foundation framework.

## Topics

### Classes

- [NSKeyValueObservation](nskeyvalueobservation.md)
- [NSKeyValueSharedObservers](nskeyvaluesharedobservers.md) — A collection of key-value observations which may be registered with multiple observable objects
- [NSKeyValueSharedObserversSnapshot](nskeyvaluesharedobserverssnapshot.md) — A collection of key-value observations which may be registered with multiple observable objects. Create using `-[NSKeyValueSharedObservers snapshot]`

### Protocols

- [DiscreteFormatStyle](discreteformatstyle.md) — A format style that transforms a continuous input into a discrete output and provides information about its discretization boundaries.
- [NSKeyValueObservingCustomization](nskeyvalueobservingcustomization.md) — Conforming to NSKeyValueObservingCustomization is not required to use Key-Value Observing. Provide an implementation of these functions if you need to disable auto-notifying for a key, or add dependent keys

### Structures

- [AsyncCharacterSequence](asynccharactersequence.md) — An asynchronous sequence of characters.
- [AsyncLineSequence](asynclinesequence.md) — An asynchronous sequence of lines of text.
- [AsyncUnicodeScalarSequence](asyncunicodescalarsequence.md) — An asychronous sequence of Unicode scalar values.
- [Expression](expression.md)
- [NSAttributedStringFormattingContextKey](nsattributedstringformattingcontextkey.md) — A type that represents a key in the formatting context dictionary.
- [NSKeyValueChangeKey](nskeyvaluechangekey.md) — The keys that can appear in the change dictionary.
- [NSKeyValueObservedChange](nskeyvalueobservedchange.md)
- [NSKeyValueOperator](nskeyvalueoperator.md) — These constants define the available array operators. See [Using Collection Operators](https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/KeyValueCoding/CollectionOperators.html) for more information.
- [PresentationIntent](presentationintent.md) — A type that defines presentation intent for blocks of characters like paragraphs, lists, block quotes, and tables.

### Variables

- [NSOperationNotSupportedForKeyException](nsoperationnotsupportedforkeyexception.md)
- [NSURLSessionUploadTaskResumeData](nsurlsessionuploadtaskresumedata.md) — Key in the userInfo dictionary of an NSError received during a failed upload.
- [kCFStringEncodingASCII](kcfstringencodingascii.md)

### Macros

- [Expression(_:)](<expression(__).md>)
- [Predicate(_:)](<predicate(__).md>)

### Type Aliases

- [uuid_string_t](uuid_string_t.md)
- [uuid_t](uuid_t.md)

## See Also

### Reference

- [Foundation Enumerations](foundation-enumerations.md)
