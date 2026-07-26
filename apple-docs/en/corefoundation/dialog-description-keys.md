---
title: Dialog Description Keys
framework: Core Foundation
symbol_kind: article
role: collectionGroup
role_heading: API Collection
platforms: []
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/corefoundation/dialog-description-keys
source_url: 'https://developer.apple.com/documentation/corefoundation/dialog-description-keys'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/corefoundation/dialog-description-keys.json'
content_hash: 'sha256:1af2fae6b0545ce6'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Foundation](../corefoundation.md) · [CFUserNotification](cfusernotification.md)

# Dialog Description Keys

<sub>API Collection</sub>

Keys used in a user notification’s description dictionary, which describes the contents of the notification dialog to display.

## Overview

When creating the user notification with [CFUserNotificationCreate](<cfusernotificationcreate(__________).md>), the description dictionary must have a value for [kCFUserNotificationAlertHeaderKey](kcfusernotificationalertheaderkey.md). All other keys are optional.

The button title keys must be given in right-to-left order—you therefore must use the `kCFUserNotificationDefaultButtonTitleKey` constant for the rightmost button even if it is conceptually not a “default” button (for example, if you want a single “Cancel” button that should not have color, should not pulse, and should not have return for a key equivalent). If, however, you set the `kCFUserNotificationNoDefaultButtonFlag`, the rightmost button does not behave as a default button (although it will still be the “default” button in the sense of using `kCFUserNotificationDefaultButtonTitleKey` and `kCFUserNotificationDefaultResponse`). The following code fragment shows how you can create a notification that contains a single “Cancel” button that does not behave as a default button.

```objc
const void* keys[] = {kCFUserNotificationAlertHeaderKey,
                      kCFUserNotificationProgressIndicatorValueKey,
                      kCFUserNotificationDefaultButtonTitleKey};
const void* values[] = {CFSTR("Progress"),
                        kCFBooleanTrue,
                        CFSTR("Cancel")};
CFDictionaryRef parameters = CFDictionaryCreate(0, keys, values,
        sizeof(keys)/sizeof(*keys), &kCFTypeDictionaryKeyCallBacks,
        &kCFTypeDictionaryValueCallBacks);
SInt32 err = 0;
CFUserNotificationCreate(kCFAllocatorDefault, 0,
        kCFUserNotificationPlainAlertLevel | kCFUserNotificationNoDefaultButtonFlag,
        &err, parameters);
```

If you set the `kCFUserNotificationNoDefaultButtonFlag` flag and do not specify a value for `kCFUserNotificationDefaultButtonTitleKey`, the notification will have no buttons.

## Topics

### Constants

- [kCFUserNotificationIconURLKey](kcfusernotificationiconurlkey.md) — A file URL pointing to the icon to display in the dialog.
- [kCFUserNotificationSoundURLKey](kcfusernotificationsoundurlkey.md) — A file URL pointing to a sound that will be played when the alert appears.
- [kCFUserNotificationLocalizationURLKey](kcfusernotificationlocalizationurlkey.md) — A file URL pointing to a bundle that contains localized versions of the strings displayed in the dialog.
- [kCFUserNotificationAlertHeaderKey](kcfusernotificationalertheaderkey.md) — The title of the notification dialog.
- [kCFUserNotificationAlertMessageKey](kcfusernotificationalertmessagekey.md) — The message string to display in the dialog.
- [kCFUserNotificationDefaultButtonTitleKey](kcfusernotificationdefaultbuttontitlekey.md) — The title of the default button.
- [kCFUserNotificationAlternateButtonTitleKey](kcfusernotificationalternatebuttontitlekey.md) — The title of an optional alternate button.
- [kCFUserNotificationOtherButtonTitleKey](kcfusernotificationotherbuttontitlekey.md) — The title of an optional third button.
- [kCFUserNotificationProgressIndicatorValueKey](kcfusernotificationprogressindicatorvaluekey.md) — A value to indicate the progress of an operation.
- [kCFUserNotificationPopUpTitlesKey](kcfusernotificationpopuptitleskey.md) — The list of strings to display in a pop-up menu.
- [kCFUserNotificationTextFieldTitlesKey](kcfusernotificationtextfieldtitleskey.md) — The list of titles for all the text fields to display.
- [kCFUserNotificationCheckBoxTitlesKey](kcfusernotificationcheckboxtitleskey.md) — The list of titles for all the checkboxes or radio buttons to display.
- [kCFUserNotificationTextFieldValuesKey](kcfusernotificationtextfieldvalueskey.md) — The list of values to put into the text fields. If only one text field is to be displayed, you can pass its value string directly without putting it into an array first.
- [kCFUserNotificationPopUpSelectionKey](kcfusernotificationpopupselectionkey.md) — The item that was selected from a pop-up menu.

## See Also

### Constants

- [Alert Levels](1534483-alert-levels.md) — Flags identifying the seriousness of a user notification.
- [Response Codes](1534504-response-codes.md) — Response codes identifying the button that was pressed to dismiss a notification dialog.
- [Button Flags](1534481-button-flags.md) — Flags that alter the display of buttons in a user notification dialog.
- [Alert Levels](1534483-alert-levels.md) — Flags identifying the seriousness of a user notification.
- [Response Codes](1534504-response-codes.md) — Response codes identifying the button that was pressed to dismiss a notification dialog.
- [Button Flags](1534481-button-flags.md) — Flags that alter the display of buttons in a user notification dialog.
