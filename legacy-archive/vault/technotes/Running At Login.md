---
title: Running At Login
apple_id: DTS40007991
resource_type: Technical Note
platform: macOS
topic: Security
technology: Security
published: '2008-09-16'
source_url: https://developer.apple.com/library/archive/technotes/tn2228/_index.html
archived_at: '2026-07-26T19:54:09.561650Z'
---
> 导航：[总目录](../README.md) · [technotes](../_indexes/technotes.md)



Technical Note TN2228

# Running At Login

This technote explains how you can write code that is coordinated with the login process. This is useful in a number of circumstances. For example, if you're developing a product for managed installations that resets the user's preferences to some known state, you want your code to run after the user's home directory is mounted but before any user processes have run. Historically such products might have used the login hook, but the technique described in this technote (an authorization plug-in) has a number of important advantages over the login hook.

This technote is targeted at Mac OS X developers whose products must be coordinated with the GUI login process.

[Introduction](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgnbqgaydoojzgewugsbrfvjukq2ujfhu4mi)[Close But No Cigar](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgnbqgaydoojzgewugsbrfvjukq2ujfhu4mq)[Login Hook](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgnbqgaydoojzgewugsbrfvjvkqstivbviskpjyza)[Daemon](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgnbqgaydoojzgewugsbrfvjvkqstivbviskpjyzq)[Agent](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgnbqgaydoojzgewugsbrfvjvkqstivbviskpjy2a)[Do The Right Thing](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgnbqgaydoojzgewugsbrfvjukq2ujfhu4nq)[Getting Started](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgnbqgaydoojzgewugsbrfvjvkqstivbviskpjy3a)[Always Mount A Scratch Monkey](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgnbqgaydoojzgewugsbrfvjvkqstivbviskpjy3q)[Fast User Switching](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgnbqgaydoojzgewugsbrfvjvkqstivbviskpjy4a)[Debugging](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgnbqgaydoojzgewugsbrfvjvkqstivbviskpjy4q)[Installing Your Plug-in](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgnbqgaydoojzgewugsbrfvjvkqstivbviskpjyyta)[Context Issues](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgnbqgaydoojzgewugsbrfvjvkqstivbviskpjyytc)[Authorization Auxiliary Information](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgnbqgaydoojzgewugsbrfvjvkqstivbviskpjyyte)[Danger Will Robinson](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgnbqgaydoojzgewugsbrfvjukq2ujfhu4mju)[Allowing Home Directory Access](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgnbqgaydoojzgewugsbrfvjvkqstivbviskpjyyti)[Preventing Home Directory Access](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgnbqgaydoojzgewugsbrfvjvkqstivbviskpjyytk)[Mach Bootstrap Namespace Issues](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgnbqgaydoojzgewugsbrfvjvkqstivbviskpjyytm)[Be Nice To Your Host](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgnbqgaydoojzgewugsbrfvjvkqstivbviskpjyyto)[Host Death Issues](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgnbqgaydoojzgewugsbrfvjvkqstivbviskpjyytq)[Further Reading](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgnbqgaydoojzgewugsbrfvjukq2ujfhu4mrq)[Document Revision History](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgnbqgaydoojzgewvezlwnfzws33ojbuxg5dpoj4s2rdpnz2ey2lonncwyzlnmvxhiskel4yq)

## Introduction

