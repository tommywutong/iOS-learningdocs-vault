---
title: Sessions API Result Codes
framework: Security
symbol_kind: article
role: collectionGroup
role_heading: API Collection
platforms: []
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/security/sessions-api-result-codes
source_url: 'https://developer.apple.com/documentation/security/sessions-api-result-codes'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/security/sessions-api-result-codes.json'
content_hash: 'sha256:422e95008db5bb10'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Security](../security.md) · [Sessions](sessions.md)

# Sessions API Result Codes

<sub>API Collection</sub>

Recognize result codes specific to the sessions API.

## Discussion

Use the [SecCopyErrorMessageString](<seccopyerrormessagestring(____).md>) function to obtain a human readable string corresponding to these status codes.

The functions of the sessions API may also return result codes from the authorization services API listed in [Authorization Services Result Codes](authorization-services-result-codes.md) or the general codes listed in [Security Framework Result Codes](security-framework-result-codes.md).

## Topics

### Codes

- [errSessionSuccess](errsessionsuccess.md) — The operation completed successfully.
- [errSessionInvalidId](errsessioninvalidid.md) — Detected an invalid session ID.
- [errSessionInvalidAttributes](errsessioninvalidattributes.md) — Detected an invalid set of request attribute bits.
- [errSessionAuthorizationDenied](errsessionauthorizationdenied.md) — Authorization denied.
- [errSessionValueNotSet](errsessionvaluenotset.md) — The requested session attribute has not been set.
- [errSessionInternal](errsessioninternal.md) — An unrecognized internal error occurred.
- [errSessionInvalidFlags](errsessioninvalidflags.md) — Encountered invalid flags or options.
