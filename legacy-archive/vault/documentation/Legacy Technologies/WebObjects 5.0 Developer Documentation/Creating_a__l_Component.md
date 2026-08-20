---
title: WebObjects 5.0 Developer Documentation
apple_id: TP40006776
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_5/DirectToWeb/Customizing/Creating_a__l_Component.html
archived_at: '2026-07-15T08:12:23.599420Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 5.0 Developer Documentation](webobjects.md)


|  |
| --- |
| __PATH__[Documentation](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/index.html) __>__ [WebObjects](webobjects.md) |

[![Previous](attachments/DirectToWeb/Images/previous.gif)](Modifying_t_Web_Factory.md)[!](Modifying_a_eb_Template.md)

## Creating a Custom Property-Level Component

Sometimes you need a custom property-level component that
implements specialized behavior or that works with a type of attribute that
Direct to Web doesn't already support (such as a QuickTime movie). Direct to Web
provides a property-level component called D2WCustomComponent to make it easier
to create such a component. To use the D2WCustomComponent, you first create a
custom component. Then you use the Web Assistant to tell Direct to Web to use
it.

### Specifying the Custom Component

The
custom property-level component must be a reusable component that defines two
keys: `object` and `key`. The value for `object`
specifies the enterprise object that the reusable component manipulates, for
example, a Movie object. The value for `key` specifies the key of the
property that the component manipulates, for example,
`dateReleased`.

You can get the
property by defining two instance variables in your component:

```
EOEnterpriseObject object; String key;
```

and using
the EOKeyValueCoding method `valueForKey`:

```
NSTimestamp
date = object.valueForKey(key);
```

To store a value for
the property, you use `takeValueForKey`:

```
object.takeValueForKey(date,key);
```

If you are
using a nonsynchronizing component (see "Reusable Components" in the
_WebObjects Developer's Guide_), you need to get the values for the
`object` and `key` bindings using the
`valueForBinding` method before you get or store the
property.

```
EOEnterpriseObject object = valueForBinding("object");
String key = valueForBinding("key");
```

["EditDatePopup
Listings"](../Appendix/EditDatePopup_Listings.md#apple-krifqusfiyytami) shows an example custom component called EditDatePopup that uses
pop-up lists to edit dates. The example lists the `.html`,
`.wod`, and `.java` files that specify the custom
component.

### Using the Custom Component With Direct to Web

Once the custom component has been
compiled, you can use the Web Assistant to instruct your Direct to Web
application to use it. Follow these steps to configure your application to use
the pop-up list date editing component for the `dateReleased`
attribute on the Movie edit page:

1. Open the Web Assistant.
   See ["Customizing Your
   Application With the WebAssistant"](../WalkThrough/Customizing_ebAssistant.md#apple-ijbusschjjbeu).
2. Click the "Expert mode"
   button.

   In Expert mode, you can make changes that affect all pages for a given
   task.
3. Select the Properties tab.
4. Select the
   `edit` task and the Movie entity.
5. Click
   `dateReleased` in the Show browser.
6. In the right
   column, choose D2WCustomComponent from the pop-up list.
7. Enter the
   name `EditDatePopup` in the Component text box.

You can also use the Web Assistant to configure your application to
use the EditDatePopup component on every edit page by following these
steps:

1. Select the `edit` task and "\*all\*" for
   the entity.
2. Click NSTimestamp in the type browser in the second
   column.
3. In the right column, choose D2WCustomComponent from the
   pop-up list.
4. Enter the name `EditDatePopup` in the
   Component text box.

You can also configure
your application to use the custom component by setting rules with the rule
editor. To do so, use the rules shown in [Listing 4-5](#apple-ijauerkjivdus).
(To launch the RuleEditor application Control-double-click
`user.d2wmodel` in the Resourses group in the Groups & Files list of
Project Builder's main window.)

__Listing
4-5__

```
((task = "edit") and (not (attribute = nil)) and
(attribute.valueClassName = "NSTimestamp")) => componentName =
"D2WCustomComponent"

((task = "edit") and (not (attribute = nil)) and ((attribute.valueClassName =
"NSTimestamp")) => customComponentName = "EditDatePopup"
```

You also need to set the assignment class (Assignment) and the
priority (100) for each rule. For more information about using the rule editor,
see ["Adding
Rules to Define the Default Behavior"](Adding_a_Ne_Application.md#apple-ijbusq2eivceq).

[![Previous](attachments/DirectToWeb/Images/previous.gif)](Modifying_t_Web_Factory.md)[!](Modifying_a_eb_Template.md)

© 2001 Apple Computer, Inc.

Shop the [Apple Online Store](http://www.apple.com/store/) (1-800-MY-APPLE), visit an [Apple Retail Store](http://www.apple.com/retail/), or find a [reseller](http://www.apple.com/buy/locator/).

- [Mailing Lists](http://lists.apple.com/)
- [RSS Feeds](https://developer.apple.com/rss/)

Copyright © 2016 Apple Inc. All rights reserved.

- [Terms of Use](http://www.apple.com/legal/internet-services/terms/site.html)
- [Privacy Policy](http://www.apple.com/privacy/)
