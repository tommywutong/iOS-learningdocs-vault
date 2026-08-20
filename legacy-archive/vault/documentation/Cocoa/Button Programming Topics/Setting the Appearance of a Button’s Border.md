---
title: Button Programming Topics
apple_id: 10000019i
resource_type: Guide
platform: macOS
topic: User Experience
technology: AppKit
published: '2014-10-16'
source_url: https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/Button/Tasks/SettingButtonBorder.html
archived_at: '2026-07-15T07:11:38.113104Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Button Programming Topics](Introduction%20to%20Buttons.md)


[Next](Setting%20a%20Button%E2%80%99s%20Title.md)[Previous](Querying%20Button%20Matrices.md)

# Setting the Appearance of a Button’s Border

You can control what your button’s border looks like by changing its shape and shading. Note that the border doesn’t appear if `isBordered` returns `NO`. Use [setBordered:](https://developer.apple.com/documentation/appkit/nsbutton/1525565-bordered) to change its value.

To change the border’s shape, change the button’s bezel type with [setBezelStyle:](https://developer.apple.com/documentation/appkit/nsbutton/1527022-bezelstyle). There are two major categories of bezel type.

- If your button is identified mainly by text, use [NSRoundedBezelStyle](https://developer.apple.com/documentation/appkit/nsroundedbezelstyle). It uses the appropriate bezel style for a text button, which is a rounded rectangle, like this:

  ![Text button](attachments/Tasks/art/pushbutton.gif)
- If your button is identified mainly by an icon, use [NSRegularSquareBezelStyle](https://developer.apple.com/documentation/appkit/nsregularsquarebezelstyle), [NSThickSquareBezelStyle](https://developer.apple.com/documentation/appkit/nsthicksquarebezelstyle), or [NSThickerSquareBezelStyle](https://developer.apple.com/documentation/appkit/nsthickersquarebezelstyle). These types use a rectangular button with a border. The small style has a 2-pixel border; the medium style, 3-pixel; the large style, 4-pixel. The three types are shown here:

  ![Icon buttons](attachments/Tasks/art/bezelbuttonstyles.gif)

[Next](Setting%20a%20Button%E2%80%99s%20Title.md)[Previous](Querying%20Button%20Matrices.md)

