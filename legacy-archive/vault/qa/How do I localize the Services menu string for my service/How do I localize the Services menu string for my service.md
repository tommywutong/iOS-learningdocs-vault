---
title: How do I localize the Services menu string for my service
apple_id: DTS40009797
resource_type: QA
platform: macOS
topic: User Experience
technology: AppKit
published: '2010-03-29'
source_url: https://developer.apple.com/library/archive/qa/qa1605/_index.html
archived_at: '2026-07-18T02:32:40.734530Z'
---
> 导航：[总目录](../../README.md) · [qa](../../_indexes/qa.md)



Technical Q&A QA1605

# How do I localize the Services menu string for my service

## Q:  How do I localize the Services menu string for my service?

A: How do I localize the Services menu string for my service?

When you provide a service, either via an Automator created workflow or via an advertised service from your application, you may provide a string that is presented as a menu item in the Services menu, or in contextual menus. This string can be localized so that users with different language preferences can easily find your service. Figure 1 shows an example service that uses the menu item string "Apply Test Service", localized into French.

__Figure 1__  Example of a localized service menu item.

!!

The Services menu item for your service is declared in your application or Automator workflow's `Info.plist` file, under an `NSServices`, `NSMenuItem` key. There is always a single entry in the `NSMenuItem` dictionary named "default" that contains the default text used for your service menu item, as shown in Listing 1.

__Listing 1__  Example service Info.plist section.

```
<key>NSServices</key> <array>     <dict>         <key>NSMenuItem</key>         <dict>             <key>default</key>             <string>Apply Test Service</string>         </dict> ...
```

Note that if your application is providing multiple services, there will be an `NSMenuItem` entry in the `Info.plist` file for each service.

To localize this text, you will need to add a UTF-16 encoded strings file named `ServicesMenu.strings` to your application project or Automator workflow bundle resources (details on how to do this are below). This strings file will contain, for each service menu item you are providing, an entry that uses the default text as the key, and the translated text as the value. For each language you wish to support, you will provide a translated `ServicesMenu.strings` file in a language-specific project (`.lproj`) directory in your project resources. As an example, the French version of the `ServicesMenu.strings` file for the example service shown in Figure 1 with the Info.plist file described in Listing 1 would look something like Listing 2, and would be found in the `Resources/fr.lproj` directory in the example service's project bundle.

__Listing 2__  Example ServicesMenu.strings file.

```
/*     ServicesMenu.strings      Created on 3/12/10. */  "Apply Test Service" = "Appliquer Service Test";
```

If you are providing a service via an application, you will add your localized `ServicesMenu.strings` file to your application project via Xcode or other preferred localization management developer tool (such as AppleGlot). If you are providing a service from an Automator created workflow, you will need to manually add the strings files and `.lproj` resource directories to the workflow bundle. You can find Automator created workflow bundles in your home directory under `~/Library/Services`.

Once you have provided localized text for your service menu item title, you may need to refresh the Services menu list to see the changes. One way to refresh the list of services shown in the Services menu is by using the services debugging tool `pbs`. This is a command-line tool located in `/System/Library/CoreServices` that provides useful services debugging features, such as refreshing the list of services or printing out the current list of registered services. Listing 3 shows an example of a command-line you can enter into the Terminal application to refresh the list of services for English and French.

__Listing 3__  Example use of pbs to refresh services.

```
/System/Library/CoreServices/pbs -existing_languages en fr
```


For more information on Services, including details on other services properties in the `Info.plist` file, please see the _[Services Implementation Guide](https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/SysServices/introduction.html#//apple_ref/doc/uid/10000101)_. For more information on Internationalization, Localization, bundles, resources and strings files, see the _Internationalization Programming Topics_ guide.

---

#### Document Revision History

| __Date__ | __Notes__ |
| 2010-03-29 | New document that describes how to localize the Services menu string for a service, including Automator created services. |

