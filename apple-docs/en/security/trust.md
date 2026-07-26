---
title: Trust
framework: Security
symbol_kind: article
role: collectionGroup
role_heading: API Collection
platforms: []
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/security/trust
source_url: 'https://developer.apple.com/documentation/security/trust'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/security/trust.json'
content_hash: 'sha256:f9a14ac0ae70e6c8'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Security](../security.md) · [Certificate, Key, and Trust Services](certificate-key-and-trust-services.md)

# Trust

<sub>API Collection</sub>

Evaluate trust based on a given policy.

## Overview

Before using a certificate, you evaluate its trustworthiness for a particular purpose.

If you know that a certificate comes unaltered from its sender, you can be confident that its embedded public key does as well. You can also take at face value claims made by the certificate about when and for what purpose the public key may be used. You can securely engage in the operations described in [Using Keys for Encryption](using-keys-for-encryption.md) and [Signing and Verifying](signing-and-verifying.md) without prior arrangement between sender and receiver.

## Topics

### Essentials

- [Creating a Trust Object](creating-a-trust-object.md) — Construct a trust object from a certificate and a policy.
- [SecTrustCreateWithCertificates](<sectrustcreatewithcertificates(______).md>) — Creates a trust management object based on certificates and policies.
- [SecTrust](sectrust.md) — An object used to evaluate trust.
- [SecTrustGetTypeID](<sectrustgettypeid().md>) — Returns the unique identifier of the opaque type to which a trust object belongs.

### Trust Evaluation

- [Evaluating a Trust and Parsing the Result](evaluating-a-trust-and-parsing-the-result.md) — Learn what to expect when evaluating a trust object.
- [SecTrustEvaluateWithError](<sectrustevaluatewitherror(____).md>) — Evaluates trust for the specified certificate and policies.
- [SecTrustEvaluateAsyncWithError](<sectrustevaluateasyncwitherror(______).md>) — Evaluates a trust object asynchronously on the specified dispatch queue.
- [SecTrustWithErrorCallback](sectrustwitherrorcallback.md) — A block called with the results of an asynchronous trust evaluation.

### Trust Evaluation Result

- [Discovering Why a Trust Evaluation Failed](discovering-why-a-trust-evaluation-failed.md) — Determine whether you can recover from a failed trust evaluation.
- [SecTrustGetTrustResult](<sectrustgettrustresult(____).md>) — Returns the result code from the most recent trust evaluation.
- [SecTrustResultType](sectrustresulttype.md) — Trust evaluation result codes.
- [SecTrustCopyResult](<sectrustcopyresult(__).md>) — Returns a dictionary containing information about an evaluated trust.
- [Trust Result Dictionary Keys](trust-result-dictionary-keys.md) — Recognize the keys that appear in a dictionary containing information about an evaluated certification chain.

### Trust Components

- [SecTrustCopyPublicKey](<sectrustcopypublickey(__).md>) — Returns the public key for a leaf certificate after it has been evaluated. _(deprecated)_
- [SecTrustGetCertificateCount](<sectrustgetcertificatecount(__).md>) — Returns the number of certificates in an evaluated certificate chain.
- [SecTrustGetCertificateAtIndex](<sectrustgetcertificateatindex(____).md>) — Returns a specific certificate from the certificate chain used to evaluate trust. _(deprecated)_
- [SecTrustGetVerifyTime](<sectrustgetverifytime(__).md>) — Gets the absolute time against which the certificates in a trust management object are verified.
- [SecTrustCopyAnchorCertificates](<sectrustcopyanchorcertificates(__).md>) — Retrieves the anchor (root) certificates stored by macOS.
- [SecTrustCopyCustomAnchorCertificates](<sectrustcopycustomanchorcertificates(____).md>) — Retrieves the custom anchor certificates, if any, used by a given trust.
- [SecTrustCopyExceptions](<sectrustcopyexceptions(__).md>) — Returns an opaque cookie containing exceptions to trust policies that will allow future evaluations of the current certificate to succeed.
- [SecTrustCopyPolicies](<sectrustcopypolicies(____).md>) — Retrieves the policies used by a given trust management object.
- [SecTrustCopyProperties](<sectrustcopyproperties(__).md>) — Returns an array containing the properties of a trust object. _(deprecated)_

