---
title: WebObjects 3.5 Developer Documentation
apple_id: TP40006773
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-11-29'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/GettingStarted/Movies/Movies13.html
archived_at: '2026-07-15T07:54:12.682895Z'
---
> 导航：[总目录](../../../../../../../README.md) · 未编入索引的页面


[!Table of Contents](MoviesTOC.md) [!Previous Section](Movies12.md)

# Examining Your Project

Whenever you create a new project, Project Builder populates the project with ready-made files and directories. What it includes depends on the choices you make in the wizard, so this project has a set of files different from those of the GuestBook project.
Like GuestBook, the Movies project contains a Main component (__Main.wo__) and classes (__Application.java__, __Session.java__, and __Main.java__). It also includes some files that the GuestBook doesn't have: a model file and images used by the Main component.
In Project Builder, navigate to the Movie project's Resources category. This is where the model, named __Movies.eomodeld__, is located. Later in this tutorial you'll use EOModeler to open the model and enhance it.!
Navigate to the Web Server Resources category. This is where your project's images are located: __DBWizardInsert.gif__, __DBWizardUpdate.gif__, and __DBWizardDelete.gif__, for the "Insert/New," "Save to database," and "Delete" buttons, respectively.
The biggest difference between the GuestBook and Movies projects are their Main components. Whereas the Main component you created for the GuestBook project was empty, the Main component for the Movies project contains a fully functional user interface. Also, the __Main.java__ class already contains code that supplies the component with behavior. In the next sections, you'll examine Movies' __Main.wo__ component and its __Main.java__ class.

[!Table of Contents](MoviesTOC.md) [!Next Section](Movies14.md)

Copyright © 2016 Apple Inc. All rights reserved.

- [Terms of Use](http://www.apple.com/legal/internet-services/terms/site.html)
- [Privacy Policy](http://www.apple.com/privacy/)
