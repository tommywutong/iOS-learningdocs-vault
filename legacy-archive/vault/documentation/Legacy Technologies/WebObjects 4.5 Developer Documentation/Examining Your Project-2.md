---
title: WebObjects 4.5 Developer Documentation
apple_id: TP40006775
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.5/System/Documentation/Developer/WebObjects/GettingStarted/GettingStarted.33.html
archived_at: '2026-07-15T08:07:46.958365Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 4.5 Developer Documentation](webobjects.md)


__PATH__
[Documentation](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/index.html) __>__ [WebObjects 4.5](webobjects.md) __>__
Getting Started With WebObjects

---

[!](Creating%20a%20WebObjects%20Database%20Application.md) [!](Running%20Movies.md) [!](Examining%20the%20Variables.md)

---

#  Examining Your Project

Whenever you create a new project, Project Builder populates the project with ready-made files and directories. What it includes depends on the choices you make in the wizard, so this project has a set of files different from those of the GuestBook project.

Like GuestBook, the Movies project contains a Main component (__Main.wo__). It also includes some files that the GuestBook doesn't have: classes (__Application.java__, __Session.java__, __DirectAction.java__, and __Main.java__), a model file, and images used by the Main component.

In Project Builder, navigate to the Movie project's Resources category. This is where the model, named __Movies.eomodeld__, is located. Later in this tutorial you'll use EOModeler to open the model and enhance it.!

Navigate to the Web Server Resources category. This is where your project's images are located: __DBWizardUpdate.gif__, __DBWizardDelete.gif__, and __DBWizardInsert.gif__, for the "Save to database," "Delete", and "Insert/New" buttons, respectively.

The biggest difference between the GuestBook and Movies projects is their Main components. Whereas the Main component you created for the GuestBook project was empty, the Main component for the Movies project contains a fully functional user interface. Also, the __Main.java__ class already contains code that supplies the component with behavior. In the next sections, you'll examine the Movies project's __Main.wo__ component and its __Main.java__ class.

#### [Examining the Variables](Examining%20the%20Variables.md#apple-obtwmslehuytenbqgi)

#### [Examining the Bindings](Examining%20the%20Bindings.md#apple-obtwmslehuytinjzga)

---

© 1999 Apple Computer, Inc. – (Last Updated 24 Aug 99)

[!](Creating%20a%20WebObjects%20Database%20Application.md) [!](Running%20Movies.md) [!](Examining%20the%20Variables.md)

Copyright © 2016 Apple Inc. All rights reserved.

- [Terms of Use](http://www.apple.com/legal/internet-services/terms/site.html)
- [Privacy Policy](http://www.apple.com/privacy/)
