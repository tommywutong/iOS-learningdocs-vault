---
title: WebObjects 4.0 Developer Documentation
apple_id: TP40006774
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.0/System/Documentation/Developer/WebObjects/JavaClient/CSJ_Tutorial.e.html
archived_at: '2026-07-15T08:00:17.974266Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 4.0 Developer Documentation](webobjects.md)


__PATH__
[WebObjects 4.0 Documentation](webobjects.md) __>__
[JavaClient Tutorial](Creating%20a%20Java%20Client%20WebObjects%20Application.md)

_Creating a Java Client WebObjects Application_

[Previous](CSJ_Tutorial.d.md) | [Back Up One Level](CSJ_Tutorial.d.md) | [Next](CSJ_Tutorial.f.md)

###  Client Files

The significant addition to a Java Client project is a subproject named __ClientSideJava.subproj__
. This subproject comes with two preconfigured files: a __.java__
file reflecting the name of the project (in this case, __StudioManager.java__
) and, in the Interfaces "suitcase," an Interface Builder archive (or "nib") file, also named after the project (__StudioManager.nib__
).

####  The Nib File

The nib file in a Java Client application seems identical to nib files in stand-alone Yellow Box applications. You drag objects from palettes onto a window "surface" and these palettes and their objects look exactly like objects in stand-alone. However, these similarities of appearances are deceiving.

When the EOJavaClient palette has been loaded into Interface Builder and you create a user interface, the nib file contains two parallel object graphs, one populated with Yellow Box objects and the other with Swing (JFC) objects. The Swing object graph constitutes a "Java archive" that is loaded onto the client.

####   The Interface Controller

In a Java Client application an interface controller--an EOInterfaceController object--mediates between the applet interface and the model objects on the client. When you use Project Builder to create a Java Client project, it automatically generates code for a custom EOInterfaceController subclass and makes an object of this class the owner of the nib file. The class is named after the project and includes the package prefix of _project_
.__client__
.

In the Model-View-Controller design paradigm, the interface controller plays the role of (obviously) controller. It has four outlets:

- To its __component__
  , which is preset to the window in the nib file and functions as the "view" (it can be set to something else)

- To the client's editing context (__editingContext__
  ), which serves as the "model"

- To the controller display group (__controllerDisplayGroup__
  ), a kind of general-purpose display group that contains the interface controller itself and nothing else; through it the applications can specify user-interface dependencies and can control the interface through associations

To the master display group (__masterDisplayGroup__
) in master-detail interfaces

---

\xA9 1999 Apple Computer, Inc.

[Previous](CSJ_Tutorial.d.md) | [Back Up One Level](CSJ_Tutorial.d.md) | [Next](CSJ_Tutorial.f.md)

Copyright © 2016 Apple Inc. All rights reserved.

- [Terms of Use](http://www.apple.com/legal/internet-services/terms/site.html)
- [Privacy Policy](http://www.apple.com/privacy/)
