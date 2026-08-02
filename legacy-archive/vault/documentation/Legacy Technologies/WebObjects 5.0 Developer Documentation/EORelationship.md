---
title: WebObjects 5.0 Developer Documentation
apple_id: TP40006776
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_5/EOAccessRef/Java/Classes/EORelationship.html
archived_at: '2026-07-15T08:13:41.680573Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 5.0 Developer Documentation](webobjects.md)


|  |
| --- |
| __PATH__[Documentation](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/index.html) __>__ [WebObjects](webobjects.md) |

[![Table of Contents](attachments/EOAccessRef/Java/Art/up.gif)](../EOAccessTOC.md) 

# EORelationship

> __Inherits from:__ Object
>
> __Implements:__
> EOPropertyListEncoding
> EOSQLExpression.SQLValue
>
> __Package:__ com.webobjects.eoaccess

---

## Class Description

---

An EORelationship describes an association between two entities, based on attributes of those two entities. By defining EORelationships in your application's EOModel, you can cause the relationships defined in the database to be automatically resolved as enterprise objects are fetched. For example, a Movie entity may contain its __studioId__ as an attribute, but without an EORelationship __studioId__ will only appear in a movie enterprise object as a number. With an EORelationship explicitly connecting the Movie entity to a Studio entity, a movie enterprise object will automatically be given its studio enterprise object when an EODatabaseChannel fetches it from the database. The two entities that make up a relationship can be in the same model or two different models, as long as they are in the same model group.

