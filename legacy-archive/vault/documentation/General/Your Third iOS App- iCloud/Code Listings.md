---
title: 'Your Third iOS App: iCloud'
apple_id: TP40011317
resource_type: Guide
platform: iOS
topic: General
technology: null
published: '2013-09-18'
source_url: https://developer.apple.com/library/archive/documentation/General/Conceptual/iCloud101/CodeListings/CodeListings.html
archived_at: '2026-07-15T07:34:29.654564Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Your Third iOS App: iCloud](About%20Your%20Third%20iOS%20App.md)


[Next](Document%20Revision%20History.md)[Previous](Next%20Steps.md)

# Code Listings

This appendix provides listings for the interfaces and implementations of the `STEAppDelegate`, `STEMasterViewController`, `STEDetailViewController`, and `STESimpleTextDocument` classes. The listings do not show unchanged method implementations from the file templates.


```objc
#import <UIKit/UIKit.h>

@interface STEAppDelegate : UIResponder <UIApplicationDelegate>
@property (strong, nonatomic) UIWindow *window;
@end
```



```objc
#import "STEAppDelegate.h"

@implementation STEAppDelegate
@synthesize window = _window;

- (void)initializeiCloudAccess {
    dispatch_async(dispatch_get_global_queue(DISPATCH_QUEUE_PRIORITY_DEFAULT, 0), ^{
        if ([[NSFileManager defaultManager] URLForUbiquityContainerIdentifier:nil])
            NSLog(@"iCloud is available.\n");
        else
            NSLog(@"iCloud is not available.\n");
    });
}

- (BOOL)application:(UIApplication *)application
        didFinishLaunchingWithOptions:(NSDictionary *)launchOptions
{
    [self initializeiCloudAccess];
    // Override point for customization after application launch.
    return YES;
}
@end
```



```objc
#import <UIKit/UIKit.h>

@interface STEMasterViewController : UITableViewController
@property (weak, nonatomic) IBOutlet UIBarButtonItem *addButton;
@end
```



