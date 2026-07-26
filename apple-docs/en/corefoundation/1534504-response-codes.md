---
title: Response Codes
framework: Core Foundation
symbol_kind: article
role: collectionGroup
role_heading: API Collection
platforms: []
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/corefoundation/1534504-response-codes
source_url: 'https://developer.apple.com/documentation/corefoundation/1534504-response-codes'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/corefoundation/1534504-response-codes.json'
content_hash: 'sha256:d75b625716469ec8'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Foundation](../corefoundation.md) · [CFUserNotification](cfusernotification.md)

# Response Codes

<sub>API Collection</sub>

Response codes identifying the button that was pressed to dismiss a notification dialog.

## Overview

To extract this value from the response flags of a dismissed notification (such as returned by [CFUserNotificationReceiveResponse](<cfusernotificationreceiveresponse(______).md>)), you must perform a bitwise-AND operation between the returned response flags and `0x3` before comparing the value to these constants.

## Topics

### Constants

- [kCFUserNotificationDefaultResponse](kcfusernotificationdefaultresponse.md) — The default button was pressed.
- [kCFUserNotificationAlternateResponse](kcfusernotificationalternateresponse.md) — The alternate button was pressed.
- [kCFUserNotificationOtherResponse](kcfusernotificationotherresponse.md) — The third button was pressed.
- [kCFUserNotificationCancelResponse](kcfusernotificationcancelresponse.md) — No button was pressed and the notification timed out.

## See Also

### Constants

- [Alert Levels](1534483-alert-levels.md) — Flags identifying the seriousness of a user notification.
- [Button Flags](1534481-button-flags.md) — Flags that alter the display of buttons in a user notification dialog.
- [Alert Levels](1534483-alert-levels.md) — Flags identifying the seriousness of a user notification.
- [Button Flags](1534481-button-flags.md) — Flags that alter the display of buttons in a user notification dialog.
- [Dialog Description Keys](dialog-description-keys.md) — Keys used in a user notification’s description dictionary, which describes the contents of the notification dialog to display.
