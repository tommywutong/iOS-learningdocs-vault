---
title: WebObjects 3.5 Developer Documentation
apple_id: TP40006773
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-11-29'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/GettingStarted/GuestBookPlus/GuestBookPlus8.html
archived_at: '2026-07-15T07:54:02.671718Z'
---
> 导航：[总目录](../../../../../../../README.md) · 未编入索引的页面


[!Table of Contents](GuestBookPlusTOC.md) [!Previous Section](GuestBookPlus7.md)

# Keeping Track of Multiple Guests

You've been using the variable __currentGuest__ in the Main component to hold the information entered by the user. You'll need another variable (an array) to store the list of all the guests who have registered.
Before doing this, it is important to understand the scope and life span of variables in WebObjects:

- _Component variables_, such as __currentGuest__, exist for the lifetime of the component. These variables are defined in the component (in this case, __Main.java__) and are accessible only by its methods. Each user that uses a component gets a separate instance of the variable.
- _Session variables_ exist for the lifetime of one user's session and are accessible by all code in the session. They are defined in __Session.java__. An instance of each session variable is created for each user.
- _Application variables_ live as long as the application does and are accessible by all code in the application. They are defined in __Application.java__. A single instance of an application variable is shared by all users of the application.

[!Table of Contents](GuestBookPlusTOC.md) [!Next Section](GuestBookPlus9.md)

Copyright © 2016 Apple Inc. All rights reserved.

- [Terms of Use](http://www.apple.com/legal/internet-services/terms/site.html)
- [Privacy Policy](http://www.apple.com/privacy/)
