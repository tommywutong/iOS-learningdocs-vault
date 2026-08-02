---
title: WebObjects 5.0 Developer Documentation
apple_id: TP40006776
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_5/DirectToWeb/Architecture/Rendering_t_eb_Template.html
archived_at: '2026-07-15T08:12:23.077850Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 5.0 Developer Documentation](webobjects.md)


|  |
| --- |
| __PATH__[Documentation](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/index.html) __>__ [WebObjects](webobjects.md) |

[![Previous](attachments/DirectToWeb/Images/previous.gif)](Rendering_a__An_Example.md)[![Next](attachments/DirectToWeb/Images/next.gif)](Setting_the_Property_Key.md)

## Rendering the Direct to Web Template

Now the WebObjects framework begins to render the template. [Listing 3-4](#apple-ijdemrckijduq) shows
excerpts from the HTML template for the BASQueryPage Direct to Web
template; the listed portions of the file are discussed in this
example. [Listing 3-5](#apple-ijauuq2gijdec) shows the corresponding sections in the bindings
file.

First, the Direct to Web template displays the page wrapper.
To do so, it needs to resolve the WOComponentName binding for the
PageWrapper WOSwitchComponent (see [Listing 3-5](#apple-ijauuq2gijdec)). A WOSwitchComponent
displays a nested component that has the name specified by its WOComponentName
binding, which in this case is bound to the `d2wContext.pageWrapperName` key.
Since the Direct to Web Context can't find it in its dictionary,
it invokes the rule engine to resolve the key, which fires the rule:

```
*true* => pageWrapperName = "PageWrapper"
```

The Direct to Web context returns "PageWrapper" for the
WOComponentName binding and the WOSwitchComponent displays the application's `PageWrapper.wo` component.
The template continues to render, resolving its keys in a similar
way.

__Listing
3-4 BASQueryPage.html excerpts__

```
<WEBOBJECT NAME=PageWrapper>
.
.
    <WEBOBJECT NAME=ResourceRepetition>
.
.
        ... <WEBOBJECT NAME=ResourceLabel>: ... </WEBOBJECT>
.
.
        <WEBOBJECT NAME=ResourceInputRepresentation></WEBOBJECT>
.
.
    </WEBOBJECT>
</WEBOBJECT>
```

__Listing
3-5 BASQueryPage.wod excerpts__

```
PageWrapper: WOSwitchComponent {
    WOComponentName = pageWrapperName;
    ...
}

ResourceInputRepresentation: WOSwitchComponent {
    WOComponentName = d2wContext.componentName;
    ...
}

ResourceLabel: WOString {
    ...
    value = d2wContext.displayNameForProperty;
}

ResourceRepetition: WORepetition {
    ...
    item = d2wContext.propertyKey;
    list = d2wContext.displayPropertyKeys;
}
```

[![Previous](attachments/DirectToWeb/Images/previous.gif)](Rendering_a__An_Example.md)[![Next](attachments/DirectToWeb/Images/next.gif)](Setting_the_Property_Key.md)

© 2001 Apple Computer, Inc.

Copyright © 2016 Apple Inc. All rights reserved.

- [Terms of Use](http://www.apple.com/legal/internet-services/terms/site.html)
- [Privacy Policy](http://www.apple.com/privacy/)
