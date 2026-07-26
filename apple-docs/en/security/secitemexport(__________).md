---
title: 'SecItemExport(_:_:_:_:_:)'
framework: Security
symbol_kind: func
role: symbol
role_heading: Function
platforms: [macOS 10.7+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/security/secitemexport(_:_:_:_:_:)'
source_url: 'https://developer.apple.com/documentation/security/secitemexport(_:_:_:_:_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/security/secitemexport%28_%3A_%3A_%3A_%3A_%3A%29.json'
content_hash: 'sha256:db7c2978e93694fb'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Security](../security.md)

# SecItemExport(_:_:_:_:_:)

<sub>Function</sub>

Exports one or more certificates, keys, or identities.

<sub>macOS</sub>

```swift
func SecItemExport(_ secItemOrArray: CFTypeRef, _ outputFormat: SecExternalFormat, _ flags: SecItemImportExportFlags, _ keyParams: UnsafePointer<SecItemImportExportKeyParameters>?, _ exportedData: UnsafeMutablePointer<CFData?>) -> OSStatus
```

## Parameters

- `secItemOrArray` — The keychain item or items to export. You can export only the following types of keychain items: [SecCertificate](seccertificate.md), [SecKey](seckey.md), and [SecIdentity](secidentity.md). If you are exporting exactly one item, you can specify a [SecKeychainItem](seckeychainitem.md) object. Otherwise this parameter is a [CFArray](../corefoundation/cfarray.md) object containing a number of items of type [SecKeychainItem](seckeychainitem.md).

- `outputFormat` — The format of the desired external representation for the item. Set this parameter to [kSecFormatUnknown](secexternalformat/formatunknown.md) to use the default for that item type. Possible values for this parameter and default values are enumerated in [SecExternalFormat](secexternalformat.md).

- `flags` — A flag field indicating whether the exported item should have PEM armor. PEM armor refers to a way of expressing binary data as an ASCII string so that it can be transferred over text-only channels such as email. Set this flag to [kSecItemPemArmour](secitemimportexportflags/pemarmour.md) if you want PEM armoring.

- `keyParams` — A pointer to a structure containing a set of input parameters for the function. If no key items are being exported, these parameters are optional and you can set the `keyParams` parameter to `NULL`. For more information, see [SecItemImportExportKeyParameters](secitemimportexportkeyparameters.md).

- `exportedData` — On return, the variable referenced by this argument is overwritten with a [CFData](../corefoundation/cfdata.md) object containing the external representation of the keychain item or items. You are responsible for releasing this object by calling [CFRelease](../corefoundation/cfrelease.md).

## Return Value

A result code. See [Security Framework Result Codes](security-framework-result-codes.md).

## Discussion

This function works only with keys, certificates, and identities. An identity is the combination of a certificate and its associated private key. Although public keys are commonly stored in certificates, they can be stored separately in the keychain as well; for example, when you call the [SecKeyCreatePair](seckeycreatepair.md) function to create a key pair, both the public and private keys are stored in the keychain. Use the [SecKeychainSearchCopyNext](seckeychainsearchcopynext.md) function to find a key or certificate. Use the [SecIdentitySearchCopyNext](secidentitysearchcopynext.md) function in the Certificate, Key, and Trust API to find an identity.
