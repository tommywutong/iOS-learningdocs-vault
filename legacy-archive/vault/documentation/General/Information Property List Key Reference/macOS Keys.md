---
title: Information Property List Key Reference
apple_id: TP40009247
resource_type: Guide
platform: watchOS|tvOS|iOS|macOS
topic: General
technology: null
published: '2018-06-04'
source_url: https://developer.apple.com/library/archive/documentation/General/Reference/InfoPlistKeyReference/Articles/GeneralPurposeKeys.html
archived_at: '2026-07-15T07:34:59.264188Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Information Property List Key Reference](About%20Info.plist%20Keys%20and%20Values.md)


[Next](iOS%20Keys.md)[Previous](Cocoa%20Keys.md)

# macOS Keys

The keys in this chapter define assorted functionality related to macOS bundles.

Table 1 contains an alphabetical listing of macOS–specific keys, the corresponding name for that key in the Xcode property list editor, and a high-level description of each key. Detailed information about each key is available in later sections.

__Table 1__  Summary of macOS keys

| Key | Xcode name | Summary |
| APInstallerURL | “Installation directory base file URL” | A URL-based path to the files you want to install. See [APInstallerURL](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgiydambrgqztcljrga3dknzx) for details. |
| APFiles | “Installation files” | An array of dictionaries describing the files or directories that can be installed. See [APFiles](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgiydambrgqztcljrga3dmmbw) for details. |
| ATSApplicationFontsPath | “Application fonts resource path” | The path to a single font file or directory of font files in the bundle’s `Resources` directory. See [ATSApplicationFontsPath](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4tenjtfvjvooa) for details. |
| CSResourcesFileMapped | “Resources should be file-mapped” | If true, Core Services routines map the bundle’s resource files into memory instead of reading them. See [CSResourcesFileMapped](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4tenjtfuytemrvgmyq) for details. |
| NSMainStoryboardFile | “Main storyboard file base name” | Specifies the name of the app’s storyboard resource file. See [NSMainStoryboardFile](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4tenjtfvjvoni) for details. |
| QLSandboxUnsupported | None | Specifies that a Quick Look plug-in does not support sandboxing. See for details. |
| QuartzGLEnable | None | Specifies whether the app uses Quartz GL. See [QuartzGLEnable](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4tenjtfvjvomjx) for details. |

`APInstallerURL` (`String` - macOS) identifies the base path to the files you want to install. You must specify this path using the form `file://localhost/path/`. All installed files must reside within this directory.

`APFiles` (`Array` - macOS) specifies a file or directory you want to install. You specify this key as a dictionary, the contents of which contains information about the file or directory you want to install. To specify multiple items, nest the `APFiles` key inside itself to specify files inside of a directory. Table 2 lists the keys for specifying information about a single file or directory.

__Table 2__  Keys for APFiles dictionary

| Key | Xcode name | Type | Description |
| __APFileDescriptionKey__ | “Install file description text” | `String` | A short description of the item to display in the Finder’s Info window |
| __APDisplayedAsContainer__ | “Display with folder icon” | `String` | If “Yes” the item is shown with a folder icon in the Info panel; otherwise, it is shown with a document icon |
| __APFileDestinationPath__ | “File destination path” | `String` | Where to install the component as a path relative to the app bundle |
| __APFileName__ | “Install file name” | `String` | The name of the file or directory |
| __APFileSourcePath__ | “Install file source path” | `String` | The path to the component in the app package relative to the `APInstallerURL` path. |
| __APInstallAction__ | “File install action” | `String` | The action to take with the component: “Copy” or “Open” |

`ATSApplicationFontsPath` (`String` - macOS) identifies the location of a font file or directory of fonts in the bundle’s `Resources` directory. If present, macOS activates the fonts at the specified path for use by the bundled app. The fonts are activated only for the bundled app and not for the system as a whole. The path itself should be specified as a relative directory of the bundle’s Resources directory. For example, if a directory of fonts was at the path `/Applications/MyApp.app/Contents/Resources/Stuff/MyFonts/`, you should specify the string `Stuff/MyFonts/` for the value of this key.

`CSResourcesFileMapped` (`Boolean` - macOS) specifies whether to map this app’s resource files into memory. Otherwise, they are read into memory normally. File mapping can improve performance in situations where you are frequently accessing a small number of resources. However, resources are mapped into memory read-only and cannot be modified.

`NSMainStoryboardFile` (`String` - macOS) contains a string with the name of the app’s main storyboard file (minus the `.storyboard` filename extension). A storyboard file is an Interface Builder archive containing the app’s view controllers, the connections between those view controllers and their immediate views, and the segues between view controllers. When this key is present, the main storyboard file is loaded automatically at launch time and its initial view controller is installed in the app’s window.

This key is mutually exclusive with the [NSMainNibFile](Cocoa%20Keys.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgiydambrgqztcljrga3temrr) key. You should include one of these keys in your `Info.plist` file but not both. This key is supported in macOS 10.10 and later.

`QLSandboxUnsupported` (`Boolean` - macOS) allows a Quick Look plug-in to opt out of sandboxing. A code-signed Quick Look plug-in—which includes all plug-ins that are bundled in apps available in the Mac App Store—is sandboxed by default. Use this key to temporarily disable sandboxing while you update your plug-in to be compatible with it.

`QuartzGLEnable` (`Boolean` - macOS) specifies whether this app uses Quartz GL.

| Value | Description |
| --- | --- |
| `true` | Turn on Quartz GL for the app’s windows. (This works only when the computer has at least 1 GB of RAM). |
| `false` | Disable Quartz GL. Quartz GL will not be available, even after using `[<NSWindow> setPreferredBackingLocation:]`. |

Quartz GL is not supported on computers with more than one video card installed.

To turn on Quartz QL for testing use the Quartz Debug app, located in `<Xcode>/Applications`.

This key is available in macOS 10.5 and later.

[Next](iOS%20Keys.md)[Previous](Cocoa%20Keys.md)

