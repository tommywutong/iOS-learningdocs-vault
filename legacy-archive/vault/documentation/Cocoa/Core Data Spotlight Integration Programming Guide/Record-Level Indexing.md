---
title: Core Data Spotlight Integration Programming Guide
apple_id: TP40008065
resource_type: Guide
platform: macOS
topic: Data Management
technology: CoreData
published: '2012-07-23'
source_url: https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/SpotlightCoreData/Articles/recordLevel.html
archived_at: '2026-07-15T07:19:21.181010Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Core Data Spotlight Integration Programming Guide](Introduction.md)


[Next](Document%20Revision%20History.md)[Previous](Store%20Metadata-Level%20Indexing.md)

# Record-Level Indexing

For non-document-based programs, you can create Spotlight indexes where each record is indexed individually.

You can create Spotlight indexes where each record is indexed individually. This feature is only supported in non-document-based applications. For document-based applications, you should use store metadata as described in [Store Metadata-Level Indexing](Store%20Metadata-Level%20Indexing.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4danrvfvbuqmjqgawvgvzr).

In this approach, Core Data manages a directory in the Library/Caches/Metadata/Core Data/ in a user’s home directory (the structure of this directory is private—don’t depend on it). For each separate program, Core Data creates a subdirectory; within each subdirectory Core Data creates a further subdirectory for each persistent store used by the program. Within the directory for a given store, for each instance of each entity that you choose to index, Core Data creates a new _external record file_. The external record files are used by Spotlight to index the persistent store.

There are three processes involved in creating and maintaining the Spotlight index:

- Your program.

  Within your program, the Core Data framework maintains the persistent store and creates the external record files to trigger the spotlight indexing
- The Spotlight importer.

  The importer does the actual indexing. It is launched whenever an external record changes.

  You have to write and maintain the importer; for every external record, it needs to add suitable data to the Spotlight index. This is in many respects the most important part of developing the importer.
- Core Data External Record daemon.

  This is a secondary process used by the Core Data framework. It is used to improve performance if you modify a large number of records (more than a hundred or so) at the same time. In this situation, Core Data writes a single work file which the external daemon subsequently unpacks to create individual external records.

The main purpose of the external record file is simply to serve as a pointer to a record (an instance of an entity) in a persistent store. In the importer, you fetch a corresponding managed object from your application’s persistent store and use it to update the Spotlight index.

Provided that at least one property for an entity is specified as being indexed (see [Configuring the Model](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4danrvfvbuqmjqgewvgvzv)), then whenever a change to an instance of that entity is committed to the persistent store, the corresponding external record file is updated (minimally the last modification date changed). The external record file may be empty (a zero-length file), however you can also, optionally, specify properties whose values Core Data should store in the file. The importer does not use any data you may have specified should be stored in the external record itself (to understand how you might use it, see [Using External Records](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4danrvfvbuqmjqgewvgvzrga)).

When you create a new project with Xcode, choose a non-document-based application that uses Core Data for storage and has Spotlight Indexing (“Core Data Application with Spotlight Importer”). The Xcode template adds the Importer files and creates a build target for the importer. There are then two targets that you have to manage—the application and the importer. They both share a common managed object model.

To enable Spotlight indexing, you need to specify which properties of which entities should be indexed and which—if any—of those properties should be added to the external record.

In Configuration inspector, for each of the properties that you want to be indexed, select:

- Index in Spotlight
- (Optional) Store in external record file

Provided that at least one property for an entity has the “Index in Spotlight” flag set, then whenever a change to an instance of that entity is committed to the persistent store, the corresponding external record file is updated (minimally the last modification date changed). This means that the Spotlight importer will run and so the Spotlight index will be updated with new data.

If you only choose “Index in Spotlight,” Core Data just creates a zero-length file for the corresponding record. If you also select “Store in External Record”, the property is added to the contents of the external record. Simple types, such as strings, dates, and numbers, are exported directly; relationships are stored as UUIDs.

The importer does not itself use any data you may have specified should be stored in the external record. You may, however, want to use the external records yourself, for example for error recovery or to assist debugging—see [Using External Records](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4danrvfvbuqmjqgewvgvzrga). Unless you do, though, to avoid the overhead of duplicating data and taking up space on disk, you should not choose to store property values in the external record.

