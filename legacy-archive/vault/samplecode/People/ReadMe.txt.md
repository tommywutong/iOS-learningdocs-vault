---
title: People
apple_id: DTS40009050
resource_type: Sample Code
platform: macOS
topic: Data Management
technology: SyncServices
published: '2009-07-21'
source_url: https://developer.apple.com/library/archive/samplecode/SyncServices_People/Listings/ReadMe_txt.html
archived_at: '2026-07-18T03:25:53.934278Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [People](People.md)


[Next](main.m.md)[Previous](People.md)

# ReadMe.txt

```
People Application - Sync Services Example

About the People Example

The People application is designed to demonstrate the sync process with a specific client. It extends the contact's information found in the Address Book application by adding a picture to the contact's information and a location (the schema extension adds Candid and Extreme photos, and Location properties to the com.apple.Contacts schema). The add, remove and search contact options are also available. It is also possible to edit an existing contact's information, that is, it is possible to edit the name, middle name, last name, company, and location properties within the People's example and sync it with Address Book. Consequently, the People application and the Address Book application will both have the same contacts and contacts' information after syncing. You can use the Sync Services API from both Objective-C and C programs. This is meant to serve as a guideline for development and to help understand the sync process as a whole.

The People application also offers the options to select the sync mode for the data: fast sync, slow sync, refresh sync and to pull the truth. 

Building and Running the Application

Building and launching
1. Open the People.xcodeproj file with Xcode.
2. Verify that the Active SDK is set to Mac OS X 10.6 and that the correct Active Architecture is selected.
3. Select Build and Run.
4. Copy the PeopleSchemaExtension.syncschema bundle from the build products folder into the folder  /Library/SyncServices/Schemas/
5. Launch the People application

Viewing Changes in Database and Debugging

You can check the way in which your data and the Truth database are altered using Syncrospector. Syncrospectoris a helpful tool that makes debugging easier since it helps visualize how data is pushed and pulled from the Truth database. For more information, visit: Apple Developer Documentation: Using Syncrospector


People.xcodeproj - Description

This is a brief description of the classes contained in the People.xcodeproj file.

AppController
Describes and controls the behavior of the interface. Receives messages every time a contact is added, removed, or updated, as well as the activity of that contact's image. Controls the model and view of the application, the actions sent and received to/from the application. Saves and edits the information in the database, and awakes it from nib.

AppControllerExtensions
Extends the AppController class to find a contact and to sort the names in the display.

AppControllerSyncing
Controls the syncing activities of the application like the pushing and pulling of data to/from the database, changes the sync mode as a response to a selected option, and controls the states of the sync cycle.

Change
Computes record changes done to the contacts' database, such as add, remove and modify applied to a record.

Constants
Defines fixed key values, view types and sync modes. Helps make other classes "clean" by calling keys with the specified values anywhere in the code.

LastNameFilter
Identifies and manages unique records.

NSArrayExtras
Extends the NSArray and NSMutableArray classes to keep track of changes done to records.

NSEventExtras
Extends the NSEvent class to respond to specific events in the UI, such as a delete or return keys press.

TableView
Controls the number of rows and columns visible in the application, and makes a cell editable or not as a response to key press.

PeopleImageViews
Controls the image view for the contacts and extends itself by adding a "drag image" support that responds to the user's actions in the People application window.

PeopleSchemaExtension.xcodeproj - Description

This is a brief description of the files contained in the PeopleSchemaExtension.xcodeproj file.

PeopleSchemaExtension_Prefix.pch
Contains the prefix header for the source filer of the PeopleSchemaExtension target in the PeopleSchemaExtension project.

Schema-strings
Defines the constants that define the schema for PeopleSchemaExtension.

Note: .plist files contain specific schemas and structures for the client and the application. These files help visualize the way in which data is accessed and stored. A a recommendation, go over the schemas and .plist files to get a broad idea of the project.

Other Resources

• Introduction to Sync Services Programming Guide
• Introduction to Sync Services Tutorial
```

[Next](main.m.md)[Previous](People.md)

