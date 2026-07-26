---
title: NSNetServices Errors
framework: Foundation
symbol_kind: article
role: collectionGroup
role_heading: API Collection
platforms: []
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/nsnetservices-errors
source_url: 'https://developer.apple.com/documentation/foundation/nsnetservices-errors'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsnetservices-errors.json'
content_hash: 'sha256:f7567601210669ad'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Foundation](../foundation.md) · [Bonjour](bonjour.md) · [NetService](netservice.md)

# NSNetServices Errors

<sub>API Collection</sub>

If an error occurs, the delegate error-handling methods return a dictionary with the following keys.

## Topics

### Constants

- [NSNetServicesErrorCode](netservice/errorcode-swift.type.property.md) — This key identifies the error that occurred during the most recent operation.
- [NSNetServicesErrorDomain](netservice/errordomain.md) — This key identifies the originator of the error, which is either the `NSNetService` object or the mach network layer. For most errors, you should not need the value provided by this key.

## See Also

### Constants

- [ErrorCode](netservice/errorcode-swift.enum.md) — These constants identify errors that can occur when accessing net services.
- [Options](netservice/options.md) — These constants specify options for a network service.