You usually define relationships in your EOModel with the EOModeler application, which is documented in _Enterprise Objects Framework Tools and Techniques_. EORelationships are primarily for use by the Enterprise Objects Framework; unless you have special needs you shouldn't need to access them in your application's code. If you have such a need, you can create your own EORelationship objects as outlined in the sections ["Creating a Simple Relationship" (page 281)](EORelationship.Concepts.md#apple-ineeuqscjjeui) and ["Creating a Flattened Relationship" (page 283)](EORelationship.Concepts.md#apple-ineeurcbi5cui).

A relationship is directional: One entity is considered the source, and the other is considered the destination. The relationship belongs to the source entity, and may only be traversed from source to destination. To simulate a two-way relationship you have to create an EORelationship for each direction. Although the relationship is directional, no inverse is implied (although an inverse relationship may exist).

A relationship maintains an array of joins identifying attributes from the related entities (see the EOJoin class specification for more information). Most relationships simply relate the objects of one entity to those of another by comparing attribute values between them. Such a relationship must be defined as to-one or to-many based on how many objects of the destination match each object of the source. This is called the __cardinality__ of the relationship. In a to-one relationship, there must be exactly one destination object for each source object; in a to-many relationship there can be any number of destination objects for each source object. See ["Creating a Simple Relationship"](EORelationship.Concepts.md#apple-ineeuqscjjeui) for more information.

A chain of relationships across several entities can be flattened, creating a single relationship that spans them all. For example, suppose you have a relationship between movies and directors, and a relationship between directors and talent. You can traverse these relationships to create a flattened relationship going directly from movies to talent. A flattened relationship is determined to be to-many or to-one based on the relationships it spans; if all are to-one, then the flattened relationship is to-one, but if any of them is to-many the flattened relationship is to-many. See ["Creating a Flattened Relationship" (page 283](EORelationship.Concepts.md#apple-ineeurcbi5cui)) for more information.

Like the other major modeling classes, EORelationship provides a user dictionary that the application can use to store application-specific information related to the relationship.

## Specifying the Join Semantic

The relationship holds the join semantic; you specify this semantic with [setJoinSemantic](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpkjswyylunfxw443infyc643forfg62loknsw2ylooruwg). There are four types of join semantic : [InnerJoin](#apple-ineeuskii5cuc), [FullOuterJoin](#apple-ineeurkfiraue), [LeftOuterJoin](#apple-ineeusckivbus), and [RightOuterJoin](#apple-ineeuskjifdee). An inner join produces results only for destinations of the join relationship that have non-NULL values. A full outer join produces results for all source records, regardless of the values of the relationships. A left outer join preserves rows in the left (source) table, keeping them even if there's no corresponding row in the right table, while a right outer join preserves rows in the right (destination) table. Note that not all join semantics are supported by all database servers.

## Constants

---

EORelationship defines the following `int` constants to specify the manner in which a join should be made:

- InnerJoin
- FullOuterJoin
- LeftOuterJoin
- RightOuterJoin

## Interfaces Implemented

---

> EOPropertyListEncoding
> awakeWithPropertyList
> encodeIntoPropertyList

## Method Types

---

> Constructors
> [EORelationship](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpkjswyylunfxw443infyc6rkpkjswyylunfxw443infya)
>
> Accessing the relationship name
> [beautifyName](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpkjswyylunfxw443infyc6ytfmf2xi2lgpfhgc3lf)
> [name](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpkjswyylunfxw443infyc63tbnvsq)
> [setName](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpkjswyylunfxw443infyc643forhgc3lf)
>
> Using joins
> [addJoin](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpkjswyylunfxw443infyc6ylemrfg62lo)
> [joins](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpkjswyylunfxw443infyc62tpnfxhg)
> [joinSemantic](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpkjswyylunfxw443infyc62tpnfxfgzlnmfxhi2ld)
> [removeJoin](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpkjswyylunfxw443infyc64tfnvxxmzkkn5uw4)
> [setJoinSemantic](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpkjswyylunfxw443infyc643forfg62loknsw2ylooruwg)
>
> Accessing attributes joined on
> [destinationAttributes](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpkjswyylunfxw443infyc6zdfon2gs3tboruw63sbor2he2lcov2gk4y)
> [sourceAttributes](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpkjswyylunfxw443infyc643povzggzkbor2he2lcov2gk4y)
>
> Accessing the definition
> [componentRelationships](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpkjswyylunfxw443infyc6y3pnvyg63tfnz2fezlmmf2gs33oonugs4dt)
> [definition](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpkjswyylunfxw443infyc6zdfmzuw42lunfxw4)
> [setDefinition](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpkjswyylunfxw443infyc643forcgkztjnzuxi2lpny)
>
> Accessing the entities joined
> [anyInverseRelationship](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpkjswyylunfxw443infyc6ylopfew45tfojzwkutfnrqxi2lpnzzwq2lq)
> [destinationEntity](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_5/EOAccessRef/Java/Classes/EORelationship.html#//apple_ref/java/instm/EORelationship/destinationEntity)
> [entity](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpkjswyylunfxw443infyc6zlooruxi6i)
> [inverseRelationship](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpkjswyylunfxw443infyc62loozsxe43fkjswyylunfxw443infya)
> [setEntity](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpkjswyylunfxw443infyc643forcw45djor4q)
>
> Checking the relationship type
> [isCompound](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpkjswyylunfxw443infyc62ltinxw24dpovxgi)
> [isFlattened](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpkjswyylunfxw443infyc62ltizwgc5dumvxgkza)
> [isMandatory](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpkjswyylunfxw443infyc62ltjvqw4zdborxxe6i)
> [setIsMandatory](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpkjswyylunfxw443infyc643forexgtlbnzsgc5dpoj4q)
> [validateValue](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpkjswyylunfxw443infyc65tbnruwiylumvlgc3dvmu)
>
> Accessing whether the relationship is to-many
> [isToMany](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpkjswyylunfxw443infyc62ltkrxu2ylope)
> [setToMany](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpkjswyylunfxw443infyc643forkg6tlbnz4q)
>
> Relationship qualifiers
> [qualifierWithSourceRow](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpkjswyylunfxw443infyc64lvmfwgsztjmvzfo2lunbjw65lsmnsve33x)
>
> Checking references
> [referencesProperty](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpkjswyylunfxw443infyc64tfmzsxezlomnsxgudsn5ygk4tupe)
>
> Controlling batch fetches
> [numberOfToManyFaultsToBatchFetch](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpkjswyylunfxw443infyc63tvnvrgk4spmzkg6tlbnz4umylvnr2hgvdpijqxiy3iizsxiy3i)
> [setNumberOfToManyFaultsToBatchFetch](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpkjswyylunfxw443infyc643forhhk3lcmvze6zsun5gwc3tzizqxk3duonkg6qtborrwqrtforrwq)
>
> Taking action upon a change
> [deleteRule](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpkjswyylunfxw443infyc6zdfnrsxizksovwgk)
> [propagatesPrimaryKey](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpkjswyylunfxw443infyc64dsn5ygcz3borsxgudsnfwwc4tzjnsxs)[setDeleteRule](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpkjswyylunfxw443infyc643forcgk3dforsve5lmmu)
> [setPropagatesPrimaryKey](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpkjswyylunfxw443infyc643forihe33qmftwc5dfonihe2lnmfzhss3fpe)
> [ownsDestination](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpkjswyylunfxw443infyc633xnzzuizltoruw4ylunfxw4)
> [setOwnsDestination](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpkjswyylunfxw443infyc643forhxo3ttirsxg5djnzqxi2lpny)
>
> Accessing the user dictionary
> [setUserInfo](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpkjswyylunfxw443infyc643forkxgzlsjfxgm3y)
> [userInfo](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpkjswyylunfxw443infyc65ltmvzes3tgn4)

## Constructors

---

### EORelationship

`public EORelationship()`

Description forthcoming.

`public EORelationship( NSDictionary propertyList, EOEntity owner)`

Creates and returns a new EORelationship is initialized from _propertyList_-a dictionary containing only property list data types (that is, NSDictionaries, Strings, NSArrays, and next.util.ImmutableBytes). This constructor is used by EOModeler when it reads in a Model from a file, for example. The _owner_ argument should be the EORelationship's Entity. EORelationships created from a property list must receive an awakeWithPropertyList message immediately after creation before they are fully functional, but the __awake...__ message should be deferred until the all of the other objects in the model have also been created.

__See Also:__ encodeIntoPropertyList (EOPropertyListEncoding interface)

---

## Instance Methods

---

### addJoin

`public void addJoin(EOJoin aJoin)`

Adds a source-destination attribute pair to the relationship. Throws an exception if the relationship is flattened, if either the source or destination attributes are flattened, or if either of _aJoin_'s attributes already belongs to another join of the relationship.

__See Also:__ [joins](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpkjswyylunfxw443infyc62tpnfxhg), [isFlattened](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpkjswyylunfxw443infyc62ltizwgc5dumvxgkza), [setDefinition](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpkjswyylunfxw443infyc643forcgkztjnzuxi2lpny)

---

### anyInverseRelationship

`public EORelationship anyInverseRelationship()`

Searches the relationship's destination entity for a user-created, back-referencing relationship joining on the same keys. If none is found, it looks for a "hidden" inverse relationship that was manufactured by the Framework. If none is found, the Enterprise Objects Framework creates a "hidden" inverse relationship and returns that. Hidden relationships are used internally by the Framework.

__See Also:__ [inverseRelationship](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpkjswyylunfxw443infyc62loozsxe43fkjswyylunfxw443infya)

---

### __awakeWithPropertyList__

`public void awakeWithPropertyList(NSDictionary pList)`

Description forthcoming.

---

### beautifyName

`public void beautifyName()`

Makes the relationship's name conform to a standard convention. Names that conform to this style are all lower-case except for the initial letter of each embedded word other than the first, which is upper case. Thus, "NAME" becomes "name", and "FIRST_NAME" becomes "firstName". This method is used in reverse-engineering a model.

__See Also:__ [setName](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpkjswyylunfxw443infyc643forhgc3lf), beautifyNames (EOModel)

---

### componentRelationships

`public NSArray componentRelationships()`

Returns an array of base relationships making up a flattened relationship, or `null` if the relationship isn't flattened.

__See Also:__ [definition](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpkjswyylunfxw443infyc6zdfmzuw42lunfxw4)

---

### definition

`public String definition()`

Returns the data path of a flattened relationship; for example "department.facility". If the relationship isn't flattened, __definition__ returns `null`.

__See Also:__ [componentRelationships](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpkjswyylunfxw443infyc6y3pnvyg63tfnz2fezlmmf2gs33oonugs4dt)

---

### deleteRule

`public int deleteRule()`

Returns a rule that describes the action to take when an object is being deleted. The returned rule is one of the following integers (defined in the control layer's EOClassDescription class):

|  |  |
| --- | --- |
| __Value__ | __Description__ |
| `EOClassDescription. DeleteRuleNullify` | Delete the department and remove any back reference the employee has to the department. |
| `EOClassDescription. DeleteRuleCascade` | Delete the department and all of the employees it contains. |
| `EOClassDescription. DeleteRuleDeny` | Refuse the deletion if the department contains employees. |
| `EOClassDescription. DeleteRuleNoAction` | Delete the department, but ignore the department's employees relationship. You should use this delete rule with caution since it can leave dangling references in your object graph. |

---

### destinationAttributes

`public NSArray destinationAttributes()`

Returns the destination attributes of the relationship. These correspond one-to-one with the attributes returned by [sourceAttributes](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpkjswyylunfxw443infyc643povzggzkbor2he2lcov2gk4y). Returns `null` if the relationship is flattened.

__See Also:__ [joins](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpkjswyylunfxw443infyc62tpnfxhg), destinationAttribute (EOJoin)

---

### destinationEntity

`public EOEntity destinationEntity()`

Returns the relationship's destination entity, which is determined by the destination entity of its joins for a simple relationship, and by whatever ends the data path for a flattened relationship. For example, if a flattened relationship's definition is "department.facility", the destination entity is the Facility entity.

__See Also:__ [entity](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpkjswyylunfxw443infyc6zlooruxi6i)

---

### __encodeIntoPropertyList__

`public void encodeIntoPropertyList(NSMutableDictionary pList)`

Description forthcoming.

---

### entity

`public EOEntity entity()`

Returns the relationship's source entity.

__See Also:__ [destinationEntity](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_5/EOAccessRef/Java/Classes/EORelationship.html#//apple_ref/java/instm/EORelationship/destinationEntity), addRelationship (EOEntity)

---

### inverseRelationship

`public EORelationship inverseRelationship()`

Searches the relationship's destination entity for a user-created, back-referencing relationship joining on the same keys. Returns the inverse relationship if one is found, `null` otherwise.

__See Also:__ [anyInverseRelationship](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpkjswyylunfxw443infyc6ylopfew45tfojzwkutfnrqxi2lpnzzwq2lq)

---

### isCompound

`public boolean isCompound()`

Returns `true` if the relationship contains more than one join (that is, if it joins more than one pair of attributes), `false` if it has only one join. See "Creating a Simple Relationship" (page 281) for information on compound relationships.

__See Also:__ [joins](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpkjswyylunfxw443infyc62tpnfxhg), [joinSemantic](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpkjswyylunfxw443infyc62tpnfxfgzlnmfxhi2ld)

---

### isFlattened

`public boolean isFlattened()`

Returns `true` if the relationship traverses more than two entities, `false` otherwise. See "Creating a Flattened Relationship" (page 283) for an example of a flattened relationship.

---

### isMandatory

`public boolean isMandatory()`

Returns `true` if the target of the relationship is required, `false` if it can be `null`.

__See Also:__ [setIsMandatory](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpkjswyylunfxw443infyc643forexgtlbnzsgc5dpoj4q)

---

### isToMany

`public boolean isToMany()`

Returns `true` if the relationship is to-many, `false` if it's to-one.

__See Also:__ [setToMany](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpkjswyylunfxw443infyc643forkg6tlbnz4q)

---

### joinSemantic

`public int joinSemantic()`

Returns the semantic used to create SQL expressions for this relationship. The returned join semantic is one of the following:

|  |  |
| --- | --- |
| __Constant__ | __Description__ |
| `InnerJoin` | Produces results only for destinations of the join relationship that have non-NULL values. |
| `FullOuterJoin` | Produces results for all source records, regardless of the values of the relationships. |
| `LeftOuterJoin` | Preserves rows in the left (source) table, keeping them even if there's no corresponding row in the right table. |
| `RightOuterJoin` | Preserves rows in the right (destination) table, keeping them even if there's no corresponding row in the left table. |

__See Also:__ [joins](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpkjswyylunfxw443infyc62tpnfxhg)

---

### joins

`public NSArray joins()`

Returns all joins used by relationship.

__See Also:__ [destinationAttributes](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpkjswyylunfxw443infyc6zdfon2gs3tboruw63sbor2he2lcov2gk4y), [joinSemantic](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpkjswyylunfxw443infyc62tpnfxfgzlnmfxhi2ld), [sourceAttributes](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpkjswyylunfxw443infyc643povzggzkbor2he2lcov2gk4y)

---

### name

`public String name()`

Returns the relationship's name.

---

### numberOfToManyFaultsToBatchFetch

`public int numberOfToManyFaultsToBatchFetch()`

Returns the number of to-many faults that are triggered at one time.

---

### ownsDestination

`public boolean ownsDestination()`

Returns `true` if the receiver's source object owns its destination objects, `false` otherwise. See the method description for [setOwnsDestination](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpkjswyylunfxw443infyc643forhxo3ttirsxg5djnzqxi2lpny) for more discussion of this topic.

__See Also:__ [destinationAttributes](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpkjswyylunfxw443infyc6zdfon2gs3tboruw63sbor2he2lcov2gk4y)

---

### propagatesPrimaryKey

`public boolean propagatesPrimaryKey()`

Returns `true` if objects should propagate their primary key to related objects through this relationship. Objects only propagate their primary key values if the corresponding values in the destination object aren't already set.

---

### qualifierWithSourceRow

`public com.webobjects.eocontrol.EOQualifier qualifierWithSourceRow( NSDictionary sourceRow)`

Returns a qualifier that can be used to fetch the destination of the receiving relationship, given _sourceRow_.

---

### referencesProperty

`public boolean referencesProperty(Object aProperty)`

Returns `true` if _aProperty_ is in the relationship's data path or is an attribute belonging to one of the relationship's joins; otherwise, it returns `false`. See the class description for information on how relationships reference properties.

__See Also:__ [referencesProperty](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpkjswyylunfxw443infyc64tfmzsxezlomnsxgudsn5ygk4tupe) (EOEntity)

---

### __relationshipPath__

`public String relationshipPath()`

Description forthcoming.

---

### removeJoin

`public void removeJoin(EOJoin aJoin)`

Deletes _aJoin_ from the relationship. Does nothing if the relationship is flattened.

__See Also:__ [addJoin](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpkjswyylunfxw443infyc6ylemrfg62lo)

---

### setDefinition

`public void setDefinition(String definition)`

Changes the relationship to a flattened relationship by releasing any joins and attributes (both source and destination) associated with the relationship and setting _definition_ as its data path. "department.facility" is an example of a definition that could be supplied to this method.

If the relationship's entity hasn't been set, this method won't work correctly. See "Creating a Flattened Relationship" (page 283) for more information on flattened relationships.

__See Also:__ [addJoin](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpkjswyylunfxw443infyc6ylemrfg62lo), [setEntity](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpkjswyylunfxw443infyc643forcw45djor4q)

---

### setDeleteRule

`public void setDeleteRule(int deleteRule)`

Set a rule describing the action to take when object is being deleted. _deleteRule_ can be one of the following (defined in the control layer's EOClassDescription):

- `EOClassDescription.DeleteRuleNullify`
- `EOClassDescription.DeleteRuleCascade`
- `EOClassDescription.DeleteRuleDeny`
- `EOClassDescription.DeleteRuleNoAction`

For more discussion of what these rules mean, see the method description for [deleteRule](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpkjswyylunfxw443infyc6zdfnrsxizksovwgk).

---

### setEntity

`public void setEntity(EOEntity anEntity)`

Sets the entity of the relationship to _anEntity_. If the relationship is currently owned by a different entity, this method will remove the relationship from that entity. This method doesn't add the relationship to the new entity. EOEntity's addRelationship method invokes this method.

You only need to use this method when creating a flattened relationship; use EOEntity's __addRelationship__ to associate an existing relationship with an entity.

__See Also:__ [setDefinition](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpkjswyylunfxw443infyc643forcgkztjnzuxi2lpny)

---

### setIsMandatory

`public void setIsMandatory(boolean flag)`

Specifies according to _flag_ whether the target of the relationship must be supplied or can be `null`.

---

### setJoinSemantic

`public void setJoinSemantic(int joinSemantic)`

Sets the semantic used to create SQL expressions for this relationship. _joinSemantic_ should be one of the following:

- [InnerJoin](#apple-ineeuskii5cuc)
- [FullOuterJoin](#apple-ineeurkfiraue)
- [LeftOuterJoin](#apple-ineeusckivbus)
- [RightOuterJoin](#apple-ineeuskjifdee)

__See Also:__ [addJoin](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpkjswyylunfxw443infyc6ylemrfg62lo), [joinSemantic](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpkjswyylunfxw443infyc62tpnfxfgzlnmfxhi2ld)

---

### setName

`public void setName(String name)`

Sets the relationship's name to _name_. Throws a verification exception if _name_ is not a valid relationship name, and an invalid argument exception if _name_ is already in use by an attribute or another relationship in the same entity.

This method forces all objects in the model to be loaded into memory.

__See Also:__ [beautifyName](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpkjswyylunfxw443infyc6ytfmf2xi2lgpfhgc3lf)

---

### setNumberOfToManyFaultsToBatchFetch

`public void setNumberOfToManyFaultsToBatchFetch(int size)`

Sets the number of "toMany" faults that are fired at one time to _size_.

__See Also:__ [isToMany](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpkjswyylunfxw443infyc62ltkrxu2ylope), [numberOfToManyFaultsToBatchFetch](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpkjswyylunfxw443infyc63tvnvrgk4spmzkg6tlbnz4umylvnr2hgvdpijqxiy3iizsxiy3i)

---

### setOwnsDestination

`public void setOwnsDestination(boolean flag)`

Sets according to _flag_ whether a receiver's source object owns its destination objects. The default is `false`. When a source object owns its destination objects, it means that the destination objects can't exist independently. For example, in a personnel database, dependents can't exist without having an associated employee. Removing a dependent from an employee's __dependents__ array would have the effect of also deleting the dependent from the database, unless you transferred the dependent to a different employee.

__See Also:__ [deleteRule](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpkjswyylunfxw443infyc6zdfnrsxizksovwgk), [setDeleteRule](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpkjswyylunfxw443infyc643forcgk3dforsve5lmmu), [ownsDestination](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpkjswyylunfxw443infyc633xnzzuizltoruw4ylunfxw4)

---

### setPropagatesPrimaryKey

`public void setPropagatesPrimaryKey(boolean flag)`

Specifies according to _flag_ whether objects should propagate their primary key to related objects through this relationship. For example, an Employee object might propagate its primary key to an EmployeePhoto object. Objects only propagate their primary key values if the corresponding values in the destination object aren't already set.

---

### setToMany

`public void setToMany(boolean flag)`

Sets a simple relationship as to-many according to _flag_. Throws an exception if the receiver is flattened. See the class description for considerations in setting this flag.

__See Also:__ [isFlattened](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpkjswyylunfxw443infyc62ltizwgc5dumvxgkza)

---

### setUserInfo

`public void setUserInfo(NSDictionary dictionary)`

Sets the _dictionary_ of auxiliary data, which your application can use for whatever it needs. _dictionary_ can only contain property list data types (that is, NSDictionary, String, NSArray, and NSData).

---

### sourceAttributes

`public NSArray sourceAttributes()`

Returns the source attributes of a simple (non-flattened) relationship. These correspond one-to-one with the attributes returned by [destinationAttributes](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpkjswyylunfxw443infyc6zdfon2gs3tboruw63sbor2he2lcov2gk4y). Returns `null` if the relationship is flattened.

__See Also:__ [joins](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpkjswyylunfxw443infyc62tpnfxhg), sourceAttribute (EOJoin)

---

### __toString__

`public String toString()`

Returns a String representation of the receiver.

---

### userInfo

`public NSDictionary userInfo()`

Returns a dictionary of user data. Your application can use this data for whatever it needs.

---

### validateValue

`public Object validateValue(Object value) throws NSValidation.ValidationException`

For relationships marked as mandatory, throws a validation exception if the receiver is to-one and _value_ is `null`, or if the receiver is to-many an _value_ has a count of 0. A mandatory relationship is one in which the target of the relationship is required. Returns `null` to indicate success.

__See Also:__ [isMandatory](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpkjswyylunfxw443infyc62ltjvqw4zdborxxe6i), [setIsMandatory](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpkjswyylunfxw443infyc643forexgtlbnzsgc5dpoj4q)

---

### valueForSQLExpression

`public String valueForSQLExpression(EOSQLExpression context)`

Conformance to EOSQLExpression.SQLValue

---

© 2001 Apple Computer, Inc. (Last Published April 13, 2001)

[![Table of Contents](attachments/EOAccessRef/Java/Art/up.gif)](../EOAccessTOC.md)

Copyright © 2016 Apple Inc. All rights reserved.

- [Terms of Use](http://www.apple.com/legal/internet-services/terms/site.html)
- [Privacy Policy](http://www.apple.com/privacy/)
