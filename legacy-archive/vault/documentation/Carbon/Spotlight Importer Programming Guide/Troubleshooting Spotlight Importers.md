---
title: Spotlight Importer Programming Guide
apple_id: TP40001267
resource_type: Guide
platform: macOS
topic: Data Management
technology: CoreServices
published: '2013-08-08'
source_url: https://developer.apple.com/library/archive/documentation/Carbon/Conceptual/MDImporters/Concepts/Troubleshooting.html
archived_at: '2026-07-15T05:23:21.329442Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Spotlight Importer Programming Guide](About%20Spotlight%20Importers.md)


[Next](Document%20Revision%20History.md)[Previous](Spotlight%20Importer%20Performance.md)

# Troubleshooting Spotlight Importers

Rare is the project that is flawless from the start. Troubleshooting a Spotlight importer can be difficult given that it is run by the system automatically as required and is run outside the development environment.

This article describes how to explicitly run your metadata importer for testing and provides a number of techniques for troubleshooting problems.

An application’s Spotlight importer resides within the application’s bundle in the subdirectory `MyApp.app/Contents/Library/Spotlight`. Standalone importers can be installed in one of the following locations:

```
~/Library/Spotlight
/Library/Spotlight
```

If your importer is not part of an application bundle, create an installer package that installs the importer in one of the above locations. To have existing files imported, you need to have a `postinstall` script for your installer that includes the following command, specifying your importer installation location:

```
/usr/bin/mdimport -r InstallDirectory/YourPlug-In
```


When a user first runs your application, the Spotlight importer is found and Spotlight begins importing any existing files. If you update your application and the Spotlight importer, make sure that the importer bundle has a different date stamp. When the updated application is run for the first time Spotlight reindexes the existing files with the new importer.

Running the `mdimport` command (located in `/usr/bin`) with the `-L` option returns a list of all the currently recognized importers and their paths.

```
/usr/bin/mdimport -L
```

```
2005-01-16 02:56:37.634 mdimport[673] Paths: id(501) (
    "/System/Library/Spotlight/RichText.mdimporter",
    "/System/Library/Spotlight/Image.mdimporter",
    "/System/Library/Spotlight/Audio.mdimporter",
    "/System/Library/Spotlight/Font.mdimporter",
    "/System/Library/Spotlight/PDF.mdimporter",
    "/System/Library/Spotlight/Chat.mdimporter",
    "/System/Library/Spotlight/iCal.mdimporter",
    "/System/Library/Spotlight/Mail.mdimporter",
    "/System/Library/Spotlight/QuickTime.mdimporter",
    "/System/Library/Spotlight/vCard.mdimporter",
    "/Users/me/Library/Spotlight/MyCustomImporter.mdimporter",
    "/System/Library/Spotlight/QuartzComposer.mdimporter",
    "/System/Library/Spotlight/PS.mdimporter",
    "/System/Library/Spotlight/SystemPrefs.mdimporter",
    "/System/Library/Spotlight/Application.mdimporter"
)
```


If your importer resides within your application’s wrapper, it may not be found automatically during testing. Importers are detected when the bundle’s modification date is changed. You can explicitly register your application by specifying the `-f` flag to `lsregister`. The `lsregister` tool is found in `/System/Library/Frameworks/CoreServices.framework/Frameworks/LaunchServices.framework/Versions/A/Support/` on OS X v10.5 and later.

```
lsregister -f MyApp.app
```

Another possibility is that your application may be untrusted. Spotlight importers are not loaded from untrusted applications. Launching the application for the first time causes the application to be trusted.

New Spotlight importers are detected by comparing the importer’s modification date. If the date is the same as a previously loaded importer, the new importer is not automatically detected. If you copy the updated importer to the Spotlight directory using `cp -r`, the change is not noted by Spotlight. The solution is to either remove the existing importer before copying the updated version, or use the `touch` command on the importer `.mdimporter` directory to explicitly update the date.

You can test your Spotlight importer using the `mdimport` command (located in `/usr/bin`). Run `mdimport` with the debug level set to 2 and specify a file that you can import data from:

```
/usr/bin/mdimport -d2 test.myCustomDocument
```

This command produces out like this:

