---
title: UIRequiredDeviceCapabilities Cannot Be Changed in App Updates
source: Ole Begemann
source_key: oleb
source_url: 'https://oleb.net/blog/2011/12/uirequireddevicecapabilities-cannot-be-changed-in-app-updates/'
original_language: en
published: ''
status: active
license: 未声明 → 仅私有归档
archived_at: 2026-07-26
content_hash: 'sha256:0329e9af0b142684'
translated: false
---

> 原文：[UIRequiredDeviceCapabilities Cannot Be Changed in App Updates](https://oleb.net/blog/2011/12/uirequireddevicecapabilities-cannot-be-changed-in-app-updates/)　·　Ole Begemann

# UIRequiredDeviceCapabilities Cannot Be Changed in App Updates

**Update May 10, 2012:** Apple replied to my bug report:

> Engineering has determined that this issue behaves as intended based on the following information: Developers can add restrictions to `UIRequiredDeviceCapabilities` on app updates provided any device that is dropped cannot support the min os version specified.

**Update January 11, 2012:** Added a screenshot of the Xcode validation error.

Earlier this month, I wrote about [How to Restrict Your iOS App to Modern Hardware](https://oleb.net/blog/2011/12/how-to-restrict-your-ios-app-to-modern-hardware/). One of the suggestions I made was to use the `UIRequiredDeviceCapabilities` key in your `Info.plist` file to make your app run only on devices with armv7 CPUs. Several people contacted me afterwards to tell me that this approach only works for new apps.

You heard that right: **when updating an app, it seems you cannot add new restrictions to the Required Device Capabilities.** One developer who contacted me said he has been fighting with this for more than 2 years, and all due to the simple mistake of omitting the “telephony” requirement in version 1.0 of his app.[1](#fn:1)

## Automatic Rejection by Xcode’s Validator

According to the feedback I got, this is not even an issue that could be discussed during the app review process. Instead, it seems that the automatic validation service that Apple has integrated into Xcode will reject any update with more restrictive `UIRequiredDeviceCapabilities` than the earlier version before you can even upload it to iTunes Connect.

![Xcode validation error after updating UIRequiredDeviceCapabilities](https://oleb.net/media/xcode-validation-uirequireddevicecapabilities.jpg)

<sub>Xcode validation error after updating `UIRequiredDeviceCapabilities`. [Screenshot by Noel Llopis](https://twitter.com/noel_llopis/status/156428438994042880).</sub>

# How About Not Changing the Deployment Target for Your App’s Lifetime?

I think this is a very bad rule on Apple’s side and I wonder how it can be reconciled with other Apple policies regarding app updates. Ultimately, raising the required device capabilities is equivalent to increasing your app’s Deployment Target[2](#fn:2), something that Apple has no problem with in an app update.

One could argue that from the perspective of the users, [a minimum OS version is easier to communicate than changed hardware requirements](https://twitter.com/olemoritz/status/142587108509491200) but I find that unconvincing. If anything, changed hardware requirements should be easier to understand than changes on the software side since every user knows that hardware cannot be updated while it’s a lot harder to grasp why an old device should not be able to run a new OS version. And Apple does a bad job of communicating changed OS version requirements anyway so it strikes me as odd that they should care so much about the hardware side of things.

In addition, there are some hardware features Apple actively pushes, encouraging developers to adopt them in their apps. The prime example is probably the non-backwards compatible OpenGL ES 2.0. During the recent iOS 5 Tech Talks, [Apple actively rallied developers to switch to OpenGL ES 2](https://oleb.net/blog/2011/11/ios5-tech-talk-allan-schaffer-opengl-es-glkit/) to make their apps better. But how is a developer supposed to switch from OpenGL ES 1.1 to 2.0 if he is not permitted to add the corresponding `UIRequiredDeviceCapabilities` key to its updated app? In that case, he would be forced to increase the Deployment Target to iOS 4.3+ (all devices that run iOS 4.3 also support OpenGL ES 2.0) and his `Info.plist` would not reflect the correct hardware requirements anymore. Looks like a bad workaround to me.

## Downgrades are Possible

It is worth noting that the other way – lowering the required device capabilities – is indeed possible. One developer told me that they had no problems when they _removed_ a requirement from their app.

# Please File a Bug Report

If you also think this is a bad policy that Apple should change, please [file a bug report](https://bugreport.apple.com/). Feel free to refer to the bug ID under which I reported the problem: rdar://10623835.

1. To quote from this developer’s e-mail to me: I exchanged several emails with Apple support but they reject to change this even in this exceptional and logical case. [↩︎](#fnref:1)
2. In Apple’s terminology, the Deployment Target indicates the minimum OS version that an app can run on. For instance, setting the Deployment Target of an app to iOS 4.3 has the same effect in practice as using the `UIRequiredDeviceCapabilities` to restrict the app to the armv7 architecture because the sets of all iOS devices that can run iOS 4.3 and have an armv7-capable CPU are identical. Apple takes measures to avoid the installation of apps on devices that do not fulfill the Deployment Target requirements. [↩︎](#fnref:2)
