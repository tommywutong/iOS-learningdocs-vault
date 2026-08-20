---
title: WebObjects 5.0 Developer Documentation
apple_id: TP40006776
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_5/EOControlRef/Java/Classes/EOGenericRecord.html
archived_at: '2026-07-15T08:13:46.912181Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 5.0 Developer Documentation](webobjects.md)


|  |
| --- |
| __PATH__[Documentation](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/index.html) __>__ [WebObjects](webobjects.md) |

[![Table of Contents](attachments/EOControlRef/Java/Art/up.gif)](../EOControlTOC.md) 

# EOGenericRecord

> **__Inherits from:__**
> : [EOCustomObject](EOCustomObject.md#apple-f4xwc4dqnrsv64tfmyxwuylwmexwg3bpivhug5ltorxw2t3cnjswg5a)

> **__Package:__**
> : com.webobjects.eocontrol

---

## Class Description

---

EOGenericRecord is a generic enterprise object class that can be used in place of custom classes when you don't need custom behavior. It implements the EOEnterpriseObject interface to provide the basic enterprise object behavior. An EOGenericRecord object has an EOClassDescription that provides metadata about the generic record, including the name of the entity that the generic record represents and the names of the record's attributes and relationships. A generic record stores its properties in a dictionary using its attribute and relationship names as keys.

In the typical case of applications that access a relational database, the access layer's modeling objects are an important part of how generic records map to database rows: If an EOModel doesn't have a custom enterprise object class defined for a particular entity, an EODatabaseChannel using that model creates EOGenericRecords when fetching objects for that entity from the database server. During this process, the EODatabaseChannel also sets each generic record's class description to an EOEntityClassDescription, providing the link to the record's associated modeling objects. (EOModel, EODatabaseChannel, and EOEntityClassDescription are defined in EOAccess.)

## Creating an Instance of EOGenericRecord

The best way to create an instance of EOGenericRecord is using the EOClassDescription method createInstanceWithEditingContext as follows:

> ```
> EOEnterpriseObject newEO;
> String entityName;       // Assume this exists.
>
> EOClassDescription description =
>     ClassDescription.classDescriptionForEntityName(entityName);
> newEO = description.createInstanceWithEditingContext(null, null);
> ```

__createInstanceWithEditingContext__ is preferable to using the constructor because the same code works if you later use a custom enterprise object class instead of EOGenericRecord. You can get an EOClassDescription for an entity name as shown above. Alternatively, you can get an EOClassDescription for a destination key of an existing enterprise object as follows:

> ```
> EOEnterpriseObject newEO;
> EOEnterpriseObject existingEO;   // Assume this exists.
> String relationshipName;       // Assume this exists.
> EOClassDescription sourceDesc = existingEO.classDescription();
> EOClassDescription desc =     sourceDesc.classDescriptionForDestinationKey(relationshipName);
>
> newEO = desc.createInstanceWithEditingContext(null, null);
> ```

The technique in this example is useful for inserting a new destination object into an existing enterprise object-for creating a new Movie object to add to a Studio's array of Movies, for example.

## Constructors

---

### EOGenericRecord

`public EOGenericRecord( EOEditingContext anEditingContext, EOClassDescription aClassDescription, EOGlobalID globalID)`

Creates a new EOGenericRecord. The new EOGenericRecord gets its metadata from _aClassDescription_. You should pass __null__ for _anEditingContext_ and _globalID_, because the arguments are optional: EOGenericRecord's implementation does nothing with them. Throws an exception if _aClassDescription_ is __null__.

You shouldn't use these constructors to create new EOGenericRecords. Rather, use EOClassDescription's createInstanceWithEditingContext method. See the class description for more information.

`public EOGenericRecord()`

Description forthcoming.

`public EOGenericRecord(EOClassDescription classDescription)`

Description forthcoming.

---

## Static Methods

---

### usesDeferredFaultCreation

`public static boolean usesDeferredFaultCreation()`

Returns `true`, specifying that EOGenericRecords use deferred faulting (which is more efficient than the regular faulting mechanism.)

---

## Instance Methods

---

### __classDescription__

`public EOClassDescription classDescription()`

Description forthcoming.

---

### storedValueForKey

`public abstract Object storedValueForKey(String key)`

Overrides the default implementation to simply invoke [valueForKey](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpi5sw4zlsnfrvezldn5zgil3wmfwhkzkgn5zewzlz).

__See Also:__ storedValueForKey (EOKeyValueCoding)

---

### takeStoredValueForKey

`public abstract void takeStoredValueForKey( Object value, String key)`

Overrides the default implementation to simply invoke [takeValueForKey](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpi5sw4zlsnfrvezldn5zgil3umfvwkvtbnr2wkrtpojfwk6i).

__See Also:__ takeStoredValueForKey (EOKeyValueCoding)

---

### takeValueForKey

`public void takeValueForKey( Object value, String key)`

Invokes the receiver's willChange method, and sets the value for the property identified by _key_ to _value_. If _value_ is null, this method removes the receiver's dictionary entry for _key_. (EOGenericRecord overrides the default implementation.) If _key_ is not one of the receiver's attribute or relationship names, EOGenericRecord's implementation does not invoke handleTakeValueForUnboundKey. Instead, EOGenericRecord's implementation does nothing.

---

### valueForKey

`public Object valueForKey(String key)`

Returns the value for the property identified by _key_. (EOGenericRecord overrides the default implementation.) If _key_ is not one of the receiver's attribute or relationship names, EOGenericRecord's implementation does not invoke handleQueryWithUnboundKey. Instead, EOGenericRecord's implementation simply returns null. This method calls willRead.

---

© 2001 Apple Computer, Inc. (Last Published April 19, 2001)

[![Table of Contents](attachments/EOControlRef/Java/Art/up.gif)](../EOControlTOC.md)

Copyright © 2016 Apple Inc. All rights reserved.

- [Terms of Use](http://www.apple.com/legal/internet-services/terms/site.html)
- [Privacy Policy](http://www.apple.com/privacy/)
