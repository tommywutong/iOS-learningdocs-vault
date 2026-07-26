---
title: Static Code Validation Flags
framework: Security
symbol_kind: article
role: collectionGroup
role_heading: API Collection
platforms: []
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/security/static-code-validation-flags
source_url: 'https://developer.apple.com/documentation/security/static-code-validation-flags'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/security/static-code-validation-flags.json'
content_hash: 'sha256:4837eab21ba8f40a'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Security](../security.md) · [Code Signing Services](code-signing-services.md)

# Static Code Validation Flags

<sub>API Collection</sub>

Use these supplemental flags to test the validity of a static code signature.

## Overview

These flags supplement the flags described in [SecCSFlags](seccsflags.md). Use these additional constants with the flags parameter of the [SecStaticCodeCheckValidity](<secstaticcodecheckvalidity(______).md>) and [SecStaticCodeCheckValidityWithErrors](<secstaticcodecheckvaliditywitherrors(________).md>) functions to control the validation of code in the file system.

## Topics

### Constants

- [kSecCSCheckAllArchitectures](kseccscheckallarchitectures.md) — For multi-architecture (universal) Mach-O programs, validate all architectures included.
- [kSecCSDoNotValidateExecutable](kseccsdonotvalidateexecutable.md) — Do not validate the contents of the main executable.
- [kSecCSDoNotValidateResources](kseccsdonotvalidateresources.md) — Do not validate the presence and contents of all bundle resources (if any).
- [kSecCSBasicValidateOnly](kseccsbasicvalidateonly.md) — Do not validate either the main executable or the bundle resources, if any.
- [kSecCSCheckNestedCode](kseccschecknestedcode.md) — For code in bundle form, locate and recursively check embedded code.
- [kSecCSStrictValidate](kseccsstrictvalidate.md) — Perform additional checks to ensure the validity of code in bundle form.
- [kSecCSFullReport](kseccsfullreport.md)
- [kSecCSCheckGatekeeperArchitectures](kseccscheckgatekeeperarchitectures.md)
- [kSecCSRestrictSymlinks](kseccsrestrictsymlinks.md)
- [kSecCSRestrictToAppLike](kseccsrestricttoapplike.md)
- [kSecCSRestrictSidebandData](kseccsrestrictsidebanddata.md)
- [kSecCSUseSoftwareSigningCert](kseccsusesoftwaresigningcert.md)
- [kSecCSValidatePEH](kseccsvalidatepeh.md)
- [kSecCSSingleThreaded](kseccssinglethreaded.md)
