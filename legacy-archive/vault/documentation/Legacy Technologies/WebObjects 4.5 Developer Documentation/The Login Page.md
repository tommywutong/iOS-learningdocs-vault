---
title: WebObjects 4.5 Developer Documentation
apple_id: TP40006775
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.5/System/Documentation/Developer/WebObjects/WOTools/ToolsTechniques.5d.html
archived_at: '2026-07-15T08:11:09.692461Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 4.5 Developer Documentation](webobjects.md)


__PATH__
[Documentation](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/index.html) __>__ [WebObjects 4.5](webobjects.md) __>__
Tools and Techniques

[!](Using%20Your%20Direct%20to%20Web%20Application.md) [!](Launching%20a%20Direct%20to%20Web%20Application.md) [!](Dynamically%20Generated%20Pages.md)

---

#  The Login Page

When you launch your application, your web browser displays the Direct to Web login screen:

!

The login page is the default implementation of your Main component, __Main.wo__
. It contains text fields to enter a name and password, as well as a submit button (Login) and an Enable Assistant checkbox. To go to the application's default first page, check Enable Assistant and click the Login button. You don't need to enter a name and password, because the default application provides no password-checking logic. If you don't check Enable Assistant before clicking the Login button, you won't have access to the Web Assistant.

You can modify the login page (__Main.wo__
) to provide any behavior or appearance you like. For example, you can add your own password-checking logic.

---

© 1999 Apple Computer, Inc. – (Last Updated July 27 99)

[!](Using%20Your%20Direct%20to%20Web%20Application.md) [!](Launching%20a%20Direct%20to%20Web%20Application.md) [!](Dynamically%20Generated%20Pages.md)

Copyright © 2016 Apple Inc. All rights reserved.

- [Terms of Use](http://www.apple.com/legal/internet-services/terms/site.html)
- [Privacy Policy](http://www.apple.com/privacy/)
