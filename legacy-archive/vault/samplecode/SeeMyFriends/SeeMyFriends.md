---
title: SeeMyFriends
apple_id: DTS10003683
resource_type: Sample Code
platform: macOS
topic: Data Management
technology: SyncServices
published: '2006-10-16'
source_url: https://developer.apple.com/library/archive/samplecode/SeeMyFriends/Introduction/Intro.html
archived_at: '2026-07-18T03:23:37.268431Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md)


[Next](ReadMe.txt.md)

# SeeMyFriends

|  |  |
| --- | --- |
| __Last Revision:__ | Version 1.1, 2006-10-16 Fixed compilation errors (bug #4471526) [(Full Revision History)](Document%20Revision%20History.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgmjqgaydgnrygmwvezlwnfzws33ojbuxg5dpoj4s2rdpnz2ey2lonncwyzlnmvxhiskel4yq) |
| __Build Requirements:__ | Xcode |
| __Runtime Requirements:__ | Mac OS X 10.4 and Later |

SeeMyFriends displays all user's Contact data in a very simple way (first name, last name, picture if present) in a custom HIView whose content is updated when the contacts are changed by another sync client. SeeMyFriends itself does not allow modification of data, and is a read-only sync client. Therefore, it does not have an explicit sync button but instead is expected to be triggered through the mechanism of sync alert. It will however trigger a sync at launch to update its content.
A way to test SeeMyFriends is to change some data (like a first name or last name attribute) in Address Book and wait for the change to be synchronized. It will automatically appear in SeeMyFriends. SeeMyFriends sync data are archived between two launches of the app in a subfolder of ~/Library/Application Support.The archiving is done using the HIArchive mechanism.
SeeMyFriend is using the Model-View-Controller paradigm in a Carbon application and through the use of an Controller object written in Objective-C (SMFWindowController). This object is managing the content of the main window, as well as interaction with SyncServices.

[Next](ReadMe.txt.md)

