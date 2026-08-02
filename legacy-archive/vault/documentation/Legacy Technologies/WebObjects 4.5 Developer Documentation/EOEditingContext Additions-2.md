---
title: WebObjects 4.5 Developer Documentation
apple_id: TP40006775
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.5/System/Library/Frameworks/EOAccess.framework/ObjC_classic/Classes/EOEditingContextAdditions.html
archived_at: '2026-07-15T08:11:33.590673Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 4.5 Developer Documentation](webobjects.md)


__PATH__
[Documentation](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/index.html) __>__ [WebObjects 4.5](webobjects.md) __>__
EOAccess Reference

[![Table of Contents](attachments/images/up.gif)](../EOAccessTOC.md) 

# EOEditingContext Additions

> __Category
> of:__ EOEditingContext

> __Declared in:__  EOAccess/EOUtilities.h

---

## Category Description

---

[EOEditingContext Additions](#apple-ivhukzdjoruw4z2dn5xhizlyoqqeczdenf2gs33oom) is a collection
of convenience methods intended to make common operations with EOF
easier. [EOEditingContext Additions](#apple-ivhukzdjoruw4z2dn5xhizlyoqqeczdenf2gs33oom) is a category
on EOEditingContext provided in EOAccess.

|  |
| --- |
| The Objective-C source code for EOUtilities is available as an example. On Mac OS X Server systems, see __/System/Developer/Examples/EnterpriseObjects/Sources/EOUtilities__. On NT, see $_NEXT_ROOT___\Developer\Examples\EnterpriseObjects\Sources\EOUtilities__. |

## Method Types

---

> **Creating new objects**
> : [- createAndInsertInstanceOfEntityNamed:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2fmruxi2lom5bw63tumv4hiicbmrsgs5djn5xhgl3dojswc5dfifxgisloonsxe5cjnzzxiylomnsu6zsfnz2gs5dzjzqw2zlehi)
>
> **Fetching multiple objects**
> : [- objectsForEntityNamed:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2fmruxi2lom5bw63tumv4hiicbmrsgs5djn5xhgl3pmjvgky3uondg64sfnz2gs5dzjzqw2zlehi)
> : [- objectsForEntityNamed:qualifierFormat:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2fmruxi2lom5bw63tumv4hiicbmrsgs5djn5xhgl3pmjvgky3uondg64sfnz2gs5dzjzqw2zlehjyxkylmnftgszlsizxxe3lboq5a)
> : [- objectsMatchingValue:forKey:entityNamed:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2fmruxi2lom5bw63tumv4hiicbmrsgs5djn5xhgl3pmjvgky3uongwc5ddnbuw4z2wmfwhkzj2mzxxes3fpe5gk3tunf2hsttbnvswioq)
> : [- objectsMatchingValues:entityNamed:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2fmruxi2lom5bw63tumv4hiicbmrsgs5djn5xhgl3pmjvgky3uongwc5ddnbuw4z2wmfwhkzlthjsw45djor4u4ylnmvsdu)
> : [- objectsOfClass:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2fmruxi2lom5bw63tumv4hiicbmrsgs5djn5xhgl3pmjvgky3uonhwmq3mmfzxgoq)
> : [- objectsWithFetchSpecificationNamed:entityNamed:bindings:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2fmruxi2lom5bw63tumv4hiicbmrsgs5djn5xhgl3pmjvgky3uonlws5diizsxiy3iknygky3jmzuwgylunfxw4ttbnvswiotfnz2gs5dzjzqw2zlehjrgs3tenfxgo4z2)
>
> **Fetching single objects**
> : [- objectForEntityNamed:qualifierFormat:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2fmruxi2lom5bw63tumv4hiicbmrsgs5djn5xhgl3pmjvgky3uizxxerlooruxi6komfwwkzb2of2wc3djmzuwk4sgn5zg2yluhi)
> : [- objectMatchingValue:forKey:entityNamed:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2fmruxi2lom5bw63tumv4hiicbmrsgs5djn5xhgl3pmjvgky3ujvqxiy3infxgovtbnr2wkotgn5zewzlzhjsw45djor4u4ylnmvsdu)
> : [- objectMatchingValues:entityNamed:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2fmruxi2lom5bw63tumv4hiicbmrsgs5djn5xhgl3pmjvgky3ujvqxiy3infxgovtbnr2wk4z2mvxhi2lupfhgc3lfmq5a)
> : [- objectWithFetchSpecificationNamed:entityNamed:bindings:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2fmruxi2lom5bw63tumv4hiicbmrsgs5djn5xhgl3pmjvgky3uk5uxi2cgmv2gg2ctobswg2lgnfrwc5djn5xe4ylnmvsduzlooruxi6komfwwkzb2mjuw4zdjnztxgoq)
> : [- objectWithPrimaryKey:entityNamed:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2fmruxi2lom5bw63tumv4hiicbmrsgs5djn5xhgl3pmjvgky3uk5uxi2cqojuw2ylspffwk6j2mvxhi2lupfhgc3lfmq5a)
> : [- objectWithPrimaryKeyValue:entityNamed:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2fmruxi2lom5bw63tumv4hiicbmrsgs5djn5xhgl3pmjvgky3uk5uxi2cqojuw2ylspffwk6kwmfwhkzj2mvxhi2lupfhgc3lfmq5a)
>
> **Fetching raw rows**
> : [- executeStoredProcedureNamed:arguments:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2fmruxi2lom5bw63tumv4hiicbmrsgs5djn5xhgl3fpbswg5lumvjxi33smvsfa4tpmnswi5lsmvhgc3lfmq5gc4thovwwk3tuom5a)
> : [- objectFromRawRow:entityNamed:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2fmruxi2lom5bw63tumv4hiicbmrsgs5djn5xhgl3pmjvgky3uizzg63ksmf3ve33xhjsw45djor4u4ylnmvsdu)
> : [- rawRowsForEntityNamed:qualifierFormat:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2fmruxi2lom5bw63tumv4hiicbmrsgs5djn5xhgl3smf3ve33xondg64sfnz2gs5dzjzqw2zlehjyxkylmnftgszlsizxxe3lboq5a)
> : [- rawRowsMatchingValue:forKey:entityNamed:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2fmruxi2lom5bw63tumv4hiicbmrsgs5djn5xhgl3smf3ve33xongwc5ddnbuw4z2wmfwhkzj2mzxxes3fpe5gk3tunf2hsttbnvswioq)
> : [- rawRowsMatchingValues:entityNamed:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2fmruxi2lom5bw63tumv4hiicbmrsgs5djn5xhgl3smf3ve33xongwc5ddnbuw4z2wmfwhkzlthjsw45djor4u4ylnmvsdu)
> : [- rawRowsWithSQL:modelNamed:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2fmruxi2lom5bw63tumv4hiicbmrsgs5djn5xhgl3smf3ve33xonlws5dikniuyotnn5sgk3comfwwkzb2)
> : [- rawRowsWithStoredProcedureNamed:arguments:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2fmruxi2lom5bw63tumv4hiicbmrsgs5djn5xhgl3smf3ve33xonlws5dikn2g64tfmrihe33dmvshk4tfjzqw2zlehjqxez3vnvsw45dthi)
>
> **Accessing the EOF stack**
> : [- connectWithModelNamed:connectionDictionaryOverrides:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2fmruxi2lom5bw63tumv4hiicbmrsgs5djn5xhgl3dn5xg4zldorlws5dijvxwizlmjzqw2zlehjrw63tomvrxi2lpnzcgsy3unfxw4ylspfhxmzlsojuwizlthi)
> : [- databaseContextForModelNamed:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2fmruxi2lom5bw63tumv4hiicbmrsgs5djn5xhgl3emf2gcytbonsug33oorsxq5cgn5ze233emvwe4ylnmvsdu)
>
> **Accessing object data**
> : [- destinationKeyForSourceObject:relationshipNamed:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2fmruxi2lom5bw63tumv4hiicbmrsgs5djn5xhgl3emvzxi2lomf2gs33ojnsxsrtpojjw65lsmnsu6ytkmvrxiotsmvwgc5djn5xhg2djobhgc3lfmq5a)
> : [- localInstanceOfObject:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2fmruxi2lom5bw63tumv4hiicbmrsgs5djn5xhgl3mn5rwc3cjnzzxiylomnsu6zspmjvgky3uhi)
> : [- localInstancesOfObjects:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2fmruxi2lom5bw63tumv4hiicbmrsgs5djn5xhgl3mn5rwc3cjnzzxiylomnsxgt3gj5rguzldorztu)
> : [- primaryKeyForObject:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2fmruxi2lom5bw63tumv4hiicbmrsgs5djn5xhgl3qojuw2ylspffwk6kgn5ze6ytkmvrxioq)
>
> **Accessing model information**
> : [- entityForClass:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2fmruxi2lom5bw63tumv4hiicbmrsgs5djn5xhgl3fnz2gs5dzizxxeq3mmfzxgoq)
> : [- entityForObject:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2fmruxi2lom5bw63tumv4hiicbmrsgs5djn5xhgl3fnz2gs5dzizxxet3cnjswg5b2)
> : [- entityNamed:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2fmruxi2lom5bw63tumv4hiicbmrsgs5djn5xhgl3fnz2gs5dzjzqw2zlehi)
> : [- modelGroup](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2fmruxi2lom5bw63tumv4hiicbmrsgs5djn5xhgl3nn5sgk3chojxxk4a)

## Instance Methods

---

### connectWithModelNamed:connectionDictionaryOverrides:

`- (void)connectWithModelNamed:(NSString
*)modelName
connectionDictionaryOverrides:(NSDictionary
*)overrides`

Connects to the database using the connection
information in the specified model and the provided overrides dictionary.
This method facilitates per-session database logins in WebObjects
applications. Typically, you'd put a login name and password in
the overrides dictionary and otherwise use the values in the model's
connection dictionary. Raises an exception if the connection failed.

---

### __createAndInsertInstanceOfEntityNamed:__

`- (id)createAndInsertInstanceOfEntityNamed:(NSString
*)entityName`

Creates a new enterprise object for the specified
entity, inserts it into the receiver, and returns the new object.

---

### databaseContextForModelNamed:

`- (EODatabaseContext *)databaseContextForModelNamed:(NSString
*)modelName`

Returns the database context used to service
the specified model.

---

### destinationKeyForSourceObject:relationshipNamed:

`- (NSDictionary *)destinationKeyForSourceObject:(id)object
relationshipNamed:(NSString *)relationshipName`

Returns the foreign key for the rows at the
destination entity of the specified relationship. As an example,
given entities Department and Employee with a relationship called
"department" joining `Department.ID` and `Employee.deptID`,
invoking this method on a Department object with ID equal to 5 returns
a dictionary with a value of 5 for the `deptID` key.

__See
Also:__  [- primaryKeyForObject:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2fmruxi2lom5bw63tumv4hiicbmrsgs5djn5xhgl3qojuw2ylspffwk6kgn5ze6ytkmvrxioq)

---

### entityForClass:

`- (EOEntity *)entityForClass:(Class)classObject`

Returns the entity associated with the specified
class. Raises an exception if the specified entity can't be found
or if more than one entity is associated with the class.

__See
Also:__  [- entityForObject:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2fmruxi2lom5bw63tumv4hiicbmrsgs5djn5xhgl3fnz2gs5dzizxxet3cnjswg5b2), [- entityNamed:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2fmruxi2lom5bw63tumv4hiicbmrsgs5djn5xhgl3fnz2gs5dzjzqw2zlehi), [- objectsOfClass:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2fmruxi2lom5bw63tumv4hiicbmrsgs5djn5xhgl3pmjvgky3uonhwmq3mmfzxgoq)

---

### entityForObject:

`- (EOEntity *)entityForObject:(id)object`

Returns the entity associated with the provided
enterprise object. Raises an exception if the specified entity can't
be found.

__See Also:__  [- entityForClass:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2fmruxi2lom5bw63tumv4hiicbmrsgs5djn5xhgl3fnz2gs5dzizxxeq3mmfzxgoq), [- entityNamed:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2fmruxi2lom5bw63tumv4hiicbmrsgs5djn5xhgl3fnz2gs5dzjzqw2zlehi)

---

### entityNamed:

`- (EOEntity *)entityNamed:(NSString
*)entityName`

Returns the entity with the specified name. Raises an
exception if the specified entity can't be found.

__See
Also:__  [- entityForClass:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2fmruxi2lom5bw63tumv4hiicbmrsgs5djn5xhgl3fnz2gs5dzizxxeq3mmfzxgoq), [- entityForObject:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2fmruxi2lom5bw63tumv4hiicbmrsgs5djn5xhgl3fnz2gs5dzizxxet3cnjswg5b2)

---

### executeStoredProcedureNamed:arguments:

`- (NSDictionary *)executeStoredProcedureNamed:(NSString
*)storedProcedureName
arguments:(NSDictionary *)arguments`

Executes the specified stored procedure with
the provided arguments. Returns the stored procedure's return
values (if any). Use only with stored procedures that don't return
results rows.

__See Also:__  [- rawRowsWithStoredProcedureNamed:arguments:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2fmruxi2lom5bw63tumv4hiicbmrsgs5djn5xhgl3smf3ve33xonlws5dikn2g64tfmrihe33dmvshk4tfjzqw2zlehjqxez3vnvsw45dthi)

---

### localInstanceOfObject:

`- (id)localInstanceOfObject:(id)object`

Translates the specified enterprise object from
another editing context to the specified one.

__See
Also:__  [- localInstancesOfObjects:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2fmruxi2lom5bw63tumv4hiicbmrsgs5djn5xhgl3mn5rwc3cjnzzxiylomnsxgt3gj5rguzldorztu)

---

### localInstancesOfObjects:

`- (NSArray *)localInstancesOfObjects:(NSArray
*)objects`

Translates the specified enterprise objects
from another editing context to the specified one.

__See
Also:__  [- localInstanceOfObject:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2fmruxi2lom5bw63tumv4hiicbmrsgs5djn5xhgl3mn5rwc3cjnzzxiylomnsu6zspmjvgky3uhi)

---

### modelGroup

`- (EOModelGroup *)modelGroup`

Returns the model group associated with the
editing context's root object store, an EOObjectStoreCoordinator.

---

### objectFromRawRow:entityNamed:

`- (id)objectFromRawRow:(NSDictionary
*)row
entityNamed:(NSString *)entityName`

Fetches and returns the object corresponding
to the specified raw row (using EOEditingContext's __faultForRawRow:entityNamed:__).
This method can only be used on raw rows that include the row's primary
key.

---

### objectMatchingValue:forKey:entityNamed:

`- (id)objectMatchingValue:(id)value
forKey:(NSString *)key
entityNamed:(NSString *)entityName`

Creates an EOKeyValueQualifier with the specified
key and value and returns matching enterprise objects. Raises an `EOMoreThanOneException` unless
exactly one object is retrieved.

__See Also:__  [- objectMatchingValues:entityNamed:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2fmruxi2lom5bw63tumv4hiicbmrsgs5djn5xhgl3pmjvgky3ujvqxiy3infxgovtbnr2wk4z2mvxhi2lupfhgc3lfmq5a), [- objectsMatchingValue:forKey:entityNamed:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2fmruxi2lom5bw63tumv4hiicbmrsgs5djn5xhgl3pmjvgky3uongwc5ddnbuw4z2wmfwhkzj2mzxxes3fpe5gk3tunf2hsttbnvswioq)

---

### objectMatchingValues:entityNamed:

`- (id)objectMatchingValues:(NSDictionary
*)values
entityNamed:(NSString *)entityName`

Creates EOKeyValueQualifiers for each key-value
pair in the specified dictionary, ANDs these qualifiers together
into an EOAndQualifier, and returns matching enterprise objects. Raises an `EOMoreThanOneException` unless
exactly one object is retrieved.

__See Also:__  [- objectMatchingValue:forKey:entityNamed:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2fmruxi2lom5bw63tumv4hiicbmrsgs5djn5xhgl3pmjvgky3ujvqxiy3infxgovtbnr2wkotgn5zewzlzhjsw45djor4u4ylnmvsdu), [- objectsMatchingValues:entityNamed:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2fmruxi2lom5bw63tumv4hiicbmrsgs5djn5xhgl3pmjvgky3uongwc5ddnbuw4z2wmfwhkzlthjsw45djor4u4ylnmvsdu)

---

### objectsForEntityNamed:

`- (NSArray *)objectsForEntityNamed:(NSString
*)entityName`

Fetches and returns the enterprise objects associated
with the specified entity.

__See Also:__  [- objectsForEntityNamed:qualifierFormat:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2fmruxi2lom5bw63tumv4hiicbmrsgs5djn5xhgl3pmjvgky3uondg64sfnz2gs5dzjzqw2zlehjyxkylmnftgszlsizxxe3lboq5a), [- objectsMatchingValue:forKey:entityNamed:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2fmruxi2lom5bw63tumv4hiicbmrsgs5djn5xhgl3pmjvgky3uongwc5ddnbuw4z2wmfwhkzj2mzxxes3fpe5gk3tunf2hsttbnvswioq), [- objectsMatchingValues:entityNamed:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2fmruxi2lom5bw63tumv4hiicbmrsgs5djn5xhgl3pmjvgky3uongwc5ddnbuw4z2wmfwhkzlthjsw45djor4u4ylnmvsdu)

---

### objectsMatchingValue:forKey:entityNamed:

`- (NSArray *)objectsMatchingValue:(id)value
forKey:(NSString *)key
entityNamed:(NSString *)entityName`

Creates an EOKeyValueQualifier with the specified
key and value and returns matching enterprise objects.

__See
Also:__  [- objectMatchingValue:forKey:entityNamed:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2fmruxi2lom5bw63tumv4hiicbmrsgs5djn5xhgl3pmjvgky3ujvqxiy3infxgovtbnr2wkotgn5zewzlzhjsw45djor4u4ylnmvsdu), [- objectsForEntityNamed:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2fmruxi2lom5bw63tumv4hiicbmrsgs5djn5xhgl3pmjvgky3uondg64sfnz2gs5dzjzqw2zlehi), [- objectsMatchingValues:entityNamed:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2fmruxi2lom5bw63tumv4hiicbmrsgs5djn5xhgl3pmjvgky3uongwc5ddnbuw4z2wmfwhkzlthjsw45djor4u4ylnmvsdu)

---

### objectsMatchingValues:entityNamed:

`- (NSArray *)objectsMatchingValues:(NSDictionary
*)values
entityNamed:(NSString *)entityName`

Creates EOKeyValueQualifiers for each key-value
pair in the specified dictionary, ANDs these qualifiers together
into an EOAndQualifier, and returns matching enterprise objects.

__See
Also:__  [- objectMatchingValues:entityNamed:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2fmruxi2lom5bw63tumv4hiicbmrsgs5djn5xhgl3pmjvgky3ujvqxiy3infxgovtbnr2wk4z2mvxhi2lupfhgc3lfmq5a), [- objectsForEntityNamed:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2fmruxi2lom5bw63tumv4hiicbmrsgs5djn5xhgl3pmjvgky3uondg64sfnz2gs5dzjzqw2zlehi), [- objectsMatchingValue:forKey:entityNamed:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2fmruxi2lom5bw63tumv4hiicbmrsgs5djn5xhgl3pmjvgky3uongwc5ddnbuw4z2wmfwhkzj2mzxxes3fpe5gk3tunf2hsttbnvswioq)

---

### objectsOfClass:

`- (NSArray *)objectsOfClass:(Class)classObject`

Fetches and returns the enterprise objects associated
with the specified class. Raises an `EOMoreThanOneException` if
more than one entity for the class exists.

__See
Also:__  [- entityForClass:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2fmruxi2lom5bw63tumv4hiicbmrsgs5djn5xhgl3fnz2gs5dzizxxeq3mmfzxgoq)

---

### objectsWithFetchSpecificationNamed:entityNamed:bindings:

`- (NSArray *)objectsWithFetchSpecificationNamed:(NSString
*)fetchSpecName
entityNamed:(NSString *)entityName
bindings:(NSDictionary *)bindings`

Fetches and returns the enterprise objects retrieved
with the specified fetch specification and bindings.

__See
Also:__  [- objectWithFetchSpecificationNamed:entityNamed:bindings:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2fmruxi2lom5bw63tumv4hiicbmrsgs5djn5xhgl3pmjvgky3uk5uxi2cgmv2gg2ctobswg2lgnfrwc5djn5xe4ylnmvsduzlooruxi6komfwwkzb2mjuw4zdjnztxgoq)

---

### objectsForEntityNamed:qualifierFormat:

`- (NSArray *)objectsForEntityNamed:(NSString
*)entityName
qualifierFormat:(NSString *)format,
...`

Creates a qualifier with the provided format
string and arguments, and returns matching enterprise objects.

__See
Also:__  [- objectForEntityNamed:qualifierFormat:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2fmruxi2lom5bw63tumv4hiicbmrsgs5djn5xhgl3pmjvgky3uizxxerlooruxi6komfwwkzb2of2wc3djmzuwk4sgn5zg2yluhi), [- objectsForEntityNamed:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2fmruxi2lom5bw63tumv4hiicbmrsgs5djn5xhgl3pmjvgky3uondg64sfnz2gs5dzjzqw2zlehi)

---

### objectWithFetchSpecificationNamed:entityNamed:bindings:

`- (id)objectWithFetchSpecificationNamed:(NSString
*)fetchSpecName
entityNamed:(NSString *)entityName
bindings:(NSDictionary *)bindings`

Fetches and returns the enterprise objects retrieved
with the specified fetch specification and bindings. Raises an `EOMoreThanOneException` unless
exactly one object is retrieved.

__See Also:__  [- objectsWithFetchSpecificationNamed:entityNamed:bindings:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2fmruxi2lom5bw63tumv4hiicbmrsgs5djn5xhgl3pmjvgky3uonlws5diizsxiy3iknygky3jmzuwgylunfxw4ttbnvswiotfnz2gs5dzjzqw2zlehjrgs3tenfxgo4z2)

---

### objectWithPrimaryKey:entityNamed:

`- (id)objectWithPrimaryKey:(NSDictionary
*)keyDictionary
entityNamed:(NSString *)entityName`

Fetches and returns the enterprise object identified
by the specified primary key dictionary. Raises an `EOMoreThanOneException` unless
exactly one object is retrieved.

__See Also:__  [- objectMatchingValue:forKey:entityNamed:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2fmruxi2lom5bw63tumv4hiicbmrsgs5djn5xhgl3pmjvgky3ujvqxiy3infxgovtbnr2wkotgn5zewzlzhjsw45djor4u4ylnmvsdu), [- objectWithPrimaryKeyValue:entityNamed:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2fmruxi2lom5bw63tumv4hiicbmrsgs5djn5xhgl3pmjvgky3uk5uxi2cqojuw2ylspffwk6kwmfwhkzj2mvxhi2lupfhgc3lfmq5a), [- primaryKeyForObject:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2fmruxi2lom5bw63tumv4hiicbmrsgs5djn5xhgl3qojuw2ylspffwk6kgn5ze6ytkmvrxioq)

---

### objectWithPrimaryKeyValue:entityNamed:

`- (id)objectWithPrimaryKeyValue:(id)value
entityNamed:(NSString *)entityName`

Fetches and returns the enterprise object identified
by the specified primary key value. For use only with enterprise
objects that have non-compound primary keys. Raises an `EOMoreThanOneException` unless
exactly one object is retrieved.

__See Also:__  [- objectsMatchingValues:entityNamed:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2fmruxi2lom5bw63tumv4hiicbmrsgs5djn5xhgl3pmjvgky3uongwc5ddnbuw4z2wmfwhkzlthjsw45djor4u4ylnmvsdu), [- objectWithPrimaryKey:entityNamed:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2fmruxi2lom5bw63tumv4hiicbmrsgs5djn5xhgl3pmjvgky3uk5uxi2cqojuw2ylspffwk6j2mvxhi2lupfhgc3lfmq5a)

---

### objectForEntityNamed:qualifierFormat:

`- (id)objectForEntityNamed:(NSString
*)entityName
qualifierFormat:(NSString *)format,
...`

Creates a qualifier with the provided format
string and arguments, and returns matching enterprise objects. Raises an `EOMoreThanOneException` unless
exactly one object is retrieved.

__See Also:__  [- objectsForEntityNamed:qualifierFormat:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2fmruxi2lom5bw63tumv4hiicbmrsgs5djn5xhgl3pmjvgky3uondg64sfnz2gs5dzjzqw2zlehjyxkylmnftgszlsizxxe3lboq5a), [- rawRowsForEntityNamed:qualifierFormat:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2fmruxi2lom5bw63tumv4hiicbmrsgs5djn5xhgl3smf3ve33xondg64sfnz2gs5dzjzqw2zlehjyxkylmnftgszlsizxxe3lboq5a)

---

### primaryKeyForObject:

`- (NSDictionary *)primaryKeyForObject:(id)object`

Returns the primary key dictionary for the specified
enterprise object.

__See Also:__  [- objectWithPrimaryKey:entityNamed:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2fmruxi2lom5bw63tumv4hiicbmrsgs5djn5xhgl3pmjvgky3uk5uxi2cqojuw2ylspffwk6j2mvxhi2lupfhgc3lfmq5a), [- objectWithPrimaryKeyValue:entityNamed:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2fmruxi2lom5bw63tumv4hiicbmrsgs5djn5xhgl3pmjvgky3uk5uxi2cqojuw2ylspffwk6kwmfwhkzj2mvxhi2lupfhgc3lfmq5a)

---

### rawRowsWithSQL:modelNamed:

`- (NSArray *)rawRowsWithSQL:(NSString
*)sqlString
modelNamed:(NSString *)modelName`

Evaluates the specified SQL and returns the
resulting raw rows.

__See Also:__  [- rawRowsForEntityNamed:qualifierFormat:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2fmruxi2lom5bw63tumv4hiicbmrsgs5djn5xhgl3smf3ve33xondg64sfnz2gs5dzjzqw2zlehjyxkylmnftgszlsizxxe3lboq5a), [- rawRowsWithStoredProcedureNamed:arguments:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2fmruxi2lom5bw63tumv4hiicbmrsgs5djn5xhgl3smf3ve33xonlws5dikn2g64tfmrihe33dmvshk4tfjzqw2zlehjqxez3vnvsw45dthi)

---

### rawRowsWithStoredProcedureNamed:arguments:

`- (NSArray *)rawRowsWithStoredProcedureNamed:(NSString
*)storedProcedureName
arguments:(NSDictionary *)arguments`

Executes the specified stored procedure with
the provided arguments and returns the resulting raw rows.

__See
Also:__  [- rawRowsWithSQL:modelNamed:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2fmruxi2lom5bw63tumv4hiicbmrsgs5djn5xhgl3smf3ve33xonlws5dikniuyotnn5sgk3comfwwkzb2)

---

### rawRowsMatchingValue:forKey:entityNamed:

`- (NSArray *)rawRowsMatchingValue:(id)value
forKey:(NSString *)key
entityNamed:(NSString *)entityName`

Creates an EOKeyValueQualifier with the specified
key and value and returns matching raw rows.

__See
Also:__  [- objectMatchingValue:forKey:entityNamed:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2fmruxi2lom5bw63tumv4hiicbmrsgs5djn5xhgl3pmjvgky3ujvqxiy3infxgovtbnr2wkotgn5zewzlzhjsw45djor4u4ylnmvsdu), [- objectsMatchingValue:forKey:entityNamed:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2fmruxi2lom5bw63tumv4hiicbmrsgs5djn5xhgl3pmjvgky3uongwc5ddnbuw4z2wmfwhkzj2mzxxes3fpe5gk3tunf2hsttbnvswioq), [- rawRowsMatchingValues:entityNamed:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2fmruxi2lom5bw63tumv4hiicbmrsgs5djn5xhgl3smf3ve33xongwc5ddnbuw4z2wmfwhkzlthjsw45djor4u4ylnmvsdu)

---

### rawRowsMatchingValues:entityNamed:

`- (NSArray *)rawRowsMatchingValues:(NSDictionary
*)values
entityNamed:(NSString *)entityName`

Creates EOKeyValueQualifiers for each key-value
pair in the specified dictionary, ANDs these qualifiers together
into an EOAndQualifier, and returns matching raw rows.

__See
Also:__  [- objectMatchingValues:entityNamed:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2fmruxi2lom5bw63tumv4hiicbmrsgs5djn5xhgl3pmjvgky3ujvqxiy3infxgovtbnr2wk4z2mvxhi2lupfhgc3lfmq5a), [- objectsMatchingValues:entityNamed:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2fmruxi2lom5bw63tumv4hiicbmrsgs5djn5xhgl3pmjvgky3uongwc5ddnbuw4z2wmfwhkzlthjsw45djor4u4ylnmvsdu), [- rawRowsMatchingValue:forKey:entityNamed:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2fmruxi2lom5bw63tumv4hiicbmrsgs5djn5xhgl3smf3ve33xongwc5ddnbuw4z2wmfwhkzj2mzxxes3fpe5gk3tunf2hsttbnvswioq)

---

### rawRowsForEntityNamed:qualifierFormat:

`- (NSArray *)rawRowsForEntityNamed:(NSString
*)entityName
qualifierFormat:(NSString *)format,
...`

Creates a qualifier for the specified entity
and with the specified qualifier format and returns matching raw
row dictionaries.

__See Also:__  [- objectsForEntityNamed:qualifierFormat:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2fmruxi2lom5bw63tumv4hiicbmrsgs5djn5xhgl3pmjvgky3uondg64sfnz2gs5dzjzqw2zlehjyxkylmnftgszlsizxxe3lboq5a), [- rawRowsWithSQL:modelNamed:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2fmruxi2lom5bw63tumv4hiicbmrsgs5djn5xhgl3smf3ve33xonlws5dikniuyotnn5sgk3comfwwkzb2)

---

[![Table of Contents](attachments/images/up.gif)](../EOAccessTOC.md)
