---
title: 'SecItemImport(_:_:_:_:_:_:_:_:)'
framework: Security
symbol_kind: func
role: symbol
role_heading: Function
platforms: [macOS 10.7+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/security/secitemimport(_:_:_:_:_:_:_:_:)'
source_url: 'https://developer.apple.com/documentation/security/secitemimport(_:_:_:_:_:_:_:_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/security/secitemimport%28_%3A_%3A_%3A_%3A_%3A_%3A_%3A_%3A%29.json'
content_hash: 'sha256:300ab420e5f5bfef'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Security](../security.md)

# SecItemImport(_:_:_:_:_:_:_:_:)

<sub>Function</sub>

Imports one or more certificates, keys, or identities and optionally adds them to a keychain.

<sub>macOS</sub>

```swift
func SecItemImport(_ importedData: CFData, _ fileNameOrExtension: CFString?, _ inputFormat: UnsafeMutablePointer<SecExternalFormat>?, _ itemType: UnsafeMutablePointer<SecExternalItemType>?, _ flags: SecItemImportExportFlags, _ keyParams: UnsafePointer<SecItemImportExportKeyParameters>?, _ importKeychain: SecKeychain?, _ outItems: UnsafeMutablePointer<CFArray?>?) -> OSStatus
```

## Parameters

- `importedData` — A [CFData](../corefoundation/cfdata.md) object containing the data to import.

- `fileNameOrExtension` — Optional. The name of the file from which the external representation was previously read, or if that is unknown, then the file extension (`.p7r`, for example). This serves as a hint for the key format and key type detection code.

- `inputFormat` — Optional. The address of a [SecExternalFormat](secexternalformat.md) variable. If you know what format the external representation is in, set the initial value of this variable to an appropriate format constant to eliminate the need to detect the format. If not, set it to [kSecFormatUnknown](secexternalformat/formatunknown.md). On return, the variable referenced by this argument is set to the format that the function actually detected. Pass `NULL` if you don’t know or don’t care what format the external representation is in.

- `itemType` — Optional. The address of a [SecExternalItemType](secexternalitemtype.md) variable. Before calling this function, if you know what type of key the external representation contains, set the variable to an appropriate type constant to eliminate the need to detect the key type. If not, set it to [kSecItemTypeUnknown](secexternalitemtype/itemtypeunknown.md). On return, the variable referenced by this argument is set to the type of key that the function actually detected. Pass `NULL` if you don’t know or don’t care what key type the external representation contains.

- `flags` — A set of import flags. See [SecItemImportExportFlags](secitemimportexportflags.md) for valid values. Note that PEM formatting is determined internally via inspection of the incoming data, so the [kSecItemPemArmour](secitemimportexportflags/pemarmour.md) flag  is ignored.

- `keyParams` — A pointer to a structure containing a set of input parameters for the function. See [SecItemImportExportKeyParameters](secitemimportexportkeyparameters.md).

- `importKeychain` — Optional. The keychain into which the item should be imported. Pass `NULL` if you do not want to import the item into a keychain.

- `outItems` — Optional. The address of a [CFArray](../corefoundation/cfarray.md) variable that, upon return, will contain a list of keychain items. Pass `NULL` if you do not want a copy of these items. Upon return, the referenced variable is overwritten by a new [CFArray](../corefoundation/cfarray.md) array that contains [SecKeychainItem](seckeychainitem.md) objects, each of which may be a [SecCertificate](seccertificate.md), [SecKey](seckey.md), or [SecIdentity](secidentity.md) object. The caller is responsible for releasing this [CFArray](../corefoundation/cfarray.md) object. > [!note] Note > When importing a PKCS12 blob, typically one [SecIdentity](secidentity.md) object and zero or more additional [SecCertificate](seccertificate.md) objects are returned in `outItems`. No [SecKey](seckey.md) objects are returned unless a key is found in the incoming blob that does not have a matching certificate.

## Return Value

A result code. See [Security Framework Result Codes](security-framework-result-codes.md).

## Discussion

This function uses the `fileNameOrExtension`, `inputFormat`, and `itemType` parameters to help it interpret the incoming data. In most cases, [SecItemImport](<secitemimport(________________).md>) can correctly interpret an external item if none of these are specified, but it is safer for you not to count on that ability.

When the output item type is [kSecItemTypeAggregate](secexternalitemtype/itemtypeaggregate.md), you can use the [CFGetTypeID(_:)](<../corefoundation/cfgettypeid(__).md>) function to determine the Core Foundation type of each item and the functions in `Getting Information About Keychain Services and Types` to determine the keychain item type of each item. For example, the following code determines whether the item is a certificate:

```objc
CFTypeID theID = CFGetTypeID(theItem);
if (SecCertificateGetTypeID() == theID)
```

You can pass in `NULL` for both `outItems` and `importKeychain` to determine what is inside a given external data representation. When you do, the function returns the input format and the item type without modifying the data in any way.
