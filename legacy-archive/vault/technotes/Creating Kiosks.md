---
title: Creating Kiosks
apple_id: DTS10003090
resource_type: Technical Note
platform: macOS
topic: User Experience
technology: AppKit
published: '2011-04-13'
source_url: https://developer.apple.com/library/archive/technotes/tn2062/_index.html
archived_at: '2026-07-26T19:53:49.813222Z'
---
> 导航：[总目录](../README.md) · [technotes](../_indexes/technotes.md)



Technical Note TN2062

# Creating Kiosks

This technote offers a general overview of the technologies that specifically support kiosk on OS X.

__Important:__ The techniques discussed in this technote are intended only for developers who are working with a vertical market which requires kiosk behavior. Some of these techniques should not be used by developers targeting the mass market of regular Mac OS X users.

[Introduction](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgmjqgaydgmbzgawugsbrfvjukq2ujfhu4mi)[General Kiosk Guidelines](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgmjqgaydgmbzgawugsbrfvjukq2ujfhu4mq)[NSApplication presentationOptions API](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgmjqgaydgmbzgawugsbrfvjukq2ujfhu4my)[Replacing the Finder](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgmjqgaydgmbzgawugsbrfvjukq2ujfhu4na)[Enabling a Firmware Password](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgmjqgaydgmbzgawugsbrfvjukq2ujfhu4ni)[Frequently Asked Kiosk Questions](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgmjqgaydgmbzgawugsbrfvjukq2ujfhu4nq)[How do I prevent users from booting off alternative media (bootable CDs, external hard drives, etc.)?](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgmjqgaydgmbzgawugsbrfvjvkqstivbviskpjy3a)[How do I prevent new media (CDs, DVDs, iPods, USB/Firewire hard drives, etc.) from becoming mounted? How do I prevent media from being ejected?](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgmjqgaydgmbzgawugsbrfvjvkqstivbviskpjy3q)[How do I disable the power button?](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgmjqgaydgmbzgawugsbrfvjvkqstivbviskpjy4a)[How do I disable sleep?](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgmjqgaydgmbzgawugsbrfvjvkqstivbviskpjy4q)[How can I monitor keyboard or mouse events?](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgmjqgaydgmbzgawugsbrfvjvkqstivbviskpjyyta)[Document Revision History](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgmjqgaydgmbzgawvezlwnfzws33ojbuxg5dpoj4s2rdpnz2ey2lonncwyzlnmvxhiskel4yq)

## Introduction

Developers working in vertical markets, for example education, have been creating kiosks or adding kiosk behavior to their applications for quite some time. Specifically, this means the ability to lock the user into a certain application or disable certain operating system functionality normally available. Developers requiring kiosk behavior on computer systems have often been forced to use ad hoc solutions which often were quite hard to maintain over the long-term.

This technote offers a general overview of the technologies that specifically support or are useful to kiosk developers on OS X.

