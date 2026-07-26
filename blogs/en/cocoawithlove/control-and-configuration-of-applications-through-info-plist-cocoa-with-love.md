---
title: 'Control and configuration of applications through Info.plist | Cocoa with Love'
source: Cocoa with Love (Matt Gallagher)
source_key: cocoawithlove
source_url: 'https://www.cocoawithlove.com/2009/08/control-and-configuration-of.html'
original_language: en
published: ''
status: frozen
license: All rights reserved（页脚明示）→ 严格私有
archived_at: 2026-07-26
content_hash: 'sha256:6fab619385653860'
translated: false
---

> 原文：[Control and configuration of applications through Info.plist | Cocoa with Love](https://www.cocoawithlove.com/2009/08/control-and-configuration-of.html)　·　Cocoa with Love (Matt Gallagher)

The Info.plist file is home to the metadata about your application used by the operating system. Most Cocoa programmers know that it stores the bundle identifier, icon name and version number of an application but the Info.plist can also control access to essential iPhone hardware resources and can change the very nature of your Mac OS X applications. In this post, I'll cover basic Info.plist usage and also explain some of the rarer settings.

## The default fields: identifiers, icons and version numbers

The Info.plist is the main source of metadata that the operating system has to learn information about your application. Everything that the operating system may need to know (names, icons, supported file types, URL types, `NSApplication` subclasses) may all be specified in the Info.plist.

The file itself is familiar to almost all Cocoa programmers since Xcode inserts one automatically into every project created from an application template.

Probably the most common settings are:

- — the identifier for your application, normally in the form "com.[company].[application]". The iPhone tries to fill in the application name from the Project's product name but will fail if you ever try to build for a device if there are spaces or differences in capitalization so you may just want to set this manually.
- — almost every application I ship names its icon "Icon.[png/icns]". Why Apple can't put a default value here, I don't know.
- — this isn't the only version number since you can embed a different version in the Project Settings. If you don't have a formal build system in place though, you'll need to make certain that this number is always different every time you give a build to someone to test (a crash log is useless if you can't guarantee which version it came from).

## How Xcode builds the Info.plist

Most of the other settings that are in the Info.plist by default have either good initial values (like the `NSMainNibFile` value which is automatically set to the name of the Nib file that the template itself includes), are largely pointless (like the `CFBundleSignature` which is a campy Mac OS 9 throwback) or are generated from values defined in the Project settings (like the `CFBundleName`).

The reason why the fields in the Info.plist can be generated from "Project settings" fields is that their values are filled in when the Info.plist file is "built" by Xcode.

Building the Info.plist file is actually the first stage in building for an application — the file is build immediately after creating the directory structure for the bundle. You can control the Info.plist's build settings in the "Packaging" section of the Target settings — including setting a different Info.plist for each target if needed.

While most stages of a build are handled by an external process (like gcc or ibtool), if you look through the Build Results window log, you'll notice that the Info.plist is built by a tool that identifies itself as `<com.apple.tools.info-plist-utility>`. This isn't actually a separate tool — it is described as "abstract" by the "Built-in compilers.pbcompspec" in the DevToolCore.framework and is implemented internally by the `XCInfoPlistUtilityCommandInvocation` class in the DevToolCore.framework. Xcode passes the arguments into this class (like it would for any other build stage) and the class parses the arguments and handles all the work itself.

## Reading from the Info.plist in your program

While the Info.plist is primary metadata that your program advertises to the operating system and external programs, your program can easily read any of the fields in the Info.plist for its own purposes using the `NSBundle`'s `infoDictionary`. For example, the URL to an iPhone app's own page on the iTunes App Store would be:

```objc
NSURL *appURL =
    [NSURL URLWithString:[NSString stringWithFormat:@"http://www.itunes.com/app/%@",
        [[[[NSBundle mainBundle] infoDictionary] objectForKey:@"CFBundleDisplayName"]
            stringByAddingPercentEscapesUsingEncoding:NSUTF8StringEncoding]]];
```

Technically, you can store anything you want in the Info.plist file but generally your own data would be better put in a separate file so you don't slow the operating system down when it needs to open and parse the Info.plist file to extract the data it needs.

## Essential iPhone Info.plist entries

### Aesthetic settings

A number of fields are required in the Info.plist to control aesthetic options for an iPhone application. These include:

- — set this to disable the gloss highlight that the Springboard applies to your application's icon.
- — use this to start your application in a non-portrait orientation.
- — use this to enable black or transparent status bars.

### Avoiding WiFi disconnections

Any iPhone application that requires a WiFi connection must set `UIRequiresPersistentWiFi` to `<true/>`, otherwise the iPhone will abruptly disconnect the WiFi connection after 30 minutes of use. No warning, no error: 30 minutes and you'll lose WiFi without this flag.

### Invoking your iPhone application by URL

The `CFBundleURLTypes` key allows you to specify URL schemes that will cause the iPhone to switch to your application. No, you can't override the schemes for the built-in applications.

If your application is launched using a URL type named _scheme_, then you can also provide a different startup image "Default-_scheme_.png" instead of the regular "Default.png".

## Essential Mac OS X Info.plist entries

### Changing the application type

You can create an application with no UI — no appearance in the Dock, no menubar and can't be the frontmost application — by setting the `LSBackgroundOnly` flag in the Info.plist.

Realistically though, you're more likely to make your application `LSUIElement`. The reason why this flag is better, is that your application _can_ be frontmost if you open a window but the other traits of `LSBackgroundOnly` remain (no appearance in the Dock and no menubar).

Why would you want an application with no appearance in the Dock? If you're making an `NSStatusBar` application (little applications that run as icons in the right of the menubar).

The following code adds an entry to the status bar when the application starts:

```objc
- (void)applicationDidFinishLaunching:(NSNotification *)notification
{
    statusItem = [[[NSStatusBar systemStatusBar]
        statusItemWithLength:NSSquareStatusItemLength] retain];
    
    [statusItem setMenu:statusMenu];
    [statusItem setHighlightMode:YES];
    [statusItem setToolTip:@"My Status Bar App"];
    [statusItem setTitle:nil];
    [statusItem setImage:[NSImage imageNamed:@"StatusBarIcon"]];
}
```

### Accepted document types

Document types accepted by an application can be set by editing the Info.plist file (the `CFBundleDocumentTypes` dictionary) although this is easier to do on the Properties tab of the Target settings.

## Conclusion

Looking back over the range of topics that I've covered, you can see that the Info.plist controls a very diverse range of application settings and capabilities. There are many more options that I haven't listed here so if you're trying to specify default localizations, change the `NSApplication` subclass, set environment variables for your application, specify a minimum OS versions and more, have a look at [Runtime Configuration Guidelines: Property List Key Reference](http://developer.apple.com/documentation/MacOSX/Conceptual/BPRuntimeConfig/Articles/PListKeys.html) for other fields.
