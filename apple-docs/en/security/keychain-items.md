---
title: Keychain items
framework: Security
symbol_kind: article
role: collectionGroup
role_heading: API Collection
platforms: []
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/security/keychain-items
source_url: 'https://developer.apple.com/documentation/security/keychain-items'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/security/keychain-items.json'
content_hash: 'sha256:8351ef7794382689'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Security](../security.md) · [Keychain services](keychain-services.md)

# Keychain items

<sub>API Collection</sub>

Embed confidential information in items that you store in a keychain.

## Overview

When you want to store a secret such as a password or cryptographic key, you package it as a keychain item. Along with the data itself, you provide a set of publicly visible attributes both to control the item’s accessibility and to make it searchable. As shown in Figure 1, keychain services handles data encryption and storage (including data attributes) in a keychain, which is an encrypted database stored on disk. Later, authorized processes use keychain services to find the item and decrypt its data.

![](../../../attachments/192ae065b3c41c60bff42cbf95f0d33c/media-2891903@2x.png)

<sub>Diagram showing data being encrypted and then combined with attributes into a keychain item before being stored in a keychain.</sub>

## Topics

### Essentials

- [Using the keychain to manage user secrets](using-the-keychain-to-manage-user-secrets.md) — Relieve the user of remembering small secrets by storing them in the keychain.
- [TN3137: On Mac keychain APIs and implementations](../technotes/tn3137-on-mac-keychains.md) — Learn how the keychain on macOS differs from other Apple platforms.
- [SecKeychainItem](seckeychainitem.md) — An opaque type that represents a keychain item.
- [SecKeychainItemGetTypeID](<seckeychainitemgettypeid().md>) — Returns the unique identifier of the opaque type to which a keychain item object belongs. _(deprecated)_

### Adding keychain items

- [Adding a password to the keychain](adding-a-password-to-the-keychain.md) — Add network credentials to the keychain on behalf of the user.
- [SecItemAdd](<secitemadd(____).md>) — Adds one or more items to a keychain.
- [Item class keys and values](item-class-keys-and-values.md) — Specify the class of a keychain item.
- [Item attribute keys and values](item-attribute-keys-and-values.md) — Specify the attributes of keychain items.

### Keychain item search

- [Searching for keychain items](searching-for-keychain-items.md) — Find keychain items based on search criteria that you specify.
- [SecItemCopyMatching](<secitemcopymatching(____).md>) — Returns one or more keychain items that match a search query, or copies attributes of specific keychain items.
- [Search attribute keys and values](search-attribute-keys-and-values.md) — Filter a keychain item search.
- [Item return result keys](item-return-result-keys.md) — Specify how you want returned keychain item data formatted.

### Keychain item modification

- [Updating and deleting keychain items](updating-and-deleting-keychain-items.md) — Modify items in the keychain when the user’s data changes.
- [SecItemUpdate](<secitemupdate(____).md>) — Modifies items that match a search query.
- [SecItemDelete](<secitemdelete(__).md>) — Deletes items that match a search query.

### Keychain item access

- [Sharing access to keychain items among a collection of apps](sharing-access-to-keychain-items-among-a-collection-of-apps.md) — Enable apps to share keychain items with each other by adding the apps to an access group.
- [Keychain Access Groups Entitlement](../bundleresources/entitlements/keychain-access-groups.md) — The identifiers for the keychain groups that the app may share items with.
- [Restricting keychain item accessibility](restricting-keychain-item-accessibility.md) — Set the conditions under which an app can access a keychain item such as a password.
- [SecAccessControlCreateWithFlags](<secaccesscontrolcreatewithflags(________).md>) — Creates a new access control object with the specified protection type and flags.
- [SecAccessControlCreateFlags](secaccesscontrolcreateflags.md) — Access control constants that dictate how a keychain item may be used.
- [SecAccessControl](secaccesscontrol.md) — An opaque type that contains information about how a keychain item may be used.
- [SecAccessControlGetTypeID](<secaccesscontrolgettypeid().md>) — Returns the unique identifier of the opaque type to which a keychain item access control object belongs.

### Import and export

- [SecItemImport](<secitemimport(________________).md>) — Imports one or more certificates, keys, or identities and optionally adds them to a keychain.
- [SecItemExport](<secitemexport(__________).md>) — Exports one or more certificates, keys, or identities.
- [SecExternalFormat](secexternalformat.md) — The external format of a keychain item.
- [SecExternalItemType](secexternalitemtype.md) — The import item type.
- [SecItemImportExportFlags](secitemimportexportflags.md) — The import and export function flags.
- [SecItemImportExportKeyParameters](secitemimportexportkeyparameters.md) — The import/export parameter structure.
- [SecKeyImportExportFlags](seckeyimportexportflags.md) — The import/export parameter structure flags.
- [SEC_KEY_IMPORT_EXPORT_PARAMS_VERSION](sec_key_import_export_params_version.md) — The import/export parameter structure version.
- [SecKeyImportExportParameters](seckeyimportexportparameters.md) — The legacy import/export parameter structure. _(deprecated)_