In some circumstances it is necessary to run code as the user logs in, and to guarantee that the code runs to completion before the login can continue. For example, if you're developing an administrative product that wants to reset the user's preferences to a particular state, you have to do that after the home directory is mounted (otherwise, your product wouldn't work for FileVault users or for users with network home directories) but before any applications have had a chance to run and read those preferences.

This technote describes the recommended approach for running code that's coordinated with the login process. It starts with an overview of the techniques that have been used for this in the past, but which are fundamentally flawed (Close But No Cigar). It then describes the recommended technique, namely, creating an authorization plug-in (Do The Right Thing). Finally, it concludes with a discussion of some of the gotchas associated with this technique (Danger Will Robinson).

__Important:__ Formal support for authorization plug-ins was added in Mac OS X 10.4. If you need to do this sort of thing on earlier systems, please contact [Developer Technical Support](mailto:dts.apple.com).

__Important:__ This technote only covers GUI logins; it does not cover other types of logins (for example, SSH logins or AppleShare logins).

__Note:__ This technote only discusses login; it does not cover issues related to logout. Specifically, while the authorization plug-in technique described in this technote is a good alternative for the login hook, there is currently no equivalent replacement for the logout hook
(r. [4905756](rdar://problem/4905756))
.

It's important to understand when an authorization plug-in is not appropriate. Two common cases are:

- If you wish to present a user interface that runs asynchronously with respect to the login process (for example, you're developing assistive technology for Mac OS X and you want to provide assistance at login time), you should investigate creating a pre-login launchd agent, as illustrated by [Sample Code 'PreLoginAgents'](https://developer.apple.com/samplecode/PreLoginAgents/index.html).
- If you wish to present a login user interface that supplants the standard user interface displayed at login time (for example, you want to display the user interface for a fingerprint reader), you should investigate `SFAuthorizationPluginView`. [Sample Code 'NameAndPassword'](https://developer.apple.com/samplecode/NameAndPassword/index.html) shows an example of how to do this.

[Back to Top](#)

## Close But No Cigar

Historically developers have used a number of techniques for running code at login time, and most of them are inadequate for various reasons. This section describes those techniques and their problems.

### Login Hook

The login hook is documented in [System Startup Programming Topics](https://developer.apple.com/documentation/MacOSX/Conceptual/BPSystemStartup/Articles/CustomLogin.html#//apple_ref/doc/uid/20002134). It has a number of drawbacks and is generally considered to be deprecated. Specifically:

- There is only one login hook, which means that it's not suitable for shrink wrap developers because you can't be guaranteed that the user hasn't already installed some other software that's using it. In general, you should consider the login hook to be reserved for use by site administrators.
- The login hook is run at one specific time during the login process (after the home directory has been mounted), which is not flexible enough to cover all circumstances.

### Daemon

Various developers have tried to do this sort of thing from a daemon (a launchd daemon or a startup item). There are a number of problems with using a daemon for this sort of thing.

- It is subject to race conditions. Mac OS X's startup is highly asynchronous. Thus it's possible (albeit somewhat unlikely) that the user might log in before your daemon has even been started.
- There's no guarantee that a daemon can access the home directory (especially for FileVault and network home directory users), which makes them unsuitable for certain tasks.

See [Technical Note TN2083, 'Daemons and Agents'](https://developer.apple.com/technotes/tn2005/tn2083.html) for more information about daemons.

### Agent

Various developers have tried to use an agent (a launchd agent, a login item, or global login item) to do this sort of thing. This technique is unsuitable for a number of reasons.

- It is subject to race conditions. Agents are launched after login in parallel with other items of their class. Thus, there's no way to be sure that the changes made by an agent will affect its peers.
- Agents always run after the home directory has been mounted, which makes them unsuitable for certain tasks.

See [Technical Note TN2083, 'Daemons and Agents'](https://developer.apple.com/technotes/tn2005/tn2083.html) for more information about agents.

[Back to Top](#)

## Do The Right Thing

The recommended approach for running code that's coordinated with the login process is to create an __authorization plug-in__.

__Important:__ To understand the rest of this section you will need a basic understanding of Authorization Services. If you've not used Authorization Services before, I suggest you read the [Authorization Concepts](https://developer.apple.com/documentation/Security/Conceptual/authorization_concepts/02authconcepts/chapter_2_section_1.html#//apple_ref/doc/uid/TP30000995-CH205-TP9) chapter of [Performing Privileged Operations With Authorization Services](https://developer.apple.com/documentation/Security/Conceptual/authorization_concepts/01introduction/chapter_1_section_1.html).

When the user logs in, `loginwindow` tries to acquire the `system.login.console` authorization right. If you look at the right definition in the authorization database (currently `/etc/authorization`), you'll see something like Listing 1. Specifically, the `mechanisms` array contains a list of mechanism strings associated with this authorization right.

__Listing 1__  The console login authorization right on Mac OS X 10.5

```
<key>system.login.console</key> <dict>     <key>class</key>     <string>evaluate-mechanisms</string>     <key>comment</key>     <string>Login mechanism based rule. Not for general use, yet.</string>     <key>mechanisms</key>     <array>         <string>builtin:smartcard-sniffer,privileged</string>         <string>loginwindow:login</string>         <string>builtin:reset-password,privileged</string>         <string>builtin:auto-login,privileged</string>         <string>builtin:authenticate,privileged</string>         <string>HomeDirMechanism:login,privileged</string>         <string>HomeDirMechanism:status</string>         <string>MCXMechanism:login</string>         <string>loginwindow:success</string>         <string>loginwindow:done</string>     </array> </dict>
```

__Warning:__ The location of the authorization database is subject to change. To ensure long-term binary compatibility you must access the database using the authorization database API.

__Note:__ The exact definition of the `system.login.console` authorization right varies over time. The techniques described in this technote are carefully crafted to avoid too much dependency on the exact right definition and will be supported for the foreseeable future.

When `loginwindow` tries to acquire the `system.login.console` right, Authorization Services runs each of the mechanisms described by the strings in the array, in turn. Each string includes the name of the authorization plug-in (before the colon) and the name of the mechanism implemented by that plug-in (after the colon). It optionally ends with ",privileged", to indicate that the mechanism should be run as root (more about this in Context Issues).

It's possible to write an authorization plug-in that implements a custom mechanism, and then add the name of that mechanism to this array and have it called at login time. This happens for both manual and automatic logins.

The position of your mechanism in the array determines when it will be run. The default right specification for `system.login.console` lists one mechanism (`loginwindow:login`) that presents the login window user interface and another (`HomeDirMechanism:login,privileged`) that mounts the user's home directory (if, say, it's a network home directory, or on a FileVault disk image). When you install a custom mechanism, you should place it so that it runs at the appropriate point relative to these standard mechanisms. The position you choose depends on the nature of your product. For example:

- In some circumstances you might want to run before the user's home directory is mounted. For example, you might be implementing a network file system and you want to set up the user's credentials so that the home directory mounting process works properly. In that case you should install your mechanism before any instance of `HomeDirMechanism` in the array.
- In some circumstances you might want to run after the user's home directory is mounted. For example, you might be writing a tool for managed installations that sets up certain preferences in certain ways, and you can't access the user's preferences folder until their home directory is mounted. In that case you should install your mechanism after all instances of `HomeDirMechanism` in the array.

__Warning:__ Regardless of the position of your mechanism in this array, your code will run in an unusual environment, with numerous gotchas. Danger Will Robinson describes these gotchas in more detail.

### Getting Started

The best place to start when developing an authorization plug-in is [Sample Code 'NullAuthPlugin'](https://developer.apple.com/samplecode/NullAuthPlugin/index.html). Grab the sample and start customizing!

The remainder of this section describes some of the issues that you might encounter while creating your plug-in.

### Always Mount A Scratch Monkey

__Warning:__ If your authorization plug-in is not found, or the mechanism it implements fails, you will not be able to log in to the system via the GUI.

The easiest way to avoid being bitten by this is to enable SSH logins on your machine (Remote Login in the Sharing panel of System Preferences). That way, if anything goes wrong, you can log in via SSH to debug and correct it.

If you run into problems and you haven't enabled SSH (or you don't have access to another machine to use as the SSH client), you can fix things by booting the machine in [single user mode](http://support.apple.com/kb/HT1492).

Regardless, I strongly recommend that you make a backup of your authorization database before doing any work with authorization plug-ins. Listing 2 shows how to do this on current systems.

__Listing 2__  Backing up and restoring the authorization database

```
$ # Backup the authorization database $ sudo cp /etc/authorization /etc/authorization-orig $ # Restore from the backup $ sudo cp /etc/authorization-orig /etc/authorization
```

### Fast User Switching

In many cases you do not need to restart the machine to test your authorization plug-in. Instead, you can enable fast user switching (in the Account panel of System Preferences) and switch directly to the login window. From there, log in as a different user. Your authorization plug-in's mechanisms will be invoked in much the same way as they would be at startup time.

### Debugging

The mechanics of debugging an authorization plug-in can be challenging. For example:

- You will definitely need two machines because the authorization plug-in runs at login time, which means there's no way to use the debugger on the machine running the plug-in.
- It is possible to use Xcode's two-machine debugging facility to debug your plug-in in the Xcode IDE. See [Technical Note TN2108, 'Debugging An Authorization Plug-In With Xcode'](https://developer.apple.com/technotes/tn2008/tn2108.html) for instructions on how to do this.
- In many cases, however, it's easier to simply SSH into the machine and run command line GDB.
- Remember that your code is a plug-in that's hosted in a system process (see Context Issues for details), and thus you will need to run GDB as root (typically using [sudo](x-man-page://8/sudo)).

You can also add copious logging to your plug-in and debug it by trolling through the logs. [Sample Code 'NullAuthPlugin'](https://developer.apple.com/samplecode/NullAuthPlugin/index.html) shows how to do that using [syslog](x-man-page://3/syslog); a more modern example would use [ASL](https://developer.apple.com/library/archive/technotes/tn2228/<x-man-page:/3/asl>). For an example of how to use ASL, see [Sample Code 'SampleD'](https://developer.apple.com/samplecode/SampleD/index.html).

### Installing Your Plug-in

On Mac OS X 10.5 and later, third party authorization plug-ins should be installed in `/Library/Security/SecurityAgentPlugins`. On earlier systems, they must be installed in `/System/Library/CoreServices/SecurityAgentPlugins`. The files and directories that make up the plug-in must be owned by `root` with an owning group of `wheel`, and they must not be writable by anyone other than root.

Once you have installed your plug-in, you must activate it by modifying the authorization database. During development you can do this by editing the authorization database file (currently `/etc/authorization`) directly. However, for wide scale deployment you must modify the database using the APIs provided by the Security framework (`<Security/AuthorizationDB.h>`).

Listing 3 shows an example of how to do this. The top-level routine, `AddMechanismToConsoleLoginRight`, will add a mechanism to the `mechanisms` array of the `system.login.console` authorization right, either before or after `HomeDirMechanism`.

__Listing 3__  Activating an authorization plug-in

```c
#include <assert.h> #include <CoreServices/CoreServices.h> #include <Security/Security.h>  static void InsertMechanismRelativeToHomeDirMechanism(     CFMutableArrayRef   mechanisms,     CFStringRef         mechanismStr,     Boolean             beforeHomeDirMechanism )     // Adds the mechanism specified mechanismStr to the mechanisms array.      // If beforeHomeDirMechanism is true, mechanismStr is added immediately      // before the first instance of "HomeDirMechanism"; otherwise it is added      // after the last instance. {     CFIndex         mechanismCount;     CFIndex         mechanismIndex;     CFIndex         insertionIndex;     Boolean         isHomeDirMechanism;     CFStringRef     mechanism;      assert(mechanisms != NULL);     assert(mechanismStr != NULL);      mechanismCount = CFArrayGetCount(mechanisms);     insertionIndex = mechanismCount; // add after last entry by default     for (mechanismIndex = 0; mechanismIndex < mechanismCount; mechanismIndex++) {         mechanism = CFArrayGetValueAtIndex(mechanisms, mechanismIndex);         isHomeDirMechanism = (                (mechanism != NULL)              && (CFGetTypeID(mechanism) == CFStringGetTypeID())              && CFStringHasPrefix(mechanism, CFSTR("HomeDirMechanism:"))         );         if (isHomeDirMechanism) {             if (beforeHomeDirMechanism) {                 insertionIndex = mechanismIndex;                 break;             } else {                 insertionIndex = mechanismIndex + 1;             }         }     }     CFArrayInsertValueAtIndex(mechanisms, insertionIndex, mechanismStr); }  static OSStatus AddMechanismToConsoleLoginRight(     AuthorizationRef    authRef,     CFStringRef         authPluginName,     CFStringRef         mechanismID,     Boolean             privileged,     Boolean             beforeHomeDirMechanism )     // Adds the mechanism specified authPluginName and mechanismID to the      // "mechanisms" array of the "system.login.console" right definition.      // If privileged is true, the mechanism runs as root. If      // beforeHomeDirMechanism is true, mechanismStr is added immediately      // before the first instance of "HomeDirMechanism"; otherwise it is added      // after the last instance. {     OSStatus                err;     CFStringRef             mechanismStr;     CFDictionaryRef         rightDict;     CFStringRef             authClass;     CFArrayRef              authMechanisms;     CFMutableArrayRef       newMechanisms;     CFMutableDictionaryRef  newRightDict;     static const char *     kConsoleLoginRightName = "system.login.console";      assert(authRef != NULL);     assert(authPluginName != NULL);     assert(mechanismID != NULL);      mechanismStr = NULL;     rightDict = NULL;     newRightDict = NULL;     newMechanisms = NULL;      // Construct a correctly formatted mechanism string.      err = noErr;     mechanismStr = CFStringCreateWithFormat(         NULL,          NULL,          CFSTR("%@:%@%@"),          authPluginName,          mechanismID,          (privileged ? CFSTR(",privileged") : CFSTR(""))     );     if (mechanismStr == NULL) {         err = coreFoundationUnknownErr;     }      // Get the right definition and check the class is "evaluate-mechanisms".      if (err == noErr) {         err = AuthorizationRightGet(kConsoleLoginRightName, &rightDict);     }     if (err == noErr) {         authClass = (CFStringRef) CFDictionaryGetValue(rightDict, CFSTR("class"));         if ( (authClass == NULL)            || (CFGetTypeID(authClass) != CFStringGetTypeID()) ) {             err = coreFoundationUnknownErr;         } else if ( ! CFEqual(authClass, CFSTR("evaluate-mechanisms")) ) {             err = errAuthorizationInternal;         }     }      // Get the mechanisms array and check whether our mechanism is already present.      if (err == noErr) {         authMechanisms = (CFArrayRef) CFDictionaryGetValue(             rightDict,              CFSTR("mechanisms")         );         if ( (authMechanisms == NULL)            || (CFGetTypeID(authMechanisms) != CFArrayGetTypeID()) ) {             err = coreFoundationUnknownErr;         }     }     if ( (err == noErr)        && ! CFArrayContainsValue(                authMechanisms,                 CFRangeMake(0, CFArrayGetCount(authMechanisms)),                 mechanismStr            ) ) {          // If it's not, add our mechanism and write back the right definition.          newMechanisms = CFArrayCreateMutableCopy(NULL, 0, authMechanisms);         if (newMechanisms == NULL) {             err = coreFoundationUnknownErr;         }         if (err == noErr) {             InsertMechanismRelativeToHomeDirMechanism(                 newMechanisms,                  mechanismStr,                  beforeHomeDirMechanism             );              newRightDict = CFDictionaryCreateMutableCopy(NULL, 0, rightDict);             if (newRightDict == NULL) {                 err = coreFoundationUnknownErr;             }             if (err == noErr) {                 CFDictionarySetValue(                     newRightDict,                      CFSTR("mechanisms"),                      newMechanisms                 );                  err = AuthorizationRightSet(                     authRef,                      kConsoleLoginRightName,                      newRightDict,                      NULL,                      NULL,                      NULL                 );             }         }     }      // Clean up.      if (newRightDict != NULL) {         CFRelease(newRightDict);     }     if (newMechanisms != NULL) {         CFRelease(newMechanisms);     }     if (rightDict != NULL) {         CFRelease(rightDict);     }     if (mechanismStr != NULL) {         CFRelease(mechanismStr);     }      return err; }
```

You do not need to restart the system for it to recognize the new authorization plug-in or your changes to the authorization database.

### Context Issues

Authorization mechanisms run in a very unusual context, the specific values of which depend on whether you install your mechanisms as privileged or not. Table 1 is a brief summary of the context inherited by each type of authorization mechanism.

__Note:__ For more information about the context issues covered by this table, see [Technical Note TN2083, 'Daemons and Agents'](https://developer.apple.com/technotes/tn2005/tn2083.html).

__Table 1__  Authorization mechanism context

| Privileged | UI OK? | EUID / RUID [1] | Bootstrap Namespace | Process [2] |
| yes | no | 0 / 0 | see below [3] | authorizationhost |
| no | yes | 92 / 92 | see below [3] | SecurityAgent |

__Notes:__

1. Effective user ID and real user ID, respectively.
2. This information is provided for debugging purposes only. The actual process used to run authorization mechanisms should not be considered part of the authorization plug-in API.
3. Authorization mechanisms have to be very careful when dealing with Mach bootstrap namespaces. This is discussed in more detail in Mach Bootstrap Namespace Issues.
4. UID 92 is `_securityagent`. It is a special user ID used to run the `SecurityAgent` process, and thus the login window user interface.

In many cases it may be necessary for your plug-in to implement a pair of cooperating authorization mechanisms, one that runs privileged and one that runs non-privileged. For example, if you're writing an authorization plug-in that completely resets the user's home directory on login, you may need two mechanisms:

- A privileged mechanism to actually modify the user's home directory.
- A non-privileged mechanism to display progress information.

This is because a privileged mechanism can't display UI and a non-privileged mechanism runs as UID 92, and thus can't modify the user's home directory.

If you need to create two or more authorization mechanisms, you can use authorization auxiliary information to communicate between them, as described in the next section.

### Authorization Auxiliary Information

Authorization Services maintains two dictionaries of __auxiliary information__ that it passes from one plug-in to the next. These are the __context__ and the __hints__ discussed in detail in the [Authorization Plug-in Reference](https://developer.apple.com/documentation/Security/Reference/AuthorizationPluginRef/Reference/reference.html).

There are two common uses for this auxiliary information:

1. If you've created two cooperating mechanisms, you can pass information between them by way of the authorization hints. That is, the first mechanism that runs can deposit information in the hints to be picked up by the second mechanism.
2. If you need information about the user that is currently logging in, you can get it from the authorization context.

As an example of point 2, if you're developing an authorization plug-in that resets the user's preferences, you will need to know the user ID of the user who is logging in (so you can switch to that user when writing to the file system) and the path to their home directory. You can get these from the "uid" and "home" context values, respectively. Listing 4 shows how you can get the "uid" value from the authorization context.

__Listing 4__  Accessing the 'uid' context value

```c
static uid_t GetUIDFromContext(     const AuthorizationCallbacks *  authServerFuncs,      AuthorizationEngineRef          engine )     // Returns the "uid" value from the authorization context, or      // -2 (nobody) if the value is not present or can't be fetched.      // authServerFuncs is the value passed to your plug-in's      // AuthorizationPluginCreate routine. engine is the value      // passed to your MechanismCreate routine. {     OSStatus                    err;     uid_t                       result;     AuthorizationContextFlags   junkFlags;     const AuthorizationValue *  value;      assert(authServerFuncs != NULL);     assert(engine != NULL);      result = (uid_t) -2;     err = authServerFuncs->GetContextValue(engine, "uid", &junkFlags, &value);     if ( (err == noErr) && (value->length == sizeof(uid_t)) ) {         result = * (const uid_t *) value->data;     } else {         // [... log the failure ...]     }      return result; }
```

[Back to Top](#)

## Danger Will Robinson

The following sections describe a number of non-obvious pitfalls associated with creating an authorization plug-in.

### Allowing Home Directory Access

If you're writing an authorization mechanism that wants to access the user's home directory, you must consider file system permissions. Specifically, non-privileged authorization mechanisms run as effective user ID (EUID) 92 (`_securityagent`). Standard permissions checking will typically prevent them from accessing the user's home directory.

On the other hand privileged authorization mechanisms run as EUID 0 (`root`). Thus, you might think that such mechanisms can always access the user's home directory (assuming they run after `HomeDirMechanism`), however, that's not the case. Most network file systems treat root accesses as if they were accesses by the user `nobody`. Thus, if the user has a network home directory, a privileged authorization mechanism will have to set its EUID to that of the user logging in before being able to access the user's home directory.

You can get the user ID of the user logging in from the authorization context (see Authorization Auxiliary Information). You can change the EUID using `pthread_setugid_np` as discussed in Be Nice To Your Host.

### Preventing Home Directory Access

If you're writing an authorization mechanism that runs before `HomeDirMechanism` (that is, before the user's home directory is guaranteed to be mounted), you must be careful not to try and access their home directory. This can be tricky, especially in situations where you have to switch the EUID to the UID of the logging in user, because some common frameworks access the home directory in non-obvious ways.

The framework that causes most problems in this respect is Core Foundation. Core Foundation tries to access the user's home directory to determine their default text encoding (stored in the file `~/.CFUserTextEncoding`). If you switch the EUID to the UID of the logging in user and then call CF, you may have problems when Core Foundation accesses this file. You can prevent this access by setting an environment variable that tells Core Foundation the default text encoding to use. The environment variable name is `__CF_USER_TEXT_ENCODING`. Its value should be constructed with the format string "0x%X:0:0", where %X is replaced by the UID of the logging in user.

__Important:__ Setting `__CF_USER_TEXT_ENCODING` may be necessary but not sufficient to ensure that your code runs correctly in this context. Mac OS X's many and various frameworks are littered with references to the user's home directory, and there's no list of what routines are safe to call in this context. Ultimately you will just have to try things and see what works.

To maximize your chance of ongoing binary compatibility, you should try to limit yourself to low-level frameworks. Specifically, frameworks that are daemon-safe should be more-or-less safe in the context. On the other hand frameworks that are not daemon-safe are almost certainly going to cause problems.

See [Technical Note TN2083, 'Daemons and Agents'](https://developer.apple.com/technotes/tn2005/tn2083.html) for a list of daemon-safe frameworks.

### Mach Bootstrap Namespace Issues

Your authorization mechanism inherits a very unusual Mach bootstrap namespace. The namespace is ultimately destined to become the GUI per-session bootstrap namespace for the user logging in. However, while the login is in progress, the availability of Mach-based services can vary in non-obvious ways.

__Warning:__ Your authorization plug-in must not register services in its bootstrap namespace, nor hold a reference to the namespace that persists beyond the execution of your authorization mechanisms. Both of these activities will yield unspecified results.

__Note:__ For detailed information about Mach bootstrap namespaces, see [Technical Note TN2083, 'Daemons and Agents'](https://developer.apple.com/technotes/tn2005/tn2083.html).

Table 2 shows how you can access Mach services registered in specific namespaces on Mac OS X 10.5 and later.

__Table 2__  Accessing Mach services from an authorization mechanism on Mac OS X 10.5

| Mach Bootstrap Namespace | How To Access |
| global | always accessible |
| per-user | see [1] below |
| pre-login | always accessible |
| GUI per-session | never accessible |
| non-GUI per-session | never accessible |

__Notes:__

1. To access per-user services (like the Kerberos credentials cache, `edu.mit.Kerberos.CCacheServer`) you must switch your EUID to that of the UID of the logging in user. This has a number of important consequences.

   - Your mechanism must run privileged, otherwise it will run as EUID 92 (`_securityagent`) and be unable to switch its EUID.
   - Your mechanism must run after the "uid" context value has been set up (see Authorization Auxiliary Information). On current systems this means it must run after the `builtin:authenticate,privileged` mechanism. This won't be a problem if you run immediately before or immediately after `HomeDirMechanism`.

Table 3 shows the same information for Mac OS X 10.4.x.

__Table 3__  Accessing Mach services from an authorization mechanism on Mac OS X 10.4.x

| Mach Bootstrap Namespace [1] | How To Access |
| global | always accessible |
| pre-login / GUI per-session | see [2] below |
| non-GUI per-session | never accessible |

__Notes:__

1. Mac OS X 10.4.x does not support per-user or non-GUI per-session namespaces.
2. On Mac OS X 10.4.x there is no clear transition between the pre-login context and the GUI per-session context. Your authorization mechanism inherits a reference to a namespace that is initially the pre-login namespace and then, once login is complete, becomes the GUI per-session namespace. However, most GUI per-session services are not registered until after authorization is complete (and thus, aren't available to your mechanism).

### Be Nice To Your Host

Your authorization plug-in is loaded and executed within a system process (see Context Issues for the details). You should attempt to be as nice to your host process as possible. Specifically:

- Try to avoid changing process-wide values. For example, if you change the current working directory you could cause problems for other threads running within the same process. If there is a per-thread alternative available, use it!
- As a corollary to above, try to avoid relying on any process-wide values.
- If you must change a process-wide value, change it back when you're done. Also try to limit the amount of code that executes while the value is changed.
- Do not use excessive resources. For example, don't allocate so much memory that the host process runs out of virtual address space.
- If your plug-in uses Objective-C, add a prefix to your class names to avoid conflicts with classes used by the host process (and by other plug-ins). [Coding Guidelines for Cocoa](https://developer.apple.com/documentation/Cocoa/Conceptual/CodingGuidelines/index.html) has some useful advice on this topic.

One process-wide value that deserves special attention is the effective user ID (EUID). There are circumstances where your authorization plug-in should switch the EUID to that of the user logging in. In these circumstances you should avoid using `seteuid`, because it modifies the EUID for the entire process. Rather, you should use the per-thread alternative, `pthread_setugid_np`; Listing 5 shows an example of how to use this routine.

__Listing 5__  Creating a file as a specific user

```c
#include <assert.h> #include <errno.h> #include <fcntl.h> #include <pthread.h> #include <unistd.h> #include <sys/stat.h> #include <sys/kauth.h>  static int CreateFileAsUserGroup(const char *path, uid_t uid, gid_t gid)     // Creates a file and returns the file descriptor. On error, returns      // -1 and errno is set to an error value. {     int     err;     int     fd;     int     junk;      fd = -1;      err = pthread_setugid_np(uid, gid);     if (err == 0) {         fd = open(path, O_CREAT | O_EXCL | O_RDWR, S_IRWXU);          err = errno; // preserve errno across the pthread_setugid_np         junk = pthread_setugid_np(KAUTH_UID_NONE, KAUTH_GID_NONE);         assert(junk == 0);         errno = err;     }     return fd; }
```

__Note:__ While `pthread_setugid_np` is not currently documented
(r. [4738641](rdar://problem/4738641))
it is fully supported on all systems that support authorization plug-ins.

### Host Death Issues

The system process that hosts your authorization plug-in will typically terminate at the end of the login process, which means that your authorization plug-in will not continue to execute during the login session. If you wish to maintain a presence during the login session, you should use some other mechanism (typically a GUI launchd agent or a global login item).

__Warning:__ Do not attempt to maintain a presence during the login session by forking from within your authorization plug-in. The resulting process will inherit an unusual execution context which is likely to lead to long-term binary compatibility problems.

For more information about launchd agents and login items, see [Technical Note TN2083, 'Daemons and Agents'](https://developer.apple.com/technotes/tn2005/tn2083.html)

[Back to Top](#)

## Further Reading

- [ADC Reference Library > Security > Authorization](https://developer.apple.com/referencelibrary/Security/idxAuthorization-date.html)
- [Performing Privileged Operations With Authorization Services](https://developer.apple.com/documentation/Security/Conceptual/authorization_concepts/01introduction/chapter_1_section_1.html)
- [Authorization Plug-in Reference](https://developer.apple.com/documentation/Security/Reference/AuthorizationPluginRef/Reference/reference.html)
- [Secure Coding Guide](https://developer.apple.com/documentation/Security/Conceptual/SecureCodingGuide/index.html )
- [System Startup Programming Topics](https://developer.apple.com/documentation/MacOSX/Conceptual/BPSystemStartup/Articles/CustomLogin.html#//apple_ref/doc/uid/20002134)
- [Coding Guidelines for Cocoa](https://developer.apple.com/documentation/Cocoa/Conceptual/CodingGuidelines/index.html)
- [Technical Note TN2083, 'Daemons and Agents'](https://developer.apple.com/technotes/tn2005/tn2083.html)
- [Technical Note TN2108, 'Debugging An Authorization Plug-In With Xcode'](https://developer.apple.com/technotes/tn2008/tn2108.html)
- [Sample Code 'NullAuthPlugin'](https://developer.apple.com/samplecode/NullAuthPlugin/index.html)
- [Sample Code 'NameAndPassword'](https://developer.apple.com/samplecode/NameAndPassword/index.html)
- [Sample Code 'PreLoginAgents'](https://developer.apple.com/samplecode/PreLoginAgents/index.html)
- [Sample Code 'SampleD'](https://developer.apple.com/samplecode/SampleD/index.html)
- [seteuid](x-man-page://2/seteuid) man page
- [ASL](https://developer.apple.com/library/archive/technotes/tn2228/<x-man-page:/3/asl>) man page
- [syslog](x-man-page://3/syslog) man page
- [How to start up in single-user or verbose mode](http://support.apple.com/kb/HT1492)

[Back to Top](#)

---

#### Document Revision History

| __Date__ | __Notes__ |
| 2008-09-16 | New document that describes how to write code that's coordinated with the login process. |

