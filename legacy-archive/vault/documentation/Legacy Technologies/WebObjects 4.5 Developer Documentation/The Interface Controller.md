---
title: WebObjects 4.5 Developer Documentation
apple_id: TP40006775
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.5/System/Documentation/Developer/WebObjects/JavaClient/JavaClientTutorial.17.html
archived_at: '2026-07-15T08:08:53.699088Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 4.5 Developer Documentation](webobjects.md)


__PATH__
[Documentation](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/index.html) __>__ [WebObjects 4.5](webobjects.md) __>__
Creating a Java Client Application: A Tutorial

[!](Client%20Files.md) [!](The%20Nib%20File.md) [!](Server%20Files.md)

---

#   The Interface Controller

In a Java Client application an interface controller--an EOInterfaceController object--mediates between the applet interface and the model objects on the client. When you use Project Builder to create a Java Client project, it automatically generates code for a custom EOInterfaceController subclass and makes an object of this class the owner of the nib file. The class is named after the project and includes the package prefix of _project_.__client__.

In the Model-View-Controller design paradigm, the interface controller plays the role of (obviously) controller. It has four outlets:

- 

  To its __component__, which is preset to the window in the nib file and functions as the "view" (it can be set to something else)
- 

  To the client's editing context (__editingContext__), which serves as the "model"
- 

  To the controller display group (__controllerDisplayGroup__), a kind of general-purpose display group that contains the interface controller itself and nothing else; through it the applications can specify user-interface dependencies and can control the interface through associations
- 

  To the master display group (__masterDisplayGroup__) in master-detail interfaces

---

© 1999 Apple Computer, Inc. – (Last Updated 13 Sep 99)

[!](Client%20Files.md) [!](The%20Nib%20File.md) [!](Server%20Files.md)