There are several options you can set for the store to specify where the external records should be stored, the extension for the external record file names, and the format in which the external records should be written:

**`NSExternalRecordsDirectoryOption`**
: This constant specifies the directory URL where the external records are stored.

You must specify a directory in the user’s `Library/Caches/Metadata/CoreData` or `Library/CoreData` directory. You must use this in conjunction with the `NSExternalRecordsExtensionOption` option.

**`NSExternalRecordExtensionOption`**
: This constant specifies the extension used for the external record files.

You must use this in conjunction with the `NSExternalRecordsDirectoryOption` option.

**`NSExternalRecordsFileFormatOption`**
: This constant specifies the file format to use when writing external records.

The default is to write the records as XML (`NSXMLExternalRecordType`)—this is a good choice if you want a human-readable format, or want to be able to share content with other applications. Otherwise you should typically use the binary format (`NSBinaryExternalRecordType`).

You set these options when you configure the persistent store coordinator, as shown in the following example:

```
NSString *externalRecordsSupportFolder = <#Path for records folder#>;
NSURL *storeURL = <#URL for the store#>;

NSMutableDictionary *storeOptions = @{
    NSExternalRecordExtensionOption:@"MyExtension",
    NSExternalRecordsDirectoryOption:externalRecordsSupportFolder,
    NSExternalRecordsFileFormatOption:NSBinaryExternalRecordType};

NSPersistentStoreCoordinator *aPSC = <#Get the coordinator#>;.
if (![aPSC addPersistentStoreWithType:NSSQLiteStoreType configuration:nil URL:storeURL
           options:storeOptions error:&error]) {
    [[NSApplication sharedApplication] presentError:error];
}
```


This section describes primarily the features of an importer that are unique to Core Data. To understand the fundamentals of how to implement a Spotlight importer, you should read _[Spotlight Importer Programming Guide](../../Carbon/Spotlight%20Importer%20Programming%20Guide/About%20Spotlight%20Importers.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytenrx)_. Note also that most of the configuration and implementation details are discussed in the Importer ReadMe file and provided as comments in the templates.

Broadly speaking, there are two aspects to implementing the importer: configuring the project settings, for example, the file extension for your external record type; and customizing the method that adds data from a record to the Spotlight index. The latter aspect is probably the most important aspect of the task.

First, if you’re using a custom store type, you have to link the custom store class into your project. Then there are three additional settings that you need to configure:

- The extension for external record file.

  In the template, this is given as `YOUR_EXTERNAL_RECORD_EXTENSION`; you have to provide a custom extension for your file type (for example, `myFileType`). This is a `#define`, so you can just use:

```
#define YOUR_EXTERNAL_RECORD_EXTENSION @"myFileType"
```

  and leave `define`d constant intact throughout the project.
- A UTI for your record files.

  In the template, this is given as `YOUR_EXTERNAL_RECORD_EXTENSION`; you have to provide a custom UTI for your type (for example, `mycompany.mytype1`). This is a string literal in several files (info.plist), so you have to change each occurrence.
- The store type.

  In `MySpotlightImporter.m`, you need to define the type of the persistent store your program creates. By default, it’s specifies as the XML store type:

```
#define YOUR_STORE_TYPE NSXMLStoreType
```

You need to specify the extension and UTI for records in the project’s plist files. If you define your own UTI, you specify it in the Importer-Info.plist file. For details, see _[Spotlight Importer Programming Guide](../../Carbon/Spotlight%20Importer%20Programming%20Guide/About%20Spotlight%20Importers.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytenrx)_.

The goal of the importer is to add to the Spotlight index chosen properties from a record identified by an external record file. Most of the code is provided by the project template, and—aside from the configuration outlined in [Project Configuration](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4danrvfvbuqmjqgewvgvzrge)—there should be little need to modify the implementation of any of the methods other than:

```objc
- (BOOL)importFileAtPath:(NSString *)filePath attributes:(NSMutableDictionary *)spotlightData error:(NSError **)error
```

This is the method that actually fetches a managed object for the record and adds appropriate key-value pairs to the `spotlightData` dictionary to be added to the Spotlight index. The template code retrieves the managed object; you have to write the code to add key-value pairs to the `spotlightData` dictionary.

