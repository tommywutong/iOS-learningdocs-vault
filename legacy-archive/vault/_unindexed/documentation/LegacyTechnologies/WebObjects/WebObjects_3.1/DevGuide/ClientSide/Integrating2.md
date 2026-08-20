---
title: WebObjects 3.1 Developer Documentation
apple_id: TP40006772
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-11-29'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.1/DevGuide/ClientSide/Integrating2.html
archived_at: '2026-07-15T07:46:37.169580Z'
---
> 导航：[总目录](../../../../../../../README.md) · 未编入索引的页面


[!Table of Contents](ClientSideComponents.mif.md)
[!Previous Section](Integrating1.md)

## __2. Make the appropriate WOApplet bindings__

In the component's ".wod" file, associate each identifier with a WOApplet dynamic element and initialize the standard WOApplet attributes as well as those specific to the applet class.

```
INPUTFIELD : WOApplet {
    code = "next.wo.client.controls.TextFieldApplet.class";
    codebase = "/WebObjects/Java";
    width = "200";
    height = "20";
    associationClass = "next.wo.client.SimpleAssociation";
    stringValue = inputString
};

FUNCTION : WOApplet {
    code = "next.wo.client.controls.ChoiceApplet.class";
    codebase = "/WebObjects/Java";
    width = "100";
    height = "20";
    associationClass = "next.wo.client.SimpleAssociation";
    itemList = functionItemList;
    selectedItem = functionSelectedItem;
    backgroundColor = "white";
};

BUTTON : WOApplet {
    code = "next.wo.client.controls.ButtonApplet.class";
    codebase = "/WebObjects/Java";
    width = "200";
    height = "20";
    associationClass = "next.wo.client.SimpleAssociation";
    title = "DoIt";
    action = "capitalizeString"
};

OUTPUTFIELD : WOApplet {
    code = "next.wo.client.controls.TextFieldApplet.class";
    codebase = "/WebObjects/Java";
    width = "200";
    height = "20";
    associationClass = "next.wo.client.SimpleAssociation";
    stringValue = outputString;
    enabled = "NO";
};
```

The following WOApplet attributes are standard and require assigned values. Although you could bind these attributes to variables, they are assigned constants in most cases. Constant values should be quoted.

**__code__**
: The class (including complete package prefix) of the applet.

**__codebase__**
: The _`DOCUMENT_ROOT`_ subdirectory containing the package specified in the __code__ attribute.

**__width__**
: The width of the applet, in pixels.

**__height__**
: The height of the applet, in pixels.

**__associationClass__**
: The subclass of Association for objects that get and set the state of applets and cause methods to be invoked in the server when actions are triggered in the applet. For the applet controls provided by NeXT, the Association subclass is SimpleAssociation. As the example shows, you must specify the package as well as the class. This attribute is optional. If you do not specify an Association subclass, however, then the applet is largely ornamental (as in WebObjects 2.0), since it is only able to accept initial values.

The reference section "[Client-Side Applet Controls](../../Reference/ClientSideComponents/Applets/CSControls.mif.book.md)" describes the attributes representing the keys and actions of particular applets provided by NeXT.

[!Table of Contents](ClientSideComponents.mif.md)
[!Next Section](Integrating3.md)
