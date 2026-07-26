---
title: 'CFUserNotificationCreateRunLoopSource(_:_:_:_:)'
framework: Core Foundation
symbol_kind: func
role: symbol
role_heading: Function
platforms: [macOS 10.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/corefoundation/cfusernotificationcreaterunloopsource(_:_:_:_:)'
source_url: 'https://developer.apple.com/documentation/corefoundation/cfusernotificationcreaterunloopsource(_:_:_:_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/corefoundation/cfusernotificationcreaterunloopsource%28_%3A_%3A_%3A_%3A%29.json'
content_hash: 'sha256:9e3f0846a9292b63'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Foundation](../corefoundation.md)

# CFUserNotificationCreateRunLoopSource(_:_:_:_:)

<sub>Function</sub>

Creates a run loop source for a user notification.

<sub>macOS</sub>

```swift
func CFUserNotificationCreateRunLoopSource(_ allocator: CFAllocator!, _ userNotification: CFUserNotification!, _ callout: CFUserNotificationCallBack!, _ order: CFIndex) -> CFRunLoopSource!
```

## Parameters

- `allocator` — The allocator to use to allocate memory for the new object. Pass `NULL` or kCFAllocatorDefault to use the current default allocator.

- `userNotification` — The user notification to use.

- `callout` — The callback function to invoke when the user notification dialog is dismissed.

- `order` — A priority index indicating the order in which run loop sources are processed. User notifications currently ignore this parameter. Pass `0` for this value.

## Return Value

The new CFRunLoopSource object. Ownership follows the [The Create Rule](https://developer.apple.com/library/archive/documentation/CoreFoundation/Conceptual/CFMemoryMgmt/Concepts/Ownership.html#//apple_ref/doc/uid/20001148-103029).

## Discussion

A run loop source needs to be added to a run loop before it can fire and call its callback function. To add the source to a run loop, use [CFRunLoopAddSource](<cfrunloopaddsource(______).md>).

## See Also

### CFUserNotification Miscellaneous Functions

- [CFUserNotificationCancel](<cfusernotificationcancel(__).md>) — Cancels a user notification dialog.
- [CFUserNotificationCheckBoxChecked](<cfusernotificationcheckboxchecked(__).md>) — Returns a flag used to set or test a checkbox’s state.
- [CFUserNotificationCreate](<cfusernotificationcreate(__________).md>) — Creates a CFUserNotification object and displays its notification dialog on screen.
- [CFUserNotificationDisplayAlert](<cfusernotificationdisplayalert(______________________).md>) — Displays a user notification dialog and waits for a user response.
- [CFUserNotificationDisplayNotice](<cfusernotificationdisplaynotice(________________).md>) — Displays a user notification dialog that does not need a user response.
- [CFUserNotificationGetResponseDictionary](<cfusernotificationgetresponsedictionary(__).md>) — Returns the dictionary containing all the text field values from a dismissed notification dialog.
- [CFUserNotificationGetResponseValue](<cfusernotificationgetresponsevalue(______).md>) — Extracts the values of the text fields from a dismissed notification dialog.
- [CFUserNotificationGetTypeID](<cfusernotificationgettypeid().md>) — Returns the type identifier for the `CFUserNotification` opaque type.
- [CFUserNotificationPopUpSelection](<cfusernotificationpopupselection(__).md>) — Returns a flag used to set the selected element of a pop-up menu.
- [CFUserNotificationReceiveResponse](<cfusernotificationreceiveresponse(______).md>) — Waits for the user to respond to a notification or for the notification to time out.
- [CFUserNotificationSecureTextField](<cfusernotificationsecuretextfield(__).md>) — Returns a flag used to set the secure state of a text field.
- [CFUserNotificationUpdate](<cfusernotificationupdate(________).md>) — Updates a displayed user notification dialog with new user interface information.
