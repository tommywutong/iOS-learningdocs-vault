---
title: Signing Information Dictionary Keys
framework: Security
symbol_kind: article
role: collectionGroup
role_heading: API Collection
platforms: []
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/security/signing-information-dictionary-keys
source_url: 'https://developer.apple.com/documentation/security/signing-information-dictionary-keys'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/security/signing-information-dictionary-keys.json'
content_hash: 'sha256:6010963c31ad4c30'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Security](../security.md) · [Code Signing Services](code-signing-services.md)

# Signing Information Dictionary Keys

<sub>API Collection</sub>

Use these keys from the information dictionary when you retrieve information from a code signature.

## Overview

Use these keys when examining the dictionary returned by the [SecCodeCopySigningInformation](<seccodecopysigninginformation(______).md>) function to obtain information about the signed code.

## Topics

### Constants

- [kSecCodeInfoCdHashes](kseccodeinfocdhashes.md) — A key whose value is an array containing the unique binary identifier for every digest algorithm supported in the signature.
- [kSecCodeInfoCertificates](kseccodeinfocertificates.md) — A key whose value is an array of certificates representing the certificate chain of the signing certificate as seen by the system.
- [kSecCodeInfoChangedFiles](kseccodeinfochangedfiles.md) — A key whose value is a list of all files in the code that may have been modified by the process of signing it.
- [kSecCodeInfoCMS](kseccodeinfocms.md) — A key whose value is the CMS cryptographic object that secures the code signature.
- [kSecCodeInfoDesignatedRequirement](kseccodeinfodesignatedrequirement.md) — A keys whose value is the designated requirement of the code.
- [kSecCodeInfoDigestAlgorithm](kseccodeinfodigestalgorithm.md) — A key whose value is a number indicating the cryptographic hash function.
- [kSecCodeInfoDigestAlgorithms](kseccodeinfodigestalgorithms.md) — A key whose value is a list of the kinds of cryptographic hash functions available within the signature.
- [kSecCodeInfoEntitlements](kseccodeinfoentitlements.md) — A key whose value represents the embedded entitlement blob of the code, if any.
- [kSecCodeInfoEntitlementsDict](kseccodeinfoentitlementsdict.md) — A key whose value is a dictionary of embedded entitlements.
- [kSecCodeInfoFormat](kseccodeinfoformat.md) — A key whose value is a string representing the type and format of the code in a form suitable for display to a knowledgeable user.
- [kSecCodeInfoFlags](kseccodeinfoflags.md) — A key whose value indicates the static (on-disk) state of the object.
- [kSecCodeInfoIdentifier](kseccodeinfoidentifier.md) — A key whose value is the signing identifier sealed into the signature.
- [kSecCodeInfoImplicitDesignatedRequirement](kseccodeinfoimplicitdesignatedrequirement.md) — A key whose value is the designated requirement (DR) that the system generated—or would have generated—for the code in the absence of an explicitly-declared DR.
- [kSecCodeInfoMainExecutable](kseccodeinfomainexecutable.md) — A key whose value is a URL locating the main executable file of the code.
- [kSecCodeInfoPList](kseccodeinfoplist.md) — A key whose value is an information dictionary containing the contents of the secured `Info.plist` file as seen by Code Signing Services.
- [kSecCodeInfoPlatformIdentifier](kseccodeinfoplatformidentifier.md) — A key whose value identifies the operating system release with which the code is associated, if any.
- [kSecCodeInfoRequirements](kseccodeinforequirements.md) — A key whose value is the internal requirements of the code as a text string in canonical syntax.
- [kSecCodeInfoRequirementData](kseccodeinforequirementdata.md) — A key whose value is the internal requirements of the code as a binary blob.
- [kSecCodeInfoRuntimeVersion](kseccodeinforuntimeversion.md) — A key whose value represents the runtime version.
- [kSecCodeInfoSource](kseccodeinfosource.md) — The source of the code signature used for the code object in a format suitable for display.
- [kSecCodeInfoStatus](kseccodeinfostatus.md) — A key whose value is the set of code status flags for the running code.
- [kSecCodeInfoTeamIdentifier](kseccodeinfoteamidentifier.md) — A key whose value is the team identifier.
- [kSecCodeInfoTime](kseccodeinfotime.md) — A key whose value is the signing date embedded in the code signature.
- [kSecCodeInfoTimestamp](kseccodeinfotimestamp.md) — A key whose value indicates the actual signing date.
- [kSecCodeInfoTrust](kseccodeinfotrust.md) — A key whose value is the trust object the system uses to evaluate the validity of the code’s signature.
- [kSecCodeInfoUnique](kseccodeinfounique.md) — A key whose value is a binary number that uniquely identifies static code.
