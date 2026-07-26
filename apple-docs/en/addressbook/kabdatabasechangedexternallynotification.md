---
title: kABDatabaseChangedExternallyNotification
framework: Address Book
symbol_kind: var
role: symbol
role_heading: Global Variable
platforms: [macOS]
languages: [occ]
beta: false
deprecated: false
doc_path: /documentation/addressbook/kabdatabasechangedexternallynotification
source_url: 'https://developer.apple.com/documentation/addressbook/kabdatabasechangedexternallynotification'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/addressbook/kabdatabasechangedexternallynotification.json'
content_hash: 'sha256:529e629391e8db5c'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Address Book](../addressbook.md)

# kABDatabaseChangedExternallyNotification

<sub>Global Variable</sub>

Posted when a process other than the current one has changed the Address Book database.

<sub>macOS</sub>

```objc
extern NSString * const kABDatabaseChangedExternallyNotification;
```

## Discussion

Depending on the operation performed on the address book, one or more of the following keys may be included in the user-info dictionary: `kABInsertedRecords`, `kABUpdatedRecords`, and `kABDeletedRecords`. The values for each of the keys are the unique IDs of the records that were inserted, updated, or deleted, respectively. If the values for all the keys are `nil`, every record has changes. For example, this happens when the Address Book database  is restored from a backup copy.

> [!note] Note
> The system posts this notification on the main actor.

## See Also

### Notifications

- [kABDatabaseChangedNotification](kabdatabasechangednotification.md) — Posted when this process has changed the Address Book database.
