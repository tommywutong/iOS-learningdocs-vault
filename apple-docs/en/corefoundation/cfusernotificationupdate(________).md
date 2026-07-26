---
title: 'CFUserNotificationUpdate(_:_:_:_:)'
framework: Core Foundation
symbol_kind: func
role: symbol
role_heading: Function
platforms: [macOS 10.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/corefoundation/cfusernotificationupdate(_:_:_:_:)'
source_url: 'https://developer.apple.com/documentation/corefoundation/cfusernotificationupdate(_:_:_:_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/corefoundation/cfusernotificationupdate%28_%3A_%3A_%3A_%3A%29.json'
content_hash: 'sha256:348d925dac776dd4'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Foundation](../corefoundation.md)

# CFUserNotificationUpdate(_:_:_:_:)

<sub>Function</sub>

Updates a displayed user notification dialog with new user interface information.

<sub>macOS</sub>

```swift
func CFUserNotificationUpdate(_ userNotification: CFUserNotification!, _ timeout: CFTimeInterval, _ flags: CFOptionFlags, _ dictionary: CFDictionary!) -> Int32
```

## Parameters

- `userNotification` — The user notification to update.

- `timeout` — The new timeout value for the dialog.

- `flags` — A set of flags describing the type of notification to display. See [CFUserNotificationCreate](<cfusernotificationcreate(__________).md>) for details.

- `dictionary` — A description of the elements to display in the notification dialog. The possible keys are listed in [Dialog Description Keys](dialog-description-keys.md).

## Return Value

`0` if the cancel was successful; a non-`0` value otherwise.

## See Also

### CFUserNotification Miscellaneous Functions

- [CFUserNotificationCancel](<cfusernotificationcancel(__).md>) — Cancels a user notification dialog.
- [CFUserNotificationCheckBoxChecked](<cfusernotificationcheckboxchecked(__).md>) — Returns a flag used to set or test a checkbox’s state.
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
