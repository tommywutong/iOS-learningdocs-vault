---
title: 'Your Third iOS App: iCloud'
apple_id: TP40011317
resource_type: Guide
platform: iOS
topic: General
technology: null
published: '2013-09-18'
source_url: https://developer.apple.com/library/archive/documentation/General/Conceptual/iCloud101/SearchingforiCloudDocuments/SearchingforiCloudDocuments.html
archived_at: '2026-07-15T07:34:35.932819Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Your Third iOS App: iCloud](About%20Your%20Third%20iOS%20App.md)


[Next](Troubleshooting.md)[Previous](Implementing%20the%20Detail%20View%20Controller.md)

# Searching for iCloud Documents

Documents created by an app on one device must be discoverable by the same app running on the user’s other devices. An app discovers documents in an iCloud container directory is by using a metadata query object, which is an instance of the [NSMetadataQuery](https://developer.apple.com/documentation/foundation/nsmetadataquery) class. A metadata query object searches the available iCloud container directories for files matching the criteria you specify.

Because documents can appear in a container directory (or disappear from the directory) at any time, it often makes sense to start a query and leave it running. In such a case, you should create the query object in some central part of your app and keep a reference to that object for the lifetime of your app.

The `STEMasterViewController` class creates a metadata query object early in the life of the app and starts it. This query returns an initial set of documents right away and sends later updates when changes occur.

Because the query runs constantly while the app is running, the `STEMasterViewController` class uses an instance variable to store a query object persistently.

![bullet](../../../_unindexed/Resources/1282/Images/task_2x.png)To declare the storage for the metadata query object

1. In the project navigator, select `STEMasterViewController.m`.
2. Add a private instance variable called `_query` to store the metadata query object.

   The type of the variable is a pointer to [NSMetadataQuery](https://developer.apple.com/documentation/foundation/nsmetadataquery). The top of your class implementation should now look like the following:

```objc
@implementation STEMasterViewController {
    NSMutableArray *documents;
    NSMetadataQuery *_query;
}
@synthesize addButton;
```

You initialize the `_query` instance variable during the app launch cycle.

![bullet](../../../_unindexed/Resources/1282/Images/task_2x.png)To configure and start the search query at initialization time

1. In the project navigator, select `STEMasterViewController.m`.
2. Define a new method called `textDocumentQuery` to create the query object.

   The implementation of this method creates a new `NSMetadataQuery` object and configures it to look only for text documents in the `Documents` directory of the app’s iCloud containers. The implementation of this method is as follows:

```objc
- (NSMetadataQuery*)textDocumentQuery {
    NSMetadataQuery* aQuery = [[NSMetadataQuery alloc] init];
    if (aQuery) {
        // Search the Documents subdirectory only.
        [aQuery setSearchScopes:[NSArray
                    arrayWithObject:NSMetadataQueryUbiquitousDocumentsScope]];

        // Add a predicate for finding the documents.
        NSString* filePattern = [NSString stringWithFormat:@"*.%@",
                    STEDocFilenameExtension];
        [aQuery setPredicate:[NSPredicate predicateWithFormat:@"%K LIKE %@",
                    NSMetadataItemFSNameKey, filePattern]];
    }

    return aQuery;
}
```
3. Define a new method called `setupAndStartQuery` to start the query.

   The `setupAndStartQuery` method retrieves the metadata query object, configures the notification handlers, and starts the query. The implementation of this method is as follows:

```objc
- (void)setupAndStartQuery {
   // Create the query object if it does not exist.
   if (!_query)
      _query = [self textDocumentQuery];

   // Register for the metadata query notifications.
   [[NSNotificationCenter defaultCenter] addObserver:self
        selector:@selector(processFiles:)
        name:NSMetadataQueryDidFinishGatheringNotification
        object:nil];
   [[NSNotificationCenter defaultCenter] addObserver:self
        selector:@selector(processFiles:)
        name:NSMetadataQueryDidUpdateNotification
        object:nil];

   // Start the query and let it run.
   [_query startQuery];
}
```
4. Add a forward declaration of the `setupAndStartQuery` method at the top of the file.
5. Update the [awakeFromNib](https://developer.apple.com/documentation/objectivec/nsobject/1402907-awakefromnib) method to call the `setupAndStartQuery` method.

   Your `awakeFromNib` method should now look similar to the following:

```objc
- (void)awakeFromNib {
   [super awakeFromNib];

   if (!documents)
      documents = [[NSMutableArray alloc] init];

   self.navigationItem.leftBarButtonItem = self.editButtonItem;
   [self setupAndStartQuery];
}
```


Search results are delivered in two phases: the initial gathering phase and the update phase. The initial gathering phase occurs immediately after you start a metadata query and is the first set of results to be returned. Thereafter, the query object sends update notifications only when the files in the directory change. For both the initial gathering phase and for updates, the metadata query results include all of the files currently found in the specified location.

The Simple Text Editor app uses the metadata query notifications to update its list of documents and refresh its user interface accordingly.

![bullet](../../../_unindexed/Resources/1282/Images/task_2x.png)To process the list of documents

1. In the project navigator, select `STEMasterViewController.m`.
2. Add the following implementation of the custom `processFiles:` method.

   This method builds a list of discovered files, filtering out files that should be hidden. When processing the results of a search query, disable updates temporarily while you process the list of files. This prevents the query results from changing while you are iterating through them.

```objc
- (void)processFiles:(NSNotification*)aNotification {
    NSMutableArray *discoveredFiles = [NSMutableArray array];

    // Always disable updates while processing results.
    [_query disableUpdates];

    // The query reports all files found, every time.
    NSArray *queryResults = [_query results];
    for (NSMetadataItem *result in queryResults) {
        NSURL *fileURL = [result valueForAttribute:NSMetadataItemURLKey];
        NSNumber *aBool = nil;

        // Don't include hidden files.
        [fileURL getResourceValue:&aBool forKey:NSURLIsHiddenKey error:nil];
        if (aBool && ![aBool boolValue])
            [discoveredFiles addObject:fileURL];
    }

    // Update the list of documents.
    [documents removeAllObjects];
    [documents addObjectsFromArray:discoveredFiles];
    [self.tableView reloadData];

    // Reenable query updates.
    [_query enableUpdates];
}
```


At this point, you should have everything you need to build and run the complete app. You should be able to create new documents in iCloud, open existing documents, and edit the contents of those documents. If you have multiple devices associated with the provisioning profile, you should also be able to plug in each device and see the files created on one show up on the other.

If the app does not behave as you expect, you can troubleshoot the problem using the information in [Troubleshooting](Troubleshooting.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgeytgmjxfvbuqnrnknltc).

Now that you have completed the implementation of searching, you have completed your third iOS app. Congratulations!

Take a moment to think about how iCloud impacted your overall app architecture. Most of the work needed to support iCloud is in the data portion of your app. And when you use a [UIDocument](https://developer.apple.com/documentation/uikit/uidocument) object to manage your files, the amount of work you have to do is actually small.

[Next](Troubleshooting.md)[Previous](Implementing%20the%20Detail%20View%20Controller.md)

