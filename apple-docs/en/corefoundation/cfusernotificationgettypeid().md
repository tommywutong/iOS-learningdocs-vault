---
title: CFUserNotificationGetTypeID()
framework: Core Foundation
symbol_kind: func
role: symbol
role_heading: Function
platforms: [macOS 10.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/corefoundation/cfusernotificationgettypeid()
source_url: 'https://developer.apple.com/documentation/corefoundation/cfusernotificationgettypeid()'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/corefoundation/cfusernotificationgettypeid%28%29.json'
content_hash: 'sha256:6bec4408835b7416'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Foundation](../corefoundation.md)

# CFUserNotificationGetTypeID()

<sub>Function</sub>

Returns the type identifier for the `CFUserNotification` opaque type.

<sub>macOS</sub>

```swift
func CFUserNotificationGetTypeID() -> CFTypeID
```

## Return Value

The type identifier for the `CFUserNotification` opaque type.

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
- [CFUserNotificationPopUpSelection](<cfusernotificationpopupselection(__).md>) — Returns a flag used to set the selected element of a pop-up menu.
- [CFUserNotificationReceiveResponse](<cfusernotificationreceiveresponse(______).md>) — Waits for the user to respond to a notification or for the notification to time out.
- [CFUserNotificationSecureTextField](<cfusernotificationsecuretextfield(__).md>) — Returns a flag used to set the secure state of a text field.
- [CFUserNotificationUpdate](<cfusernotificationupdate(________).md>) — Updates a displayed user notification dialog with new user interface information.
