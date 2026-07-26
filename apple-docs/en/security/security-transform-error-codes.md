---
title: Security Transform Error Codes
framework: Security
symbol_kind: article
role: collectionGroup
role_heading: API Collection
platforms: []
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/security/security-transform-error-codes
source_url: 'https://developer.apple.com/documentation/security/security-transform-error-codes'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/security/security-transform-error-codes.json'
content_hash: 'sha256:1ede06db48499cb6'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Security](../security.md) · [Security Transforms](security-transforms.md)

# Security Transform Error Codes

<sub>API Collection</sub>

Recognize the error codes used in error objects created by a transform on failure.

## Topics

### Constants

- [kSecTransformErrorAttributeNotFound](ksectransformerrorattributenotfound.md) — The attribute was not found.
- [kSecTransformErrorInvalidOperation](ksectransformerrorinvalidoperation.md) — An invalid operation was attempted.
- [kSecTransformErrorNotInitializedCorrectly](ksectransformerrornotinitializedcorrectly.md) — A required initialization is missing: It is most likely a missing required attribute.
- [kSecTransformErrorMoreThanOneOutput](ksectransformerrormorethanoneoutput.md) — A transform has an internal routing error that has caused multiple outputs instead of a single discrete output.
- [kSecTransformErrorInvalidInputDictionary](ksectransformerrorinvalidinputdictionary.md) — A dictionary used to import a transform has invalid data.
- [kSecTransformErrorInvalidAlgorithm](ksectransformerrorinvalidalgorithm.md) — A transform that needs an algorithm as an attribute received an invalid algorithm.
- [kSecTransformErrorInvalidLength](ksectransformerrorinvalidlength.md) — A transform that needs a length such as a digest transform has been given an invalid length.
- [kSecTransformErrorInvalidType](ksectransformerrorinvalidtype.md) — An invalid type has been set on an attribute.
- [kSecTransformErrorInvalidInput](ksectransformerrorinvalidinput.md) — The input set on a transform is invalid.
- [kSecTransformErrorNameAlreadyRegistered](ksectransformerrornamealreadyregistered.md) — A custom transform of a particular name has already been registered.
- [kSecTransformErrorUnsupportedAttribute](ksectransformerrorunsupportedattribute.md) — An illegal action such as setting a read-only attribute has occurred.
- [kSecTransformOperationNotSupportedOnGroup](ksectransformoperationnotsupportedongroup.md) — An illegal action on a group transform has occurred.
- [kSecTransformErrorMissingParameter](ksectransformerrormissingparameter.md) — A transform is missing a required attribute.
- [kSecTransformErrorInvalidConnection](ksectransformerrorinvalidconnection.md) — A connection between transforms in different groups was attempted.
- [kSecTransformTransformIsExecuting](ksectransformtransformisexecuting.md) — An illegal operation was called on a Transform while it was executing.
- [kSecTransformInvalidOverride](ksectransforminvalidoverride.md) — An illegal override was given to a custom transform.
- [kSecTransformTransformIsNotRegistered](ksectransformtransformisnotregistered.md) — A custom transform was asked to be created but the transform has not been registered.
- [kSecTransformErrorAbortInProgress](ksectransformerrorabortinprogress.md) — The abort attribute has been set and the transform is in the process of shutting down.
- [kSecTransformErrorAborted](ksectransformerroraborted.md) — The transform was aborted.
- [kSecTransformInvalidArgument](ksectransforminvalidargument.md) — An invalid argument was given to a Transform API.
