---
title: WebObjects 4.0 Developer Documentation
apple_id: TP40006774
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.0/System/Documentation/Developer/WebObjects/Reference/ClientSideComponents/SupportClasses/next.wo.client.SimpleAssoc.html
archived_at: '2026-07-18T01:23:31.681033Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 4.0 Developer Documentation](webobjects.md)



Interface next.wo.client.SimpleAssociationDestination

```
All Packages  Class Hierarchy  This Package  Previous  Next
```

---

# Interface next.wo.client.SimpleAssociationDestination

**public interface __SimpleAssociationDestination__

**extends [Object](http://www.javasoft.com/products/JDK/1.0.2/api/java.lang.Object.html)

**extends [KeyValueCoding](Interface%20next.util.KeyValueCoding.md)******

The SimpleAssociationDestination interface allows applets that implement it to be the destinations of SimpleAssociations. By implementing these methods, plus the KeyValueCoding methods, the applet takes on the responsibilities of the Association object. The SimpleAssociation class simply passes calls to __valueForKey(__String__)__, __takeValueForKey(__Object, String__)__, and __keys()__ along to its destination. Associations are required for the exchange of state and action information with the AppletGroupController, which handles communication with the server.

**__See Also:__**
: [Association](Class%20next.wo.client.Association.md), [KeyValueCoding](Interface%20next.util.KeyValueCoding.md)

---

## Method Index

**![ o ](attachments/System/Documentation/Developer/WebObjects/Reference/ClientSideComponents/SupportClasses/images/red-ball-small.gif)
[__keys__](#apple-nnsxs4zife)()**
: Applets must implement this method to return the list (as a Vector object) of the keys for the state that they manage.

**![ o ](attachments/System/Documentation/Developer/WebObjects/Reference/ClientSideComponents/SupportClasses/images/red-ball-small.gif)
[__setAssociation__](#apple-onsxiqltonxwg2lboruw63q)(Association)**
: Implemented by applets so that they can store the Association object _assoc_ (an instance of SimpleAssociation) so that later, when an action is triggered in the applet, they can send __invokeAction(__String__)__ to that object.

## Methods

![ o ](attachments/System/Documentation/Developer/WebObjects/Reference/ClientSideComponents/SupportClasses/images/red-ball.gif)
__keys__

```
  public abstract Vector keys()
```

: Applets must implement this method to return the list (as a Vector object) of the keys for the state that they manage.

![ o ](attachments/System/Documentation/Developer/WebObjects/Reference/ClientSideComponents/SupportClasses/images/red-ball.gif)
__setAssociation__

```
  public abstract void setAssociation(Association assoc)
```

: Implemented by applets so that they can store the Association object _assoc_ (an instance of SimpleAssociation) so that later, when an action is triggered in the applet, they can send __invokeAction(__String__)__ to that object. This results in the invocation of the associated action method in the server.
Note that even applets that do not have actions must implement this method, even if as a "null" method.

**__See Also:__**
: [invokeAction](Class%20next.wo.client.Association.md#apple-nfxhm33lmvawg5djn5xa)

---

```
All Packages  Class Hierarchy  This Package  Previous  Next
```
