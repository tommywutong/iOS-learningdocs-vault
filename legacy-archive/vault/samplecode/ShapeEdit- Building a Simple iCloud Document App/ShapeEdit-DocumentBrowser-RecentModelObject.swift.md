---
title: 'ShapeEdit: Building a Simple iCloud Document App'
apple_id: TP40016100
resource_type: Sample Code
platform: iOS
topic: Data Management
technology: UIKit
published: '2016-09-13'
source_url: https://developer.apple.com/library/archive/samplecode/ShapeEdit/Listings/ShapeEdit_DocumentBrowser_RecentModelObject_swift.html
archived_at: '2026-07-18T03:23:43.550438Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [ShapeEdit: Building a Simple iCloud Document App](ShapeEdit-%20Building%20a%20Simple%20iCloud%20Document%20App.md)


[Next](ShapeEdit-DocumentBrowser-RecentModelObjectsManager.swift.md)[Previous](ShapeEdit-DocumentBrowser-DocumentBrowserController.swift.md)

# ShapeEdit/DocumentBrowser/RecentModelObject.swift

```swift
/*
    Copyright (C) 2016 Apple Inc. All Rights Reserved.
    See LICENSE.txt for this sample’s licensing information

    Abstract:
    This is the RecentsModelObject which listens for notifications about a single recent object. It then forwards the notifications on to the delegate.
*/

import Foundation

/**
    The delegate protocol implemented by the object that wants to be notified
    about changes to this recent.
*/
protocol RecentModelObjectDelegate: class {
    func recentWasDeleted(recent: RecentModelObject)
    func recentNeedsReload(recent: RecentModelObject)
}

/**
    The `RecentModelObject` manages a single recent on disk.  It is registered
    as a file presenter and as such is notified when the recent changes on
    disk.  It forwards these notifications on to its delegate.
*/
class RecentModelObject: NSObject, NSFilePresenter, ModelObject {
    // MARK: - Properties

    weak var delegate: RecentModelObjectDelegate?

    private(set) var URL: NSURL

    private(set) var displayName = ""

    private(set) var subtitle = ""

    private(set) var bookmarkDataNeedsSave = false

    private var bookmarkData: NSData?

    private var isSecurityScoped = false

    static let displayNameKey = "displayName"
    static let subtitleKey = "subtitle"
    static let bookmarkKey = "bookmark"

    var presentedItemURL: NSURL? {
        return URL
    }

    var presentedItemOperationQueue: NSOperationQueue {
        return NSOperationQueue.mainQueue()
    }

    deinit {
        URL.stopAccessingSecurityScopedResource()
    }

    // MARK: - NSCoding

    required init?(URL: NSURL) {
        self.URL = URL

        do {
            super.init()

            try refreshNameAndSubtitle()

            bookmarkDataNeedsSave = true
        }
        catch {
            return nil
        }
    }

    required init?(coder aDecoder: NSCoder) {
        do {
            displayName = aDecoder.decodeObjectOfClass(NSString.self, forKey: RecentModelObject.displayNameKey) as! String

            subtitle = aDecoder.decodeObjectOfClass(NSString.self, forKey: RecentModelObject.subtitleKey) as! String

            // Decode the bookmark into a URL.
            var bookmarkDataIsStale: ObjCBool = false

            guard let bookmark = aDecoder.decodeObjectOfClass(NSData.self, forKey: RecentModelObject.bookmarkKey) else {
                throw ShapeEditError.BookmarkResolveFailed
            }

            bookmarkData = bookmark

            URL = try NSURL(byResolvingBookmarkData: bookmark, options: .WithoutUI, relativeToURL: nil, bookmarkDataIsStale: &bookmarkDataIsStale)

            /*
                The URL is security-scoped for external documents, which live outside
                of the application's sandboxed container.
            */
            isSecurityScoped = URL.startAccessingSecurityScopedResource()

            if bookmarkDataIsStale {
                self.bookmarkDataNeedsSave = true

                print("\(URL) is stale.")
            }

            super.init()

            do {
                try self.refreshNameAndSubtitle()
            }
            catch {
                // Ignore the error, use the stale display name.
            }
        }
        catch let error {
            print("bookmark for \(displayName) failed to resolve: \(error)")

            URL = NSURL()

            bookmarkDataNeedsSave = false

            self.bookmarkData = NSData()

            super.init()

            return nil
        }
    }

    func encodeWithCoder(aCoder: NSCoder) {
        do {
            aCoder.encodeObject(displayName, forKey: RecentModelObject.displayNameKey)

            aCoder.encodeObject(subtitle, forKey: RecentModelObject.subtitleKey)

            if bookmarkDataNeedsSave {
                /*
                    Encode our URL into a security scoped bookmark.  We need to be sure
                    to mark the bookmark as suitable for a bookmark file or it won't
                    resolve properly.
                */
                bookmarkData = try URL.bookmarkDataWithOptions(.SuitableForBookmarkFile, includingResourceValuesForKeys: nil, relativeToURL: nil)

                self.bookmarkDataNeedsSave = false
            }

            aCoder.encodeObject(bookmarkData, forKey: RecentModelObject.bookmarkKey)
        }
        catch {
            print("bookmark for \(displayName) failed to encode: \(error).")
        }
    }

    // MARK: - NSFilePresenter Notifications

    func accommodatePresentedItemDeletionWithCompletionHandler(completionHandler: NSError? -> Void) {
        /*
            Notify our delegate that the recent was deleted, then call the completion 
            handler to allow for the deletion to go through.
        */
        delegate?.recentWasDeleted(self)

        completionHandler(nil)
    }

    func presentedItemDidMoveToURL(newURL: NSURL) {
        /*
            Update our presented item URL to the new location, then notify our
            delegate that the recent needs to be refreshed in the UI.
        */
        URL = newURL

        do {
            try refreshNameAndSubtitle()
        }
        catch {
             // Ignore a failure here. We'll just keep the old display name.
        }

        delegate?.recentNeedsReload(self)
    }

    func presentedItemDidChange() {
        // Notify the delegate that the recent needs to be refreshed in the UI.
        delegate?.recentNeedsReload(self)
    }

    // MARK: - Initialization Support

    private func refreshNameAndSubtitle() throws {
        var refreshedName: AnyObject?

        try URL.getPromisedItemResourceValue(&refreshedName, forKey: NSURLLocalizedNameKey)

        displayName = refreshedName as! String

        let fileManager = NSFileManager.defaultManager()

        if let ubiquitousContainer = fileManager.URLForUbiquityContainerIdentifier(nil) {
            var relationship: NSURLRelationship = .Other

            try fileManager.getRelationship(&relationship, ofDirectoryAtURL: ubiquitousContainer, toItemAtURL: URL)

            if relationship != .Contains {
                var externalContainerName: AnyObject?

                try URL.getPromisedItemResourceValue(&externalContainerName, forKey: NSURLUbiquitousItemContainerDisplayNameKey)

                subtitle = "in \(externalContainerName as! String)"
            }
            else {
                subtitle = ""
            }
        }
        else {
            throw ShapeEditError.SignedOutOfiCloud
        }
    }

    /// Two RecentModelObjects are equal iff their urls are equal.
    override func isEqual(object: AnyObject?) -> Bool {
        guard let other = object as? RecentModelObject else {
            return false
        }

        return other.URL.isEqual(URL)
    }

    /// Hash method implemented to match `isEqual(_:)`'s constraints.
    override var hash: Int {
        return URL.hash
    }
}
```

[Next](ShapeEdit-DocumentBrowser-RecentModelObjectsManager.swift.md)[Previous](ShapeEdit-DocumentBrowser-DocumentBrowserController.swift.md)

