---
title: WebObjects 4.5 Developer Documentation
apple_id: TP40006775
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.5/System/Documentation/Developer/WebObjects/JavaClient/JavaClientTutorial.22.html
archived_at: '2026-07-15T08:09:01.615254Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 4.5 Developer Documentation](webobjects.md)


__PATH__
[Documentation](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/index.html) __>__ [WebObjects 4.5](webobjects.md) __>__
Creating a Java Client Application: A Tutorial

[!](Building%20and%20Testing%20Your%20Application.md) [!](Building%20and%20Testing%20Your%20Application.md) [!](Building%20the%20Application.md)

---

#  Testing the Interface

With your current interface you can test-run your application in Interface Builder and try inserting and deleting some Studio objects.

1. 

   Test your interface.

   Choose Document !
   Test Interface (File !
   Test Interface on Windows NT).

   !

You will find that you cannot save your changes to the database. The save fails because the File's Owner object (an instance of a custom subclass of EOInterfaceController) is created on the client side when the application is started. No Yellow Box object corresponding to the File's Owner is available during testing. If you had any custom code, Interface Builder would also have no way to test it. To test the save function or any custom code, you must build the project and then run the application.

---

© 1999 Apple Computer, Inc. – (Last Updated 13 Sep 99)

[!](Building%20and%20Testing%20Your%20Application.md) [!](Building%20and%20Testing%20Your%20Application.md) [!](Building%20the%20Application.md)
