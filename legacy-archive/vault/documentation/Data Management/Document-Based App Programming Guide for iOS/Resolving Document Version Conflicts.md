---
title: Document-Based App Programming Guide for iOS
apple_id: TP40011149
resource_type: Guide
platform: tvOS|iOS
topic: Data Management
technology: UIKit
published: '2012-09-19'
source_url: https://developer.apple.com/library/archive/documentation/DataManagement/Conceptual/DocumentBasedAppPGiOS/ResolveVersionConflicts/ResolveVersionConflicts.html
archived_at: '2026-07-15T07:24:00.046203Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Document-Based App Programming Guide for iOS](About%20Document-Based%20Applications%20in%20iOS.md)


[Next](Document%20Revision%20History.md)[Previous](Change%20Tracking%20and%20Undo%20Operations.md)

# Resolving Document Version Conflicts

In an iCloud world, when a user has installed a document-based application on multiple devices or desktop systems, there can be conflicts between different versions of the same document. Recall that an application updates a document file in the local container directory and those changes are then transmitted—usually immediately—to iCloud. But what if this transmission is not immediate? For example, you edit a document using the Mac OS X version of your application, but you’ve also edited the same document using the iPad version of the application—and you did so while the device was in Airplane Mode. When you switch off Airplane Mode, the local change to the document is transferred to iCloud. iCloud notices a conflict and notifies the application.

