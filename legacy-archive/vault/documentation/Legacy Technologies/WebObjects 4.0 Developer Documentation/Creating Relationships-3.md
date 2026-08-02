---
title: WebObjects 4.0 Developer Documentation
apple_id: TP40006774
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.0/System/Library/Frameworks/EOAccess.framework/Resources/English.lproj/Documentation/Reference/ObjC_classic/Classes/More/CreatingRelationships.html
archived_at: '2026-07-18T01:28:17.896699Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 4.0 Developer Documentation](webobjects.md)


__PATH__
[WebObjects 4.0 Documentation](webobjects.md) __>__
[EOAccess Reference](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.0/System/Library/Frameworks/EOAccess.framework/Resources/English.lproj/Documentation/Reference/ObjC_classic/frameset.html)

[!](EORelationship-2.md)
[!](EOSQLExpression-3.md)

---

# Creating Relationships

---

## Creating a Simple Relationship

A simple relationship is defined by the attributes it compares in connecting its source and destination entities. Each source-destination pair of attributes is encapsulated in an EOJoin object. For example, to create a relationship from the Movie entity to the Studio entity, a join has to be created from the `studioId` attribute of the Movie entity to the same attribute of the Studio entity. The values of these two attributes must be equal for a match to result. Note that `studioId` is the primary key attribute for the Studio entity, so there can only be one studio per movie; this relationship is therefore to-one.

This code excerpt creates an EORelationship for the relationship described above and adds it to the EOEntity for the Movie entity:

> ```
> EOEntity *movieEntity;       // Assume this exists.  EOEntity *studioEntity;      // Assume this exists.EOAttribute *studioIDAttribute;EOAttribute *movieStudioIDAttribute;EOJoin *toStudioJoin;EORelationship *toStudioRelationship;studioIDAttribute = [studioEntity attributeNamed:@"studioId"];movieStudioIDAttribute = [movieEntity attributeNamed:@"studioId"];toStudioJoin = [[[EOJoin alloc]    initWithSourceAttribute:movieStudioIDAttribute    destinationAttribute:studioIDAttribute] autorelease];toStudioRelationship = [[[EORelationship alloc] init] autorelease];[toStudioRelationship setName:@"studio"];[movieEntity addRelationship:toStudioRelationship];[toStudioRelationship addJoin:toStudioJoin];[toStudioRelationship setToMany:NO];[toStudioRelationship setJoinSemantic:EOInnerJoin];
> ```

This code first gets the attributes from the source and destination entities, and then creates an EOJoin with them. Next, a new EORelationship is created, its name is set, and it's added to `movieEntity`. The EOJoin is added to the relationship and the relationship is set to be to-one. Finally, in the `setJoinSemantic:` line, [EOInnerJoin](EORelationship-2.md#apple-gu2dk) indicates that only objects that actually have a matching destination object will be included in the result when the relationship is traversed.

Creating a to-many relationship in the opposite direction merely swaps the source and destination attributes, and assigns the relationship to the EOEntity for the Studio entity:

> ```
> EOJoin *toMoviesJoin;EORelationship *toMoviesRelationship;toMoviesJoin = [[[EOJoin alloc]    initWithSourceAttribute:studioIDAttribute    destinationAttribute:movieStudioIDAttribute] autorelease];toMoviesRelationship = [[[EORelationship alloc] init] autorelease];[toMoviesRelationship setName:@"movies"];[studioEntity addRelationship:toMoviesRelationship];[toMoviesRelationship addJoin:toMoviesJoin];[toMoviesRelationship setToMany:YES];[toMoviesRelationship setJoinSemantic:EOInnerJoin];
> ```

Note that this relationship is to-many precisely because the destination attribute isn't the primary key for its entity (Movie), and therefore isn't unique with regard to that entity.

A relationship isn't restricted to only one EOJoin. It's entirely possible for a relationship to be defined based on two or more attributes in the source and destination entities. For example, consider an employees database that contains a picture of each employee identified by first and last name. You'd define the relationship by joining each of the first and last names in the Employee entity to the same attribute in the `EmpPhoto` attribute.

A simple relationship is considered to reference all of the attributes in its joins. You can use the [`referencesProperty:`](../EORelationship.md#apple-gqztq) method to find out if an EORelationship references a particular attribute.

---

## Creating a Flattened Relationship

A flattened relationship depends on several simple relationships already existing. Assuming that several do exist, creating a flattened relationship is straightforward. For example, suppose that the Movie entity has a to-many relationship to the Director entity, called `toDirectors`. The Director entity in turn has a relationship to the Talent entity called `toTalent`. In the Movies database, the Director table acts as an intermediate table between Movie and Talent. In this situation, it make sense to flatten the relationship Movies has to Director (`toDirectors`) to give Movie access to the Talent table through Director's `toTalent` relationship. For more discussion of when to use flattened relationships, see the chapters "Designing Enterprise Objects" and "Advanced Enterprise Object Modeling" in the _Enterprise Objects Framework Developer's Guide_.

This code excerpt creates a flattened relationship from Movie to Talent:

> ```
> EOEntity *movieEntity;   // Assume this exists.EORelationship *toDirectorsRelationship;toDirectorsRelationship = [[[EORelationship alloc] init] autorelease];[toDirectorsRelationship setName:@"directors"];[toDirectorsRelationship setEntity:movieEntity];[movieEntity addRelationship:toDirectorsRelationship];[toDirectorsRelationship setDefinition:@"toDirector.toTalent"];
> ```

All that's needed to establish the relationship is a data path (also called the definition) naming each component relationship connected, with the names separated by periods. Note that because the cardinality of a flattened relationship is determinable from its components, no [`setToMany:`](../EORelationship.md#apple-gyzde) message is required here.

A simple relationship is considered to reference all of the relationships in its definition, plus every attribute referenced by the component relationships. You can use the [`referencesProperty:`](../EORelationship.md#apple-gqztq) method to find out if an EORelationship references another relationship or attribute.

****

---

[!](EORelationship-2.md)
[!](EOSQLExpression-3.md)

---

_Copyright © 1998, Apple Computer, Inc. All rights
reserved._
