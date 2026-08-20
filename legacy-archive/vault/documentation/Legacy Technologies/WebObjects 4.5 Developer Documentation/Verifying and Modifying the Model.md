---
title: WebObjects 4.5 Developer Documentation
apple_id: TP40006775
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.5/System/Documentation/Developer/WebObjects/JavaClient/JavaClientTutorial.1b.html
archived_at: '2026-07-15T08:08:53.830039Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 4.5 Developer Documentation](webobjects.md)


__PATH__
[Documentation](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/index.html) __>__ [WebObjects 4.5](webobjects.md) __>__
Creating a Java Client Application: A Tutorial

[!](Tutorial.md) [!](Other%20Server%20Files.md) [!](Assigning%20Primary%20Keys.md)

---

# Verifying and Modifying the Model

Even if you use an existing model or create a model with the wizard after selecting all the automated functions, you still need to do, or at least verify, the following things:

- 

  Make sure that each entity has a primary key.
- 

  Specify the properties that you don't want displayed, particularly keys.
- 

  Add or modify relationships to the Studio, Movie, Talent, and Movie Role entities.
- 

  Generate source files for the Studio and Talent classes.

1. 

   Open the model file.

   In Project Builder's project browser, click Resources in the leftmost column

   Select __StudioManager__
   __.____eomodeld__
   .

   Double-click the EOModeler document icon, displayed above the right side of the project browser.

   !

   When the model document is opened, the Model Editor (in table mode by default) lists the entities you selected from the Movies database, along with the names of their associated database tables and class names.
2. 

   Add a column for client-side classes.

   If no Client Side Class column appears in the Model Editor, choose Client-Side Class Name from the pop-up list at the bottom of the Model Editor.

   !

   The steps you should perform with EOModeler are described in more detail in the following sections.

#### [Assigning Primary Keys](Assigning%20Primary%20Keys.md#apple-obtwmslehuytambwgq2da)

#### [Removing Primary and Foreign Keys as Class Properties](Removing%20Primary%20and%20Foreign%20Keys%20as%20Class%20Properties.md#apple-obtwm3dehuytambwgq4ti)

---

© 1999 Apple Computer, Inc. – (Last Updated 13 Sep 99)

[!](Tutorial.md) [!](Other%20Server%20Files.md) [!](Assigning%20Primary%20Keys.md)
