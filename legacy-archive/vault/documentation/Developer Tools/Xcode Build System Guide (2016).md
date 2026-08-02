---
title: Xcode Build System Guide
apple_id: TP40003931
resource_type: Guide
platform: Xcode Developer Tools
topic: Xcode
technology: null
published: '2016-09-29'
source_url: https://developer.apple.com/library/archive/documentation/DeveloperTools/Reference/XcodeBuildSettingRef/0-Introduction/introduction.html
archived_at: '2026-07-15T07:30:59.197863Z'
---
> 导航：[总目录](../../README.md) · [documentation](../../_indexes/documentation.md)


[Next](https://developer.apple.com/library/archive/documentation/DeveloperTools/Reference/XcodeBuildSettingRef/1-Build_Setting_Reference/build_setting_ref.html)

An updated version of Build Settings Reference is now available in Xcode Help. To access it:

1. In Xcode, choose Help > Xcode Help, or open the [Xcode Help](http://help.apple.com/xcode/mac/) website.

2. Search for “build settings.”

# Introduction

Xcode uses build settings to specify aspects of the build process followed to generate a product. A build setting is a variable that determines how build tasks are performed.

You can customize most of the build settings listed in this document using the target and product editors in the Xcode application, configuration files, and `xcodebuild` invocations. However, there are build settings that can be customized only through indirect means and build settings that are not customizable. Build settings that are not customizable do not have a “Default value” entry in their reference.

In addition, Xcode lets you assign conditional values to build settings. The conditions include build factors such as the architecture you’re targeting and the SDK you’re using. Build settings with conditional values are known as _conditional build settings_.

This document is intended for developers who need to get a deep understanding of how the Xcode build system works.

To fully understand how a target’s build settings affect a build and how they relate to one another, this document uses the following terms to describe each build setting and the build settings that relate to it.

**_Alias_**
: Additional name used to identify a build setting.

**_bundle file path_ or _bundle directory path_**
: String that represents a location inside a bundled product. See _[Bundle Programming Guide](../Core%20Foundation/Bundle%20Programming%20Guide/Introduction.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgeydambqgezdg2i)_ for information on product bundles.

**_C-based language_**
: C, C++, Objective-C, and Objective-C++.

**_C++–based language_**
: C++, and Objective-C++.

**_Companion_**
: Build settings that are used in conjunction with the referring build setting to accomplish its action. If you customize the referring build setting, you should review the specifications of its companion build settings.

**_Default value_**
: The buildtime value of a build setting when there’s no corresponding setting specification for the target.

**_Effector_**
: Build setting whose value is used to compute the default value of the referring build setting.

**_Effect_**
: Build setting whose default value is computed using the value of the referring build setting.

**_file path_ or _directory path_**
: String that represents a fully qualified filesystem path. When a path contains spaces, the path must be surrounded by single quotation marks (`'`) or double quotation marks (`"`), or the spaces must be escaped with a backslash (`\`).

**_filename_**
: String that may contain numbers, letters, dashes (`-`), periods (`.`) or underscores (`_`).

**_identifier_**
: String that may contain digits, letters, dashes (`-`), plus signs (`+`), and underscores (`_`).

**_installed product_**
: A product configured for distribution to its users.

**_installed product directory_**
: Directory that represents the root directory (`/`) on a user’s computer.

**_number_**
: String that may contain only digits.

**_numeric identifier_**
: String that may contain numbers and periods.

**_option specification_**
: String that may contain the characters an identifier may contain as well as spaces. When an option specification contains spaces, it must be surrounded by single quotation marks (`'`) or double quotation marks (`"`).

**_Prerequisite_**
: Expression that must be true for the referring build setting to take effect.

**_Prerequisite for_**
: The referring build setting’s value allows or suppresses the behavior specified by the referred build setting.

**_project file path_ or _project directory path_**
: String that represents a location inside a project directory.

**_Related to_**
: Build setting with a conceptual relationship with the referring build setting except for prerequisites, companions, effects, and effectors.

**_uniform type identifier_ (UTI)**
: String that specifies a type. This string uses the reverse-DNS (Domain Name System) to uniquely identify an item in a way that other systems can recognize. See _[Uniform Type Identifiers Overview](../File%20Management/Uniform%20Type%20Identifiers%20Overview/Introduction%20to%20Uniform%20Type%20Identifiers%20Overview.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytgmjz)_ for details on uniform type identifiers.

**_Value_**
: Value of a build setting at build time. This is not necessarily the build setting specification. See [Build Settings](https://developer.apple.com/library/archive/documentation/DeveloperTools/Conceptual/XcodeBuildSystem/300-Build_Settings/bs_build_settings.html#//apple_ref/doc/uid/TP40002691) for details.

This document assumes that all the Xcode SDKs are installed on your computer.

If you develop products using C++, you may need to customize these build settings in your targets:

- [GCC_ENABLE_CPP_EXCEPTIONS (Enable C++ Exceptions)](https://developer.apple.com/library/archive/documentation/DeveloperTools/Reference/XcodeBuildSettingRef/1-Build_Setting_Reference/build_setting_ref.html#//apple_ref/doc/uid/TP40003931-CH3-SW10)
- [GCC_ENABLE_CPP_RTTI (Enable C++ Runtime Types)](https://developer.apple.com/library/archive/documentation/DeveloperTools/Reference/XcodeBuildSettingRef/1-Build_Setting_Reference/build_setting_ref.html#//apple_ref/doc/uid/TP40003931-CH3-SW9)
- [GCC_WARN_EFFECTIVE_CPLUSPLUS_VIOLATIONS (Effective C++ Violation)](https://developer.apple.com/library/archive/documentation/DeveloperTools/Reference/XcodeBuildSettingRef/1-Build_Setting_Reference/build_setting_ref.html#//apple_ref/doc/uid/TP40003931-CH3-SW98)
- [GCC_WARN_HIDDEN_VIRTUAL_FUNCTIONS (Hidden Virtual Functions)](https://developer.apple.com/library/archive/documentation/DeveloperTools/Reference/XcodeBuildSettingRef/1-Build_Setting_Reference/build_setting_ref.html#//apple_ref/doc/uid/TP40003931-CH3-SW99)
- [GCC_WARN_NON_VIRTUAL_DESTRUCTOR (Nonvirtual Destructor)](https://developer.apple.com/library/archive/documentation/DeveloperTools/Reference/XcodeBuildSettingRef/1-Build_Setting_Reference/build_setting_ref.html#//apple_ref/doc/uid/TP40003931-CH3-SW100)
- [OTHER_CPLUSPLUSFLAGS (Other C++ Flags)](https://developer.apple.com/library/archive/documentation/DeveloperTools/Reference/XcodeBuildSettingRef/1-Build_Setting_Reference/build_setting_ref.html#//apple_ref/doc/uid/TP40003931-CH3-SW19)
- [LINKER_DISPLAYS_MANGLED_NAMES (Display Mangled Names)](https://developer.apple.com/library/archive/documentation/DeveloperTools/Reference/XcodeBuildSettingRef/1-Build_Setting_Reference/build_setting_ref.html#//apple_ref/doc/uid/TP40003931-CH3-SW101)
- [STANDARD_C_PLUS_PLUS_LIBRARY_TYPE (C++ Standard Library Type)](https://developer.apple.com/library/archive/documentation/DeveloperTools/Reference/XcodeBuildSettingRef/1-Build_Setting_Reference/build_setting_ref.html#//apple_ref/doc/uid/TP40003931-CH3-SW91)

Use these build settings to customize your debugging experience:

- [BUILD_VARIANTS (Build Variants)](https://developer.apple.com/library/archive/documentation/DeveloperTools/Reference/XcodeBuildSettingRef/1-Build_Setting_Reference/build_setting_ref.html#//apple_ref/doc/uid/TP40003931-CH3-SW48)
- [DEBUG_INFORMATION_FORMAT (Debug Information Format)](https://developer.apple.com/library/archive/documentation/DeveloperTools/Reference/XcodeBuildSettingRef/1-Build_Setting_Reference/build_setting_ref.html#//apple_ref/doc/uid/TP40003931-CH3-SW52)
- [GCC_DEBUGGING_SYMBOLS (Level of Debug Symbols)](https://developer.apple.com/library/archive/documentation/DeveloperTools/Reference/XcodeBuildSettingRef/1-Build_Setting_Reference/build_setting_ref.html#//apple_ref/doc/uid/TP40003931-CH3-SW8)
- [GCC_GENERATE_DEBUGGING_SYMBOLS (Generate Debug Symbols)](https://developer.apple.com/library/archive/documentation/DeveloperTools/Reference/XcodeBuildSettingRef/1-Build_Setting_Reference/build_setting_ref.html#//apple_ref/doc/uid/TP40003931-CH3-SW102)
- [DEAD_CODE_STRIPPING (Dead Code Stripping)](https://developer.apple.com/library/archive/documentation/DeveloperTools/Reference/XcodeBuildSettingRef/1-Build_Setting_Reference/build_setting_ref.html#//apple_ref/doc/uid/TP40003931-CH3-SW5)
- [PRESERVE_DEAD_CODE_INITS_AND_TERMS (Don’t Dead-Strip Inits and Terms)](https://developer.apple.com/library/archive/documentation/DeveloperTools/Reference/XcodeBuildSettingRef/1-Build_Setting_Reference/build_setting_ref.html#//apple_ref/doc/uid/TP40003931-CH3-SW103)
- [STRIP_STYLE (Strip Style)](https://developer.apple.com/library/archive/documentation/DeveloperTools/Reference/XcodeBuildSettingRef/1-Build_Setting_Reference/build_setting_ref.html#//apple_ref/doc/uid/TP40003931-CH3-SW96)

The following sections describe build settings you can use to customize a build or to inquire about a the configuration of a build at build time.

[Next](https://developer.apple.com/library/archive/documentation/DeveloperTools/Reference/XcodeBuildSettingRef/1-Build_Setting_Reference/build_setting_ref.html)

