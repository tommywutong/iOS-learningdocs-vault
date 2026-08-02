---
title: WebObjects 4.0 Developer Documentation
apple_id: TP40006774
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.0/System/Documentation/Developer/WebObjects/Reference/ClientSideComponents/SupportClasses/next.util.KeyValueCoding.html
archived_at: '2026-07-18T01:23:24.203877Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 4.0 Developer Documentation](webobjects.md)



Interface next.util.KeyValueCoding

```
All Packages  Class Hierarchy  This Package  Previous  Next
```

---

# Interface next.util.KeyValueCoding

**public interface __KeyValueCoding__

**extends [Object](http://www.javasoft.com/products/JDK/1.0.2/api/java.lang.Object.html)****

Classes implement the KeyValueCoding interface to return and set the values of obect attributes as identified by a string _key_. In contrast to the Java "put" convention, this interface uses the more Objective-C-like __takeValueForKey(__Object, String__)__.
The value set by the __takeValueForKey(__Object, String__)__ method must be a property-list type of object. In Java, this must be a String, Vector, Hashtable, or byte[] object; the corresponding Objective-C object types are NSString, NSArray, NSDictionary, and NSData.
In the client-side components feature, Association objects must implement the methods of this interface to set and return the values of their associated applets. Applets can assume the responsibility of an Association object by implementing the SimpleAssociationDestination interface, which includes the methods of the KeyValueCoding interface. Key-value coding in client-side components must always deal with state keys, never with actions.

**__See Also:__**
: [SimpleAssociationDestination](Interface%20next.wo.client.SimpleAssociationDestination.md), [Association](Class%20next.wo.client.Association.md)

---

## Method Index

**![ o ](attachments/System/Documentation/Developer/WebObjects/Reference/ClientSideComponents/SupportClasses/images/red-ball-small.gif)
[__takeValueForKey__](#apple-orqwwzkwmfwhkzkgn5zewzlzfbvgc5tbfzwgc3thfzhwe2tfmn2cyidkmf3gcltmmfxgolstorzgs3thfe)(Object, String)**
: Sets the value of the applet state or binding identified by _key_ to _value_.

**![ o ](attachments/System/Documentation/Developer/WebObjects/Reference/ClientSideComponents/SupportClasses/images/red-ball-small.gif)
[__valueForKey__](#apple-ozqwy5lfizxxes3fpeuguylwmexgyylom4xfg5dsnfxgoki)(String)**
: Returns the value (as a property-list object) for the applet state or action identified by _key_.

## Methods

![ o ](attachments/System/Documentation/Developer/WebObjects/Reference/ClientSideComponents/SupportClasses/images/red-ball.gif)
__valueForKey__

```
  public abstract Object valueForKey(String key)
```

: Returns the value (as a property-list object) for the applet state or action identified by _key_.

![ o ](attachments/System/Documentation/Developer/WebObjects/Reference/ClientSideComponents/SupportClasses/images/red-ball.gif)
__takeValueForKey__

```
  public abstract void takeValueForKey(Object value,

                                       String key)
```

: Sets the value of the applet state or binding identified by _key_ to _value_. The _value_ must be a property-list type of object: String, Vector, Hashtable, or byte[]. Note that you can have nested property-lists, like a Vector containing Hashtables.

---

```
All Packages  Class Hierarchy  This Package  Previous  Next
```
