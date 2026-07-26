---
title: 'CFUserNotificationCreate(_:_:_:_:_:)'
framework: Core Foundation
symbol_kind: func
role: symbol
role_heading: Function
platforms: [macOS 10.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/corefoundation/cfusernotificationcreate(_:_:_:_:_:)'
source_url: 'https://developer.apple.com/documentation/corefoundation/cfusernotificationcreate(_:_:_:_:_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/corefoundation/cfusernotificationcreate%28_%3A_%3A_%3A_%3A_%3A%29.json'
content_hash: 'sha256:27bc50571d3084e3'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Foundation](../corefoundation.md)

# CFUserNotificationCreate(_:_:_:_:_:)

<sub>Function</sub>

Creates a CFUserNotification object and displays its notification dialog on screen.

<sub>macOS</sub>

```swift
func CFUserNotificationCreate(_ allocator: CFAllocator!, _ timeout: CFTimeInterval, _ flags: CFOptionFlags, _ error: UnsafeMutablePointer<Int32>!, _ dictionary: CFDictionary!) -> CFUserNotification!
```

## Parameters

- `allocator` — The allocator to use to allocate memory for the new object. Pass `NULL` or kCFAllocatorDefault to use the current default allocator.

- `timeout` — The time to wait before the notification dialog dismisses itself if the user does not respond. If `0`, the notification never times out.

- `flags` — A set of flags describing the type of notification to display. These flags specify an alert level for the notification (see [Alert Levels](1534483-alert-levels.md)), determine whether radio buttons or checkboxes are to be used (see [Button Flags](1534481-button-flags.md)), specify which, if any, of these buttons are checked by default (see [CFUserNotificationCheckBoxChecked](<cfusernotificationcheckboxchecked(__).md>)), specify whether any of the text fields are to be secure text fields (see [CFUserNotificationSecureTextField](<cfusernotificationsecuretextfield(__).md>)), and determine which element of a pop-up menu, if present, should be selected by default (see [CFUserNotificationPopUpSelection](<cfusernotificationpopupselection(__).md>)). Combine these flags together by performing a bitwise-OR operation with all the individual flags.

- `error` — On return contains an integer error code. If `0`, the user notification was successfully created and displayed.

- `dictionary` — A description of the elements to display in the notification dialog. The possible keys are listed in [Dialog Description Keys](dialog-description-keys.md). The dictionary must contain a value for the key [kCFUserNotificationAlertHeaderKey](kcfusernotificationalertheaderkey.md), but the other keys are optional.

## Return Value

The new CFUserNotification object. Ownership follows the [The Create Rule](https://developer.apple.com/library/archive/documentation/CoreFoundation/Conceptual/CFMemoryMgmt/Concepts/Ownership.html#//apple_ref/doc/uid/20001148-103029).

## See Also

### CFUserNotification Miscellaneous Functions

- [CFUserNotificationCancel](<cfusernotificationcancel(__).md>) — Cancels a user notification dialog.
- [CFUserNotificationCheckBoxChecked](<cfusernotificationcheckboxchecked(__).md>) — Returns a flag used to set or test a checkbox’s state.
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
