---
title: WebObjects 4.0 Developer Documentation
apple_id: TP40006774
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.0/System/Documentation/Developer/WebObjects/WOTools/DirectToWeb22.html
archived_at: '2026-07-18T01:24:57.061520Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 4.0 Developer Documentation](webobjects.md)


__PATH__
[WebObjects 4.0 Documentation](webobjects.md) __>__
[WebObjects Tools and Techniques](WebObjects%20Tools%20and%20Techniques.md)

[!Table of Contents](WebObjects%20Tools%20and%20Techniques.md) [!Previous Section](Generating%20Components.md)

# Modifying Your Application's Code

You can modify your application's code just as you would in any other WebObjects application. In addition, there is an API for you to use specifically in Direct to Web applications. This consists of a set of methods defined in the D2W class. Some of these methods allow an object to control the WebAssistant. Others return various components (inspect, query, list, and so on) defined for an entity in a session; the component objects returned must implement the appropriate interface:

```
QueryPageInterface queryPageForEntityNamed (String entity, WOSession
session);
ListPageInterface listPageForEntityNamed (String entity, WOSession
session);
EditPageInterface editPageForEntityNamed (String entity, WOSession
session);
InspectPageInterface inspectPageForEntityNamed (String entity,
WOSession session);
SelectPageInterface selectPageForEntityNamed (String entity,
WOSession session);
EditRelationshipPageInterface editRelationshipPageForEntityNamed
(String entity, WOSession session);
QueryAllPageInterface queryAllPage (WOSession session);
```


You can override these methods to customize the component returned. The __defaultPage__ method of the D2W class is also one you might want to override; this method returns the application's default page which, by default, is the query-all page.
If you make a subclass of D2W to override certain methods, make sure you call the __setFactory__ class method with an instance of the new class as argument.
The following example overrides __defaultPage__:

```
import com.apple.yellow.foundation.*;
import com.apple.yellow.eocontrol.*;
import com.apple.yellow.directtoweb.*;
import com.apple.yellow.webobjects.*;

public class D2WExtendedFactory extends D2W {

    static {
        D2W.setFactory(new D2WExtendedFactory());
    }

    public WOComponent defaultPage (WOSession session) {
        return WOApplication.application().pageWithName("MyDefaultPage",
session.context());
    }

}
```

[!Table of Contents](WebObjects%20Tools%20and%20Techniques.md) [!Next Section](Using%20Direct%20to%20Web%20in%20Other%20WebObjects%20Applications.md)
