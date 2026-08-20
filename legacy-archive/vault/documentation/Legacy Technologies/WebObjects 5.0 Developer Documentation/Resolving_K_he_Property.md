---
title: WebObjects 5.0 Developer Documentation
apple_id: TP40006776
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_5/DirectToWeb/Architecture/Resolving_K_he_Property.html
archived_at: '2026-07-15T08:12:23.092742Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 5.0 Developer Documentation](webobjects.md)


|  |
| --- |
| __PATH__[Documentation](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/index.html) __>__ [WebObjects](webobjects.md) |

[![Previous](attachments/DirectToWeb/Images/previous.gif)](Setting_the_Property_Key.md)[![Next](attachments/DirectToWeb/Images/next.gif)](The_Rule_System.md)

## Resolving Keys That Depend on the Property

As the WebObjects framework continues to render the `ResourceRepetition` WORepetition, it
encounters the `ResourceLabel` WOString.
See [Listing 3-4](Rendering_t_eb_Template.md#apple-ijdemrckijduq). The `value` attribute
is bound to `d2wContext.displayNameForProperty`.
This causes the following rule to fire:

```
*true* => displayNameForProperty = "defaultDisplayNameForProperty"
```

The derived value for the `defaultDisplayNameForProperty` key
is implemented by a method that capitalizes the property key in
the context's dictionary, inserts spaces between words with mixed
case, and returns the resulting name "Category", which the template
displays.

Next, the template displays the property-level component that
queries for the `category` attribute.
Since this component is known only at runtime, the Direct to Web
template displays it with a WOSwitchComponent called `ResourceInputRepresentation`.
See [Listing 3-5](Rendering_t_eb_Template.md#apple-ijauuq2gijdec).
The WOSwitchComponent's `WOComponentName` attribute
is bound to `d2wContext.componentName`.
When the context evaluates this key, the following rule fires:

```
((task = "query") and (not(attribute = null))
    and (attribute.valueClassName = "NSString")
    => componentName = "D2WQueryStringComponent"
```

Thus the WOSwitchComponent displays a `D2WQueryStringComponent.wo` reusable component
from the DirectToWeb framework.

The rest of the template renders in a similar way.

[![Previous](attachments/DirectToWeb/Images/previous.gif)](Setting_the_Property_Key.md)[![Next](attachments/DirectToWeb/Images/next.gif)](The_Rule_System.md)

© 2001 Apple Computer, Inc.

Copyright © 2016 Apple Inc. All rights reserved.

- [Terms of Use](http://www.apple.com/legal/internet-services/terms/site.html)
- [Privacy Policy](http://www.apple.com/privacy/)
