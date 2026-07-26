---
title: 'SecTrustSettingsCopyTrustSettings(_:_:_:)'
framework: Security
symbol_kind: func
role: symbol
role_heading: Function
platforms: [Mac Catalyst 13.0+, macOS 10.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/security/sectrustsettingscopytrustsettings(_:_:_:)'
source_url: 'https://developer.apple.com/documentation/security/sectrustsettingscopytrustsettings(_:_:_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/security/sectrustsettingscopytrustsettings%28_%3A_%3A_%3A%29.json'
content_hash: 'sha256:824169174442179b'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Security](../security.md)

# SecTrustSettingsCopyTrustSettings(_:_:_:)

<sub>Function</sub>

Obtains the trust settings for a certificate.

<sub>Mac Catalyst, macOS</sub>

```swift
func SecTrustSettingsCopyTrustSettings(_ certRef: SecCertificate, _ domain: SecTrustSettingsDomain, _ trustSettings: UnsafeMutablePointer<CFArray?>) -> OSStatus
```

## Parameters

- `certRef` — The certificate for which you want the trust settings. Pass the value [kSecTrustSettingsDefaultRootCertSetting](ksectrustsettingsdefaultrootcertsetting.md) to obtain the default root certificate trust settings for the domain.

- `domain` — The domain from which you want to get trust settings. For possible values, see [SecTrustSettingsDomain](sectrustsettingsdomain.md).

- `trustSettings` — On return, an array of [CFDictionary](../corefoundation/cfdictionary.md) objects that specify the trust settings for the certificate. For the contents of the dictionaries, see the discussion below. In Objective-C, call the [CFRelease](../corefoundation/cfrelease.md) function to release this object when you’re finished with it.

## Return Value

A result code. See [Security Framework Result Codes](security-framework-result-codes.md). Returns [errSecItemNotFound](errsecitemnotfound.md) if no trust settings exist for the specified certificate and domain.

## Discussion

The system expresses each certificate’s trust settings as a [CFArray](../corefoundation/cfarray.md) that includes any number (including zero) of dictionaries of type [CFDictionary](../corefoundation/cfdictionary.md), each of which describes one set of usage constraints. Each usage-constraints dictionary may contain any of the following key-value pairs:

- **[kSecTrustSettingsPolicy](ksectrustsettingspolicy.md)** — A policy object ([SecPolicy](secpolicy.md)) that specifies the certificate verification policy; for example: TLS or SMIME. Create a policy object using the `SecPolicyCreate` functions; for example, to create a standard TLS verification policy, use [SecPolicyCreateSSL](<secpolicycreatessl(____).md>).
- **[kSecTrustSettingsApplication](ksectrustsettingsapplication.md)** — A trusted application reference ([SecTrustedApplication](sectrustedapplication.md)) for the app that checks the certificate’s trust settings. Use the [SecTrustedApplicationCreateFromPath](<sectrustedapplicationcreatefrompath(____).md>) function to get this reference.
- **[kSecTrustSettingsPolicyString](ksectrustsettingspolicystring.md)** — A [CFString](../corefoundation/cfstring.md) that contains policy-specific data. For an SMIME policy, this string contains an email address. For a TLS policy, it contains a host name.
- **[kSecTrustSettingsKeyUsage](ksectrustsettingskeyusage.md)** — A [CFNumber](../corefoundation/cfnumber.md) that contains an `SInt32` value specifying the operations that can use the encryption key in this certificate. For possible values, see [SecTrustSettingsKeyUsage](sectrustsettingskeyusage.md).
- **[kSecTrustSettingsResult](ksectrustsettingsresult.md)** — A `CFNumber` that contains an `SInt32` value indicating the effective trust setting for this usage-constraints dictionary.

The system includes a usage-constraints dictionary in its evaluation of trust for a certificate only if the policy, application, and key use given in the dictionary match the use for which the system is evaluating the certificate. If this is the case, then the system combines the value of the `kSecTrustSettingsResult` key with the values from other matching dictionaries to determine the overall trust setting for the certificate, using a logical `OR` operation.

If this key isn’t present, the system assumes a default value of `kSecTrustSettingsResultTrustRoot`. Only a root certificate can have this value; therefore it’s invalid to create a usage-constraints dictionary for a non-root certificate without this key.

For the possible values for this key, see [SecTrustSettingsResult](sectrustsettingsresult.md).

- **[kSecTrustSettingsAllowedError](ksectrustsettingsallowederror.md)** — A [CFNumber](../corefoundation/cfnumber.md) that contains an `SInt32` value indicating a `CSSM_RETURN` result code. If the system encounters this result code due to an error when it evaluates the trust for a certificate, it ignores the error.

The system applies this “allowed error” value to the certificate evaluation only if the usage-constraints dictionary meets the criteria described with the `kSecTrustSettingsResult` key. A usage-constraints dictionary with no constraints but with an allowed error value causes the system to always ignore that value when evaluating a certificate.

The system determines the overall trust settings for a certificate by combining the trust-settings results from all the usage-constraints dictionaries that match the use for which it’s evaluating the certificate. Trust settings for a given use apply if _any_ of the dictionaries in the certificate’s trust-settings array matches the specified use.

If the value of the [kSecTrustSettingsResult](ksectrustsettingsresult.md) key is a value other than [kSecTrustSettingsResultUnspecified](sectrustsettingsresult/unspecified.md) for a usage constraints-dictionary that has no constraints, the system uses the default value [kSecTrustSettingsResultTrustRoot](sectrustsettingsresult/trustroot.md). To specify a value for the [kSecTrustSettingsAllowedError](ksectrustsettingsallowederror.md) component without explicitly trusting or distrusting the associated certificate, set the value of the [kSecTrustSettingsResult](ksectrustsettingsresult.md) key to [kSecTrustSettingsResultUnspecified](sectrustsettingsresult/unspecified.md).

The `trustSettings` parameter can return a valid but empty [CFArray](../corefoundation/cfarray.md). This empty trust-settings array means “always trust this certificate” with an overall trust setting for the certificate of [kSecTrustSettingsResultTrustRoot](sectrustsettingsresult/trustroot.md). However, an empty trust settings array isn’t the same as no trust settings, where the `trustSettings` parameter returns `NULL`. No trust-settings array means “this certificate must be verifiable using a known trusted certificate”.

> [!note] Note
> The trust settings result value [kSecTrustSettingsResultTrustRoot](sectrustsettingsresult/trustroot.md) can only apply to root (self-signed) certificates. It’s an error to apply it to non-root certificates, including implicitly by using an empty trust settings array. Instead, use [kSecTrustSettingsResultTrustAsRoot](sectrustsettingsresult/trustasroot.md).

### Special considerations

The system authenticates the person before making changes to per-user trust settings. On macOS 11 and later, the system authenticates the person as an administrator before making changes to system-wide trust settings. Therefore, you can only modify trust settings when running in a GUI environment; for example, a launch daemon can’t modify the settings.
