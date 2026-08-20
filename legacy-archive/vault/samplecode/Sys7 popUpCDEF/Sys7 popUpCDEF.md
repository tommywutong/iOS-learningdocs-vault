---
title: Sys7 popUpCDEF
apple_id: DTS10000620
resource_type: Sample Code
platform: macOS
topic: null
technology: null
published: '2003-01-30'
source_url: https://developer.apple.com/library/archive/samplecode/Sys7_popUpCDEF/Introduction/Intro.html
archived_at: '2026-07-18T03:25:57.580376Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md)


[Next](SimplePopupCDEF.c.md)

# Sys7 popUpCDEF

|  |  |
| --- | --- |
| __Last Revision:__ | Version 1.0, 2003-01-30 First Version |
| __Build Requirements:__ |  |
| __Runtime Requirements:__ | Carbon |

A simple example of using the PopupCDEF available in System 7 and later. This CDEF allows you to create and work with popup menus in windows and dialogs a lot more easily than in the past. You use the same code as for controls. You no longer have to seperate control clicks from PopupClicks, calling TrackControl does the 'InsertMenu/PopupMenuSelect/DeleteMenu' stuff for you. The popupCDEF also handles things like using the window font, adding a resource menu (like a font menu) and other things from within the resource definition, there is less code you have to put in your application. But some things have bitten folks, like making sure the tracking works correctly and the eternal question, "Where's the MenuHandle?". This sample shows those things. Look at the function DoDocumentClick to see how tracking and getting the value of a popup is done, and the function GetPopUpMenuHandle to see the proper way to access the MenuHandle of a popupCDEF popup menu. And of course, look at the Rez file (or look with ResEdit or your favorite resource editior) to see how the different popup setups are defined.

[Next](SimplePopupCDEF.c.md)

