---
title: CFUserNotification
framework: Core Foundation
symbol_kind: class
role: symbol
role_heading: Class
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/corefoundation/cfusernotification
source_url: 'https://developer.apple.com/documentation/corefoundation/cfusernotification'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/corefoundation/cfusernotification.json'
content_hash: 'sha256:cd7c958f511c2067'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Foundation](../corefoundation.md)

# CFUserNotification

<sub>Class</sub>

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
class CFUserNotification
```

## Overview

A `CFUserNotification` object presents a simple dialog on the screen and optionally receives feedback from the user. The contents of the dialog can include a header, a message, an icon, text fields, a pop-up button, radio buttons or checkboxes, and up to three ordinary buttons. Use `CFUserNotification` in processes that do not otherwise have user interfaces, but may need occasional interaction with the user.

You create a user notification with the [CFUserNotificationCreate](<cfusernotificationcreate(__________).md>) function. You pass in a dictionary whose keys describe the items to place into the dialog. (See [Dialog Description Keys](dialog-description-keys.md) for the list of keys.) A set of flags passed to the function determines, among other things, whether secure text fields are used (such as for password fields), whether radio buttons or checkboxes are used, and which of these buttons are checked by default. You can also specify a timeout for the dialog, in which case the dialog cancels itself if the user does not respond in the allotted time period.

A user notification displays its dialog as soon as it is created. If any reply is required, it may be awaited in one of two ways: either synchronously, using [CFUserNotificationReceiveResponse](<cfusernotificationreceiveresponse(______).md>), or asynchronously, using a run loop source created with [CFUserNotificationCreateRunLoopSource](<cfusernotificationcreaterunloopsource(________).md>). [CFUserNotificationReceiveResponse](<cfusernotificationreceiveresponse(______).md>) has a timeout parameter that determines how long it will block (zero meaning indefinitely) and it may be called as many times as necessary until a response arrives. If a user notification has not yet received a response, it may be updated with new information or it may be cancelled. User notifications may not be reused.

`CFUserNotification` provides two convenience functions, [CFUserNotificationDisplayNotice](<cfusernotificationdisplaynotice(________________).md>) and [CFUserNotificationDisplayAlert](<cfusernotificationdisplayalert(______________________).md>), to display very basic dialogs that either require no response from the user or require only a single button to be pressed, respectively.

## Relationships

- **Conforms To**: [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md)

## Topics

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
- [CFUserNotificationUpdate](<cfusernotificationupdate(________).md>) — Updates a displayed user notification dialog with new user interface information.

### Callbacks

- [CFUserNotificationCallBack](cfusernotificationcallback.md) — Callback invoked when an asynchronous user notification dialog is dismissed.

### Constants

- [Alert Levels](1534483-alert-levels.md) — Flags identifying the seriousness of a user notification.
- [Response Codes](1534504-response-codes.md) — Response codes identifying the button that was pressed to dismiss a notification dialog.
- [Button Flags](1534481-button-flags.md) — Flags that alter the display of buttons in a user notification dialog.
- [Alert Levels](1534483-alert-levels.md) — Flags identifying the seriousness of a user notification.
- [Response Codes](1534504-response-codes.md) — Response codes identifying the button that was pressed to dismiss a notification dialog.
- [Button Flags](1534481-button-flags.md) — Flags that alter the display of buttons in a user notification dialog.
- [Dialog Description Keys](dialog-description-keys.md) — Keys used in a user notification’s description dictionary, which describes the contents of the notification dialog to display.

## See Also

### Opaque Types

- [CFAllocator](cfallocator.md)
- [CFArray](cfarray.md)
- [CFAttributedString](cfattributedstring.md)
- [CFBag](cfbag.md)
- [CFBinaryHeap](cfbinaryheap.md)
- [CFBitVector](cfbitvector.md)
- [CFBoolean](cfboolean.md)
- [CFBundle](cfbundle.md)
- [CFCalendar](cfcalendar.md)
- [CFCharacterSet](cfcharacterset.md)
- [CFData](cfdata.md)
- [CFDate](cfdate.md)
- [CFDateFormatter](cfdateformatter.md)
- [CFDictionary](cfdictionary.md)
- [CFError](cferror.md)
