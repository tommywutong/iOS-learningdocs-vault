---
title: Document-Based App Programming Guide for iOS
apple_id: TP40011149
resource_type: Guide
platform: tvOS|iOS
topic: Data Management
technology: UIKit
published: '2012-09-19'
source_url: https://developer.apple.com/library/archive/documentation/DataManagement/Conceptual/DocumentBasedAppPGiOS/ManageDocumentLifeCycle/ManageDocumentLifeCycle.html
archived_at: '2026-07-15T07:24:00.024447Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Document-Based App Programming Guide for iOS](About%20Document-Based%20Applications%20in%20iOS.md)


[Next](Change%20Tracking%20and%20Undo%20Operations.md)[Previous](Creating%20a%20Custom%20Document%20Object.md)

# Managing the Life Cycle of a Document

A document goes through a typical life cycle. A document-based application is responsible for managing its progress through that cycle. As you can see from the following list, most of these life-cycle events are initiated by the user:

- The user first creates a document.
- The user opens an existing document and the application displays it in the document’s view or views.
- The user edits the document.
- A user may ask to put a document in iCloud storage or may request the removal of a document from iCloud storage.
- During editing, saving, or other actions, errors or conflicts can happen; the application should learn about these errors and conflicts and either attempt to handle them or inform the user.
- The user closes a selected document.
- The user deletes an existing document.

The following sections discuss the procedures a document-based application must complete for these life-cycle operations.

_All_ documents of an application are stored either in the local sandbox or in an iCloud container directory. A user should not be able to select individual documents for storage in iCloud.

When an application launches for the first time on a device, it should do the following:

- If iCloud is not configured, tell users that they need to configure iCloud if they want to save files there.
- If iCloud is configured but not enabled for the application, ask users if they want to enable iCloud—in other words, ask if they want all of their documents saved to iCloud. Store the response as a user preference.

Based on this preference, an application writes document files either to the local application sandbox or the iCloud container directory. (For details, see [Moving Documents to and from iCloud Storage](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgeytcnbzfvbuqnbnknltk).) An application should expose a switch in the Settings application that enables users to move documents between local storage and iCloud storage.

