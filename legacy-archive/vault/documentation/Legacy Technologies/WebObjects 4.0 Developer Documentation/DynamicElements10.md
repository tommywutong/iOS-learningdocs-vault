---
title: WebObjects 4.0 Developer Documentation
apple_id: TP40006774
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.0/System/Documentation/Developer/WebObjects/DevGuide/DynamicElements10.html
archived_at: '2026-07-18T01:20:08.820858Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 4.0 Developer Documentation](webobjects.md)


__PATH__
[WebObjects 4.0 Documentation](webobjects.md) __>__
[WebObjects Developer's Guide](The%20WebObjects%20Developer%27s%20Guide.md)

[!Table of Contents](Dynamic%20Elements.md) [!Previous Section](DynamicElements9.md)

### When You Don't Have an Applet's Source Code

If you have an applet but do not have the source code for it, you must follow these steps to create an Association class for it:

- Declare a subclass of the Association class.

```
    class MyAssociation extends Association {
        ...
    }
```

- Implement the __keys__ method to return a list (Vector) of keys managed by the applet. See ["When You Have an Applet's Source Code"](DynamicElements9.md#apple-guztmoa) for an example.
- Implement the __takeValueForKey__ and __valueForKey__ methods to set and get the values of keys. Use Association's __destination__ method to obtain the destination object (that is, the applet).

```
    synchronized public Object valueForKey(String key) {
        Object dest = this.destination();
        if (key.equals("title")) {
            return ((MyApplet)dest).getLabel();
        }
    }

    synchronized public void takeValueForKey(Object value,
String key) {
        Object dest = this.destination();
        if (key.equals("title")) {
            if ((value != null) && !(value instanceof
String)) {
                System.out.println("Object value of wrong
type set for key
                'title'.  Value must be a String.");
        } else {
            ((MyApplet)dest).setLabel(((value == null)
                ? ""
                : (String)value));
        }
    }
```


Note that the class of the destination applet (in this example, MyApplet) must be cast.

If the applet triggers an action method, it must have some mechanism for communicating this event to observers (such as an __observeGadget__ method).

- The Association responds to the triggering of the applet's action by sending __invokeAction__ to itself.

```
    // fictictious method
    public void observeGadget(Object sender, String action)
{
        if ((sender instanceof Gadget) &&
action.equals("vacuum")) {
            this.invokeAction(action);
        }
    }
```


Note that in this hypothetical example, the Association must first set itself up as an observer in the applet.
[!Table of Contents](Dynamic%20Elements.md) [! Next Section](Common%20Methods.md)

Copyright © 2016 Apple Inc. All rights reserved.

- [Terms of Use](http://www.apple.com/legal/internet-services/terms/site.html)
- [Privacy Policy](http://www.apple.com/privacy/)