```
2005-01-16 02:59:04.930 mdimport[678] Import '/Users/me/Documents/test.myCustomDocument'
type 'com.apple.mycocoadocumentapp.mycustomdocument'
using 'file://localhost/Users/me/Library/Spotlight/MyCustomImporter.mdimporter/'
2005-01-16 02:59:04.931 mdimport[678] Sending attributes
of '/Users/me/Documents/test.myCustomDocument' to server.
Attributes: '{
    "_kMDItemImporterCrashed" = <null>;
    "com_apple_metadata_modtime" = 127555123.1940155;
    "com_apple_myCocoaDocumentApp_myCustomDocument_notes" = "Remember to feed the cats!";
    kMDItemAuthors = ("Tori”,”Simon",”Daniel”);
    kMDItemContentType = "com.apple.mycocoadocumentapp.mycustomdocument";
    kMDItemContentTypeTree = ("com.apple.mycocoadocumentapp.mycustomdocument", "public.data", "public.item");
    kMDItemDisplayName = {"" = "test.myCustomDocument"; };
    kMDItemKind = {en = DocumentType; };
    kMDItemTitle = "Be sure to remember to...";
}'
```

The first line of the output indicates the file that is being imported, as well as the UTI that the file maps to. The remaining lines list the attribute keys and values that were imported from the file.

You should ensure that all the appropriate metadata keys that your importer returns are present in the output. You'll notice that a number of metadata keys specific to the file system are also available for each file. These are provided by the metadata system and are not your responsibility.

You can debug your importer by running `mdimport` under `gdb`.

The following command loads `mdimport` under `gdb`:

```
gdb mdimport
```

After `mdimport` has started, set a breakpoint on your import function:

```
b MyImporterGetAttributesFromFileFunction
```

Then start the `mdimport` process, specifying the file to import:

```
r /path/to/my/test/file
```


You can determine the UTI that the system thinks belongs to your file by using the `mdimport` command with a debug level of 1:

```
/usr/bin/mdimport -d1 test.myCustomDocument
```

The output shows the UTI type that the system has determined for the file:

```
 2005-01-16 03:00:07.212 mdimport[683] Import '/Users/me/Documents/ test.myCustomDocument'
 type 'com.apple.mycocoadocumentapp.mycustomdocument'  using
'file://localhost/Users/me/Library/Spotlight/MyCustomImporter.mdimporter/'
```

The type should match the UTI that your importer supports.

If running `mdimport` with a debug level of 1 returns no output, you should ensure that the file you're attempting to import is not in the `/tmp` directory or some other System directory. Files in those locations are not imported.

If running `mdimport` returns a UTI other than one you expect, you'll need to ensure that the file you're attempting to import is actually the type of file you think it is. The UTI of a file is determined by the extension or file type.

It is also possible that a dynamic UTI is returned:

```
2005-01-16 03:01:16.989 mdimport[691] Import '/Users/me/Documents/test.myCustomDocument'
 type 'dyn.ah62d4rv4ge8048pdsz31k55rqv10g7prqz1hkqu' no mdimporter
```

Typically, the return of a dynamic UTI indicates that the file is not mapping to a known UTI. You should check that:

1. The test file is the correct file type.
2. The test file has the correct filename extension or file type set.
3. If your application is declaring the UTI type for the file, that the application’s `Info.plist` file has the correct entries in the `UTExportedTypeDeclarations` entry as shown here:

```
    <key>UTExportedTypeDeclarations</key>
    <array>
        <dict>
            <key>UTTypeConformsTo</key>
            <array>
                <string>public.data</string>
            </array>
            <key>UTTypeDescription</key>
            <string>My Document Type</string>
            <key>UTTypeIdentifier</key>
            <string>com.apple.mycocoadocumentapp.mycustomdocument</string>
            <key>UTTypeTagSpecification</key>
            <dict>
                <key>public.filename-extension</key>
                <array>
                    <string>myCustomDocument</string>
                </array>
            <key>com.apple.ostype</key>
            <string>T78q</string>
            </dict>
        </dict>
    </array>
```
4. Ensure that your application lives in a location where Launch Services can detect the mappings. Running the application also ensures that the mappings are made.

If running `mdimport` with a debug level of 3 does not list any of your custom metadata attributes, you should check that:

1. Your metadata importer is being found using the `mdimport -L` command.
2. Your metadata importer's `Info.plist` file has the correct plug-in type for metadata importers in the `CFPlugInTypes` entry. The key should be `8B08C4BF-415B-11D8-B3F9-0003936726FC`:

```
    <key>CFPlugInTypes</key>
    <dict>
        <key>8B08C4BF-415B-11D8-B3F9-0003936726FC</key>
        <array>
            <string>8AED83B3-C412-11D8-85A3-000393D59866</string>
        </array>
    </dict>
```
3. The UUID that you created for your importer is unique and is in both the `CFPlugInFactories` and `CFPluginTypes` entries of the importer's `Info.plist` file. Here, the UUID is `8AED83B3-C412-11D8-85A3-000393D59866`:

