---
title: WebObjects 4.5 Developer Documentation
apple_id: TP40006775
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.5/System/Library/Frameworks/EOControl.framework/ObjC_classic/Classes/EOGenericRecord.html
archived_at: '2026-07-15T08:11:39.809928Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 4.5 Developer Documentation](webobjects.md)


__PATH__
[Documentation](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/index.html) __>__ [WebObjects 4.5](webobjects.md) __>__
EOControl Reference

[![Table of Contents](attachments/images/up.gif)](../EOControlTOC.md) 

# EOGenericRecord

> **__Inherits
> from:__**
> : NSObject

> **__Conforms to:__**
> : NSCoding
> : NSObject (NSObject)

> __Declared in:__ : EOControl/EOGenericRecord.h

---

## Class Description

---

EOGenericRecord is a generic enterprise object class that
can be used in place of custom classes when you don't need custom
behavior. It implements the [EOEnterpriseObject](EOEnterpriseObject-3.md#apple-ijaueqsdjbfeq) interface
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
the EOClassDescription method [createInstanceWithEditingContext:globalID:zone:](EOClassDescription-3.md#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2dnrqxg42emvzwg4tjob2gs33of5rxezlborsus3ttorqw4y3fk5uxi2cfmruxi2lom5bw63tumv4hiothnrxweylmjfcdu6tpnzstu) as
follows:

> ```
> id newEO;
> NSString *entityName;             // Assume this exists.
>
> newEO = [[EOClassDescription classDescriptionForEntityName:entityName]
>     createInstanceWithEditingContext:nil
>     globalID:nil
>      zone:nil];
> ```

__createInstanceWithEditingContext:globalID:zone:__ is
preferable to EOGenericRecord's __init...__ method because
the same code works if you later use a custom enterprise object
class instead of EOGenericRecord. You can get an EOClassDescription
for an entity name as shown above. Alternatively, you can get an
EOClassDescription for a destination key of an existing enterprise
object as follows:

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

The technique in this example is useful for inserting a new
destination object into an existing enterprise object-for creating
a new Movie object to add to a Studio's array of Movies, for example.

## Class Methods

---

### useDeferredFaultCreation

`+ (BOOL)useDeferredFaultCreation`

Returns YES, specifying that EOGenericRecords
use deferred faulting (which is more efficient than the regular
faulting mechanism).

---

## Instance Methods

---

### init

`- (id)init`

Don't invoke
this method. It doesn't work to create instances of EOGenericRecord
or its subclasses. Subclasses of EOGenericRecord shouldn't implement
this method. Rather, they should implement [initWithEditingContext:classDescription:globalID:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2hmvxgk4tjmnjgky3pojsc62lonf2fo2lunbcwi2lunfxgoq3pnz2gk6duhjrwyyltoncgk43dojuxa5djn5xduz3mn5rgc3cjiq5a).

---

### initWithEditingContext:classDescription:globalID:

`- (id)initWithEditingContext:(EOEditingContext
*)anEditingContext
classDescription:(EOClassDescription
*)aClassDescription
globalID:(EOGlobalID *)globalID`

The designated initializer, this method initializes
a newly allocated EOGenericRecord to get its metadata from _aClassDescription_.
You should pass __nil__ for _anEditingContext_ and _globalID_,
because the arguments are optional: EOGenericRecord's implementation
does nothing with them. Raises an NSInternalInconsistencyException
if _aClassDescription_ is __nil__.
Returns __self__.

You shouldn't use
this method to create new EOGenericRecords. Rather, use EOClassDescription's [createInstanceWithEditingContext:globalID:zone:](EOClassDescription-3.md#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2dnrqxg42emvzwg4tjob2gs33of5rxezlborsus3ttorqw4y3fk5uxi2cfmruxi2lom5bw63tumv4hiothnrxweylmjfcdu6tpnzstu) method.
See the class description for more information.

---

### storedValueForKey:

`- (id)storedValueForKey:(NSString
*)key`

Overrides the default implementation to simply
invoke [valueForKey:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2hmvxgk4tjmnjgky3pojsc65tbnr2wkrtpojfwk6j2).

__See
Also:__  [storedValueForKey:](EOKeyValueCoding-3.md#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw45dgnuxukt2lmv4vmylmovsug33enfxgol3torxxezlekzqwy5lfizxxes3fpe5a) ( [EOKeyValueCoding](EOKeyValueCoding-3.md#apple-ineucq2iizduu))

---

### takeStoredValue:forKey:

`- (void)takeStoredValue:(id)value
forKey:(NSString *)key`

Overrides the default implementation to simply
invoke [takeValue:forKey:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2hmvxgk4tjmnjgky3pojsc65dbnnsvmylmovstuztpojfwk6j2).

__See
Also:__  [takeStoredValue:forKey:](EOKeyValueCoding-3.md#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw45dgnuxukt2lmv4vmylmovsug33enfxgol3umfvwku3un5zgkzcwmfwhkzj2mzxxes3fpe5a) ( [EOKeyValueCoding](EOKeyValueCoding-3.md#apple-ineucq2iizduu))

---

### takeValue:forKey:

`- (void)takeValue:(id)value
forKey:(NSString *)key`

Invokes the receiver's [willChange](EOEnterpriseObject-3.md#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw45dgnuxukt2fnz2gk4tqojuxgzkpmjvgky3uf53ws3dminugc3thmu) method, and sets the value
for the property identified by _key_ to _value_. If _value_ is nil,
this method removes the receiver's dictionary entry for _key_.
(EOGenericRecord overrides the default implementation.) If _key_ is
not one of the receiver's attribute or relationship names, EOGenericRecord's
implementation does not invoke [handleTakeValue:forUnboundKey:](EOKeyValueCoding-3.md#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw45dgnuxukt2lmv4vmylmovsug33enfxgol3imfxgi3dfkrqwwzkwmfwhkzj2mzxxevlomjxxk3tejnsxsoq). Instead, EOGenericRecord's
implementation does nothing.

---

### valueForKey:

`- (id)valueForKey:(NSString
*)key`

Returns the value for the property identified
by _key_. (EOGenericRecord overrides
the default implementation.) If _key_ is
not one of the receiver's attribute or relationship names, EOGenericRecord's implementation
does not invoke [handleQueryWithUnboundKey:](EOKeyValueCoding-3.md#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw45dgnuxukt2lmv4vmylmovsug33enfxgol3imfxgi3dfkf2wk4tzk5uxi2cvnzrg65lomrfwk6j2). Instead,
EOGenericRecord's implementation simply returns nil.

---

[![Table of Contents](attachments/images/up.gif)](../EOControlTOC.md)
