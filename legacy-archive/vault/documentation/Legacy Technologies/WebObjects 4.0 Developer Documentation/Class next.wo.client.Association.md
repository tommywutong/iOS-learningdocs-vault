---
title: WebObjects 4.0 Developer Documentation
apple_id: TP40006774
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.0/System/Documentation/Developer/WebObjects/Reference/ClientSideComponents/SupportClasses/next.wo.client.Association.html
archived_at: '2026-07-18T01:23:31.587773Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 4.0 Developer Documentation](webobjects.md)



Class next.wo.client.Association

```
All Packages  Class Hierarchy  This Package  Previous  Next
```

---

# Class next.wo.client.Association

```
java.lang.Object

   |

   +----next.wo.client.Association
```

---

**public class __Association__

**extends [Object](http://www.javasoft.com/products/JDK/1.0.2/api/java.lang.Object.html)

**implements [KeyValueCoding](Interface%20next.util.KeyValueCoding.md)******

The Association class is an abstract class that defines the required behavior for objects that know how to get and set the values of applet keys (for state) and communicate that data to the AppletGroupController. These objects are also responsible for detecting actions triggered by their destination applets and sending __invokeAction(__String__)__ to have the appropriate action method invoked in the server. Subclasses of Association must implement the KeyValueCoding interface methods __takeValueForKey(__Object, String__)__ and __valueForKey__(String__)__ as well as the __keys()__ method.
If you have access to the source code of an applet, consider implementing the SimpleAssociationDestination interface in the applet instead of creating a subclass of Association.

**__See Also:__**
: [KeyValueCoding](Interface%20next.util.KeyValueCoding.md), [SimpleAssociationDestination](Interface%20next.wo.client.SimpleAssociationDestination.md)

---

![Method Index](attachments/System/Documentation/Developer/WebObjects/Reference/ClientSideComponents/SupportClasses/images/method-index.gif)

**![ o ](attachments/System/Documentation/Developer/WebObjects/Reference/ClientSideComponents/SupportClasses/images/red-ball-small.gif)
[__destination__](#apple-mrsxg5djnzqxi2lpnyucs)()**
: Returns the destination (the applet) of the Association object.

**![ o ](attachments/System/Documentation/Developer/WebObjects/Reference/ClientSideComponents/SupportClasses/images/red-ball-small.gif)
[__takeValueForKey__](#apple-orqwwzkwmfwhkzkgn5zewzlz)(Object, String)**
: Because Association explicitly implements the KeyValueCoding interface but is an abstract class, it declares this method as abstract.

**![ o ](attachments/System/Documentation/Developer/WebObjects/Reference/ClientSideComponents/SupportClasses/images/red-ball-small.gif)
[__valueForKey__](#apple-ozqwy5lfizxxes3fpeuguylwmexgyylom4xfg5dsnfxgoki)(String)**
: Because Association explicitly implements the KeyValueCoding interface but is an abstract class, it declares this method as abstract.

## Methods

![ o ](attachments/System/Documentation/Developer/WebObjects/Reference/ClientSideComponents/SupportClasses/images/red-ball.gif)
__valueForKey__

```
  public abstract Object valueForKey(String key)
```

: Because Association explicitly implements the KeyValueCoding interface but is an abstract class, it declares this method as abstract. Subclasses of Association must implement this KeyValueCoding method.

**__See Also:__**
: [KeyValueCoding](Interface%20next.util.KeyValueCoding.md)

![ o ](attachments/System/Documentation/Developer/WebObjects/Reference/ClientSideComponents/SupportClasses/images/red-ball.gif)
__takeValueForKey__

```
  public abstract void takeValueForKey(Object value,

                                       String key)
```

: Because Association explicitly implements the KeyValueCoding interface but is an abstract class, it declares this method as abstract. Subclasses of Association must implement this KeyValueCoding method.

**__See Also:__**
: [KeyValueCoding](Interface%20next.util.KeyValueCoding.md)

![ o ](attachments/System/Documentation/Developer/WebObjects/Reference/ClientSideComponents/SupportClasses/images/red-ball.gif)
__keys__

```
  public abstract Vector keys()
```

: Subclasses must implement this method to return the list (as a Vector object) of the keys for the state managed by the associated applet.

![ o ](attachments/System/Documentation/Developer/WebObjects/Reference/ClientSideComponents/SupportClasses/images/red-ball.gif)
__destination__

```
  public Object destination()
```

: Returns the destination (the applet) of the Association object.

![ o ](attachments/System/Documentation/Developer/WebObjects/Reference/ClientSideComponents/SupportClasses/images/red-ball.gif)
__invokeAction__

```
  public void invokeAction(String action)
```

: When the Association determines that an action has been triggered in the destination applet, it should send this message to itself to have the bound action method in the server-side component invoked. The argument _action_ should be the name of the action managed by the applet. for example:

```
    this.invokeAction("selectionChanged");
```

---

```
All Packages  Class Hierarchy  This Package  Previous  Next
```