As [Monitoring Document-State Changes and Handling Errors](Managing%20the%20Life%20Cycle%20of%20a%20Document.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgeytcnbzfvbuqnbnknltm) describes, your application becomes aware of document-version conflicts by observing the [UIDocumentStateChangedNotification](https://developer.apple.com/documentation/uikit/uidocumentstatechangednotification) notification. If the [documentState](https://developer.apple.com/documentation/uikit/uidocument/1619982-documentstate) property changes to [UIDocumentStateInConflict](https://developer.apple.com/documentation/uikit/uidocumentstate/uidocumentstateinconflict), multiple versions of the same document exist. The application is responsible for resolving those conflicts as soon as possible, with or without the user’s help.

You learn about the conflicting versions of a document through two class methods of the [NSFileVersion](https://developer.apple.com/documentation/foundation/nsfileversion) class. The [currentVersionOfItemAtURL:](https://developer.apple.com/documentation/foundation/nsfileversion/1412963-currentversionofitematurl) method returns an `NSFileVersion` object representing what’s referred to as the _current file_; the current file is chosen by iCloud on some basis as the current “conflict winner” and is the same across all devices. By calling the [unresolvedConflictVersionsOfItemAtURL:](https://developer.apple.com/documentation/foundation/nsfileversion/1417854-unresolvedconflictversionsofitem) method, you get an array of `NSFileVersion` objects; these objects are called _conflict versions_, and each represents an unresolved version conflict for the file located at the specified URL. `NSFileVersion` objects can give you information helpful in resolving conflicts, such as modification dates, localized document names, and localized names of saving computers.

Your application can follow one of three strategies for resolving document-version conflicts:

- Merge the changes from the conflicting versions.
- Choose one of the document versions based on some pertinent factor, such as the version with the latest modification date.
- Enable the user to view conflicting versions of a document and select the one to use.

Which strategy is best to use depends a lot upon your document data. If you can merge the contents of different document versions without introducing contradictory elements, then follow that strategy. Or choose the document version with the latest modification date if your application doesn’t suffer any loss of data as a result.

Generally, you should try to resolve the conflict without involving the user, but for some applications that might not be possible. If an application takes the user-centered approach, it should discreetly inform the user about the version conflict and expose a button or other control that initiates the resolution procedure. [An Example: Letting the User Pick the Version](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgeytcnbzfvbuqnrnknlte) examines the code of an application that lets the user select the document version to use.

When your application or its users resolve a document version conflict by picking a version of a document, your application should complete the following steps:

- If the chosen version is a conflict version, replace the current document file with the conflict-version document file.

  To to this, call the [replaceItemAtURL:options:error:](https://developer.apple.com/documentation/foundation/nsfileversion/1412297-replaceitem) method on the `NSFileVersion` object representing the version, passing in the document’s current-file URL.
- If the chosen version is a conflict version, revert the document so that it displays the new data in the document file

  To do this, call the `UIDocument` method [revertToContentsOfURL:completionHandler:](https://developer.apple.com/documentation/uikit/uidocument/1619974-reverttocontentsofurl) on the document object, passing in the document’s current-file URL.
- Disassociate all conflict versions with the document’s file URL.

  To do this, call the `NSFileVersion` class method [removeOtherVersionsOfItemAtURL:error:](https://developer.apple.com/documentation/foundation/nsfileversion/1411537-removeotherversionsofitematurl), passing in the document’s file URL.
- Mark each conflict version as resolved so that iOS doesn’t raise it again as a conflicting version.

  To do this, set the [resolved](https://developer.apple.com/documentation/foundation/nsfileversion/1414906-resolved) property of each `NSFileVersion` object representing a conflict version to `YES`. This step should always be done last.
- Remove the resolved versions of the document.

  For any versions you no longer need, call the [removeAndReturnError:](https://developer.apple.com/documentation/foundation/nsfileversion/1407486-remove) method of `NSFileVersion` to reclaim the storage for the file. Document revisions remain on the server until you delete them.

Our sample document-based application is a simple text editor. It would be difficult for such an application to locate and merge textual differences in conflicting versions of the document, and even if it did, the resulting document might not be what the user wants. The application could pick the document version with the most recent modification date, but then again there’s no way to be certain that is the version the user wants. A good conflict-resolution strategy in this case is to let the user, who is most familiar with the document’s contents, pick the version she or he wants.

You might recall the code shown in Listing 6-1 from [Monitoring Document-State Changes and Handling Errors](Managing%20the%20Life%20Cycle%20of%20a%20Document.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgeytcnbzfvbuqnbnknltm). This code shows the method of the document’s view controller that handles the [UIDocumentStateChangedNotification](https://developer.apple.com/documentation/uikit/uidocumentstatechangednotification) notification posted by `UIDocument` when there is a change in document state. If the new document state is [UIDocumentStateInConflict](https://developer.apple.com/documentation/uikit/uidocumentstate/uidocumentstateinconflict), the view controller shows a Resolve Conflicts button in a custom status view. (It also sets the color of the status indicator to red.)

__Listing 6-1__  Detecting a conflict in document versions

```objc
-(void)documentStateChanged {
    UIDocumentState state = _document.documentState;
    [_statusView setDocumentState:state];
    if (state & UIDocumentStateEditingDisabled) {
        [_textView resignFirstResponder];
    }

    if (state & UIDocumentStateInConflict) {
        [self showConflictButton];            // <------ Shows "Resolve Conflicts" button
    }
    else {
        [self hideConflictButton];
        [self dismissModalViewControllerAnimated:YES];
    }
}
```

When the user taps the button, UIKit invokes the method in Listing 6-2. This method displays modally the view of a custom conflict-resolver view controller.

__Listing 6-2__  Showing the user interface for resolving document version conflicts

```objc
-(void)conflictButtonPushed
{
    ConflictResolverViewController* conflictResolver = [[ConflictResolverViewController alloc]
        initWithURL:_document.fileURL delegate:self];
    [self presentViewController:conflictResolver animated:YES completion:nil];
    [conflictResolver release];
}
```

The `ConflictResolverViewController` object creates a page view controller ([UIPageViewController](https://developer.apple.com/documentation/uikit/uipageviewcontroller) object) that allows user to page between, and examine, the current-file document and each conflict-version document. In the tool bar of each document view is a Select Version button. If the user taps that button, one of the two custom delegation methods shown in Listing 6-3 is called, depending on whether the chosen document is the current-file document or a conflict-version document.

__Listing 6-3__  Resolving a document version conflict

```objc
-(void)conflictResolver:(ConflictResolverViewController *)conflictResolver
       didResolveWithFileVersion:(NSFileVersion *)fileVersion {
    [self dismissViewControllerAnimated:YES completion:nil];
    [fileVersion replaceItemAtURL:_document.fileURL options:0 error:nil];
    [NSFileVersion removeOtherVersionsOfItemAtURL:_document.fileURL error:nil];
    [_document revertToContentsOfURL:_document.fileURL completionHandler:nil];
    NSArray* conflictVersions = [NSFileVersion unresolvedConflictVersionsOfItemAtURL:_document.fileURL];
    for (NSFileVersion* fileVersion in conflictVersions) {
        fileVersion.resolved = YES;
    }
}

-(void)conflictResolverDidResolveWithCurrentVersion:(ConflictResolverViewController*)conflictResolver {
    [self dismissViewControllerAnimated:YES completion:nil];
    [NSFileVersion removeOtherVersionsOfItemAtURL:_document.fileURL error:nil];
    NSArray* conflictVersions = [NSFileVersion unresolvedConflictVersionsOfItemAtURL:_document.fileURL];
    for (NSFileVersion* fileVersion in conflictVersions) {
        fileVersion.resolved = YES;
    }
}
```

These methods illustrate the steps described in [How to Tell iOS That a Document Version Conflict Is Resolved](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgeytcnbzfvbuqnrnknltm). If the chosen document is a conflict version, the delegate calls [replaceItemAtURL:options:error:](https://developer.apple.com/documentation/foundation/nsfileversion/1412297-replaceitem) on the passed-in `NSFileVersion` object to replace the document file in the iCloud container directory with the chosen document. The delegate then enumerates the array containing `NSFileVersion` objects representing all conflict versions of the document and sets the [resolved](https://developer.apple.com/documentation/foundation/nsfileversion/1414906-resolved) property of each object to `YES`. It then asks `NSFileVersion` to remove all other conflict versions of the document associated with the document’s file URL and calls [revertToContentsOfURL:completionHandler:](https://developer.apple.com/documentation/uikit/uidocument/1619974-reverttocontentsofurl) to revert the displayed document to the new contents of the document file.

The second delegation method, invoked when the current document file is selected, is much simpler. It sets the `resolved` property of all `NSFileVersion` objects representing conflict versions to `YES` and removes all conflict versions associated with the document file URL.

[Next](Document%20Revision%20History.md)[Previous](Change%20Tracking%20and%20Undo%20Operations.md)

