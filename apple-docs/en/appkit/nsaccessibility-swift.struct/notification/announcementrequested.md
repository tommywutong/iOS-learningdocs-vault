---
title: announcementRequested
framework: AppKit
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [macOS 10.7+]
languages: [swift, swift, occ]
beta: false
deprecated: false
doc_path: /documentation/appkit/nsaccessibility-swift.struct/notification/announcementrequested
source_url: 'https://developer.apple.com/documentation/appkit/nsaccessibility-swift.struct/notification/announcementrequested'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/appkit/nsaccessibility-swift.struct/notification/announcementrequested.json'
content_hash: 'sha256:5da9fce1fd4c14a0'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [AppKit](../../../appkit.md) · [NSAccessibility](../../nsaccessibility-swift.struct.md) · [Notification](../notification.md)

# announcementRequested

<sub>Type Property</sub>

This notification posts when an app needs to make an announcement to the user. If VoiceOver is enabled, it’s presented via speech and/or braille. Otherwise, it does nothing.

<sub>macOS</sub>

```swift
static let announcementRequested: NSAccessibility.Notification
```

## Discussion

This notification requires a `userInfo` dictionary with the key [NSAccessibilityAnnouncementKey](../notificationuserinfokey/announcement.md) and a localized string containing the announcement. To help an assistive app determine the importance of the announcement, add the appropriate [NSAccessibilityPriorityKey](../notificationuserinfokey/priority.md) to the `userInfo` dictionary.

**Swift**

```swift
let announcement = "The input was invalid."
NSAccessibility.post(
    element: NSApp.mainWindow as Any,
    notification: .announcementRequested,
    userInfo: [
        .announcement: announcement,
        .priority: NSAccessibilityPriorityLevel.medium.rawValue
    ])
```

**Objective-C**

```objc
NSString *announcement = @"The input was invalid.";
NSAccessibilityPostNotificationWithUserInfo(NSApp, NSAccessibilityAnnouncementRequestedNotification, @{
    NSAccessibilityAnnouncementKey : announcement,
    NSAccessibilityPriorityKey : @(NSAccessibilityPriorityMedium) 
});
```

If you need more control over how your announcements are pronounced, such as including punctuation or setting the spoken language, you can use [NSAttributedString](../../../foundation/nsattributedstring.md). For a list of available string attributes, see [NSAttributedString.Key](../../../foundation/nsattributedstring/key.md).

**Swift**

```swift
let announcement = NSAttributedString(
    string: "pain",
    attributes: [.accessibilityLanguage: "fr"]
)
NSAccessibility.post(
    element: NSApp.mainWindow as Any,
    notification: .announcementRequested,
    userInfo: [
        .announcement: announcement,
        .priority: NSAccessibilityPriorityLevel.medium.rawValue
    ])
```

**Objective-C**

```objc
NSAttributedString *announcement =
    [[NSAttributedString alloc] initWithString:@"pain" attributes: @{
    NSAccessibilityLanguageTextAttribute : @"fr"
}];
NSAccessibilityPostNotificationWithUserInfo(NSApp, NSAccessibilityAnnouncementRequestedNotification, @{
    NSAccessibilityAnnouncementKey : announcement,
    NSAccessibilityPriorityKey : @(NSAccessibilityPriorityMedium)
});
```

## See Also

### Notification names

- [NSAccessibilityApplicationActivatedNotification](applicationactivated.md) — This notification is posted after the app has been activated. Post this notification using the [NSAccessibilityPostNotification](<../post(element_notification_).md>) function instead of an `NSNotificationCenter` instance.
- [NSAccessibilityApplicationDeactivatedNotification](applicationdeactivated.md) — This notification is posted after the app has been deactivated.  Post this notification using the [NSAccessibilityPostNotification](<../post(element_notification_).md>) function instead of an `NSNotificationCenter` instance.
- [NSAccessibilityApplicationHiddenNotification](applicationhidden.md) — This notification is posted after the app is hidden. Post this notification using the [NSAccessibilityPostNotification](<../post(element_notification_).md>) function instead of an `NSNotificationCenter` instance.
- [NSAccessibilityApplicationShownNotification](applicationshown.md) — This notification is posted after the app is shown. Post this notification using the [NSAccessibilityPostNotification](<../post(element_notification_).md>) function instead of an `NSNotificationCenter` instance.
- [NSAccessibilityCreatedNotification](created.md) — This notification is posted after an accessibility element is created. Post this notification using the [NSAccessibilityPostNotification](<../post(element_notification_).md>) function instead of an `NSNotificationCenter` instance.
- [NSAccessibilityDrawerCreatedNotification](drawercreated.md) — This notification is posted after a drawer appears. Post this notification using the [NSAccessibilityPostNotification](<../post(element_notification_).md>) function instead of an `NSNotificationCenter` instance.
- [NSAccessibilityFocusedUIElementChangedNotification](focuseduielementchanged.md) — This notification is posted after an accessibility element gains focus. Post this notification using the [NSAccessibilityPostNotification](<../post(element_notification_).md>) function instead of an `NSNotificationCenter` instance.
- [NSAccessibilityFocusedWindowChangedNotification](focusedwindowchanged.md) — This notification is posted after the key window changes. Post this notification using the [NSAccessibilityPostNotification](<../post(element_notification_).md>) function instead of an `NSNotificationCenter` instance.
- [NSAccessibilityHelpTagCreatedNotification](helptagcreated.md) — This notification is posted after a help tag appears. Post this notification using the [NSAccessibilityPostNotification](<../post(element_notification_).md>) function instead of an `NSNotificationCenter` instance.
- [NSAccessibilityLayoutChangedNotification](layoutchanged.md) — This notification is posted after the UI changes in a way that requires the attention of an accessibility client. This notification should be accompanied by a `userInfo` dictionary with the key [NSAccessibilityUIElementsKey](../notificationuserinfokey/uielements.md) and an array containing the UI elements that have been added or changed. Post this notification using the [NSAccessibilityPostNotification](<../post(element_notification_).md>) function instead of an `NSNotificationCenter` instance.
- [NSAccessibilityMainWindowChangedNotification](mainwindowchanged.md) — This notification is posted after the main window changes. Post this notification using the [NSAccessibilityPostNotification](<../post(element_notification_).md>) function instead of an `NSNotificationCenter` instance.
- [NSAccessibilityMovedNotification](moved.md) — This notification is posted after an accessibility element moves. Post this notification using the [NSAccessibilityPostNotification](<../post(element_notification_).md>) function instead of an `NSNotificationCenter` instance.
- [NSAccessibilityResizedNotification](resized.md) — This notification is posted after an accessibility element’s size changes. Post this notification using the [NSAccessibilityPostNotification](<../post(element_notification_).md>) function instead of an `NSNotificationCenter` instance.
- [NSAccessibilityRowCollapsedNotification](rowcollapsed.md) — This notification is posted after a row collapses. Post this notification using the [NSAccessibilityPostNotification](<../post(element_notification_).md>) function instead of an `NSNotificationCenter` instance.
- [NSAccessibilityRowCountChangedNotification](rowcountchanged.md) — This notification is posted after a row is added or deleted. Post this notification using the [NSAccessibilityPostNotification](<../post(element_notification_).md>) function instead of an `NSNotificationCenter` instance.
