---
title: FxPlug SDK Overview
apple_id: TP40002180
resource_type: Guide
platform: macOS
topic: Apple Applications
technology: null
published: '2016-10-27'
source_url: https://developer.apple.com/library/archive/documentation/AppleApplications/Conceptual/FXPlug_overview/Entitlements/Entitlements.html
archived_at: '2026-07-15T05:17:55.869088Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [FxPlug SDK Overview](About%20the%20FxPlug%20SDK.md)


[Next](Creating%20FxPlug%20Plug-ins%20for%20Final%20Cut%20Pro.md)[Previous](FxPlug%20Concepts%20and%20API.md)

# Working with Entitlements

Motion, Final Cut Pro, and Compressor are in the process of moving to a sandboxed model. This chapter provides a brief overview of application sandboxing. You’ll also learn how to specify entitlements for a sandboxed application and understand how plug-ins are loaded.

Application sandboxing restricts an application’s access to only system resources, including the file system, for which it’s explicitly given access. A sandboxed application is given a _code signature_ to prevent tampering, and a list of system resources it’s allowed to access. This list of system resources is called its _entitlements_—see [Specifying Entitlements](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgazdcobqfvbuqmrthawvgvzu). Figure 3-1 compares access levels for an application with sandboxing and an application without sandboxing.

__Figure 3-1__  Application sandboxing

!!

Prior to application sandboxing, loading arbitrary third-party code had full system access, presenting a potential security issue. There are three ways to combat this:

- Restrict the host application’s entitlements to the basic necessities.
- Force loaded code, such as a plug-in, to operate with no more entitlements than the host (_privilege inheritance_).
- Design the host application to take advantage of OS-mediated XPC Services, a type of interprocess communication (IPC), which are handled securely at the system level.

  An XPC Service is a lightweight “helper tool” process that can be spawned with its own entitlements to perform work on behalf of an application. Having its own entitlements is called _privilege separation_ and dramatically reduces the possible harm from a malicious attack in the case of code injection or the like.

FxPlug plug-ins conveniently bundle the necessary components for a traditional XPC Service, making it easier for developers to adopt. For most plug-in developers who do not need entitlements beyond what’s provided by Motion and Final Cut Pro, migrating existing plug-ins is a simple process that consists mostly of adding Xcode targets and plist entities. For developers who want to use extra entitlements, such as network access, address book access, or the built-in camera, migrating code into an XPC Service can help.

