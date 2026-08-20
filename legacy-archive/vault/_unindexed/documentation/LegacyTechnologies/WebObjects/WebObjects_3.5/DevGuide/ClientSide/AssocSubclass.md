---
title: WebObjects 3.5 Developer Documentation
apple_id: TP40006773
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-11-29'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/DevGuide/ClientSide/AssocSubclass.html
archived_at: '2026-07-15T07:51:08.598811Z'
---
> 导航：[总目录](../../../../../../../README.md) · 未编入索引的页面


[!Table of Contents](ClientSideTOC.md) [!Previous Section](ImplementingSAD.md)

# When You Don't Have an Applet's Source Code

If you have an applet but do not have the source code for it, you must follow these steps to create an Association class for it:

- Declare a subclass of the Association class.

```
    class MyAssociation extends Association {
        ...
    }
```

- Implement the keys method to return a list (Vector) of keys managed by the applet. See ["When You Have an Applet's Source Code"](ImplementingSAD.md#apple-gizdooa) for an example.
- Implement the takeValueForKey and valueForKey methods to set and get the values of keys. Use Association's destination method to obtain the destination object (that is, the applet).

```
    synchronized public Object valueForKey(String key) {
        Object dest = this.destination();
        if (key.equals("title")) {
            return ((MyApplet)dest).getLabel();
        }
    }

    synchronized public void takeValueForKey(Object value, String key) {
        Object dest = this.destination();
        if (key.equals("title")) {
            if ((value != null) && !(value instanceof String)) {
                System.out.println("Object value of wrong type set for key
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

- The Association responds to the triggering of the applet's action by sending invokeAction to itself.

```
    // fictictious method
    public void observeGadget(Object sender, String action) {
        if ((sender instanceof Gadget) && action.equals("vacuum")) {
            this.invokeAction(action);
        }
    }
```


Note that in this hypothetical example, the Association must first set itself up as an observer.

Copyright © 2016 Apple Inc. All rights reserved.

- [Terms of Use](http://www.apple.com/legal/internet-services/terms/site.html)
- [Privacy Policy](http://www.apple.com/privacy/)
