---
title: Checking Code Signing and Sandboxing Status in Code
source: Ole Begemann
source_key: oleb
source_url: 'https://oleb.net/blog/2012/02/checking-code-signing-and-sandboxing-status-in-code/'
original_language: en
published: ''
status: active
license: 未声明 → 仅私有归档
archived_at: 2026-07-27
content_hash: 'sha256:d8f10f0109c3af81'
translated: false
---

> 原文：[Checking Code Signing and Sandboxing Status in Code](https://oleb.net/blog/2012/02/checking-code-signing-and-sandboxing-status-in-code/)　·　Ole Begemann

# Checking Code Signing and Sandboxing Status in Code

**WARNING:** Please do not use this code in your apps. It was just a quick experiment and is neither well tested nor secure.

**Updates:**

- February 23, 2012: I put the code for the category on GitHub and added a corresponding link to the article. I also added a custom prefix to the category methods to avoid possible namespace problems.
- July 4, 2014: Added warning not to use the code.

# The codesign Utility

On the command line, you can use the `codesign` utility to check whether a Mac app is signed. For example, `codesign --display --verbose=4 /Applications/Preview.app` will display a whole lot of info about Preview’s code signature:

```
Executable=/Applications/Preview.app/Contents/MacOS/Preview
Identifier=com.apple.Preview
Format=bundle with Mach-O universal (i386 x86_64)
CodeDirectory v=20100 size=12266 flags=0x0(none) hashes=605+5 location=embedded
Hash type=sha1 size=20
CDHash=c8a47e06c8372dca11ab0bf03f121e1f69638a54
Signature size=4064
Authority=Software Signing
Authority=Apple Code Signing Certification Authority
Authority=Apple Root CA
Info.plist entries=32
Sealed Resources rules=12 files=172
Internal requirements count=1 size=1144
```

You can also use `codesign` to determine whether an app is sandboxed and, if so, list its sandboxing entitlements. The command `codesign --display --entitlements - /Applications/Preview.app` will display the contents of the entitlements property list that is embedded in the application binary:

```
Executable=/Applications/Preview.app/Contents/MacOS/Preview
��qq`<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
    <key>com.apple.security.app-sandbox</key>
    <true/>
    <key>com.apple.security.files.user-selected.read-write</key>
    <true/>
    <key>com.apple.security.device.camera</key>
    <true/>
    <key>com.apple.security.print</key>
    <true/>
    <key>com.apple.security.app-protection</key>
    <true/>
    <key>com.apple.security.camera</key>
    <true/>
    <key>com.apple.security.documents.user-selected.read-write</key>
    <true/>
    <key>com.apple.security.temporary-exception.mach-lookup.global-name</key>
    <array>
        <string>com.apple.systemuiserver.screencapture</string>
    </array>
</dict>
</plist>
```

# Doing it in Code

Can we do the same in code? Yes we can. With a lot of help from my coworkers [Jörg Jacobsen](http://www.joergjacobsen.com/) (see [his work on XPC and Sandboxing](https://github.com/iMediaSandboxing/XPCKit) for the iMedia framework) and [Christian Beer](http://chbeer.de/) (who pointed me to the [source code for the `codesign` utility](http://opensource.apple.com/source/security_systemkeychain/security_systemkeychain-39457/src/)), I wrote a category on `NSBundle` that can tell you for any application bundle:

- whether it has a valid code signature,
- whether it is sandboxed and
- whether it was downloaded from the Mac App Store.

The public interface for the category looks like this and should be self-explanatory:

```
// NSBundle+OBCodeSigningInfo.h
typedef enum {
    OBCodeSignStateUnsigned = 1,
    OBCodeSignStateSignatureValid,
    OBCodeSignStateSignatureInvalid,
    OBCodeSignStateSignatureNotVerifiable,
    OBCodeSignStateSignatureUnsupported,
    OBCodeSignStateError
} OBCodeSignState;

@interface NSBundle (OBCodeSigningInfo)

- (BOOL)ob_comesFromAppStore;
- (BOOL)ob_isSandboxed;
- (OBCodeSignState)ob_codeSignState;

@end
```

## Code Signing Services

For the implementation, we need to look at the [Code Signing Services](https://developer.apple.com/library/mac/#documentation/Security/Reference/CodeSigningRef/Reference/reference.html) in the Security framework. The [`SecStaticCodeCreateWithPath()`](https://developer.apple.com/library/mac/documentation/Security/Reference/CodeSigningRef/Reference/reference.html#//apple_ref/c/func/SecStaticCodeCreateWithPath) takes the URL of an app bundle and returns a reference to a so-called static code object that represents the bundle’s code. We can then call the function [`SecStaticCodeCheckValidityWithErrors()`](https://developer.apple.com/library/mac/documentation/Security/Reference/CodeSigningRef/Reference/reference.html#//apple_ref/c/func/SecStaticCodeCheckValidityWithErrors) on the static code object to obtain information about its code signature.

## Additional Requirements for the Signature (Sandboxing)

To determine whether an app is sandboxed, we can call `SecStaticCodeCheckValidityWithErrors()` again, this time with the additional code requirement (passed as the third argument to the function) that the code object contains a certain entitlement (which is `com.apple.security.app-sandbox` in our case). The call to create this requirement looks like this:

```
static SecRequirementRef sandboxRequirement = NULL;
SecRequirementCreateWithString(CFSTR("entitlement[\"com.apple.security.app-sandbox\"] exists"), kSecCSDefaultFlags, &sandboxRequirement);
```

Have a look at the [documentation for the Code Signing Requirement Language](https://developer.apple.com/library/mac/#documentation/Security/Conceptual/CodeSigningGuide/RequirementLang/RequirementLang.html) to learn how to formulate other requirements you might have.

## Mac App Store Receipt Check

The implementation of the last method, `-ob_comesFromAppStore`, is rather unrelated. It simply checks whether the bundle contains a Mac App Store receipt. OS X 10.7 has a special method to find the App Store receipt in the bundle: [`appStoreReceiptURL`](https://developer.apple.com/library/mac/documentation/Cocoa/Reference/Foundation/Classes/NSBundle_Class/Reference/Reference.html#//apple_ref/doc/uid/20000214-DontLinkElementID_1). If 10.6 compatibility is important for you, you have to hard-code the path to the receipt at `Contents/_MASReceipt/receipt`.

## The Source Code

Check out the full source code of the category below. I use [associative references](https://developer.apple.com/library/mac/#DOCUMENTATION/Cocoa/Conceptual/ObjectiveC/Chapters/ocAssociativeReferences.html) to cache the values of some variables that I use in multiple places, such as the code signature state. **Update February 23, 2012:** The code is now also [available on GitHub](https://github.com/ole/NSBundle-OBCodeSigningInfo).

```
// NSBundle+OBCodeSigningInfo.m
#import "NSBundle+OBCodeSigningInfo.h"
#import <Security/SecRequirement.h>
#import <objc/runtime.h>

@interface NSBundle (OBCodeSigningInfoPrivateMethods)
- (SecStaticCodeRef)ob_createStaticCode;
- (SecRequirementRef)ob_sandboxRequirement;
@end

@implementation NSBundle (OBCodeSigningInfo)

- (BOOL)ob_comesFromAppStore
{
    // Check existence of Mac App Store receipt
    NSURL *appStoreReceiptURL = [self appStoreReceiptURL];
    NSFileManager *fileManager = [[NSFileManager alloc] init];
    BOOL appStoreReceiptExists = [fileManager fileExistsAtPath:[appStoreReceiptURL path]];
    return appStoreReceiptExists;
}

- (BOOL)ob_isSandboxed
{
    BOOL isSandboxed = NO;
    if ([self ob_codeSignState] == OBCodeSignStateSignatureValid)
    {
        SecStaticCodeRef staticCode = [self ob_createStaticCode];
        SecRequirementRef sandboxRequirement = [self ob_sandboxRequirement];
        if (staticCode && sandboxRequirement) {
            OSStatus codeCheckResult = SecStaticCodeCheckValidityWithErrors(staticCode, kSecCSBasicValidateOnly, sandboxRequirement, NULL);
            if (codeCheckResult == errSecSuccess) {
                isSandboxed = YES;
            }
            CFRelease(staticCode);
        }
    }
    return isSandboxed;
}

- (OBCodeSignState)ob_codeSignState
{
    // Return cached value if it exists
    static const void *kOBCodeSignStateKey;
    NSNumber *resultStateNumber = objc_getAssociatedObject(self, kOBCodeSignStateKey);
    if (resultStateNumber) {
        return [resultStateNumber integerValue];
    }

    // Determine code sign status
    OBCodeSignState resultState = OBCodeSignStateError;
    SecStaticCodeRef staticCode = [self ob_createStaticCode];
    if (staticCode)
    {
        OSStatus signatureCheckResult = SecStaticCodeCheckValidityWithErrors(staticCode, kSecCSBasicValidateOnly, NULL, NULL);
        switch (signatureCheckResult) {
            case errSecSuccess: resultState = OBCodeSignStateSignatureValid; break;
            case errSecCSUnsigned: resultState = OBCodeSignStateUnsigned; break;
            case errSecCSSignatureFailed:
            case errSecCSSignatureInvalid:
                resultState = OBCodeSignStateSignatureInvalid;
                break;
            case errSecCSSignatureNotVerifiable: resultState = OBCodeSignStateSignatureNotVerifiable; break;
            case errSecCSSignatureUnsupported: resultState = OBCodeSignStateSignatureUnsupported; break;
            default: resultState = OBCodeSignStateError; break;
        }
        CFRelease(staticCode);
    }
    else
    {
        resultState = OBCodeSignStateError;
    }

    // Cache the result
    resultStateNumber = [NSNumber numberWithInteger:resultState];
    objc_setAssociatedObject(self, kOBCodeSignStateKey, resultStateNumber, OBJC_ASSOCIATION_RETAIN);

    return resultState;
}

#pragma mark - Private helper methods

- (SecStaticCodeRef)ob_createStaticCode
{
    NSURL *bundleURL = [self bundleURL];
    SecStaticCodeRef staticCode = NULL;
    SecStaticCodeCreateWithPath((__bridge CFURLRef)bundleURL, kSecCSDefaultFlags, &staticCode);
    return staticCode;
}

- (SecRequirementRef)ob_sandboxRequirement
{
    static SecRequirementRef sandboxRequirement = NULL;
    static dispatch_once_t onceToken;
    dispatch_once(&onceToken, ^{
        SecRequirementCreateWithString(CFSTR("entitlement[\"com.apple.security.app-sandbox\"] exists"), kSecCSDefaultFlags, &sandboxRequirement);
    });
    return sandboxRequirement;
}

@end
```
