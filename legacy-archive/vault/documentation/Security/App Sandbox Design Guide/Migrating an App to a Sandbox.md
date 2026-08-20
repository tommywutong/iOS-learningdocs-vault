---
title: App Sandbox Design Guide
apple_id: TP40011183
resource_type: Guide
platform: macOS
topic: Security
technology: null
published: '2016-09-13'
source_url: https://developer.apple.com/library/archive/documentation/Security/Conceptual/AppSandboxDesignGuide/MigratingALegacyApp/MigratingAnAppToASandbox.html
archived_at: '2026-07-27T06:57:08.399198Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [App Sandbox Design Guide](About%20App%20Sandbox.md)


[Next](App%20Sandbox%20Checklist.md)[Previous](Designing%20for%20App%20Sandbox.md)

# Migrating an App to a Sandbox

An app that is not sandboxed places its support files in locations that are inaccessible to a sandboxed version of the same app. For example, whereas a non-sandboxed app might store files in `~/Library/Application Support/<bundle_id>`, the sandboxed version of the same app does not have access to that directory. Instead, the sandbox location for the `Application Support` directory (obtained using the [NSFileManager](https://developer.apple.com/documentation/foundation/filemanager) method [URLForDirectory:inDomain:appropriateForURL:create:error:](https://developer.apple.com/documentation/foundation/filemanager/1407693-url)) is within the app’s container, typically found at `~/Library/Containers/<bundle_id>`.

If you previously distributed your app without sandboxing and you now want to provide a sandboxed version, you must tell macOS to move your support files into their new, sandbox-accessible locations.

__Note:__ The system automatically migrates your app’s preferences file (`~/Library/Preferences/<bundle_id>.plist`) on first launch of your sandboxed app. You do not need to explicitly request that it be migrated.

## The Migration Process

When a user launches any app, before the app starts running, macOS checks to see if the app is sandboxed. If so, macOS checks to see if a sandbox container directory exists for that app within the user’s `Library/Containers` folder. If a container directory already exists, then no migration is needed, and the app begins running immediately.

However, if the app’s container directory does not exist, macOS creates it and then migrates the per-user preference file for the app. macOS then carries out any additional migration actions specified in the app's _container migration manifest_.

A _container migration manifest_ is a special [property list](https://developer.apple.com/library/archive/documentation/General/Conceptual/DevPedia-CocoaCore/PropertyList.html#//apple_ref/doc/uid/TP40008195-CH44) file you use to specify certain actions macOS should perform the first time the user launches the sandboxed version of your app. The file must be named `container-migration.plist`, and must appear in the `Contents/Resources` directory within your app bundle. You include certain properties to describe the migration actions you wish to perform:

- Use the `Move` property to move files or directories (for example, your app’s `Application Support` directory) from their legacy location into your container.

  This property contains an array of objects specifying the files and directories you want to move. For each item, you have a choice of allowing the system to place the item appropriately in your container (by indicating the item’s source location using a string) or explicitly specifying the destination location (by indicating both the source and destination locations in an array of two strings).

  macOS moves—it does not copy—the files and directories you specify. That is, the files and directories migrated into your app’s container no longer exist at their original locations. Directories are moved recursively.
- Use the `Symlink` property to create symbolic links inside your new container to files outside of it.

  __Note:__ For symbolic links to be useful, you must combine them with temporary exception entitlements to grant access to whatever files or folders the symbolic links point to.
- Use the `MigrateScriptsForApplication` property to migrate app specific scripts to a location accessible to your sandboxed app.

  This property contains either a string or an array of strings naming a folder (or folders) under `~/Library/Scripts/Applications` containing scripts that the app uses. The contents of any named folder or folders are moved to `~/Library/Application Scripts/<bundle_id>`. The old folder or folders are then each replaced with a symbolic link to the one new location, so other apps looking for the scripts in their legacy location can still find them.

Container migration is a one-way process: You are responsible for providing a way to undo it, should you need to do so during development or testing. The section [Undoing a Migration for Testing](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgeytcobtfvbuqnrnknltcmq) provides a suggestion about this.

## Creating a Container Migration Manifest

To support migration of app support files when a user first launches the sandboxed version of your app, create a container migration manifest.

![bullet](attachments/Resources/1282/Images/task_2x.png)To create and add a container migration manifest to an Xcode project

1. Add a property list file to the Xcode project.

   The Property List template is in the macOS “Resource” group in the file template dialog.

   __Important:__ Be sure to name the file `container-migration.plist` spelled and lowercased exactly this way.
2. Add a `Move` property to the container migration manifest.

   The `Move` property contains an array of files to move into your container directory. This property is usually the lone top-level key in a container migration manifest. You add it to the empty file as follows:

   - Right-click the empty editor for the new `.plist` file, then choose Add Row.
   - In the Key column, enter `Move` as the name of the key.

     You must use this exact casing and spelling.
   - In the Type column, choose `Array`.
3. Optionally add a `Symlink` property to the container migration manifest.

   The `Symlink` property contains an array of files to link into your container directory. The resulting symbolic links in your container directory point to files elsewhere.
4. Optionally add a `MigrateScriptsForApplication` property to the container migration manifest.

   The `MigrateScriptsForApplication` property contains a string or an array of strings naming script directories in `~/Library/Scripts/Applications` whose content should be merged into `~/Library/Application Scripts/<bundle_id>`.
5. Add strings to the `Move` (or `Symlink`) array for the files or folders you want to migrate.

   For example, suppose you want to migrate your `Application Support` directory (along with its contained files and subdirectories) to your container. If your directory is named after the app name, for example `AppSandboxQuickStart`, and is currently within the `~/Library/Application Support` directory, use the following string as the value for the new property list item:

   ```
   ${ApplicationSupport}/AppSandboxQuickStart
   ```

   No trailing slash character is required, and space characters are permitted. The search-path constant in the path is equivalent to `~/Library/Application Support`. This constant is described, along with other commonly used directories, in [Use Variables to Specify Support-File Directories](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgeytcobtfvbuqnrnknltm).

   Add as many strings as needed to identify all the original (before sandboxing) paths of files or folders you want to migrate.

   __Note:__ When you specify a directory to be moved, the move is recursive—it includes all the subdirectories and files within the directory you specify.
6. If you are migrating scripts, add a string or array of strings to the `MigrateScriptsForApplication` property.

   For example, suppose you want to migrate the scripts from the `~/Library/Scripts/Applications/AppSandboxQuickStart` directory. In this case, add the following string:

   ```
   AppSandboxQuickStart
   ```

   As a result of migration, any files in `~/Library/Scripts/Applications/AppSandboxQuickStart` are moved to `~/Library/Application Scripts/com.Acme.AppSandboxQuickStart`, and the `AppSandboxQuickStart` directory itself is replaced by a symbolic link to the new location.

Before you first test a migration manifest, provide a way to undo the migration, such as suggested in [Undoing a Migration for Testing](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgeytcobtfvbuqnrnknltcmq).

![bullet](attachments/Resources/1282/Images/task_2x.png)To test a container migration manifest

1. In the Finder, open two windows as follows:

   - In one window, view the contents of the `~/Library/Containers/` directory.
   - In the other window, view the contents of the directory containing the support files named in the container migration manifest—that is, the files you want to migrate.
2. Build and run the Xcode project.

Upon successful migration, the support files disappear from the original (nonsandbox) directory and appear in your app’s container.

If you want to alter the arrangement of support files during migration, use a slightly more complicated `.plist` structure. Specifically, for a file or directory whose migration destination you want to control, provide both a starting and an ending path. The ending path is relative to the `Data` directory in your container. In specifying an ending path, you can use any of the search-path constants described in [Use Variables to Specify Support-File Directories](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgeytcobtfvbuqnrnknltm).

If your destination path specifies a custom directory (one that isn’t part of a standard container), the system creates the directory during migration.

The following task assumes that you’re using the Xcode property list editor and working with the container migration manifest you created earlier in this chapter.

![bullet](attachments/Resources/1282/Images/task_2x.png)To control the destination of a migrated file or directory

1. In the container migration manifest, add a new item to the `Move` (or `Symlink`) array.
2. In the Type column, choose Array.
3. Add two strings as children of the new array item.
4. In the top string of the pair, specify the origin path of the file or directory you want to migrate.
5. In the bottom string of the pair, specify the destination (sandbox) custom path for the file or directory you want to migrate.

File migration proceeds from top-to-bottom through the container migration manifest. Take care to list items in an order that works. For example, suppose you want to move your entire `Application Support` directory as-is, except for one file. You want that file to go into a new directory parallel to `Application Support` in the container.

For this approach to work, you must specify the individual file move before you specify the move of the `Application Support` directory—that is, specify the individual file move higher in the container migration manifest. (If `Application Support` were specified to be moved first, the individual file would no longer be at its original location at the time the migration process attempted to move it to its new, custom location in the container.)

## Undoing a Migration for Testing

When testing migration of support files, you may find it necessary to perform migration more than once. To support this, you need a way to restore your starting directory structures—that is, the structures as they exist prior to migration.

One way to do this is to make a copy of the directories to migrate before you perform a first migration (including, if applicable, any scripts directories affected by the `MigrateScriptsForApplication` property). Save this copy in a location unaffected by the migration manifest. The following task assumes you have created this sort of backup copy.

![bullet](attachments/Resources/1282/Images/task_2x.png)To manually undo a container migration for testing purposes

1. If you specified `MigrateScriptsForApplication` in your manifest, remove the symbolic link or links created in `~/Library/Scripts/Applications` during migration.
2. Manually copy the files and directories—those specified in the manifest, including any script directories, if applicable—from your backup copy to their original (premigration) locations. (Be careful not to remove the files from your backup copy as you do so.)
3. Delete your app’s container.
4. Delete `~/Library/Application Scripts/<bundle_id>`, if it exists.

The next time you launch the app, the system recreates the container and migrates the support files according to the current version of the container migration manifest.

## An Example Container Migration Manifest

Listing 4-1 shows an example manifest as viewed in a text editor.

__Listing 4-1__  An example container migration manifest

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
   <key>Move</key>
   <array>
      <string>${Library}/AppSandboxQuickStart/MyConfiguration.plist</string>
      <array>
         <string>${Library}/AppSandboxQuickStart/MyDataStore.xml</string>
         <string>${ApplicationSupport}/AppSandboxQuickStart/MyDataStore.xml</string>
      </array>
   </array>
   <key>MigrateScriptsForApplication</key>
   <string>AppSandboxQuickStart</string>
</dict>
</plist>
```

This manifest specifies the migration of two items from the user’s `Library` directory to the app’s container. For the first item, `MyConfiguration.plist`, only the origin path is specified, leaving it to the migration process to place the file appropriately.

For the second item, `MyDataStore.xml`, both an origin and a custom destination path are specified.

Finally, the optional `MigrateScriptsForApplication` property causes any scripts in `~/Library/Scripts/Applications/AppSandboxQuickStart` to be moved to `~/Library/Application Scripts/com.Acme.AppSandboxQuickStart`, leaving a symbolic link to the new directory in place of the legacy one.

The `${Library}` and `${ApplicationSupport}` portions of the paths are variables you can use as a convenience. For a list of variables you can use in a container migration manifest, see [Use Variables to Specify Support-File Directories](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgeytcobtfvbuqnrnknltm).

## Use Variables to Specify Support-File Directories

When you specify a path in a container migration manifest, you can use certain variables that correspond to commonly used support file directories. These variables work in origin and destination paths, but the path that a variable resolves to depends on the context. Refer to Table 4-1.

__Table 4-1__  How system directory variables resolve depending on context

| Context | Variable resolves to |
| Origin path | Home-relative path (relative to the `~` directory) |
| Destination path | Container-relative path (relative to the `Data` directory in the container) |

The variables you can use for specifying support-file directories are described in [Table 4-2](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgeytcobtfvbuqnrnknlto). For an example of how to use these variables, see [Listing 4-1](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgeytcobtfvbuqnrnknltk).

__Table 4-2__  Variables for use in migration paths

| Variable | Meaning |
| `${ApplicationSupport}` | The directory containing application support files. Corresponds to the [NSApplicationSupportDirectory](https://developer.apple.com/documentation/foundation/filemanager/searchpathdirectory/applicationsupportdirectory) search-path constant. |
| `${AutosavedInformation}` | The directory containing the user’s autosaved documents. Corresponds to the [NSAutosavedInformationDirectory](https://developer.apple.com/documentation/foundation/nssearchpathdirectory/nsautosavedinformationdirectory) search-path constant. |
| `${Caches}` | The directory containing discardable cache files. Corresponds to the [NSCachesDirectory](https://developer.apple.com/documentation/foundation/nssearchpathdirectory/nscachesdirectory) search-path constant. |
| `${Document}`  `${Documents}` | Each variable corresponds to the directory containing the user’s documents. Corresponds to the [NSDocumentDirectory](https://developer.apple.com/documentation/foundation/nssearchpathdirectory/nsdocumentdirectory) search-path constant. |
| `${Home}` | The current user’s home directory. Corresponds to the directory returned by the [NSHomeDirectory](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Functions/FoundationFunctions/Description.html#//apple_ref/c/func/NSHomeDirectory) function. When in a destination path in a manifest, resolves to the container directory. |
| `${Library}` | The directory containing application-related support and configuration files. Corresponds to the [NSLibraryDirectory](https://developer.apple.com/documentation/foundation/nssearchpathdirectory/nslibrarydirectory) search-path constant. |
| `${BundleId}` | The app’s bundle identifier, for use in either an origin or destination path. |

[Next](App%20Sandbox%20Checklist.md)[Previous](Designing%20for%20App%20Sandbox.md)