### Advanced Trust Configuation

- [Configuring a Trust](configuring-a-trust.md) — Work around a recoverable trust failure.
- [SecTrustSetVerifyDate](<sectrustsetverifydate(____).md>) — Sets the date and time against which the certificates in a trust management object are verified.
- [SecTrustSetAnchorCertificates](<sectrustsetanchorcertificates(____).md>) — Sets the anchor certificates used when evaluating a trust management object.
- [SecTrustSetAnchorCertificatesOnly](<sectrustsetanchorcertificatesonly(____).md>) — Reenables trusting built-in anchor certificates.
- [SecTrustSetExceptions](<sectrustsetexceptions(____).md>) — Sets a list of exceptions that should be ignored when the certificate is evaluated.
- [SecTrustSetPolicies](<sectrustsetpolicies(____).md>) — Sets the policies to use in an evaluation.
- [SecTrustSetOptions](<sectrustsetoptions(____).md>) — Sets option flags for customizing evaluation of a trust object.
- [SecTrustOptionFlags](sectrustoptionflags.md) — The option flags used to condition a trust evaluation.
- [SecTrustGetNetworkFetchAllowed](<sectrustgetnetworkfetchallowed(____).md>) — Indicates whether a trust evaluation is permitted to fetch missing intermediate certificates from the network.
- [SecTrustSetNetworkFetchAllowed](<sectrustsetnetworkfetchallowed(____).md>) — Specifies whether a trust evaluation is permitted to fetch missing intermediate certificates from the network.
- [SecTrustSetOCSPResponse](<sectrustsetocspresponse(____).md>) — Attaches Online Certificate Status Protocol (OSCP) response data to a trust object.
- [SecTrustSetSignedCertificateTimestamps](<sectrustsetsignedcertificatetimestamps(____).md>) — Attaches signed certificate timestamp data to a trust object.

### Trust Settings

- [SecTrustSettingsCopyCertificates](<sectrustsettingscopycertificates(____).md>) — Obtains an array of all certificates that have trust settings in a specific trust settings domain.
- [SecTrustSettingsCopyModificationDate](<sectrustsettingscopymodificationdate(______).md>) — Obtains the date and time at which a certificate’s trust settings were last modified.
- [Usage Constraints Dictionary Keys](usage-constraints-dictionary-keys.md) — Use these trust settings keys in a usage constraints dictionary.
- [SecTrustSettingsCopyTrustSettings](<sectrustsettingscopytrustsettings(______).md>) — Obtains the trust settings for a certificate.
- [SecTrustSettingsCreateExternalRepresentation](<sectrustsettingscreateexternalrepresentation(____).md>) — Obtains an external, portable representation of the specified domain’s trust settings.
- [SecTrustSettingsImportExternalRepresentation](<sectrustsettingsimportexternalrepresentation(____).md>) — Imports trust settings into a trust domain.
- [SecTrustSettingsRemoveTrustSettings](<sectrustsettingsremovetrustsettings(____).md>) — Deletes the trust settings for a certificate.
- [SecTrustSettingsSetTrustSettings](<sectrustsettingssettrustsettings(______).md>) — Specifies trust settings for a certificate.
- [SecTrustSettingsKeyUsage](sectrustsettingskeyusage.md) — Allowed uses for the encryption key in a certificate.
- [SecTrustSettingsResult](sectrustsettingsresult.md) — Trust settings returned in usage constraints dictionaries.
- [SecTrustSettingsDomain](sectrustsettingsdomain.md) — The trust settings domains.

### Legacy Symbols

- [SecTrustEvaluate](<sectrustevaluate(____).md>) — Evaluates trust for the specified certificate and policies. _(deprecated)_
- [SecTrustEvaluateAsync](<sectrustevaluateasync(______).md>) — Evaluates a trust object asynchronously on the specified dispatch queue. _(deprecated)_
- [SecTrustCallback](sectrustcallback.md) — A block called with the results of an asynchronous trust evaluation.
- [SecTrustSetKeychains](<sectrustsetkeychains(____).md>) — Sets the keychains searched for intermediate certificates when evaluating a trust management object. _(deprecated)_
