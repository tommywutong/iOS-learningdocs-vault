---
title: ABPeoplePickerValueSelectionDidChangeNotification
framework: Address Book
symbol_kind: var
role: symbol
role_heading: Global Variable
platforms: [macOS 10.3+]
languages: [occ]
beta: false
deprecated: false
doc_path: /documentation/addressbook/abpeoplepickervalueselectiondidchangenotification
source_url: 'https://developer.apple.com/documentation/addressbook/abpeoplepickervalueselectiondidchangenotification'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/addressbook/abpeoplepickervalueselectiondidchangenotification.json'
content_hash: 'sha256:d53c134fb888dcf4'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Address Book](../addressbook.md)

# ABPeoplePickerValueSelectionDidChangeNotification

<sub>Global Variable</sub>

Posted when the selection in a multivalue property is changed.

<sub>macOS</sub>

```objc
extern NSString * const ABPeoplePickerValueSelectionDidChangeNotification;
```

## Discussion

The system posts this notification on the main actor.

## See Also

### Notifications

- [ABPeoplePickerGroupSelectionDidChangeNotification](abpeoplepickergroupselectiondidchangenotification.md) — Posted when the selection in the group list is changed.
- [ABPeoplePickerNameSelectionDidChangeNotification](abpeoplepickernameselectiondidchangenotification.md) — Posted when the selection in the name list is changed.
- [ABPeoplePickerDisplayedPropertyDidChangeNotification](abpeoplepickerdisplayedpropertydidchangenotification.md) — Posted when the displayed property in the record list is changed.
