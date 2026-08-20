---
title: WebObjects 4.0 Developer Documentation
apple_id: TP40006774
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.0/System/Documentation/Developer/WebObjects/DevGuide/ReusableComponents9.html
archived_at: '2026-07-18T01:20:22.106412Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 4.0 Developer Documentation](webobjects.md)


__PATH__
[WebObjects 4.0 Documentation](webobjects.md) __>__
[WebObjects Developer's Guide](The%20WebObjects%20Developer%27s%20Guide.md)

[!Table of Contents](Creating%20Reusable%20Components.md) [!Previous Section](Search%20Path%20for%20Reusable%20Components.md)

# Designing for Reusability

Here are some points to consider when creating reusable components:

- Make sure that your reusable component generates HTML that can be embedded in the HTML of its parent component.

A reusable component should be designed to be a "good citizen" within the context in which it will be used. Thus, for example, the template file for a reusable component should not start and end with the <HTML> and </HTML> tags (since these tags will be supplied by the parent component). Similarly, it is unlikely that a reusable component's template would contain <BODY>, <HEAD>, or <TITLE> tags.

Further, if you intend your component to be used within a form along with other components, don't declare the form (<FORM...> ... </FORM>) within the reusable component's template file. Instead, let the parent component declare the form. Similar considerations pertain to submit buttons. Since most browsers allow only one submit button within a form, putting a submit button in a reusable component severely limits where it can be used.

- Guard against name conflicts.

Reusable components are identified by name only. See ["Search Path for Reusable Components"](Search%20Path%20for%20Reusable%20Components.md#apple-ha4tq). Those that reside within a particular application's application directory are available only to that application. Those that reside in a framework (for example, __WOExtensions.framework__) are available to all applications that link to it. Suppose you have a component named NavigationControl in your application and one of the frameworks that your application links to also has a NavigationControl component. Which one will be used in your application? The result is indeterminate.

Reusable component names need to be system-wide unique. Consider adding a prefix to component names to increase the likelihood that they will be unique.

- Provide attributes for all significant features.

The more customizable a component is, the more likely it is that people will be able to reuse it. For example, if the AlertPanel component discussed in ["Centralizing Application Resources"](ReusableComponents1.md#apple-giztc) let you set the titles of the hyperlinks (say, to OK and Cancel, or Send Now and Send Later), the panel could be adapted for use in many more applications.

- Provide default values for attributes wherever possible.

Don't require people to set more attributes than are strictly required by the design of your reusable component. In your component's initialization method, you can provide default values for optional attributes. When the component is created, the attribute values specified in the initialization method are used unless others are specified in the parent's declarations file.

For example, the AlertPanel component's __init__ method could set these default values:

```
    - init {
            [super init];
            alertString = @"Alert!";
            alertFontColor = @"#ff0000";
            alertFontSize = 6;

            infoString = @"User should provide an infoString";
            infoFontColor = @"#ff0000";
            infoFontSize = 4;

            borderSize = 2;
            tableWidth = @"50%";
            return self;
    }
```


Then, in a declarations file, you are free to specify all or just a few attributes. This declaration specifies values for all attributes:

_Complete Declaration_

```
    ALERT: AlertPanel {
            infoString = message;
            infoFontSize = 4;
            infoFontColor = "#500000";
            alertString = "New Release";
            alertFontColor = "#A00000";
            alertFontSize = 6;
            tableWidth = "50%";
    };
```


This declaration specifies a value for just one attribute; all others will use the default values provided by the component's __init__ method:

___Partial Declaration___

```
ALERT: AlertPanel {
            alertString = "Choice not available.";
    };
```

- Consider building reusable components from reusable components.

Rather than building a monolithic component, consider how the finished component can be built from several, smaller components. You may be able to employ these smaller components in more than one reusable component.

- Document the reusable component's interface and requirements.

If you plan to make your components available to other programmers, you should provide simple documentation that includes information on:

- What attributes are available and which are required
- What the default values are for optional attributes
- What context needs to be provided for the component. For example, does it need to be embedded in a form?
- Any restrictions that affect its use. For example, is it possible to have a submit button in the same form as the one that contains this component?

In addition, it's helpful if you provide an example showing how to use your component.

[!Table of Contents](Creating%20Reusable%20Components.md) [!Next Section](Managing%20State.md)

Copyright © 2016 Apple Inc. All rights reserved.

- [Terms of Use](http://www.apple.com/legal/internet-services/terms/site.html)
- [Privacy Policy](http://www.apple.com/privacy/)
