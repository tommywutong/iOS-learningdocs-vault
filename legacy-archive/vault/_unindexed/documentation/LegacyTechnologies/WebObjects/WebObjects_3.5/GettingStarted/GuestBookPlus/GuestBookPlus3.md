---
title: WebObjects 3.5 Developer Documentation
apple_id: TP40006773
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-11-29'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/GettingStarted/GuestBookPlus/GuestBookPlus3.html
archived_at: '2026-07-15T07:53:55.240936Z'
---
> 导航：[总目录](../../../../../../../README.md) · 未编入索引的页面


[!Table of Contents](GuestBookPlusTOC.md) [!Previous Section](GuestBookPlus2.md)

## Binding the Class's Instance Variables to the Form Elements

In the first chapter, you bound the input elements to variables in Main's code. Now you'll modify the bindings to use the class you just created.

- Select Web Components in the first column of the browser.
- Double-click __Main__ in the second column of the browser to open the component in WebObjects Builder.
- Using the Add Variable/Method panel, add a variable called __currentGuest__ to your component and specify its type as Guest. (Note that you can now choose Guest from the Type pop-up menu.)

An entry for __currentGuest__ appears in the object browser. Notice the ">" symbol to the right of its name. This means that there is additional data to be displayed in the second column.

- Select __currentGuest__ in the object browser.

The second column displays the three fields of __currentGuest__, as determined by the definition of its class, Guest.

- Click __guestName__ in the second column of the object browser next to __currentGuest__ and drag the cursor to the Name text field.

This time, when the Inspector opens, there is already a binding for the __value__ attribute (__guestName__), because you bound it in the first tutorial.

- Double-click the row containing the __value__ binding.

This removes the binding for __guestName__ you made previously and binds __currentGuest.guestName__ to the __value__ attribute.

- Bind the other two input elements to __currentGuest.email__ and __currentGuest.comments__.

[!Table of Contents](GuestBookPlusTOC.md) [!Next Section](GuestBookPlus4.md)

Copyright © 2016 Apple Inc. All rights reserved.

- [Terms of Use](http://www.apple.com/legal/internet-services/terms/site.html)
- [Privacy Policy](http://www.apple.com/privacy/)
