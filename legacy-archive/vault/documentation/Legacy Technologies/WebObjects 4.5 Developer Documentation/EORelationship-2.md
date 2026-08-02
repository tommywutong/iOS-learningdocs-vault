---
title: WebObjects 4.5 Developer Documentation
apple_id: TP40006775
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.5/System/Library/Frameworks/EOAccess.framework/Java/Classes/More/EORelationship.html
archived_at: '2026-07-15T08:11:33.099756Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 4.5 Developer Documentation](webobjects.md)


__PATH__
[WebObjects 4.5 Documentation](webobjects.md) __>__
EOAdaptor Reference

[![Table of Contents](attachments/images/up.gif)](../../EOAccessTOC.md)

# EORelationship

## Creating a Simple Relationship

A simple relationship is defined by the attributes it compares
in connecting its source and destination entities. Each source-destination
pair of attributes is encapsulated in an EOJoin object. For example,
to create a relationship from the Movie entity to the Studio entity,
a join has to be created from the __studioId__ attribute
of the Movie entity to the same attribute of the Studio entity.
The values of these two attributes must be equal for a match to
result. Note that __studioId__ is the primary
key attribute for the Studio entity, so there can only be one studio
per movie; this relationship is therefore to-one.

This code excerpt creates an EORelationship for the relationship
described above and adds it to the EOEntity for the Movie entity:

> ```
> EOEntity movieEntity;       // Assume this exists.
> EOEntity studioEntity;      // Assume this exists.
> EOAttribute studioIDAttribute;
> EOAttribute movieStudioIDAttribute;
> EOJoin toStudioJoin;
> EORelationship toStudioRelationship;
>
> studioIDAttribute = studioEntity.attributeNamed("studioId");
> movieStudioIDAttribute = movieEntity.attributeNamed("studioId");
>
> toStudioJoin = new EOJoin(movieStudioIDAttribute, studioIDAttribute);
>
> toStudioRelationship = new EORelationship();
> toStudioRelationship.setName("studio");
> movieEntity.addRelationship(toStudioRelationship);
> toStudioRelationship.addJoin(toStudioJoin);
> toStudioRelationship.setToMany(false);
> toStudioRelationship.setJoinSemantic(EORelationship.InnerJoin);
> ```

This code first gets the attributes from the source and destination
entities, and then creates an EOJoin with them. Next, a new EORelationship
is created, its name is set, and it's added to __movieEntity__.
The EOJoin is added to the relationship and the relationship is
set to be to-one. Finally, in the __setJoinSemantic__ line, [InnerJoin](EORelationship.md#apple-ineeuskii5cuc) indicates that only objects
that actually have a matching destination object will be included
in the result when the relationship is traversed.

Creating a to-many relationship in the opposite direction
merely swaps the source and destination attributes, and assigns
the relationship to the EOEntity for the Studio entity:

> ```
> EOJoin toMoviesJoin;
> EORelationship toMoviesRelationship;
>
> toMoviesJoin = new EOJoin(studioIDAttribute, movieStudioIDAttribute);
> toMoviesRelationship = new EORelationship();
>
> toMoviesRelationship.setName("movies");
> studioEntity.addRelationship(toMoviesRelationship);
> toMoviesRelationship.addJoin(toMoviesJoin);
> toMoviesRelationship.setToMany(true);
> toMoviesRelationship.setJoinSemantic(EORelationship.InnerJoin);
> ```

Note that this relationship is to-many precisely because the
destination attribute isn't the primary key for its entity (Movie),
and therefore isn't unique with regard to that entity.

A relationship isn't restricted to only one EOJoin. It's
entirely possible for a relationship to be defined based on two
or more attributes in the source and destination entities. For example,
consider an employees database that contains a picture of each employee
identified by first and last name. You'd define the relationship
by joining each of the first and last names in the Employee entity
to the same attribute in the __EmpPhoto__ attribute.

A simple relationship is considered to reference all of the
attributes in its joins. You can use the [referencesProperty](EORelationship.md#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpkjswyylunfxw443infyc64tfmzsxezlomnsxgudsn5ygk4tupe) method
to find out if an EORelationship references a particular attribute.

## Creating a Flattened Relationship

A flattened relationship depends on several simple relationships
already existing. Assuming that several do exist, creating a flattened
relationship is straightforward. For example, suppose that the Movie
entity has a to-many relationship to the Director entity, called __toDirectors__.
The Director entity in turn has a relationship to the Talent entity
called __toTalent__. In the Movies database,
the Director table acts as an intermediate table between Movie and
Talent. In this situation, it make sense to flatten the relationship
Movies has to Director (__toDirectors__) to
give Movie access to the Talent table through Director's __toTalent__ relationship.
For more discussion of when to use flattened relationships, see
the chapters "Designing Enterprise Objects" and "Advanced
Enterprise Object Modeling" in the _Enterprise Objects
Framework Developer's Guide_.

This code excerpt creates a flattened relationship from Movie
to Talent:

> ```
> EOEntity movieEntity;   // Assume this exists.
> EORelationship toDirectorsRelationship = new EORelationship();
>
> toDirectorsRelationship.setName("directors");
> toDirectorsRelationship.setEntity(movieEntity);
> movieEntity.addRelationship(toDirectorsRelationship);
> toDirectorsRelationship.setDefinition:("toDirector.toTalent");
> ```

All that's needed to establish the relationship is a data
path (also called the definition) naming each component relationship
connected, with the names separated by periods. Note that because
the cardinality of a flattened relationship is determinable from
its components, no [setToMany](EORelationship.md#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpkjswyylunfxw443infyc643forkg6tlbnz4q) message is required here.

A simple relationship is considered to reference all of the
relationships in its definition, plus every attribute referenced
by the component relationships. You can use the [referencesProperty](EORelationship.md#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpkjswyylunfxw443infyc64tfmzsxezlomnsxgudsn5ygk4tupe) method
to find out if an EORelationship references another relationship
or attribute.

:

[![Table of Contents](attachments/images/up.gif)](../../EOAccessTOC.md)