The `path` argument of `importFileAtPath:attributes:error:` is the path to an external record file. Using this path, the `NSPersistentStoreCoordinator` class can retrieve information about the record:

```
NSDictionary *pathInfo = [NSPersistentStoreCoordinator elementsDerivedFromExternalRecordURL:[NSURL fileURLWithPath:filePath]];
```

There are three pieces of information the importer needs from the record:

- The URL for the managed object model
- The URL for the persistent store
- The URI for the record itself

```
self.modelURL = [NSURL fileURLWithPath:[pathInfo valueForKey:NSModelPathKey]];
self.storeURL = [NSURL fileURLWithPath:[pathInfo valueForKey:NSStorePathKey]];
NSURL *objectURI = [pathInfo valueForKey:NSObjectURIKey];
```

Given these, the importer can create the Core Data stack and the object ID for the appropriate managed object, and so retrieve the managed object:

```
NSManagedObject *instance = [[self managedObjectContext] objectWithID:oid];
```

Given the managed object, you can update the Spotlight index data.

In general, though, you adopt the following pattern: For each entity, you:

1. Set a display string for the record
2. Iterate through the managed object’s attributes and relationships, adding suitable entries to the Spotlight data dictionary.

First, you set display string (the string that Spotlight displays for the record in the search results menu):

```
NSString *displayString = <#Create a display string from a managed object#>;
[spotlightData setObject:displayString forKey:(__bridge id<NSCopying>)kMDItemDisplayName];
```

