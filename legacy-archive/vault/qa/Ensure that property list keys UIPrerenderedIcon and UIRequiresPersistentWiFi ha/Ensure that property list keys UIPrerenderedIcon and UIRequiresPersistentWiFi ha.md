---
title: Ensure that property list keys UIPrerenderedIcon and UIRequiresPersistentWiFi
  have a Boolean value type
apple_id: DTS40008000
resource_type: QA
platform: iOS
topic: Data Management
technology: null
published: '2008-09-18'
source_url: https://developer.apple.com/library/archive/qa/qa1614/_index.html
archived_at: '2026-07-18T02:32:42.285305Z'
---
> 导航：[总目录](../../README.md) · [qa](../../_indexes/qa.md)



Technical Q&A QA1614

# Ensure that property list keys UIPrerenderedIcon and UIRequiresPersistentWiFi have a Boolean value type

## Q:  Why are the keys `UIPrerenderedIcon` and `UIRequiresPersistentWiFi` in my `Info.plist` ignored as of iPhone OS 2.1?

A: Beginning with iPhone OS 2.1 the value type for the keys `UIPrerenderedIcon` and `UIRequiresPersistentWiFi` must be `Boolean`. If these keys are suddenly being ignored it may be because you had succeeded previously by providing a `String` value of "YES". This is no longer supported.

The keys `UIPrerenderedIcon` and `UIRequiresPersistentWiFi` in an iPhone application's `Info.plist` used to allow `String` value type (see Listing 1) in addition to `Boolean`. Starting with iPhone OS 2.1, if you need to set these values, you must ensure that the value type for these keys is set to `Boolean` (see Listing 2). If you do not, these keys will simply be ignored and the default behaviors will persist. In the case of `UIPrerenderedIcon`, this means the application icon would still get the default sheen and bevel effects applied when you didn't intend them. If `UIRequiresPersistentWiFi` is ignored, the WiFi picker may not be displayed and the WiFI connection will close after 30 minutes when you intended it to be maintained for the life of the application.

__Listing 1__  A `String` value was acceptable in iPhone OS 2.0

```
// BAD: This used to work, but will be ignored post 2.0
    <key>UIPrerenderedIcon</key>
    <string>YES</string>
```


__Listing 2__  In iPhone OS 2.1 these keys require a `Boolean` value type

```
// GOOD: This prevents the sheen and bevel effects from being applied to the application icon
    <key>UIPrerenderedIcon</key>
    <true/>
// GOOD: This keeps the current WiFi connection open for the life of the application
    <key>UIRequiresPersistentWiFi</key>
    <true/>
```

Although you may edit the contents of the `Info.plist` directly as shown in Listings 1 and 2, you may prefer to use the Property List Editor application. To use the application, add the desired key to the list, and then use either the Edit menu (shown in Figure 1) or the contextual menu (shown in Figure 2) to set the "Value Type" to `Boolean`.

__Figure 1__  Using the Edit menu in Property List Editor to set `Boolean` value type.

!!

__Figure 2__  Alternatively using the contextual menu in Property List Editor to set `Boolean` value type.

!!

---

#### Document Revision History

| __Date__ | __Notes__ |
| 2008-09-18 | New document that Starting with iPhone OS 2.1, UIPrerenderedIcon and UIRequiresPersistentWiFi must be Boolean or they are ignored. |

