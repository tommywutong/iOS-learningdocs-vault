---
title: WebObjects 4.5 Developer Documentation
apple_id: TP40006775
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.5/System/Documentation/Developer/WebObjects/JavaClient/JavaClientTutorial.f.html
archived_at: '2026-07-15T08:09:18.914104Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 4.5 Developer Documentation](webobjects.md)


__PATH__
[Documentation](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/index.html) __>__ [WebObjects 4.5](webobjects.md) __>__
Creating a Java Client Application: A Tutorial

[!](Tutorial.md) [!](Enterprise%20Objects%20and%20Relational%20Databases.md) [!](Creating%20the%20StudioManager%20Project.md)

---

# What Goes Into the StudioManager Application

As with most Java Client WebObjects applications, you create the Java Client StudioManager application using the following ingredients:

- 

  __A model you produce using the EOModeler application provided with Enterprise Objects Framework.__ A model defines a mapping between your enterprise objects and data in a relational database.
- 

  __A user interface.__
  You use Interface Builder to construct a Web-based user interface that can interact with the Java Client. You must load a special palette (__EOJavaClient.palette__) as well as the standard __EOPalette.palette__. With the __EOJavaClient.palette__ you can compose a user interface made from "widgets" derived from the Java Foundation Classes (JFC), informally known as Swing. Your application can also have pages dynamically generated entirely from objects on the server; for help in composing these pages, use WebObjects Builder.
- 

  __Web components__. The Main component is automatically set up to have a WOJavaClientApplet component that is bound to the interface controller on the server. You can add other Web components with or without a Java Client linkage. Also provided are "skeletal" implementation files for the server-side application, session, and direct-action objects as well as API bindings files for server-side components.
- 

  __Source code for enterprise object classes.__ In the StudioManager application, these are Studio and Talent. Movie uses the default enterprise object class, EOGenericRecord, since it has no custom behavior. This is described in more detail in later sections.

In addition, the StudioManager application requires a database server on which you've installed the Movies example database. The final ingredients in the application are the Enterprise Objects Framework, WebObjects and Foundation classes, interfaces, and protocols, which you link into your application.

In this tutorial you'll learn the basic things you must do to create a Java Client WebObjects application. You'll discover how to:

- 

  Create a new project using Project Builder.
- 

  Create a new model based on the Movies database using EOModeler.
- 

  Edit your project's nib file in Interface Builder.
- 

  Write source code for the Studio and Movie enterprise object classes.
- 

  Build your project in Project Builder.

__Related Concepts:__

[What is an Enterprise Object?](What%20is%20an%20Enterprise%20Object.md#apple-obtwmslehuytambwga4dm)

---

© 1999 Apple Computer, Inc. – (Last Updated 13 Sep 99)

[!](Tutorial.md) [!](Enterprise%20Objects%20and%20Relational%20Databases.md) [!](Creating%20the%20StudioManager%20Project.md)
