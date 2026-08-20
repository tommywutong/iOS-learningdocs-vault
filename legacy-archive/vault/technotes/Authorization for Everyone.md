---
title: Authorization for Everyone
apple_id: DTS10003110
resource_type: Technical Note
platform: macOS
topic: Security
technology: Security
published: '2008-01-30'
source_url: https://developer.apple.com/library/archive/technotes/tn2095/_index.html
archived_at: '2026-07-26T19:53:50.336314Z'
---
> 导航：[总目录](../README.md) · [technotes](../_indexes/technotes.md)



Technical Note TN2095

# Authorization for Everyone

Mac OS X is a multi-user system that can be used in a variety of environments, each with radically different authorization requirements. For example, the iMac installed at your uncle's home is a completely open system, whereas an iMac installed in a university laboratory is extremely restricted.

There is no way that you, an application developer, can make authorization decisions that are appropriate for all of these environments. Instead, you should let the system administrator make those decisions. You can use Authorization Services to do this in a secure, standard way.

This technote is targeted at all Mac OS X application developers. It is of specific interest to those developers who have not used Authorization Services in the past. It explains how you can add authorization support to your application without compromising the out-of-box experience for your traditional customers.

[Introduction](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgmjqgaydgmjrgawugsbrfvjukq2ujfhu4mi)[Supporting Mac OS X version 10.3 and Later](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgmjqgaydgmjrgawugsbrfvjukq2ujfhu4mq)[Define Your Authorization Right](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgmjqgaydgmjrgawugsbrfvjukq2ujfhu4my)[Acquiring the Right](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgmjqgaydgmjrgawugsbrfvjukq2ujfhu4na)[A Tour of the Authorization Policy Database](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgmjqgaydgmjrgawugsbrfvjukq2ujfhu4ni)[Modifying the Policy Database](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgmjqgaydgmjrgawugsbrfvjukq2ujfhu4nq)[Adding the Right Programmatically](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgmjqgaydgmjrgawugsbrfvjukq2ujfhu4ny)[Localization](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgmjqgaydgmjrgawugsbrfvjukq2ujfhu4oa)[Bundle Reference Count Problems](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgmjqgaydgmjrgawugsbrfvjukq2ujfhu4oi)[Supporting Earlier Systems](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgmjqgaydgmjrgawugsbrfvjukq2ujfhu4mjq)[Summary](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgmjqgaydgmjrgawugsbrfvjukq2ujfhu4mjr)[References](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgmjqgaydgmjrgawugsbrfvjukq2ujfhu4mjs)[Document Revision History](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgmjqgaydgmjrgawvezlwnfzws33ojbuxg5dpoj4s2rdpnz2ey2lonncwyzlnmvxhiskel4yq)

## Introduction

Most developers who create applications for Mac OS X only consider authorization issues when the system's privileges model prevents them from performing their work. Using Authorization Services to implement this sort of application (called a __system-restricted__ application in the [Authorization Services documentation](https://developer.apple.com/documentation/Security/Conceptual/authorization_concepts/index.html)) is well understood, and there is a sample program, [BetterAuthorizationSample](https://developer.apple.com/samplecode/BetterAuthorizationSample/index.html), that demonstrate this clearly. However, Authorization Services is designed for more than just this. When you write a Mac OS X application, even if it has no system-restricted functionality, you should consider whether you can take advantage of Authorization Services. Specifically, you should think about whether a system administrator might want to restrict some features of your application to some subset of users. Consider the following examples:

- Imagine you're writing a CD burning application. A school system administrator might want to allow all users to burn data CDs, but only specific users to burn audio CDs.
- Imagine you're writing a consumer TV tuner application. You might want to allow a parent (the system administrator, in this case) to restrict certain channels from the children.

It's important to stress that the system privileges model does not prevent these sorts of activity. For example, as far as the CD driver is concerned, any user is allowed to burn discs. However, you can use Authorization Services to add an authorization layer to your application, which is then known as a __self-restricted__ application.

