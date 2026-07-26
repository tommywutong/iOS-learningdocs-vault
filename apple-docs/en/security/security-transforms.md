---
title: Security Transforms
framework: Security
symbol_kind: article
role: collectionGroup
role_heading: API Collection
platforms: []
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/security/security-transforms
source_url: 'https://developer.apple.com/documentation/security/security-transforms'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/security/security-transforms.json'
content_hash: 'sha256:f7583ece324e495d'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Security](../security.md)

# Security Transforms

<sub>API Collection</sub>

Perform cryptographic functions like encoding, encryption, signing, and signature verification.

## Overview

You use security transforms to assemble a chain of security-related operations that you apply to a stream of data in macOS.

## Topics

### Transforms

- [SecTransformCreateReadTransformWithReadStream](<sectransformcreatereadtransformwithreadstream(__).md>) — Creates a read transform from a read stream reference. _(deprecated)_
- [SecTransform](sectransform.md) — A Core Foundation type that represents a security transform. _(deprecated)_
- [SecTransformGetTypeID](<sectransformgettypeid().md>) — Returns the unique identifier of the opaque type to which a security transform object belongs. _(deprecated)_

### Encoding

- [SecEncodeTransformCreate](<secencodetransformcreate(____).md>) — Creates an encode transform object. _(deprecated)_
- [SecDecodeTransformCreate](<secdecodetransformcreate(____).md>) — Creates a decode transform object. _(deprecated)_

### Encrypting

- [SecEncryptTransformCreate](<secencrypttransformcreate(____).md>) — Creates an encryption transform object. _(deprecated)_
- [SecDecryptTransformCreate](<secdecrypttransformcreate(____).md>) — Creates a decryption transform object. _(deprecated)_
- [SecEncryptTransformGetTypeID](<secencrypttransformgettypeid().md>) — Returns the unique identifier of the opaque type to which an encryption transform belongs. _(deprecated)_
- [SecDecryptTransformGetTypeID](<secdecrypttransformgettypeid().md>) — Returns the unique identifier of the opaque type to which a decryption transform belongs. _(deprecated)_

### Signing

- [SecSignTransformCreate](<secsigntransformcreate(____).md>) — Creates a signing transform object. _(deprecated)_
- [SecVerifyTransformCreate](<secverifytransformcreate(______).md>) — Creates a verify transform object. _(deprecated)_
- [SecDigestTransformCreate](<secdigesttransformcreate(______).md>) — Creates a digest transform object. _(deprecated)_
- [SecDigestTransformGetTypeID](<secdigesttransformgettypeid().md>) — Returns the unique identifier of the opaque type to which a digest transform belongs. _(deprecated)_

### Custom Transforms

- [SecTransformCreate](<sectransformcreate(____).md>) — Creates a transform computation object. _(deprecated)_
- [SecTransformRegister](<sectransformregister(______).md>) — Registers a custom transform. _(deprecated)_
- [SecTransformCreateFP](sectransformcreatefp.md) — A pointer to a function that creates a new instance of a custom transform. _(deprecated)_
- [SecTransformInstanceBlock](sectransforminstanceblock.md) — A block that you return from a transform creation function.
- [SecTransformImplementationRef](sectransformimplementationref.md) — An opaque pointer to a block that implements an instance of a transform.

### Transform Groups

- [SecTransformCreateGroupTransform](<sectransformcreategrouptransform().md>) — Creates an object that acts as a container for a set of connected transforms. _(deprecated)_
- [SecTransformFindByName](<sectransformfindbyname(____).md>) — Finds a member of a transform group by its name. _(deprecated)_
- [SecGroupTransform](secgrouptransform.md) — A Core Foundation type that represents a container holding a group of transforms. _(deprecated)_
- [SecGroupTransformGetTypeID](<secgrouptransformgettypeid().md>) — Returns the Core Foundation type ID for a transform group container. _(deprecated)_

### Transform Characteristics

