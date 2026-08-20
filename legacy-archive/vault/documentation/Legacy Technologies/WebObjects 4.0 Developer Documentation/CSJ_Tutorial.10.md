---
title: WebObjects 4.0 Developer Documentation
apple_id: TP40006774
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.0/System/Documentation/Developer/WebObjects/JavaClient/CSJ_Tutorial.10.html
archived_at: '2026-07-15T07:59:15.617756Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 4.0 Developer Documentation](webobjects.md)


__PATH__
[WebObjects 4.0 Documentation](webobjects.md) __>__
[JavaClient Tutorial](Creating%20a%20Java%20Client%20WebObjects%20Application.md)

_Creating a Java Client WebObjects Application_

[Previous](CSJ_Tutorial.f.md) | [Back Up One Level](Creating%20a%20Java%20Client%20WebObjects%20Application.md) | [Next](CSJ_Tutorial.11.md)

##  Verifying and Modifying the Model

Even if you use an existing model or create a model with the wizard after selecting all the automated functions, you still need to do, or at least verify, the following things:

- Make sure that each entity has a primary key.
  
- Specify the properties that you don't want displayed, particularly keys.
  
- Add or modify relationships to the Studio, Movie, Talent, and Movie Role entities.
  - Generate source files for the Studio and Talent classes.

    __1. Open the model file.__

    > In Project Builder's project browser, click Resources in the leftmost column
    >
    > 
    >
    > Select __StudioManager.__
    > __eomodeld__
    > .
    >
    > 
    >
    > Double-click the EOModeler document icon, displayed above the right side of the project browser.
    >
    > ###### 
    >
    > !
    >
    > ###### 
    >
    > 
    >
    > When the model document is opened, the Model Editor (in table mode by default) lists the entities you selected from the Movies database, along with the names of their associated database tables and class names.

    __2. Add a column for client-side classes.__

    > If no Client Side Class column appears in the Model Editor, choose Client-Side Class Name from the pop-up list at the bottom of the Model Editor.
    >
    > ###### 
    >
    > !
    >
    > 
    >
    > The steps you should perform with EOModeler are described in more detail in the following sections.
    >
    > ---
    >
    > \xA9 1999 Apple Computer, Inc.
    >
    > [Previous](CSJ_Tutorial.f.md) | [Back Up One Level](Creating%20a%20Java%20Client%20WebObjects%20Application.md) | [Next](CSJ_Tutorial.11.md)
    >
    > 
    >
    > Copyright © 2016 Apple Inc. All rights reserved.
    >
    > - [Terms of Use](http://www.apple.com/legal/internet-services/terms/site.html)
    > - [Privacy Policy](http://www.apple.com/privacy/)
