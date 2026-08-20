---
title: Open Directory Plug-in Programming Guide
apple_id: TP40000918
resource_type: Guide
platform: macOS
topic: Networking, Internet, & Web
technology: DirectoryService
published: '2015-03-09'
source_url: https://developer.apple.com/library/archive/documentation/Networking/Conceptual/Open_Dir_Plugin/ConfiguringanOpenDirectoryPlug-in/ConfiguringanOpenDirectoryPlug-in.html
archived_at: '2026-07-27T06:57:05.825847Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Open Directory Plug-in Programming Guide](Introduction.md)


[Next](Client%20Side%20Buffer%20Parsing.md)[Previous](Property%20List%20for%20an%20Open%20Directory%20Plug-in.md)

# Retired Document

__Important:__
Support for DirectoryService plug-ins has been deprecated and will be removed in a future release.

A new architecture was introduced in OS X v10.9 to allow the creation of native Open Directory modules. Unlike DirectoryService, `opendirectoryd` uses modules implemented as a standalone process that uses XPC to communicate with `opendirectoryd`. Implementing a module as an XPC service ensures a private address space and improves security and reliability, because modules cannot crash another module or `opendirectoryd`.

# Configuring an Open Directory Plug-in

In OS X v10.1, Open Directory plug-ins are configured through the Directory Setup application, which supports local configuration only. The Directory Setup application launches your plug-in configuration application when an administrator selects your plug-in for configuration. The configuration application to launch is specified in the property list file. Local configuration in OS X v10.1 is described in the section [Local Configuration](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaydsmjyfvbuqmjtfuytqmjygi).

In OS X v10.2 and later, administrators use the Directory Access application to select Open Directory plug-ins for configuration. If you provide a Directory Access plug-in that uses custom calls to communicate with your Open Directory plug-in, your Open Directory plug-in can be configured locally and remotely. Local and remote configuration in OS X v10.2 and later is described in the section [Remote Configuration](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaydsmjyfvbuqmjtfuytqnbrg4).

## Local Configuration

In OS X v10.1, the property list file is used to specify a configuration application that is to be launched when an administrator selects a plug-in for configuration. The `CFBundleConfigAvail` property specifies the full pathname, including filename, for the configuration application to launch. For example:

```
"CFBundleConfigAvail" = "/System/Library/Frameworks/DirectoryService.framework/ Resources/YourPlugInConfig.app"
```

You can also specify the name of the configuration file to open when your configuration application is launched:

```
“CFBundleConfigFile” = "/Library/Preferences/DirectoryService/ YourPlugInConfig.xml"
```

In this example, the configuration file is in XML format, as indicated by the extension `.xml`.

If your plug-in does not have a configuration application, it can set `CFBundleConfigAvail` to `Not Available`. If the `CFBundleConfigFile` property is missing from your property list file or is set to `Not Available`, but `CFBundleConfigFile` is set to a file name, the file is opened with its default application. If `CFBundleConfigAvail` is set, but `CFBundleConfigFile` is missing or set to `Not Available`, the configuration application is launched without a file. If both properties are missing or set to `Not Available`, the Configure button is dimmed when your plug-in is selected.

## Remote Configuration

OS X v10.2 and later supports remote configuration. To configure your Open Directory plug-in remotely, you need to create a Directory Access plug-in having the same name as your Open Directory plug-in but ending with `.daplug` instead of `.dsplug`. You can place your Directory Access plug-in in the Directory Access application bundle:

```
/Applications/Utilities/Directory Access.app/Contents/PlugIns/myplug.daplug
```

Your Directory Access plug-in should implement at least two functions:

- handle the Configure button click
- accept a PluginAPIImplementor object that provides your Directory Access plug-in with the information necessary to handle local and remote connections

You should use custom calls to your plug-in so you can support remote configuration as well as local configuration.If you need to support configuration of your Open Directory plug-in in OS X v10.1 as well as OS X v10.2 and later, you’ll need to use the `CFBundleConfigAvail` property in your property list file for OS X v10.1 and have a Directory Access plug-in for OS X v10.2 and later. If both types of configuration are installed on the same system running OS X v10.2 or later, your Directory Access plug-in will override the launching of the configuration application specified by the `CFBundleConfigAvail` property.