- [SecTransformSetAttribute](<sectransformsetattribute(________).md>) — Sets a static value for an attribute in a transform. _(deprecated)_
- [SecTransformGetAttribute](<sectransformgetattribute(____).md>) — Gets the current value of a transform attribute. _(deprecated)_
- [SecTransformCustomSetAttribute](<sectransformcustomsetattribute(________).md>) — Sets an attribute value on a custom transform. _(deprecated)_
- [SecTransformCustomGetAttribute](<sectransformcustomgetattribute(______).md>) — Gets an attribute value from a custom transform. _(deprecated)_
- [SecTransformPushbackAttribute](<sectransformpushbackattribute(______).md>) — Pushes a single value back for a specific attribute. _(deprecated)_
- [Transform Attributes](transform-attributes.md) — Specify the attributes of a transform.
- [SecTransformAttribute](sectransformattribute.md) — A direct reference to a security transform attribute. _(deprecated)_
- [SecTransformStringOrAttribute](sectransformstringorattribute.md) — A type that may be either a string or an attribute reference. _(deprecated)_
- [SecTransformMetaAttributeType](sectransformmetaattributetype.md) — The keys that describe the metadata attributes of transform attributes. _(deprecated)_

### Actions

- [SecTransformSetDataAction](<sectransformsetdataaction(______).md>) — Changes the way a custom transform processes data. _(deprecated)_
- [SecTransformSetAttributeAction](<sectransformsetattributeaction(________).md>) — Requests a callback when an attribute is set. _(deprecated)_
- [SecTransformSetTransformAction](<sectransformsettransformaction(______).md>) — Changes the way that a transform deals with transform lifecycle behaviors. _(deprecated)_
- [SecTransformActionBlock](sectransformactionblock.md) — A block that overrides the default behavior of a custom transform. _(deprecated)_
- [SecTransformAttributeActionBlock](sectransformattributeactionblock.md) — A block used to override the default attribute handling for when an attribute is set. _(deprecated)_
- [SecTransformDataBlock](sectransformdatablock.md) — A block used to override the default data handling for a transform.
- [Actions](actions.md) — Use actions to trigger particular behaviors.

### Piping

- [SecTransformConnectTransforms](<sectransformconnecttransforms(____________).md>) — Chains transforms together. _(deprecated)_

### Execution

- [SecTransformExecute](<sectransformexecute(____).md>) — Executes a transform or transform group synchronously. _(deprecated)_
- [SecTransformExecuteAsync](<sectransformexecuteasync(______).md>) — Executes transform or transform group asynchronously. _(deprecated)_
- [SecTransformNoData](<sectransformnodata().md>) — Returns an object from inside a ProcessData override that says that although no data is being returned the transform is still active and awaiting data. _(deprecated)_
- [SecMessageBlock](secmessageblock.md) — A block that delivers messages during asynchronous operations.

### Import and Export

- [SecTransformCopyExternalRepresentation](<sectransformcopyexternalrepresentation(__).md>) — Creates a dictionary that contains enough information to be able to recreate a transform. _(deprecated)_
- [SecTransformCreateFromExternalRepresentation](<sectransformcreatefromexternalrepresentation(____).md>) — Creates a transform instance from a dictionary of parameters. _(deprecated)_

### Reporting Errors

- [kSecTransformErrorDomain](ksectransformerrordomain.md) — The domain of any error object created by a transform on failure.
- [Security Transform Error Codes](security-transform-error-codes.md) — Recognize the error codes used in error objects created by a transform on failure.
- [kSecTransformPreviousErrorKey](ksectransformpreviouserrorkey.md) — The key in an error’s `userInfo` dictionary whose value specifies the previous error when multiple errors occur during transform evaluation.
- [kSecTransformAbortOriginatorKey](ksectransformabortoriginatorkey.md) — The key in an error’s `userInfo` dictionary whose value indicates the transform that caused the chain to abort.

## See Also

### Related Documentation

- [Security Transforms Programming Guide](https://developer.apple.com/library/archive/documentation/Security/Conceptual/SecTransformPG/Introduction/Introduction.html#//apple_ref/doc/uid/TP40010801)