[Back to Top](#)

## General Kiosk Guidelines

Using the techniques and APIs described in this technote, it is possible to force Mac OS X into states which can be very difficult to recover from. For example, using this technote it is fairly trivial to create an application that launches on startup, takes over the entire screen, and cannot be quit. Recovering from this state can be quite complicated if prior preparations have not been made. It is recommended that developers anticipate this possibility, and configure their machines to facilitate recovery. Apple recommends that all kiosk developers take the following steps:

- Disable automatic login.
- Create an alternate admin account exclusively for recovering from misconfigurations.
- Whenever possible, test all changes in a single user account rather than applying them to the entire system.

With this configuration, if a problem occurs and the active account is no longer functional, recovery is fairly trivial. Simply log into the recovery account and use that admin account to clear up whatever misconfiguration issue is causing problems.

[Back to Top](#)

## NSApplication presentationOptions API

Starting in Mac OS X 10.5, the older `SystemUIMode` API has been replaced by the NSApplication `presentationOptions` API. `SetSystemUIMode` and `GetSystemUIMode` have not been formally deprecated, but the newer NSApplication API should generally be used instead. The `presentationOptions` API is documented as part of NSApplication; the full details can be found in the [NSApplication Class Reference](https://developer.apple.com/library/mac/#documentation/Cocoa/Reference/ApplicationKit/Classes/NSApplication_Class/Reference/Reference.html).

Both `presentationOptions` and `currentSystemPresentationOptions` are KVO-observable. A client that observes `currentSystemPresentationOptions` will receive notifications under three different circumstances.

- The observing app is the active application, and makes a change itself using either `-setPresentationOptions:` or `SetSystemUIMode`.
- Another application is active, and makes such changes of its own.
- Making a different application active causes the current set of presentation options to change.

[Back to Top](#)

## Replacing the Finder

In Mac OS X, launchd is responsible for the automatic processes and daemons including the Finder. For more information on launchd, see the following documents:

- [launchd man page](x-man-page://launchd)
- [Creating launchd Daemons and Agents](https://developer.apple.com/mac/library/documentation/MacOSX/Conceptual/BPSystemStartup/Articles/LaunchOnDemandDaemons.html)
- [Technical Note TN2083: Daemons and Agents](https://developer.apple.com/mac/library/technotes/tn2005/tn2083.html)

In Mac OS X 10.6, the plist that actually controls Finder launching is the file `com.apple.Finder.plist` found in `/System/Library/LaunchAgents`. The plist structure is quite simple, and you can change the global `Finder` by changing the `Program` property of that plist. However, it is generally preferable to override the system-wide `Finder` by placing a modified plist in `/Library/LaunchAgents`. In addition, you can also override the `Finder` on a per-user basis by adding a custom plist to the `~/Library/LaunchAgents` of that user's home folder.

[Back to Top](#)

## Enabling a Firmware Password

The firmware password is a security feature available on Mac OS X systems. Enabling the firmware password prevents users from choosing the startup disk at boot, as well as disabling a number of other features that would be inappropriate in a kiosk environment.

There is currently no public programmatic solution to setting the firmware password (r. 3075615). This means this setting cannot be set by an installer. However, an administrator can enable using the process described in [Setting up firmware password protection in Mac OS X](http://support.apple.com/kb/ht1352). This document also contains more details on what activities the firmware password will restrict.

__Important:__ The firmware password can be reset by a user who gains physical access to the inside of the computer. Systems which use a firmware password need to be protected from users gaining physical access to the internals of the computer.

[Back to Top](#)

## Frequently Asked Kiosk Questions

### How do I prevent users from booting off alternative media (bootable CDs, external hard drives, etc.)?

Among other things, enabling a firmware password prevents the user from selecting a different startup device when booting. See the section Enabling a Firmware Password for more information.

### How do I prevent new media (CDs, DVDs, iPods, USB/Firewire hard drives, etc.) from becoming mounted? How do I prevent media from being ejected?

`DiskArbitration` is the framework responsible for managing all mounting and ejecting on the system. Using `DiskArbitration`, you can screen devices before mount and respond in a variety of ways, including blocking the mount attempt or forcing a volume to mount read-only. For more information on `DiskArbitration`, see the [DiskArbitration Framework Reference](https://developer.apple.com/library/mac/#documentation/Darwin/Reference/DiscArbitrationFramework/DiskArbitration_h/index.html).

__Important:__ It is possible to bypass `DiskArbitration` and mount a volume manually using the [mount command](x-man-page://mount). If a kiosk app needs to prevent or control mounting, it should also consider preventing users from directly executing shell commands, either through `Terminal` or through other indirect means.

### How do I disable the power button?

There is currently no supported way to disable the power button. Developers concerned about forced reboots should secure the computer's boot process using a firmware password.

### How do I disable sleep?

This is described by [Technical Q&A QA1340: Registering and unregistering for sleep and wake notifications](https://developer.apple.com/library/mac/#qa/qa1340/_index.html). It includes information on how to monitor and prevent sleep.

### How can I monitor keyboard or mouse events?

Quartz Event Taps allow an application to observe and alter the stream of low-level user input events before their delivery. Using this API, it is possible to create, hide, or modify a variety of keyboard events before they reach the higher level system. For more information on this API, see the [Quartz Event Services Reference](https://developer.apple.com/library/mac/#documentation/Carbon/Reference/QuartzEventServicesRef/Reference/reference.html).

[Back to Top](#)

---

#### Document Revision History

| __Date__ | __Notes__ |
| 2011-04-13 | revison information |
| 2003-02-24 | Discusses techniques used in creating applications which require kiosk-like functionality on Mac OS X. |
|  | New document that discusses techniques used in creating applications which require kiosk-like functionality on Mac OS X. |

