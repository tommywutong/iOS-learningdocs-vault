---
title: WebObjects 4.5 Developer Documentation
apple_id: TP40006775
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.5/System/Documentation/Developer/WebObjects/DevGuide/DynamicElements9.html
archived_at: '2026-07-15T08:05:32.552628Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 4.5 Developer Documentation](webobjects.md)


__PATH__
[Documentation](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/index.html) __>__ [WebObjects 4.5](webobjects.md) __>__
WebObjects Developer's Guide

---

[!Table of Contents](Dynamic%20Elements.md) [!Previous Section](DynamicElements8.md)

## When You Have an Applet's Source Code

If you write an applet, or acquire the source code for an applet, you can follow these steps to give the applet the associative behavior it needs to be a client-side component:

- In Project Builder, add the ClientSideJava subproject to your project. To do so, double-click the word "Subprojects" in the browser and then choose __ClientSideJava.subproj__ in the Open panel.
- Add your class to the ClientSideJava subproject. Double-click Classes in the subproject and then choose your __.java__ file in the Open panel.
- In the class declaration, insert the "implements SimpleAssociationDestination" clause.

```
    public class MyApplet extends Applet implements
    SimpleAssociationDestination {
         ....
    }
```

- Implement the __keys__ method to return a list (Vector) of state keys managed by the applet.

```
    public Vector keys() {
        Vector keys = new Vector(1);
        keys.addElement("title");
        return keys;
    }
```

- Implement the __takeValueForKey__ and __valueForKey__ methods to set and get the values of keys.

```
    synchronized public Object valueForKey(String key) {
        if (key.equals("title")) {
            return this.getLabel();
        }
    }

    synchronized public void takeValueForKey(Object value,
String key) {
        if (key.equals("title")) {
            if ((value != null) && !(value instanceof String)
{
                System.out.println("Object value of wrong
type set for key
                'title'.  Value must be a String.");
            } else {
                this.setLabel(((value == null) ? "" :
(String)value));
        }
    }
```


You should be able to access the keys directly or, ideally, through accessor methods (in this example, __getLabel__ and __setLabel__). It is a good idea to use the synchronized modifier with __takeValueForKey__ and __valueForKey__ because these methods can be invoked from other threads to read or set data.

The value for a key must be a property-list type of object (either singly or in combination, such as an array of string objects). The corresponding property-list type of objects for Objective-C and Java are:

|  __Objective-C__ |  Java |
| --- | --- |
|  NSString |  String |
|  NSArray |  Vector |
|  NSDictionary |  Hashtable |
|  NSData |  byte[] |

```
```


The remaining steps apply only if the applet has an action.

- Declare an instance variable for the applet's Association object and then, in __setAssociation__, assign the passed-in object to that variable.

```
    protected Association _assoc;
    ...
    synchronized public void setAssociation(Association
assoc) {
        _assoc = assoc;
    }
```


The Association object must be stored so that it can be used later as the receiver of the __invokeAction__ message. The Association forwards the action to the AppletGroupController, which handles the invocation of the server-side action method.

- When an action is invoked in the applet, send __invokeAction__ to the applet's Association.

```
    synchronized public boolean action(Event evt, Object
what) {
        if (_assoc != null) {
            _assoc.invokeAction("action");
        }
        return true;
}
```

[!Table of Contents](Dynamic%20Elements.md) [!Next Section](DynamicElements10.md)
