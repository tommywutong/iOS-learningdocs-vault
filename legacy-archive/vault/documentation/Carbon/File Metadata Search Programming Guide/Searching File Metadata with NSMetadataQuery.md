---
title: File Metadata Search Programming Guide
apple_id: TP40001841
resource_type: Guide
platform: iOS|macOS
topic: Data Management
technology: CoreServices
published: '2011-09-28'
source_url: https://developer.apple.com/library/archive/documentation/Carbon/Conceptual/SpotlightQuery/Concepts/QueryingMetadata.html
archived_at: '2026-07-15T05:24:41.708258Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [File Metadata Search Programming Guide](About%20File%20Metadata%20Queries.md)


[Next](File%20Metadata%20Query%20Expression%20Syntax.md)[Previous](Searching%20iCloud%20and%20the%20Desktop.md)

# Searching File Metadata with NSMetadataQuery

In order for your application to search Spotlight metadata, you must create a query using the NSMetadataQuery class provided by the Foundation framework. Queries can be run in two modes: asynchronous, and asynchronous with live updates. The first simply performs the search on the files that exist at the time of the initial search. The latter continues to search. updating the data as the files that fulfill or no longer fulfill the search parameters update.

There are four main steps for executing an asynchronous metadata query:

- Defining and initializing the search.
- Initiating the search.
- Listen for batch notifications.
- Listening for the completion notification.
- Stopping the query.
- Processing results.

A live asynchronous Spotlight query allows your application to monitor the specified scope for changes that happen ‘on the fly’. The only significant difference in the code is that rather than stopping the query, you simply suspend the query while processing the results, and then resume the search when processing is completed.

