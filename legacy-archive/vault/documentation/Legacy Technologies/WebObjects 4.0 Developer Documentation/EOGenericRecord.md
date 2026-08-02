---
title: WebObjects 4.0 Developer Documentation
apple_id: TP40006774
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.0/System/Library/Frameworks/EOControl.framework/Resources/English.lproj/Documentation/Reference/Java/Classes/EOGenericRecord.html
archived_at: '2026-07-18T01:28:26.205626Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 4.0 Developer Documentation](webobjects.md)


__PATH__
[WebObjects 4.0 Documentation](webobjects.md) __>__
[EOControl Reference](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.0/System/Library/Frameworks/EOControl.framework/Resources/English.lproj/Documentation/Reference/Java/frameset.html)

[!](EOFetchSpecification.md)
[!](EOGlobalID.md)

---

# EOGenericRecord

__Inherits From:__
EOCustomObject : Object(Java Client)
NSObject (Yellow Box)

__Implements:__
EOEnterpriseObject
EOKeyValueCoding (EOEnterpriseObject)
EOKeyValueCodingAdditions (EOEnterpriseObject)
EORelationshipManipulation (EOEnterpriseObject)
EOValidation (EOEnterpriseObject)
EOFaulting (EOEnterpriseObject)

__Package:__
com.apple.client.eocontrol (Java Client)
com.apple.yellow.eocontrol (Yellow Box)

## Class Description

EOGenericRecord is a generic enterprise object class that can be used in place of custom classes when you don't need custom behavior. It implements the EOEnterpriseObject interface to provide the basic enterprise object behavior. An EOGenericRecord object has an EOClassDescription that provides metadata about the generic record, including the name of the entity that the generic record represents and the names of the record's attributes and relationships. A generic record stores its properties in a dictionary using its attribute and relationship names as keys.

In the typical case of applications that access a relational database, the access layer's modeling objects are an important part of how generic records map to database rows: If an EOModel doesn't have a custom enterprise object class defined for a particular entity, an EODatabaseChannel using that model creates EOGenericRecords when fetching objects for that entity from the database server. During this process, the EODatabaseChannel also sets each generic record's class description to an EOEntityClassDescription, providing the link to the record's associated modeling objects. (EOModel, EODatabaseChannel, and EOEntityClassDescription are defined in EOAccess.)

---

### Creating an Instance of EOGenericRecord

The best way to create an instance of EOGenericRecord is using the EOClassDescription method [__createInstanceWithEditingContext__](EOClassDescription.md)as follows:

> ```
> EOEnterpriseObject newEO;
> String entityName;       // Assume this exists.
>
> ClassDescription description =
>     ClassDescription.classDescriptionForEntityName(entityName);
> newEO = description.createInstanceWithEditingContext(null, null);
> ```

[__createInstanceWithEditingContext__](EOClassDescription.md)is preferable to using the constructor because the same code works if you later use a custom enterprise object class instead of EOGenericRecord. You can get an EOClassDescription for an entity name as shown above. Alternatively, you can get an EOClassDescription for a destination key of an existing enterprise object as follows:

> ```
> EOEnterpriseObject newEO;
> EOEnterpriseObject existingEO;   // Assume this exists.
> String relationshipName;       // Assume this exists.
> ClassDescription sourceDesc = existingEO.classDescription();
> ClassDescription desc = sourceDesc.classDescriptionForDestinationKey(relationshipName);
>
> newEO = desc.createInstanceWithEditingContext(null, null);
> ```

The technique in this example is useful for inserting a new destination object into an existing enterprise object-for creating a new Movie object to add to a Studio's array of Movies, for example.

## Constructors

---

#### EOGenericRecord

public __EOGenericRecord__ (EOEditingContext _anEditingContext_, EOClassDescription _aClassDescription_, EOGlobalID _globalID_)

Creates a new EOGenericRecord. The new EOGenericRecord gets its metadata from _aClassDescription_. You should pass __null__ for _anEditingContext_ and _globalID_, because the arguments are optional: EOGenericRecord's implementation does nothing with them. Throws an exception if _aClassDescription_ is __null__ .

You shouldn't use these constructors to create new EOGenericRecords. Rather, use EOClassDescription's [__createInstanceWithEditingContext__](EOClassDescription.md)method. See the class description for more information.

## Instance Methods

---

#### storedValueForKey

public abstract java.lang.Object __storedValueForKey__ (java.lang.String _key_)

Overrides the default implementation to simply invoke __valueForKey__ .

__See also:__ [__storedValueForKey__](EOKeyValueCoding.md)([EOKeyValueCoding](EOKeyValueCoding.md))

---

#### takeStoredValueForKey

public abstract void __takeStoredValueForKey__ (
java.lang.Object _value_,
java.lang.String _key_)

Overrides the default implementation to simply invoke __takeValueForKey__ .

__See also:__ [__takeStoredValueForKey__](EOKeyValueCoding.md)([EOKeyValueCoding](EOKeyValueCoding.md))

---

#### takeValueForKey

public void __takeValueForKey__ (
java.lang.Object _value_,
java.lang.String _key_)

Invokes the receiver's [__willChange__](EOEnterpriseObject.md)method, and sets the value for the property identified by _key_ to _value_. If _value_ is __null__ , this method removes the receiver's dictionary entry for _key_. (EOGenericRecord overrides the default implementation.) If _key_ is not one of the receiver's attribute or relationship names, EOGenericRecord's implementation does not invoke [__handleTakeValueForUnboundKey__](EOKeyValueCoding.md). Instead, EOGenericRecord's implementation does nothing.

---

#### valueForKey

public java.lang.Object __valueForKey__ (java.lang.String _key_)

Returns the value for the property identified by _key_. (EOGenericRecord overrides the default implementation.) If _key_ is not one of the receiver's attribute or relationship names, EOGenericRecord's implementation does not invoke [__handleQueryWithUnboundKey__](EOKeyValueCoding.md). Instead, EOGenericRecord's implementation simply returns __null__ . This method calls [__willRead__](EOFaulting.md).

---

[!](EOFetchSpecification.md)
[!](EOGlobalID.md)

---

_Copyright © 1998, Apple Computer, Inc. All rights reserved._
