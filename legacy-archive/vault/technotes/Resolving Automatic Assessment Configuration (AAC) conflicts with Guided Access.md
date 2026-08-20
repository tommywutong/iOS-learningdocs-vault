---
title: Resolving Automatic Assessment Configuration (AAC) conflicts with Guided Access
  and Single App Mode
apple_id: DTS40017583
resource_type: Technical Note
platform: iOS
topic: Data Management
technology: UIKit
published: '2016-12-06'
source_url: https://developer.apple.com/library/archive/technotes/tn2448/_index.html
archived_at: '2026-07-26T19:54:15.202084Z'
---
> 导航：[总目录](../README.md) · [technotes](../_indexes/technotes.md)



Technical Note TN2448

# Resolving Automatic Assessment Configuration (AAC) conflicts with Guided Access and Single App Mode

Restrictions imposed by AAC may not be enforced when Guided Access or Single App Mode are enabled. This document describes techniques to detect these cases, so assessment apps can respond appropriately.

[Introduction](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgnbqgaytonjygmwugsbrfvke4vcbi4yq)[Prerequisites](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgnbqgaytonjygmwugsbrfvke4vcbi4za)[Discussion](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgnbqgaytonjygmwugsbrfvke4vcbi4zq)[Document Revision History](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgnbqgaytonjygmwvezlwnfzws33ojbuxg5dpoj4s2rdpnz2ey2lonncwyzlnmvxhiskel4yq)

## Introduction

If an app with the AAC entitlement (available on iOS 9.3.2 and higher) is launched on a device and Guided Access has been manually initiated on the device, or SAM (Single App Mode) configured for that app via a profile, then Guided Access and SAM will override the restrictions imposed by AAC. This document describes techniques to detect if this is the case, so the app can optionally stop the assessment.

For definitions of Guided Access, SAM, and AAC, please see [Knowledge Base article HT204775](https://support.apple.com/en-us/HT204775).

[Back to Top](#)

## Prerequisites

This document assumes that you already have an app using AAC that works as desired on unsupervised iOS devices.

[Back to Top](#)

## Discussion

When both Guided Access or SAM and AAC have been configured for an app, Guided Access or SAM will take precedence over AAC. Consequently, certain restrictions that are automatically imposed by AAC, such as turning off spell check, dictionary lookup, predictive typing, etc, will become inactive. Developers of assessment apps will want to discover if these restrictions are inactive, so they can either stop the assessment or warn the user, as appropriate.

The best practice is to not initiate Guided Access and to not configure any profiles with SAM for an assessment app, and to use AAC alone for assessment apps.

If an app can’t assume that Guided Access or SAM are not configured, the app needs to check whether Guided Access or SAM have been enabled. Because AAC requires iOS 9.3.2 or later, the app needs to check the iOS version before checking the state of Guided Access or SAM. Checking the version of iOS is illustrated in Listing 1.

__Listing 1__  Checking if an app is running on iOS 9.3.2 or higher.

```
// Are we running on iOS 9.3.2 or higher?

let osVersion_9_3_2 = OperatingSystemVersion(majorVersion: 9, minorVersion: 3, patchVersion: 2)

if ProcessInfo.processInfo.isOperatingSystemAtLeast(osVersion_9_3_2) {
    // We are on iOS 9.3.2 or higher.
}
```

Checking for Guided Access or SAM should be done at least 2 seconds after app launch, as in Listing 2.

__Listing 2__  Checking if Guided Access or SAM is already active on the device.

```
DispatchQueue.main.asyncAfter(deadline: .now() + 2.0) {
    if UIAccessibilityIsGuidedAccessEnabled() {
        // Guided Access is enabled.
        // Test should not proceed until the user disables Guided Access.
    }
}
```

The two code snippets should be combined to perform an effective check, and this should be done before the app invokes AAC mode. It is up to you to determine if the correct action in this case is to abort the test, display a warning, continue, or to take some other action.

[Back to Top](#)

---

#### Document Revision History

| __Date__ | __Notes__ |
| 2016-12-06 | New document that describes the conditions under which conflicts occur between AAC and Guided Access (or Single Access Mode), and how to programmatically check for the conflict. |

