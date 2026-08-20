---
title: Sandboxing and Automation in OS X
apple_id: DTS40015156
resource_type: QA
platform: macOS
topic: Interapplication Communication
technology: null
published: '2015-05-23'
source_url: https://developer.apple.com/library/archive/qa/qa1888/_index.html
archived_at: '2026-07-18T02:35:23.188257Z'
---
> 导航：[总目录](../README.md) · [qa](../_indexes/qa.md)



Technical Q&A QA1888

# Sandboxing and Automation in OS X

## Q:  How does sandboxing affect my scriptable app, AppleScript app, or Automator action in OS X?

A: As explained in [App Sandbox Design Guide](https://developer.apple.com/library/mac/documentation/Security/Conceptual/AppSandboxDesignGuide/AboutAppSandbox/AboutAppSandbox.html), a non-sandboxed app has the full rights of the user who is running that app and can access any resources that the user can access. If that app or the frameworks it is linked against contain security holes, an attacker can potentially exploit those holes to take control of that app. In doing so, the attacker gains the ability to do anything that the user can do.

A sandboxed app, on the other hand, has limited access to resources. Instead of having free rein of the OS, a sandboxed app must request entitlements for the resources it needs. See [Entitlement Key Reference](https://developer.apple.com/library/mac/documentation/Miscellaneous/Reference/EntitlementKeyReference/Chapters/AboutEntitlements.html). By limiting access to resources in this manner, App Sandbox provides a last line of defense against the theft, corruption, or deletion of user data if an attacker successfully exploits security holes in your app or the frameworks it is linked against.

Because sandboxing limits interaction with files and folders and between apps in OS X, there are certain impacts on automation-related apps, such as scriptable apps, AppleScript apps, and Automator actions.

For security reasons, Apple encourages all developers to sandbox their apps. Sandboxing is a requirement if you intend to distribute your app via the Mac App Store.

Currently, when you adopt sandboxing in an app, your app retains the ability to:

- Receive Apple events
- Send Apple events to itself
- Respond to Apple events it receives

Your app cannot, however, send Apple events to other apps unless you request a __scripting-targets entitlement__ or an __apple-events temporary exception entitlement__. In the same way, regardless of whether your app is sandboxed, any external sandboxed app that attempts to interact with your app must also request the appropriate entitlements to do so.

A scripting-targets entitlement is a request to access a specific subset of scripting terminology, known as an access group, in the target app. For example, your app might create messages in Mail. In this situation, your app would request an entitlement for the compose access group in Mail. Scripting-targets entitlements provides the OS with fine-grained knowledge of the inter-application tasks your app is supposed to perform. This ensures that your app does only what the user expects, and isn’t being exploited by an attacker for some malicious function. For more information on scripting-targets entitlements, see [Enabling Scripting of Other Apps](https://developer.apple.com/library/mac/documentation/Miscellaneous/Reference/EntitlementKeyReference/Chapters/EnablingAppSandbox.html#//apple_ref/doc/uid/TP40011195-CH4-SW25) in Entitlement Key Reference.

An apple-events temporary exception entitlement is needed when an app doesn’t implement the necessary access groups for the scripting terminology your app needs to use. Note that this type of entitlement is intended to be temporary, and your app should not plan to use it indefinitely. If an Apple app doesn’t implement the access groups you need, you should file a [bug report](http://bugreport.apple.com/) indicating that you need this support. If the app is a third-party app, you should contact the developer and request that they implement this support in a future version of their app. For more information about apple-events temporary exception entitlements, see [Apple Event Temporary Exception](https://developer.apple.com/library/mac/documentation/Miscellaneous/Reference/EntitlementKeyReference/Chapters/AppSandboxTemporaryExceptionEntitlements.html#//apple_ref/doc/uid/TP40011195-CH5-SW3) in Entitlement Key Reference.

Automator actions are plug-in bundles that are loaded and run by Automator and the OS. Automator actions can be installed into `/Library/Automator/` and `~/Library/Automator/`. If you’re an app developer, actions can also be embedded into the `/Contents/Library/Automator/` directory within your app bundle. Regardless of where your action is installed and whether your app itself is sandboxed, the action runs within the context of the app that loads it. When actions are loaded and run by Automator or the OS, they are run outside of a sandbox, and can access any file, folder, or app that the user can access.

- Ensure that your app adheres to all current review guidelines and requirements. See [Mac App Store Review Guidelines](https://developer.apple.com/appstore/mac/resources/approval/guidelines.html).
- If your app needs to interact with files or folders in standard locations outside your app’s sandbox, request the appropriate entitlements. See [Enabling Access to Files in Standard Locations](https://developer.apple.com/library/mac/documentation/Miscellaneous/Reference/EntitlementKeyReference/Chapters/EnablingAppSandbox.html#//apple_ref/doc/uid/TP40011195-CH4-SW7) in Entitlement Key Reference.
- If your app needs to interact with files or folders in other locations outside your app’s sandbox, allow the user to choose them if at all possible and request the appropriate entitlement. See [Enabling User-Selected File Access](https://developer.apple.com/library/mac/documentation/Miscellaneous/Reference/EntitlementKeyReference/Chapters/EnablingAppSandbox.html#//apple_ref/doc/uid/TP40011195-CH4-SW6) in Entitlement Key Reference.
- If your app sends Apple events to other apps, avoid requesting temporary entitlements if you don’t absolutely need to do so. For example, instead of using the Finder to interact with files or folders, try using methods provided by [NSFileManager](https://developer.apple.com/library/mac/documentation/Cocoa/Reference/Foundation/Classes/NSFileManager_Class/index.html). If you do need to interact with an app, and that app has access groups for the interactions your app performs, request a scripting-targets entitlement. Otherwise, request an apple-events temporary exception entitlement. See [Enabling Scripting of Other Apps](https://developer.apple.com/library/mac/documentation/Miscellaneous/Reference/EntitlementKeyReference/Chapters/EnablingAppSandbox.html#//apple_ref/doc/uid/TP40011195-CH4-SW25) and [Apple Event Temporary Exception](https://developer.apple.com/library/mac/documentation/Miscellaneous/Reference/EntitlementKeyReference/Chapters/AppSandboxTemporaryExceptionEntitlements.html#//apple_ref/doc/uid/TP40011195-CH5-SW3) in Entitlement Key Reference. Note that requesting apple-events temporary exception entitlements for the Finder and System Events will likely result in rejection during the app review process, because granting access to these processes gives your app free rein over much of the operating system. For system-level tasks, use other methods, as discussed above.
- When submitting your app in iTunes Connect, list any entitlements your app requests and provide detailed information justifying why they are needed.

- [App Distribution Guide](https://developer.apple.com/library/mac/documentation/IDEs/Conceptual/AppDistributionGuide/Introduction/Introduction.html)
- [App Sandboxing](https://developer.apple.com/app-sandboxing/)
- [App Sandbox Design Guide](https://developer.apple.com/library/mac/documentation/Security/Conceptual/AppSandboxDesignGuide/AboutAppSandbox/AboutAppSandbox.html)
- [Developer ID and Gatekeeper](https://developer.apple.com/developer-id/)
- [Entitlement Key Reference](https://developer.apple.com/library/mac/documentation/Miscellaneous/Reference/EntitlementKeyReference/Chapters/AboutEntitlements.html)
- [FAQs on App Sandboxing](https://developer.apple.com/devcenter/download.action?path=/Mac_OS_X/app_sandboxing_faq/app_sandboxing_faqs.pdf)
- [Technical Q&A QA1773: Common app sandboxing issues](https://developer.apple.com/library/mac/qa/qa1773/_index.html)

- [Apple Event Temporary Exception in Entitlement Key Reference](https://developer.apple.com/library/mac/documentation/Miscellaneous/Reference/EntitlementKeyReference/Chapters/AppSandboxTemporaryExceptionEntitlements.html#//apple_ref/doc/uid/TP40011195-CH5-SW3)
- [Enabling Scripting of Other Apps in Entitlement Key Reference](https://developer.apple.com/library/mac/documentation/Miscellaneous/Reference/EntitlementKeyReference/Chapters/EnablingAppSandbox.html#//apple_ref/doc/uid/TP40011195-CH4-SW25)
- [Gatekeeper and Signing Applets in AppleScript Release Notes](https://developer.apple.com/library/mac/releasenotes/AppleScript/RN-AppleScript/RN-10_8/RN-10_8.html#//apple_ref/doc/uid/TP40000982-CH108-SW8)
- [Sandboxing and Running Scripts in AppleScript Release Notes](https://developer.apple.com/library/mac/releasenotes/AppleScript/RN-AppleScript/RN-10_8/RN-10_8.html#//apple_ref/doc/uid/TP40000982-CH108-SW11)
- [Sandboxing and Scriptability in AppleScript Release Notes](https://developer.apple.com/library/mac/releasenotes/AppleScript/RN-AppleScript/RN-10_8/RN-10_8.html#//apple_ref/doc/uid/TP40000982-CH108-SW9)
- [Technical Q&A QA1802: Adopting Scripting Targets for Composing Mail](https://developer.apple.com/library/mac/qa/qa1802/_index.html)
- [WWDC2012 - Secure Automation Techniques in OS X](https://developer.apple.com/videos/wwdc/2012/#206)

---

#### Document Revision History

| __Date__ | __Notes__ |
| 2015-05-23 | Updated link to App Sandboxing FAQ document. |
| 2015-02-05 | New document that provides information about how sandboxing affects a scriptable app, AppleScript app, or Automator action in OS X. |

