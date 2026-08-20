---
title: Resolving "0xE800003A", applications not launching and "missing entitlement"
apple_id: DTS40008782
resource_type: Technical Note
platform: iOS
topic: Xcode
technology: null
published: '2009-05-11'
source_url: https://developer.apple.com/library/archive/technotes/tn2242/_index.html
archived_at: '2026-07-26T19:54:09.621195Z'
---
> 导航：[总目录](../README.md) · [technotes](../_indexes/technotes.md)



# Retired Document

__Important:__
This document may not represent best practices for current development. Links to downloads and other resources may no longer be valid.

Technical Note TN2242

# Resolving "0xE800003A", applications not launching and "missing entitlement"

__Important:__ This document may not represent best practices for current development. Links to downloads and other resources may no longer be valid.

If your application fails to launch on the device with an error of "0xE800003A", it generally means your application is signed in a way that prevents it from launching on the device on which it's running.

There are a number of reasons why this might happen. The most common reasons are an incorrect (or no) Code Signing Identity was selected in Xcode's Build Info pane or a mismatch between your App ID (in your provisioning profile) and your Bundle Identifier (in your Info.plist).

Resolve the former issue by ensuring you've selected the correct Code Signing Identity (under the grey provisioning profile name); resolve the latter issue by ensuring your App ID and Bundle ID match; they need to be identical to run your application on the device. This document provides background and details.