```objc
#import "STEMasterViewController.h"
#import "STESimpleTextDocument.h"
#import "STEDetailViewController.h"

NSString *STEDocFilenameExtension = @"stedoc";
NSString *DisplayDetailSegue = @"DisplayDetailSegue";
NSString *STEDocumentsDirectoryName = @"Documents";
NSString *DocumentEntryCell = @"DocumentEntryCell";

@interface STEMasterViewController()
- (NSString*)newUntitledDocumentName;
- (void)setupAndStartQuery;
@end

@implementation STEMasterViewController {
    NSMutableArray *documents;
    NSMetadataQuery *_query;
}
@synthesize addButton;

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

    [_query startQuery];
}

- (void)awakeFromNib
{
    [super awakeFromNib];

    if (!documents)
        documents = [[NSMutableArray alloc] init];

    self.navigationItem.leftBarButtonItem = self.editButtonItem;
    [self setupAndStartQuery];
}

- (void)didReceiveMemoryWarning
{
    [super didReceiveMemoryWarning];
    // Release any cached data, images, etc that aren't in use.
}

#pragma mark Document Management

- (NSString*)newUntitledDocumentName {
    NSInteger docCount = 1;   // Start with 1 and go from there.
    NSString *newDocName = nil;

    // At this point, the document list should be up to date.
    BOOL done = NO;
    while (!done) {
        newDocName = [NSString stringWithFormat:@"Note %d.%@",
                        docCount, STEDocFilenameExtension];

        // Look for an existing document with the same name. If one is
        // found, increment the docCount value and try again.
        BOOL nameExists = NO;
        for (NSURL* aURL in documents) {
            if ([[aURL lastPathComponent] isEqualToString:newDocName]) {
                docCount++;
                nameExists = YES;
                break;
            }
        }

        // If the name wasn't found, exit the loop.
        if (!nameExists)
            done = YES;
    }
    return newDocName;
}

- (IBAction)addDocument:(id)sender {
    dispatch_async(dispatch_get_global_queue(DISPATCH_QUEUE_PRIORITY_DEFAULT, 0), ^{
        // Create the new URL object on a background queue.
        NSFileManager *fm = [NSFileManager defaultManager];
        NSURL *newDocumentURL = [fm URLForUbiquityContainerIdentifier:nil];

        if (newDocumentURL) {
            newDocumentURL = [newDocumentURL
                URLByAppendingPathComponent:STEDocumentsDirectoryName
                isDirectory:YES];
            newDocumentURL = [newDocumentURL
                URLByAppendingPathComponent:[self newUntitledDocumentName]];

            // Perform the remaining tasks on the main queue.
            dispatch_async(dispatch_get_main_queue(), ^{
                // Update the data structures and table.
                [documents addObject:newDocumentURL];

                // Update the table.
                NSIndexPath* newCellIndexPath =
                [NSIndexPath indexPathForRow:([documents count] - 1) inSection:0];
                [self.tableView insertRowsAtIndexPaths:[NSArray arrayWithObject:newCellIndexPath]
                                 withRowAnimation:UITableViewRowAnimationAutomatic];

                [self.tableView selectRowAtIndexPath:newCellIndexPath
                                animated:YES
                                scrollPosition:UITableViewScrollPositionMiddle];

                // Segue to the detail view controller to begin editing.
                UITableViewCell* selectedCell = [self.tableView
                               cellForRowAtIndexPath:newCellIndexPath];
                [self performSegueWithIdentifier:DisplayDetailSegue sender:selectedCell];
            });
        }
    });
}

- (void)prepareForSegue:(UIStoryboardSegue *)segue sender:(id)sender {
    if (![segue.identifier isEqualToString:DisplayDetailSegue])
        return;

    // Get the detail view controller.
    STEDetailViewController* destVC =
           (STEDetailViewController*)segue.destinationViewController;

    // Find the correct dictionary from the documents array.
    NSIndexPath *cellPath = [self.tableView indexPathForSelectedRow];
    UITableViewCell *theCell = [self.tableView cellForRowAtIndexPath:cellPath];
    NSURL *theURL = [documents objectAtIndex:[cellPath row]];

    // Assign the URL to the detail view controller and
    // set the title of the view controller to the doc name.
    destVC.detailItem = theURL;
    destVC.navigationItem.title = theCell.textLabel.text;
}


#pragma mark Table View methods

- (NSInteger)tableView:(UITableView *)tableView
             numberOfRowsInSection:(NSInteger)section {
    return [documents count];
}

- (UITableViewCell*)tableView:(UITableView *)tableView
                    cellForRowAtIndexPath:(NSIndexPath *)indexPath {
    UITableViewCell *newCell = [tableView dequeueReusableCellWithIdentifier:DocumentEntryCell];
    if (!newCell)
        newCell = [[UITableViewCell alloc] initWithStyle:UITableViewCellStyleDefault
                                           reuseIdentifier:DocumentEntryCell];

    if (!newCell)
        return nil;

    // Get the doc at the specified row.
    NSURL *fileURL = [documents objectAtIndex:[indexPath row]];

    // Configure the cell.
    newCell.textLabel.text = [[fileURL lastPathComponent] stringByDeletingPathExtension];
    return newCell;
}

 - (void)tableView:(UITableView *)tableView
         commitEditingStyle:(UITableViewCellEditingStyle)editingStyle
         forRowAtIndexPath:(NSIndexPath *)indexPath {
     if (editingStyle == UITableViewCellEditingStyleDelete) {
         NSURL *fileURL = [documents objectAtIndex:[indexPath row]];

         // Don't use file coordinators on the app's main queue.
         dispatch_async(dispatch_get_global_queue(DISPATCH_QUEUE_PRIORITY_DEFAULT, 0), ^{
             NSFileCoordinator *fc = [[NSFileCoordinator alloc]
                                      initWithFilePresenter:nil];
             [fc coordinateWritingItemAtURL:fileURL
                 options:NSFileCoordinatorWritingForDeleting
                 error:nil
                 byAccessor:^(NSURL *newURL) {
                     NSFileManager *fm = [[NSFileManager alloc] init];
                     [fm removeItemAtURL:newURL error:nil];
             }];

         });

         // Remove the URL from the documents array.
         [documents removeObjectAtIndex:[indexPath row]];

         // Update the table UI. This must happen after
         // updating the documents array.
         [tableView deleteRowsAtIndexPaths:[NSArray arrayWithObject:indexPath]
                    withRowAnimation:UITableViewRowAnimationAutomatic];
     }
 }


#pragma mark Query Method

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



```objc
#import <UIKit/UIKit.h>
#import "STESimpleTextDocument.h"

@interface STEDetailViewController : UIViewController <STESimpleTextDocumentDelegate>

@property (strong, nonatomic) NSURL *detailItem;
@property (strong, nonatomic) IBOutlet UILabel *detailDescriptionLabel;
@property (weak, nonatomic) IBOutlet UITextView *textView;

@end
```



```objc
#import "STEDetailViewController.h"

@interface STEDetailViewController ()
- (void)configureView;
@end

@implementation STEDetailViewController {
    STESimpleTextDocument *_document;
}
@synthesize detailItem = _detailItem;
@synthesize detailDescriptionLabel = _detailDescriptionLabel;
@synthesize textView = _textView;