```
    <key>CFPlugInFactories</key>
    <dict>
        <key>8AED83B3-C412-11D8-85A3-000393D59866</key>
        <string>MetadataImporterPluginFactory</string>
    </dict>
    <key>CFPlugInTypes</key>
    <dict>
        <key>8B08C4BF-415B-11D8-B3F9-0003936726FC</key>
        <array>
            <string>8AED83B3-C412-11D8-85A3-000393D59866</string>
        </array>
    </dict>
```
4. You have the correct UTI type for your importer listed in the `LSItemContentTypes` entry in the importer’s `Info.plist` file:

```
    <key>CFBundleDocumentTypes</key>
    <array>
        <dict>
            <key>CFBundleTypeRole</key>
            <string>MDImporter</string>
            <key>LSItemContentTypes</key>
            <array>
                <string>com.apple.mycocoadocumentapp.mycustomdocument</string>
            </array>
        </dict>
    </array>
```
5. Your UTI is all lowercase in the `Info.plist` and the `schema.xml` files.
6. If your importer reads metadata from a file bundle, ensure that the `UTTypeConformsTo` entry in the importer's `Info.plist` file includes `com.apple.package` as the file UTI.
7. Your `schema.xml` file is valid.

   You can test whether your `schema.xml` file is well formed by running the command `mdcheckschema` (located in `/usr/bin`).

```
/usr/bin/mdcheckschema ~/Library/Spotlight/MyCustomImporter.mdimporter/Contents/Resources/schema.xml
```

```
/Users/me/Library/Spotlight/MyCustomImporter.mdimporter/Contents/Resources/schema.xml : succesfully parsed.
```
8. Your implementation of `GetMetadataForFile` is populating the dictionary with the correct metadata entries and is returning `true`.
9. You return only CFTypes of CFString, CFNumber, CFBoolean, and CFDate as attribute values. If an attribute is specified as multivalued, you must return a CFArray of the expected CFType.

You can determine the metadata attributes and values in the system store for a file by using the `mdls` command:

```
mdls /Applications/iTunes.app
```

```
/Applications/iTunes.app -------------
kMDItemAttributeChangeDate = 2005-01-16 03:03:14 -0500
kMDItemContentType         = "com.apple.application-bundle"
kMDItemContentTypeTree     = (
    "com.apple.application-bundle",
    "com.apple.application",
    "public.executable",
    "com.apple.bundle",
    "public.directory",
    "public.item",
    "com.apple.package"
)
kMDItemCopyright           = "iTunes 4.7, Copyright 2000-2004 Apple Computer, Inc."
kMDItemDisplayName         = "iTunes"
kMDItemFSContentChangeDate = 2005-01-08 18:17:52 -0500
kMDItemFSCreationDate      = 2005-01-08 18:17:52 -0500
kMDItemFSCreatorCode       = 0
kMDItemFSFinderFlags       = 0
kMDItemFSInvisible         = 0
kMDItemFSLabel             = 0
kMDItemFSName              = "iTunes.app"
kMDItemFSNodeCount         = 1
kMDItemFSOwnerGroupID      = 80
kMDItemFSOwnerUserID       = 0
kMDItemFSSize              = 0
kMDItemFSTypeCode          = 0
kMDItemID                  = 64286
kMDItemKind                = "Application"
kMDItemLastUsedDate        = 2005-01-16 01:01:10 -0500
kMDItemUsedDates           = (
    2005-01-08 18:17:52 -0500,
    2005-01-13 19:00:00 -0500,
    2005-01-15 19:00:00 -0500
)
kMDItemVersion             = "4.7"
```

You can also specify a specific metadata attribute to return the value of:

```
mdls -name kMDItemContentType /Applications/iTunes.app
```

```
/Applications/iTunes.app -------------
kMDItemContentType = "com.apple.application-bundle"
```


If your application saves its files as a bundle, you must take precautions to ensure that Spotlight doesn’t attempt to import your file bundle before all the data is written to the bundle.

See [Spotlight and Document Bundles](https://developer.apple.com/library/archive/documentation/Carbon/Conceptual/MetadataIntro/Concepts/DocumentBundles.html#//apple_ref/doc/uid/TP40002007) for additional details.

[Next](Document%20Revision%20History.md)[Previous](Spotlight%20Importer%20Performance.md)