When an FxPlug plug-in needs to communicate with its out-of-process XPC Service, developers can employ the new [FxPrincipalAPI](https://developer.apple.com/documentation/fxplug/fxprincipalapi), which returns a proxy object.

This proxy object accepts method calls, relays them across processes, and returns the results. It’s fast, asynchronous, and less complicated than setting up your own XPC Service. The proxy object knows what methods can be used by way of a developer-established protocol, which is linked to by both the in-host component (the _Embedded Principal_) and the out-of-process XPC Service (the _Service Principal_—see [Embedded Principal and Service Principal Communication](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgazdcobqfvbuqmrthawvgvzs)), as shown in Figure 3-2.

__Figure 3-2__  FxPlug proxy object

!

All three components (Embedded Principal, Service Principal, and Protocol) are combined into a single bundle, an application bundle. This application bundle is the new FxPlug 3.0 plug-in structure—see [Creating a New FxPlug Application Bundle](Working%20with%20FxPlug%20Application%20Bundles.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgazdcobqfvbuqnbnknltm) and [Converting Old FxPlug Plug-ins to New FxPlug Plug-ins](Working%20with%20FxPlug%20Application%20Bundles.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgazdcobqfvbuqnbnknlto). Multiple filters can be bundled into a single application and use the same Service Principal. Developers can take advantage of this new structure and write an application that users see when they double-click the plug-in, and plug-ins no longer have to live in a special folder in the system.

Refer to _[Entitlement Key Reference](../../Miscellaneous/Entitlement%20Key%20Reference/About%20Entitlements.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgeytcojv)_ for information on how to specify entitlements for your FxPlug plug-ins.

Plug-in discovery transpires via PlugInKit, a new OS X v10.9 system component. Launch Services automatically registers your plug-in with PlugInKit when the user copies the file to their system the first time. When Motion or Final Cut Pro runs, it queries PlugInKit for all FxPlug plug-ins and loads any it finds. Your plug-in must have an additional entry in its plist file for PlugInKit-specific data.

For plug-ins using dynamic registration, the `+sharedInstance` method is not called when loaded from PlugInKit; instead, the `-init` method is called.

With Launch Services now handling the discovery of FxPlug plug-ins, a few new challenges have arisen for developers. When developing a plug-in, it’s not uncommon to have several project folders, with build directories that contain various versions of the same plug-in. However, host applications can only load one plug-in with a particular identifier, and the plug-in that gets loaded may not be the one you want.

Host applications deterministically load plug-ins with identical identifiers using the following set of rules:

- For end users, plug-ins in the `/Applications` folder (and its subfolders) have top priority.
- Additional plug-ins discovered on disk that are not a duplicate of one in the `/Applications` folder are first ranked by version (the highest version has priority) and, if their versions match, then by lexicographical order (the first plug-in of a descending order list is chosen).

For example, say you develop the FxBrightness.app FxPlug plug-in and the end user places it into `/Applications`. The plug-in in `/Applications` is the one that loads when the host application launches. If they move it out of `/Applications`, it still loads unless another copy of FxBrightness.app is put into `/Applications`, in which case that one loads.

If an end user has two copies of the FxBrightness.app FxPlug plug-in on disk, and neither is in `/Applications`, the second set of criteria applies. First the version is checked, and if they are the same, then the path is used to chose the plug-in to load.

For third-party developers, the same rules apply, but with finer-grained controls to help ease the process. Using a _defaults write_ from the command line, developers can specify _ignore_ and _priority_ paths.

- Ignore paths—No plug-ins in the specified paths (and subfolders) are loaded.
- Priority paths—Plug-ins in the specified paths take priority over all other plug-ins with the same identifier. Priority paths apply in the order they are specified, with the first path having highest priority.

The `defaults write` command is:

```
defaults write <host-application> <path-type> -array <paths>
```

Where:

- `host-application`—The host application for which the path defaults are to be applied: `com.apple.motionapp` (for Motion) or `com.apple.FinalCut` (for Final Cut Pro).
- `path-type`—The path type: `FxPlugPriorityPaths` (for Priority) or `FxPlugIgnorePaths` (for Ignore).
- `paths`—The list of directories, separated by a space. Leave this blank to clear the paths.

By default, the host application priority path is `/Applications`. If a new priority path is specified, `/Applications` are no longer considered a priority unless explicitly set as such.

In any collisions between priority and ignore paths, the ignore paths are applied first, to cull plug-ins.

The Embedded Principal can get an XPC proxy for the Service Principal via the `+[FxPrincipalAPI servicePrincipal]` method. Likewise, the Service Principal can get an XPC proxy for the embedded principal via the `+[FxPrincipalAPI embeddedPrincipal]` method. These two principals must agree on a protocol for their communication, and you must include the protocol name in the PlugInKit entry of the plug-in’s Info.plist file. When a connection is established, you can asynchronously call any methods listed in the agreed-upon protocols of each principal.

If the plug-in does not make use of an XPC and requires no special permissions, it may work entirely as embedded code. You must still specify an XPC Principal class and name it in the XPC-Info.plist, but you may omit defining a protocol. If you do, be sure to list the value for Protocol as NSObject.

An XPC service is expected to keep minimal state so the OS may start and stop it as needed without disrupting communication between the XPC and the host. As such, the OS can kill the XPC if, for example, system memory is getting low. The host application is expected to restart the XPC whenever it needs to communicate with it.

For a typical application that owns its XPC, restarting the XPC is not usually a problem. However, because an FxPlug’s XPC belongs to the plug-in, the host application is not always aware that it’s trying to communicate with the XPC.

Starting with Final Cut Pro X 10.3 and Motion 5.3, the host application ensures the XPC is running before making any calls to the plug-in’s embedded code. There are still times, however, when the plug-in may be called directly by the OS to perform actions and may need to communicate with its XPC. For example, if a plug-in has a custom view to display a custom parameter, the OS directly calls the view’s -`drawRect:` method. In cases like this, the plug-in should call the `[-FxCustomParameterActionAPI startAction:]` method before performing any communication with the XPC, and then call `[-FxCustomParameterActionAPI endAction:]` when it is finished.

As a rule, whenever a plug-in is going to communicate with its XPC, and it wasn’t directly called by the host application, the plug-in needs to call `-startAction:`/`-endAction:`.

[Next](Creating%20FxPlug%20Plug-ins%20for%20Final%20Cut%20Pro.md)[Previous](FxPlug%20Concepts%20and%20API.md)

