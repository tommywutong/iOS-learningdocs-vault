---
title: WebObjects 4.0 Developer Documentation
apple_id: TP40006774
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.0/System/Documentation/Developer/WebObjects/JavaClient/CSJ_Tutorial.12.html
archived_at: '2026-07-15T07:59:18.629507Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 4.0 Developer Documentation](webobjects.md)


__PATH__
[WebObjects 4.0 Documentation](webobjects.md) __>__
[JavaClient Tutorial](Creating%20a%20Java%20Client%20WebObjects%20Application.md)

_Creating a Java Client WebObjects Application_

[Previous](CSJ_Tutorial.11.md) | [Back Up One Level](CSJ_Tutorial.10.md) | [Next](CSJ_Tutorial.13.md)

###  Removing Primary and Foreign Keys as Class Properties

By default, EOModeler makes class properties for all of an entity's attributes (except for non-database attributes that you add to the entity). When an attribute is a class property, it means that the property will be included in your class definition and that it can be fetched from the database. To put it another way, only attributes that are marked as class properties become part of your enterprise objects.

You should only mark as class properties those attributes whose values are meaningful in the objects that are created when you fetch from the database. Attributes that are essentially database artifacts, such as primary and foreign keys, shouldn't be marked as class properties unless the key has meaning to the user and must be displayed in the user interface. For more discussion of primary and foreign keys, see the section [Adding Relationships](CSJ_Tutorial.1b.md#apple-gm3dmmrt)
.

Eliminating primary and foreign keys as class properties has no adverse effect on how Enterprise Objects Framework manages enterprise objects in your application.

__2.

Remove primary and foreign keys as class properties.__

> In the model-entity view of the Model Editor, select the entity you want to modify.
>
> 
>
> Identify an attribute (typically a primary or foreign key) that you do not want to be a class property
>
> 
>
> Click the diamond icon next to the attribute to remove it as a server-side class property.
>
> 
>
> Click the double-arrow icon next to the attribute to remove it as a client-side class property.
>
> 
>
> Save the model by choosing Save from the Model menu.
>
> ###### 
>
> !
>
> 
>
> You'll be returning to EOModeler to enhance your model in later exercises, but for now you're ready to build the first stage of the StudioManager application.
>
> ---
>
> \xA9 1999 Apple Computer, Inc.
>
> [Previous](CSJ_Tutorial.11.md) | [Back Up One Level](CSJ_Tutorial.10.md) | [Next](CSJ_Tutorial.13.md)
>
> 
>
> Copyright © 2016 Apple Inc. All rights reserved.
>
> - [Terms of Use](http://www.apple.com/legal/internet-services/terms/site.html)
> - [Privacy Policy](http://www.apple.com/privacy/)
