---
title: 'CFUserNotificationReceiveResponse(_:_:_:)'
framework: Core Foundation
symbol_kind: func
role: symbol
role_heading: Function
platforms: [macOS 10.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/corefoundation/cfusernotificationreceiveresponse(_:_:_:)'
source_url: 'https://developer.apple.com/documentation/corefoundation/cfusernotificationreceiveresponse(_:_:_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/corefoundation/cfusernotificationreceiveresponse%28_%3A_%3A_%3A%29.json'
content_hash: 'sha256:1d7da76bb7a7c541'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Foundation](../corefoundation.md)

# CFUserNotificationReceiveResponse(_:_:_:)

<sub>Function</sub>

Waits for the user to respond to a notification or for the notification to time out.

<sub>macOS</sub>

```swift
func CFUserNotificationReceiveResponse(_ userNotification: CFUserNotification!, _ timeout: CFTimeInterval, _ responseFlags: UnsafeMutablePointer<CFOptionFlags>!) -> Int32
```

## Parameters

- `userNotification` — The user notification to use.

- `timeout` — The amount of time to wait for the user to respond to `userNotification` or for the notification to time out. If neither happens before `timeout` passes, this function returns a non-`0` value. If `timeout` is `0`, the function blocks until the user notification is dismissed.

- `responseFlags` — On return, contains flags identifying how the notification was dismissed, the state of any checkboxes, and the selected element of the pop-up menu. Bits 0-1 of the value hold an identifier for the button pressed by the user (see [Response Codes](1534504-response-codes.md)). Extract the identifier by performing a bitwise-AND operation with `0x3`. Bits 8-15 of `responseFlags` hold the state of up to 8 checkboxes or radio buttons, if present. Extract the flags by performing bitwise-AND operations with the return value of [CFUserNotificationCheckBoxChecked](<cfusernotificationcheckboxchecked(__).md>). Bits 24-31 hold the index number of the element selected in a pop-up menu, if present. Extract the index by performing a 24-bit right shift: `responseFlags >> 24`.

## Return Value

`0` if the call successfully received a response; a non-`0` value otherwise.

## Discussion

Use this function to poll a user notification for a user response. You can call it any number of times on the same user notification.

To avoid polling and blocking your thread’s execution, you can create a run loop source for the user notification with [CFUserNotificationCreateRunLoopSource](<cfusernotificationcreaterunloopsource(________).md>). You will then receive a callback when the dialog is dismissed.

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
- [CFUserNotificationSecureTextField](<cfusernotificationsecuretextfield(__).md>) — Returns a flag used to set the secure state of a text field.
- [CFUserNotificationUpdate](<cfusernotificationupdate(________).md>) — Updates a displayed user notification dialog with new user interface information.
