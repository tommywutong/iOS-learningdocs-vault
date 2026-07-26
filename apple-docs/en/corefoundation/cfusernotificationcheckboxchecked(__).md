---
title: 'CFUserNotificationCheckBoxChecked(_:)'
framework: Core Foundation
symbol_kind: func
role: symbol
role_heading: Function
platforms: [macOS 10.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/corefoundation/cfusernotificationcheckboxchecked(_:)'
source_url: 'https://developer.apple.com/documentation/corefoundation/cfusernotificationcheckboxchecked(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/corefoundation/cfusernotificationcheckboxchecked%28_%3A%29.json'
content_hash: 'sha256:be1f8b569544b167'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Foundation](../corefoundation.md)

# CFUserNotificationCheckBoxChecked(_:)

<sub>Function</sub>

Returns a flag used to set or test a checkbox’s state.

<sub>macOS</sub>

```swift
func CFUserNotificationCheckBoxChecked(_ i: CFIndex) -> CFOptionFlags
```

## Parameters

- `i` — The index of the checkbox to set or test. The index corresponds to the order in which the checkbox titles are listed in the [kCFUserNotificationCheckBoxTitlesKey](kcfusernotificationcheckboxtitleskey.md) array of the user notification’s description dictionary. `idx` must be in the range `0` to `7`.

## Return Value

A flag that can be used either to set the state of a checkbox when creating a user notification with [CFUserNotificationCreate](<cfusernotificationcreate(__________).md>) or to test a checkbox’s state returned in a user notification’s response flags, such as from [CFUserNotificationReceiveResponse](<cfusernotificationreceiveresponse(______).md>), when the notification dialog is dismissed.

## See Also

### CFUserNotification Miscellaneous Functions

- [CFUserNotificationCancel](<cfusernotificationcancel(__).md>) — Cancels a user notification dialog.
- [CFUserNotificationCreate](<cfusernotificationcreate(__________).md>) — Creates a CFUserNotification object and displays its notification dialog on screen.
- [CFUserNotificationCreateRunLoopSource](<cfusernotificationcreaterunloopsource(________).md>) — Creates a run loop source for a user notification.
- [CFUserNotificationDisplayAlert](<cfusernotificationdisplayalert(______________________).md>) — Displays a user notification dialog and waits for a user response.
- [CFUserNotificationDisplayNotice](<cfusernotificationdisplaynotice(________________).md>) — Displays a user notification dialog that does not need a user response.
- [CFUserNotificationGetResponseDictionary](<cfusernotificationgetresponsedictionary(__).md>) — Returns the dictionary containing all the text field values from a dismissed notification dialog.
- [CFUserNotificationGetResponseValue](<cfusernotificationgetresponsevalue(______).md>) — Extracts the values of the text fields from a dismissed notification dialog.
- [CFUserNotificationGetTypeID](<cfusernotificationgettypeid().md>) — Returns the type identifier for the `CFUserNotification` opaque type.
- [CFUserNotificationPopUpSelection](<cfusernotificationpopupselection(__).md>) — Returns a flag used to set the selected element of a pop-up menu.
- [CFUserNotificationReceiveResponse](<cfusernotificationreceiveresponse(______).md>) — Waits for the user to respond to a notification or for the notification to time out.
- [CFUserNotificationSecureTextField](<cfusernotificationsecuretextfield(__).md>) — Returns a flag used to set the secure state of a text field.
- [CFUserNotificationUpdate](<cfusernotificationupdate(________).md>) — Updates a displayed user notification dialog with new user interface information.
