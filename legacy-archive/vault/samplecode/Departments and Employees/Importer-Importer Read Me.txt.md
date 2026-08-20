---
title: Departments and Employees
apple_id: DTS10004314
resource_type: Sample Code
platform: macOS
topic: Data Management
technology: CoreData
published: '2007-05-31'
source_url: https://developer.apple.com/library/archive/samplecode/DepartmentAndEmployees/Listings/Importer_Importer_Read_Me_txt.html
archived_at: '2026-07-18T03:06:39.485386Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [Departments and Employees](Departments%20and%20Employees.md)


[Next](Importer-main.c.md)[Previous](Importer-GetMetadataForFile.c.md)

# Importer/Importer Read Me.txt

```

//==============================================================================
// Core Data Document-based Application Spotlight Importer
//==============================================================================

Spotlight importers should be provided by all applications that support custom 
document formats. A Spotlight importer parses your document format for relevant 
information and assigning that information to the appropriate metadata keys.

The bundle target in this project creates a Spotlight importer bundle installed 
inside of the wrapper of the application target.  This bundle includes all of 
the code necessary to import the metadata information from Core Data stores.
The only default metadata for a Core Data store is the store ID and store type,
neither of which is imported.  To have metadata from your stores imported, you
must first add the information you are interested to the metadata for your 
store (see the NSPersistentStoreCoordinator setMetadataForPersistentStore: API)
and then pull the information for import in the GetMetadataForFile function in
the 'GetMetadataForFile.c' file.

Additionally, the importer must contain a list of the Uniform Type Identifiers
(UTI) for your application in order to import the data.  (The UTI information is
used by Spotlight to know which importer to invoke for a given file.)  If the
UTI is not already registered by your application, you will need to register it
in the importer bundle.  (For more information on registering UTIs for
applications, consult the documentation at http://developer.apple.com)

-----------------------------------------------------------------------------

To set UTI types the bundle will import:

1) Open the "Targets" group to display the targets for the project

2) Double-click on the icon for the importer target to bring up the target
   inspector, and select the "Properties" tab

3) At the bottom of the inspector, click the "Open Info.plist as File"
   button at the bottom of the pane to display the Info.plist

4) Modify the CFBundleDocumentTypes entry to contain an array of Uniform Type 
   Identifiers (UTI) for the LSItemContentTypes your importer can handle

-----------------------------------------------------------------------------
```

[Next](Importer-main.c.md)[Previous](Importer-GetMetadataForFile.c.md)

