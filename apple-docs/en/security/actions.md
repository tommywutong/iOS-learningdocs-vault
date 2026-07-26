---
title: Actions
framework: Security
symbol_kind: article
role: collectionGroup
role_heading: API Collection
platforms: []
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/security/actions
source_url: 'https://developer.apple.com/documentation/security/actions'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/security/actions.json'
content_hash: 'sha256:5b65ea33148c2bd5'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Security](../security.md) · [Security Transforms](security-transforms.md)

# Actions

<sub>API Collection</sub>

Use actions to trigger particular behaviors.

## Topics

### Constants

- [kSecTransformActionAttributeNotification](ksectransformactionattributenotification.md) — An action that triggers when an attribute is set. _(deprecated)_
- [kSecTransformActionAttributeValidation](ksectransformactionattributevalidation.md) — An action that triggers to perform validation of an attribute. _(deprecated)_
- [kSecTransformActionCanExecute](ksectransformactioncanexecute.md) — An action that triggers to verify that all required attributes are either set or connected to another transform. _(deprecated)_
- [kSecTransformActionExternalizeExtraData](ksectransformactionexternalizeextradata.md) — An action that triggers after data is stored. _(deprecated)_
- [kSecTransformActionFinalize](ksectransformactionfinalize.md) — An action that triggers just before deleting a custom transform to enable custom cleanup operations. _(deprecated)_
- [kSecTransformActionInternalizeExtraData](ksectransformactioninternalizeextradata.md) — An action that triggers after attributes are read into a transform. _(deprecated)_
- [kSecTransformActionProcessData](ksectransformactionprocessdata.md) — An action that triggers to process the data of an attribute. _(deprecated)_
- [kSecTransformActionStartingExecution](ksectransformactionstartingexecution.md) — An action that triggers just before starting execution of a custom transform. _(deprecated)_
