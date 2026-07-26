---
title: Button Flags
framework: Core Foundation
symbol_kind: article
role: collectionGroup
role_heading: API Collection
platforms: []
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/corefoundation/1534481-button-flags
source_url: 'https://developer.apple.com/documentation/corefoundation/1534481-button-flags'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/corefoundation/1534481-button-flags.json'
content_hash: 'sha256:2f996bdec375050d'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Foundation](../corefoundation.md) · [CFUserNotification](cfusernotification.md)

# Button Flags

<sub>API Collection</sub>

Flags that alter the display of buttons in a user notification dialog.

## Overview

You specify these flags when you create the user notification with [CFUserNotificationCreate](<cfusernotificationcreate(__________).md>).

## Topics

### Constants

- [kCFUserNotificationNoDefaultButtonFlag](kcfusernotificationnodefaultbuttonflag.md) — Displays the dialog without the default, alternate, or other buttons.
- [kCFUserNotificationUseRadioButtonsFlag](kcfusernotificationuseradiobuttonsflag.md) — Creates a group of radio buttons instead of checkboxes for the elements in the [kCFUserNotificationCheckBoxTitlesKey](kcfusernotificationcheckboxtitleskey.md) array in the user notification’s description dictionary.

## See Also

### Constants

- [Alert Levels](1534483-alert-levels.md) — Flags identifying the seriousness of a user notification.
- [Response Codes](1534504-response-codes.md) — Response codes identifying the button that was pressed to dismiss a notification dialog.
- [Alert Levels](1534483-alert-levels.md) — Flags identifying the seriousness of a user notification.
- [Response Codes](1534504-response-codes.md) — Response codes identifying the button that was pressed to dismiss a notification dialog.
- [Dialog Description Keys](dialog-description-keys.md) — Keys used in a user notification’s description dictionary, which describes the contents of the notification dialog to display.