You then iterate through the attributes and relationships for the managed object. For each property that you marked as to be indexed ([Configuring the Model](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4danrvfvbuqmjqgewvgvzv)), you add a suitable entry to the `spotlightData` dictionary. For each entry, you choose a suitable metadata attribute key (for example, `kMDItemTextContent`—see [MDItemRef](https://developer.apple.com/documentation/coreservices/mditemref) for a list of attribute keys that are common to many file types) and an appropriate representation of the value:

It’s up to you to determine how the transform the hierarchically-organized data in your application into a representation suitable for the Spotlight index. _You must consider relationships between entities._ For example, given an application that has Person and Address entities, and a to-many relationship from Person to Address, you might:

- In the Person entity, flatten the relationship to Address and just index the Person entity.

  In this case, users will be able to find a person using any of the addresses to which they have a relationship.
- In the Address entity, flatten the relationship to Person and just index the Address entity.

  In this case, users will only be able to find a person if they also have an associated address.
- In the Address entity, flatten the relationship to Person and index both the Address and Person entities.

When you do flatten a relationship, you need to consider how the source object will be updated if the destination changes. For example, if you change just the Zip code of a person’s address, how should this change be noticed in your application and propagated to the Spotlight index (if at all)?

The most important aspect of developing your importer is deciding how to import each entity. You can use the following approach to avoid the need to use multiple conditional statements within the `importFileAtPath:attributes:error:` method and instead focus on each entity individually.

In `importFileAtPath:attributes:error:`, you can create an [NSInvocation](https://developer.apple.com/documentation/foundation/nsinvocation) object that sends a message to `self`, where the selector follows the format `import<EntityName>:attributes:` and the method returns a `BOOL` value that indicates whether the import was successful. For each imported entity, you then implement a method of the form:

```objc
- (BOOL)import<EntityName>:(EntityClass *)instance
                attributes:(NSMutableDictionary *)spotlightData
```

The `importFileAtPath:attributes:error:` method determines the entity name of the current record, and constructs a suitable `NSInvocation` object:

```objc
- (BOOL)importFileAtPath:(NSString *)filePath attributes:(NSMutableDictionary *)spotlightData error:(NSError **)error {

    NSDictionary *pathInfo =
        [NSPersistentStoreCoordinator elementsDerivedFromExternalRecordURL:
                                            [NSURL fileURLWithPath:filePath]];

    NSString *entityName = [pathInfo objectForKey:NSEntityNameInPathKey];

    self.modelURL = [NSURL fileURLWithPath:[pathInfo valueForKey:NSModelPathKey]];
    self.storeURL = [NSURL fileURLWithPath:[pathInfo valueForKey:NSStorePathKey]];

    NSURL  *objectURI = [pathInfo valueForKey:NSObjectURIKey];
    NSManagedObjectID *oid =
        [[self persistentStoreCoordinator] managedObjectIDForURIRepresentation:objectURI];

    if (!oid) {
        NSLog(@"%@:%s to find object id from path %@", [self class], _cmd, filePath);
        return NO;
    }

    /*
     Create and invoke an NSInvocation object that sends a message to self where:
         The selector follows the format import<EntityName>:attributes:
         The return value is a BOOL.
    */

    NSString *importSelectorString =
        [NSString stringWithFormat:@"import%@:attributes:", entityName];
    SEL importSelector = NSSelectorFromString(importSelectorString);
    if (![self respondsToSelector:importSelector]) {
        NSLog(@"%@:%s Couldn't import an instance of entity %@",
            [self class], _cmd, entityName);
        return NO;
    }

    NSManagedObject *instance = [[self managedObjectContext] objectWithID:oid];

    NSMethodSignature *methodSignature = [self methodSignatureForSelector:importSelector];
    NSInvocation *invocation =
        [NSInvocation invocationWithMethodSignature:methodSignature];
    [invocation setTarget:self];
    [invocation setSelector:importSelector];
    [invocation setArgument:&instance atIndex:2];
    [invocation setArgument:&spotlightData atIndex:3];

    BOOL returnValue;
    [invocation invoke];
    [invocation getReturnValue:&returnValue];
    return returnValue;
}
```

Given the preceding implementation of `importFileAtPath:attributes:error:`, suppose you have a model that contains two entities, Person and Address, and that there is a to-many relationship from Person to Address. You might implement the method to import instances of the Person entity as follows:

```objc
- (BOOL)importPerson:(Person *)person attributes:(NSMutableDictionary *)spotlightData {

    // Set the display name for Spotlight search results.
    [spotlightData setObject:[person fullName] forKey:(__bridge id<NSCopying>)kMDItemDisplayName];

    NSDate *dob = person.dateOfBirth;
    if (dob != nil) {
        [spotlightData setObject:dob forKey:(__bridge id<NSCopying>)kMDItemTimestamp];
    }

    NSMutableString *text = [NSMutableString stringWithFormat:@"%@", [person fullName]];

    for (NSManagedObject *address in person.addresses) {

        NSString *component;

        component = [address street1];
        if (component) {
            [text appendFormat:@" %@", component];
        }
        component = [address city];
        if (component) {
            [text appendFormat:@" %@", component];
        }
        component = [address state];
        if (component) {
            [text appendFormat:@" %@", component];
        }
        component = [address zip];
        if (component) {
            [text appendFormat:@" %@", component];
        }
    }

    [spotlightData setObject:text forKey:(__bridge id<NSCopying>)kMDItemTextContent];
    return YES;
}
```


The final aspect of supporting Spotlight integration is to display the appropriate record when the user makes a selection after a Spotlight search. You have to implement the application delegate method [application:openFiles:](https://developer.apple.com/documentation/appkit/nsapplicationdelegate/1428742-application) to respond to an open file request for an external record:

```objc
- (void)application:(NSApplication *)theApplication openFiles:(NSArray *)files {

    NSString *aPath = [files lastObject]; // Just an example to get at one of the paths.

    if (aPath && [aPath hasSuffix:YOUR_EXTERNAL_RECORD_EXTENSION]) {
        // Decode URI from path.
        NSURL *objectURI = [[NSPersistentStoreCoordinator elementsDerivedFromExternalRecordURL:[NSURL fileURLWithPath:aPath]] objectForKey:NSObjectURIKey];
        if (objectURI) {
            NSManagedObjectID *moid = [[self persistentStoreCoordinator] managedObjectIDForURIRepresentation:objectURI];
            if (moid) {
                    NSManagedObject *mo = [[self managedObjectContext] objectWithID:moid];

                    // Your code to select the object in your application's UI.
            }
        }
    }
}
```

The template shows how to identify the managed object that the user selected. How you then ensure that this object is displayed in the user interface is dependent entirely upon your application architecture and the schema in your managed object model.

The importer does not use any data you may have specified should be stored in the external record itself (see [Overview](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4danrvfvbuqmjqgewvgvzt)). In other programs, however, you can use the following `NSPersistentStoreCoordinator` methods to interact with external records:

- [elementsDerivedFromExternalRecordURL:](https://developer.apple.com/documentation/coredata/nspersistentstorecoordinator/1468919-elementsderived) is a class method that takes a URL to an external record file and returns a dictionary with the derived elements such as the name of the entity and the URI for the managed object instance.
- [importStoreWithIdentifier:fromExternalRecordsDirectory:toURL:options:withType:error:](https://developer.apple.com/documentation/coredata/nspersistentstorecoordinator/1468788-importstore) creates and populates a new store using external records found at a specified location.

In some circumstances, therefore, you could use the external record for example for error recovery or to recreate a store that has somehow become corrupted. You might also use the XML representation to allow data exchange with other programs. It’s up to you to decide what information might be useful and in what situations you might use this data, and so which properties of which entities you want to include in the external record.

The structure of the external records directory is not guaranteed to remain constant between releases of the operating system. You can, though, regardless of their layout, simply iterate through the external records directories (for example, using `NSFileManager`’s [enumeratorAtPath:](https://developer.apple.com/documentation/foundation/filemanager/1408726-enumerator)) to retrieve all the files whose path extension is that which you specified for your external records.

You can also use the external records as a diagnostic when you are developing your program and the importer. You can ensure that the correct information is being added to the records, and that they’re being updated when you expect them to be—although note the caveat in [Why aren’t my records in sync?](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4danrvfvbuqmjqgewvgvzz).

Many hints for troubleshooting are given in the _[Spotlight Importer Programming Guide](../../Carbon/Spotlight%20Importer%20Programming%20Guide/About%20Spotlight%20Importers.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytenrx)_. In particular, you can test your importer using `/usr/bin/mdimport`, as illustrated by this example:

```
/usr/bin/mdimport -d2 ~/Library/Caches/Metadata/CoreData/$ApplicationName/$StoreID/$Entity/$fileName
```


To test your importer, create a link from the Spotlight plugins directory (`/Library/Spotlight`) to the newly-built importer, or copy the importer to the `/Library/Spotlight` directory.

_The default project includes the Spotlight importer as an application resource_; if you want to test the importer from the /Library/Spotlight directory, make sure that you remove the importer from the application.

When you use `/usr/bin/mdimport` in debug mode, it reports which importer it uses. Check the path carefully.

If the importer can’t find a custom class, make sure that you added it to the importer target in Xcode.

If the importer can’t find custom methods, recall that the default template sets the managed object class for entities to `NSManagedObject`; you can skip entities for which you do want to use your custom class:

```
// Clear out all custom classes used by the model to avoid having to link them
// with the importer. Remove this code if you need to access your custom logic.
NSString *managedObjectClassName = [NSManagedObject className];
for (NSEntityDescription *entity in managedObjectModel) {
    if (![[entity name] isEqualToString:@"Person"]) {
        [entity setManagedObjectClassName:managedObjectClassName];
    }
}
```


If Spotlight isn’t using your importer, make sure that you set the UTI consistently throughout the project.

Recall also that letters in the UTI must all be lowercase.

The process is generally very efficient. Much of the work is offloaded to background processes, so your program is not directly impacted. If you save a large number of records (more than a hundred or so), Core Data writes a single work file which it subsequently unpacks to create individual files. Sometimes, however, external records may temporarily become out-of-sync with the persistent store—see [Why aren’t my records in sync?](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4danrvfvbuqmjqgewvgvzz).

As is the case with any Spotlight-related process, the index is not guaranteed to always immediately reflect what's in the source (the persistent store). As described in [Overview](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4danrvfvbuqmjqgewvgvzt), there are three processes that manage data—your program, the importer, and the Core Data daemon—all of which run concurrently. If you create a few hundred new records, the importer should be able to keep up. If you update and delete a larger number of records, however, it's possible that things will get temporarily out of sync.

There are a couple of other issues that you need to bear in mind—particularly relevant during development:

- If you change your model or the file format, external records will not be updated until the source record is modified.
- If you delete an entity from your model, the external record directory for that entity will not be deleted.

If necessary, you can cause an entire store to be reindexed (and so all the external records to be recreated) simply by deleting the corresponding external record directory.

[Next](Document%20Revision%20History.md)[Previous](Store%20Metadata-Level%20Indexing.md)

