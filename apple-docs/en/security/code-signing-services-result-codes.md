---
title: Code Signing Services Result Codes
framework: Security
symbol_kind: article
role: collectionGroup
role_heading: API Collection
platforms: []
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/security/code-signing-services-result-codes
source_url: 'https://developer.apple.com/documentation/security/code-signing-services-result-codes'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/security/code-signing-services-result-codes.json'
content_hash: 'sha256:33946d5f2be54490'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Security](../security.md) · [Code Signing Services](code-signing-services.md)

# Code Signing Services Result Codes

<sub>API Collection</sub>

Recognize result codes specific to the code signing services API.

## Discussion

Use the [SecCopyErrorMessageString](<seccopyerrormessagestring(____).md>) function to obtain a human readable string corresponding to these status codes.

The functions of the [Code Signing Services](code-signing-services.md) API may also return the general codes listed in [Security Framework Result Codes](security-framework-result-codes.md). In particular, you might expect to encounter [errSecSuccess](errsecsuccess.md), [errSecUnimplemented](errsecunimplemented.md), [errSecParam](errsecparam.md), and [errSecAllocate](errsecallocate.md).

## Topics

### Code-signing format result codes

- [errSecCSAmbiguousBundleFormat](errseccsambiguousbundleformat.md) — The bundle could be an app or a framework.
- [errSecCSBadBundleFormat](errseccsbadbundleformat.md) — The bundle format is unrecognized, invalid, or unsuitable.
- [errSecCSBadDictionaryFormat](errseccsbaddictionaryformat.md) — A required information property list (Info.plist) file or resource is malformed.
- [errSecCSBadDiskImageFormat](errseccsbaddiskimageformat.md) — The disk image format unrecognized, invalid, or unsuitable.
- [errSecCSBadObjectFormat](errseccsbadobjectformat.md) — The object file format invalid or unsuitable.

### Code-signing database issue result codes

- [errSecCSDBAccess](errseccsdbaccess.md) — Cannot access signature database.
- [errSecCSDBDenied](errseccsdbdenied.md) — Access to signature database denied.
- [errSecCSDbCorrupt](errseccsdbcorrupt.md) — A system database or file is corrupt.
- [errSecCSSigDBAccess](errseccssigdbaccess.md) — Can’t access signature database.
- [errSecCSSigDBDenied](errseccssigdbdenied.md) — Access to signature database denied.

### Code-signing host protocol issue result codes

- [errSecCSHostProtocolContradiction](errseccshostprotocolcontradiction.md) — Host protocol violation: contradictory hosting modes.
- [errSecCSHostProtocolDedicationError](errseccshostprotocoldedicationerror.md) — Host protocol violation: operation not allowed with or for a dedicated guest.
- [errSecCSHostProtocolInvalidAttribute](errseccshostprotocolinvalidattribute.md) — Code signing host returned invalid or inconsistent attributes for guest code.
- [errSecCSHostProtocolInvalidHash](errseccshostprotocolinvalidhash.md) — Host protocol violation: invalid hash of guest code.
- [errSecCSHostProtocolNotProxy](errseccshostprotocolnotproxy.md) — Host protocol violation: proxy hosting not engaged.
- [errSecCSHostProtocolRelativePath](errseccshostprotocolrelativepath.md) — Host protocol violation: absolute guest path required.
- [errSecCSHostProtocolStateError](errseccshostprotocolstateerror.md) — Host protocol violation: invalid guest state change request.
- [errSecCSHostProtocolUnrelated](errseccshostprotocolunrelated.md) — Host protocol violation: the specified code is not a guest of the specified code signing host.

### Code-signing signature issue result codes

- [errSecCSSignatureFailed](errseccssignaturefailed.md) — Code or signature modified.
- [errSecCSSignatureInvalid](errseccssignatureinvalid.md) — Invalid format for signature.
- [errSecCSSignatureNotVerifiable](errseccssignaturenotverifiable.md) — Signature cannot be read.
- [errSecCSSignatureUnsupported](errseccssignatureunsupported.md) — Unsupported type or version of signature.
- [errSecCSUnsigned](errseccsunsigned.md) — Code object is not signed.
- [errSecCSUnsignedNestedCode](errseccsunsignednestedcode.md) — Nested code is unsigned.
- [errSecCSUnsupportedDigestAlgorithm](errseccsunsupporteddigestalgorithm.md) — The signature digest algorithm(s) specified are not supported.
- [errSecCSSignatureUntrusted](errseccssignatureuntrusted.md) — The signature is valid but signer isn’t trusted.

### Code-signing file format issue result codes

- [errSecCSDSStoreSymlink](errseccsdsstoresymlink.md) — A `.DS_Store` file can’t be a symlink.
- [errSecCSFileHardQuarantined](errseccsfilehardquarantined.md) — File open or execution not allowed.
- [errSecCSInvalidSymlink](errseccsinvalidsymlink.md) — Invalid destination for symbolic link in bundle.
- [errSecCSNoMainExecutable](errseccsnomainexecutable.md) — The code has no main executable file.
- [errSecCSRegularFile](errseccsregularfile.md) — The main executable or Info.plist must be a regular file (and not, for example, a symbolic link).
- [errSecCSUnsealedAppRoot](errseccsunsealedapproot.md) — Unsealed contents present in the bundle root.
- [errSecCSUnsealedFrameworkRoot](errseccsunsealedframeworkroot.md) — Unsealed contents present in the root directory of an embedded framework.

### Code-signing resource issue result codes

