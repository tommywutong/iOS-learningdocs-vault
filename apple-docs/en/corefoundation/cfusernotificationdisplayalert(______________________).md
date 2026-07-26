---
title: 'CFUserNotificationDisplayAlert(_:_:_:_:_:_:_:_:_:_:_:)'
framework: Core Foundation
symbol_kind: func
role: symbol
role_heading: Function
platforms: [macOS 10.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/corefoundation/cfusernotificationdisplayalert(_:_:_:_:_:_:_:_:_:_:_:)'
source_url: 'https://developer.apple.com/documentation/corefoundation/cfusernotificationdisplayalert(_:_:_:_:_:_:_:_:_:_:_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/corefoundation/cfusernotificationdisplayalert%28_%3A_%3A_%3A_%3A_%3A_%3A_%3A_%3A_%3A_%3A_%3A%29.json'
content_hash: 'sha256:ecc44e119b1fede3'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Foundation](../corefoundation.md)

# CFUserNotificationDisplayAlert(_:_:_:_:_:_:_:_:_:_:_:)

<sub>Function</sub>

Displays a user notification dialog and waits for a user response.

<sub>macOS</sub>

```swift
func CFUserNotificationDisplayAlert(_ timeout: CFTimeInterval, _ flags: CFOptionFlags, _ iconURL: CFURL!, _ soundURL: CFURL!, _ localizationURL: CFURL!, _ alertHeader: CFString!, _ alertMessage: CFString!, _ defaultButtonTitle: CFString!, _ alternateButtonTitle: CFString!, _ otherButtonTitle: CFString!, _ responseFlags: UnsafeMutablePointer<CFOptionFlags>!) -> Int32
```

## Parameters

- `timeout` — The amount of time to wait for the user to dismiss the notification dialog before the dialog dismisses itself. Pass `0` to have the dialog never time out.

- `flags` — A set of flags describing the type of notification dialog to display. The value is normally just the alert level from [Alert Levels](1534483-alert-levels.md). If you don’t want a default button displayed, perform a bitwise-OR operation with the alert level and the constant [kCFUserNotificationNoDefaultButtonFlag](kcfusernotificationnodefaultbuttonflag.md).

- `iconURL` — A file URL pointing to the icon to display in the dialog. If `NULL`, a default icon is used based on the notification’s alert level specified in `flags`.

- `soundURL` — Not used.

- `localizationURL` — A file URL pointing to a bundle that contains localized versions of the strings displayed in the dialog. Can be `NULL`.

- `alertHeader` — The title of the notification dialog. Cannot be `NULL`.

- `alertMessage` — The message string to display in the dialog. Can be `NULL`.

- `defaultButtonTitle` — The title of the default button. If `NULL`, the string `OK` is used.

- `alternateButtonTitle` — The title of an optional alternate button. Can be `NULL`.

- `otherButtonTitle` — The title of an optional third button. Can be `NULL`.

- `responseFlags` — On return, contains flags identifying how the notification was dismissed. See [Response Codes](1534504-response-codes.md) for details.

## Return Value

`0` if the cancel was successful; a non-`0` value otherwise.

## Discussion

This function blocks the current thread’s execution until the dialog is dismissed, either by the user or by timing out.

## See Also

### CFUserNotification Miscellaneous Functions

- [CFUserNotificationCancel](<cfusernotificationcancel(__).md>) — Cancels a user notification dialog.
- [CFUserNotificationCheckBoxChecked](<cfusernotificationcheckboxchecked(__).md>) — Returns a flag used to set or test a checkbox’s state.
- [CFUserNotificationCreate](<cfusernotificationcreate(__________).md>) — Creates a CFUserNotification object and displays its notification dialog on screen.
- [CFUserNotificationCreateRunLoopSource](<cfusernotificationcreaterunloopsource(________).md>) — Creates a run loop source for a user notification.
- [CFUserNotificationDisplayNotice](<cfusernotificationdisplaynotice(________________).md>) — Displays a user notification dialog that does not need a user response.
- [CFUserNotificationGetResponseDictionary](<cfusernotificationgetresponsedictionary(__).md>) — Returns the dictionary containing all the text field values from a dismissed notification dialog.
- [CFUserNotificationGetResponseValue](<cfusernotificationgetresponsevalue(______).md>) — Extracts the values of the text fields from a dismissed notification dialog.
- [CFUserNotificationGetTypeID](<cfusernotificationgettypeid().md>) — Returns the type identifier for the `CFUserNotification` opaque type.
- [CFUserNotificationPopUpSelection](<cfusernotificationpopupselection(__).md>) — Returns a flag used to set the selected element of a pop-up menu.
- [CFUserNotificationReceiveResponse](<cfusernotificationreceiveresponse(______).md>) — Waits for the user to respond to a notification or for the notification to time out.
- [CFUserNotificationSecureTextField](<cfusernotificationsecuretextfield(__).md>) — Returns a flag used to set the secure state of a text field.
- [CFUserNotificationUpdate](<cfusernotificationupdate(________).md>) — Updates a displayed user notification dialog with new user interface information.