The ability to create a self-restricted application has always been part of Authorization Services. However, prior to Mac OS X version 10.3, there was no way to do this and maintain the simple out-of-box experience (that is, no password dialogs) expected by those users who administer their own system. Mac OS X version 10.3 introduced new Authorization Services routines that give you the best of both worlds.

- You can use Authorization Services so that a system administrator, if one exists, can restrict access to certain parts of your application.
- However, by default, these restrictions do not inconvenience users who administer their own systems.

The next eight sections explain how to achieve this ideal solution on Mac OS X version 10.3 and later. The last section, Supporting Earlier Systems, explains how to achieve a similar solution on earlier versions of Mac OS X.

[Back to Top](#)

## Supporting Mac OS X version 10.3 and Later

The following sections explain how you can use Authorization Services on Mac OS X version 10.3 and later to implement a self-restricted application which never displays a password dialog unless the system administrator configures it to do so. The first step is to define your custom authorization right. Next you must modify your application to acquire that right. To understand why this sometimes brings up an authorization dialog, you must understand the authorization policy database. Once you understand the database you can modify it to include a right specification for your custom right, either manually or programmatically. Finally, you can learn about two common gotchas when using this technique, namely, how to support a localizable prompt for your custom right and how to work around a bug in Authorization Services.

[Back to Top](#)

## Define Your Authorization Right

The first step is to work out which user-level operations a system administrator might want to restrict and define a right name for each of these authorized operations. Right names form a hierarchical namespace using reverse DNS notation. In this example I'll use the right name shown in Listing 1, which lists the company name first `com.apple.` then my organization within the company `dts.` then the product name `SelfRestrictedSample.` and finally the operation within that product (in this example it's the unimaginatively named `xyz`).

__Listing 1__  Defining a right name.

```
const char kXYZRightName[] = "com.apple.dts.SelfRestrictedSample.xyz";
```

Typically you define one right per authorized operation. For example, a CD burning application might define `com.SurfSoftware.SurfBurner.Burn.Audio` and `com.SurfSoftware.SurfBurner.Burn.Data`.

[Back to Top](#)

## Acquiring the Right

The next step is to modify your the code so that it acquires the right before doing the operation. An example of this is shown in Listing 2. The basic idea is to call `AuthorizationCopyRights`, passing it the name of the right you want to acquire (for example, the name defined in Listing 1). `AuthorizationCopyRights` will try to acquire the right on your behalf (possibly displaying a password dialog; we'll get to that in the next section) and return an error code indicating whether it was successful.

__Listing 2__  Obtaining the right.

```
extern OSStatus AcquireRight(const char *rightName)     // This routine calls Authorization Services to acquire      // the specified right. {     OSStatus                         err;     static const AuthorizationFlags  kFlags =                    kAuthorizationFlagInteractionAllowed                  | kAuthorizationFlagExtendRights;     AuthorizationItem   kActionRight = { rightName, 0, 0, 0 };     AuthorizationRights kRights      = { 1, &kActionRight };      assert(gAuthorization != NULL);      // Request the application-specific right.      err = AuthorizationCopyRights(         gAuthorization,         // authorization         &kRights,               // rights         NULL,                   // environment         kFlags,                 // flags         NULL                    // authorizedRights     );      return err; }
```

__Note:__ In Listing 2, `gAuthorization` is a reference to the application's authorization instance. This is set up by the startup code in Listing 5.

[Back to Top](#)

## A Tour of the Authorization Policy Database

If you modify your code as described above and then test it thoroughly, you'll find that under some circumstances it brings up a dialog asking you to enter an administrator user name and password. One easy way to reproduce this is to create a non-administrator user, log in as that user, then run your application and do the authorized operation. If you're shipping a consumer application, this authentication dialog is probably not what you want. However, before you try to prevent the dialog being displayed, you need to understand why it's displayed.

Authorization on Mac OS X is controlled by a policy database. In current versions of Mac OS X, this database is held in `/etc/authorization`. The database format is described in comments at the top of that file.

__Warning:__ The location and format of the policy database is subject to change. Do not code any of this knowledge into an application that you expect to be binary compatible with future releases of Mac OS X.

In fact, the format of the policy database has changed with Mac OS X version 10.3. This section uses the new format, although it should be relatively easy for to you to map the concepts described here on to the old format.

To understand why Authorization Services brings up dialog when you ask for a custom right, you have to understand a little about how the policy database works. Listing 3 shows an extract from the policy database as installed by Mac OS X version 10.3.

__Listing 3__  A policy database extract.

```xml
<?xml version="1.0" encoding="UTF-8"?> <!DOCTYPE plist PUBLIC [...]> <plist version="1.0"> <dict>     [...]     <key>rights</key>     <dict>         <key>system.device.dvd.setregion.initial</key>         <dict>             <key>class</key>             <string>user</string>             <key>comment</key>             <string>Used by the dvd player to set the  regioncode the first time. Note that changed the region code  after it has been set requires a different right  (system.device.dvd.setregion.change) Credentials remain valid  indefinitely after they've been obtained. An acquired  credential is shared amongst all clients.</string>             <key>group</key>             <string>admin</string>             <key>mechanisms</key>             <array>                <string>builtin:authenticate</string>             </array>             <key>shared</key>             <true/>         </dict>         [...]         <key>config.add.</key>         <dict>             <key>class</key>             <string>allow</string>             <key>comment</key>             <string>wildcard right for adding rights.              Anyone is allowed to add any (non-wildcard)              rights</string>         </dict>         [...]         <key></key>         <dict>             <key>class</key>             <string>rule</string>             <key>comment</key>             <string>All other rights will be matched by this rule. Credentials remain valid 5 minutes after they've been obtained. An acquired credential is shared amongst all clients.             </string>             <key>rule</key>             <string>default</string>         </dict>         [...]     </dict>     <key>rules</key>     <dict>         [...]     </dict> </dict> </plist>
```

The database consists of two dictionaries, `rights` and `rules`. In this discussion we'll concentrate on the `rights` dictionary. It contains a set of key/value pairs, called __right specifications__. The key is the right name and the value is information about the right, including a description of what the user must do to acquire the right. Listing 2 shows three rights.

- `system.device.dvd.setregion.initial` controls whether the user is allowed to set the initial region code for the DVD drive. By default, a user must prove that they are an administrator (in group `admin`) in order to set the DVD region.
- `config.add.` is a __wildcard right specification__ (it ends with a dot) that matches any right whose name starts with "`config.add.`". It controls whether a user is allowed to add a right specification to the policy database. By default any user is allowed to add a right specification.
- The right specification with an empty key string is known as the __default right specification__. To obtain this right a user must satisfy the default rule which, by default on current versions of Mac OS X, is to prove that they are an administrator.

When your program asks for a right, Authorization Services executes the following algorithm.

1. It searches the policy database for a right specification whose key exactly matches the right name.
2. If that fails, it searches the policy database for a wildcard right specification whose key matches the right name. If multiple are present, it uses the one with the longest key.
3. If that fails, it uses the default right specification.

Once it has found the appropriate right specification, Authorization Services evaluates the specification to decide whether to grant the right. In some cases this is easy (in the example in Listing 3  `config.add.` is always granted) but in other cases it can be more complex (for example, setting the DVD region requires that you enter an administrator password).

The presence of the default right has implications for self-restricted programs that use custom rights. Consider the code in Listing 1 and Listing 2. The requested right, `com.apple.dts.SelfRestrictedSample.xyz`, does not match any particular right specification in the policy database, and thus the default right specification is used. This is why the code in Listing 2 brings up an dialog asking for an administrator password.

__Note:__ You may notice that the code Listing 2 does not always bring up a password dialog. This is because of the way authorization credentials are shared. See [DTS QA 1277 Security Credentials](https://developer.apple.com/qa/qa2001/qa1277.html) for more information about this.

[Back to Top](#)

## Modifying the Policy Database

The obvious way to avoid this password dialog is to add a new right specification to the policy database that specifically allows anyone to acquire your custom right. For a system administrator this is easy. They can simply open the file with a text editor (or indeed Property List Editor), make the appropriate changes, and then save the changes back. For example, to add a right specification that allows anyone to acquire the right from Listing 1, you can simply add the text in Listing 4 to the policy database.

__Listing 4__  A 'always allow' right specification for the right from Listing 1.

```
 [...]         <key>com.apple.dts.SelfRestrictedSample.xyz</key>         <dict>             <key>rule</key>             <string>allow</string>         </dict>     [...]
```

__Note:__ The policy database file is only writable by root. You can edit it using a Terminal-based text editor run via [sudo](x-man-page://8/sudo), or with a GUI text editor that prompts you for an administrator password when you attempt to save privileged files (such as modern versions of BBEdit).

This approach is appropriate if you expect your customers to have a skilled system administrator handy (for example, if your application is sold for use in university laboratories). However, it's not appropriate for programs sold to the majority of Mac users, who do not have a dedicated system administrator. Furthermore, programmatically modifying the policy database file directly is not an option because, as mentioned earlier, the location and format of the database is subject to change.

The solution to this conundrum is the new Authorization database API added in Mac OS X version 10.3.

[Back to Top](#)

## Adding the Right Programmatically

The code in Listing 5 shows how you can add a right specification to the policy database using the Authorization Services routines released with Mac OS X version 10.3. The code is fairly straightforward. It first calls `AuthorizationCreate` to create a reference to the application's authorization instance. It then calls `AuthorizationRightGet` to see whether there is an existing right specification for its custom right. If that exists, the code does nothing: either the system administrator has already added their own right specification or the program has previously been run. If, however, no specification exists for the custom right, the code creates a new specification (using `AuthorizationRightSet`) that allows anyone to obtain the right.

__Listing 5__  Adding a right programmatically.

```c
static OSStatus SetupRight(     AuthorizationRef    authRef,      const char *        rightName,      CFStringRef         rightRule,      CFStringRef         rightPrompt )     // Checks whether a right exists in the authorization database      // and, if not, creates the right and sets up its initial value. {     OSStatus err;      // Check whether our right is already defined.      err = AuthorizationRightGet(rightName, NULL);     if (err == noErr) {          // A right already exists, either set up in advance by          // the system administrator or because this is the second          // time we've run. Either way, there's nothing more for          // us to do.      } else if (err == errAuthorizationDenied) {          // The right is not already defined. Let's create a          // right definition based on the rule specified by the          // caller (in the rightRule parameter). This might be          // kAuthorizationRuleClassAllow (which allows anyone to          // acquire the right) or          // kAuthorizationRuleAuthenticateAsAdmin (which requires          // the user to authenticate as an admin user)          // or some other value from "AuthorizationDB.h". The          // system administrator can modify this right as they          // see fit.          err = AuthorizationRightSet(             authRef,                // authRef             rightName,              // rightName             rightRule,              // rightDefinition             rightPrompt,            // descriptionKey             NULL,                   // bundle, NULL indicates main             NULL                    // localeTableName,          ); // NULL indicates                                     // "Localizable.strings"          // The ability to add a right is, itself, governed by a non-NULLdescriptionKey         // right. If we can't get that right, we'll get an error         // from the above routine. We don't want that error         // stopping the application from launching, so we          // swallow the error.          if (err != noErr) {             #if ! defined(NDEBUG)                 fprintf(                     stderr,                      "Could not create default right (%ld)\n",                      err                 );             #endif             err = noErr;         }     }      return err; }  extern OSStatus SetupAuthorization(void)     // Called as the application starts up. Creates a connection      // to Authorization Services and then makes sure that our      // right (kActionRightName) is defined. {     OSStatus err;      // Connect to Authorization Services.      err = AuthorizationCreate(NULL, NULL, 0, &gAuthorization);      // Set up our rights.      if (err == noErr) {         err = SetupRight(             gAuthorization,              kAlphaRightName,              CFSTR(kAuthorizationRuleClassAllow),              CFSTR("YOU MUST BE AUTHORIZED TO DO XYZ")         );     }     [...]      return err; }
```

This sequence ensures that the right specification is added to the policy database so the system administrator, if any, can then look through the policy database to examine the right specification created by your application, and set its value appropriately. Listing 6 shows how that right specification might look.

__Listing 6__  The right specification added by the code from Listing 5.

```
 [...]         <key>com.apple.dts.SelfRestrictedSample.xyz</key>         <dict>             <key>default-prompt</key>             <dict>                 <key></key>                 <string>YOU MUST BE AUTHORIZED TO DO XYZ</string>             </dict>             <key>rule</key>             <string>allow</string>         </dict>         [...]
```

`AuthorizationRightSet` has a lot of flexibility that is not demonstrated by Listing 5. The last two parameters allow you to supply a localized form of the right's prompt. This is explained in detail in the next section. In addition, the third parameter can either be a string (the name of one of the common rules for acquiring a right) or a dictionary (a detailed specification of how to acquire the right). You can read the header comments in `AuthorizationDB.h` (part of the Security framework) for more information about this.

[Back to Top](#)

## Localization

When you call `AuthorizationRightSet` you pass in three parameters that control the prompt displayed when the user must authenticate to obtain the right. These parameters are:

- `descriptionKey`, a `CFStringRef`
- `bundle`, a `CFBundleRef`
- `localeTableName`, a `CFStringRef`

The `bundle` and `localeTableName` parameters determine the localization table file that contains the prompt. If `bundle` is `NULL`, the routine uses the main bundle (as returned by `CFBundleGetMainBundle`). If `localeTableName` is `NULL`, the routine uses the `Localizable.strings` file in the specified bundle.

The `descriptionKey` parameter is used to look up a string within the localization table file. If this is `NULL`, no prompt is associated with the right.

When you call `AuthorizationRightSet` with a non-`NULL` `descriptionKey`, it iterates over every localization in the bundle. For each localization, it looks for the appropriate localization table file and then looks up the description key in that table. It then adds the resulting string to the `default-prompt` dictionary in the right specification.

For example, if your application has no localizations the code in Listing 5 generates the right specification in Listing 6. However, if you have two localizations, English (en) and Australian English (en_AU), the code in Listing 5 will generate the right specification shown in Listing 7.

__Listing 7__  The localized right specification added by the code from Listing 5.

```
 [...]         <key>com.apple.dts.SelfRestrictedSample.xyz</key>         <dict>             <key>default-prompt</key>             <dict>                 <key></key>                 <string>YOU MUST BE AUTHORIZED TO DO XYZ</string>                 <key>en</key>                 <string>You must be authorized to do xyz.</string>                 <key>en_AU</key>                 <string>Strewth! You must be authorised to do xyz.</string>             </dict>             <key>rule</key>             <string>allow</string>         </dict>         [...]
```

With this right specification you will see that, when prompted to authorize, a user who prefers English over Australian English will see the message "You must be authorized to do xyz" while a user who prefers Australian English over English will see "Strewth! You must be authorised to do xyz". For Australians it's very important that every sentence contains an expletive (and that "authorised" be spelt with an 's').

__Important:__ For the right specification shown in Listing 7 the authorization dialog will never appear because the rule always allows the right to be granted. You can see the authorization dialog by editing the authorization policy database and changing `<string>allow</string>` to `<string>authenticate-admin</string>`.

__Note:__ You can tell the system that you prefer Australian English over English by reordering the items in the Language panel of the International panel of System Preferences. You must first enable Australian English in the dialog displayed by clicking the "Edit List" button.

When choosing a prompt it's important that you use an entire sentence. The string displayed in the authorization dialog is composed of a number of distinct sentences, and your prompt string must fit into that model.

Finally, you should be aware that, currently, Authorization Services does not support localization synonyms (r. [3430642](rdar://problem/3430642)). Thus, the folder for the localization in your bundle must be "en.lproj", not "English.lproj".

[Back to Top](#)

## Bundle Reference Count Problems

There is one final gotcha associated with `AuthorizationRightSet`. Due to a bug (r. [3446163](rdar://problem/3446163)), `AuthorizationRightSet` will decrement the reference count of the bundle on which it operates. If you call `AuthorizationRightSet` multiple times the bundle reference count will go to zero and the bundle will be released. If you pass `NULL` to the `bundle` parameter of `AuthorizationRightSet`, this will release the main bundle and your application will quickly crash.

This bug is fixed in Mac OS X 10.4 and later. However, you can still work around the bug by artificially incrementing the reference count of the bundle. Listing 8 shows the recommended code for this workaround.

__Listing 8__  Recommended workaround for reference count bug.

```c
static OSStatus AuthorizationRightSetWithWorkaround(     AuthorizationRef    authRef,     const char *        rightName,     CFTypeRef           rightDefinition,     CFStringRef         descriptionKey,     CFBundleRef         bundle,     CFStringRef         localeTableName )     // The AuthorizationRightSet routine has a bug where it      // releases the bundle parameter that you pass in (or the      // main bundle if you pass NULL). If you do pass NULL and      // call AuthorizationRightSet multiple times, eventually the      // main bundle's reference count will hit zero and you crash.      //     // This routine works around the bug by doing an extra retain      // on the bundle. It should also work correctly when the bug      // is fixed.     //     // Note that this technique is not thread safe, so it's      // probably a good idea to restrict your use of it to      // application startup time, where the threading environment      // is very simple. {     OSStatus        err;     CFBundleRef     clientBundle;     CFIndex         originalRetainCount;      // Get the effective bundle.      if (bundle == NULL) {         clientBundle = CFBundleGetMainBundle();     } else {         clientBundle = bundle;     }     assert(clientBundle != NULL);      // Remember the original retain count and retain it. We force      // a retain because if the retain count was 1 and the bug still      // exists, the next call might decrement the count to 0, which      // would free the object.      originalRetainCount = CFGetRetainCount(clientBundle);     CFRetain(clientBundle);      // Call through to Authorization Services.      err = AuthorizationRightSet(         authRef,          rightName,          rightDefinition,          descriptionKey,          clientBundle,          localeTableName     );      // If the retain count is now magically back to its original      // value, we've encountered the bug and we print a message.     // Otherwise the bug must've been fixed and we just balance      // our retain with a release.      if ( CFGetRetainCount(clientBundle) == originalRetainCount ) {         fprintf(             stderr,              "AuthForAll: Working around <rdar://problems/3446163>\n"         );     } else {         CFRelease(clientBundle);     }      return err; }
```

[Back to Top](#)

## Supporting Earlier Systems

The Authorization Services routines described in the previous sections do not help if your application needs to run on earlier versions of Mac OS X. There are two strategies that you can use if you need compatibility with earlier systems.

- You can simply test for the presence of the new Authorization Services routines and do no authorization at all if they're not present. This has the benefit of simplicity, although system administrators who have not updated to Mac OS X version 10.3 do not get any control over who can use which features of your application.
- You can attempt to emulate `AuthorizationRightGet` by reading the authorization policy database directly. This directly contradicts the advice given earlier, but it is acceptable if you only do it on older systems, where the format and location of the authorization policy database will not change. On Mac OS X version 10.3 and later, where the new Authorization Services routines are present, you must use the new routines and not assume anything about the authorization policy database format.

[Back to Top](#)

## Summary

Authorization Services allows you to create a self-restricted application, wherein a system administrator can control which users are allowed to access which features. With Mac OS X version 10.3 you can implement this without compromising the out-of-box experience for your typical customers. It's easy to adopt Authorization Services and doing so will make the system administrators of the world very happy.

[Back to Top](#)

## References

- [Inside Mac OS X: Performing Privileged Operations With Authorization Services](https://developer.apple.com/documentation/Security/Conceptual/authorization_concepts/index.html)
- [Q&A 1277 Security Credentials](https://developer.apple.com/qa/qa2001/qa1277.html)
- [BetterAuthorizationSample Code](https://developer.apple.com/samplecode/BetterAuthorizationSample/index.html)

[Back to Top](#)

---

#### Document Revision History

| __Date__ | __Notes__ |
| 2008-01-30 | Updated to include BetterAuthorizationSample References. |
| 2003-10-23 | New document that describes applications of Authorization Services beyond simple privilege requesting. |

