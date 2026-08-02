---
title: App Sandbox Design Guide
apple_id: TP40011183
resource_type: Guide
platform: macOS
topic: Security
technology: null
published: '2016-09-13'
source_url: https://developer.apple.com/library/archive/documentation/Security/Conceptual/AppSandboxDesignGuide/AboutAppSandbox/AboutAppSandbox.html
archived_at: '2026-07-27T06:57:08.315690Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md)


[Next](App%20Sandbox%20Quick%20Start.md)

# About App Sandbox

_App Sandbox_ is an access control technology provided in macOS, enforced at the kernel level. It is designed to contain damage to the system and the user’s data if an app becomes compromised. Apps distributed through the Mac App Store must adopt App Sandbox. Apps signed and distributed outside of the Mac App Store with Developer ID can (and in most cases should) use App Sandbox as well.

## At a Glance

Complex systems will always have vulnerabilities, and software complexity only increases over time. No matter how carefully you adopt secure coding practices and guard against bugs, attackers only need to get through your defenses once to succeed. While App Sandbox doesn’t prevent attacks against your app, it does minimize the harm a successful one can cause.

A non-sandboxed app has the full rights of the user who is running that app, and can access any resources that the user can access. If that app or any framework it is linked against contain security holes, an attacker can potentially exploit those holes to take control of that app, and in doing so, the attacker gains the ability to do anything that the user can do.

Designed to mitigate this problem, the App Sandbox strategy is twofold:

1. App Sandbox enables you to describe how your app interacts with the system. The system then grants your app the access it needs to get its job done, and no more.
2. App Sandbox allows the user to transparently grant your app additional access by way of Open and Save dialogs, drag and drop, and other familiar user interactions.

（原归档配图获取待重试：`about_sandboxing.png`）

App Sandbox is not a silver bullet. Apps can still be compromised, and a compromised app can still do damage. But the scope of potential damage is severely limited when an app is restricted to the minimum set of privileges it needs to get its job done.

### App Sandbox is Based on a Few Straightforward Principles

By limiting access to sensitive resources on a per-app basis, App Sandbox provides a last line of defense against the theft, corruption, or deletion of user data, or the hijacking of system hardware, if an attacker successfully exploits security holes in your app. For example, a sandboxed app must explicitly state its intent to use any of the following resources using entitlements:

- Hardware (Camera, Microphone, USB, Printer)
- Network Connections (Inbound or Outbound)
- App Data (Calendar, Location, Contacts)
- User Files (Downloads, Pictures, Music, Movies, User Selected Files)

Access to any resource not explicitly requested in the project definition is rejected by the system at run time. If you are writing a sketch app, for example, and you know your app will never need access to the microphone, you simply don’t ask for access, and the system knows to reject any attempt your (perhaps compromised) app makes to use it.

On the other hand, a sandboxed app has access to the specific resources you request, allows users to expand the sandbox by performing typical actions in the usual way (such as drag and drop), and can automatically perform many additional actions deemed safe, including:

- Invoking Services from the Services menu
- Reading most world readable system files
- Opening files chosen by the user

The elements of App Sandbox are entitlements, container directories, user-determined permissions, privilege separation, and kernel enforcement. Working together, these prevent an app from accessing more of the system than is necessary to get its job done.

__Relevant chapters:__ [App Sandbox Quick Start](App%20Sandbox%20Quick%20Start.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgeytcobtfvbuqmrnknltg), [App Sandbox in Depth](App%20Sandbox%20in%20Depth.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgeytcobtfvbuqmznknlti)

### Design Your Apps with App Sandbox in Mind

After you understand the basics, look at your app in light of this security technology. First, determine if your app is suitable for sandboxing. (Most apps are.) Then resolve any API incompatibilities and determine which entitlements you need. Finally, consider applying privilege separation to maximize the defensive value of App Sandbox.

__Relevant chapter:__ [Designing for App Sandbox](Designing%20for%20App%20Sandbox.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgeytcobtfvbuqnbnknltc)

### Xcode Helps You Migrate an Existing App to App Sandbox

Some file system locations that your app uses are different when you adopt App Sandbox. In particular, you gain a container directory to be used for app support files, databases, caches, and other files apart from user documents. Xcode and macOS support migration of files from their legacy locations to your container.

__Relevant chapter:__ [Migrating an App to a Sandbox](Migrating%20an%20App%20to%20a%20Sandbox.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgeytcobtfvbuqnrnknltc)

### Preflight Your App Before Distribution

After you have adopted App Sandbox in your app, as a last step each time you distribute it, double check that you are following best practices.

__Relevant chapter:__ [App Sandbox Checklist](App%20Sandbox%20Checklist.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgeytcobtfvbuqobnknltc)

## How to Use This Document

To get up and running with App Sandbox, perform the tutorial in [App Sandbox Quick Start](App%20Sandbox%20Quick%20Start.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgeytcobtfvbuqmrnknltg). Before sandboxing an app you intend to distribute, be sure you understand [App Sandbox in Depth](App%20Sandbox%20in%20Depth.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgeytcobtfvbuqmznknlti). When you’re ready to start sandboxing a new app, or to convert an existing app to adopt App Sandbox, read [Designing for App Sandbox](Designing%20for%20App%20Sandbox.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgeytcobtfvbuqnbnknltc). If you’re providing a new, sandboxed version of your app to users already running a version that is not sandboxed, read [Migrating an App to a Sandbox](Migrating%20an%20App%20to%20a%20Sandbox.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgeytcobtfvbuqnrnknltc). Finally, before distributing your app, work through the [App Sandbox Checklist](App%20Sandbox%20Checklist.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgeytcobtfvbuqobnknltc) to verify that you are following best practices for App Sandbox.

## Prerequisites

Before you read this document, make sure you understand the overall macOS development process by reading _[Mac App Programming Guide](../../General/Mac%20App%20Programming%20Guide/About%20OS%20X%20App%20Design.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgeydknbt)_.

## See Also

To complement the damage containment provided by App Sandbox, you must provide a first line of defense by adopting secure coding practices throughout your app. To learn how, read _[Security Overview](../Security%20Overview/About%20Software%20Security.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaydsnzw)_ and _[Secure Coding Guide](../Secure%20Coding%20Guide/Introduction%20to%20Secure%20Coding%20Guide.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgazdimjv)_.

An important step in adopting App Sandbox is requesting entitlements for your app. For details on all the available entitlements, see _[Entitlement Key Reference](../../Miscellaneous/Entitlement%20Key%20Reference/About%20Entitlements.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgeytcojv)_.

You can enhance the benefits of App Sandbox in a full-featured app by implementing privilege separation. You do this using XPC, a macOS implementation of interprocess communication. To learn the details of using XPC, read _[Daemons and Services Programming Guide](../../Mac%20OSX/Daemons%20and%20Services%20Programming%20Guide/About%20Daemons%20and%20Services.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgeydambqge3te2i)_.

[Next](App%20Sandbox%20Quick%20Start.md)
