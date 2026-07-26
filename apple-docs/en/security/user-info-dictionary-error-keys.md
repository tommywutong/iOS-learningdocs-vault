---
title: User Info Dictionary Error Keys
framework: Security
symbol_kind: article
role: collectionGroup
role_heading: API Collection
platforms: []
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/security/user-info-dictionary-error-keys
source_url: 'https://developer.apple.com/documentation/security/user-info-dictionary-error-keys'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/security/user-info-dictionary-error-keys.json'
content_hash: 'sha256:21d8d88aab01bc3a'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Security](../security.md) · [Code Signing Services](code-signing-services.md)

# User Info Dictionary Error Keys

<sub>API Collection</sub>

Recognize the keys of the user info dictionary provided by functions that return error objects.

## Overview

Code Signing Services functions that return an error on failure may provide additional information by populating the error’s user info dictionary with any of these keys. Use the [CFErrorCopyUserInfo(_:)](<../corefoundation/cferrorcopyuserinfo(__).md>) function to retrieve the user info dictionary from the error object.

These keys are always supplemental and optional. Don’t rely on their presence or absence to categorize an error. Use the primary `OSStatus` return codes listed in [Code Signing Services Result Codes](code-signing-services-result-codes.md) for that.

## Topics

### Constants

- [kSecCFErrorArchitecture](kseccferrorarchitecture.md) — A key whose value is a string containing the name of the architecture that is causing the problem.
- [kSecCFErrorPattern](kseccferrorpattern.md) — A key whose value is a string containing a regular expression that’s part of a resource specification that did not parse correctly.
- [kSecCFErrorResourceSeal](kseccferrorresourceseal.md) — A key whose value is a Core Foundation object containing the part of the resource seal that had a problem.
- [kSecCFErrorResourceAdded](kseccferrorresourceadded.md) — A key whose value is a URL pointing to the resource on disk that is not included in the signed resources for the code.
- [kSecCFErrorResourceAltered](kseccferrorresourcealtered.md) — A key whose value is a URL pointing to the resource on disk that has been altered.
- [kSecCFErrorResourceMissing](kseccferrorresourcemissing.md) — A key whose value is a URL indicating the location of the missing resource as it is specified in the `CodeResources` file.
- [kSecCFErrorResourceSideband](kseccferrorresourcesideband.md) — A key whose value is a URL representing a sealed resource with invalid sideband data (resource fork, etc.).
- [kSecCFErrorInfoPlist](kseccferrorinfoplist.md) — A key whose value is a Core Foundation object identifying the invalid component or key in the dictionary.
- [kSecCFErrorGuestAttributes](kseccferrorguestattributes.md) — A key whose value is a Core Foundation object containing an attribute that is unrecognized or that contains a value of the wrong type.
- [kSecCFErrorRequirementSyntax](kseccferrorrequirementsyntax.md) — A key whose value is a string containing a compilation error generated when parsing a requirement.
- [kSecCFErrorPath](kseccferrorpath.md) — A key whose value is a URL indicating the subcomponent containing the error.
