---
title: WebObjects 4.5 Developer Documentation
apple_id: TP40006775
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.5/System/Documentation/Developer/WebObjects/Topics/ProgrammingTopics.16.html
archived_at: '2026-07-15T08:09:56.020723Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 4.5 Developer Documentation](webobjects.md)


__PATH__
[Documentation](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/index.html) __>__ [WebObjects 4.5](webobjects.md) __>__
Programming Topics

[!](WebObjects%20Programming%20Topics.md) [!](Creating%20a%20WODisplayGroup.md) [!](Batching%20the%20Output%20of%20a%20WODisplayGroup.md)

#   Using Master-Peer Configurations

##  Synopsis

Explains what a master-peer EODatabaseDataSource configuration is, how it differs from a master-detail configuration, when to use it, and how to use it.

##  Discussion

EODatabaseDataSources are usually used in a master-detail configuration where an EODatabaseDataSource acts as the master and an EODetailDataSource acts as the detail. However, you can also use two EODatabaseDataSources in a master-peer configuration where one acts as the master and the other acts as the detail (see Figure 1).

!

Master-Peer Configuration

!

The peer EODatabaseDataSource in a master-peer configuration operates independently of its master. It goes to the database to fetch its objects and maintains those objects in its own array. Because the peer data source acts independently, if you add or remove objects from the peer, the changes aren't automatically reflected in the master. The database is updated correctly, but the master's relationship array (if it exists) isn't. Consequently, if you're using master-peer and the master has a to-many relationship as a class property, you're responsible for modifying the master's relationship array to keep it in sync with the peer.

###  When to Use Master-Peer

You might want to use a master-peer configuration instead of a master-detail if the master doesn't have a class property that represents a relationship to the peer. With master-detail, the master must have a class property that represents a relationship to the detail, but because a peer does its own fetching, the master in a master-peer doesn't have this restriction.