Another common cause is you're doing an Ad Hoc distribution and haven't added and configured the `Entitlements.plist`, as described in the "Building your Application with Xcode for Distribution" section of the iPhone Developer Program Portal User Guide in the [iPhone Portal](https://developer.apple.com/iphone).

Other causes include not adding the device UDID to your provisioning profile or having multiple iPhone Developer (or Distribution) certificates. Read this document for more on this and other possible causes and resolutions.

[Mismatch between App ID and Bundle Identifier](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgnbqgaydqnzygiwugsbrfvgusu2nifkegsa)[A brief digression](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgnbqgaydqnzygiwugsbrfvgusu2nifkegsbnifpueusjivdf6rcji5jeku2tjfhu4)[Important caveats for selecting and using a Bundle Identifier](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgnbqgaydqnzygiwugsbrfvgusu2nifkegsbnjfgvat2skrau4vc7inavmrkbkrjv6rspkjpvgrkmivbviskoi5puctsel5kvgskoi5pucx2ckvheitcfl5euirkokreumskfki)[Ad Hoc Distribution not properly configured](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgnbqgaydqnzygiwugsbrfvauix2ij5bq)[Other causes and resolutions](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgnbqgaydqnzygiwugsbrfvhviscfkjpugqkvkncvg)[Missing or incorrect Unique Device Identifier (UDID)](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgnbqgaydqnzygiwugsbrfvhviscfkjpugqkvkncvglknjfjvgskoi5pu6us7jfhegt2skjcugvc7kvhesukvivpuirkwjfbukx2jircu4vcjizeukus7l5kuiskel4)[Revoked certificates](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgnbqgaydqnzygiwugsbrfvhviscfkjpugqkvkncvglksivle6s2firpugrkskreumskdifkekuy)[Document Revision History](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgnbqgaydqnzygiwvezlwnfzws33ojbuxg5dpoj4s2rdpnz2ey2lonncwyzlnmvxhiskel4yq)

## Mismatch between App ID and Bundle Identifier

If your App ID (in your provisioning profile) and your Bundle Identifier (in your `Info.plist`) do not match, your application won't launch on the device. Check your Console log for an "`entitlement 'application-identifier' has value not permitted by provisioning profile`" error to confirm this mismatch (see Listing 1).

__Listing 1__  A Console Log error pointing to a App ID/Bundle ID mismatch.

```
Mon Sep 22 19:38:20 unknown securityd[391] <Error>: mobile_installat[399] SecItemCopyMatching: missing entitlement
Mon Sep 22 19:38:20 unknown mobile_installation_proxy[399] <Error>: entitlement 'application-identifier' has value not permitted by a provisioning profile
Mon Sep 22 19:38:20 unknown mobile_installation_proxy[399] <Error>: verify_executable: Could not validate signature: e8008016

[...]

Mon Sep 22 19:38:20 unknown mobile_installation_proxy[399] <Error>: install_application: Could not preflight application install
Mon Sep 22 19:38:20 unknown mobile_installation_proxy[399] <Error>: handle_install: Installation failed
```

To resolve this, make sure your App ID and your Bundle Identifier match. For example, if your App ID is `A1B2C3D4E5.com.yourcompany.productname` then your Bundle Identifier needs to be `com.yourcompany.productname`.

__Important:__ The 10-character prefix in the App ID __is not included__ in the Bundle Identifier when entering it into Xcode.

If you created an App ID with a wildcard ("\*") at the end of the ID (e.g. `A1B2C3D4E5.com.yourcompany.*`), you have more flexibility in your choice of Bundle Identifier, as you can use almost anything in place of the wildcard. For example, if you had two applications, you'd be able to use the same App ID (and therefore the same provisioning profile), simply by changing the Bundle Identifier in your project.

- App ID: `A1B2C3D4E5.com.yourcompany.*`
- Bundle ID for Application 1: `com.yourcompany.product1`
- Bundle ID for Application 2: `com.yourcompany.product2`

You can even enter just a wildcard as your App ID (e.g. `A1B2C3D4E5.*`). This gives you ultimate flexibility as you'd be able to use any Bundle Identifier at all. This is the easiest setup because it requires no changes to your default Bundle Identifier in your project.

__Important:__ The App ID seed prefix (in these examples, "`A1B2C3D4E5`") is unique to you. Any applications you create which share the same App ID will have access to the same Keychain "slice" associated with that App ID. Consider the security implications of this if you develop applications that shouldn't share Keychain information. Generally, use different App IDs for unrelated applications.

### A brief digression

The default Bundle Identifier in new projects is `com.yourcompany.${PRODUCT_NAME:identifier}`. "`${PRODUCT_NAME:identifier}`" is a variable and will be replaced by the name of your application. This is a source of confusion as you might change your project or application name over the course of development, which changes the effective Bundle Identifier.

If you keep the default Bundle Identifier, and you haven't used the wildcard in your App ID, changing your product name will cause the `0xE800003A` error. If you think there's a chance you'll change your project or application name in the future, do one of two things:

- Create and use a wildcard ("\*") in your App ID (e.g. `A1B2C3D4E5.com.yourcompany.*`); or,
- Replace the default Bundle Identifier with an explicit one (e.g. `com.yourcompany.yourproductname`)

### Important caveats for selecting and using a Bundle Identifier

Selecting and using a Bundle Identifier (and by extension, an App ID) has these important caveats:

- While you can change your Bundle Identifer at will prior to placing your application for sale in the App Store, once it's available for sale, you cannot change your Bundle Identifier. Choose one carefully. Fortunately, the Bundle Identifier is not publicly displayed, so it does not have any marketing requirements, nor a need to be clever. It only needs to be unique within the App Store. We recommend using reverse domain notation (`com.yourcompany`) as the basis of your Bundle ID, especially if you own your domain name. An alternative is reverse email address notation (e.g. `com.domainname.username`)
- The Bundle Identifier (and App ID) is an example of a "Uniform Type Identifier" (UTI), so you can only use valid UTI characters for your Bundle Identifier. In particular, you can't use spaces or underscores. From "[The UTI Character Set](../documentation/File%20Management/Uniform%20Type%20Identifiers%20Overview/Uniform%20Type%20Identifier%20Concepts.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytgmjzfvbuqmrqgiwvgvzs):

  "You may use the Roman alphabet in upper and lower case (A–Z, a–z), the digits 0 through 9, the dot (“.”), and the hyphen (“-”). This restriction is based on DNS name restrictions, set forth in RFC 1035.... Uniform type identifiers may also contain any of the Unicode characters greater than U+007F.... Any illegal character appearing in a UTI string—for example, underscore ("_"), colon (":"), or space (" ")—will cause the string to be rejected as an invalid UTI. At the API layer, no error is generated for invalid UTIs."

  If your project name or application name contains a space or other illegal character, either use an explicit Bundle ID (e.g. `A1B2C3D4E5.com.yourcompany.yourproductname`) instead of the default Bundle Identifier, or change your Product Name in your Target's Build Info pane.

  __Warning:__ While an invalid UTI may work when testing on your device, it will generally cause an error when uploaded to the App Store.
[Back to Top](#)

## Ad Hoc Distribution not properly configured

If you're doing an Ad Hoc distribution, you must properly configure your project to include an `Entitlements.plist` file and uncheck the `get-task-allow` checkbox (which sets it to `False`). You can confirm this is the cause of your errors by looking in the Console for errors similar to that in Listing 2

__Listing 2__  A Console Log error pointing to an improperly configured Ad Hoc Distribution.

```
Tue Nov 11 14:20:24 unknown mobile_installation_proxy[2012] <Error>: install_embedded_profile: Skipping the installation of the embedded profile
Tue Nov 11 14:20:24 unknown securityd[2004] <Error>: mobile_installat[2012] SecItemCopyMatching: missing entitlement
Tue Nov 11 14:20:25 unknown mobile_installation_proxy[2012] <Error>: entitlement 'get-task-allow' has value not permitted by a provisioning profile
Tue Nov 11 14:20:25 unknown mobile_installation_proxy[2012] <Error>: verify_executable: Could not validate signature: e8008016

[...]

Tue Nov 11 14:20:25 unknown mobile_installation_proxy[2012] <Error>: install_application: Could not preflight application install
Tue Nov 11 14:20:25 unknown mobile_installation_proxy[2012] <Error>: handle_install: Installation failed
```

See the "Building your Application with Xcode for Distribution" section of the iPhone Developer Program Portal User Guide in the [iPhone Portal](https://developer.apple.com/iphone) for instructions on setting up your `Entitlements.plist`.

[Back to Top](#)

## Other causes and resolutions

While a mismatch between the App ID and the Bundle Identifier or an improperly configured Ad Hoc distribution are the most common causes of this error, there are others:

### Missing or incorrect Unique Device Identifier (UDID)

Your provisioning profile may not include the UDID of the device to which you're deploying. This may happen when you add a new device to your development pool, when you're doing an Ad Hoc distribution, or if you forget to send the provisioning profile to your Ad Hoc testers.

It may also include an incorrect UDID, either because it was mistyped, or because it's not all lowercase (which would happen when copying UDIDs from iTunes 7).

### Revoked certificates

If you've revoked your "iPhone Developer" or "iPhone Distribution" certificates, kept the old certificates on your Keychain, and your provisioning profile or project continue to reference the old certificate, Xcode may sign your application with a certificate that's different from the one in your provisioning profile. You should delete the revoked certificates (after making a backup, of course), and update and install your provisioning profiles.

[Back to Top](#)

---

#### Document Revision History

| __Date__ | __Notes__ |
| 2009-05-11 | New document that describes why your application may fail to launch on devices and related error messages. |

