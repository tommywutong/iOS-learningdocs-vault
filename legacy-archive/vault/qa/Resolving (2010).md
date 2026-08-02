---
title: Resolving
apple_id: DTS40010234
resource_type: QA
platform: iOS
topic: Xcode
technology: null
published: '2010-08-06'
source_url: https://developer.apple.com/library/archive/qa/qa1705/_index.html
archived_at: '2026-07-18T02:34:14.767973Z'
---
> 导航：[总目录](../README.md) · [qa](../_indexes/qa.md)



Technical Q&A QA1705

# Resolving

## Q:  I have a JavaScript test that successfully automates user interactions in the iPhone Simulator under the iOS SDK 4.0. I upgraded to iOS SDK 4.0.1; Instruments displays "Unexpected error in -[UIATarget_0x.. frontMostApp], /SourceCache/UIAutomation_Sim/UIAutomation-37/Framework/UIATargetElements.m line 437" when I run the above script in the iPhone Simulator.

A: You are getting the "Unexpected error in -[UIATarget_0x.. frontMostApp], /SourceCache/UIAutomation_Sim/UIAutomation-37/Framework/UIATargetElements.m line 437" error message because of a bug in Instruments with iOS SDK 4.0.1.

UI Automation is Accessibility based. As such, the Automation instruments reads and writes an accessibility preference file (specified by `com.apple.Accessibility.plist`) for the iPhone Simulator at


```
~/Library/Application Support/iPhone Simulator/<version> where <version> is an iOS SDK version.
```

In iOS SDK 4.0.1, Automation writes the above file at


```
~/Library/Application Support/iPhone Simulator/4.0
```

but reads it at


```
~/Library/Application Support/iPhone Simulator/4.0.1
```

Automation displays the above error message since `com.apple.Accessibility.plist` does not exist at its expected location. You can workaround this bug by making a symlink between your iPhone Simulator 4.0 and 4.0.1 folders.

Follow these steps to create a symlink between your iPhone Simulator 4.0 and 4.0.1 folders:

1. Quit Instruments and the iPhone Simulator if they are opened.
2. Run the following commands in the Terminal application on your machine:


```
cd ~/Library/Application\ Support/iPhone\ Simulator/
ln -s 4.0.1 4.0
```

---

#### Document Revision History

| __Date__ | __Notes__ |
| 2010-08-06 | New document that describes how to resolve the "UIATarget_0x.. frontMostApp]..UIATargetElements.m line 437" error message in Instruments. |

