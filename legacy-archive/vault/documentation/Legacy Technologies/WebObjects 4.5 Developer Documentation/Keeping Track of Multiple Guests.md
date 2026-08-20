---
title: WebObjects 4.5 Developer Documentation
apple_id: TP40006775
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.5/System/Documentation/Developer/WebObjects/GettingStarted/GettingStarted.1d.html
archived_at: '2026-07-15T08:07:18.786027Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 4.5 Developer Documentation](webobjects.md)


__PATH__
[Documentation](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/index.html) __>__ [WebObjects 4.5](webobjects.md) __>__
Getting Started With WebObjects

---

[!](Enhancing%20Your%20Application.md) [!](Creating%20the%20Guest%20Object.md) [!](Creating%20a%20Guest%20List.md)

---

#  Keeping Track of Multiple Guests

You've been using the variable __currentGuest__ in the Main component to hold the information entered by the user. You'll need another variable (an array) to store the list of all the guests who have registered.

Before doing this, it is important to understand the scope and life span of variables in WebObjects:

- 

  _Component variables,_ such as __currentGuest__, exist for the lifetime of the component. These variables are defined in the component (in this case, __Main.java__) and are accessible only by its methods. Each user that uses a component gets a separate instance of the variable.
- 

  _Session variables_ exist for the lifetime of one user's session and are accessible by all code in the session. They are defined in __Session.java__. An instance of each session variable is created for each user.
- 

  _Application variables_ live as long as the application does and are accessible by all code in the application. They are defined in __Application.java__. A single instance of an application variable is shared by all users of the application.

#### [Creating a Guest List](Creating%20a%20Guest%20List.md#apple-obtwmslehuytemjtg4)

#### [Adding Guests to the Guest List](Adding%20Guests%20to%20the%20Guest%20List.md#apple-obtwmslehu3tsnrr)

---

© 1999 Apple Computer, Inc. – (Last Updated 24 Aug 99)

[!](Enhancing%20Your%20Application.md) [!](Creating%20the%20Guest%20Object.md) [!](Creating%20a%20Guest%20List.md)

Copyright © 2016 Apple Inc. All rights reserved.

- [Terms of Use](http://www.apple.com/legal/internet-services/terms/site.html)
- [Privacy Policy](http://www.apple.com/privacy/)
