---
title: Handling Default Values With NSUserDefaults
source: Ole Begemann
source_key: oleb
source_url: 'https://oleb.net/blog/2014/02/nsuserdefaults-handling-default-values/'
original_language: en
published: ''
status: active
license: 未声明 → 仅私有归档
archived_at: 2026-07-26
content_hash: 'sha256:fc58c6cefb6f4dd7'
translated: false
---

> 原文：[Handling Default Values With NSUserDefaults](https://oleb.net/blog/2014/02/nsuserdefaults-handling-default-values/)　·　Ole Begemann

# Handling Default Values With NSUserDefaults

The [`NSUserDefaults`](https://developer.apple.com/library/ios/documentation/cocoa/reference/foundation/Classes/NSUserDefaults_Class/Reference/Reference.html) class is the API for storing and retrieving user preferences in Cocoa. It is very simple to use, yet I haven often seen it used incorrectly or inefficiently, especially when it comes to handling default values for preferences.

Consider this example:

```
BOOL showTutorialOnLaunch =
    [[NSUserDefaults standardUserDefaults] boolForKey:@"ShowTutorial"];
```

This only works correctly if a value for the key `"ShowTutorial"` has already been set. If the defaults database contains no value for the specified key, the `boolForKey:` method defaults to returning `NO`, which is probably not the default value you would want in this example. The caller has no way of distinguishing between `NO` and _no value_; the same is true for the other `NSUserDefaults` methods that return primitive values, such as `integerForKey:`.

## Workarounds

I can think of three obvious workarounds to this problem, all of which are ugly (and all of which I have seen in actual production code):

1. Rephrase all user defaults keys so that `NO` or `0` is the correct default value. In our example, this would mean renaming `"ShowTutorial"` to `"HideTutorial"`. This may be a workable solution for boolean values, but is extremely impractical or impossible for numbers and more complex values.
2. Always use `-[NSUserDefaults objectForKey:]` instead of the primitive accessor methods:

  ```
  NSNumber *showTutorialOnLaunch =
      [[NSUserDefaults standardUserDefaults] objectForKey:@"ShowTutorial"];
  if (showTutorialOnLaunch == nil) {
      // No value found
      showTutorialOnLaunch = @YES;
  }
  ```

  `objectForKey:` returns `nil` when a value is not present, which can be distinguished from a valid object that represents `NO` or `0`. This works but makes the code less readable and more complex than it needs to be.
3. Write custom code that stores the default values for all preferences in the user defaults on the first launch of your app (requiring another flag that tells your app whether it is being launched for the first time or not). This is essentially what we will do, but in a more elegant way.

## The registerDefaults: Method

A better way is to take advantage of the [`registerDefaults:`](https://developer.apple.com/library/ios/documentation/cocoa/reference/foundation/Classes/NSUserDefaults_Class/Reference/Reference.html#//apple_ref/doc/uid/20000318-CIHDDCDB) method. `registerDefaults:` expects a dictionary containing the default values for all of your app’s preferences.

To edit the default values, you should create a `DefaultPreferences.plist` file containing such a dictionary in Xcode and add it to your target. At runtime, your app can then load that file and pass its contents to `registerDefaults:`:

```
NSURL *defaultPrefsFile = [[NSBundle mainBundle]
    URLForResource:@"DefaultPreferences" withExtension:@"plist"];
NSDictionary *defaultPrefs =
    [NSDictionary dictionaryWithContentsOfURL:defaultPrefsFile];
[[NSUserDefaults standardUserDefaults] registerDefaults:defaultPrefs];
```

When you later invoke `-[NSUserDefaults boolForKey:]` from anywhere in your code, it will return the correct default value if no specific value is stored under that key.

Note that you have to do this on _every launch_ of your app before you read any values from the user defaults because `registerDefaults:` does not persist the default values to disk. The `application:didFinishLaunchingWithOptions:` method is usually the right place.

## Defaults Domains

So how does this work? The user defaults database actually consists of a hierarchy of layers, or domains. Whenever you read the value for a key, `NSUserDefaults` traverses this domain hierarchy from top to bottom and returns the first value it finds. It works a bit like the [responder chain](https://developer.apple.com/library/ios/documentation/EventHandling/Conceptual/EventHandlingiPhoneOS/event_delivery_responder_chain/event_delivery_responder_chain.html#//apple_ref/doc/uid/TP40009541-CH4-SW1). Domains can be persistent (values are stored on disk) or volatile (values are only valid for the lifetime of the `NSUserDefaults` instance).

The most important domain is called the _application domain_. This is where your app’s settings are stored when you invoke any of the `-[NSUserDefaults set...ForKey:]` methods. In contrast, the `registerDefaults:` method stores the values you pass it in the the lower-priority volatile _registration domain_ to serve as a fallback for any value that is not found in the application domain.

There is also a _global domain_ where system-wide settings are stored and language-specific domains that contain regional preferences such as month names or date formats for each locale.

Last but not least, Apple uses the same technique to allow us to override user defaults values via command line arguments. Every Cocoa app automatically inspects its command line arguments for key/value pairs of the form `-KEY VALUE` and will add these to the user defaults under the aptly named _argument domain_. Since the argument domain has the highest priority of all, we can use it to temporarily override any preference. Most of you probably know that this is very useful for testing a localized app in another language, for instance with `-AppleLanguages (de)`[1](#fn:1). In this case, we override the default language, which is normally defined in the global domain.

The complete search order for user defaults domains looks like this:

| Domain | State |
|---|---|
| `NSArgumentDomain` | volatile |
| Application | persistent |
| `NSGlobalDomain` | persistent |
| Languages | volatile |
| `NSRegistrationDomain` | volatile |

## When Your App Uses a Settings Bundle

Keep in mind that you should also use `registerDefaults:` when your app uses a [Settings Bundle](https://developer.apple.com/library/ios/documentation/Cocoa/Conceptual/UserDefaults/Preferences/Preferences.html). Since you already specified default values inside the settings bundle’s plist, you may expect that your app picks these up automatically. However, that is not the case. The information contained in the settings bundle is only read by the iOS Settings.app and never by your app.

In order to have your app use the same defaults as shown inside the Settings.app, you have to manually copy the user defaults keys and their default values into a separate plist file and register it with the defaults database as shown above.

1. The parentheses around `(de)` are important because the value for the key `AppleLanguages` must be an array. [↩︎](#fnref:1)