A static Spotlight search is a search that simply runs, returns the results and quits. it is intended as a one-time search that does not monitor changes (which is possible using live searches, discussed in Creating a Live Search.

The first step in creating a query is defining a search expression that returns the desired results. If you are using `MDMetadataQuery` to execute the query, create your search expression predicate using the syntax described in [File Metadata Query Expression Syntax](File%20Metadata%20Query%20Expression%20Syntax.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytqnbzfvbuuqsfjjbeqsa). You must register a notification to inform you as data batches are returned and when the initial search is complete. You can also optionally register the scope, sorting, and a delegate.

![bullet](../../../_unindexed/Resources/1282/Images/task_2x.png)To define a search

1. Create an [NSMetadataQuery](https://developer.apple.com/documentation/foundation/nsmetadataquery) instance.
2. Register to receive the [NSMetadataQueryDidUpdateNotification](https://developer.apple.com/documentation/foundation/nsnotification/name/1413406-nsmetadataquerydidupdate) notification which is sent when batches of search content is returned.

   This notification may not be generated depending on the batch value.
3. Register to receive the [NSMetadataQueryDidFinishGatheringNotification](https://developer.apple.com/documentation/foundation/nsnotification/name/1414740-nsmetadataquerydidfinishgatherin) notification which is sent when the initial search is completed.

The search predicate is created using the syntax specified in [File Metadata Query Expression Syntax](File%20Metadata%20Query%20Expression%20Syntax.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytqnbzfvbuuqsfjjbeqsa). The fields that can be searched are defined in the _[File Metadata Attributes Reference](../../File%20Metadata%20Attributes%20Reference/About%20the%20File%20Metadata%20Attributes%20Reference.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytmobz)_. The attributes references lists the available metadata keys and the type of data that you must supply to search that attribute (a string, number, an array of strings, a date, or a Uniform Type Identifier.

![bullet](../../../_unindexed/Resources/1282/Images/task_2x.png)To create the query

- Create an `NSPredicate` instance with the appropriate Spotlight query expression.

If you are using `NSMetadataQuery`, you can specify the sort order of the results by providing an array of sort descriptors. The sorting is based on the metadata attribute key of each returned `NSMetadataItem` object.

![bullet](../../../_unindexed/Resources/1282/Images/task_2x.png)To set the search order

- Create an NSSortDescriptor with the desired metadata key for sorting, in this case `kMDItemDisplayName`.

An application limits where search results are collected from by specifying a search scope. The search scope is provided to the query as an array of predefined location constants, URLs, and directory paths. The predefined location constants provide convenient values for restricting a query to the user's home directory, locally mounted volumes and the user's home directory, or remote mounted volumes.

The search scopes specify where the metadata query searches for the files. Table 2-1 lists the available scopes.

__Table 2-1__  Supported Search Scopes

| Scope Constant | Supported Operating Systems | Description |
| [NSMetadataQueryUbiquitousDocumentsScope](https://developer.apple.com/documentation/foundation/nsmetadataqueryubiquitousdocumentsscope) | iOS and OS X | Search all files in the Documents directories of the application’s iCloud container directories. |
| [NSMetadataQueryUbiquitousDataScope](https://developer.apple.com/documentation/foundation/nsmetadataqueryubiquitousdatascope) | iOS and OS X | Search all files not in the Documents directories of the application’s iCloud container directories. |
| [NSMetadataQueryNetworkScope](https://developer.apple.com/documentation/foundation/nsmetadataquerynetworkscope) | OS X | Search all user-mounted remote volumes. |
| [NSMetadataQueryLocalComputerScope](https://developer.apple.com/documentation/foundation/nsmetadataquerylocalcomputerscope) | OS X | Search all local mounted volumes, including the user home directory. The user’s home directory is searched even if it is a remote volume. |
| [NSMetadataQueryUserHomeScope](https://developer.apple.com/documentation/foundation/nsmetadataqueryuserhomescope) | OS X | Search the user’s home directory. |

The search scopes are specified as an array of the scope constants.

![bullet](../../../_unindexed/Resources/1282/Images/task_2x.png)To specify the search scope

- Send your instance of `NSMetadataSearch` a [setSearchScopes:](https://developer.apple.com/documentation/foundation/nsmetadataquery/1412155-searchscopes) message, passing an array of the appropriate scopes.

  This query will search the User’s directory on the computer as well as the iCloud Documents folder. This same search code could be run on iOS by simply removing the unsupported [NSMetadataQueryUserHomeScope](https://developer.apple.com/documentation/foundation/nsmetadataqueryuserhomescope) scope constant.

Once you have created and configured a query object, you can execute the query itself. When running, a query typically has two phases: an initial results gathering phase and a live-update phase.

During the initial results gathering phase, the existing Spotlight system store is searched for files that match the search expression. The query sends notifications as the results are returned in batches using the [NSMetadataQueryDidUpdateNotification](https://developer.apple.com/documentation/foundation/nsnotification/name/1413406-nsmetadataquerydidupdate). In a single query this can be useful for indicating the state of the search progress, while in live searches it becomes more important.

The query sends the application a [NSMetadataQueryDidFinishGatheringNotification](https://developer.apple.com/documentation/foundation/nsnotification/name/1414740-nsmetadataquerydidfinishgatherin) notification when the initial results gathering phase has completed.

To run the search, send a [startQuery](https://developer.apple.com/documentation/foundation/nsmetadataquery/1407304-startquery) message to your instance of `NSMetadataSearch`.

Before your application interacts with the returned results, it must first stop the query. You can disable updates during the initial gathering phase of a search or during the live-update phase.

An application determines the number of results that have been returned by invoking the `NSMetadataQuery` instance method [resultCount](https://developer.apple.com/documentation/foundation/nsmetadataquery/1418315-resultcount). The application then accesses individual result items by their indexed position. Rather than traversing the `results` (which is intended for use with Cocoa Bindings), it is better to request the result item at desired index using the [resultAtIndex:](https://developer.apple.com/documentation/foundation/nsmetadataquery/1410162-result) method.

The result items are returned as an object instance of type [NSMetadataItem](https://developer.apple.com/documentation/foundation/nsmetadataitem). Each object encapsulates the metadata attributes for the file. Your application then retrieves the metadata attributes from these items by passing each instance a [valueForAttribute:](https://developer.apple.com/documentation/foundation/nsmetadataitem/1411721-valueforattribute) message with the name of the desired metadata attribute.

![bullet](../../../_unindexed/Resources/1282/Images/task_2x.png)To access the results

1. Stop the query that is in progress.
2. Iterate over the results, performing whatever action is appropriate for your application.
3. Remove the observers for the notifications.

   This step is optional if you intend to run the query multiple times. However if you intend to use the same setup code, you may wish to remove the observers regardless.

Creating a Static File Metadata Search shows the code required to implement a static search.

__Listing 2-1__  Static Spotlight search implementation

```objc
// Initialize Search Method
- (void)initiateSearch
{
    // Create the metadata query instance. The metadataSearch @property is
    // declared as retain
    self.metadataSearch=[[[NSMetadataQuery alloc] init] autorelease];

    // Register the notifications for batch and completion updates
    [[NSNotificationCenter defaultCenter] addObserver:self
                                             selector:@selector(queryDidUpdate:)
                                                 name:NSMetadataQueryDidUpdateNotification
                                               object:metadataSearch];

    [[NSNotificationCenter defaultCenter] addObserver:self
                                             selector:@selector(initalGatherComplete:)
                                                 name:NSMetadataQueryDidFinishGatheringNotification
                                               object:metadataSearch];

    // Configure the search predicate to find all images using the
    // public.image UTI
    NSPredicate *searchPredicate;
    searchPredicate=[NSPredicate predicateWithFormat:@"kMDItemContentTypeTree == 'public.image'"];
    [metadataSearch setPredicate:searchPredicate];

    // Set the search scope. In this case it will search the User's home directory
    // and the iCloud documents area
    NSArray *searchScopes;
    searchScopes=[NSArray arrayWithObjects:NSMetadataQueryUserHomeScope,
                  NSMetadataQueryUbiquitousDocumentsScope,nil];
    [metadataSearch setSearchScopes:searchScopes];

    // Configure the sorting of the results so it will order the results by the
    // display name
    NSSortDescriptor *sortKeys=[[[NSSortDescriptor alloc] initWithKey:(id)kMDItemDisplayName
                                                            ascending:YES] autorelease];
    [metadataSearch setSortDescriptors:[NSArray arrayWithObject:sortKeys]];

    // Begin the asynchronous query
    [metadataSearch startQuery];

}

// Method invoked when notifications of content batches have been received
- (void)queryDidUpdate:sender;
{
    NSLog(@"A data batch has been received");
}


// Method invoked when the initial query gathering is completed
- (void)initalGatherComplete:sender;
{
    // Stop the query, the single pass is completed.
    [metadataSearch stopQuery];

    // Process the content. In this case the application simply
    // iterates over the content, printing the display name key for
    // each image
    NSUInteger i=0;
    for (i=0; i < [metadataSearch resultCount]; i++) {
        NSMetadataItem *theResult = [metadataSearch resultAtIndex:i];
        NSString *displayName = [theResult valueForAttribute:(NSString *)kMDItemDisplayName];
        NSLog(@"result at %lu - %@",i,displayName);
    }

    // Remove the notifications to clean up after ourselves.
    // Also release the metadataQuery.
    // When the Query is removed the query results are also lost.
    [[NSNotificationCenter defaultCenter] removeObserver:self
                                                    name:NSMetadataQueryDidUpdateNotification
                                                  object:metadataSearch];
    [[NSNotificationCenter defaultCenter] removeObserver:self
                                                    name:NSMetadataQueryDidFinishGatheringNotification
                                                  object:metadataSearch];
    self.metadataSearch=nil;
}

@end
```


A live search is configured in a manner virtual to an identical search with only a small number of changes.

- The query must be suspended using [disableUpdates](https://developer.apple.com/documentation/foundation/nsmetadataquery/1416337-disableupdates) before accessing the updated data.
- Data is typically handled in the `queryDidUpdate:` method in some form.
- The query is then restarted using [enableUpdates](https://developer.apple.com/documentation/foundation/nsmetadataquery/1416943-enableupdates) to continue the search.

[Next](File%20Metadata%20Query%20Expression%20Syntax.md)[Previous](Searching%20iCloud%20and%20the%20Desktop.md)

