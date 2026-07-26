---
title: Xcode Build Configuration Files
source: NSHipster (Mattt)
source_key: nshipster
source_url: 'https://nshipster.com/xcconfig/'
original_language: en
published: 2020-02-27
status: active
license: CC BY-NC（页脚明示）→ 可非商业再分发，须署名
archived_at: 2026-07-27
content_hash: 'sha256:ba2c87cf62e26b6f'
translated: false
---

> 原文：[Xcode Build Configuration Files](https://nshipster.com/xcconfig/)　·　NSHipster (Mattt)

# [Xcode Build Configuration Files](https://nshipster.com/xcconfig/)

Written by  [Mattt](https://nshipster.com/authors/mattt/)  February 27^th, 2020 ([revised](https://github.com/nshipster/articles/commits/master/2020-02-27-xcconfig.md))

Software development best practices [prescribe](https://12factor.net/config) strict separation of configuration from code. Yet developers on Apple platforms often struggle to square these guidelines with Xcode’s project-heavy workflow.

Understanding what each project setting does and how they all interact with one another is a skill that can take years to hone. And the fact that much of this information is buried deep within the GUIs of Xcode does us no favors.

Navigate to the “Build Settings” tab of the project editor, and you’ll be greeted by _hundreds_ of build settings spread across layers of projects, targets, and configurations — _and that’s to say nothing of the other six tabs!_

![Xcode build settings](https://nshipster.com/assets/xcconfig-project-build-settings--light-4c8624f6a37113dc51e85964be85519b079d44118061f753d15764a6124f92c1ece20d536c077bf64f5ba183604947a68d603aad9a0c6da7481db34fbbf26a6f.png)

Fortunately, there’s a better way to manage all of this configuration that doesn’t involve clicking through a maze of tabs and disclosure arrows.

This week, we’ll show you how you can use text-based `xcconfig` files to externalize build settings from Xcode to make your projects more compact, comprehensible, and powerful.

---

[Xcode build configuration files](https://help.apple.com/xcode/mac/current/#/dev745c5c974), more commonly known by their `xcconfig` file extension, allow build settings for your app to be declared and managed without Xcode. They’re plain text, which means they’re much friendlier to source control systems and can be modified with any editor.

Fundamentally, each configuration file consists of a sequence of key-value assignments with the following syntax:

```
BUILD_SETTING_NAME = value
```

For example, to specify the Swift language version for a project, you’d specify the `SWIFT_VERSION` build setting like so:

```
SWIFT_VERSION = 5.0
```

---

At first glance, `xcconfig` files bear a striking resemblance to `.env` files, with their simple, newline-delimited syntax. But there’s more to Xcode build configuration files than meets the eye. _Behold!_

### Retaining Existing Values

To append rather than replace existing definitions, use the `$(inherited)` variable like so:

```
BUILD_SETTING_NAME = $(inherited)additional value
```

You typically do this to build up lists of values, such as the paths in which the compiler searches for frameworks to find included header files (`FRAMEWORK_SEARCH_PATHS`):

```
FRAMEWORK_SEARCH_PATHS = $(inherited) $(PROJECT_DIR)
```

Xcode assigns inherited values in the following order (from lowest to highest precedence):

- Platform Defaults
- Xcode Project xcconfig File
- Xcode Project File Build Settings
- Target xcconfig File
- Target Build Settings

### Referencing Values

You can substitute values from other settings by their declaration name with the following syntax:

```
BUILD_SETTING_NAME = $(ANOTHER_BUILD_SETTING_NAME)
```

Substitutions can be used to define new variables according to existing values, or inline to build up new values dynamically.

```
OBJROOT = $(SYMROOT)
CONFIGURATION_BUILD_DIR = $(BUILD_DIR)/$(CONFIGURATION)-$(PLATFORM_NAME)
```

### Setting Fallback Values for Referenced Build Settings

In Xcode 11.4 and later, you can use the `default` evaluation operator to specify a fallback value to use if the referenced build setting evaluates as empty.

```
$(BUILD_SETTING_NAME:default=value)
```

### Conditionalizing Build Settings

You can conditionalize build settings according to their SDK (`sdk`), architecture (`arch`), and / or configuration (`config`) according to the following syntax:

```
BUILD_SETTING_NAME[sdk=sdk] = value for specified sdk
BUILD_SETTING_NAME[arch=architecture] = value for specified architecture
BUILD_SETTING_NAME[config=configuration] = value for specified configuration
```

Given a choice between multiple definitions of the same build setting, the compiler resolves according to specificity.

```
BUILD_SETTING_NAME[sdk=sdk][arch=architecture] = value for specified sdk and architectures
BUILD_SETTING_NAME[sdk=*][arch=architecture] = value for all other sdks with specified architecture
```

For example, you might specify the following build setting to speed up local builds by only compiling for the active architecture:

```
ONLY_ACTIVE_ARCH[config=Debug][sdk=*][arch=*] = YES
```

### Including Build Settings from Other Configuration Files

A build configuration file can include settings from other configuration files using the same `#include` syntax as the equivalent `C` directive on which this functionality is based:

```
#include "path/to/File.xcconfig"
```

As we’ll see later on in the article, you can take advantage of this to build up cascading lists of build settings in really powerful ways.

## Creating Build Configuration Files

To create a build configuration file, select the “File \> New File…” menu item (⌘N), scroll down to the section labeled “Other”, and select the Configuration Settings File template. Next, save it somewhere in your project directory, making sure to add it to your desired targets

![Xcode new configuration file](https://nshipster.com/assets/xcconfig-new-file--light-2196fa7cbd39f743d406ba6de095699bd6bc8965a9f92d0d5fd98d59d54b89cd949dc82ca4fd4735b40dd55a423d462ce94085077a5b5cdfa78edffdce5e6537.png)

Once you’ve created an `xcconfig` file, you can assign it to one or more build configurations for its associated targets.

![Xcode project configuration](https://nshipster.com/assets/xcconfig-project-configurations--light-9fa05b222eb93e0c144f00a1fd9996f53ff005d6af16cbbda35a217065efbe59057e968c0c7ba7f50cc185de958504aceabc1bd43fd4f72e8d682133f77c7fa9.png)

---

Now that we’ve covered the basics of using Xcode build configuration files let’s look at a couple of examples of how you can use them to manage development, stage, and production environments.

---

## Customizing App Name and Icon for Internal Builds

Developing an iOS app usually involves juggling various internal builds on your simulators and test devices (as well as the latest version from the App Store, to use as a reference).

You can make things easier on yourself with `xcconfig` files that assign each configuration a distinct name and app icon.

```
// Development.xcconfig
PRODUCT_NAME = $(inherited) α
ASSETCATALOG_COMPILER_APPICON_NAME = AppIcon-Alpha

//////////////////////////////////////////////////

// Staging.xcconfig
PRODUCT_NAME = $(inherited) β
ASSETCATALOG_COMPILER_APPICON_NAME = AppIcon-Beta
```

## Managing Constants Across Different Environments

If your backend developers comport themselves according to the aforementioned [12 Factor App](https://12factor.net/config) philosophy, then they’ll have separate endpoints for development, stage, and production environments.

On iOS, perhaps the most common approach to managing these environments is to use conditional compilation statements with build settings like `DEBUG`.

```
import Foundation

#if DEBUG
let apiBaseURL = URL(string: "https://api.staging.example.com")!
#else
let apiBaseURL = URL(string: "https://api.example.com")!
#endif
```

This gets the job done, but runs afoul of the canon of code / configuration separation.

An alternative approach takes these environment-specific values and puts them where they belong — into `xcconfig` files.

```
// Development.xcconfig
API_BASE_URL = api.staging.example.com

//////////////////////////////////////////

// Production.xcconfig
API_BASE_URL = api.example.com
```

However, to pull these values programmatically, we’ll need to take one additional step:

### Accessing Build Settings from Swift

Build settings defined by the Xcode project file, `xcconfig` files, and environment variables, are only available at build time. When you run the compiled app, none of that surrounding context is available. _(And thank goodness for that!)_

But wait a sec — don’t you remember seeing some of those build settings before in one of those other tabs? Info, was it?

As it so happens, that info tab is actually just a fancy presentation of the target’s `Info.plist` file. At build time, that `Info.plist` file is compiled according to the build settings provided and copied into the resulting app [bundle](https://nshipster.com/bundles-and-packages/). Therefore, by adding references to `$(API_BASE_URL)`, you can access the values for those settings through the `infoDictionary` property of Foundation’s `Bundle` API. _Neat!_

![Xcode Info.plist](https://nshipster.com/assets/xcconfig-project-info-plist--light-3c51d15109870c490ca5116b14bf6eb428047a5cdee9bf6041e208088d20518cbb960ba9f093f828b37bb6346aa5a435dd77f862014eb43a76b0135b8c3b3d42.png)

Following this approach, we might do something like the following:

```
import Foundation

enum Configuration {
    enum Error: Swift.Error {
        case missingKey, invalidValue
    }

    static func value<T>(for key: String) throws -> T where T: LosslessStringConvertible {
        guard let object = Bundle.main.object(forInfoDictionaryKey:key) else {
            throw Error.missingKey
        }

        switch object {
        case let value as T:
            return value
        case let string as String:
            guard let value = T(string) else { fallthrough }
            return value
        default:
            throw Error.invalidValue
        }
    }
}

enum API {
    static var baseURL: URL {
        return try! URL(string: "https://" + Configuration.value(for: "API_BASE_URL"))!
    }
}
```

When viewed from the call site, we find that this approach harmonizes beautifully with our best practices — not a single hard-coded constant in sight!

```
let url = URL(string: path, relativeTo: API.baseURL)!
var request = URLRequest(url: url)
request.httpMethod = method
```

---

Xcode projects are monolithic, fragile, and opaque. They’re a source of friction for collaboration among team members and generally a drag to work with.

Fortunately, `xcconfig` files go a long way to address these pain points. Moving configuration out of Xcode and into `xcconfig` files confers a multitude of benefits and offers a way to distance your project from the particulars of Xcode without leaving the Cupertino-approved “happy path”.
