---
title: Resetting Privacy Settings in iOS and macOS
apple_id: DTS40017608
resource_type: QA
platform: iOS|macOS
topic: General
technology: null
published: '2017-02-15'
source_url: https://developer.apple.com/library/archive/qa/qa1906/_index.html
archived_at: '2026-07-18T02:35:33.376804Z'
---
> 导航：[总目录](../../README.md) · [qa](../../_indexes/qa.md)



Technical Q&A QA1906

# Resetting Privacy Settings in iOS and macOS

## Q:  iOS prompted me for access to Contacts when I first launched my app, which uses the NSContactsUsageDescription key. I was not prompted in the subsequent runs of my app. How do I get prompted again?

A: When your app, which uses a purpose string (also called usage description), attempts to access user's data, the system displays a consent alert that allows the user to grant or deny access to them such as the ones shown in Figure 1 and Figure 2.

__Figure 1__  iOS prompting the user for access to Contacts for the MGContacts app.

!

__Figure 2__  macOS prompting the user for access to Contacts for the QuickContacts app.

!

The consent alert only appears the first time your app asks for permission. To display it again, you must reset privacy settings on your device or system.

- For iOS apps, tap Settings > General > Reset > Reset Location & Privacy on your device to reset all location and privacy settings for your app as shown in Figure 3.

__Figure 3__  Tap Reset Location & Privacy to reset privacy settings.

!

- For iOS Simulator apps, delete the app from the Simulator or tap Settings > General > Reset > Reset Location & Privacy in the Simulator to reset all location and privacy settings for your app.
- For macOS apps, use the tccutil command line tool, which allows you to reset access for all applications to a specific service in Terminal as follows:


```
tccutil reset service
```

  where `service` is the name of the service for which privacy settings will be reset. See Listing 1, Listing 2, and Listing 3 for examples on how to reset permissions for Contacts, Calendar, and Reminders, respectively.

  __Listing 1__  Reset all permissions for Contacts.

```
tccutil reset AddressBook
```


  __Listing 2__  Reset all permissions for Calendar.

```
tccutil reset Calendar
```


  __Listing 3__  Reset all permissions for Reminders.

```
tccutil reset Reminders
```

---

#### Document Revision History

| __Date__ | __Notes__ |
| 2017-02-15 | New document that describes how to reset privacy settings for iOS and macOS apps. |

