---
title: WebObjects 4.0 Developer Documentation
apple_id: TP40006774
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.0/System/Documentation/Developer/WebObjects/DevGuide/DynamicElements2.html
archived_at: '2026-07-18T01:20:08.916699Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 4.0 Developer Documentation](webobjects.md)


__PATH__
[WebObjects 4.0 Documentation](webobjects.md) __>__
[WebObjects Developer's Guide](The%20WebObjects%20Developer%27s%20Guide.md)

[!Table of Contents](Dynamic%20Elements.md) [!Previous Section](Server-Side%20Dynamic%20Elements.md)

## How Server-Side Dynamic Elements Work

To learn how server-side dynamic elements work, consider how the example page shown in [Figure 10](Server-Side%20Dynamic%20Elements.md#apple-gqzdima) would look in WebObjects Builder's raw mode:

```
Choose between the following menu options:<BR><BR>
<WEBOBJECT NAME="OPTION_REPETITION">
    <WEBOBJECT NAME="OPTION_LINK">
        <WEBOBJECT NAME="OPTION_NAME"></WEBOBJECT>
    </WEBOBJECT>
</WEBOBJECT>
```


Each WEBOBJECT tag denotes the position of a dynamic element. Notice that the tag specifies only where the dynamic element should go; it does not specify the dynamic element's type. The type is specified in the __.wod__ file:

```
OPTION_REPETITION:WORepetition {
        list = allOptions;
        item = currentOption
};
OPTION_LINK:WOHyperlink {
        action = pickOption
};
OPTION_NAME:WOString {
        value = currentOption
};
```


In the __.wod__ file, each element is identified by name and then its type is specified. The outermost dynamic element in the HTML file (OPTION_REPETITION) defines a WORepetition, the next element is a WOHyperlink, and the innermost element is a WOString.
Each type specification is followed by a list of _attributes_. Dynamic elements define several attributes that you bind to different values to configure the element for your application. Usually, you bind attributes to variables or methods from your component's code (see [Figure 12](#apple-gqztcoi)).

!

Figure 12. Dynamic Element Bindings

In our example, the Main component binds to two attributes of WORepetition: __list__ and __item__. The __list__ attribute specifies the list that the WORepetition should iterate over. The __item__ attribute specifies a variable whose value will be updated in each iteration of the list (like an index variable in a __for__ loop). The Main component binds the __list__ attribute to an array named __allOptions__ and the __item__ attribute to a variable named __currentOption__.
The WOHyperlink has an __action__ attribute, which is bound to a method called __pickOptions__. The __action__ attribute specifies a method that should be invoked when the user clicks the link. In this case, the __pickOptions__ method determines which link the user clicked and then returns the appropriate page.
Finally, the WOString element defines a __value__ attribute, which specifies the string you want displayed. This __value__ attribute is bound to the __currentOption__ variable, which is also bound to the __item__ attribute of the WORepetition. As you'll recall, __currentOption__ is updated with each iteration that the WORepetition makes. So, for each item in the __allOptions__ array (assigned to the WORepetition's __list__ attribute), the WORepetition updates the __currentOption__ variable to point to that item and then the WOString prints it on the page.

[!Table of Contents](Dynamic%20Elements.md) [!Next Section](DynamicElements3.md)

Copyright © 2016 Apple Inc. All rights reserved.

- [Terms of Use](http://www.apple.com/legal/internet-services/terms/site.html)
- [Privacy Policy](http://www.apple.com/privacy/)
