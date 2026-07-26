---
title: 'Testing Core Data with very big hierarchical data sets | Cocoa with Love'
source: Cocoa with Love (Matt Gallagher)
source_key: cocoawithlove
source_url: 'https://www.cocoawithlove.com/2008/03/testing-core-data-with-very-big.html'
original_language: en
published: ''
status: frozen
license: All rights reserved（页脚明示）→ 严格私有
archived_at: 2026-07-27
content_hash: 'sha256:2603c1f0ae981e2a'
translated: false
---

> 原文：[Testing Core Data with very big hierarchical data sets | Cocoa with Love](https://www.cocoawithlove.com/2008/03/testing-core-data-with-very-big.html)　·　Cocoa with Love (Matt Gallagher)

I test Core Data's performance with a one million object data set stored in a basic three-tiered hierarchy. I look at the performance when building, loading, fetching and traversing.

## The test data

My test data will be a three-tier hierarchy. This arrangement reflects data where containment of one set in another is important. It also creates a situation where graph traversal, searching and containment testing can be performed in more than one way, with no approach being obviously better — leading to a desire for performance testing.

![](https://www.cocoawithlove.com/assets/objc-era/coredatasetentities.png)

The following tests will all use the same data:

- one top-tier object
- one thousand mid-tier objects, each connected to the top-tier object
- one million bottom-tier objects, with one thousand connected to each mid-tier object

Each bottom-tier object will have a name with the following format: "Object x, y, z" where "x", "y" and "z" are the index of the top, mid and bottom tiers to which is it connected. This is so that every name is unique and for debugging, I can check that I get the object that I expect.

## Building the test document

The following are the times taken to create and save to disk the above described data. Each improvement shown incorporates the previous improvements.

| Create method | Time taken | Peak memory |
|---|---|---|
| Create all objects and save at once | 368.236 seconds | 798 MB |
| As above but invoking setUndoManager:nil on the context first | 342.618 seconds | 778 MB |
| Wrap the contents of the outer loop in an NSAutoreleasePool init/release and NSManagedObjectContext save | 262.511 seconds | 254 MB |
| Invoke NSManagedObjectContext reset after each save | 258.904 seconds | 20.1 MB |

The different save approaches that I have speed tested are those given by Apple on their [Core Data Programming Guide: Efficiently Importing Data](http://developer.apple.com/documentation/Cocoa/Conceptual/CoreData/Articles/cdImporting.html) page.

Having never created a million object document in Core Data before, I didn't expect document creation to take this long. Taking 4-6 minutes to save a 77.1MB file really didn't seem right. Apple claim that Core Data can cope with terabyte databases; I dread the thought of ever creating one of those.

To determine how slow Core Data is, relative to direct SQLite data creation, I wrote a command line tool to talk to sqlite3 directly and write 1 million rows of data to the ZBOTTOMLEVEL table. This took 124 seconds, so Core Data is roughly doubling the time involved. This is probably reasonable, although it still _feels_ like its taking too long.

Despite my frustration with the length of time, the saving does appear to be highly linear. This table showed a 1 million row database saving in 250 seconds. For 10,000 objects I recorded 2.5 seconds and for 100,000 I recorded 25 seconds and 10 million rows took around 40 minutes (approximately 2,500 seconds).

Out of curiosity, I tried saving the 1 million line document as an XML file. This took 941 seconds, most of which was spent thrashing more than 3 GB of memory around on my computer (which has 2.25 GB of RAM and didn't appreciate the effort). I don't know what all the memory was doing, since the XML file was 227.8 MB and the objects before saving only took around 100 MB of RAM.

The last option (-[NSManagedObjectContext reset]) is particularly inconvenient in an application (since you must refetch every NSManagedObject from the context) but due to its effects on memory useage (12 times less memory than any other technique) it is the only option that would remain usable if you were creating and saving a 20 million row database in this way.

## Load the set of all Bottom-Tier object names

My first test will be to build a set of all names of children of Bottom-Tier objects under the Top-Tier objects. This type of action might be done if you are testing names for uniqueness within the hierarchy or if you simply want a list of all the names the hierarchy uses.

I will test by two approaches. First will be an NSFetchRequest with the following NSPredicate:

```objc
[NSPredicate predicateWithFormat:@"midLevel.topLevel == %@", topLevelObject];
```

and then building an NSSet of the "name" keys from each object in the returned array.

Second will be a keyPath fetch:

```objc
bottomLevelNames = [topLevelObject valueForKeyPath:
    @"midLevel.@distinctUnionOfSets.bottomLevel.name"];
```

| Fetch method | Time taken (first iteration) | Time taken (averaged over 4 subsequent iterations) |
|---|---|---|
| NSFetchRequest | 27.4 seconds | 15.3 seconds |
| keyPath access | 217.1 seconds | 6.4 seconds |
| keyPath access after prefetching (which took 13.9 seconds) | 18.5 seconds | 6.4 seconds |

Prefetching involved using an NSFetchRequest to return all BottomLevel objects in the database while using setRelationshipKeyPathsForPrefetching: with an array containing "midLevel" to further fetch the MidLevel objects.

Conclusions to draw from this data:

- NSFetchRequest is the fastest approach for a cold start
- Using keyPaths on non-prefetched data is extremely slow
- keyPaths are very fast once cached

I did also test iterating over all the objects in a "for (child in parentChildSet)" approach. This is really a manual form of the "keyPath" approach and unsurprisingly returned almost identical times.

## Find a Bottom-Tier object with a specific name

This test will search for the BottomLevel object in the hierarchy, with a specific "name" value.

I will perform this test in 4 different ways:

- As before, one search approach will use an NSFetchPredicate to perform the work, with no database field indexed.
- A second search will also use an NSFetchPredicate, this time with the "name" field on BottomLevel indexed.
- A third approach will compare this with the most naive approach: a manual traversal of the entire object graph looking for the BottomLevel object with the given "name".
- Finally, I will try to cache the lookup by generating mapping in the TopLevel object which maps from "name" values to the BottomLevel object with that value in the hierarchy and compare this cached lookup to the other approaches.

Both NSFetchRequest tests will use the following NSPredicate:

```objc
[NSPredicate predicateWithFormat:
    "midLevel.topLevel == %@ AND name == 'Object 5, 5, 0'", topLevelObject];
```

The manual traversal will traverse over all objects and test the name for equality with @"Object 5, 5, 0". Since manual traversal can exit as soon as it finds a match, I will base my timing on matches found after exactly 500,000 comparisons (which should offer an appropriate average).

The cached mapping of "name" values to BottomLevel objects will be a NSDictionary built as follows:

```objc
NSSet *bottomLevelSet = [topLevelObject
    valueForKeyPath:@"midLevel.@distinctUnionOfSets.bottomLevel"];
NSArray *bottomLevelArray = [bottomLevelSet allObjects];
NSArray *bottomLevelNames = [bottomLevelArray valueForKey:@"name"];
NSDictionary *bottomLevelKeyedByName =
    [NSDictionary
        dictionaryWithObjects:bottomLevelArray
        forKeys:bottomLevelNames];
```

| Fetch method | Time taken |
|---|---|
| NSFetchRequest (no indexing of 'name') | 670,000 microseconds |
| NSFetchRequest (with 'name' indexed) | 2,174 microseconds |
| keyPath traversal (average after prefetching) | 940,000 microseconds |
| NSDictionary (after setup of 12.6 seconds) | 24 microseconds |

The keyPath traversal only needs to traverse until it finds the value it wants. I deliberately searched for a non-existent value (forcing full traversal) and halved it to get this average value.

After I ran these tests, I tried an NSFetchRequest without the hierarchic constraint (using the predicate format string: @"name == 'Object 5, 5, 0'"). This approximately halved the time taken but showed that a JOIN is not as catastrophic as forgetting to index a search field.

Conclusions from this data:

- NSFetchRequest is predictably fast on this type of lookup.
- It is really important to index fields (using the checkbox in the XCode Data Model editor). Without this, SQLite manually searches every element and is almost as slow as a full traversal.
- Iterating over a million string comparisons is much faster than I expected but still not as fast as having an indexed lookup
- Nothing gets close to NSDictionary (once it is setup). It is 100 times faster than an SQL indexed lookup. This is unsurprising since it is a data structure designed specifically for this type of lookup.

## Final conclusions

Core Data is not a panacea for all data management ills. It does not make everything magically fast. Obviously, there are still areas where it can be slow (sometimes very slow) and there are data access approaches which must be avoided.

NSFetchRequest does what it should and does it quickly. Provided you index your search fields.

It seems like NSSQLStore could save a little faster. 4-6 minutes to save a 77.1 MB document doesn't seem right. However, it isn't an order of magnitude slower than bare SQLite and it's still faster than NSXMLStore or NSBinaryStore for anything bigger than trivial sizes.

Basic iteration over cached Core Data objects works surprisingly well given how much work is being done. Millions of keyPath accesses and millions of string comparisons happen within a second — not significantly slower than SQLite's optimised version of the same when searching without an index.
