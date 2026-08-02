---
title: Opening Keyboard Settings from a Keyboard Extension
apple_id: DTS40017508
resource_type: QA
platform: iOS
topic: Interapplication Communication
technology: UIKit
published: '2016-08-02'
source_url: https://developer.apple.com/library/archive/qa/qa1924/_index.html
archived_at: '2026-07-18T02:37:00.069079Z'
---
> 导航：[总目录](../../README.md) · [qa](../../_indexes/qa.md)



Technical Q&A QA1924

# Opening Keyboard Settings from a Keyboard Extension

## Q:  I want to make it easier for the users of my iOS custom keyboard to enable it. How can I open Keyboard Settings from my keyboard extension?

A: iOS custom keyboard extensions can replace the iOS system keyboard with a custom keyboard for use in all apps. To enable a custom keyboard, an iOS user must open the Settings app and navigate to General > Keyboard > Keyboards > Add A New Keyboard.

You can make it easier for your customers to enable your custom keyboard by opening Keyboard settings directly. To do this, you will need to add a URL Type with a URL Scheme of "`prefs`" to your Xcode project, then call `openURL` with the URL scheme shown in Listing 1 from an appropriate UI in your extension or containing app.

__Listing 1__  URL scheme to open Settings app to Keyboards.

```
prefs:root=General&path=Keyboard
```


You need to add a URL Type with a URL Scheme of "`prefs`" to your Xcode project. Without it, iOS will not recognize this URL scheme and the Settings app will not open.

To add a URL Type, open your Xcode project then follow these steps (illustrated in Figure 1):

1. Navigate to your project's Target.
2. Select the Info tab.
3. Open the URL Types disclosure triangle and click the plus (+) button to add a new type.
4. Type in "prefs" in the URL Scheme field. Leave the remaining items at their defaults.

__Figure 1__  Adding a URL Type with a URL Scheme of 'prefs'.

!!

To use this URL scheme in your app, open it as you would any URL (like a web link). Be sure to ask before opening Keyboard settings.

__Listing 2__  Opening Keyboard settings (Swift).

```
let keyboardSettingsURL = NSURL(string: "prefs:root=General&path=Keyboard")
UIApplication.sharedApplication().openURL(keyboardSettingsURL!)
```


__Listing 3__  Opening Keyboard settings (Objective-C).

```
 NSURL *keyboardSettingsURL = [NSURL URLWithString: @"prefs:root=General&path=Keyboard"];
 [[UIApplication sharedApplication] openURL:keyboardSettingsURL];
```


__Listing 4__  Opening Keyboard settings (HTML).

```
<a href="prefs:root=General&path=Keyboard">Open Keyboard settings</a>
```


---

#### Document Revision History

| __Date__ | __Notes__ |
| 2016-08-02 | New document that describes how to open the Keyboard settings from your iOS keyboard extension, making it easier for users to enable your extension. |

