---
title: UDID Replacement APIs in iOS 6
source: Ole Begemann
source_key: oleb
source_url: 'https://oleb.net/blog/2012/09/udid-apis-in-ios-6/'
original_language: en
published: ''
status: active
license: 未声明 → 仅私有归档
archived_at: 2026-07-27
content_hash: 'sha256:cad859586436587a'
translated: false
---

> 原文：[UDID Replacement APIs in iOS 6](https://oleb.net/blog/2012/09/udid-apis-in-ios-6/)　·　Ole Begemann

# UDID Replacement APIs in iOS 6

In a last minute change to iOS 6, Apple added an option for users to opt out of targeted advertising. The setting can be found in the iOS Settings app under General \> About \> Advertising. I see no reason why Apple did not place it in the more obvious new Privacy section other than to hide it from most casual users.

[![The Limit Ad Tracking option in iOS 6 Settings](https://oleb.net/media/ios-6-limit-ad-tracking.png)](https://oleb.net/media/ios-6-limit-ad-tracking.png)

<sub>The Limit Ad Tracking option in iOS 6 Settings. It can be found under General \> About \> Advertising.</sub>

> iOS 6 introduces the Advertising Identifier, a non-permanent, non-personal device identifier, that advertising networks will use to give you more control over advertisers’ ability to use tracking methods. If you choose to limit ad tracking, advertising networks using the Advertising Identifier may no longer gather information to serve you targeted ads. In the future all advertising networks will be required to use the Advertising Identifier. However, until advertising networks transition to using the Advertising Identifier you may still receive targeted ads from other networks.

iOS apps can read the state of this preference and are required to respect it (see below). I would have loved if Mobile Safari also used this setting to send an appropriate [Do Not Track HTTP header](https://en.wikipedia.org/wiki/Do_Not_Track) but unfortunately that is not (yet?) the case.^[1](#fn:1)

# `identifierForVendor`

After the [deprecation of the UDID](http://techcrunch.com/2011/08/19/apple-ios-5-phasing-out-udid/) in iOS 5, iOS 6 comes with two new APIs that are meant to replace the UDID.

First, the [`UIDevice`](https://developer.apple.com/library/ios/#documentation/UIKit/Reference/UIDevice_Class/Reference/UIDevice.html) class has a new property called [`identifierForVendor`](https://developer.apple.com/library/ios/documentation/UIKit/Reference/UIDevice_Class/Reference/UIDevice.html#//apple_ref/doc/uid/TP40006902-CH3-SW49). Here’s what the documentation has to say about it:

> An alphanumeric string that uniquely identifies a device to the app’s vendor. (read-only)
> 
> The value of this property is the same for apps that come from the same vendor running on the same device. A different value is returned for apps on the same device that come from different vendors, and for apps on different devices regardless of vendor.

The `identifierForVendor` can be used by companies to follow users across multiple apps from the same vendor, but it doesn’t allow the tracking of user behavior across a multitude of apps from several developers. The fact that the identifier is bound to the device and not to a particular user (with a particular Apple ID and iCloud account) makes me wonder how useful it is in practice. In my opinion, it often makes more sense to [generate a custom UUID and use it to identify a particular user](https://oleb.net/blog/2011/09/how-to-replace-the-udid/). If you store this UUID in iCloud (using the key-value store) and use the same iCloud container identifier for all your apps, you can identify a user across all your apps and across all their devices pretty reliably even though you have no access to the user’s iCloud credentials.

**Update September 24, 2012:** Note that the OS automatically deletes the current `identifierForVendor` when the user deletes the last application from a particular vendor. If he later reinstalls one or more apps from that vendor, the OS will generate a new identifier. The `identifierForVendor` gets backed up during normal device backups. Restoring a backup to the same device will also restore all existing vendor identifiers. Because the identifier is device-specific, it will not be restored to a different device, though.

If `identifierForVendor` were the only replacement API for the UDID, I suppose ad network companies would be pretty pissed at Apple. For whatever reason, Apple felt it needed to provide a better tracking method for advertisers. The new AdSupport framework consists of one small class, [`ASIdentifierManager`](https://developer.apple.com/library//ios/#documentation/AdSupport/Reference/ASIdentifierManager_Ref/ASIdentifierManager.html), which encapsulates access to an [`advertisingIdentifier`](https://developer.apple.com/library/ios/documentation/AdSupport/Reference/ASIdentifierManager_Ref/ASIdentifierManager.html#//apple_ref/doc/uid/TP40012654-CH1-SW4)^[2](#fn:2). Moreover, the [`advertisingTrackingEnabled`](https://developer.apple.com/library/ios/documentation/AdSupport/Reference/ASIdentifierManager_Ref/ASIdentifierManager.html#//apple_ref/doc/uid/TP40012654-CH1-SW3) property tells you whether the user has opted out of ad tracking with the switch in Settings mentioned above.^[3](#fn:3)

Let’s have a look at the documentation for these properties:

> `advertisingIdentifier`: An alphanumeric string unique to each device, used only for serving advertisements. (read-only)
> 
> Unlike the `identifierForVendor` property of `UIDevice`, the same value is returned to all vendors. This identifier may change—for example, if the user erases the device—so you should not cache it.
> 
> `advertisingTrackingEnabled`: A Boolean value that indicates whether the user has limited ad tracking. (read-only)
> 
> Check the value of this property before performing any advertising tracking. If the value is `NO`, use the advertising identifier only for the following purposes: frequency capping, conversion events, estimating the number of unique users, security and fraud detection, and debugging.

The problem with these requirements is that Apple has no way to enforce them. The data aggregation required for ad targeting happens on the ad company’s server, which Apple has no control over. All they can ensure during app review is that apps that send the `advertisingIdentifier` over the network also include the user’s opt-out setting—if the company then respects the user’s preference on their server is under no-one’s control.

The fact that the identifier changes when the device is erased sounds good at first but doesn’t do much for a user’s privacy in practice. Or how often do you reset and erase your iPhone? Yeah, I thought so. I would love a setting that allowed the user to manually reset the identifier (like removing cookies in a web browser) or even tell the OS to reset it on a regular basis (say, weekly) in order to avoid longtime tracking by ad networks.

# A Move Against Analytics Companies?

I wonder whether Apple’s aim with these API changes is specifically to restrict the other popular use case of device tracking: app analytics networks. The very specific names of the new APIs (they all have “advertising” in their name) seem to suggest that Apple will not tolerate apps that use these APIs for other purposes, such as broad-scale analytics across multiple apps and vendors. Remember how adamant Steve Jobs was towards analytics aggregators like [Flurry](http://www.flurry.com) in [his 2010 interview at the D8 conference](http://www.iphonejd.com/iphone_jd/2010/06/steve-jobs-at-d8.html):

> One day we read in the paper that a company called Flurry Analytics has detected that we have some new iPhone and other tablet devices that we’re using on our campus. And we thought, ‘What the hell?’ And the way that they detected this was they’re getting developers to put their software in their apps, and their software is sending out information about the device and about its geolocation and other things back to Flurry. No customer is ever asked about this, it’s violating every rule in our privacy policy with our developers, and we went through the roof about this. So we said ‘No, we’re not going to allow this. This is violating our privacy policies, and it’s pissing us off that they’re publishing new data about our new products.’ So we said that we’re only going to allow these analytics that don’t give device information and that are for solely for the purpose of advertising.

[Watch the video (from 1:30:02)](https://www.youtube.com/watch?v=LrS7JQv-zgY&t=1h13m02s).

It is conceivable that app reviewers could try to identify non-advertising-related usages of the `advertisingIdentifier` and reject such apps. It will be interesting to see if Apple has something like this in mind.

1. I tested this by visiting [http://donottrack.us](http://donottrack.us) with Mobile Safari with the Limit Ad Tracking switch set to on. The web site reported that the browser does support the Do Not Track header but that the Do Not Track preference was not set. [↩︎](#fnref:1)
2. Unlike the deprecated `uniqueIdentifier` property, these new attributes return a [`NSUUID`](https://developer.apple.com/library/ios/documentation/Foundation/Reference/NSUUID_Class/Reference/Reference.html#//apple_ref/doc/c_ref/NSUUID) instance and not a plain string. Use the [`-UUIDString`](https://developer.apple.com/library/ios/documentation/Foundation/Reference/NSUUID_Class/Reference/Reference.html#//apple_ref/doc/uid/TP40012254-CH1-SW10) method to get a string representation of a `NSUUID`. [↩︎](#fnref:2)
3. Note that the `-[UIDevice identifierForAdvertising]` property that was present in the iOS 6 betas is gone. The functionality has been moved into the `ASIdentifierManager` class. [↩︎](#fnref:3)
