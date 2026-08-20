---
title: SimpleStickies
apple_id: DTS40009051
resource_type: Sample Code
platform: macOS
topic: Data Management
technology: SyncServices
published: '2009-10-14'
source_url: https://developer.apple.com/library/archive/samplecode/SyncServices_SimpleStickies/Listings/ReadMe_txt.html
archived_at: '2026-07-18T03:25:55.085081Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [SimpleStickies](SimpleStickies.md)


[Next](main.m.md)[Previous](SimpleStickies.md)

# ReadMe.txt

```
Simple Stickies - Sync Services Example

About the SimpleStickies Example

This example is meant to help develop individual applications that sync data amongst themselves. The SimpleStickies application relies on the Stickies schema. This application allows you to create sticky notes that are displayed in a table view and utilizes the Sync Services framework to sync them locally as well as over MobileMe. The application will sync whenever it saves its records to a local file. This example also demonstrates the use of the ISyncSessionDriver class. Using ISyncSessionDriver's automatic sync alert handling, the application will sync whenever another application, device, server, or peer syncs data belonging to the same schema.

You can also extend a schema or create your own schema to sync custom objects. You can use the Sync Services API from both Objective-C and C programs. This is meant to serve as a guideline for development and to help understand the sync process as a whole.

Building and Running the Application

Building and launching
1. Open the SimpleStickies.xcodeproj file with Xcode.
2. Verify that the Active SDK is set to Mac OS X 10.6 and that the correct Active Architecture is selected. 
3. Select Build and Run.

Quick tutorial 
  You should sync stickies over MobileMe from one instance of SimpleStickies to another running on another computer or user account to demonstrate the pushing and pulling of records.
• Launch the SimpleStickies application and create a new sticky note
• Select File > Sync (cmd-s) to save and sync the record to the truth database.
• Open System Preferences and select the MobileMe preference pane
• Select the Sync tab and enable the Stickies dataclass
• Click Sync Now and choose to replace information on MobileMe with information from your computer for stickies
• Launch the SimpleStickies Application on another computer or user account
• On the computer or user account mentioned directly above, open System Preferences and select the MobileMe preference pane
• Select the Sync tab and enable the Stickies dataclass
• Click Sync Now and choose to replace information on your computer with data from MobileMe for stickies
• Your sticky note will be synced from MobileMe and appear in the SimpleStickies Application
• Feel free to add, edit, or delete sticky notes from either computer or user account and sync these changes across MobileMe
• You can verify that records are pushed into the truth using Syncrospector

Cleanup for SimpleStickies (restore the truth and SimpleStickies to its initial state without affecting other applications, schemas and MobileMe)
• Exit the SimpleStickies application
• Remove the application data: rm ~/Library/Application\ Support/SyncExamples/com.mycompany.SimpleStickies.xml
• Unregister the SimpleStickies client from the Clients view (cmd-1) in Syncrospector. The client identifier is com.mycompany.SimpleStickies.
• Unregister the schema for Stickies from the Schemas view (cmd-6) in Syncrospector. The schema is named com.mycompany.Stickies

SimpleStickies.xcodeproj - Description

This is a brief description of the classes contained in the SimpleStickies.xcodeproj file.


AppDelegate
Class that controls the Cocoa application and window delegate. It is also the ISyncSessionDriver delegate and data source. This class creates the window containing the table of Note records. This window creates and updates Note records.

DataSource
Implements a simple data source to save and load records to a plist and read/write access from the application. Keeps track of the records that were added or deleted and defines the schema.

Entity
Defines the mapping between application Entity objects and the data source schema. Sets keys for relationships and defines accessor methods for the entity's properties.

EntityModel
Maintains an entity-relationship model representation, defines the entity's properties with to-one and to-many relationships. Initializes the model representation and keeps track of an entity's properties through key-value representations.

RecordTransformer
Takes care of converting data, transforms a KVC compliant object into a sync record and back for convenient pushing and pulling of data.

Note
Controls the attributes of a Note object, like size, position, color, font, and specifies default properties (which can be edited).

MainMenu.nib
Contains the Cocoa main menu and Note window with the table view. Contains the AppDelegate object.

Note: .plist files contain specific schemas and structures for the client and the application. These files help visualize the way in which data is accessed and stored. We recommend going over the schemas and .plist files to get a broad idea of the project.

Viewing Changes in Database and Debugging

You can check the way in which your data and the Truth database are altered using Syncrospector. Syncrospector is a helpful tool that makes debugging easier since it helps visualize how data is pushed and pulled from the Truth database. For more information, visit: Apple Developer Documentation: Using Syncrospector

Other Resources

• Introduction to Sync Services Programming Guide
• Introduction to Sync Services Tutorial
```

[Next](main.m.md)[Previous](SimpleStickies.md)