## DirectoryAccess Plug-ins

Starting with Mac OS 10.2, the Directory Access application, used by administrators to configure Open Directory, supports DirectoryAccess plug-ins. DirectoryAccess plug-ins are stored in the `Contents/PlugIns` directory inside the Directory Access application directory. A DirectoryAccess plug-in must be an NSBundle, have a name that matches the Open Directory plug-in it configures and have the extension `.daplug`. For Mac OS 10.3 and later, you can use the `pluginName` method to override the name showing in the list.

The bundle’s main class should support the DirectoryAccessPlugin interface, described below:

```objc
- (void)setPluginAPIImplementor:(id)implementor;
- (BOOL)saveChanges; // Return FALSE if can’t save for some reason.
- (BOOL)revertChanges;
- (BOOL)applicationWillQuitSavingChanges:(BOOL)save;
- (BOOL)applicationWillLockSavingChanges:(BOOL)save;
- (BOOL)isDirty;
- (void)configureButtonClicked:(id)sender;
- (void)setEnabled:(BOOL)enabled forLocation:(NSString*)location;
- (BOOL)isEnabledForLocation:(NSString*)location;
```

Table 11-1 describes each method.

__Table 11-1__  DirectoryAccessPlugin interface methods

| Method | Description |
| `setPluginAPIImplementor`: | Provides the API implementor used for callbacks. |
| `saveChanges`: | Called when the Apply button is clicked. |
| `revertChanges`: | Called when the Revert button is clicked. |
| `applicationWillQuitSavingChanges:` | Called before the application quits, with the `save` parameter indicating whether to save changes. If appropriate, `saveChanges` will be called after `applicationWillQuitSavingChanges`. |
| `applicationWillLockSavingChanges:` | Called before the application locks, with the `save` parameter indicating whether to save changes. If appropriate, `saveChanges` or `revertChanges` will be called after `applicationWillLockSavingChanges`. |
| `isDirty`: | Indicates whether the DirectoryAccess plug-in has any unsaved changes. Return `YES` from `isDirty` to ensure that the user is prompted to save changes when quitting or locking. |
| `configureButtonClicked`: | Called when your DirectoryAccess plug-in is selected when the Configure button is clicked or if your plug-in is double-clicked. |
| `setEnabled` | Used to override the state of the Enabled checkbox. |
| `isEnabledForLocation` | Used to override the state of the Enabled for Location checkbox. |

Your bundle’s main class is not required to implement all of the methods in `DirectoryAccessPlugin.h`; instead, it should implement only those methods that your DirectoryAccess plug-in actually needs. The most likely methods that you will need to implement are `setPluginAPIImplementor:` and `configureButtonClicked:`.

Starting with OS X v10.4, new DirectoryAccess methods are available:

```objc
// PluginAPIImplementor new methods available in OS X v10.4  and later
- (BOOL)canSetEnabledForLocation:(NSString*)location;
- (NSString*)hostName;
- (BOOL)saveSearchPolicies;
- (BOOL)isNodeOnAuthSearchPolicy:(NSString*)nodeName;
- (BOOL)isNodeOnContactSearchPolicy:(NSString*)nodeName;
- (void)addNodeToAuthSearchPolicy:(NSString*)nodeName;
- (void)addNodeToContactsSearchPolicy:(NSString*)nodeName;
- (void)deleteNodeFromAuthSearchPolicy:(NSString *)nodeName;
- (void)deleteNodeFromContactsSearchPolicy:(NSString *)nodeName;
- (void)deleteNodesFromAuthSearchPolicyWithPrefix:(NSString *)prefix;
- (void)deleteNodesFromContactsSearchPolicyWithPrefix:(NSString  *)prefix;
- (void)nodeNameChangedFrom:(NSString*)oldNodeNameto:(NSString*)newNodeName;
- (NSString *)pluginVersionWithPrefix:(NSString *)prefix;
- (BOOL)isPluginEnabled:(NSString*)prefix;
- (void)setPlugin:(NSString*)prefix enabled:(BOOL)enabled;
```

Table 11-2 describes the new DirectoryAccessPlugin interface methods.

__Table 11-2__  New DirectoryAccessPlugin interface methods