#pragma mark View Management

- (void)viewWillAppear:(BOOL)animated {
    [super viewWillAppear:animated];

    // Clear out the text view contents.
    self.textView.text = @"";

    // Create the document and assign the delegate.
    _document = [[STESimpleTextDocument alloc] initWithFileURL:self.detailItem];
    _document.delegate = self;

    // If the file exists, open it; otherwise, create it.
    NSFileManager *fm = [NSFileManager defaultManager];
    if ([fm fileExistsAtPath:[self.detailItem path]])
        [_document openWithCompletionHandler:nil];
    else
        // Save the new document to disk.
        [_document saveToURL:self.detailItem
                   forSaveOperation:UIDocumentSaveForCreating
                   completionHandler:nil];

    // Register for the keyboard notifications
    [[NSNotificationCenter defaultCenter] addObserver:self
                        selector:@selector(keyboardWillShow:)
                        name:UIKeyboardWillShowNotification
                        object:nil];
    [[NSNotificationCenter defaultCenter] addObserver:self
                        selector:@selector(keyboardWillHide:)
                        name:UIKeyboardWillHideNotification
                        object:nil];
}

- (void)viewWillDisappear:(BOOL)animated {
    [super viewWillDisappear:animated];

    NSString *newText = self.textView.text;
    _document.documentText = newText;

    // Close the document.
    [_document closeWithCompletionHandler:nil];

    [[NSNotificationCenter defaultCenter] removeObserver:self
                        name:UIKeyboardWillShowNotification
                        object:nil];
    [[NSNotificationCenter defaultCenter] removeObserver:self
                        name:UIKeyboardWillHideNotification
                        object:nil];
}


#pragma mark Keyboard Handlers

- (void)keyboardWillShow:(NSNotification*)aNotification {
    NSDictionary *info = [aNotification userInfo];
    CGRect kbSize = [[info objectForKey:UIKeyboardFrameEndUserInfoKey]
                            CGRectValue];
    double duration = [[info objectForKey:UIKeyboardAnimationDurationUserInfoKey]
                            doubleValue];

    UIEdgeInsets insets = self.textView.contentInset;
    insets.bottom += kbSize.size.height;

    [UIView animateWithDuration:duration animations:^{
        self.textView.contentInset = insets;
    }];
}

- (void)keyboardWillHide:(NSNotification*)aNotification {
    NSDictionary *info = [aNotification userInfo];
    double duration = [[info objectForKey:UIKeyboardAnimationDurationUserInfoKey]
                            doubleValue];

    // Reset the text view's bottom content inset.
    UIEdgeInsets insets = self.textView.contentInset;
    insets.bottom = 0;

    [UIView animateWithDuration:duration animations:^{
        self.textView.contentInset = insets;
    }];
}
```



```objc
#import <UIKit/UIKit.h>

@protocol STESimpleTextDocumentDelegate;

@interface STESimpleTextDocument : UIDocument
@property (copy, nonatomic) NSString* documentText;
@property (weak, nonatomic) id<STESimpleTextDocumentDelegate> delegate;
@end

@protocol STESimpleTextDocumentDelegate <NSObject>
@optional
- (void)documentContentsDidChange:(STESimpleTextDocument*)document;
@end
```



```objc
#import "STESimpleTextDocument.h"

@implementation STESimpleTextDocument
@synthesize documentText = _documentText;
@synthesize delegate = _delegate;

- (void)setDocumentText:(NSString *)newText {
    NSString* oldText = _documentText;
    _documentText = [newText copy];

    // Register the undo operation.
    [self.undoManager setActionName:@"Text Change"];
    [self.undoManager registerUndoWithTarget:self
            selector:@selector(setDocumentText:)
            object:oldText];
}

- (id)contentsForType:(NSString *)typeName
      error:(NSError *__autoreleasing *)outError {
    if (!self.documentText)
        self.documentText = @"";

    NSData *docData = [self.documentText dataUsingEncoding:NSUTF8StringEncoding];

    return docData;
}

- (BOOL)loadFromContents:(id)contents
        ofType:(NSString *)typeName
        error:(NSError *__autoreleasing *)outError {
    if ([contents length] > 0)
        self.documentText = [[NSString alloc]
                initWithData:contents
                encoding:NSUTF8StringEncoding];
    else
        self.documentText = @"";

    // Tell the delegate that the document contents changed.
    if (self.delegate && [self.delegate respondsToSelector:
                           @selector(documentContentsDidChange:)])
        [self.delegate documentContentsDidChange:self];

    return YES;
}

@end
```

[Next](Document%20Revision%20History.md)[Previous](Next%20Steps.md)

