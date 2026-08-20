---
title: Suppressing the "unexpectedly quit" alert
apple_id: DTS10002344
resource_type: QA
platform: macOS
topic: null
technology: null
published: '2008-03-11'
source_url: https://developer.apple.com/library/archive/qa/qa1288/_index.html
archived_at: '2026-07-18T02:30:21.202186Z'
---
> 导航：[总目录](../README.md) · [qa](../_indexes/qa.md)



Technical Q&A QA1288

# Suppressing the "unexpectedly quit" alert

## Q:  How can I suppress the "The application <application> has unexpectedly quit" alert?

A: How can I suppress the "The application <application> has unexpectedly quit" alert?

You can suppress this alert by modifying CrashReporter's modes of operation. CrashReporter has three modes of operation: `Basic,`  `Developer,` and `Server`. See _[CrashReporter](https://developer.apple.com/library/archive/technotes/tn2004/tn2123.html#//apple_ref/doc/uid/DTS10003386)_ for a description of these modes. Use the CrashReporterPrefs or Terminal application to change these modes of operation.

- CrashReporterPrefs - This application was introduced with Mac OS X 10.4 (Xcode 2.0). It is part of the developer tools (/Developer/Applications/Utilities/CrashReporterPrefs.app). Launch CrashReporterPrefs to select a mode of operation.
- Terminal - Type the following command in the Terminal window to choose a mode of operation :

  `defaults write com.apple.CrashReporter DialogType <mode>`

  where `<mode>` represents one of the three operating modes.

  Once modified, `DialogType` will be written to `~/Library/Preferences/com.apple.CrashReporter.plist.`

Use the `CFPreferencesSetAppValue` function to programmatically modify CrashReporter's modes of operation. See Listing 1 for an example of programmatically suppressing the "The application <application> has unexpectedly quit" alert; this example sets `DialogType` to `Developer.`

__Listing 1__  Programmatically suppressing the alert dialog.

```
CFStringRef key = CFSTR("DialogType"); CFStringRef value = CFSTR("Developer"); CFStringRef appID = CFSTR("com.apple.CrashReporter");  CFPreferencesSetAppValue(key, value, appID);
```


- [CFPreferencesSetAppValue](https://developer.apple.com/documentation/corefoundation/1515528-cfpreferencessetappvalue)

---

#### Document Revision History

| __Date__ | __Notes__ |
| 2008-03-11 | Updated content for Mac OS X 10.4 and 10.5. Fixed a typographical error. "~Library/Preferences/com.apple.CrashReporter.plist" should be "~/Library/Preferences/com.apple.CrashReporter.plist." |
| 2003-10-10 | New document that describes how to suppress the "unexpectedly quit" alert. |