| Method | Description |
| `canSetEnabledForLocation`: | Used to determine whether to enable or disable the checkbox in the Services list. |
| hostName | Returns the host name of the machine being configured; useful when configuring a plug-in on a remote system. |
| `saveSearchPolicies` | Causes any pending search policy changes to be saved; can be used in conjunction with other methods that manipulate search policy lists. |
| `isNodeOnAuthSearchPolicy:` | Returns `YES` if the specified node name is on the authentication search policy; otherwise, returns `NO`. |
| isNodeonContactsSearchPolicy: | Returns `YES` if the specified node name is on the contacts search policy; otherwise, returns `NO`. |
| addNodeToAuthSeachPolicy: | Adds the specified node name to the authentication search policy and changes the authentication search policy to a custom search policy if necessary. |
| `addNodeToContactsSearchPolicy`: | Adds the specified node name to the contacts search policy and changes the contacts search policy to a custom search policy if necessary. |
| `deleteNodeFromAuthSearchPolicy:` | Removes the specified node name from the authentication search policy. |
| deleteNodeFromContactsSearchPolicy: | Removes the specified node name from the contacts search policy. |
| `deleteNodesFromAuthSearchPolicyWithPrefix` | Removes all node names that have the specified prefix from the authentication search policy. Useful when disabling a plug-in. |
| `deleteNodesFromContactsSearchPolcyWithPrefix` | Removes all node names that have the specified prefix from the contacts search policy. Useful when disabling a plug-in. |
| `nodeNameChangedFrom: to:` | Renames any nodes on either search policy from the old name to the new name. Useful when a configuration change in your plug-in changes a node name. |
| `plug-inVersionWithPrefix:` | Returns the version number from the named plug-in’s `Info.plist`. Useful when using one configuration plug-in to configure different versions of an Open Directory plug-in. |
| `isPluginEnabled:` | Returns `YES` if the Open Directory plug-in is set to be enabled; otherwise returns `NO`. |
| `setPlugin: enabled:` | Sets the specified plug-in enabled state as specified. Useful if you want to enable your plug-in when configuring it to be added to the search policy from within your custom configuration sheet. |

The file `PluginAPIImplementor.h` defines the following object and methods:

```objc
@interface PluginAPIImplementor : NSObject {
}

- (BOOL)preflightDSRef;
- (BOOL)preflightAuthRights;
- (OSStatus)makeAuthExternalForm:(AuthorizationExternalForm*)authExtForm;
- (tDirReference)dsRef;
- (AuthorizationRef)authorizationRef;
- (void)pluginEnableStateChanged:(NSString*)pluginName to:(BOOL)newstate;
- (void)reloadSearchPolicies;
- (void)markDirty:(id)sender;
```

The `PluginAPIImplementor` object provides callbacks to DirectoryAccess plug-ins and is passed using `setPluginAPIImplementor:` after the plug-in is loaded and initialized. If you want your Open Directory plug-in to be configurable remotely, or if you need to call any Open Directory functions, you must use the API reference provided by `dsRef`.

The recommended strategy is to have a specially named node, such as `/MyPlugin` for a DirectoryAccess plug-in named `MyPlugin`, that you open and call `dsDoPluginCustomCall` to read and write. To make changes, you can use `makeAuthExternalForm:` to put an externalized `AuthorizationRef` into the buffer so that your DirectoryAccess plug-in can verify that the user is authorized to make changes. Directory Access requires the system.services.directory.configure authorization right, which you can check from your DirectoryAccess plug-in using `AuthorizationCopyRights`. This prevents a malicious user from reconfiguring your Open Directory plug-in without first providing an administrator name and password.

Before performing a read operation, you should call `preflightDSRef`. This ensures that the connection is still established and reconnects if it isn’t. If this method returns `NO`, your DirectoryAccess plug-in should also return `NO` to indicate the operation failed.

Before performing a write operation, you should call `preflightAuthRights` to ensure that the `AuthorizationRef` is still valid. If `preflightAuthRights` returns `NO`, your DirectoryAccess plug-in should also return `NO` to indicate to the DirectoryAccess application that the `saveChanges` call failed.

[Next](Client%20Side%20Buffer%20Parsing.md)[Previous](Property%20List%20for%20an%20Open%20Directory%20Plug-in.md)
