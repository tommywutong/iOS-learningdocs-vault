---
title: 'PhotoEditor: Crafting Modern Cocoa Apps'
apple_id: TP40017384
resource_type: Sample Code
platform: macOS
topic: User Experience
technology: null
published: '2016-10-27'
source_url: https://developer.apple.com/library/archive/samplecode/PhotoEditor/Listings/Photo_Editor_PhotoDocument_swift.html
archived_at: '2026-07-18T03:18:49.535364Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [PhotoEditor: Crafting Modern Cocoa Apps](PhotoEditor-%20Crafting%20Modern%20Cocoa%20Apps.md)


[Next](Photo%20Editor-CanvasClipView.swift.md)[Previous](Photo%20Editor-PhotoDocumentWindowController.swift.md)

# Photo Editor/PhotoDocument.swift

```swift
/*
 Copyright (C) 2016 Apple Inc. All Rights Reserved.
 See LICENSE.txt for this sample’s licensing information

 Abstract:
 The PhotoDocument subclasses NSDocument and does the basic data abstraction.
*/

import Cocoa

class PhotoDocument: NSDocument {

    /*
        This enumerated type is currently needed due to a Bridging problem that exists between the Swift 3 Error protocol and NSError.
        This will be fixed in a future update.
        For more information see: https://github.com/apple/swift-evolution/blob/master/proposals/0112-nserror-bridging.md
    */
    enum CocoaError : Error {
        case fileReadUnknown
    }

    var photo: Photo?

    override init() {
        super.init()
        hasUndoManager = true
    }

    override class func autosavesInPlace() -> Bool {
        return true
    }

    override func makeWindowControllers() {
        let storyboard = NSStoryboard(name: "Main", bundle: nil)
        let windowController = storyboard.instantiateController(withIdentifier: "Document Window Controller") as! NSWindowController
        addWindowController(windowController)
    }

    override func data(ofType typeName: String) throws -> Data {
        guard let photoToArchive = photo else { throw NSError(domain: NSOSStatusErrorDomain, code: unimpErr, userInfo: nil) }
        return NSKeyedArchiver.archivedData(withRootObject: photoToArchive)
    }

    override func read(from data: Data, ofType typeName: String) throws {
        switch typeName {
            case "JPEG image", "Portable Network Graphics image":

                guard let image = NSImage(data: data) else { throw CocoaError.fileReadUnknown }

                photo = Photo(title: displayName, image: image)
                fileType = "Photo Document"
                fileURL = nil

                // Mark that we did a change so we get a callback to autosave
                updateChangeCount(.changeDone)

            case "Photo Document":
                guard let unarchivedPhoto = NSKeyedUnarchiver.unarchiveObject(with: data) as? Photo else { throw CocoaError.fileReadUnknown }
                photo = unarchivedPhoto

            default:
                throw NSError(domain: NSOSStatusErrorDomain, code: unimpErr, userInfo: nil)
        }
    }

}
```

[Next](Photo%20Editor-CanvasClipView.swift.md)[Previous](Photo%20Editor-PhotoDocumentWindowController.swift.md)

