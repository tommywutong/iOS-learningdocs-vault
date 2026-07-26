---
title: abDatabaseChangedExternally
framework: Foundation
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [macOS 10.0+]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: /documentation/foundation/nsnotification/name-swift.struct/abdatabasechangedexternally
source_url: 'https://developer.apple.com/documentation/foundation/nsnotification/name-swift.struct/abdatabasechangedexternally'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsnotification/name-swift.struct/abdatabasechangedexternally.json'
content_hash: 'sha256:d31c048864bb8a3c'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [Foundation](../../../foundation.md) · [NSNotification](../../nsnotification.md) · [Name](../name-swift.struct.md)

# abDatabaseChangedExternally

<sub>Type Property</sub>

Posted when a process other than the current one has changed the Address Book database.

<sub>macOS</sub>

```swift
static let abDatabaseChangedExternally: NSNotification.Name
```

## Discussion

Depending on the operation performed on the address book, one or more of the following keys may be included in the user-info dictionary: `kABInsertedRecords`, `kABUpdatedRecords`, and `kABDeletedRecords`. The values for each of the keys are the unique IDs of the records that were inserted, updated, or deleted, respectively. If the values for all the keys are `nil`, every record has changes. For example, this happens when the Address Book database  is restored from a backup copy.

> [!note] Note
> The system posts this notification on the main actor.

## See Also

### AddressBook

- [abDatabaseChanged](abdatabasechanged.md) — Posted when this process has changed the Address Book database.
- [ABPeoplePickerDisplayedPropertyDidChange](abpeoplepickerdisplayedpropertydidchange.md) — Posted when the displayed property in the record list is changed.
- [ABPeoplePickerGroupSelectionDidChange](abpeoplepickergroupselectiondidchange.md) — Posted when the selection in the group list is changed.
- [ABPeoplePickerNameSelectionDidChange](abpeoplepickernameselectiondidchange.md) — Posted when the selection in the name list is changed.
- [ABPeoplePickerValueSelectionDidChange](abpeoplepickervalueselectiondidchange.md) — Posted when the selection in a multivalue property is changed.
