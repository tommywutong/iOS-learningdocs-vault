---
title: Framework Programming Guide
apple_id: 10000183i
resource_type: Guide
platform: macOS
topic: Xcode
technology: null
published: '2013-09-17'
source_url: https://developer.apple.com/library/archive/documentation/MacOSX/Conceptual/BPFrameworks/Concepts/WeakLinking.html
archived_at: '2026-07-15T08:15:40.617791Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Framework Programming Guide](Introduction%20to%20Framework%20Programming%20Guide.md)


[Next](Guidelines%20for%20Creating%20Frameworks.md)[Previous](Frameworks%20and%20Binding.md)

# Frameworks and Weak Linking

One challenge faced by developers is that of taking advantage of new features introduced in new versions of OS X while still supporting older versions of the system. Normally, if an application uses a new feature in a framework, it is unable to run on earlier versions of the framework that do not support that feature. Such applications would either fail to launch or crash when an attempt to use the feature was made. Apple has solved this problem by adding support for weakly-linked symbols.

When a symbol in a framework is defined as weakly linked, the symbol does not have to be present at runtime for a process to continue running. The static linker identifies a weakly linked symbol as such in any code module that references the symbol. The dynamic linker uses this same information at runtime to determine whether a process can continue running. If a weakly linked symbol is not present in the framework, the code module can continue to run as long as it does not reference the symbol. However, if the symbol is present, the code can use it normally.

If you are updating your own frameworks, you should consider making new symbols weakly linked. Doing so can make it easier for clients of your framework to support it. You should also make sure that your own code checks for the existence of weakly-linked symbols before using them.

For more information regarding weak linking, including additional examples, see _[SDK Compatibility Guide](../../Developer%20Tools/SDK%20Compatibility%20Guide/Introduction.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgeydambqge3dg2i)_.

Apple frameworks use the availability macros to determine whether a symbol is weakly linked or strongly linked. Apple wraps new interfaces in its frameworks with availability macros to indicate which version of the operating system a feature first appeared. Macros are also used to indicate deprecated features and interfaces.

The availability macros defined in `/usr/include/AvailabilityMacros.h` add weak linking information to system interfaces based on the versions of OS X your project supports. When you create a new project, you tell the compiler which versions of OS X your project supports by setting the deployment target and target SDK in Xcode. The compiler uses these settings to assign appropriate values to the `MAC_OS_X_VERSION_MIN_REQUIRED` and `MAC_OS_X_VERSION_MAX_ALLOWED` macros, respectively. For information on how to modify these settings in Xcode, see “Setting Up Cross-Development in Xcode” in _[SDK Compatibility Guide](../../Developer%20Tools/SDK%20Compatibility%20Guide/Introduction.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgeydambqge3dg2i)_ or the Xcode help.

For example, suppose in Xcode you set the deployment target (minimum required version) to OS X v10.2 and the target SDK (maximum allowed version) to OS X v10.3. During compilation, the compiler would weakly link any interfaces that were introduced in OS X version 10.3 while strongly linking earlier interfaces. This would allow your application to continue running on OS X version 10.2 but still take advantage of newer features when they are available.

Before using any symbols that are introduced in a version of OS X that is later than your minimum required version, make sure you check to see that the symbol exists first. See [Using Weakly Linked Symbols](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgiydambsgm3tqljrga3dmmzt) for more information.

If you define your own frameworks, you can mark symbols as weakly linked using the `weak_import` attribute. Weak linking is especially appropriate if you introduce new features to an existing framework. To mark symbols as weakly linked, you must make sure your environment is configured to support weak linking:

- You must be using GCC version 3.1 or later. Weak linking is not supported in GCC version 2.95
- You must set the OS X Deployment Target build option of your Xcode project to OS X v10.2 or later.

The linker marks symbols as strongly linked unless you explicitly tell it otherwise. To mark a function or variable as weakly linked, add the `weak_import` attribute to the function prototype or variable declaration, as shown in the following example:

```
extern int MyFunction() __attribute__((weak_import));
extern int MyVariable __attribute__((weak_import));
```


If your framework relies on weakly linked symbols in any Apple or third-party frameworks, you must check for the existence of those symbols before using them. If you attempt to use a non-existent symbol without first checking, the dynamic linker may generate a runtime binding error and terminate the corresponding process.

If a weakly linked symbol is not available in a framework, the linker sets the address of the symbol to NULL. You can check this address in your code using code similar to the following:

```
extern int MyWeakLinkedFunction() __attribute__((weak_import));

int main()
{
    int result = 0;

    if (MyWeakLinkedFunction != NULL)
    {
        result = MyWeakLinkedFunction();
    }

    return result;
}
```


When you reference symbols in another framework, most of those symbols are linked strongly to your code. In order to create a weak link to a symbol, the framework containing the symbol must explicitly add the `weak_import` attribute to it (see [Marking Symbols for Weak Linking](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgiydambsgm3tqljrga3tenrs)). However, if you do not maintain a framework and need to link its symbols weakly, you can explicitly tell the compiler to mark all symbols as weakly linked. To do this, you must open your project in Xcode and modify the way your targets link to the framework as follows:

1. Select the target you want to modify and reveal its build phases.
2. Expand the Link Binary With Libraries build phase to view the frameworks currently linked by the target.
3. If the framework you want to weakly link to is listed in the Link Binary With Libraries build phase, select it, and choose Edit > Delete to remove it.

   Now you can tell the linker to use weak linking for that framework.
4. Select the target, open its Info window, and click Build.
5. To the Other Linker Flags build setting, add the following command-line option specification, where `<framework_name>` is the name of the framework you want to weakly link to:

```
-weak_framework <framework_name>
```
6. Build your product.

The `-weak_framework` option tells the linker to weakly link all symbols in the named framework. If you need to link to a library instead of a framework, you can use the `-weak_library` linker command instead of `-weak_framework`.

[Next](Guidelines%20for%20Creating%20Frameworks.md)[Previous](Frameworks%20and%20Binding.md)

