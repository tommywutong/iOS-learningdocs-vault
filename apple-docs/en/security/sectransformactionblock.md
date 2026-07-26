---
title: SecTransformActionBlock
framework: Security
symbol_kind: typealias
role: symbol
role_heading: Type Alias
platforms: [macOS 10.7+（13.0 起废弃）]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: /documentation/security/sectransformactionblock
source_url: 'https://developer.apple.com/documentation/security/sectransformactionblock'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/security/sectransformactionblock.json'
content_hash: 'sha256:1c1e709813ee546a'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Security](../security.md)

# SecTransformActionBlock

<sub>Type Alias</sub>

A block that overrides the default behavior of a custom transform.

> [!warning] Deprecated
> SecTransform is no longer supported

<sub>macOS</sub>

```swift
typealias SecTransformActionBlock = () -> Unmanaged<CFTypeRef>?
```

## Return Value

A dictionary of the custom items to be exported if this block is used to override the [kSecTransformActionExternalizeExtraData](ksectransformactionexternalizeextradata.md) action or  `NULL` for any other action. Alternatively, the block returns a [CFError](../corefoundation/cferror.md) object if an error occurs.

## Discussion

A  block of this type is used to override the default behavior of a custom transform. This block is associated with the SecTransformOverrideTransformAction block.

The behaviors that can be overridden are:

- [kSecTransformActionCanExecute](ksectransformactioncanexecute.md) - Determine if the transform has all of the data needed to run.
- [kSecTransformActionStartingExecution](ksectransformactionstartingexecution.md) - Called just before running ProcessData.
- [kSecTransformActionFinalize](ksectransformactionfinalize.md) - Called just before deleting the custom transform.
- [kSecTransformActionExternalizeExtraData](ksectransformactionexternalizeextradata.md) - Called to allow for writing out custom data to be exported.

For example:

```objc
SecTransformImplementationRef ref;
CFErrorRef error = NULL;
 
error = SecTransformSetTransformAction(ref, kSecTransformActionStartingExecution, ^{
    // Initialize any data needed before running
    CFErrorRef result = DoMyInitialization();
    return result;});
 
SecTransformTransformActionBlock actionBlock =
^{
    // Clean up any existing data before running
    CFErrorRef result = DoMyFinalization();
    return result;};
 
error = SecTransformSetTransformAction(ref, kSecTransformActionFinalize,actionBlock);
```
