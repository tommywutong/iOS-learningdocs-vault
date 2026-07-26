---
title: 'CFUserNotificationGetResponseValue(_:_:_:)'
framework: Core Foundation
symbol_kind: func
role: symbol
role_heading: Function
platforms: [macOS 10.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/corefoundation/cfusernotificationgetresponsevalue(_:_:_:)'
source_url: 'https://developer.apple.com/documentation/corefoundation/cfusernotificationgetresponsevalue(_:_:_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/corefoundation/cfusernotificationgetresponsevalue%28_%3A_%3A_%3A%29.json'
content_hash: 'sha256:6ba7bc3ed1a14671'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Foundation](../corefoundation.md)

# CFUserNotificationGetResponseValue(_:_:_:)

<sub>Function</sub>

Extracts the values of the text fields from a dismissed notification dialog.

<sub>macOS</sub>

```swift
func CFUserNotificationGetResponseValue(_ userNotification: CFUserNotification!, _ key: CFString!, _ idx: CFIndex) -> CFString!
```

## Parameters

- `userNotification` — The user notification to use.

- `key` — The dictionary key identifying the text fields to use. Currently, only [kCFUserNotificationTextFieldValuesKey](kcfusernotificationtextfieldvalueskey.md) is supported.

- `idx` — The index of the text field value to return. The index corresponds to the order in which text fields are listed in the [kCFUserNotificationTextFieldTitlesKey](kcfusernotificationtextfieldtitleskey.md) array in the user notification’s description dictionary.

## Return Value

The value of the text field identified by `key` and `idx`. Ownership follows the [The Get Rule](https://developer.apple.com/library/archive/documentation/CoreFoundation/Conceptual/CFMemoryMgmt/Concepts/Ownership.html#//apple_ref/doc/uid/20001148-SW1).

## See Also

### CFUserNotification Miscellaneous Functions

- [CFUserNotificationCancel](<cfusernotificationcancel(__).md>) — Cancels a user notification dialog.
- [CFUserNotificationCheckBoxChecked](<cfusernotificationcheckboxchecked(__).md>) — Returns a flag used to set or test a checkbox’s state.
- [CFUserNotificationCreate](<cfusernotificationcreate(__________).md>) — Creates a CFUserNotification object and displays its notification dialog on screen.
- [CFUserNotificationCreateRunLoopSource](<cfusernotificationcreaterunloopsource(________).md>) — Creates a run loop source for a user notification.
- [CFUserNotificationDisplayAlert](<cfusernotificationdisplayalert(______________________).md>) — Displays a user notification dialog and waits for a user response.
- [CFUserNotificationDisplayNotice](<cfusernotificationdisplaynotice(________________).md>) — Displays a user notification dialog that does not need a user response.
- [CFUserNotificationGetResponseDictionary](<cfusernotificationgetresponsedictionary(__).md>) — Returns the dictionary containing all the text field values from a dismissed notification dialog.
- [CFUserNotificationGetTypeID](<cfusernotificationgettypeid().md>) — Returns the type identifier for the `CFUserNotification` opaque type.
- [CFUserNotificationPopUpSelection](<cfusernotificationpopupselection(__).md>) — Returns a flag used to set the selected element of a pop-up menu.
- [CFUserNotificationReceiveResponse](<cfusernotificationreceiveresponse(______).md>) — Waits for the user to respond to a notification or for the notification to time out.
- [CFUserNotificationSecureTextField](<cfusernotificationsecuretextfield(__).md>) — Returns a flag used to set the secure state of a text field.
- [CFUserNotificationUpdate](<cfusernotificationupdate(________).md>) — Updates a displayed user notification dialog with new user interface information.
