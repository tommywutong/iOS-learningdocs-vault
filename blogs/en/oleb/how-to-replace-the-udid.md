---
title: How to Replace the UDID
source: Ole Begemann
source_key: oleb
source_url: 'https://oleb.net/blog/2011/09/how-to-replace-the-udid/'
original_language: en
published: ''
status: active
license: 未声明 → 仅私有归档
archived_at: 2026-07-27
content_hash: 'sha256:0af277365aca6768'
translated: false
---

> 原文：[How to Replace the UDID](https://oleb.net/blog/2011/09/how-to-replace-the-udid/)　·　Ole Begemann

# How to Replace the UDID

**Update September 20, 2012:** Also read [my follow-up article describing the situation in iOS 6](https://oleb.net/blog/2012/09/udid-apis-in-ios-6/).

iOS 5 is still in beta, yet [Techcrunch revealed a few weeks ago](http://techcrunch.com/2011/08/19/apple-ios-5-phasing-out-udid/) that Apple will deprecate the `-[UIDevice uniqueIdentifier]` method in iOS 5. This method returns a device’s UDID, the 40 character hex string that uniquely identifies each device.

Many developers use this value to anonymously track usage of their apps or to create user accounts on an app-related web service without requiring the user to register an account manually. Unfortunately, the nature of the UDID also makes it easy to track users across multiple apps if those apps talk to the same webservice such as an ad network or analytics service, as so many apps do.

Apple apparently considers this a big enough privacy problem to phase out developer access to the UDID (and rightly so if you ask me). So what should you do if your app relies on the UDID at the moment?

# Don’t Panic

Keep in mind that the method has just been [deprecated](https://en.wikipedia.org/wiki/Deprecation) in iOS 5, not removed. So for the time being, nothing really changes. Apple probably won’t remove it until the release of iOS 6 or even later, so you have plenty of time to consider alternatives.

# The MAC Address as a Replacement

Every network adapter on the planet needs a unique [MAC address](https://en.wikipedia.org/wiki/Mac_address) to identify itself on the network. Since every iOS device has at least one network interface, the MAC address can serve as a full replacement for the UDID. Check out [this code on GitHub](https://github.com/gekitz/UIDevice-with-UniqueIdentifier-for-iOS-5/blob/master/Classes/UIDevice+IdentifierAddition.m) by Georg Kitz to find out how to access it on an iOS device.

You don’t need to access private APIs to retrieve the MAC address so this should be safe for the App Store. Still, Apple clearly intends to block access to identifiers that can be used to track user behavior across multiple apps. Depending on what you use this identifier for, I would expect Apple to reject apps that do “malicious” user tracking based on the MAC address in the future.

Rather than blindly replacing the UDID with the MAC address, I urge you to think about your actual requirements. Do you really need a unique hardware identifier? I would argue that in most cases, a unique _user_ identifier is much more useful.

# Do You Really Need a Hardware Identifier?

Both the UDID and the MAC address are _device_ identifiers. As such, they don’t tell you anything about a specific _user_. While the iPhone and iPod touch are primarily personal devices and thus normally only used by one person, this is less true for the iPad, which gets often shared by a family. Also, most people will replace their device with a new one sooner or later, and often they will sell their old device or give it away to a family member.

This is a real problem if your webservice equates the hardware identifier with a specific user when it really should have been tracking users instead of devices all along. So we would have to replace the UDID with a user ID. Such a user identifier should survive software updates, full system restores and device replacements, which is more than the UDID or MAC address can do. Ideally, it should also identify the same user on multiple devices (such as an iPhone and an iPad). Admittedly, that is not possible with the simple solution I present here.

# Self-made UUIDs

To create our own unique identifier, we use the Core Foundation function [`CFUUIDCreate()`](http://developer.apple.com/library/ios/documentation/CoreFoundation/Reference/CFUUIDRef/Reference/reference.html#//apple_ref/c/func/CFUUIDCreate). It returns a reference to an opaque type `CFUUIDRef`, which we can convert into a string with the [`CFUUIDCreateString`](http://developer.apple.com/library/ios/documentation/CoreFoundation/Reference/CFUUIDRef/Reference/reference.html#//apple_ref/c/func/CFUUIDCreateString) function.

It is good practice to wrap these calls in a small `NSString` category so that we can reuse them easily (UUIDs come in handy in many cases, for example if you need to generate unique filenames):

```
@interface NSString (UUID)

+ (NSString *)uuid;

@end

@implementation NSString (UUID)

+ (NSString *)uuid
{
    NSString *uuidString = nil;
    CFUUIDRef uuid = CFUUIDCreate(NULL);
    if (uuid) {
        uuidString = (NSString *)CFUUIDCreateString(NULL, uuid);
        CFRelease(uuid);
    }
    return [uuidString autorelease];
}

@end
```

Now, in our code, we generate a fresh UUID on the first launch of our app and store it to the user defaults database:

```
#define UUID_USER_DEFAULTS_KEY @"UUID"

- (BOOL)application:(UIApplication *)application didFinishLaunchingWithOptions:(NSDictionary *)launchOptions
{
    NSUserDefaults *defaults = [NSUserDefaults standardUserDefaults];
    if ([defaults objectForKey:UUID_USER_DEFAULTS_KEY] == nil) {
        [defaults setObject:[NSString uuid] forKey:UUID_USER_DEFAULTS_KEY];
        [defaults synchronize];
    }

    ...
```

That way, our UUID will automatically be backed up and restored to a new device.