- [errSecCSResourceDirectoryFailed](errseccsresourcedirectoryfailed.md) — A directory or its signature has been modified and is therefore invalid.
- [errSecCSResourceNotSupported](errseccsresourcenotsupported.md) — Found an unsupported resource.
- [errSecCSResourceRulesInvalid](errseccsresourcerulesinvalid.md) — Invalid resource selection rule or rules.
- [errSecCSResourcesInvalid](errseccsresourcesinvalid.md) — The sealed resource directory is invalid.
- [errSecCSResourcesNotFound](errseccsresourcesnotfound.md) — Cannot find sealed resources in code.
- [errSecCSResourcesNotSealed](errseccsresourcesnotsealed.md) — Resources are not sealed by the signature.

### Other result codes

- [errSecCSBadCallbackValue](errseccsbadcallbackvalue.md) — The monitor callback returned invalid value.
- [errSecCSBadFrameworkVersion](errseccsbadframeworkversion.md) — The embedded framework contains a modified or invalid version.
- [errSecCSBadLVArch](errseccsbadlvarch.md) — The library validation flag cannot be used with an i386 binary.
- [errSecCSBadMainExecutable](errseccsbadmainexecutable.md) — The main executable failed strict validation.
- [errSecCSBadNestedCode](errseccsbadnestedcode.md) — The nested code is modified or invalid.
- [errSecCSBadResource](errseccsbadresource.md) — A sealed resource is missing or invalid.
- [errSecCSCMSTooLarge](errseccscmstoolarge.md) — The signature is too large to embed.
- [errSecCSCancelled](errseccscancelled.md) — The operation was terminated by explicit cancellation.
- [errSecCSGuestInvalid](errseccsguestinvalid.md) — The identity of guest code has been invalidated.
- [errSecCSHelperFailed](errseccshelperfailed.md) — The codesign_allocate helper tool can’t be found or used.
- [errSecCSHostReject](errseccshostreject.md) — Code rejected its host.
- [errSecCSInfoPlistFailed](errseccsinfoplistfailed.md) — The Info.plist file or the signature has been modified.
- [errSecCSInternalError](errseccsinternalerror.md) — Internal error in Code Signing Services subsystem.
- [errSecCSInvalidAttributeValues](errseccsinvalidattributevalues.md) — An attribute value associated with a key is out of range or is the wrong type.
- [errSecCSInvalidFlags](errseccsinvalidflags.md) — Invalid or inappropriate API flags specified.
- [errSecCSInvalidObjectRef](errseccsinvalidobjectref.md) — Invalid API object reference.
- [errSecCSInvalidPlatform](errseccsinvalidplatform.md) — Invalid platform identifier or platform mismatch.
- [errSecCSMultipleGuests](errseccsmultipleguests.md) — Code signing host has more than one block of guest code with this attribute value.
- [errSecCSNoMatches](errseccsnomatches.md) — No matches were found for a search or update operation.
- [errSecCSNoSuchCode](errseccsnosuchcode.md) — Code signing host has no guest code with the requested attributes.
- [errSecCSNotAHost](errseccsnotahost.md) — This code is not a code signing host.
- [errSecCSNotAppLike](errseccsnotapplike.md) — The code is valid but does not seem to be an app.
- [errSecCSNotSupported](errseccsnotsupported.md) — Operation not supported for this type of code.
- [errSecCSObjectRequired](errseccsobjectrequired.md) — A required pointer argument was null.
- [errSecCSOutdated](errseccsoutdated.md) — The presented data is out of date.
- [errSecCSReqFailed](errseccsreqfailed.md) — The code failed to satisfy one of the code requirements.
- [errSecCSReqInvalid](errseccsreqinvalid.md) — Invalid or corrupted code requirements.
- [errSecCSReqUnsupported](errseccsrequnsupported.md) — Unsupported type or version of code requirements.
- [errSecCSStaticCodeChanged](errseccsstaticcodechanged.md) — The code on disk has been modified after the code started running.
- [errSecCSStaticCodeNotFound](errseccsstaticcodenotfound.md) — Cannot find code object on disk.
- [errSecCSTooBig](errseccstoobig.md) — The code is too big for current signing format.
- [errSecCSUnimplemented](errseccsunimplemented.md) — Unimplemented code signing feature.
- [errSecCSUnsupportedGuestAttributes](errseccsunsupportedguestattributes.md) — Cannot locate guest code using this attribute set.
- [errSecCSVetoed](errseccsvetoed.md)
- [errSecCSWeakResourceEnvelope](errseccsweakresourceenvelope.md) — The resource envelope is obsolete (version 1 signature).
- [errSecCSWeakResourceRules](errseccsweakresourcerules.md) — The resource envelope is obsolete (custom omit rules).
- [errSecCSBadTeamIdentifier](errseccsbadteamidentifier.md) — A Team Identifier is wrong or inappropriate.
- [errSecCSInvalidAssociatedFileData](errseccsinvalidassociatedfiledata.md) — Resource fork, Finder information, or similar detritus not allowed.
- [errSecCSInvalidTeamIdentifier](errseccsinvalidteamidentifier.md) — A Team Identifier string is invalid.
- [errSecMultipleExecSegments](errsecmultipleexecsegments.md) — The image contains multiple executable segments.
- [errSecCSInvalidEntitlements](errseccsinvalidentitlements.md) — Encountered an invalid entitlement plist.
- [errSecCSInvalidRuntimeVersion](errseccsinvalidruntimeversion.md) — An invalid runtime version was explicity set.
- [errSecCSRevokedNotarization](errseccsrevokednotarization.md) — Notarization indicates this code has been revoked.
