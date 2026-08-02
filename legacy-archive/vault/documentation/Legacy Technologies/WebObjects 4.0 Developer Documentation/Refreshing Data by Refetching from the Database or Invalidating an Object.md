---
title: WebObjects 4.0 Developer Documentation
apple_id: TP40006774
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.0/System/Documentation/Developer/WebObjects/Topics/RefreshingData.html
archived_at: '2026-07-15T08:01:28.954298Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 4.0 Developer Documentation](webobjects.md)


__PATH__
[WebObjects 4.0 Documentation](webobjects.md) __>__
[WebObjects Programming Topics](WebObjects%20Programming%20Topics.md)

# Refreshing Data by Refetching from the Database or Invalidating an Object

##  Synopsis

Describes how to get the most current values for an object by either refreshing during a fetch or invalidating an object.

##  Discussion

Enterprise Objects Framework (EOF) automatically caches the raw dictionary of values and unique objects that are fetched from the database. The raw dictionary is cached in a set of snapshots based on a GlobalID derived from the primary keys of the database rows. All peer EOEditingContexts share this common cache of snapshots. Each EOEditingContext stores its own unique object instance for a given GlobalID. Whenever the common snapshots change, an EOObjectsChangedInStore notification is posted and all associated EOEditingContexts attempt to reconcile themselves with the new snapshot.

When an EOEditingContext fetches a row, it creates one unique object within the EditingContext based on the GlobalID. This "uniquing" process enables EOF to return the same object during a future fetch. Uniquing is an important part of EOF, because having multiple instances of the same object in the same editing context is not desirable.

When a peer editing context such as another session's _defaultEditingContext_
fires a fault to a GlobalID that has already been fetched, the last fetched data (in the snapshot cache) is used as the source instead of a real database fetch. A new object is then instantiated and uniqued in this peer editing context.

The default behavior for fetching and uniquing an object involves comparing a newly fetched row's primary keys to the previously fetched snapshot. If a snapshot already exists with the same primary keys, EOF will completely ignore the fetched row and just use the previous snapshot.

This appears to be undesirable since the new fetch might have updated data. However, if the default was to always update the objects to the latest fetched data, your objects might be updated at unknown and invalid times.

The following are two ways that an instantiated object can be refreshed with the latest database values:

· The object (row) is returned from a new fetch that specifically requests refreshing.

· The editing context for the object is asked to invalidate the object, which releases the snapshot for this object and turns all instances back to a faults.

!Warning Refreshing an object will not refresh its relationships. Only its data and flattened
attributes will be refreshed.!

####  Refreshing Data with a FetchSpecification

EOFetchSpecification's _setRefreshesRefetchedObjects_
method can be used to override the default behavior and force an update to the snapshot and, consequently, an update to all previously fetched objects.

The following code shows how to set up an EOFetchSpecification to refresh the objects it fetches.

#####  Figure 1. Java Code

```
EOEditingContext ec=session().defaultEditingContext();
```



```
EOFetchSpecification fs=new EOFetchSpecification
```



```
    ("Movie", qual, null);
```



```
fs.setRefreshesRefetchedObjects(true);
```



```
movies=ec.objectsWithFetchSpecification(fs);
```


#####  Figure 2. Objective-C Code

```
EOEditingContext *ec=[[self session] defaultEditingContext];
```



```
EOFetchSpecification *fs=[EOFetchSpecification
```



```
    fetchSpecificationWithEntityName: @"Movie"
```



```
    qualifier:nil sortOrderings: nil];
```



```
[fs setRefreshesRefetchedObjects:YES];
```



```
movies =[ec objectsWithFetchSpecification: fs];
```


####  Refreshing Data by Invalidating the Object

EOF can be forced to invalidate an object, which removes the object's snapshot from the cache and converts the object back into a fault. As soon as a message is sent to the fault, the most recent data will be refetched from the database and the fault will be converted back into the appropriate object with the data. See the programming topic "Invalidating Objects" for a discussion on how to invalidate objects.

##  See Also

· Invalidating Objects

· EOEditingContext

· EOFetchSpecification

##  Questions

· How do I force a fetch and update my existing objects?

· Why does my object still have old values even after a refetch?

· How can I force an object to update its values?

##  Keywords

· Refetch

· Invalidate

· Update Record

· Snapshot

##  Revision History

23 July, 1998. David Scheck. First Draft.

19 November, 1998. Clif Liu. Second Draft.

Copyright © 2016 Apple Inc. All rights reserved.

- [Terms of Use](http://www.apple.com/legal/internet-services/terms/site.html)
- [Privacy Policy](http://www.apple.com/privacy/)