### Legacy keychain item creation

- [SecKeychainItemCreateFromContent](<seckeychainitemcreatefromcontent(______________).md>) — Creates a new keychain item from the supplied parameters. _(deprecated)_
- [SecKeychainItemCreateCopy](<seckeychainitemcreatecopy(________).md>) — Copies a keychain item from one keychain to another. _(deprecated)_
- [SecKeychainItemCreatePersistentReference](<seckeychainitemcreatepersistentreference(____).md>) — Creates a persistent reference for a keychain item. _(deprecated)_
- [SecKeychainItemCopyFromPersistentReference](<seckeychainitemcopyfrompersistentreference(____).md>) — Provides a keychain item reference, given a persistent reference. _(deprecated)_
- [SecItemClass](secitemclass.md) — Specifies a keychain item’s class code.

### Legacy keychain item management

- [SecKeychainItemCopyAttributesAndData](<seckeychainitemcopyattributesanddata(____________).md>) — Retrieves the data and/or attributes stored in the given keychain item. _(deprecated)_
- [SecKeychainItemModifyAttributesAndData](<seckeychainitemmodifyattributesanddata(________).md>) — Updates an existing keychain item after changing its attributes or data. _(deprecated)_
- [SecKeychainItemFreeAttributesAndData](<seckeychainitemfreeattributesanddata(____).md>) — Releases the memory used by the keychain attribute list and/or the keychain data retrieved in a call to `SecKeychainItemCopyAttributesAndData`. _(deprecated)_
- [SecKeychainItemCopyContent](<seckeychainitemcopycontent(__________).md>) — Copies the data and attributes stored in the given keychain item. _(deprecated)_
- [SecKeychainItemModifyContent](<seckeychainitemmodifycontent(________).md>) — Updates an existing keychain item after changing its attributes and/or data. _(deprecated)_
- [SecKeychainItemFreeContent](<seckeychainitemfreecontent(____).md>) — Releases the memory used by the keychain attribute list and the keychain data retrieved in a call to the [SecKeychainItemCopyContent](<seckeychainitemcopycontent(__________).md>) function. _(deprecated)_
- [SecKeychainItemCopyKeychain](<seckeychainitemcopykeychain(____).md>) — Returns the keychain object of a given keychain item. _(deprecated)_
- [SecKeychainItemDelete](<seckeychainitemdelete(__).md>) — Deletes a keychain item from the default keychain’s permanent data store. _(deprecated)_
- [SecKeychainAttrType](seckeychainattrtype.md) — The keychain attribute type.
- [SecKeychainAttribute](seckeychainattribute.md) — A structure that holds a single keychain attribute.
- [SecKeychainAttributePtr](seckeychainattributeptr.md) — A pointer to a keychain attribute structure.
- [SecKeychainAttributeList](seckeychainattributelist.md) — A list of keychain attributes.

### Legacy attribute info

- [SecKeychainAttributeInfoForItemID](<seckeychainattributeinfoforitemid(______).md>) — Obtains tags for all possible attributes of a given item class. _(deprecated)_
- [SecKeychainFreeAttributeInfo](<seckeychainfreeattributeinfo(__).md>) — Releases the memory acquired by calling the `SecKeychainAttributeInfoForItemID` function. _(deprecated)_
- [SecKeychainAttributeInfo](seckeychainattributeinfo.md) — A structure that represents an attribute.
- [SecItemAttr](secitemattr.md) — Specifies a keychain item’s attributes.
- [Keychain Item Attribute Constants For Keys](keychain-item-attribute-constants-for-keys.md) — Specifies the attributes for a key item in a keychain.
- [SecAFPServerSignature](secafpserversignature.md) — Represents a 16-byte Apple File Protocol server signature block. _(deprecated)_

### Legacy password storage

- [SecKeychainAddInternetPassword](<seckeychainaddinternetpassword(______________________________).md>) — Adds a new Internet password to a keychain. _(deprecated)_
- [SecKeychainFindInternetPassword](<seckeychainfindinternetpassword(______________________________).md>) — Finds the first Internet password based on the attributes passed. _(deprecated)_
- [SecKeychainAddGenericPassword](<seckeychainaddgenericpassword(________________).md>) — Adds a new generic password to a keychain. _(deprecated)_
- [SecKeychainFindGenericPassword](<seckeychainfindgenericpassword(________________).md>) — Finds the first generic password based on the attributes passed. _(deprecated)_
- [SecProtocolType](secprotocoltype.md) — The protocol type associated with an Internet password.
- [SecAuthenticationType](secauthenticationtype.md) — The authentication type to use for an Internet password.
- [SecPassword](secpassword.md) — Contains information about a password.