Another scenario in which you might want to use a master-peer configuration is when you need to further qualify the set of objects related to the master's selected object. For example, instead of displaying all of a studio's movies, you want to display only the movies whose revenues are greater than $5,000,000. You can accomplish this by assigning an in-memory qualifier to a display group displaying the detail objects, but if the number of records in the unfiltered set is prohibitively large, the filtering is better performed in the database. Using a master-peer configuration, you can further qualify the peer's set of objects in the database by assigning an auxiliary qualifier. You must also use this auxiliary qualifier approach if the qualifier can't be executed in memory (for example, because it uses custom SQL or accesses properties not in the object graph). For an example of applying an auxiliary qualifier, see [Creating a Master-Peer Configuration](#apple-gezdgmjw)
.

###   Creating a Master-Peer Configuration

To set up a master-peer configuration, follow these basic steps:

1. 

   Create the master display group and EODatabaseDataSource.
2. 

   Create the peer display group and EODatabaseDataSource.
3. 

   Connect the display groups.
4. 

   Optionally, apply an auxiliary qualifier to the peer's data source.

For an OpenStep application, the easiest way to create a display group and its data source is to drag a model file (or an entity from EOModeler) into a nib in Interface Builder. This action creates an EODisplayGroup and a corresponding EODatabaseDataSource. Using this approach, you can then connect your two display groups as you would for a master-detail configuration, but create an EOMasterPeerAssociation instead of an EOMasterDetailAssociation.

For a WebObjects application, start out similarly by dragging a model file (or an entity from EOModeler) into a component in WebObjects Builder to create a WODisplayGroup and a corresponding EODatabaseDataSource. Do this twice, once to create a master display group and again to create the peer. Don't configure your peer display group to have a detail data source as you would for a master-detail configuration. Instead, you must establish the master-peer relationship in code, using the EODataSource method
qualifyWithRelationshipKey
. The following method demonstrates the procedure:

####  Establishing a master-peer relationship (Java)

```

public void selectObject() {  WODisplayGroup studioDisplayGroup;  // Assume this exists.  WODisplayGroup movieDisplayGroup;   // Assume this exists.   Studio studio;                      // Assume this exists.  EODatabaseDataSource movieDataSource;  movieDataSource = (EODatabaseDataSource)movieDisplayGroup.dataSource();  studioDisplayGroup.selectObject(studio);  movieDataSource.qualifyWithRelationshipKeyAndObject("toMovie", studio);  movieDisplayGroup.fetch();}
```

####  Establishing a master-peer relationship (Objective-C)

```objc

- (void)selectObject {WODisplayGroup *studioDisplayGroup; // Assume this exists.WODisplayGroup *movieDisplayGroup;  // Assume this exists. Studio *studio;                     // Assume this exists.EODatabaseDataSource *movieDataSource =(EODatabaseDataSource *)[movieDisplayGroup dataSource];[studioDisplayGroup selectObject:studio];[movieDataSource qualifyWithRelationshipKey:@"toMovie" ofObject:studio];[movieDisplayGroup fetch];}
```


In this example, the
selectObject
method is invoked when a user selects a new master object (
studio
). It updates the selection of the master display group (
studioDisplayGroup
) and requalifies the peer data source (
movieDataSource
) to match. The final step is to send a fetch message to the peer display group (
movieDisplayGroup
) causing
movieDataSource
to refetch its objects from the database using a newly formed qualifier.

For both OpenStep and WebObjects applications, to apply an auxiliary qualifier, use EODatabaseDataSource's
setAuxiliaryQualifier
method. The following example demonstrates the procedure:

####  Applying an auxiliary qualifier (Java)

```

public Component requalifyMovies() {	  DecimalNumber revenue;              // Assume this exists.  WODisplayGroup movieDisplayGroup;   // Assume this exists.  EOQualifier auxiliaryQualifier;  EODatabaseDataSource movieDataSource;  /* Construct qualifier */  Object qualifierObjects[] = { "revenue",revenue };  NSArray qualifierComponentArray = new NSArray(qualifierObjects);  auxiliaryQualifier = EOQualifier.qualifierWithQualifierFormat(    "%@ > %@",qualifierComponentArray);  /* Apply qualifier to peer data source. */  movieDataSource = (EODatabaseDataSource)movieDisplayGroup.dataSource();  movieDataSource.setAuxiliaryQualifier(auxiliaryQualifier);  /* Tell peer controller to fetch. */  movieDisplayGroup.fetch();  return this;}
```

####  Applying an auxiliary qualifier (Objective-C)

```objc

- (void)requalifyMovies {NSDecimalNumber *revenue;          // Assume this exists.id movieDisplayGroup;              // Assume this exists.EOQualifier *auxiliaryQualifier = nil;EODatabaseDataSource *movieDataSource;/* Construct qualifier. */	auxiliaryQualifier = [EOQualifier  qualifierWithQualifierFormat:@"%@ > %@", @"revenue", revenue];/* Apply qualifier to peer data source. */movieDataSource = (EODatabaseDataSource *)[movieDisplayGroup dataSource];[movieDataSource setAuxiliaryQualifier:auxiliaryQualifier];/* Tell peer controller to fetch. */[movieDisplayGroup fetch];}
```


This method constructs a qualifier that selects movies whose revenues are greater than revenue, assigns that qualifier as the auxiliary qualifier for the peer data source (
movieDataSource
), and then directs the peer display group to fetch. Because the peer display group uses an EODatabaseDataSource instead of an EODetailDataSource, the refetch performs a fetch with the qualifier in the database.

##  See Also

- 

  [Creating a WODisplayGroup](Creating%20a%20WODisplayGroup.md#apple-gi3tanbu)
- 

  WODisplayGroup
- 

  EODisplayGroup
- 

  EODatabaseDataSource
- 

  EODataSource
- 

  EODetailDataSource

##  Questions

- 

  What is a master-peer configuration?
- 

  When do I use a master-peer configuration?
- 

  How do I use a master-peer configuration?

##  Keywords

- 

  Master-peer
- 

  Master-detail
- 

  WODisplayGroup
- 

  EODisplayGroup

##  Revision History

3 February, 1999. Clif Liu. First Draft.

---

© 1999 Apple Computer, Inc.

[!](WebObjects%20Programming%20Topics.md) [!](Creating%20a%20WODisplayGroup.md) [!](Batching%20the%20Output%20of%20a%20WODisplayGroup.md)

Copyright © 2016 Apple Inc. All rights reserved.

- [Terms of Use](http://www.apple.com/legal/internet-services/terms/site.html)
- [Privacy Policy](http://www.apple.com/privacy/)
