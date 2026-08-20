---
title: iPod Library Access Programming Guide
apple_id: TP40008765
resource_type: Guide
platform: tvOS|iOS
topic: Audio, Video, & Visual Effects
technology: null
published: '2015-03-09'
source_url: https://developer.apple.com/library/archive/documentation/Audio/Conceptual/iPodLibraryAccess_Guide/UsingTheiPodLibrary/UsingTheiPodLibrary.html
archived_at: '2026-07-15T05:20:53.877178Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [iPod Library Access Programming Guide](Introduction.md)


[Next](Document%20Revision%20History.md)[Previous](Using%20the%20Media%20Item%20Picker.md)

# Using the iPod Library

Your application may need more control over managing and choosing media items than you get with the media item picker. If you want to provide a custom user interface to the device iPod library, perform specific queries, or associate custom metadata with media items, you need the database access classes of this API.

Figure 4-1 illustrates how your application and the database access classes interact to retrieve media items.

__Figure 4-1__  Using the iPod library database access classes

!

First, take a moment to notice the similarity between this figure and [Figure 1-5](About%20iPod%20Library%20Access.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4donrvfvbuqmjqgmwvgvzs). The earlier figure helped explain what a query is. This figure places the media query class among its cohorts, showing how all the database access classes relate to each other.

The figure illustrates two scenarios of interaction between your application and the device iPod library. First, moving counterclockwise from the “Your application” icon, the figure depicts the creation and configuration of a query that in turn defines a media item collection. The collection points to a particular subset of items from the library. Although not shown in the figure, the collection is the return value of invoking the query. Each media item owns a media item artwork object, as shown in the figure, among its other properties.