A document object (that is, an instance of your custom [UIDocument](https://developer.apple.com/documentation/uikit/uidocument) subclass) must have a file URL that locates the document file either in the local application sandbox or in an iCloud container directory, whichever is the user’s preference. In addition, a new document can be given a name. The following discusses guidelines and procedures related to file URLs, document names, and the creation of new documents.

The `UIDocument` class assumes a correspondence between the filename of a document and the document name (also known the display name). By default, `UIDocument` stores the filename as the value of the [localizedName](https://developer.apple.com/documentation/uikit/uidocument/1619959-localizedname) property. However, an application should not require a user to provide the document filename or display name when he or she creates a new document.

For your application, you should devise some convention for automatically generating the filenames for your new documents. Some suggestions are:

- Generate a UUID (universally unique identifier) for each document, optionally with an application-specific prefix.
- Generate a timestamp (date and time) for each document, optionally with an application-specific prefix.
- Use a sequential numbering system, for example: “Notes 1”, “Notes 2”, and so on.

For the document (display) name, you might initially use the document filename if that makes sense (such as with “Notes 1”). Or, if the document contains text and the user enters some text in the document, you might use the first line (or some part of the first line) as the display name. Your application can give users some way to customize the document name after the document has been created.

You cannot create a document object without a valid file URL. The file URL has three parts of interest: the path to the `Documents` directory in the user’s preferred document location, the document filename, and the extension of the document file. You can get a URL representing the path to the `Documents` directory in the local application sandbox through a method such as the one in Document Filename Versus Document Name.

__Listing 4-1__  Getting a URL to the application’s `Documents` directory in the local sandbox

```objc
-(NSURL*)localDocumentsDirectoryURL {
    static NSURL *localDocumentsDirectoryURL = nil;
    if (localDocumentsDirectoryURL == nil) {
        NSString *documentsDirectoryPath = [NSSearchPathForDirectoriesInDomains( NSDocumentDirectory,
            NSUserDomainMask, YES ) objectAtIndex:0];
        localDocumentsDirectoryURL = [NSURL fileURLWithPath:documentsDirectoryPath];
    }
    return localDocumentsDirectoryURL;
}
```

The file extension must be one that you specified for the document type (see [Creating and Configuring the Project](Document-Based%20Application%20Preflight.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgeytcnbzfvbuqmznknlte)). You can declare a global string to represent the extension. For example:

```
static NSString *FileExtension = @"imageNotes";
```

The final part of a document’s file URL is the filename component. As [Document Filename Versus Document Name](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgeytcnbzfvbuqnbnknlto) explains, the application should initially generate the document filename according to some convention that makes sense for the application. This generated filename can be used as the document name, or the first line (or part thereof) can be used as the document name. The application can give the user the option of customizing the document name after the document object has been created.

After you concatenate the base URL, the document filename, and the file extension, you can allocate an instance of your custom `UIDocument` subclass and initialize it with the [initWithFileURL:](https://developer.apple.com/documentation/uikit/uidocument/1619979-initwithfileurl) method, passing in the constructed file URL. The final step in creating a new document is to save it to the preferred document storage location (even though there is no content at this point). As illustrated by Setting the Preferred Storage Location for Document Files , you do this by calling the [saveToURL:forSaveOperation:completionHandler:](https://developer.apple.com/documentation/uikit/uidocument/1619988-save) method on the document object.

__Listing 4-2__  Saving a new document to the file system

```objc
-(void)viewWillAppear:(BOOL)animated {
    [super viewWillAppear:animated];
    if (_createFile) {
        [self.document saveToURL:self.document.fileURL
            forSaveOperation:UIDocumentSaveForCreating completionHandler:^(BOOL success) {
            if (success)
                _textView.text = self.document.text;
        }];
        _createFile = NO;
    }
    // .....
}
```

The save-operation parameter of the method call should be [UIDocumentSaveForCreating](https://developer.apple.com/documentation/uikit/uidocumentsaveoperation/uidocumentsaveforcreating). The final parameter of the call is a completion hander: a block that is invoked after the save operation concludes. The parameter of the block tells you whether the operation succeeded. If it did succeed, this code assigns the document text to the `text` property of the text view displaying the document content.

Opening a document might at first glance seem to be a fairly easy procedure. Your application scans the contents of its `Documents` directory for files having the document’s extension and presents those documents to the user for selection. However, when iCloud storage is factored in, things get a bit more complicated. Your application’s documents could be in the `Documents` directory of the application sandbox _or_ they could be in the `Documents` directory of the iCloud container directory.

To obtain a list of an application’s documents in iCloud storage, run a metadata query. A query is an instance of the [NSMetadataQuery](https://developer.apple.com/documentation/foundation/nsmetadataquery) class. After creating a `NSMetadataQuery` object, you give it a scope and a predicate. For iCloud storage, the scope should be [NSMetadataQueryUbiquitousDocumentsScope](https://developer.apple.com/documentation/foundation/nsmetadataqueryubiquitousdocumentsscope). A predicate is an [NSPredicate](https://developer.apple.com/documentation/foundation/nspredicate) object that, in this case, constrains a search by filename extension. Before you start running the query, register to observe the [NSMetadataQueryDidFinishGatheringNotification](https://developer.apple.com/documentation/foundation/nsnotification/name/1414740-nsmetadataquerydidfinishgatherin) and [NSMetadataQueryDidUpdateNotification](https://developer.apple.com/documentation/foundation/nsnotification/name/1413406-nsmetadataquerydidupdate) notifications. The method accepting delivery of these notifications processes the results of the query.

Listing 4-3 illustrates how you set up and run a metadata query to get the list of application documents in the iCloud mobile container. The method first tests the user’s preferred storage location for documents (the `documentsInCloud` property). If that location is the mobile container, it runs a metadata query. If the location is the application sandbox, it iterates through the contents of the application’s `Documents` directory to get the names and locations of all local document files.

__Listing 4-3__  Getting the locations of documents stored locally and in iCloud storage

```objc
-(void)viewDidLoad {
    [super viewDidLoad];
    // set up Add and Edit navigation items here....

   if (self.documentsInCloud) {
        _query = [[NSMetadataQuery alloc] init];
        [_query setSearchScopes:[NSArray arrayWithObjects:NSMetadataQueryUbiquitousDocumentsScope, nil]];
        [_query setPredicate:[NSPredicate predicateWithFormat:@"%K LIKE '*.txt'", NSMetadataItemFSNameKey]];
        NSNotificationCenter* notificationCenter = [NSNotificationCenter defaultCenter];
        [notificationCenter addObserver:self selector:@selector(fileListReceived)
            name:NSMetadataQueryDidFinishGatheringNotification object:nil];
        [notificationCenter addObserver:self selector:@selector(fileListReceived)
            name:NSMetadataQueryDidUpdateNotification object:nil];
        [_query startQuery];
    } else {
        NSArray* localDocuments = [[NSFileManager defaultManager] contentsOfDirectoryAtPath:
            [self.documentsDir path] error:nil];
        for (NSString* document in localDocuments) {
            [_fileList addObject:[[[FileRepresentation alloc] initWithFileName:[document lastPathComponent]
                url:[NSURL fileURLWithPath:[[self.documentsDir path]
                stringByAppendingPathComponent:document]]] autorelease]];
        }
    }
}
```

In this example, the predicate format is `@"%K LIKE '*.txt’"`, which means to return all filenames (the [NSMetadataItemFSNameKey](https://developer.apple.com/documentation/foundation/nsmetadataitemfsnamekey) key) that have a extension of `txt`, the file extension of this application’s document files.

After the initial query concludes, and again if there are subsequent updates, the notification method specified in Listing 4-3 (`fileListReceived`) is invoked again. Listing 4-4 shows this method’s implementation. If query updates arrive after the user has made a selection, the code also tracks the current selection.

__Listing 4-4__  Collecting information about documents in iCloud storage

```objc
-(void)fileListReceived {

 NSString* selectedFileName=nil;
    NSInteger newSelectionRow = [self.tableView indexPathForSelectedRow].row;
    if (newSelectionRow != NSNotFound) {
        selectedFileName = [[_fileList objectAtIndex:newSelectionRow] fileName];
    }
    [_fileList removeAllObjects];
    NSArray* queryResults = [_query results];
    for (NSMetadataItem* result in queryResults) {
        NSString* fileName = [result valueForAttribute:NSMetadataItemFSNameKey];
        if (selectedFileName && [selectedFileName isEqualToString:fileName]) {
            newSelectionRow = [_fileList count];
        }
        [_fileList addObject:[[[FileRepresentation alloc] initWithFileName:fileName
            url:[result valueForAttribute:NSMetadataItemURLKey]] autorelease]];
    }
    [self.tableView reloadData];
    if (newSelectionRow != NSNotFound) {
        NSIndexPath* selectionPath = [NSIndexPath indexPathForRow:newSelectionRow inSection:0];
        [self.tableView selectRowAtIndexPath:selectionPath animated:NO scrollPosition:UITableViewScrollPositionNone];
    }
}
```

The example application now has an array (`_fileList`) of custom model objects that encapsulate the name and file URL of each of the application’s documents. (`FileRepresentation` is the custom class of those objects.) The root view controller populates a plain table view with the document names

When you run a metadata query to learn about an application’s iCloud documents, the query results are placeholder items ([NSMetadataItem](https://developer.apple.com/documentation/foundation/nsmetadataitem) objects) for document files. The items contain metadata about the file, such as its URL and its modification date. The document file is not in the iCloud container directory.

The actual data for a document is not downloaded until one of the following happens:

- Your application attempts to open or access the file, such as by calling [openWithCompletionHandler:](https://developer.apple.com/documentation/uikit/uidocument/1619977-open).
- Your application calls the `NSFileManager` method [startDownloadingUbiquitousItemAtURL:error:](https://developer.apple.com/documentation/foundation/nsfilemanager/1410377-startdownloadingubiquitousitemat) to download the data explicitly.

Because downloading large document files from iCloud might result in a perceptible delay in displaying the document data, you should indicate to the user that the download has begun (for example, show “loading” or “updating”) and that the file is not currently accessible. Remove this indication when the download has completed.

The sample document-based application lists known documents in a table view. When the user taps a listed document to open it, [UITableView](https://developer.apple.com/documentation/uikit/uitableview) invokes the [tableView:didSelectRowAtIndexPath:](https://developer.apple.com/documentation/uikit/uitableviewdelegate/1614877-tableview) method of its delegate. The implementation of this method, shown in Listing 4-5, is typical for the navigation pattern: The root view controller allocates the next view controller in the sequence—in this case, the view controller presenting document data—and initializes with essential data—in this case, the document’s file URL. Based on whether the device idiom is iPad or iPhone (or iPhone touch), the root view controller adds the view controller to the split view or pushes it on the navigation controller’s stack.

__Listing 4-5__  Responding to a request to open a document

```objc
-(void)tableView:(UITableView *)tableView didSelectRowAtIndexPath:(NSIndexPath *)indexPath
{
    [self selectFileAtIndexPath:indexPath create:NO];
}

-(void)selectFileAtIndexPath:(NSIndexPath*)indexPath create:(BOOL)create
{
    NSArray* fileList = indexPath.section == 0 ? _localFileList : _ubiquitousFileList;
    DetailViewController* detailViewController = [[DetailViewController alloc]
        initWithFileURL:[[fileList objectAtIndex:indexPath.row] url] createNewFile:create];

    if ([[UIDevice currentDevice] userInterfaceIdiom] == UIUserInterfaceIdiomPad) {
        self.splitViewController.viewControllers =
            [NSArray arrayWithObjects:self.navigationController, detailViewController, nil];
    }
    else {
        [self.navigationController pushViewController:detailViewController animated:YES];
    }
    [detailViewController release];
}
```

In its initializer method (not shown), the document’s view controller (`DetailViewController` in the example) allocates an instance of the `UIDocument` subclass and initializes it by calling the [initWithFileURL:](https://developer.apple.com/documentation/uikit/uidocument/1619979-initwithfileurl) method, passing in the file URL. It assigns the newly created document object to a `document` property.

The final step in opening a document is to call the [openWithCompletionHandler:](https://developer.apple.com/documentation/uikit/uidocument/1619977-open) method on the `UIDocument` object; the document’s view controller in our sample application calls this method in [viewWillAppear:](https://developer.apple.com/documentation/uikit/uiviewcontroller/1621510-viewwillappear), as shown in Listing 4-6. The code checks the document state to verify that the document is closed before attempting to open it—there’s no need to open an already opened document.

__Listing 4-6__  Opening a document

```objc
-(void)viewWillAppear:(BOOL)animated {
    [super viewWillAppear:animated];
    if (_createFile) {
        [self.document saveToURL:self.document.fileURL forSaveOperation:UIDocumentSaveForCreating
            completionHandler:^(BOOL success) {
                _textView.text = self.document.text;
        }];
        _createFile = NO;
    }
    else {
        if (self.document.documentState & UIDocumentStateClosed) {
            [self.document openWithCompletionHandler:nil];
        }
    }
}
```

When [openWithCompletionHandler:](https://developer.apple.com/documentation/uikit/uidocument/1619977-open) is called, `UIDocument` reads data from the document file, and the document object itself creates its model objects from the data. At the conclusion of this sequence of actions, the completion handler of the `openWithCompletionHandler:` method is executed. Although the view controller in the example does not implement the completion block, the completion handler is sometimes used to assign the document data to the document’s view or views for display. (To recall what `DetailViewController` does instead to update document views, see [Listing 3-4](Creating%20a%20Custom%20Document%20Object.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgeytcnbzfvbuqobnknltm) and accompanying text.)

To close a document, send a [closeWithCompletionHandler:](https://developer.apple.com/documentation/uikit/uidocument/1619976-close) method to the document object. This method saves the document data, if necessary, and then executes the completion handler in its sole parameter.

A good time to close a document is when the document’s view controller is dismissed, such as when the user taps the back button. Before the view controller’s view disappears, the [viewWillDisappear:](https://developer.apple.com/documentation/uikit/uiviewcontroller/1621485-viewwilldisappear) method is invoked. Your view controller subclass can override this method in order to call `closeWithCompletionHandler:` on the document object, as shown in Listing 4-7.

__Listing 4-7__  Closing a document

```objc
-(void)viewDidDisappear:(BOOL)animated {
    [super viewDidDisappear:animated];
    [self.document closeWithCompletionHandler:nil];
}
```


As noted in [Setting the Preferred Storage Location for Document Files](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgeytcnbzfvbuqnbnknltq), an application should give its users the option of storing all documents in the local file system (the application sandbox) or in iCloud (the container directory). It stores this option as a user preference and refers to this preference when saving and opening documents. When the user changes the preference, the application should move all document files in the application sandbox to iCloud or move all files in the other direction, depending on the nature of the change.

When you move a document file from local storage to the `Documents` subdirectory of the iCloud container directory, its filename is unchanged. The only part of the file-URL path that is different is the part leading up to `Documents`. To get that part of the path, you need to call the [URLForUbiquityContainerIdentifier:](https://developer.apple.com/documentation/foundation/nsfilemanager/1411653-urlforubiquitycontaineridentifie) method of `NSFileManager`. Most of the time, you pass `nil` to this method to get your app’s default container directory. If your app supports multiple containers, you can request containers explicitly by passing in a string with the corresponding iCloud container identifier—a concatenation of your team ID and an application bundle ID, separated by a period. These container identifier strings are the same ones you specify in the Identifier field of your app target’s Summary view in Xcode. It is a good idea to declare a string constant for each of your app’s container identifiers, as in this example:

```
static NSString *UbiquityContainerIdentifier = @"A93A5CM278.com.acme.document.billabong";
```

The two methods in Listing 4-8 get the iCloud container identifier and append “/Documents” to it.

__Listing 4-8__  Getting the iCloud container directory URL

```objc
-(NSURL*)ubiquitousContainerURL {
    return [[NSFileManager defaultManager] URLForUbiquityContainerIdentifier:nil];
}

-(NSURL*)ubiquitousDocumentsDirectoryURL {
    return [[self ubiquitousContainerURL] URLByAppendingPathComponent:@"Documents"];
}
```


Programmatically, you put a document in iCloud storage by calling the `NSFileManager` method [setUbiquitous:itemAtURL:destinationURL:error:](https://developer.apple.com/documentation/foundation/filemanager/1413989-setubiquitous). This method requires the file URL of the document file in the application sandbox (source URL) and the destination file URL of the document file in the application’s iCloud container directory. The first parameter takes a Boolean value, which should be `YES`.

The method in Listing 4-9 illustrates how to move a document file from an application sandbox to iCloud storage. In the sample application, when the user’s preferred storage location (iCloud or local) changes, this method is called for every document file in the application sandbox. There are roughly three parts to this method:

- Compose the source URL and the destination URL.
- On a secondary dispatch queue: Call the `setUbiquitous:itemAtURL:destinationURL:error:` method and cache the result, a Boolean value (`success`) that indicates whether the document file successfully moved to the iCloud container directory.
- On the main dispatch queue: If the call succeeds, update the document’s model objects and its presentation of those objects; if the call does not succeed, log the error (or otherwise handle it).

__Listing 4-9__  Moving a document file to iCloud storage from local storage

```objc
- (void)moveFileToiCloud:(FileRepresentation *)fileToMove {
    NSURL *sourceURL = fileToMove.url;
    NSString *destinationFileName = fileToMove.fileName;
    NSURL *destinationURL = [self.documentsDir URLByAppendingPathComponent:destinationFileName];

    dispatch_queue_t q_default;
    q_default = dispatch_get_global_queue(DISPATCH_QUEUE_PRIORITY_DEFAULT, 0);
    dispatch_async(q_default, ^(void) {
        NSFileManager *fileManager = [[[NSFileManager alloc] init] autorelease];
        NSError *error = nil;
        BOOL success = [fileManager setUbiquitous:YES itemAtURL:sourceURL
            destinationURL:destinationURL error:&error];
        dispatch_queue_t q_main = dispatch_get_main_queue();
        dispatch_async(q_main, ^(void) {
            if (success) {
                FileRepresentation *fileRepresentation = [[FileRepresentation alloc]
                    initWithFileName:fileToMove.fileName url:destinationURL];
                [_fileList removeObject:fileToMove];
                [_fileList addObject:fileRepresentation];
                NSLog(@"moved file to cloud: %@", fileRepresentation);
            }
            if (!success) {
                 NSLog(@"Couldn't move file to iCloud: %@", fileToMove);
            }
        });
    });
}
```


To move a document file from an iCloud container directory to the `Documents` directory of the application sandbox, follow the same procedure described in [Moving a Document to iCloud Storage](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgeytcnbzfvbuqnbnknltcny), except switch the source URL (now the document file in the iCloud container directory) and the destination URL (now the document file in the application sandbox). In addition, the first parameter of the [setUbiquitous:itemAtURL:destinationURL:error:](https://developer.apple.com/documentation/foundation/filemanager/1413989-setubiquitous) method should now be `NO`. Listing 4-10 shows a method implementing this procedure; it is called for each file in the iCloud container directory, moving it to the application sandbox.

__Listing 4-10__  Moving a document file from iCloud storage to local storage

```objc
- (void)moveFileToLocal:(FileRepresentation *)fileToMove {
    NSURL *sourceURL = fileToMove.url;
    NSString *destinationFileName = fileToMove.fileName;
    NSURL *destinationURL = [self.documentsDir URLByAppendingPathComponent:destinationFileName];

    dispatch_queue_t q_default;
    q_default = dispatch_get_global_queue(DISPATCH_QUEUE_PRIORITY_DEFAULT, 0);
    dispatch_async(q_default, ^(void) {
        NSFileManager *fileManager = [[[NSFileManager alloc] init] autorelease];
        NSError *error = nil;
        BOOL success = [fileManager setUbiquitous:NO itemAtURL:sourceURL destinationURL:destinationURL
            error:&error];
        dispatch_queue_t q_main = dispatch_get_main_queue();
        dispatch_async(q_main, ^(void) {
            if (success) {
                FileRepresentation *fileRepresentation = [[FileRepresentation alloc]
                    initWithFileName:fileToMove.fileName url:destinationURL];
                [_fileList removeObject:fileToMove];
                [_fileList addObject:fileRepresentation];
                NSLog(@"moved file to local storage: %@", fileRepresentation);
            }
            if (!success) {
                NSLog(@"Couldn't move file to local storage: %@", fileToMove);
            }
        });
    });
}
```


A document can go through different states during its runtime life. A state can tell you whether a document is experiencing an error, a version conflict, or some other condition that is not normal. [UIDocument](https://developer.apple.com/documentation/uikit/uidocument) declares constants (of type `UIDocumentState`) to represent document states and sets the [documentState](https://developer.apple.com/documentation/uikit/uidocument/1619982-documentstate) property with one of these constants when a change is a document’s state occurs. Table 4-1 describes the state constants.

__Table 4-1__  `UIDocumentState` constants

| Document state constant | What it means |
| `UIDocumentStateNormal` | The document is open and is experiencing no conflicts or other problems. |
| `UIDocumentStateClosed` | The document is closed. A document is in this state if `UIDocument` cannot open a document, in which case document properties might not be valid. |
| `UIDocumentStateInConflict` | There are versions of the document that are in conflict. |
| `UIDocumentStateSavingError` | An error prevents `UIDocument` from saving the document. |
| `UIDocumentStateEditingDisabled` | It is not currently safe to allow users to edit the document. |

`UIDocument` also posts a notification of type [UIDocumentStateChangedNotification](https://developer.apple.com/documentation/uikit/uidocumentstatechangednotification) when a change in document state occurs. Your application should observe this notification and respond appropriately. The initializer method of the document’s view controller is a good place to add an observer, as shown in Listing 4-11. The observer in this case is the view controller.

__Listing 4-11__  Adding an observer of the `UIDocumentStateChangedNotification` notification

```objc
-(id)initWithFileURL:(NSURL*)url createNewFile:(BOOL)createNewFile {
    NSString* nibName = [[UIDevice currentDevice] userInterfaceIdiom] ==
        UIUserInterfaceIdiomPad ? @"DetailViewController_iPad" : @"DetailViewController_iPhone";
    self = [super initWithNibName:nibName bundle:nil];
    if (self) {
        _document = [[ImageNotesDocument alloc] initWithFileURL:url];
        // other code here....
        [[NSNotificationCenter defaultCenter] addObserver:self
            selector:@selector(documentStateChanged)
            name:UIDocumentStateChangedNotification object:_document];
    }
    return self;
}
```

Be sure to remove the observer from the notification center in the class’s [dealloc](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSObject/Description.html#//apple_ref/occ/instm/NSObject/dealloc) method.

When the document’s state changes, `UIDocument` posts the `UIDocumentStateChangedNotification` notification, and the notification center delivers it by invoking the notification method (`documentStateChanged` in the example). In Listing 4-12, the observing view controller gets the current state from the [documentState](https://developer.apple.com/documentation/uikit/uidocument/1619982-documentstate) property and evaluates it. If the state is `UIDocumentStateEditingDisabled`, it hides the keyboard. If there are conflicts between different versions of the document (`UIDocumentStateInConflict`), it displays a Show Conflicts button in the document view’s toolbar. (For detailed information on handling document-version conflicts, see [Resolving Document Version Conflicts](Resolving%20Document%20Version%20Conflicts.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgeytcnbzfvbuqnrnknltc).)

__Listing 4-12__  Evaluating the current document state

```objc
-(void)documentStateChanged {
    UIDocumentState state = _document.documentState;
    [_statusView setDocumentState:state];
    if (state & UIDocumentStateEditingDisabled) {
        [_textView resignFirstResponder];
    }
    if (state & UIDocumentStateInConflict) {
        [self showConflictButton];
    }
    else {
        [self hideConflictButton];
        [self dismissModalViewControllerAnimated:YES];
    }
}
```

The notification-handling method also calls a `setDocumentState:` method implemented by a private view class. This method, shown in Listing 4-13, changes other items of the document view’s toolbar depending on the document state.

__Listing 4-13__  Updating a document’s user interface to reflect its state

```objc
-(void)setDocumentState:(UIDocumentState)documentState {
    if (documentState & UIDocumentStateSavingError) {
        self.unsavedLabel.hidden = NO;
        self.circleView.image = [UIImage imageNamed:@"Red"];
    }
    else {
        self.unsavedLabel.hidden = YES;
        if (documentState & UIDocumentStateInConflict) {
            self.circleView.image = [UIImage imageNamed:@"Yellow"];
        }
        else {
            self.circleView.image = [UIImage imageNamed:@"Green"];
        }
    }
}
```

If the document could not be saved (`UIDocumentStateSavingError`), the view controller changes the status indicator to red and displays Unsaved next to it. If there are conflicting document versions, it makes the status indicator yellow (this is in addition to the Show Conflicts button mentioned earlier). Otherwise, the status indicator is green.

Just as you want to allow users to create a document, you also want to let them delete selected documents. Deletion of a document requires you to do three things:

- Remove the document file from storage (either from the local sandbox or the iCloud container directory).
- Remove the model objects used to represent the document data in memory.
- Remove the document data presented in the document view.

When you delete a document from storage, your code should approximate what `UIDocument` does for reading and writing operations. It should perform the deletion asynchronously on a background queue, and it should use file coordination. Listing 4-14 illustrates this procedure. It dispatches a task on a background queue that creates an `NSFileCoordinator` object and calls the [coordinateWritingItemAtURL:options:error:byAccessor:](https://developer.apple.com/documentation/foundation/nsfilecoordinator/1413344-coordinate) method on it. The `byAccessor` block of this method calls the `NSFileManager` method for deleting the file, [removeItemAtURL:error:](https://developer.apple.com/documentation/foundation/nsfilemanager/1413590-removeitematurl).

__Listing 4-14__  Deleting a selected document

```objc
-(void)tableView:(UITableView *)tableView commitEditingStyle:(UITableViewCellEditingStyle)editingStyle
       forRowAtIndexPath:(NSIndexPath *)indexPath {
    NSMutableArray* fileList = nil;
    if (indexPath.section == 0) {
        fileList = self.localFileList;
    }
    else {
        fileList = self.ubiquitousFileList;
    }
    NSURL* fileURL = [[fileList objectAtIndex:indexPath.row] url];
    dispatch_async(dispatch_get_global_queue(DISPATCH_QUEUE_PRIORITY_DEFAULT, 0), ^(void) {
        NSFileCoordinator* fileCoordinator = [[NSFileCoordinator alloc] initWithFilePresenter:nil];
        [fileCoordinator coordinateWritingItemAtURL:fileURL options:NSFileCoordinatorWritingForDeleting
            error:nil byAccessor:^(NSURL* writingURL) {
            NSFileManager* fileManager = [[NSFileManager alloc] init];
            [fileManager removeItemAtURL:writingURL error:nil];
        }];
    });
    [fileList removeObjectAtIndex:indexPath.row];
    [tableView deleteRowsAtIndexPaths:[[NSArray alloc] initWithObjects:&indexPath count:1]
        withRowAnimation:UITableViewRowAnimationLeft];
}
```

In this example, the user triggers the invocation of the method when he or she taps the Delete button in a row while the table view is in editing mode.

[Next](Change%20Tracking%20and%20Undo%20Operations.md)[Previous](Creating%20a%20Custom%20Document%20Object.md)

