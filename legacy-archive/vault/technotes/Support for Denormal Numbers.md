---
title: Support for Denormal Numbers
apple_id: DTS40012660
resource_type: Technical Note
platform: iOS
topic: Mathematical Computation
technology: null
published: '2012-08-14'
source_url: https://developer.apple.com/library/archive/technotes/tn2293/_index.html
archived_at: '2026-07-26T19:54:10.280990Z'
---
> 导航：[总目录](../README.md) · [technotes](../_indexes/technotes.md)



Technical Note TN2293

# Support for Denormal Numbers

iOS 6 supports the use of denormal numbers for JavaScript in your apps. Most apps will not need to enable this support. If your app needs to compute numbers that approach zero, you can now opt in to support denormal numbers—while knowing that the mathematics is accurate and adheres to industry standards. Safari on iOS 6 adheres to the IEEE-754 floating point specification, so webpages viewed in Safari automatically support denormal numbers.

[What Are Denormal Numbers?](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgnbqgaytenrwgawugsbrfvke4vcbi4yq)[Why Should I Support Denormal Numbers?](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgnbqgaytenrwgawugsbrfvke4vcbi4za)[Are There Any Consequences of Supporting Denormal Numbers?](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgnbqgaytenrwgawugsbrfvke4vcbi4zq)[How Do I Enable Support for Denormal Numbers?](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgnbqgaytenrwgawugsbrfvke4vcbi42a)[Further Reading](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgnbqgaytenrwgawugsbrfvke4vcbi43q)[Document Revision History](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgnbqgaytenrwgawvezlwnfzws33ojbuxg5dpoj4s2rdpnz2ey2lonncwyzlnmvxhiskel4yq)

## What Are Denormal Numbers?

Denormal numbers are double-precision floating point values that are very close to zero but not equal to zero. Without support for denormal numbers, the processor treats numbers that are close enough to zero as zero itself. The result is a number that is marginally less accurate than it would be using denormal numbers.

[Back to Top](#)

## Why Should I Support Denormal Numbers?

You should consider supporting denormal numbers if your app:

- Allows users to browse the web and must pass JavaScript standards test suites
- Performs floating point computations using JavaScript in a `UIWebView` which require a high degree of accuracy

[Back to Top](#)

## Are There Any Consequences of Supporting Denormal Numbers?

Enabling support for denormal numbers occurs at the processor level. After it is enabled, all double-precision floating point code that runs in your app will start using denormal numbers, not just JavaScript. If code in your app operates on double-precision numbers that are very close to zero, it is possible (although unlikely) that changing this setting will affect the behavior of your app’s native code.

[Back to Top](#)

## How Do I Enable Support for Denormal Numbers?

To support denormal numbers, include the following code in your app's `main.m` file:

__Listing 1__  Enabling support for denormal numbers

```objc
#import <fenv.h>
#import <TargetConditionals.h>
#import <UIKit/UIKit.h>

#if !TARGET_IPHONE_SIMULATOR
#import <arm/arch.h>
#endif

int main(int argc, char *argv[])
{
    #ifdef _ARM_ARCH_7
        // Enable IEEE-754 denormal support.
        fenv_t env;
        fegetenv(&env);
        env.__fpscr &= ~__fpscr_flush_to_zero;
        fesetenv(&env);
    #endif

    @autoreleasepool {
        return UIApplicationMain(argc, argv, nil, NSStringFromClass([MyAppDelegate class]));
    }
}
```

You can determine whether your app has enabled support for denormal numbers with the following line of JavaScript:

__Listing 2__  Checking denormal number support

```
alert(Number.MIN_VALUE != 0);
```

If denormal numbers are supported, an alert will read `true`; otherwise, it will read `false.`

[Back to Top](#)

## Further Reading

The full [IEEE-754 specification](http://ieeexplore.ieee.org/xpl/articleDetails.jsp?arnumber=4610935) describes the implementation details of complying to floating point equations.

The JavaScript language goes by the official name ECMAScript and is specified by the [ECMA-262 specification](http://www.ecma-international.org/publications/standards/Ecma-262.htm).

The [test262](http://test262.ecmascript.org/) test suite, developed by the body responsible for the ECMAScript language, provides numerous tests that check for compliance against requirements of the ECMA-262 specification, including support for denormal numbers.

[Back to Top](#)

---

#### Document Revision History

| __Date__ | __Notes__ |
| 2012-08-14 | New document that new document that describes how to enable web content to support denormal numbers on iOS devices. |