The second scenario in Figure 4-1 is your application receiving change notifications from the iPod library by way of the [MPMediaLibrary](https://developer.apple.com/documentation/mediaplayer/mpmedialibrary) class. By registering to receive these change notifications, your application can update any cache of library content if a user syncs their device while your application is running.

Retrieving media items from the device iPod library begins with constructing a media query. The simplest query is the generic “`everything`” query shown in Listing 4-1, which matches the entire contents of the library. The example then logs the titles of the media items to the Xcode debugger console, demonstrating use of the `items` property to invoke the query and retrieve the media items it matches.

__Listing 4-1__  Creating and using a generic media query

```
MPMediaQuery *everything = [[MPMediaQuery alloc] init];

NSLog(@"Logging items from a generic query...");
NSArray *itemsFromGenericQuery = [everything items];
for (MPMediaItem *song in itemsFromGenericQuery) {
    NSString *songTitle = [song valueForProperty: MPMediaItemPropertyTitle];
    NSLog (@"%@", songTitle);
}
```

To construct a more specific query, apply one or more media property predicates to a generic query. A predicate specifies a single logical condition to test media items against.

Listing 4-2 creates a predicate containing the condition that a media item’s “artist” property must have a particular value. The listing then adds the predicate to a query.

__Listing 4-2__  Constructing and applying a media property predicate

```
MPMediaPropertyPredicate *artistNamePredicate =
    [MPMediaPropertyPredicate predicateWithValue: @"Happy the Clown"
                                     forProperty: MPMediaItemPropertyArtist];

MPMediaQuery *myArtistQuery = [[MPMediaQuery alloc] init];
[myArtistQuery addFilterPredicate: artistNamePredicate];

NSArray *itemsFromArtistQuery = [myArtistQuery items];
```

If you were to run this code, the `itemsFromArtistQuery` array would contain only those items from the iPod library that are by Happy the Clown.

You can construct and add multiple predicates to a query to narrow what the query matches. Listing 4-3 shows this technique using two predicates.

__Listing 4-3__  Applying multiple predicates to an existing media query

```
MPMediaPropertyPredicate *artistNamePredicate =
    [MPMediaPropertyPredicate predicateWithValue: @"Sad the Joker"
                                     forProperty: MPMediaItemPropertyArtist];

MPMediaPropertyPredicate *albumNamePredicate =
    [MPMediaPropertyPredicate predicateWithValue: @"Stair Tumbling"
                                     forProperty: MPMediaItemPropertyAlbumTitle];

MPMediaQuery *myComplexQuery = [[MPMediaQuery alloc] init];

[myComplexQuery addFilterPredicate: artistNamePredicate];
[myComplexQuery addFilterPredicate: albumNamePredicate];
```

You construct each predicate using a value of your choice (such as an artist’s name) along with the appropriate media item property key. These keys are described in _[MPMediaItem Class Reference](https://developer.apple.com/documentation/mediaplayer/mpmediaitem)_ in `General Media Item Property Keys` and `Podcast Item Property Keys`.

When you apply more than one predicate to a query, the query combines them using the logical AND operator.

You can also add predicates to a query upon initialization, as shown in Listing 4-4. (The two predicates in this example are assumed to be previously defined.)

__Listing 4-4__  Applying multiple predicates when initializing a media query

```
NSSet *predicates =
    [NSSet setWithObjects: artistNamePredicate, albumNamePredicate, nil];

MPMediaQuery *specificQuery =
    [[MPMediaQuery alloc] initWithFilterPredicates: predicates];
```

Listing 4-4 first defines an [NSSet](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSSetClassCluster/Description.html#//apple_ref/occ/cl/NSSet) object that contains two predicates, then allocates and initializes a media query using the [initWithFilterPredicates:](https://developer.apple.com/documentation/mediaplayer/mpmediaquery/1621771-initwithfilterpredicates) class method.

Only certain property keys can be used to build valid predicates. These keys are tagged as “filterable” in _[MPMediaItem Class Reference](https://developer.apple.com/documentation/mediaplayer/mpmediaitem)_. If you attempt to use a query that contains an invalid predicate, the resulting behavior is undefined.

Listing 4-5 shows how to use the `canFilterByProperty:` class method to validate a media item property key before using it in a predicate.

__Listing 4-5__  Testing if a property key can be used for a media property predicate

```
if ([MPMediaItem canFilterByProperty: MPMediaItemPropertyGenre]) {

    MPMediaPropertyPredicate *rockPredicate =
        [MPMediaPropertyPredicate predicateWithValue: @"Rock"
                                         forProperty: MPMediaItemPropertyGenre];

    [query addFilterPredicate: rockPredicate];
}
```

In Listing 4-5, only if the indicated media item property key (in this example, `MPMediaItemPropertyGenre`) can be used to construct a valid predicate will the body of the if statement execute. Apple recommends that you always perform a check like this before constructing a media property predicate.

A media query is useful not only for retrieving ungrouped media items. You can also use a media query to retrieve sorted and arranged _collections_ of media items. The arrangement you get depends on the value you set for the media query’s `grouping` property.

Listing 4-6 shows how to retrieve all the songs by a particular artist, with those songs arranged into albums. The example logs the results to the Xcode debugger console.

__Listing 4-6__  Using grouping type to specify media item collections

```
MPMediaQuery *query = [[MPMediaQuery alloc] init];

[query addFilterPredicate: [MPMediaPropertyPredicate
                               predicateWithValue: @"Moribund the Squirrel"
                                      forProperty: MPMediaItemPropertyArtist]];
// Sets the grouping type for the media query
[query setGroupingType: MPMediaGroupingAlbum];

NSArray *albums = [query collections];
for (MPMediaItemCollection *album in albums) {
    MPMediaItem *representativeItem = [album representativeItem];
    NSString *artistName =
        [representativeItem valueForProperty: MPMediaItemPropertyArtist];
    NSString *albumName =
        [representativeItem valueForProperty: MPMediaItemPropertyAlbumTitle];
    NSLog (@"%@ by %@", albumName, artistName);

    NSArray *songs = [album items];
    for (MPMediaItem *song in songs) {
        NSString *songTitle =
            [song valueForProperty: MPMediaItemPropertyTitle];
        NSLog (@"\t\t%@", songTitle);
    }
}
```

You can see in Listing 4-6 that the value of the media query’s `collections` property is an array of arrays. The outer for loop iterates over the albums performed the specified artist. The inner for loop iterates over the songs in the current album.

The [MPMediaQuery](https://developer.apple.com/documentation/mediaplayer/mpmediaquery) class includes several convenience constructors for creating queries that are preconfigured with a grouping type. The following statement, for example, attaches the “albums” grouping type to a newly-allocated query:

```
MPMediaQuery *query = [MPMediaQuery albumsQuery];
```

For descriptions of all the convenience constructors, see _[MPMediaQuery Class Reference](https://developer.apple.com/documentation/mediaplayer/mpmediaquery)_.

One of the most useful and high-impact properties of a media item is its artwork. To display artwork, you use Interface Builder as well as Xcode. The steps are as follows:

1. Add a [UIImageView](https://developer.apple.com/documentation/uikit/uiimageview) object to your view layout in Interface Builder.
2. Add an IBOutlet instance variable to your view controller class to connect to the `UIImageView` object.
3. Retrieve the artwork from the media item that owns it (having previously retrieved the media item as described in this chapter).
4. Convert the artwork to a [UIImage](https://developer.apple.com/documentation/uikit/uiimage) object, then assign it to your layout’s `UIImageView` object.

Listing 4-7 shows how to do steps 3 and 4.

__Listing 4-7__  Displaying album artwork for a media item

```
MPMediaItemArtwork *artwork =
    [mediaItem valueForProperty: MPMediaItemPropertyArtwork];
UIImage *artworkImage =
    [artwork imageWithSize: albumImageView.bounds.size];

if (artworkImage) {
    albumImageView.image = artworkImage;
} else {
    albumImageView.image = [UIImage imageNamed: @"noArtwork.png"];
}
```

The `noArtwork.png` file used in the last line of Listing 4-7 is a fallback image that you add to your Xcode project, for use when a media item has no associated artwork.

[Next](Document%20Revision%20History.md)[Previous](Using%20the%20Media%20Item%20Picker.md)

