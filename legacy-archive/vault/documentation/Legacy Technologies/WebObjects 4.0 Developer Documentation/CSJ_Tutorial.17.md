---
title: WebObjects 4.0 Developer Documentation
apple_id: TP40006774
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.0/System/Documentation/Developer/WebObjects/JavaClient/CSJ_Tutorial.17.html
archived_at: '2026-07-15T07:59:27.942936Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 4.0 Developer Documentation](webobjects.md)


__PATH__
[WebObjects 4.0 Documentation](webobjects.md) __>__
[JavaClient Tutorial](Creating%20a%20Java%20Client%20WebObjects%20Application.md)

_Creating a Java Client WebObjects Application_

[Previous](CSJ_Tutorial.16.md) | [Back Up One Level](CSJ_Tutorial.16.md) | [Next](CSJ_Tutorial.18.md)

###  Testing the Interface

With your current interface you can test-run your application in Interface Builder and try inserting and deleting some Studio objects.

__1. Test your interface.__

> Choose File !
> Test Interface.
>
> ###### 
>
> !
>
> 
>
> You will find that you cannot save your changes to the database. The save fails because the File's Owner object (an instance of a custom subclass of EOInterfaceController) is instantiated on the client side when the application is started. It has no corresponding Yellow Box object that is available during testing, and thus Interface Builder cannot test it. If you had any custom code, Interface Builder would also have no way to test it. To test the save function or any custom code, you must build the project and then run the application.
>
> ---
>
> \xA9 1999 Apple Computer, Inc.
>
> [Previous](CSJ_Tutorial.16.md) | [Back Up One Level](CSJ_Tutorial.16.md) | [Next](CSJ_Tutorial.18.md)
>
> 
>
> Copyright © 2016 Apple Inc. All rights reserved.
>
> - [Terms of Use](http://www.apple.com/legal/internet-services/terms/site.html)
> - [Privacy Policy](http://www.apple.com/privacy/)
