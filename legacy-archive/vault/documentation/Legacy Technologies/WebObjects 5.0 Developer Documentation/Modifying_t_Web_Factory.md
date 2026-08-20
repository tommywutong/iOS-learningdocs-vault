---
title: WebObjects 5.0 Developer Documentation
apple_id: TP40006776
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_5/DirectToWeb/Customizing/Modifying_t_Web_Factory.html
archived_at: '2026-07-15T08:12:23.655677Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 5.0 Developer Documentation](webobjects.md)


|  |
| --- |
| __PATH__[Documentation](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/index.html) __>__ [WebObjects](webobjects.md) |

[![Previous](attachments/DirectToWeb/Images/previous.gif)](Using_Direc_pplications.md)[![Next](attachments/DirectToWeb/Images/next.gif)](Creating_a__l_Component.md)

## Modifying the Direct to Web Factory

You can override the page-creation methods of the D2W class
to customize the components they return. The `defaultPage` method
of the D2W class is one you might want to override; this method
returns the application's default page, which is the query-all
page by default.

If you make a subclass of D2W to override or add certain methods,
make sure you call the `setFactory` class
method with an instance of the new class as the argument.

[Listing 4-4](#apple-ijauer2bifeeq) is an example of how to extend the D2W class.

__Listing
4-4 Customizing the D2W class__

```
import com.webobjects.foundation.*;
import com.webobjects.eocontrol.*;
import com.webobjects.directtoweb.*;
import com.webobjects.appserver.*;

public class D2WExtendedFactory extends D2W {

    public WOComponent defaultPage (WOSession session) {
        return WOApplication.application().
            pageWithName("MyDefaultPage", session.context());
    }
}
```

Add the following Java code to the application constructor
in the `application.java` file:

```
D2W.setFactory(new D2WExtendedFactory());
```

[![Previous](attachments/DirectToWeb/Images/previous.gif)](Using_Direc_pplications.md)[![Next](attachments/DirectToWeb/Images/next.gif)](Creating_a__l_Component.md)

© 2001 Apple Computer, Inc.

Copyright © 2016 Apple Inc. All rights reserved.

- [Terms of Use](http://www.apple.com/legal/internet-services/terms/site.html)
- [Privacy Policy](http://www.apple.com/privacy/)
