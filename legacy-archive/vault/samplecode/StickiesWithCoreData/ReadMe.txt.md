---
title: StickiesWithCoreData
apple_id: DTS40009052
resource_type: Sample Code
platform: macOS
topic: Data Management
technology: SyncServices
published: '2009-10-14'
source_url: https://developer.apple.com/library/archive/samplecode/SyncServices_StickiesWithCoreData/Listings/ReadMe_txt.html
archived_at: '2026-07-18T03:25:55.537346Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [StickiesWithCoreData](StickiesWithCoreData.md)


[Next](main.m.md)[Previous](StickiesWithCoreData.md)

# ReadMe.txt

```
Stickies With Core Data - Sync Services Example

About the StickiesWithCoreData Example

This example is meant to help develop individual applications that sync data amongst themselves. The StickiesWithCoreData example demonstrates how to implement a sync client for an application that leverages the Core Data framework. It also provides an example of a sync schema that is generated from a Core Data managed object model. You can also extend a schema or create your own schema to sync custom objects. You can use the Sync Services API from both Objective-C and C programs. This is meant to serve as a guideline for development and to help understand the sync process as a whole.

Building and Running the Application

Building and launching
1. Open the StickiesWithCoreData.xcodeproj file with Xcode. 
2. Select Build and Run.
3. Verify that the Active SDK is set to Mac OS X 10.6 and that the correct Active Architecture is selected. 

Quick tutorial 
  You should sync stickies over MobileMe from one instance of StickiesWithCoreData to another running on another computer or user account to demonstrate the pushing and pulling of records.
• Launch the StickiesWithCoreData application and create a new sticky note
• Open the Debug window (Debug > Show Debug Window) or press cmd+d
• Select File > New (cmd-n) to create a new sticky note
• Select File > Save (cmd-s) to save and sync the record to the truth database.
• Open System Preferences and select the MobileMe preference pane
• Select the Sync tab and enable the Stickies dataclass
• Click Sync Now and choose to replace information on MobileMe with information from your computer for stickies
• Launch the StickiesWithCoreData Application on another computer or user account
• On the computer or user account mentioned directly above, open System Preferences and select the MobileMe preference pane
• Select the Sync tab and enable the Stickies dataclass
• Click Sync Now and choose to replace information on your computer with data from MobileMe for stickies
• Your sticky note will be synced from MobileMe and appear in the StickiesWithCoreData Application
• Feel free to add, edit, or delete sticky notes from either computer or user account and sync these changes across MobileMe
• You can verify that records are pushed into the truth using Syncrospector

StickiesWithCoreData - Description

This is a brief description of the classes contained in the StickiesWithCoreData.xcodeproj file.

AppController
Passes along the open command to the current document.  Implements the NSPersistentStoreCoordinatorSyncing protocol methods, controls the events loop, and registers the schema. Adds the feature of saving, which implements Core Data.

Sticky
Manages Stickies windows view, controls adding and removing of stickies, their record identification,  as well as their properties (such as size, text, position).

StickyResizeCornerView
Controls the size view and resizing of a Sticky.

StickyTitleBarView
Controls the color of the Sticky, and the predefined dimensions.

StickyWindow
Controls a Sticky Window when it is selected.

Note: .plist files contain specific schemas and structures for the client and the application. These files help visualize the way in which data is accessed and stored. A a recommendation, go over the schemas and .plist files to get a broad idea of the project.

Viewing Changes in Database and Debugging

You can check the way in which your data and the Truth database are altered using Syncrospector. Syncrospector is a helpful tool that makes debugging easier since it helps visualize how data is pushed and pulled from the Truth database. For more information, visit: Apple Developer Documentation: Using Syncrospector.

Other Resources

• Introduction to Sync Services Programming Guide
• Introduction to Sync Services Tutorial
```

[Next](main.m.md)[Previous](StickiesWithCoreData.md)

