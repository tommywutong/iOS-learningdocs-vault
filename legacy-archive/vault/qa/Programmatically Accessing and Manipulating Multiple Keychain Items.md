---
title: Programmatically Accessing and Manipulating Multiple Keychain Items
apple_id: DTS10004084
resource_type: QA
platform: macOS
topic: Security
technology: Security
published: '2006-10-03'
source_url: https://developer.apple.com/library/archive/qa/qa1486/_index.html
archived_at: '2026-07-18T02:31:24.980630Z'
---
> 导航：[总目录](../README.md) · [qa](../_indexes/qa.md)



Technical Q&A QA1486

# Programmatically Accessing and Manipulating Multiple Keychain Items

## Q:  Can I sequentially access encrypted Keychain Items, avoiding multiple "Deny/Allow Once/Always Allow" confirmation dialogs?

A: Can I sequentially access encrypted Keychain Items, avoiding multiple "Deny/Allow Once/Always Allow" confirmation dialogs?

No. There is currently no way to avoid the individual confirmation dialogs when using Keychain Manager or Keychain Services APIs, since the data of each retrieved item must first be decrypted before it is returned to the caller. Each item stored in your keychain is individually encrypted with its own unique key. Each of those keys has an access control list that requires the use of the confirmation dialog by default when the key is used to decrypt. Furthermore, these individual keys are themselves encrypted with a master key, which is in turn encrypted with a key derived from your passphrase.

If you don't want or need the old encrypted data content and the new data content is known to you, you can update an item without getting dialogs.

You can do this by:

- copying the old item's attributes and access
- deleting the old item
- creating a new item with the new data containing the old attributes and access

To acquire the old item's attributes and access, pass NULL for the data and data length parameters of functions that return keychain item attributes, such as `SecKeychainItemCopyAttributesAndData` and `SecKeychainItemCopyContent`. You will also need to free the memory associated with the returned attributes and access. This can be done by passing the reference variables to `SecKeychainItemFreeAttributesAndData`.

For a listing of associated functions, check out the [Keychain Services Reference](https://developer.apple.com/documentation/Security/Reference/keychainservices/index.html).

---

#### Document Revision History

| __Date__ | __Notes__ |
| 2006-10-03 | New document that an explanation on what is and is not possible using the SecKeychain API to manipulate Keychain Items. |

