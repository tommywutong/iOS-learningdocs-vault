---
title: KeyboardAccessory
apple_id: DTS40009462
resource_type: Sample Code
platform: iOS
topic: User Experience
technology: null
published: '2014-04-03'
source_url: https://developer.apple.com/library/archive/samplecode/KeyboardAccessory/Introduction/Intro.html
archived_at: '2026-07-18T03:13:22.159837Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md)


[Next](ReadMe.txt.md)

# KeyboardAccessory

|  |  |
| --- | --- |
| __Last Revision:__ | Version 1.5, 2014-04-03 Upgraded to use Auto Layout. [(Full Revision History)](Document%20Revision%20History.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgnbqgaydsnbwgiwvezlwnfzws33ojbuxg5dpoj4s2rdpnz2ey2lonncwyzlnmvxhiskel4yq) |
| __Build Requirements:__ | iOS 7.0 SDK |
| __Runtime Requirements:__ | iOS 6.0 or later |

Shows how to use a keyboard accessory view.

The application uses a single view controller. The view controller's view contains a UITextView. When you tap the text view, the view controller loads a nib file containing an accessory view that it assigns to the text view's inputAccessoryView property. The accessory view contains a button. When you tap the button, the text "You tapped me." is added to the text view. The sample also shows how you can use the keyboard-will-show and keyboard-will-hide notifications to animate resizing a view that is obscured by the keyboard.

[Next](ReadMe.txt.md)

