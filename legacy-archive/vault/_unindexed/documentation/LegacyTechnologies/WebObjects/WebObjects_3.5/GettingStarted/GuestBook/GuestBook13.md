---
title: WebObjects 3.5 Developer Documentation
apple_id: TP40006773
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-11-29'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/GettingStarted/GuestBook/GuestBook13.html
archived_at: '2026-07-15T07:53:19.949078Z'
---
> 导航：[总目录](../../../../../../../README.md) · 未编入索引的页面


[!Table of Contents](GuestBookTOC.md) [!Previous Section](GuestBook12.md)

## Implementing an Action Method

When the user clicks the Submit button, your application will respond by redisplaying the page with the submitted information shown at the bottom. To make this happen, you implement an _action method_ and bind that method to the __action__ attribute of the WOSubmitButton.

- From the Edit Main.java menu at the bottom of the object browser, choose Add Action.
  !
- Enter submit as the name of your action method.
- From the "Page returned" pop-up menu, select __null__.

The value returned by an action method represents the next page (component) to be displayed. When you return __null__ (or __nil__ if using WebScript), the current page is redrawn. In a later task, you'll see how to return a new component.

- Click Add.

The __submit__ action appears below a horizontal line in the first column of the object browser.

- Click __submit__ in the object browser and drag the cursor to the submit button.

The Inspector opens with the button's __action__ attribute selected.

- Click Connect Variable.

You just bound the __submit__ method you created to the __action__ attribute of the WOSubmitButton. You don't need to write any additional code, so your application is now ready to run. However, you may want to look at your source file.

- From the pull-down menu at the bottom of the window, choose View Source File.

Project Builder becomes active and displays the code for your component (in __Main.java__). You'll notice that this file contains declarations for the variables you created earlier, as well as a declaration for the __submit__ action method.

!

[!Table of Contents](GuestBookTOC.md) [!Next Section](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/GettingStarted/GuestBook/GuestBook14.html)

Copyright © 2016 Apple Inc. All rights reserved.

- [Terms of Use](http://www.apple.com/legal/internet-services/terms/site.html)
- [Privacy Policy](http://www.apple.com/privacy/)
