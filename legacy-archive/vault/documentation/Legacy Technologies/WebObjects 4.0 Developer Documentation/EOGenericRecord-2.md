---
title: WebObjects 4.0 Developer Documentation
apple_id: TP40006774
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.0/System/Library/Frameworks/EOControl.framework/Resources/English.lproj/Documentation/Reference/ObjC_classic/Classes/EOGenericRecord.html
archived_at: '2026-07-18T01:28:36.223659Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 4.0 Developer Documentation](webobjects.md)


__PATH__
[WebObjects 4.0 Documentation](webobjects.md) __>__
[EOControl Reference](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.0/System/Library/Frameworks/EOControl.framework/Resources/English.lproj/Documentation/Reference/ObjC_classic/frameset.html)

[!](EOFetchSpecification-2.md)
[!](EOGlobalID-2.md)

---

# EOGenericRecord

__Inherits From:__
NSObject

__Conforms To:__ NSObject (NSObject)

__Declared in:__ EOControl/EOGenericRecord.h

EOGenericRecord is a generic enterprise object class that can be used in place of custom classes when you don't need custom behavior. It implements the EOEnterpriseObject interface to provide the basic enterprise object behavior. An EOGenericRecord object has an EOClassDescription that provides metadata about the generic record, including the name of the entity that the generic record represents and the names of the record's attributes and relationships. A generic record stores its properties in a dictionary using its attribute and relationship names as keys.

In the typical case of applications that access a relational database, the access layer's modeling objects are an important part of how generic records map to database rows: If an EOModel doesn't have a custom enterprise object class defined for a particular entity, an EODatabaseChannel using that model creates EOGenericRecords when fetching objects for that entity from the database server. During this process, the EODatabaseChannel also sets each generic record's class description to an EOEntityClassDescription, providing the link to the record's associated modeling objects. (EOModel, EODatabaseChannel, and EOEntityClassDescription are defined in EOAccess.)

---

### Creating an Instance of EOGenericRecord

The best way to create an instance of EOGenericRecord is using the EOClassDescription method [__createInstanceWithEditingContext:globalID:zone:__](EOClassDescription-3.md)as follows:

> ```
> id newEO;
> NSString *entityName;             // Assume this exists.
>
> newEO = [[EOClassDescription classDescriptionForEntityName:entityName]
>     createInstanceWithEditingContext:nil
>     globalID:nil
>      zone:nil];
> ```

[__createInstanceWithEditingContext:globalID:zone:__](EOClassDescription-3.md)is preferable to EOGenericRecord's __init...__ method because the same code works if you later use a custom enterprise object class instead of EOGenericRecord. You can get an EOClassDescription for an entity name as shown above. Alternatively, you can get an EOClassDescription for a destination key of an existing enterprise object as follows:

> ```
> id newEO;
> id existingEO;              // Assume this exists.
> NSString *relationshipName; // Assume this exists.
> EOClassDescription *description = [existingEO classDescription];
>
> newEO = [[description classDescriptionForDestinationKey:relationshipName]
>     createInstanceWithEditingContext:editingContext
>     lobalID:nil
>     zone:nil];
> ```

The technique in this example is useful for inserting a new destination object into an existing enterprise object-for creating a new Movie object to add to a Studio's array of Movies, for example.

---

#### initWithEditingContext:classDescription:globalID:

- (id)__initWithEditingContext:__ (EOEditingContext \*)_anEditingContext___classDescription:__ (EOClassDescription \*)_aClassDescription___globalID:__ (EOGlobalID \*)_globalID_

The designated initializer, this method initializes a newly allocated EOGenericRecord to get its metadata from _aClassDescription_. You should pass __nil__ for _anEditingContext_ and _globalID_, because the arguments are optional: EOGenericRecord's implementation does nothing with them. Raises an NSInternalInconsistencyException if _aClassDescription_ is __nil__ . Returns __self__ .

You shouldn't use this method to create new EOGenericRecords. Rather, use EOClassDescription's [__createInstanceWithEditingContext:globalID:zone:__](EOClassDescription-3.md)method. See the class description for more information.

---

#### storedValueForKey:

- (id)__storedValueForKey:__ (NSString \*)_key_

Overrides the default implementation to simply invoke __valueForKey:__ .

__See also:__ [__storedValueForKey:__](EOKeyValueCoding-3.md)([EOKeyValueCoding](EOKeyValueCoding-3.md))

---

#### takeStoredValue:forKey:

- (void)`takeStoredValue:`(id)_value_`forKey:`(NSString \*)_key_

Overrides the default implementation to simply invoke __takeValue:forKey:__ .

__See also:__ [__takeStoredValue:forKey:__](EOKeyValueCoding-3.md)([EOKeyValueCoding](EOKeyValueCoding-3.md))

---

#### takeValue:forKey:

- (void)__takeValue:__ (id)_value___forKey:__ (NSString \*)_key_

Invokes the receiver's [__willChange__](EOEnterpriseObject-3.md)method, and sets the value for the property identified by _key_ to _value_. If _value_ is __nil__ , this method removes the receiver's dictionary entry for _key_. (EOGenericRecord overrides the default implementation.) If _key_ is not one of the receiver's attribute or relationship names, EOGenericRecord's implementation does not invoke [__handleTakeValue:forUnboundKey:__](EOKeyValueCoding-3.md). Instead, EOGenericRecord's implementation does nothing.

---

#### valueForKey:

- (id)__valueForKey:__ (NSString \*)_key_

Returns the value for the property identified by _key_. (EOGenericRecord overrides the default implementation.) If _key_ is not one of the receiver's attribute or relationship names, EOGenericRecord's implementation does not invoke [__handleQueryWithUnboundKey:__](EOKeyValueCoding-3.md). Instead, EOGenericRecord's implementation simply returns __nil__ .

---

[!](EOFetchSpecification-2.md)
[!](EOGlobalID-2.md)

---

_Copyright © 1998, Apple Computer, Inc. All rights reserved._
