---
title: WebObjects 4.5 Developer Documentation
apple_id: TP40006775
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.5/System/Library/Frameworks/EOControl.framework/Java/Classes/EOGenericRecord.html
archived_at: '2026-07-15T08:11:37.631037Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 4.5 Developer Documentation](webobjects.md)


__PATH__
[Documentation](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/index.html) __>__ [WebObjects 4.5](webobjects.md) __>__
EOControl Reference

[![Table of Contents](attachments/images/up.gif)](../EOControlTOC.md)

# EOGenericRecord

> **__Inherits
> from:__**
> : [(com.apple.client.eocontrol) EOCustomObject](EOCustomObject.md#apple-f4xwc4dqnrsv64tfmyxwuylwmexwg3bpivhug5ltorxw2t3cnjswg5a) : Object
> (com.apple.yellow.eocontrol) NSObject

> **__Implements:__**
> : EOEnterpriseObject
> : EODeferredFaulting (EOEnterpriseObject)
> : EOKeyValueCodingAdditions (EOEnterpriseObject)
> : EOKeyValueCoding.KeyBindingCreation (EOEnterpriseObject)
> : EORelationshipManipulation (EOEnterpriseObject)
> : EOValidation (EOEnterpriseObject)
> : EOFaulting (EODeferredFaulting)
> : EOKeyValueCoding (EOKeyValueCodingAdditions)
> : (com.apple.client.eocontrol only) NSKeyValueCoding (EOKeyValueCoding)
> : (com.apple.client.eocontrol only) NSInlineObservable

> **__Package:__**
> : com.apple.client.eocontrol
> : com.apple.yellow.eocontrol

---

## Class Description

---

EOGenericRecord is a generic enterprise object class that
can be used in place of custom classes when you don't need custom
behavior. It implements the [EOEnterpriseObject](EOEnterpriseObject.md#apple-ijaueqsdjbfeq) interface
to provide the basic enterprise object behavior. An EOGenericRecord
object has an EOClassDescription that provides metadata about the
generic record, including the name of the entity that the generic
record represents and the names of the record's attributes and
relationships. A generic record stores its properties in a dictionary
using its attribute and relationship names as keys.

In the typical case of applications that access a relational
database, the access layer's modeling objects are an important
part of how generic records map to database rows: If an EOModel
doesn't have a custom enterprise object class defined for a particular
entity, an EODatabaseChannel using that model creates EOGenericRecords
when fetching objects for that entity from the database server.
During this process, the EODatabaseChannel also sets each generic
record's class description to an EOEntityClassDescription, providing
the link to the record's associated modeling objects. (EOModel, EODatabaseChannel,
and EOEntityClassDescription are defined in EOAccess.)

## Creating an Instance of EOGenericRecord

The best way to create an instance of EOGenericRecord is using
the EOClassDescription method [createInstanceWithEditingContext](EOClassDescription.md#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpinwgc43tirsxgy3snfyhi2lpnyxwg4tfmf2gksloon2gc3tdmvlws5diivsgs5djnztug33oorsxq5a) as
follows:

> ```
> EOEnterpriseObject newEO;
> String entityName;       // Assume this exists.
>
> EOClassDescription description =
>     ClassDescription.classDescriptionForEntityName(entityName);
> newEO = description.createInstanceWithEditingContext(null, null);
> ```

`createInstanceWithEditingContext` is
preferable to using the constructor because the same code works if
you later use a custom enterprise object class instead of EOGenericRecord.
You can get an EOClassDescription for an entity name as shown above.
Alternatively, you can get an EOClassDescription for a destination
key of an existing enterprise object as follows:

> ```
> EOEnterpriseObject newEO;
> EOEnterpriseObject existingEO;   // Assume this exists.
> String relationshipName;       // Assume this exists.
> EOClassDescription sourceDesc = existingEO.classDescription();
> EOClassDescription desc =     sourceDesc.classDescriptionForDestinationKey(relationshipName);
>
> newEO = desc.createInstanceWithEditingContext(null, null);
> ```

The technique in this example is useful for inserting a new
destination object into an existing enterprise object-for creating
a new Movie object to add to a Studio's array of Movies, for example.

## Constructors

---

### EOGenericRecord

`public EOGenericRecord(
EOEditingContext anEditingContext,
EOClassDescription aClassDescription,
EOGlobalID globalID)`

Creates a new EOGenericRecord. The new EOGenericRecord
gets its metadata from _aClassDescription._
You should pass `null` for _anEditingContext_ and _globalID,_
because the arguments are optional: EOGenericRecord's implementation
does nothing with them. Throws an exception if _aClassDescription_ is `null`.

You
shouldn't use these constructors to create new EOGenericRecords.
Rather, use EOClassDescription's [createInstanceWithEditingContext](EOClassDescription.md#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpinwgc43tirsxgy3snfyhi2lpnyxwg4tfmf2gksloon2gc3tdmvlws5diivsgs5djnztug33oorsxq5a) method.
See the class description for more information.

---

## Instance Methods

---

### storedValueForKey

`public abstract Object storedValueForKey(String key)`

Overrides the default implementation to simply
invoke [valueForKey](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpi5sw4zlsnfrvezldn5zgil3wmfwhkzkgn5zewzlz).

__See
Also:__  [storedValueForKey](EOKeyValueCoding.md#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3tumzws6rkpjnsxsvtbnr2wkq3pmruw4zzpon2g64tfmrlgc3dvmvdg64slmv4q) ( [EOKeyValueCoding](EOKeyValueCoding.md#apple-ineucq2iizduu))

---

### takeStoredValueForKey

`public abstract void takeStoredValueForKey(
Object value,
String key)`

Overrides the default implementation to simply
invoke [takeValueForKey](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpi5sw4zlsnfrvezldn5zgil3umfvwkvtbnr2wkrtpojfwk6i).

__See
Also:__  [takeStoredValueForKey](EOKeyValueCoding.md#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3tumzws6rkpjnsxsvtbnr2wkq3pmruw4zzporqwwzktorxxezlekzqwy5lfizxxes3fpe) ( [EOKeyValueCoding](EOKeyValueCoding.md#apple-ineucq2iizduu))

---

### takeValueForKey

`public void takeValueForKey(
Object value,
String key)`

Invokes the receiver's [willChange](EOEnterpriseObject.md#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3tumzws6rkpivxhizlsobzgs43fj5rguzldoqxxo2lmnrbwqylom5sq) method, and sets the value
for the property identified by _key_ to _value._ If _value_ is null,
this method removes the receiver's dictionary entry for _key._
(EOGenericRecord overrides the default implementation.) If _key_ is
not one of the receiver's attribute or relationship names, EOGenericRecord's
implementation does not invoke [handleTakeValueForUnboundKey](EOKeyValueCoding.md#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3tumzws6rkpjnsxsvtbnr2wkq3pmruw4zzpnbqw4zdmmvkgc23fkzqwy5lfizxxevlomjxxk3tejnsxs). Instead, EOGenericRecord's
implementation does nothing.

---

### valueForKey

`public Object valueForKey(String key)`

Returns the value for the property identified
by _key._ (EOGenericRecord overrides
the default implementation.) If _key_ is
not one of the receiver's attribute or relationship names, EOGenericRecord's implementation
does not invoke [handleQueryWithUnboundKey](EOKeyValueCoding.md#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3tumzws6rkpjnsxsvtbnr2wkq3pmruw4zzpnbqw4zdmmvixkzlspflws5dikvxge33vnzsewzlz). Instead,
EOGenericRecord's implementation simply returns null. This method
calls [willRead](EOFaulting.md#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3tumzws6rkpizqxk3dunfxgol3xnfwgyutfmfsa).

---

[![Table of Contents](attachments/images/up.gif)](../EOControlTOC.md)
