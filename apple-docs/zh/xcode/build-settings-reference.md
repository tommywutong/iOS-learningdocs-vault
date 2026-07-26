---
title: 构建设置参考
framework: xcode
symbol_kind: article
role: article
role_heading: Article
platforms: []
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/xcode/build-settings-reference
source_url: 'https://developer.apple.com/documentation/xcode/build-settings-reference'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/xcode/build-settings-reference.json'
content_hash: 'sha256:5d60e7d9d641d2a1'
translated: true
---

> 导航： [技术](../technologies.md) · [Xcode](../xcode.md) · [构建系统](build-system.md)

# 构建设置参考

<sub>文章</sub>

详细列出各项 Xcode 构建设置，这些设置用于控制或改变 target 的构建方式。

## 概述

在这里查找你 Xcode 项目的构建设置。

### Active Build Action

**设置名称：** `ACTION`

一个字符串，标识正在执行的构建系统操作。

### Additional SDKs

**设置名称：** `ADDITIONAL_SDKS`

应叠加在 `SDKROOT` 指定的 SDK 之上的任何 sparse SDK 的位置。如果列出了多个 SDK，第一个具有最高优先级。此设置中指定的每个 SDK 都应是一个“sparse” SDK，例如，不能是整个 macOS 发行版的 SDK。

### Allow Multi-Platform Builds

**设置名称：** `ALLOW_TARGET_PLATFORM_SPECIALIZATION`

如果启用，允许 target 在单次构建操作中多次构建。target 会针对活动运行目标（active run destination）所在的平台构建，也会针对依赖它们的其他 target 所在的平台构建。

### Alternate Install Group

**设置名称：** `ALTERNATE_GROUP`

`ALTERNATE_PERMISSIONS_FILES` 设置下所列文件的组名或 gid。

### Alternate Install Permissions

**设置名称：** `ALTERNATE_MODE`

用于 `ALTERNATE_PERMISSIONS_FILES` 设置下所列文件的权限。

### Alternate Install Owner

**设置名称：** `ALTERNATE_OWNER`

`ALTERNATE_PERMISSIONS_FILES` 设置下所列文件的属主名或 uid。

### Alternate Permissions Files

**设置名称：** `ALTERNATE_PERMISSIONS_FILES`

应用了替代属主、组和权限的文件列表。

### Alternative Distribution - Web

**设置名称：** `ALTERNATIVE_DISTRIBUTION_WEB`

启用后，可在从 Xcode 运行时覆盖你的 App 用于网页分发的分发者标识符。

### Always Embed Swift Standard Libraries

**设置名称：** `ALWAYS_EMBED_SWIFT_STANDARD_LIBRARIES`

始终在 target 的产品中嵌入 Swift 标准库，即使该 target 不包含任何 Swift 代码。例如，如果该 target 嵌入了包含 Swift 的其他产品，或者它是一个不包含 Swift 但用于测试包含 Swift 的产品的测试 target，就应启用此设置。此设置仅适用于经过打包的产品，不适用于独立的二进制产品。

### Always Search User Paths (Deprecated)

**设置名称：** `ALWAYS_SEARCH_USER_PATHS`

此设置自 Xcode 8.3 起已废弃，未来版本可能不再支持。建议你禁用此设置。

如果启用，`#include <header.h>` 风格和 `#include "header.h"` 风格的指令都会在搜索 `HEADER_SEARCH_PATHS` 之前先搜索 `USER_HEADER_SEARCH_PATHS` 中的路径。因此，当使用 `#include <header.h>` 时，用户头文件（例如你自己的 `String.h` 头文件）的优先级会高于系统头文件。这是通过对 `USER_HEADER_SEARCH_PATHS` 中提供的路径使用 `-iquote` 标志实现的。如果禁用此设置，且你的编译器完全支持独立的用户路径，用户头文件就只能通过 `#include "header.h"` 风格的预处理器指令访问。

出于向后兼容的原因，此设置默认启用。强烈建议禁用它。

### Require Only App-Extension-Safe API

**设置名称：** `APPLICATION_EXTENSION_API_ONLY`

启用后，会使编译器和链接器禁止使用 App 扩展不可用的 API，也禁止链接未启用此设置构建的框架。

### Convert Copied Files

**设置名称：** `APPLY_RULES_IN_COPY_FILES`

启用此设置会使 target 的 Copy Files 构建阶段中的文件由构建规则处理。例如，属性列表文件（`.plist`）和字符串文件会分别按照 `PLIST_FILE_OUTPUT_FORMAT` 和 `STRINGS_FILE_OUTPUT_ENCODING` 指定的方式转换。

### Process Header Files

**设置名称：** `APPLY_RULES_IN_COPY_HEADERS`

启用此设置会使 target 的 Copy Headers 构建阶段中的所有 Public 和 Private 头文件由构建规则处理。这样就可以定义自定义构建规则来处理这些头文件。自定义脚本规则可以相对于 `HEADER_OUTPUT_DIR`（该脚本会得到此路径，且已考虑头文件可见性）来定义其输出。脚本还会收到 `SCRIPT_HEADER_VISIBILITY`（“public”或“private”）。启用此设置后，不应由构建规则处理的文件可能需要移到 Copy Files 构建阶段。

### Enable App Shortcuts Flexible Matching

**设置名称：** `APP_SHORTCUTS_ENABLE_FLEXIBLE_MATCHING`

启用后，会生成 App Shortcuts Flexible Matching 所需的资源。

### Architectures

**设置名称：** `ARCHS`

产品将为之构建的架构列表。这通常设为平台提供的一个预定义构建设置。如果指定了多个架构，则会生成一个通用二进制文件。

### Alternate App Icon Sets

**设置名称：** `ASSETCATALOG_COMPILER_ALTERNATE_APPICON_NAMES`

一组要作为附加内容包含在构建产品中的 App 图标集名称。这些图标在运行时可用作备用 App 图标。这是 `--include-all-app-icons` 的一种替代方式，可提供更精细的控制。

### Primary App Icon Set Name

**设置名称：** `ASSETCATALOG_COMPILER_APPICON_NAME`

target 默认 App 图标所用的 App 图标集名称。其内容会被合并到 `Info.plist` 中。

### Watch Complication Name

**设置名称：** `ASSETCATALOG_COMPILER_COMPLICATION_NAME`

要从资源目录中使用的 Watch 复杂功能名称。

### Generate Asset Symbols

**设置名称：** `ASSETCATALOG_COMPILER_GENERATE_ASSET_SYMBOLS`

为目录中的每个颜色和图像生成资源符号。

### Generate Swift Asset Symbol Framework Support

**设置名称：** `ASSETCATALOG_COMPILER_GENERATE_ASSET_SYMBOL_FRAMEWORKS`

为指定的 UI 框架（例如 SwiftUI、UIKit、AppKit）生成资源符号支持。

### Generate Swift Asset Symbol Extensions

**设置名称：** `ASSETCATALOG_COMPILER_GENERATE_SWIFT_ASSET_SYMBOL_EXTENSIONS`

在 Apple 框架的颜色和图像类型上生成资源符号扩展。

### Global Accent Color Name

**设置名称：** `ASSETCATALOG_COMPILER_GLOBAL_ACCENT_COLOR_NAME`

作为 target 强调色使用的颜色资源名称，在 iOS 和 watchOS 上用作默认的着色色，在 macOS 上用作强调色。

### Include All App Icon Assets

**设置名称：** `ASSETCATALOG_COMPILER_INCLUDE_ALL_APPICON_ASSETS`

当为 true 时，target 资源目录中的所有 App 图标资源都会包含在构建产品中，使其在运行时可用作备用 App 图标。当为 false 时，构建产品中只会包含主 App 图标。

### Include Asset Localizations in Info.plist

**设置名称：** `ASSETCATALOG_COMPILER_INCLUDE_INFOPLIST_LOCALIZATIONS`

启用后，会在生成的部分 Info.plist 文件中的 CFBundleLocalizations 键下，包含所选资源的本地化信息。这样即使 Bundle 中没有对应的 lproj 目录，这些资源也能在运行时使用。

### Asset Catalog Launch Image Set Name

**设置名称：** `ASSETCATALOG_COMPILER_LAUNCHIMAGE_NAME`

资源目录中启动图像集的名称，其内容会被合并到 `Info.plist` 中。

### Leaderboard Identifier Prefix

**设置名称：** `ASSETCATALOG_COMPILER_LEADERBOARD_IDENTIFIER_PREFIX`

资源目录中的排行榜可以选择指定一个 Game Center 标识符。如果没有指定，其名称将以此值作为前缀，以生成自动生成的标识符。

### Leaderboard Set Identifier Prefix

**设置名称：** `ASSETCATALOG_COMPILER_LEADERBOARD_SET_IDENTIFIER_PREFIX`

资源目录中的排行榜集可以选择指定一个 Game Center 标识符。如果没有指定，其名称将以此值作为前缀，以生成自动生成的标识符。

### Optimization

**设置名称：** `ASSETCATALOG_COMPILER_OPTIMIZATION`

没有值时，编译器使用默认优化方式。你也可以指定 `time` 以针对访问速度优化，或指定 `space` 以生成更小的已编译资源目录。

### Skip App Store Deployment

**设置名称：** `ASSETCATALOG_COMPILER_SKIP_APP_STORE_DEPLOYMENT`

是否执行 App Store 专属行为，例如各种验证。例如，为 iOS 或 watchOS App 构建时，如果不存在 1024 尺寸的 App Store 图标会发出警告，但仅在为 App Store 分发而编译时才会如此。

### Standalone Icon File Behavior

**设置名称：** `ASSETCATALOG_COMPILER_STANDALONE_ICON_BEHAVIOR`

控制除了在 Assets.car 文件中包含内容之外，是否还为主 App 图标创建独立的 PNG 或 ICNS 文件。默认情况下，会包含一小部分尺寸作为独立文件，使外部管理工具无需读取 CAR 文件即可显示具有代表性的图标。可将其设为“all”或“none”，以包含更多或更少尺寸的图标作为独立文件。

### Sticker Pack Identifier Prefix

**设置名称：** `ASSETCATALOG_COMPILER_STICKER_PACK_IDENTIFIER_PREFIX`

资源目录中的贴纸包可以选择指定一个标识符。如果没有指定，其名称将以此值作为前缀，以生成自动生成的标识符。

### Widget Background Color Name

**设置名称：** `ASSETCATALOG_COMPILER_WIDGET_BACKGROUND_COLOR_NAME`

用作小组件背景色的颜色资源名称。

### Show Notices

**设置名称：** `ASSETCATALOG_NOTICES`

显示编译资源目录期间遇到的提示信息。

### Asset Catalog Other Flags

**设置名称：** `ASSETCATALOG_OTHER_FLAGS`

将附加标志传递给资源目录编译器。

### Show Warnings

**设置名称：** `ASSETCATALOG_WARNINGS`

显示编译资源目录期间遇到的警告。

### Asset Pack Manifest URL Prefix

**设置名称：** `ASSET_PACK_MANIFEST_URL_PREFIX`

如果设为空字符串以外的任何值，`AssetPackManifest.plist` 文件中的每个 URL 都将由此字符串加上资源包名称构成。如果未设置，`AssetPackManifest.plist` 中的 URL 会按照适合资源包构建位置的方式生成。此前缀字符串不会以任何方式被转义或加引号，因此任何必要的转义都必须是 URL 字符串本身的一部分。此设置仅影响 `AssetPackManifest.plist` 文件中的 URL——不影响资源包在本地文件系统中的构建位置。

### Apple Events

**设置名称：** `AUTOMATION_APPLE_EVENTS`

一个布尔值，指示该 App 是否可以提示用户，请求向其他 App 发送 Apple 事件的权限。

### Active Build Components

**设置名称：** `BUILD_COMPONENTS`

此操作期间正在构建的组件列表。

### Build Libraries for Distribution

**设置名称：** `BUILD_LIBRARY_FOR_DISTRIBUTION`

确保你的库以适合分发的方式构建。对于 Swift，这会启用对库演进（library evolution）的支持，并生成一个模块接口文件。

### Build Known Localizations Only

**设置名称：** `BUILD_ONLY_KNOWN_LOCALIZATIONS`

启用后，只会构建项目明确支持的语言对应的内容。

### Build Variants

**设置名称：** `BUILD_VARIANTS`

将要生成的已链接二进制文件的构建变体列表。默认情况下，只会生成 `normal` 变体。其他常见值包括 `debug` 和 `profile`。

### BUILT_PRODUCTS_DIR

**设置名称：** `BUILT_PRODUCTS_DIR`

标识可以找到产品所有文件的目录。此目录包含产品文件或指向这些文件的符号链接。Run Script 构建阶段可以使用此构建设置的值，作为引用一个或多个 target 所构建的产品文件的便捷方式，即使这些文件分散在整个目录层级结构中（例如，当 `DEPLOYMENT_LOCATION` 设为 `YES` 时）。

### Bundle Loader

**设置名称：** `BUNDLE_LOADER`

指定将要加载正在链接的 Bundle 输出文件的可执行文件。Bundle 中的未定义符号会针对指定的可执行文件进行检查，就像它是该 Bundle 所链接的动态库之一那样。

### Enable C++ Container Overflow Checks

**设置名称：** `CLANG_ADDRESS_SANITIZER_CONTAINER_OVERFLOW`

启用 Address Sanitizer 时检查 C++ 容器溢出。此检查要求整个应用程序都使用 Address Sanitizer 构建。如果不是，可能会报告误报。

### Allow Non-modular Includes In Framework Modules

**设置名称：** `CLANG_ALLOW_NON_MODULAR_INCLUDES_IN_FRAMEWORK_MODULES`

启用此设置允许在框架模块内部使用非模块化的 include。这本质上是不安全的，因为当任何客户端同时导入该框架和这些非模块化 include 时，此类头文件可能导致重复定义。

### Dead Stores

**设置名称：** `CLANG_ANALYZER_DEADCODE_DEADSTORES`

检查存入变量后再也没有被读取过的值。

### Division by Zero

**设置名称：** `CLANG_ANALYZER_DIVIDE_BY_ZERO`

检查除以零的情况。

### Misuse of Grand Central Dispatch

**设置名称：** `CLANG_ANALYZER_GCD`

检查 Grand Central Dispatch API 的误用情况。

### Performance Anti-Patterns with Grand Central Dispatch

**设置名称：** `CLANG_ANALYZER_GCD_PERFORMANCE`

检查可能导致性能不佳的 Grand Central Dispatch 用法模式。

### Violation of IOKit and libkern Reference Counting Rules

**设置名称：** `CLANG_ANALYZER_LIBKERN_RETAIN_COUNT`

查找与继承自 OSObject 的对象相关的泄漏和过度释放情况。

### Missing Localization Context Comment

**设置名称：** `CLANG_ANALYZER_LOCALIZABILITY_EMPTY_CONTEXT`

当对 `NSLocalizedString()` 宏的调用缺少供本地化人员使用的上下文注释时发出警告。

### Missing Localizability

**设置名称：** `CLANG_ANALYZER_LOCALIZABILITY_NONLOCALIZED`

当一个未本地化的字符串被传递给期望本地化字符串的用户界面方法时发出警告。

### Improper Memory Management

**设置名称：** `CLANG_ANALYZER_MEMORY_MANAGEMENT`

警告内存泄漏、释放后使用以及其他 API 误用情况。

### Violation of Mach Interface Generator Conventions

**设置名称：** `CLANG_ANALYZER_MIG_CONVENTIONS`

当 MIG 例程违反内存管理约定时发出警告。

### Misuse of 'nonnull'

**设置名称：** `CLANG_ANALYZER_NONNULL`

检查 `nonnull` 参数和返回类型的误用情况。

### Dereference of Null Pointers

**设置名称：** `CLANG_ANALYZER_NULL_DEREFERENCE`

检查对空指针的解引用。

### Suspicious Conversions of NSNumber and CFNumberRef

**设置名称：** `CLANG_ANALYZER_NUMBER_OBJECT_CONVERSION`

当一个数字对象（例如 `NSNumber`、`CFNumberRef`、`OSNumber` 或 `OSBoolean` 的实例）被比较或转换为基本类型值而非另一个对象时发出警告。

### @synchronized with nil mutex

**设置名称：** `CLANG_ANALYZER_OBJC_ATSYNC`

对用作 `@synchronized` 互斥锁的 `nil` 指针发出警告。

### Misuse of Collections API

**设置名称：** `CLANG_ANALYZER_OBJC_COLLECTIONS`

如果 `CF` 集合是用非指针大小的值创建的，发出警告。检查 `NS` 集合是否使用非 Objective-C 类型的元素初始化。

### Improper Instance Cleanup in '-dealloc'

**设置名称：** `CLANG_ANALYZER_OBJC_DEALLOC`

当一个实例在 `-dealloc` 中被不正确地清理时发出警告。

### Misuse of Objective-C generics

**设置名称：** `CLANG_ANALYZER_OBJC_GENERICS`

如果一个特化的泛型类型被转换为不兼容的类型，发出警告。

### Method Signatures Mismatch

**设置名称：** `CLANG_ANALYZER_OBJC_INCOMP_METHOD_TYPES`

警告存在类型不兼容情况的 Objective-C 方法签名。

### Improper Handling of CFError and NSError

**设置名称：** `CLANG_ANALYZER_OBJC_NSCFERROR`

如果接受 `CFErrorRef` 或 `NSError` 的函数无法指示发生了错误，发出警告。

### Violation of Reference Counting Rules

**设置名称：** `CLANG_ANALYZER_OBJC_RETAIN_COUNT`

警告泄漏和不当的引用计数管理。

### Violation of 'self = [super init]' Rule

**设置名称：** `CLANG_ANALYZER_OBJC_SELF_INIT`

检查在 Objective-C 初始化方法内是否正确调用了 `super init`。

### Unused Ivars

**设置名称：** `CLANG_ANALYZER_OBJC_UNUSED_IVARS`

警告从未被使用过的私有 ivar。

### C-style Downcasts of IOKit Objects

**设置名称：** `CLANG_ANALYZER_OSOBJECT_C_STYLE_CAST`

当使用 C 风格转换将指针向下转换为 OSObject 时发出警告。感知 RTTI 的转换（OSRequiredCast、OSDynamicCast）更安全，应改用它们而非 C 风格转换，以避免潜在的类型混淆攻击。

### EXPERIMENTAL Buffer overflows

**设置名称：** `CLANG_ANALYZER_SECURITY_BUFFER_OVERFLOW_EXPERIMENTAL`

检查潜在的缓冲区溢出。

### Floating Point Value Used as Loop Counter

**设置名称：** `CLANG_ANALYZER_SECURITY_FLOATLOOPCOUNTER`

当使用浮点值作为循环计数器时发出警告（CERT: FLP30-C, FLP30-CPP）。

### Use of 'getpw', 'gets' (Buffer Overflow)

**设置名称：** `CLANG_ANALYZER_SECURITY_INSECUREAPI_GETPW_GETS`

警告 `getpw` 和 `gets` 的使用。这些函数很危险，因为它们可能引发缓冲区溢出。

### Use of 'mktemp' or Predictable 'mktemps'

**设置名称：** `CLANG_ANALYZER_SECURITY_INSECUREAPI_MKSTEMP`

警告 `mktemp` 的使用，它会生成可预测的临时文件。它已被 `mktemps` 淘汰。当 `mkstemp` 在格式字符串中传入的 `X` 少于 6 个时发出警告。

### Use of 'rand' Functions

**设置名称：** `CLANG_ANALYZER_SECURITY_INSECUREAPI_RAND`

警告 `rand`、`random` 及相关函数的使用，它们会生成可预测的随机数序列。请改用 `arc4random`。

### Use of 'strcpy' and 'strcat'

**设置名称：** `CLANG_ANALYZER_SECURITY_INSECUREAPI_STRCPY`

警告 `strcpy` 和 `strcat` 函数的使用，它们可能导致缓冲区溢出。请改用 `strlcpy` 或 `strlcat`。

### Unchecked Return Values

**设置名称：** `CLANG_ANALYZER_SECURITY_INSECUREAPI_UNCHECKEDRETURN`

警告那些返回值必须始终被检查的敏感函数的使用。

### Use of 'vfork'

**设置名称：** `CLANG_ANALYZER_SECURITY_INSECUREAPI_VFORK`

警告 `vfork` 函数的使用，它本质上是不安全的。请改用更安全的 `posix_spawn` 函数。

### Misuse of Keychain Services API

**设置名称：** `CLANG_ANALYZER_SECURITY_KEYCHAIN_API`

检查 Keychain Services API 返回的钥匙串属性列表和数据缓冲区的泄漏情况。

### Use-After-Move Errors in C++

**设置名称：** `CLANG_ANALYZER_USE_AFTER_MOVE`

当一个 C++ 对象在被移动（move）之后仍被使用时发出警告。

### C++ Language Dialect

**设置名称：** `CLANG_CXX_LANGUAGE_STANDARD`

选择一种标准或非标准的 C++ 语言方言。可选项包括：

- _C++98：_ 接受带修正案的 ISO C++ 1998，但不含 GNU 扩展。[-std=c++98]
- _GNU++98：_ 接受带修正案的 ISO C++ 1998 及 GNU 扩展。[-std=gnu++98]
- _C++11：_ 接受带修正案的 ISO C++ 2011 标准，但不含 GNU 扩展。[-std=c++11]
- _GNU++11：_ 接受带修正案的 ISO C++ 2011 标准及 GNU 扩展。[-std=gnu++11]
- _C++14：_ 接受带修正案的 ISO C++ 2014 标准，但不含 GNU 扩展。[-std=c++14]
- _GNU++14：_ 接受带修正案的 ISO C++ 2014 标准及 GNU 扩展。[-std=gnu++14]
- _C++17：_ 接受带修正案的 ISO C++ 2017 标准，但不含 GNU 扩展。[-std=c++17]
- _GNU++17：_ 接受带修正案的 ISO C++ 2017 标准及 GNU 扩展。[-std=gnu++17]
- _C++20：_ 接受带修正案的 ISO C++ 2020 标准，但不含 GNU 扩展。[-std=c++20]
- _GNU++20：_ 接受带修正案的 ISO C++ 2020 标准及 GNU 扩展。[-std=gnu++20]
- _C++23：_ 接受带修正案的 ISO C++ 2023 标准，但不含 GNU 扩展。[-std=c++23]
- _GNU++23：_ 接受带修正案的 ISO C++ 2023 标准及 GNU 扩展。[-std=gnu++23]
- _Compiler Default：_ 让编译器使用其默认的 C++ 语言方言。除非有特殊需求，这通常是最佳选择。（目前等同于 GNU++98。）

### Enable C++ Standard Library Hardening

**设置名称：** `CLANG_CXX_STANDARD_LIBRARY_HARDENING`

在 C++ 标准库中启用加固（hardening）。

可用值：

- _No：_ 禁用。不进行运行时加固检查。
- _Yes (fast)：_ 在运行时启用低开销的安全关键检查。
- _Yes (extensive)：_ 在运行时启用低开销检查，以发现安全问题及一般性逻辑错误。
- _Yes (debug)：_ 启用库中所有可用的检查，包括高开销的启发式检查和内部断言。此模式**不应**在生产环境中使用。

此设置定义了 `_LIBCPP_HARDENING_MODE` 预处理器宏的值。

### Debug Information Level

**设置名称：** `CLANG_DEBUG_INFORMATION_LEVEL`

切换启用调试符号时发出的调试信息量。这会影响生成的调试信息的大小，在某些情况下（例如使用 LTO 的大型项目）可能会有影响。

### Enable Typed Allocator in C++

**设置名称：** `CLANG_ENABLE_CPLUSPLUS_TYPED_ALLOCATOR_SUPPORT`

启用编译器对 C++ 中分配调用的重写，以向分配器提供类型信息。可缓解释放后使用（use-after-free）安全漏洞。

### Destroy Static Objects

**设置名称：** `CLANG_ENABLE_CPP_STATIC_DESTRUCTORS`

控制具有 static 或 thread 存储期的变量是否应运行其退出时析构函数。

### Enable Typed Allocator in C

**设置名称：** `CLANG_ENABLE_C_TYPED_ALLOCATOR_SUPPORT`

启用编译器对 C 中分配调用的重写，以向分配器提供类型信息。可缓解释放后使用（use-after-free）安全漏洞。

### Enable Modules (C and Objective-C)

**设置名称：** `CLANG_ENABLE_MODULES`

启用系统 API 使用模块（module）。系统头文件会作为语义模块导入，而非原始头文件。这可以带来更快的构建速度和项目索引速度。

### Enable Clang Module Debugging

**设置名称：** `CLANG_ENABLE_MODULE_DEBUGGING`

启用此设置后，`clang` 会使用 `clang` 模块和预编译头文件中可用的共享调试信息。这会带来更小的构建产物、更快的编译时间以及更完整的调试信息。仅当为分发而构建带调试信息的静态库时，才应禁用此设置。

### Objective-C Automatic Reference Counting

**设置名称：** `CLANG_ENABLE_OBJC_ARC`

编译带引用计数的 Objective-C 代码，使其使用自动引用计数（Automatic Reference Counting）。使用自动引用计数编译的代码，与使用手动引用计数（例如传统的 `retain` 和 `release` 消息）或自动引用计数编译的其他代码（例如框架）兼容。[-fobjc-arc]

### Enable Objective-C ARC Exceptions

**设置名称：** `CLANG_ENABLE_OBJC_ARC_EXCEPTIONS`

此设置使 clang 在使用 ARC 合成 retain 和 release 时，使用对异常处理安全的代码。如果没有此设置，ARC 就不是异常安全的。仅适用于 Objective-C。[-fobjc-arc-exceptions]

### Weak References in Manual Retain Release

**设置名称：** `CLANG_ENABLE_OBJC_WEAK`

编译 Objective-C 代码，为使用手动保留释放（manual retain release，MRR）语义编译的代码启用弱引用。

### Enable Stack Zero Initialization

**设置名称：** `CLANG_ENABLE_STACK_ZERO_INIT`

作为一种安全防护措施，自动将栈变量初始化为零。

### Do not index C macros

**设置名称：** `CLANG_INDEX_STORE_IGNORE_MACROS`

不要将 C 宏的条目输出到 Index Store 中。

### Implicitly Link Objective-C Runtime Support

**设置名称：** `CLANG_LINK_OBJC_RUNTIME`

在链接使用 Objective-C 代码的 target 时，隐式链接 Foundation（如果部署回旧版操作系统，还会链接一个向后兼容库，以便较新的语言特性能在原生不支持该运行时支持的操作系统上运行）。大多数使用 Objective-C 的 target 都应使用此设置，尽管在少数情况下，某个 target 应选择退出此行为。

### Link Frameworks Automatically

**设置名称：** `CLANG_MODULES_AUTOLINK`

自动链接通过 `#import` 或 `#include` 引用的 SDK 框架。此功能还要求启用对模块的支持。此构建设置仅适用于 C 系语言。

### Disable Private Modules Warnings

**设置名称：** `CLANG_MODULES_DISABLE_PRIVATE_WARNING`

禁用与推荐的私有模块命名用法相关的警告。仅当启用了对模块的支持时，此设置才有意义。

### Optimization Profile File

**设置名称：** `CLANG_OPTIMIZATION_PROFILE_FILE`

当启用 `CLANG_USE_OPTIMIZATION_PROFILE` 时所使用的性能分析数据文件的路径。

### Mode of Analysis for 'Build'

**设置名称：** `CLANG_STATIC_ANALYZER_MODE`

静态分析器在 Build 操作期间所用的深度。使用 `Deep` 可发挥分析器的全部能力。使用 `Shallow` 可加快分析速度。

### Mode of Analysis for 'Analyze'

**设置名称：** `CLANG_STATIC_ANALYZER_MODE_ON_ANALYZE_ACTION`

静态分析器在 Analyze 操作期间所用的深度。使用 `Deep` 可发挥分析器的全部能力。使用 `Shallow` 可加快分析速度。

### Side Effects in Assert Conditions

**设置名称：** `CLANG_TIDY_BUGPRONE_ASSERT_SIDE_EFFECT`

当 assert 或 NSAssert 的条件存在副作用时发出警告。断言条件在发行版构建期间不会被求值。

### Infinite Loops

**设置名称：** `CLANG_TIDY_BUGPRONE_INFINITE_LOOP`

当发现某个循环没有终止条件时发出警告。

### Moves of Universal References

**设置名称：** `CLANG_TIDY_BUGPRONE_MOVE_FORWARDING_REFERENCE`

当对通用引用（universal reference）使用 std::move，会导致非临亡（non-expiring）左值参数被意外移动时发出警告。

### Redundant Nested 'if' Conditions

**设置名称：** `CLANG_TIDY_BUGPRONE_REDUNDANT_BRANCH_CONDITION`

当一个 if 语句的条件与它嵌套于其中的更大 if 语句的条件等价、因而是冗余的时，发出警告。

### Redundant Expressions

**设置名称：** `CLANG_TIDY_MISC_REDUNDANT_EXPRESSION`

当算术或逻辑表达式的某个子表达式对结果没有影响、因而可以省略时，发出警告。

### Trivial automatic variable initialization

**设置名称：** `CLANG_TRIVIAL_AUTO_VAR_INIT`

指定栈变量应保持未初始化状态（这可能在使用未初始化的栈变量时导致无意的信息泄露），还是应进行模式初始化（pattern-initialized）。

### Enable Extra Integer Checks

**设置名称：** `CLANG_UNDEFINED_BEHAVIOR_SANITIZER_INTEGER`

除了检查有符号整数溢出之外，还检查无符号整数溢出。

### Enable Nullability Annotation Checks

**设置名称：** `CLANG_UNDEFINED_BEHAVIOR_SANITIZER_NULLABILITY`

检查函数调用、返回语句和赋值中是否违反了可空性（nullability）注解。

### Use Optimization Profile

**设置名称：** `CLANG_USE_OPTIMIZATION_PROFILE`

启用此设置后，`clang` 在构建某个 target 时会使用为其收集的优化性能分析数据。

### Use Response Files

**设置名称：** `CLANG_USE_RESPONSE_FILE`

启用此设置后，构建系统会使用响应文件（response file）在相似的多次 `clang` 调用之间共享公共参数，从而消除构建日志中的冗余信息。

### Out-of-Range Enum Assignments

**设置名称：** `CLANG_WARN_ASSIGN_ENUM`

当把超出枚举类型取值范围的整数常量赋给枚举值时发出警告。

### Usage of implicit sequentially-consistent atomics

**设置名称：** `CLANG_WARN_ATOMIC_IMPLICIT_SEQ_CST`

当某个原子操作使用了隐式的顺序一致（sequentially-consistent）内存顺序，而不是显式指定内存顺序时发出警告。

### Block Capture of Autoreleasing

**设置名称：** `CLANG_WARN_BLOCK_CAPTURE_AUTORELEASING`

警告 block 捕获隐式 autoreleasing 参数的情况。

### Implicit Boolean Conversions

**设置名称：** `CLANG_WARN_BOOL_CONVERSION`

警告那些可疑的、向布尔值的隐式转换。例如，当 `foo` 是某个函数的名称时，写成 `if (foo)` 会触发一次警告。

### Suspicious Commas

**设置名称：** `CLANG_WARN_COMMA`

警告逗号运算符的可疑用法。

### Completion Handler Misuse

**设置名称：** `CLANG_WARN_COMPLETION_HANDLER_MISUSE`

当一个被注解为完成处理程序的类函数参数，在某条执行路径上被调用了不止一次、或者根本没有被调用时发出警告。

### Implicit Constant Conversions

**设置名称：** `CLANG_WARN_CONSTANT_CONVERSION`

警告常量值的隐式转换会导致该常量值发生变化的情况，无论是精度损失，还是含义完全改变。

### Using C++11 extensions in earlier versions of C++

**设置名称：** `CLANG_WARN_CXX0X_EXTENSIONS`

使用早于 C++11 的语言标准编译 C++ 代码时，警告 C++11 扩展的使用情况。

### Deleting Instance of Polymorphic Class with No Virtual Destructor

**设置名称：** `CLANG_WARN_DELETE_NON_VIRTUAL_DTOR`

当删除一个具有虚函数、但没有虚析构函数的多态类的实例时发出警告。

### Overriding Deprecated Objective-C Methods

**设置名称：** `CLANG_WARN_DEPRECATED_OBJC_IMPLEMENTATIONS`

如果一个 Objective-C 类继承自已废弃的类，或者重写了一个已被标记为已废弃或不可用的方法，发出警告。

### Direct usage of 'isa'

**设置名称：** `CLANG_WARN_DIRECT_OBJC_ISA_USAGE`

警告直接访问 Objective-C 的 `isa` 指针、而不是使用运行时 API 的情况。

### Documentation Comments

**设置名称：** `CLANG_WARN_DOCUMENTATION_COMMENTS`

警告文档注释（`doxygen` 风格）中的问题，例如缺失或不正确的文档标签。

### Empty Loop Bodies

**设置名称：** `CLANG_WARN_EMPTY_BODY`

警告那些看起来可疑的空循环体。

### Implicit Enum Conversions

**设置名称：** `CLANG_WARN_ENUM_CONVERSION`

警告不同种类枚举值之间的隐式转换。例如，这可以捕获将错误的枚举标志用作函数或方法参数的问题。

### Implicit Float Conversions

**设置名称：** `CLANG_WARN_FLOAT_CONVERSION`

警告把浮点数转换为整数的隐式转换。

### Public Framework Header Includes Private Framework Header

**设置名称：** `CLANG_WARN_FRAMEWORK_INCLUDE_PRIVATE_FROM_PUBLIC`

当一个公共框架头文件包含了一个私有框架头文件时发出警告。

### Implicit Fallthrough in Switch Statement

**设置名称：** `CLANG_WARN_IMPLICIT_FALLTHROUGH`

警告 switch 语句中的隐式贯穿（fallthrough）。使用 `__attribute__((fallthrough))`（C/ObjC）或 `[[fallthrough]]`（C++）来标记有意的贯穿。

### Implicit Signedness Conversions

**设置名称：** `CLANG_WARN_IMPLICIT_SIGN_CONVERSION`

警告会改变整数值符号的隐式整数转换。

### Infinite Recursion

**设置名称：** `CLANG_WARN_INFINITE_RECURSION`

如果一个函数的所有路径都会调用自身，发出警告。

### Implicit Integer to Pointer Conversions

**设置名称：** `CLANG_WARN_INT_CONVERSION`

警告指针和整数之间的隐式转换。例如，这可以捕获错误地混用 `NSNumber*` 和原始整数的问题。

### Missing Noescape Annotation

**设置名称：** `CLANG_WARN_MISSING_NOESCAPE`

警告方法签名中缺失的 noescape 注解。

### Implicit Non-Literal Null Conversions

**设置名称：** `CLANG_WARN_NON_LITERAL_NULL_CONVERSION`

警告将求值为零的非字面量表达式当作空指针处理的情况。

### Incorrect Uses of Nullable Values

**设置名称：** `CLANG_WARN_NULLABLE_TO_NONNULL_CONVERSION`

当一个可空表达式被用在不允许的地方（例如作为 `_Nonnull` 参数传递）时发出警告。

### Implicit ownership types on out parameters

**设置名称：** `CLANG_WARN_OBJC_EXPLICIT_OWNERSHIP_TYPE`

警告作为输出参数的 Objective-C 对象引用上的隐式所有权类型。例如，声明一个类型为 `NSObject**` 的参数会产生警告，因为编译器会假定该输出参数的所有权类型是 `__autoreleasing`。

### Implicit Atomic Objective-C Properties

**设置名称：** `CLANG_WARN_OBJC_IMPLICIT_ATOMIC_PROPERTIES`

警告隐式为 atomic 的 `@property` 声明。

### Implicit retain of 'self' within blocks

**设置名称：** `CLANG_WARN_OBJC_IMPLICIT_RETAIN_SELF`

警告 block 内隐式保留（retain） `self` 的情况，这可能造成保留环（retain cycle）。

### Interface Declarations of Instance Variables

**设置名称：** `CLANG_WARN_OBJC_INTERFACE_IVARS`

警告在 `@interface` 中声明实例变量的情况。

### Implicit Objective-C Literal Conversions

**设置名称：** `CLANG_WARN_OBJC_LITERAL_CONVERSION`

警告从 Objective-C 字面量到不兼容类型值的隐式转换。

### Implicit Synthesized Properties

**设置名称：** `CLANG_WARN_OBJC_MISSING_PROPERTY_SYNTHESIS`

从 Xcode 4.4 开始，Apple Clang 会隐式合成那些没有使用 `@synthesize` 显式合成的属性。此设置会警告这种隐式行为，即使该属性依然会被合成。这本质上是一个向后兼容性警告，供那些希望继续显式使用 `@synthesize` 的人使用。

### Repeatedly using a __weak reference

**设置名称：** `CLANG_WARN_OBJC_REPEATED_USE_OF_WEAK`

警告在没有将弱引用赋值给强引用的情况下反复使用弱引用的情况。这通常是竞态条件的征兆——弱引用可能在多次访问之间变为 `nil`，从而导致意外行为。赋值给一个临时强引用可以确保对象在相关访问期间保持存活。

### Unintentional Root Class

**设置名称：** `CLANG_WARN_OBJC_ROOT_CLASS`

警告那些无意中没有继承根类（例如 `NSObject`）的类。

### Suspicious Pragma Pack

**设置名称：** `CLANG_WARN_PRAGMA_PACK`

当一个翻译单元缺少终止用的“#pragma pack (pop)”指令，或者紧跟在某个 #include 之后的“#pragma pack”状态与该 #include 之前的状态不同时发出警告。

### Outdated Private Module Map

**设置名称：** `CLANG_WARN_PRIVATE_MODULE`

警告没有使用推荐的私有模块布局的私有模块。

### Quoted Include In Framework Header

**设置名称：** `CLANG_WARN_QUOTED_INCLUDE_IN_FRAMEWORK_HEADER`

当框架头文件中使用了带引号的 include，而不是框架风格的 include 时发出警告。

### Range-based For Loops

**设置名称：** `CLANG_WARN_RANGE_LOOP_ANALYSIS`

警告基于范围的 for 循环。

### Semicolon Before Method Body

**设置名称：** `CLANG_WARN_SEMICOLON_BEFORE_METHOD_BODY`

警告方法实现的签名与方法体之间被忽略的分号。

### Strict Prototypes

**设置名称：** `CLANG_WARN_STRICT_PROTOTYPES`

警告非原型（non-prototype）声明。

### Suspicious Implicit Conversions

**设置名称：** `CLANG_WARN_SUSPICIOUS_IMPLICIT_CONVERSION`

警告各种可能丢失信息、或者本身就很可疑的隐式转换。

### Suspicious Moves

**设置名称：** `CLANG_WARN_SUSPICIOUS_MOVE`

警告 `std::move` 的可疑用法。

### Unguarded availability

**设置名称：** `CLANG_WARN_UNGUARDED_AVAILABILITY`

如果使用了比部署目标（deployment target）更新的 API，却没有使用“if (@available(…))”保护，发出警告。

### Unreachable Code

**设置名称：** `CLANG_WARN_UNREACHABLE_CODE`

警告可能无法到达的代码。

### Ambiguous C++ Parsing Situation

**设置名称：** `CLANG_WARN_VEXING_PARSE`

警告变量声明与函数风格转换之间的解析歧义。

### Using __bridge Casts Outside of ARC

**设置名称：** `CLANG_WARN__ARC_BRIDGE_CAST_NONARC`

警告在未使用 ARC 时使用 `__bridge` 转换的情况，此时它们不会产生任何效果。

### Duplicate Method Definitions

**设置名称：** `CLANG_WARN__DUPLICATE_METHOD_MATCH`

警告在同一个 `@interface` 中多次声明同一个方法的情况。

### Exit-Time C++ Destructors

**设置名称：** `CLANG_WARN__EXIT_TIME_DESTRUCTORS`

警告在应用程序终止时被调用的 C++ 对象析构函数。

### Enable Additional Vector Extensions

**设置名称：** `CLANG_X86_VECTOR_INSTRUCTIONS`

启用扩展向量指令的使用。仅在针对 Intel 架构时使用。

### Code Signing Entitlements

**设置名称：** `CODE_SIGN_ENTITLEMENTS`

指定代码签名 entitlement 的文件路径。

### Code Signing Identity

**设置名称：** `CODE_SIGN_IDENTITY`

你的钥匙串路径中某个钥匙串内、有效代码签名证书的名称，也称为 _common name_。缺失或无效的证书会导致构建错误。

### Code Signing Inject Base Entitlements

**设置名称：** `CODE_SIGN_INJECT_BASE_ENTITLEMENTS`

自动将平台 BaseEntitlements.plist 中的 entitlement 注入可执行文件的代码签名中。

### Code Sign Style

**设置名称：** `CODE_SIGN_STYLE`

此设置指定获取和定位签名资源所用的方法。选择 `Automatic` 可让 Xcode 自动创建和更新描述文件、App ID 和证书。选择 `Manual` 可在开发者网站上自行创建和更新这些内容。

### COMBINE_HIDPI_IMAGES

**设置名称：** `COMBINE_HIDPI_IMAGES`

将不同分辨率的图像文件合并为一个符合 HiDPI 规范的多页 TIFF 文件，适用于 macOS 10.7 及更高版本。只有位于同一目录、具有相同基本文件名和扩展名的图像文件才会被合并。文件名必须符合 HiDPI 所使用的命名约定。

### Enable Compilation Caching

**设置名称：** `COMPILATION_CACHE_ENABLE_CACHING`

为一组特定的输入缓存编译结果。

### Compilation Caching Diagnostic Info

**设置名称：** `COMPILATION_CACHE_ENABLE_DIAGNOSTIC_REMARKS`

为已缓存的编译任务输出诊断信息。

### Enable Index-While-Building Functionality

**设置名称：** `COMPILER_INDEX_STORE_ENABLE`

控制编译器是否应在构建时输出索引数据。

### Compress PNG Files

**设置名称：** `COMPRESS_PNG_FILES`

如果启用，PNG 资源文件在被复制时会被压缩。

### CONFIGURATION

**设置名称：** `CONFIGURATION`

标识该 target 用于生成产品的构建配置，例如 `Debug` 或 `Release`。

### Per-configuration Build Products Path

**设置名称：** `CONFIGURATION_BUILD_DIR`

在针对某个给定配置进行构建期间，放置构建产品的基础路径。默认情况下，此值设为 `$(BUILD_DIR)/$(CONFIGURATION)`。

### Per-configuration Intermediate Build Files Path

**设置名称：** `CONFIGURATION_TEMP_DIR`

在针对某个给定配置进行构建期间，放置中间产物的基础路径。默认情况下，此值设为 `$(PROJECT_TEMP_DIR)/$(CONFIGURATION)`。

### CONTENTS_FOLDER_PATH

**设置名称：** `CONTENTS_FOLDER_PATH`

指定生成的 Bundle 内包含产品文件的目录。

### Preserve HFS Data

**设置名称：** `COPYING_PRESERVES_HFS_DATA`

使资源在复制过程中保留资源分支（resource fork）和 Finder 信息。

### Run unifdef on Product Headers

**设置名称：** `COPY_HEADERS_RUN_UNIFDEF`

如果启用，头文件在被复制到产品中时会经过 `unifdef(1)` 工具处理。

### Unifdef Flags for Product Headers

**设置名称：** `COPY_HEADERS_UNIFDEF_FLAGS`

指定调用 `unifdef(1)` 工具复制头文件时传递给该工具的标志。除非启用了 `COPY_HEADERS_RUN_UNIFDEF`，否则此设置不起作用。

### Strip Debug Symbols During Copy

**设置名称：** `COPY_PHASE_STRIP`

指定在构建期间被复制的二进制文件（例如在 Copy Bundle Resources 或 Copy Files 构建阶段中）是否应剥离调试符号。它不会导致某个 target 的已链接产品被剥离——为此请使用 `STRIP_INSTALLED_PRODUCT`。

### CoreML Model Class Generation Language

**设置名称：** `COREML_CODEGEN_LANGUAGE`

用于生成的 CoreML 模型类的源代码语言。默认情况下，“Automatic”会分析你的项目以确定正确的语言。调整此设置可显式选择“Swift”或“Objective-C”，或者选择“None”以禁用模型类生成。

### CoreML Generated Model Inherits NSObject

**设置名称：** `COREML_CODEGEN_SWIFT_GLOBAL_MODULE`

生成标记有 @objc 且继承自 NSObject 的 Swift 模型类，以便在 Objective-C 中可以访问和使用。如果“CoreML Model Class Generation Language”设为“Objective-C”，此设置不起作用。

### Cpp Other Preprocessor Flags

**设置名称：** `CPP_OTHER_PREPROCESSOR_FLAGS`

使用独立的 C Preprocessor 规则时，传递给 C 预处理器的其他标志。

### Cpp Preprocessor Definitions

**设置名称：** `CPP_PREPROCESSOR_DEFINITIONS`

形如 `foo` 或 `foo=bar` 的预处理器宏的空格分隔列表。这些宏会在使用独立的 C Preprocessor 规则进行预处理时使用。

### Create Info.plist Section in Binary

**设置名称：** `CREATE_INFOPLIST_SECTION_IN_BINARY`

启用此设置会在产品已链接二进制文件的 `__TEXT` 段中创建一个名为 `__info_plist` 的段，其中包含该 target 经过处理的 `Info.plist` 文件。

你可以在运行时使用 [CFBundle](https://developer.apple.com/documentation/corefoundation/cfbundle) 和 [NSBundle](https://developer.apple.com/documentation/foundation/nsbundle)（Objective-C）或 [Bundle](https://developer.apple.com/documentation/foundation/nsbundle)（Swift）API，从已链接的二进制文件中读取经过处理的 `Info.plist` 文件。要打印经过处理的 `Info.plist` 文件，请使用 `plutil(1)` 命令行工具。

此设置仅适用于命令行工具 target。

### CURRENT_ARCH

**设置名称：** `CURRENT_ARCH`

正在处理的活动架构的名称。

### Current Project Version

**设置名称：** `CURRENT_PROJECT_VERSION`

此设置定义了项目的当前版本。该值必须是整数或浮点数，例如 `57` 或 `365.8`。

启用 `GENERATE_INFOPLIST_FILE` 时，会将 `Info.plist` 文件中 [CFBundleVersion](https://developer.apple.com/documentation/bundleresources/information-property-list/cfbundleversion) 键的值设为此构建设置的值。

### CURRENT_VARIANT

**设置名称：** `CURRENT_VARIANT`

正在处理的活动变体的名称。

### Compiler Launcher

**设置名称：** `C_COMPILER_LAUNCHER`

编译器启动器（launcher）的路径。此构建设置会使构建系统使用原始编译器路径和参数调用该启动器工具。例如 `distcc` 和 `ccache`。请勿使用 `CC`、`CPLUSPLUS`、`OBJCC` 或 `OBJCPLUSPLUS` 构建设置来指定编译器启动器。

### Dead Code Stripping

**设置名称：** `DEAD_CODE_STRIPPING`

激活此设置会使 `-dead_strip` 标志通过 `cc(1)` 传递给 `ld(1)`，以开启无效代码剥离。

### Debug Information Format

**设置名称：** `DEBUG_INFORMATION_FORMAT`

要生成的调试信息类型。

- _DWARF：_ 目标文件和已链接产品将使用 DWARF 作为调试信息格式。[dwarf]
- _DWARF with dSYM File：_ 目标文件和已链接产品将使用 DWARF 作为调试信息格式，同时 Xcode 还会生成一个 dSYM 文件，其中包含来自各个目标文件的调试信息（但静态库或目标文件产品不需要 dSYM 文件，也不会为其创建）。[dwarf-with-dsym]

### Debug Information Version

**设置名称：** `DEBUG_INFORMATION_VERSION`

要生成的调试信息的格式。

- _Compiler Default_： 编译器会针对所构建的平台和最低部署目标，生成适当版本的调试信息。[compiler-default]
- _DWARF 4_： 编译器会生成 DWARF 4 调试信息。[dwarf4]
- _DWARF 5_： 编译器会生成 DWARF 5 调试信息。[dwarf5]

### Defines Module

**设置名称：** `DEFINES_MODULE`

如果启用，该产品会被视为定义了自己的模块。这会在适当的时候自动生成 LLVM 模块映射文件，并允许该产品作为模块被导入。

### Deployment Location

**设置名称：** `DEPLOYMENT_LOCATION`

如果启用，构建产品除了放在构建产品文件夹中之外，还会被放置在其安装位置。

### Deployment Postprocessing

**设置名称：** `DEPLOYMENT_POSTPROCESSING`

如果启用，表示应剥离二进制文件，并应将文件模式、属主和组信息设为标准值。

### Deployment Target Build Setting Name

**设置名称：** `DEPLOYMENT_TARGET_SETTING_NAME`

用于有效平台部署目标（deployment target）的构建设置名称。这可用于借助构建设置插值来求值该构建设置，而无需硬编码其名称，例如 `$($(DEPLOYMENT_TARGET_SETTING_NAME))`，也可用于组合其名称包含它的其他设置，例如 `RECOMMENDED_<platform>_DEPLOYMENT_TARGET` 系列设置。

### DERIVED_FILE_DIR

**设置名称：** `DERIVED_FILE_DIR`

标识存放派生源文件（例如由 `lex` 和 `yacc` 生成的文件）的目录。

### Derive Mac Catalyst Product Bundle Identifier

**设置名称：** `DERIVE_MACCATALYST_PRODUCT_BUNDLE_IDENTIFIER`

启用后，当该 target 为 Mac Catalyst 构建时，Xcode 会根据其原始的 Bundle 标识符自动为其派生一个 Bundle 标识符。

### Development Assets

**设置名称：** `DEVELOPMENT_ASSET_PATHS`

仅用于开发的文件和目录。归档和安装构建将排除此内容。

### Development Team

**设置名称：** `DEVELOPMENT_TEAM`

用于签名证书和预配描述文件的开发团队的团队 ID。

### Build Documentation for C++/Objective-C++

**设置名称：** `DOCC_ENABLE_CXX_SUPPORT`

包含 C++/Objective-C++ 头文件中定义的符号的文档。

### Include Documentation for Symbols in Swift Extensions

**设置名称：** `DOCC_EXTRACT_EXTENSION_SYMBOLS`

为在扩展中定义的符号提取 Swift 符号信息，该符号所属的类型并非定义在当前模块中。

### Build Multi-Language Documentation for Swift Only Targets

**设置名称：** `DOCC_EXTRACT_OBJC_INFO_FOR_SWIFT_SYMBOLS`

为只包含 Swift 代码的 target 提取 Objective-C 符号信息，使生成的文档输出既可以按 Swift 阅读，也可以按 Objective-C 阅读。

### Build Multi-Language Documentation for Objective-C Only Targets

**设置名称：** `DOCC_EXTRACT_SWIFT_INFO_FOR_OBJC_SYMBOLS`

为只包含 Objective-C 代码的 target 提取 Swift 符号信息，使生成的文档输出既可以按 Swift 阅读，也可以按 Objective-C 阅读。

### DocC Archive Hosting Base Path

**设置名称：** `DOCC_HOSTING_BASE_PATH`

你的文档网站将要托管在的基础路径。例如，如果你计划将 DocC 存档托管在 `https://example.com/ProjectName/documentation`，而不是 `https://example.com/documentation`，请将此值设为 `"ProjectName"`。

### DOCUMENTATION_FOLDER_PATH

**设置名称：** `DOCUMENTATION_FOLDER_PATH`

标识包含该 Bundle 文档文件的目录。

### Don't Force Info.plist Generation

**设置名称：** `DONT_GENERATE_INFOPLIST_FILE`

如果启用，当 `INFOPLIST_FILE` 构建设置为空时，不要为经过打包的产品自动生成 Info.plist 文件。

### Installation Build Products Location

**设置名称：** `DSTROOT`

执行安装构建时，所有产品的根路径。例如，要将你的产品安装到系统本身，请将此路径设为 `/`。默认值为 `/tmp/$(PROJECT_NAME).dst`，以防止一次 _测试性_ 安装构建意外覆盖最终安装路径中有效且需要的数据。

通常不会按 target 设置此路径，而是在执行 `xcodebuild install` 时作为命令行选项提供。在特殊情况下，也可以在某个构建配置中设置它。

### DSYMUTIL_EMBED_RESOURCES

**设置名称：** `DSYMUTIL_EMBED_RESOURCES`

要嵌入 dSYM Bundle 的资源列表。每个条目的形式为“源=目标”，其中源路径是磁盘上的一个文件或目录，目标路径相对于该 Bundle 的 Contents/Resources 目录。

### Other DTrace Flags

**设置名称：** `DTRACE_OTHER_FLAGS`

传递给 `dtrace` 编译器的其他标志的空格分隔列表。请务必对包含空格或特殊字符的参数（例如可能包含空格的路径名）进行反斜杠转义。如果 Xcode 尚未为某个特定的 `dtrace` 标志提供界面，请使用此设置。

### Compatibility Version

**设置名称：** `DYLIB_COMPATIBILITY_VERSION`

确定生成的库、Bundle 或框架二进制文件的兼容性版本。有关为动态库分配版本号的详情，请参阅 [Dynamic Library Programming Topics](https://developer.apple.com/library/content/documentation/DeveloperTools/Conceptual/DynamicLibraries/000-Introduction/Introduction.html) 中的 [Dynamic Library Design Guidelines](https://developer.apple.com/library/content/documentation/DeveloperTools/Conceptual/DynamicLibraries/100-Articles/DynamicLibraryDesignGuidelines.html#//apple_ref/doc/uid/TP40002013-SW19)。

### Current Library Version

**设置名称：** `DYLIB_CURRENT_VERSION`

此设置定义了项目所构建的任何框架的当前版本。与 `CURRENT_PROJECT_VERSION` 一样，该值必须是整数或浮点数，例如 `57` 或 `365.8`。有关为动态库分配版本号的详情，请参阅 [Dynamic Library Programming Topics](https://developer.apple.com/library/content/documentation/DeveloperTools/Conceptual/DynamicLibraries/000-Introduction/Introduction.html) 中的 [Dynamic Library Design Guidelines](https://developer.apple.com/library/content/documentation/DeveloperTools/Conceptual/DynamicLibraries/100-Articles/DynamicLibraryDesignGuidelines.html#//apple_ref/doc/uid/TP40002013-SW19)。

### Dynamic Library Install Name Base

**设置名称：** `DYLIB_INSTALL_NAME_BASE`

设置动态库中内部“安装路径”（`LC_ID_DYLIB`）的基础值。此值会与 `EXECUTABLE_PATH` 组合，形成完整的安装路径。直接设置 `LD_DYLIB_INSTALL_NAME` 会覆盖此设置。此设置默认为该 target 的 `INSTALL_PATH`。构建动态库以外的任何产品时会忽略此设置。

### Eager Linking

**设置名称：** `EAGER_LINKING`

如果启用，构建系统会为仅含 Swift 的框架和动态库 target 输出一个 TBD 文件，以便在其依赖项完成链接之前，就能解除对依赖它的 target 的链接阻塞。

### Embed Asset Packs In Product Bundle

**设置名称：** `EMBED_ASSET_PACKS_IN_PRODUCT_BUNDLE`

将所有已构建的资源包嵌入产品 Bundle 内部。由于这会抵消按需资源（On Demand Resources）功能带来的性能优势，此设置仅在无法使用资源包服务器进行测试时才有用。

### Enable App Sandbox

**设置名称：** `ENABLE_APP_SANDBOX`

设置后，为某个 target 启用 App 沙盒化。

### Enable Code Coverage Support

**设置名称：** `ENABLE_CODE_COVERAGE`

启用带代码覆盖率插桩的构建。这仅在构建启用了代码覆盖率时使用，通常通过 Xcode scheme 或测试计划设置来完成。

### Enforce Bounds-Safe Buffer Usage in C++

**设置名称：** `ENABLE_CPLUSPLUS_BOUNDS_SAFE_BUFFERS`

启用一种严格的编程模型，通过拒绝原始指针算术（将 -Wunsafe-buffer-usage 警告作为错误启用）并要求对缓冲区操作使用加固过的 C++ 标准库 API，来保证 C++ 中的边界安全。

### Enable Language Extension for Bounds Safety in C

**设置名称：** `ENABLE_C_BOUNDS_SAFETY`

启用 -fbounds-safety 语言扩展，为 C 语言保证边界安全。

### Enable Debug Dylib Support

**设置名称：** `ENABLE_DEBUG_DYLIB`

如果启用，在受支持的平台和 SDK 上，App 和 App 扩展 target 的调试构建将把主二进制代码构建在一个单独的“NAME.debug.dylib”中。加载该 dylib 的桩可执行文件将作为主二进制文件。要让预览执行引擎和其他现代开发功能正常工作，必须启用此设置。如果你的 target 不兼容，可以禁用此设置。

### Enable Enhanced Security

**设置名称：** `ENABLE_ENHANCED_SECURITY`

启用一组安全构建设置，包括指针身份验证、类型化分配器支持、加固过的 C++ 标准库，以及与安全相关的编译器警告。这些设置可以单独禁用。

### Enable Downloads Folder

**设置名称：** `ENABLE_FILE_ACCESS_DOWNLOADS_FOLDER`

此设置指示 App 沙盒化是否允许访问用户下载目录中的文件。

### Enable Movies Folder

**设置名称：** `ENABLE_FILE_ACCESS_MOVIES_FOLDER`

此设置指示 App 沙盒化是否允许访问用户影片目录中的文件。

### Enable Music Folder

**设置名称：** `ENABLE_FILE_ACCESS_MUSIC_FOLDER`

此设置指示 App 沙盒化是否允许访问用户音乐目录中的文件。

### Enable Pictures Folder

**设置名称：** `ENABLE_FILE_ACCESS_PICTURE_FOLDER`

此设置指示 App 沙盒化是否允许访问用户图片目录中的文件。

### Enable Hardened Runtime

**设置名称：** `ENABLE_HARDENED_RUNTIME`

启用加固运行时（hardened runtime）限制。

### ENABLE_HEADER_DEPENDENCIES

**设置名称：** `ENABLE_HEADER_DEPENDENCIES`

指定是否自动跟踪对所包含头文件的依赖关系。

### Incoming Connections (Server)

**设置名称：** `ENABLE_INCOMING_NETWORK_CONNECTIONS`

设置后，启用传入的网络连接。

### Enable Incremental Distill

**设置名称：** `ENABLE_INCREMENTAL_DISTILL`

在资源目录编译器中启用增量 `distill` 选项。此功能为实验性功能，应谨慎启用。

### Enable Module Verifier

**设置名称：** `ENABLE_MODULE_VERIFIER`

为框架启用 clang 模块验证。

### Enable Foundation Assertions

**设置名称：** `ENABLE_NS_ASSERTIONS`

控制由 `NSAssert` 提供的断言逻辑是包含在预处理后的源代码中，还是在预处理期间被省略。禁用断言可以提升代码性能。

### Build Active Resources Only

**设置名称：** `ENABLE_ONLY_ACTIVE_RESOURCES`

针对单一设备构建时，省略不适用的资源。例如，为具有 Retina 显示屏的设备构建时，排除 1x 资源。

### Enable On Demand Resources

**设置名称：** `ENABLE_ON_DEMAND_RESOURCES`

如果启用，已标记的资源——文件和资源目录条目——会根据其标签组合被构建进资源包中。未标记的资源会按正常方式处理。

### Outgoing Connections (Client)

**设置名称：** `ENABLE_OUTGOING_NETWORK_CONNECTIONS`

设置后，启用传出的网络连接。

### Enable Pointer Authentication

**设置名称：** `ENABLE_POINTER_AUTHENTICATION`

以启用指针身份验证的方式构建该 target。会为 `ARCHS_STANDARD` 添加一个带指针身份验证指令的附加架构切片（arm64e）。如果 `ARCHS` 已被覆盖为不基于 `ARCHS_STANDARD`，此设置不起作用。

### Audio Input

**设置名称：** `ENABLE_RESOURCE_ACCESS_AUDIO_INPUT`

设置后，启用使用内置和外接麦克风采集音频。

### Bluetooth

**设置名称：** `ENABLE_RESOURCE_ACCESS_BLUETOOTH`

设置后，启用与已连接蓝牙设备的通信。

### Calendar

**设置名称：** `ENABLE_RESOURCE_ACCESS_CALENDARS`

设置后，启用对用户日历的读写访问。

### Camera

**设置名称：** `ENABLE_RESOURCE_ACCESS_CAMERA`

设置后，启用使用内置和外接摄像头采集图像和影片。

### Contacts

**设置名称：** `ENABLE_RESOURCE_ACCESS_CONTACTS`

设置后，启用对用户通讯录数据库的读写访问。

### Location

**设置名称：** `ENABLE_RESOURCE_ACCESS_LOCATION`

设置后，启用使用定位服务确定用户位置的访问权限。

### Photos Library

**设置名称：** `ENABLE_RESOURCE_ACCESS_PHOTO_LIBRARY`

一个布尔值，指示该 App 是否具有对用户照片图库的读写访问权限。

### Printing

**设置名称：** `ENABLE_RESOURCE_ACCESS_PRINTING`

设置后，启用使用系统已配置的打印机打印文稿和媒体的访问权限。

### USB

**设置名称：** `ENABLE_RESOURCE_ACCESS_USB`

设置后，启用与已连接 USB 设备的通信。

### Enable Security-Relevant Compiler Warnings

**设置名称：** `ENABLE_SECURITY_COMPILER_WARNINGS`

启用一组与安全相关的编译器警告，用于检查常见的边界安全和生命周期安全问题。

### Enable Strict Checking of objc_msgSend Calls

**设置名称：** `ENABLE_STRICT_OBJC_MSGSEND`

控制 `objc_msgSend` 调用在被调用之前是否必须转换为相应的函数指针类型。

### Enable Testability

**设置名称：** `ENABLE_TESTABILITY`

启用此设置会以适合针对该 target 产品运行自动化测试的选项构建该 target。

如果为调试而构建的 target，其产品将会被测试，可以启用此设置。这可能导致测试运行得比原本更慢。

启用此设置时：

- `GCC_SYMBOLS_PRIVATE_EXTERN` 被禁用（`-fvisibility=hidden` 不会传递给 `clang`）。
- `-enable-testing` 会传递给 Swift 编译器。
- `-rdynamic` 会传递给链接器。
- `STRIP_INSTALLED_PRODUCT` 被禁用（不会对生成的二进制文件运行 `strip`）。

### Enable Testing Search Paths

**设置名称：** `ENABLE_TESTING_SEARCH_PATHS`

指定构建系统是否应添加编译和链接测试相关库或框架所需的搜索路径。如果该 target 是测试 target，或者该 target 显式链接了 Testing、XCTest 或 StoreKitTest 框架，此设置默认启用。

### User Script Sandboxing

**设置名称：** `ENABLE_USER_SCRIPT_SANDBOXING`

如果启用，构建系统会对用户脚本进行沙盒化，禁止未声明的输入/输出依赖关系。

### Enable User Selected Files

**设置名称：** `ENABLE_USER_SELECTED_FILES`

此设置指示 App 沙盒化是否允许访问用户通过“打开”或“存储”对话框选择的文件。

### Excluded Architectures

**设置名称：** `EXCLUDED_ARCHS`

该 target 不应为之构建的架构列表。构建该 target 时，这些架构会从 `ARCHS` 列表中移除。如果最终得到的架构列表为空，则不会生成任何二进制文件。这可用于声明某个 target 不支持的架构，以便在 `ARCHS` 在更高层级被覆盖的环境中使用（例如通过 `xcodebuild`）。

### Excluded Explicit Target Dependencies

**设置名称：** `EXCLUDED_EXPLICIT_TARGET_DEPENDENCIES`

一个模式列表（由 `fnmatch(3)` 定义），指定在确定要构建哪些 target 时应_排除_的显式 target 依赖项的名称（另请参阅 `INCLUDED_EXPLICIT_TARGET_DEPENDENCIES`）。此设置可用于定义复杂的过滤条件，以根据其他构建设置决定应构建哪些 target。

### Sub-Directories to Exclude in Recursive Searches

**设置名称：** `EXCLUDED_RECURSIVE_SEARCH_PATH_SUBDIRECTORIES`

这是一个 `fnmatch()` 风格的文件或目录名称模式列表，在执行递归搜索时会被排除。默认情况下，此值设为 `*.nib *.lproj *.framework *.gch *.xcode* *.xcassets *.icon (*) .DS_Store CVS .svn .git .hg *.pbproj *.pbxproj`。通常，如果你覆盖此值，应通过 `$(inherited)` 宏包含默认值。

### Excluded Source File Names

**设置名称：** `EXCLUDED_SOURCE_FILE_NAMES`

一个模式列表（由 `fnmatch(3)` 定义），指定在处理该 target 构建阶段中的文件时应显式_排除_的源文件名称（另请参阅 `INCLUDED_SOURCE_FILE_NAMES`）。此设置可用于定义复杂的过滤条件，以根据其他构建设置决定该阶段应构建哪些文件；例如，`*.$(CURRENT_ARCH).c` 这样的值可以用来根据正在构建的架构排除特定文件。

### EXECUTABLES_FOLDER_PATH

**设置名称：** `EXECUTABLES_FOLDER_PATH`

标识包含其他二进制文件的目录。

### Executable Extension

**设置名称：** `EXECUTABLE_EXTENSION`

这是该 target 生成的可执行产品所使用的扩展名，其默认值基于产品类型确定。

### EXECUTABLE_FOLDER_PATH

**设置名称：** `EXECUTABLE_FOLDER_PATH`

标识包含该 target 所构建二进制文件的目录。

### EXECUTABLE_NAME

**设置名称：** `EXECUTABLE_NAME`

指定该 target 生成的二进制文件的名称。

启用 `GENERATE_INFOPLIST_FILE` 时，会将 `Info.plist` 文件中 [CFBundleExecutable](https://developer.apple.com/documentation/bundleresources/information-property-list/cfbundleexecutable) 键的值设为此构建设置的值。

### EXECUTABLE_PATH

**设置名称：** `EXECUTABLE_PATH`

指定该 target 生成的二进制文件在其 Bundle 内的路径。

### Executable Prefix

**设置名称：** `EXECUTABLE_PREFIX`

该 target 生成的可执行产品所使用的前缀，其默认值基于产品类型确定。

### EXECUTABLE_SUFFIX

**设置名称：** `EXECUTABLE_SUFFIX`

指定二进制文件名的后缀，包括将扩展名与 Bundle 名称其余部分分隔开的字符。

### Exported Symbols File

**设置名称：** `EXPORTED_SYMBOLS_FILE`

一个相对于项目的路径，指向一个列出要导出符号的文件。有关导出符号的详情，请参阅 `ld -exported_symbols_list`。

### FRAMEWORKS_FOLDER_PATH

**设置名称：** `FRAMEWORKS_FOLDER_PATH`

指定包含产品内嵌框架的目录。

### Framework Search Paths

**设置名称：** `FRAMEWORK_SEARCH_PATHS`

这是一个文件夹路径列表，这些文件夹中包含框架，编译 C、Objective-C、C++ 或 Objective-C++ 时，编译器会在其中搜索被包含或导入的头文件，链接器也会在其中搜索产品所使用的框架。路径之间以空白分隔，因此任何包含空格的路径都必须正确加引号。

### Framework Version

**设置名称：** `FRAMEWORK_VERSION`

框架 Bundle 通过将内容放在某个版本文件夹的子文件夹中来进行版本管理，该版本文件夹带有指向当前版本及其内容的链接。

### Run Build Script Phases in Parallel

**设置名称：** `FUSE_BUILD_SCRIPT_PHASES`

如果启用，连续的 run script 阶段在完整指定了其输入和输出依赖关系的情况下，将被允许并行运行。

### 'char' Type Is Unsigned

**设置名称：** `GCC_CHAR_IS_UNSIGNED_CHAR`

启用此设置会使 `char` 默认是无符号的，禁用则使 `char` 默认是有符号的。

### CodeWarrior/MS-Style Inline Assembly

**设置名称：** `GCC_CW_ASM_SYNTAX`

除标准 GCC 语法外，还为内联汇编代码启用 CodeWarrior/Microsoft 语法。

### C Language Dialect

**设置名称：** `GCC_C_LANGUAGE_STANDARD`

选择一种标准或非标准的 C 语言方言。

- _ANSI C：_ 接受 ISO C90 和 ISO C++，关闭不兼容的 GNU 扩展。[-ansi] 不兼容的 GNU 扩展包括 `asm`、`inline` 和 `typeof` 关键字（但不包括等效的 `__asm__`、`__inline__` 和 `__typeof__` 形式），以及用于注释的 `//` 语法。此设置还会启用三字符组（trigraph）。
- _C89：_ 接受 ISO C90（1990），但不含 GNU 扩展。[-std=c89]
- _GNU89：_ 接受 ISO C90 及 GNU 扩展。[-std=gnu89]
- _C99：_ 接受 ISO C99（1999），但不含 GNU 扩展。[-std=c99]
- _GNU99：_ 接受 ISO C99 及 GNU 扩展。[-std=gnu99]
- _C11：_ 接受 ISO C11（2011），但不含 GNU 扩展。[-std=c11]
- _GNU11：_ 接受 ISO C11 及 GNU 扩展。[-std=gnu11]
- _C17：_ 接受 ISO C17（2018），但不含 GNU 扩展。[-std=c17]
- _GNU17：_ 接受 ISO C17 及 GNU 扩展。[-std=gnu17]
- _C23：_ 接受 ISO C23（2024），但不含 GNU 扩展。[-std=c23]
- _GNU23：_ 接受 ISO C23 及 GNU 扩展。[-std=gnu23]
- _Compiler Default：_ 让编译器使用其默认的 C 语言方言。除非有特殊需求，这通常是最佳选择。（目前等同于 GNU99。）

### Generate Position-Dependent Code

**设置名称：** `GCC_DYNAMIC_NO_PIC`

为应用程序提供更快的函数调用。不适用于需要位置无关的共享库。

### Allow 'asm', 'inline', 'typeof'

**设置名称：** `GCC_ENABLE_ASM_KEYWORD`

控制 `asm`、`inline` 和 `typeof` 是被当作关键字处理，还是可以用作标识符。

### Recognize Builtin Functions

**设置名称：** `GCC_ENABLE_BUILTIN_FUNCTIONS`

控制是否识别不以 `__builtin_` 为前缀的内建函数。

GCC 通常会生成特殊代码，以更高效地处理某些内建函数；例如，对 `alloca` 的调用可能变成直接调整栈的单条指令，对 `memcpy` 的调用可能变成内联复制循环。生成的代码通常既更小又更快，但由于这些函数调用不再以调用的形式出现，你无法在这些调用上设置断点，也无法通过链接不同的库来改变这些函数的行为。此外，当一个函数被识别为内建函数时，GCC 可能会利用关于该函数的信息，对该函数的调用中存在的问题发出警告，或生成更高效的代码，即使生成的代码中仍然包含对该函数的调用。例如，当 `printf` 是内建函数时，`-Wformat` 会针对对 `printf` 的错误调用发出警告，并且已知 `strlen` 不会修改全局内存。

### Enable C++ Exceptions

**设置名称：** `GCC_ENABLE_CPP_EXCEPTIONS`

启用 C++ 异常处理。生成传播异常所需的额外代码。对于某些 target，这意味着 GCC 会为所有函数生成帧展开（frame unwind）信息，这可能带来显著的数据大小开销，尽管不会影响执行。如果你没有指定此选项，GCC 会为通常需要异常处理的语言（例如 C++）默认启用它，并为通常不需要异常处理的语言（例如 C）默认禁用它。但是，当编译需要与用 C++ 编写的异常处理程序正确互操作的 C 代码时，你可能需要启用此选项。

### Enable C++ Runtime Types

**设置名称：** `GCC_ENABLE_CPP_RTTI`

为每个带虚函数的类启用信息生成，供 C++ 运行时类型识别功能（`dynamic_cast` 和 `typeid`）使用。如果你不使用该语言的这部分特性，可以通过使用此标志节省一些空间。请注意，异常处理会使用相同的信息，但会按需生成它。

### Enable Exceptions

**设置名称：** `GCC_ENABLE_EXCEPTIONS`

启用异常处理。生成传播异常所需的额外代码。对于某些 target，这意味着 GCC 会为所有函数生成帧展开（frame unwind）信息，这可能带来显著的数据大小开销，尽管不会影响执行。如果你没有指定此选项，GCC 会为通常需要异常处理的语言（例如 C++ 和 Objective-C）默认启用它，并为通常不需要异常处理的语言（例如 C）默认禁用它。但是，当编译需要与用其他语言编写的异常处理程序正确互操作的 C 代码时，你可能需要启用此选项。如果你正在编译不使用异常处理的旧程序，也可能希望禁用此选项。

### Generate Floating Point Library Calls

**设置名称：** `GCC_ENABLE_FLOATING_POINT_LIBRARY_CALLS`

生成包含浮点库调用的输出。

### Kernel Development Mode

**设置名称：** `GCC_ENABLE_KERNEL_DEVELOPMENT`

激活此设置会启用内核开发模式。

### Enable Objective-C Exceptions

**设置名称：** `GCC_ENABLE_OBJC_EXCEPTIONS`

此设置为 Objective-C 代码中的异常处理启用 `@try`/`@catch`/`@throw` 语法。仅适用于 Objective-C。[-fobjc-exceptions]

### Recognize Pascal Strings

**设置名称：** `GCC_ENABLE_PASCAL_STRINGS`

识别并构造 Pascal 风格的字符串字面量。不鼓励在新代码中使用它。

Pascal 字符串字面量的形式为 `"\pstring"`。特殊转义序列 `\p` 表示该字符串的 Pascal 长度字节，会在编译时被替换为紧随其后的字符数。`\p` 只能出现在字符串字面量的开头，不能出现在宽字符串字面量中，也不能作为整型常量出现。

### Enable SSE3 Extensions

**设置名称：** `GCC_ENABLE_SSE3_EXTENSIONS`

指定二进制文件是否使用提供 IA-32 架构 SSE3 扩展访问能力的内建函数。

### Enable SSE4.1 Extensions

**设置名称：** `GCC_ENABLE_SSE41_EXTENSIONS`

指定二进制文件是否使用提供 IA-32 架构 SSE4.1 扩展访问能力的内建函数。

### Enable SSE4.2 Extensions

**设置名称：** `GCC_ENABLE_SSE42_EXTENSIONS`

指定二进制文件是否使用提供 IA-32 架构 SSE4.2 扩展访问能力的内建函数。

### Enable Trigraphs

**设置名称：** `GCC_ENABLE_TRIGRAPHS`

控制源代码中是否允许使用三字符组（trigraph）。

### Relax IEEE Compliance

**设置名称：** `GCC_FAST_MATH`

启用一些不符合 IEEE754 标准、但通常可以正常工作的浮点优化。需要严格遵循 IEEE 标准的程序可能无法配合此选项正常工作。

### Generate Debug Symbols

**设置名称：** `GCC_GENERATE_DEBUGGING_SYMBOLS`

启用或禁用调试符号的生成。启用调试符号时，可以通过 `DEBUG_INFORMATION_FORMAT` 设置控制详细程度。

### Generate Legacy Test Coverage Files

**设置名称：** `GCC_GENERATE_TEST_COVERAGE_FILES`

激活此设置会生成一个 `notes` 文件，`gcov` 代码覆盖率工具可以用它来显示程序覆盖率。

### Increase Sharing of Precompiled Headers

**设置名称：** `GCC_INCREASE_PRECOMPILED_HEADER_SHARING`

启用此选项将在共享相同前缀头文件和预编译头文件目录的 target 之间增加预编译头文件的共享程度。

Xcode 通过基于用于创建 PCH 的编译器命令行选项生成一个哈希值，来区分不同的预编译头文件（PCH）。启用此选项会将某些编译器选项从该哈希中排除。目前此选项会将搜索路径选项（`-I`、`-iquote`、`-isystem`、`-F`、`-L`）从哈希中排除。

启用预编译头文件的增强共享存在一定风险——如果两个 target 使用相同的前缀头文件，但具有不同的包含路径，导致该前缀头文件在被预编译时包含不同的文件，那么可能会产生微妙的问题，因为一个 target 会使用另一个 target 所包含文件构建出的 PCH。在这种情况下，必须关闭此选项以确保正确性。

### Inline Methods Hidden

**设置名称：** `GCC_INLINES_ARE_PRIVATE_EXTERN`

启用后，内联方法的行外副本会被声明为 `private extern`。

### Compile Sources As

**设置名称：** `GCC_INPUT_FILETYPE`

指定是根据每个源文件的文件类型来编译它，还是将该 target 中的所有源文件都当作特定语言处理。

### Instrument Program Flow

**设置名称：** `GCC_INSTRUMENT_PROGRAM_FLOW_ARCS`

激活此设置表示应添加代码，以便对程序流弧（program flow arc）进行插桩。

### Enable Linking With Shared Libraries

**设置名称：** `GCC_LINK_WITH_DYNAMIC_LIBRARIES`

启用此选项允许与共享库链接。这是大多数产品类型的默认设置。

### No Common Blocks

**设置名称：** `GCC_NO_COMMON_BLOCKS`

在 C 中，即使是未初始化的全局变量也分配在目标文件的数据段中，而不是生成为公共块（common block）。这样一来，如果同一个变量在两次不同的编译中被声明（且没有 `extern`），链接它们时就会出现错误。

### Optimization Level

**设置名称：** `GCC_OPTIMIZATION_LEVEL`

指定生成的代码在速度和二进制大小方面的优化程度。

- _None：_ 不优化。[-O0] 使用此设置时，编译器的目标是降低编译成本，并使调试产生预期的结果。各语句相互独立——如果你在语句之间用断点停止程序，就可以为任意变量赋新值，或者将程序计数器改到该函数中的任意其他语句，并得到与源代码完全一致的预期结果。
- _Fast：_ 优化编译会花费稍多的时间，对于大型函数还会占用更多的内存。[-O1] 使用此设置时，编译器会尝试在不进行任何耗费大量编译时间的优化的前提下，减小代码大小和执行时间。在 Apple 的编译器中，进行优化时默认会禁用严格别名（strict aliasing）、块重排序和块间调度。
- _Faster：_ 编译器会执行几乎所有不涉及空间-速度权衡的受支持优化。[-O2] 使用此设置时，编译器不会执行循环展开、函数内联或寄存器重命名。与 `Fast` 设置相比，此设置会同时增加编译时间和生成代码的性能。
- _Fastest：_ 开启 `Faster` 设置指定的所有优化，还会开启函数内联和寄存器重命名选项。此设置可能导致更大的二进制文件。[-O3]
- _Fastest, Smallest：_ 针对大小进行优化。此设置会启用所有通常不会增加代码大小的 `Faster` 优化，还会执行旨在减小代码大小的进一步优化。[-Os]
- _Fastest, Aggressive Optimizations：_ 此设置在启用 `Fastest` 的基础上，还会启用可能破坏严格标准合规性、但在行为良好的代码上应能正常工作的激进优化。[-Ofast]
- _Smallest, Aggressive Size Optimizations：_ 此设置通过将重复的代码模式隔离为一个编译器生成的函数，实现额外的大小节省。[-Oz]

### Precompile Prefix Header

**设置名称：** `GCC_PRECOMPILE_PREFIX_HEADER`

为前缀头文件生成一个预编译头文件，这应该会缩短总体构建时间。

如果前缀头文件或其包含的任何文件很少变化，预编译前缀头文件的效果会最好。如果前缀头文件或其包含的任何文件频繁变化，可能会对总体构建时间产生负面影响。

### Prefix Header

**设置名称：** `GCC_PREFIX_HEADER`

隐式包含指定名称的头文件。给出的路径应为相对于项目的路径，或者是绝对路径。

### Preprocessor Macros

**设置名称：** `GCC_PREPROCESSOR_DEFINITIONS`

形如 `foo` 或 `foo=bar` 的预处理器宏的空格分隔列表。

### Preprocessor Macros Not Used In Precompiled Headers

**设置名称：** `GCC_PREPROCESSOR_DEFINITIONS_NOT_USED_IN_PRECOMPS`

形如 `foo` 或 `foo=bar` 的预处理器宏的空格分隔列表。这些宏在预编译前缀头文件时不会被使用。

### Make Strings Read-Only

**设置名称：** `GCC_REUSE_STRINGS`

复用字符串字面量。

### Short Enumeration Constants

**设置名称：** `GCC_SHORT_ENUMS`

使枚举的大小仅为其可能取值范围所需的大小。

此设置生成的代码可能与未使用此设置生成的代码、或与 macOS 框架不具有二进制兼容性。

### Enforce Strict Aliasing

**设置名称：** `GCC_STRICT_ALIASING`

通过对指针是否可能指向与其他指针相同的对象做出更激进的假设，来优化代码。大量使用指针的程序可能会从中受益，但如果程序没有严格遵循 ISO C 关于对象可以用哪种类型访问的规则，可能会出现意外行为。

### Symbols Hidden by Default

**设置名称：** `GCC_SYMBOLS_PRIVATE_EXTERN`

启用后，除非在代码中使用 `__attribute__((visibility("default")))` 显式标记为要导出，否则所有符号都会被声明为 `private extern`。如果未启用，除非显式标记为 `private extern`，否则所有符号都会被导出。请参阅 [C++ Runtime Environment Programming Guide](https://developer.apple.com/library/content/documentation/DeveloperTools/Conceptual/CppRuntimeEnv/CPPRuntimeEnv.html) 中的 [Controlling Symbol Visibility](https://developer.apple.com/library/content/documentation/DeveloperTools/Conceptual/CppRuntimeEnv/Articles/SymbolVisibility.html#//apple_ref/doc/uid/TP40001670-CJBGBHEJ)。

### Statics are Thread-Safe

**设置名称：** `GCC_THREADSAFE_STATICS`

生成额外的代码，以使用 C++ ABI 中指定的例程对局部静态变量进行线程安全的初始化。对于不需要线程安全的代码，你可以禁用此选项以略微减小代码大小。

### Treat Missing Function Prototypes as Errors

**设置名称：** `GCC_TREAT_IMPLICIT_FUNCTION_DECLARATIONS_AS_ERRORS`

使关于缺失函数原型的警告被当作错误处理。仅适用于 C 和 Objective-C。

### Treat Incompatible Pointer Type Warnings as Errors

**设置名称：** `GCC_TREAT_INCOMPATIBLE_POINTER_TYPE_WARNINGS_AS_ERRORS`

启用此选项会使关于不兼容指针类型的警告被当作错误处理。

### Treat Warnings as Errors

**设置名称：** `GCC_TREAT_WARNINGS_AS_ERRORS`

启用此选项会使所有警告都被当作错误处理。

### Unroll Loops

**设置名称：** `GCC_UNROLL_LOOPS`

展开循环。展开会使代码变大，但可能通过减少所执行的分支数量而使其运行得更快。

### Use Standard System Header Directory Searching

**设置名称：** `GCC_USE_STANDARD_INCLUDE_SEARCHING`

控制是否在标准系统目录中搜索头文件。禁用时，只会搜索你使用 `-I` 选项指定的目录（以及当前文件所在目录，如果适用）。

### Compiler for C/C++/Objective-C

**设置名称：** `GCC_VERSION`

用于 C、C++ 和 Objective-C 的编译器。

### Implicit Conversion to 32 Bit Type

**设置名称：** `GCC_WARN_64_TO_32_BIT_CONVERSION`

当一个值从 64 位类型隐式转换为 32 位类型时发出警告。这是 -Wconversion 提供的警告的一个子集。

### Deprecated Functions

**设置名称：** `GCC_WARN_ABOUT_DEPRECATED_FUNCTIONS`

警告已废弃函数、变量和类型（由 `deprecated` 特性指示）的使用。

### Undefined Use of offsetof Macro

**设置名称：** `GCC_WARN_ABOUT_INVALID_OFFSETOF_MACRO`

取消勾选此设置会抑制将 `offsetof` 宏应用于非 POD 类型时产生的警告。根据 1998 年的 ISO C++ 标准，将 `offsetof` 应用于非 POD 类型是未定义行为。然而，在现有的 C++ 实现中，即使将 `offsetof` 应用于某些非 POD 类型（例如仅因为拥有构造函数而不属于 POD 类型的简单结构体），通常也能得到有意义的结果。此标志适用于那些清楚自己在编写不可移植代码、并有意选择忽略相关警告的用户。

未来版本的 C++ 标准可能会放宽对 `offsetof` 的限制。

### Missing Fields in Structure Initializers

**设置名称：** `GCC_WARN_ABOUT_MISSING_FIELD_INITIALIZERS`

如果一个结构体的初始化器缺少某些字段，发出警告。例如，以下代码会引发这样的警告，因为 `x.h` 被隐式置零：

```
struct s { int f, g, h; };
struct s x = { 3, 4 };
```

此选项不会警告指定初始化器（designated initializer），因此以下修改不会触发警告：

```
struct s { int f, g, h; };
struct s x = { .f = 3, .g = 4 };
```

### Missing Newline At End Of File

**设置名称：** `GCC_WARN_ABOUT_MISSING_NEWLINE`

当源文件不以换行符结尾时发出警告。

### Missing Function Prototypes

**设置名称：** `GCC_WARN_ABOUT_MISSING_PROTOTYPES`

导致发出关于缺失原型的警告。

### Pointer Sign Comparison

**设置名称：** `GCC_WARN_ABOUT_POINTER_SIGNEDNESS`

当通过参数传递的指针或赋给变量的指针符号不同时发出警告。

### Mismatched Return Type

**设置名称：** `GCC_WARN_ABOUT_RETURN_TYPE`

当一个具有明确返回类型（非 `void`）的函数包含没有返回值的 return 语句、或者不包含任何 return 语句时，会发出警告。当一个返回类型为 void 的函数试图返回一个值时，也会发出警告。

### Incomplete Objective-C Protocols

**设置名称：** `GCC_WARN_ALLOW_INCOMPLETE_PROTOCOL`

如果采用某个协议的类没有实现该协议要求的方法，发出警告。仅适用于 Objective-C。

### Check Switch Statements

**设置名称：** `GCC_WARN_CHECK_SWITCH_STATEMENTS`

每当一个 switch 语句的索引为枚举类型、且缺少该枚举中一个或多个具名代码对应的 case 时发出警告。存在 default 标签可以避免此警告。使用此选项时，超出枚举范围的 case 标签也会引发警告。

### Four Character Literals

**设置名称：** `GCC_WARN_FOUR_CHARACTER_CONSTANTS`

警告四字符字面量（例如 macOS 风格的 `OSTypes`：`'APPL'`）。

### Overloaded Virtual Functions

**设置名称：** `GCC_WARN_HIDDEN_VIRTUAL_FUNCTIONS`

当一个函数声明隐藏了基类中的虚函数时发出警告。

例如，在以下示例中，`A` 类版本的 `f()` 在 `B` 中被隐藏了。

```
struct A {
  virtual void f();
};

struct B: public A {
  void f(int);
};
```

因此，以下代码将无法编译。

```
B* b;
b->f();
```

此设置仅适用于 C++ 和 Objective-C++ 源文件。

### Inhibit All Warnings

**设置名称：** `GCC_WARN_INHIBIT_ALL_WARNINGS`

抑制所有警告消息。

### Initializer Not Fully Bracketed

**设置名称：** `GCC_WARN_INITIALIZER_NOT_FULLY_BRACKETED`

如果聚合体或联合体的初始化器没有完全括起来，发出警告。在以下示例中，`a` 的初始化器没有完全括起来，而 `b` 的初始化器完全括起来了。

```
int a[2][2] = { 0, 1, 2, 3 };
int b[2][2] = { { 0, 1 }, { 2, 3 } };
```

### Missing Braces and Parentheses

**设置名称：** `GCC_WARN_MISSING_PARENTHESES`

如果在某些上下文中省略了括号，例如在期望布尔值的上下文中出现赋值、或者运算符嵌套导致优先级产生混淆，发出警告。此外，还会警告可能导致混淆 `else` 分支归属于哪个 `if` 语句的写法。例如：

```
{
  if (a)
    if (b)
      foo ();
  else
    bar ();
}
```

在 C 中，每个 `else` 分支都归属于可能的最内层 `if` 语句，在上面的示例中就是 `if (b)`。这通常不是程序员所期望的结果，正如上面示例中所用的缩进所展示的那样。此构建设置会使 GCC 在存在这种混淆可能性时发出警告。要消除该警告，请在最内层 `if` 语句周围添加显式的花括号，这样 `else` 就不可能归属于外层的 `if`。例如：

```
{
  if (a)
    {
      if (b)
        foo ();
      else
        bar ();
    }
}
```

### Nonvirtual Destructor

**设置名称：** `GCC_WARN_NON_VIRTUAL_DESTRUCTOR`

当一个类声明了非虚析构函数、但该类看起来会被多态使用、因而该析构函数或许应为虚函数时发出警告。仅对 C++ 或 Objective-C++ 源文件有效。

### Pedantic Warnings

**设置名称：** `GCC_WARN_PEDANTIC`

发出严格 ISO C 和 ISO C++ 所要求的所有警告；拒绝所有使用被禁止扩展的程序，以及一些其他不遵循 ISO C 和 ISO C++ 的程序。对于 ISO C，遵循所使用的任何 `-std` 选项指定的 ISO C 标准版本。

### Hidden Local Variables

**设置名称：** `GCC_WARN_SHADOW`

每当一个局部变量遮蔽了另一个局部变量、参数或全局变量，或者遮蔽了某个内建函数时发出警告。

### Sign Comparison

**设置名称：** `GCC_WARN_SIGN_COMPARE`

当有符号值和无符号值之间的比较，在有符号值被转换为无符号值时可能产生不正确的结果时发出警告。

### Strict Selector Matching

**设置名称：** `GCC_WARN_STRICT_SELECTOR_MATCH`

当尝试使用某个选择器（selector）向类型为 `id` 或 `Class` 的接收者发送消息时，如果针对该选择器找到了多个参数和/或返回类型不同的方法，发出警告。禁用此设置时，如果发现的差异仅限于大小和对齐方式相同的类型，编译器会省略此类警告。

### Typecheck Calls to printf/scanf

**设置名称：** `GCC_WARN_TYPECHECK_CALLS_TO_PRINTF`

检查对 `printf` 和 `scanf` 的调用，确保提供的参数具有与指定格式字符串相符的类型，并且格式字符串中指定的转换是合理的。

### Undeclared Selector

**设置名称：** `GCC_WARN_UNDECLARED_SELECTOR`

如果发现某个 `@selector(...)` 表达式引用了一个未声明的选择器，发出警告。如果在该 `@selector(...)` 表达式之前，没有任何方法（无论是显式地在 `@interface` 或 `@protocol` 声明中，还是隐式地在 `@implementation` 部分中）以该名称被声明，则该选择器被视为未声明。此选项总是在发现 `@selector(...)` 表达式后立即执行检查，而 `-Wselector` 只在编译的最后阶段执行检查。这也强制推行了方法和选择器必须先声明后使用的代码风格约定。

### Uninitialized Variables

**设置名称：** `GCC_WARN_UNINITIALIZED_AUTOS`

如果某个变量可能被 `setjmp` 调用破坏、或者某个自动变量在未事先初始化的情况下被使用，发出警告。

编译器可能无法检测到自动变量被初始化的所有情况，也无法检测到所有可能导致使用先于初始化的用法模式。你可以在常规的未初始化值检查和更激进（保守）的检查之间切换，后者能发现更多问题，但检查也严格得多。

### Unknown Pragma

**设置名称：** `GCC_WARN_UNKNOWN_PRAGMAS`

当遇到 GCC 无法理解的 `#pragma` 指令时发出警告。如果使用了此命令行选项，即使是系统头文件中未知的 pragma 也会发出警告。如果警告仅由 `-Wall` 命令行选项启用，则不是这种情况。

### Unused Functions

**设置名称：** `GCC_WARN_UNUSED_FUNCTION`

每当一个静态函数被声明但未定义、或者一个非内联静态函数未被使用时发出警告。

### Unused Labels

**设置名称：** `GCC_WARN_UNUSED_LABEL`

每当一个标签被声明但未被使用时发出警告。

### Unused Parameters

**设置名称：** `GCC_WARN_UNUSED_PARAMETER`

每当一个函数参数除了在声明中出现之外未被使用时发出警告。

### Unused Values

**设置名称：** `GCC_WARN_UNUSED_VALUE`

每当一条语句计算出一个明确未被使用的结果时发出警告。

### Unused Variables

**设置名称：** `GCC_WARN_UNUSED_VARIABLE`

每当一个局部变量或非常量静态变量除了在声明中出现之外未被使用时发出警告。

### Generate Info.plist File

**设置名称：** `GENERATE_INFOPLIST_FILE`

自动生成一个 Info.plist 文件。

### Enable Intermediate Text-Based Stubs Generation

**设置名称：** `GENERATE_INTERMEDIATE_TEXT_BASED_STUBS`

为动态库和框架启用中间态基于文本的桩（Text-Based stub）生成，以便在增量构建中更精确地跟踪链接器依赖关系。

### Force Package Info Generation

**设置名称：** `GENERATE_PKGINFO_FILE`

强制将 `PkgInfo` 文件写入经过打包的产品，即使不需要此文件。

### Perform Single-Object Prelink

**设置名称：** `GENERATE_PRELINK_OBJECT_FILE`

激活此设置会使某个 target 构建出的目标文件使用 `ld -r` 预链接为单个目标文件，然后该目标文件会被链接进最终产品。这有助于在构建静态库之前，强制链接器解析符号并将目标文件链接成单个模块。此外，还可以对预链接应用一组单独的链接标志，从而对（例如）导出符号提供额外的控制。

### Generate Profiling Code

**设置名称：** `GENERATE_PROFILING_CODE`

激活此设置会使编译器和链接器生成性能分析代码。例如，GCC 会生成适合与 `gprof(1)` 一起使用的代码。

### Enable Text-Based Stubs Generation

**设置名称：** `GENERATE_TEXT_BASED_STUBS`

为动态库和框架启用基于文本的桩（Text-Based stub）生成。

### HEADERMAP_INCLUDES_FLAT_ENTRIES_FOR_TARGET_BEING_BUILT

**设置名称：** `HEADERMAP_INCLUDES_FLAT_ENTRIES_FOR_TARGET_BEING_BUILT`

指定头文件映射（header map）是否为正在构建的 target 中的每个头文件包含一个名称/路径条目。

### HEADERMAP_INCLUDES_FRAMEWORK_ENTRIES_FOR_ALL_PRODUCT_TYPES

**设置名称：** `HEADERMAP_INCLUDES_FRAMEWORK_ENTRIES_FOR_ALL_PRODUCT_TYPES`

指定头文件映射是否为正在构建的 target 中的每个头文件包含一个框架名/路径条目，包括那些不构建框架的 target。

### HEADERMAP_INCLUDES_PROJECT_HEADERS

**设置名称：** `HEADERMAP_INCLUDES_PROJECT_HEADERS`

指定头文件映射是否为项目中的每个头文件包含一个名称/路径条目，无论该头文件属于哪个 target。

### Header Search Paths

**设置名称：** `HEADER_SEARCH_PATHS`

这是一个文件夹路径列表，编译 C、Objective-C、C++ 或 Objective-C++ 时，编译器会在其中搜索被包含或导入的头文件。路径之间以空白分隔，因此任何包含空格的路径都需要正确加引号。

### Compiler Mode for CocoaTouch Documents

**设置名称：** `IBC_COCOATOUCH_COMPILER_MODE`

指示编译器应使用哪种编译模式。

### Auto-Activate Custom Fonts

**设置名称：** `IBC_COMPILER_AUTO_ACTIVATE_CUSTOM_FONTS`

指示 XIB 编译器将自定义字体添加到应用程序的 `Info.plist` 中，这会使这些字体在应用程序启动时激活。

### Show Errors

**设置名称：** `IBC_ERRORS`

显示编译 XIB 文件期间遇到的错误。

### Flatten Compiled XIB Files

**设置名称：** `IBC_FLATTEN_NIBS`

如果启用，将 XIB 文件编译为扁平化（非包装器）的 NIB 文件。扁平化之后，生成的 NIB 更加紧凑，但不再能被 Interface Builder 编辑。禁用此选项时，生成的 NIB 文件在 Interface Builder 中仍可编辑。

### Default Module

**设置名称：** `IBC_MODULE`

为未指定具体模块名称而被引用的 Swift 类定义模块名称。

### Show Notices

**设置名称：** `IBC_NOTICES`

显示编译 XIB 文件期间遇到的提示信息。

### Other Interface Builder Compiler Flags

**设置名称：** `IBC_OTHER_FLAGS`

传递给 Interface Builder 编译器的附加标志列表。如果 Xcode 尚未为某个特定的 Interface Builder 编译器标志提供界面，请使用此设置。

### Overriding Plug-In and Framework Directory

**设置名称：** `IBC_OVERRIDING_PLUGINS_AND_FRAMEWORKS_DIR`

指示 Interface Builder 从指定目录加载框架和 Interface Builder 插件。将此值设为 `$(BUILD_DIR)/$(CONFIGURATION)$(EFFECTIVE_PLATFORM_NAME)`，可确保 Interface Builder 从当前构建配置的构建产品目录中加载框架和插件。

### Plug-Ins

**设置名称：** `IBC_PLUGINS`

编译 XIB 文件时要加载的 Interface Builder 插件的路径列表。

### Plug-In Search Paths

**设置名称：** `IBC_PLUGIN_SEARCH_PATHS`

编译 XIB 文件时，用于搜索要加载的 Interface Builder 插件的路径列表。

### Strip NIB Files

**设置名称：** `IBC_STRIP_NIBS`

剥离一个 Interface Builder NIB 以减小其部署体积。生成的 NIB 更加紧凑，但不再能被 Interface Builder 编辑。禁用此选项时，生成的 NIB 文件仍可被 Interface Builder 编辑。

### Show Warnings

**设置名称：** `IBC_WARNINGS`

显示编译 XIB 文件期间遇到的警告。

### Compiler Mode for CocoaTouch Documents

**设置名称：** `IBSC_COCOATOUCH_COMPILER_MODE`

指示编译器应使用哪种编译模式。

### Auto-Activate Custom Fonts

**设置名称：** `IBSC_COMPILER_AUTO_ACTIVATE_CUSTOM_FONTS`

指示 Storyboard 编译器将自定义字体添加到应用程序的 `Info.plist` 中，这会使这些字体在应用程序启动时激活。

### Show Errors

**设置名称：** `IBSC_ERRORS`

显示编译 Storyboard 文件期间遇到的错误。

### Flatten Compiled Storyboard Files

**设置名称：** `IBSC_FLATTEN_NIBS`

将 Storyboard 文件编译为扁平化（非包装器）的 Storyboard 文件。扁平化之后，生成的 Storyboard 更加紧凑，但不再能被 Interface Builder 编辑。禁用此选项时，生成的 Storyboard 文件在 Interface Builder 中仍可编辑。

### Default Module

**设置名称：** `IBSC_MODULE`

为未指定具体模块名称而被引用的 Swift 类定义模块名称。

### Show Notices

**设置名称：** `IBSC_NOTICES`

显示编译 Storyboard 文件期间遇到的提示信息。

### Other Storyboard Compiler Flags

**设置名称：** `IBSC_OTHER_FLAGS`

传递给 Interface Builder 编译器的附加标志列表。如果 Xcode 尚未为某个特定的 Interface Builder 编译器标志提供界面，请使用此设置。

### Strip Storyboardc Files

**设置名称：** `IBSC_STRIP_NIBS`

剥离一个可编辑的 Interface Builder storyboardc 文件以减小其部署体积。生成的 storyboardc 更加紧凑，但不再能被 Interface Builder 编辑。禁用此选项时，生成的 storyboardc 文件仍可被 Interface Builder 编辑。

### Show Warnings

**设置名称：** `IBSC_WARNINGS`

显示编译 Storyboard 文件期间遇到的警告。

### Implicit Dependency Domain

**设置名称：** `IMPLICIT_DEPENDENCY_DOMAIN`

该 target 在其中进行隐式依赖匹配的域。只有当两个 target 处于同一个域中时，才会在它们之间建立隐式依赖关系。

### Included Explicit Target Dependencies

**设置名称：** `INCLUDED_EXPLICIT_TARGET_DEPENDENCIES`

一个模式列表（由 `fnmatch(3)` 定义），指定在确定要构建哪些 target 时应_包含_的显式 target 依赖项的名称。此设置只有在与 `EXCLUDED_EXPLICIT_TARGET_DEPENDENCIES` 结合使用时才有用，可用于定义复杂的过滤条件，以根据其他构建设置决定应构建哪些 target。

### Sub-Directories to Include in Recursive Searches

**设置名称：** `INCLUDED_RECURSIVE_SEARCH_PATH_SUBDIRECTORIES`

这是一个 `fnmatch()` 风格的文件或目录名称模式列表，在执行递归搜索时会被包含。默认情况下此值为空，只有当你想为 `EXCLUDED_RECURSIVE_SEARCH_PATH_SUBDIRECTORIES` 中提供的文件名模式列表提供例外时，才需要自定义此设置。

### Included Source File Names

**设置名称：** `INCLUDED_SOURCE_FILE_NAMES`

一个模式列表（由 `fnmatch(3)` 定义），指定在处理该 target 构建阶段中的文件时应显式_包含_的源文件名称。此设置只有在与 `EXCLUDED_SOURCE_FILE_NAMES` 结合使用时才有用，可用于定义复杂的过滤条件，以根据其他构建设置决定该阶段应构建哪些文件。

### Compress Index Store

**设置名称：** `INDEX_STORE_COMPRESS`

压缩索引存储（index store），减小其磁盘占用大小。

### Index only project files

**设置名称：** `INDEX_STORE_ONLY_PROJECT_FILES`

只为此项目内正在编译的源文件建立索引。不要为系统模块向索引存储输出数据。

### Expand Build Settings in Info.plist File

**设置名称：** `INFOPLIST_EXPAND_BUILD_SETTINGS`

在 `Info.plist` 文件中展开构建设置。

### Info.plist File

**设置名称：** `INFOPLIST_FILE`

相对于项目的路径，指向包含 Bundle 所使用 `Info.plist` 信息的属性列表文件。

构建系统会将你在此文件中指定的值，与它在构建过程中生成的其他值合并。产品类型、目标平台、App 隐私清单（App Privacy manifest）、来自其他构建工具的输入，以及其他内置逻辑都会影响它生成的最终 `Info.plist` 文件的内容。启用 `GENERATE_INFOPLIST_FILE` 时，构建系统还会在合并过程中包含来自构建设置的内容。

有关信息属性列表文件的详情，请参阅 [Information Property List](https://developer.apple.com/documentation/bundleresources/information-property-list)。

### Bundle Display Name

**设置名称：** `INFOPLIST_KEY_CFBundleDisplayName`

启用 `GENERATE_INFOPLIST_FILE` 时，会将 `Info.plist` 文件中 [CFBundleDisplayName](https://developer.apple.com/documentation/bundleresources/information-property-list/cfbundledisplayname) 键的值设为此构建设置的值。

### Complication Principal Class

**设置名称：** `INFOPLIST_KEY_CLKComplicationPrincipalClass`

启用 `GENERATE_INFOPLIST_FILE` 时，会将 `Info.plist` 文件中 [CLKComplicationPrincipalClass](https://developer.apple.com/documentation/bundleresources/information-property-list/clkcomplicationprincipalclass) 键的值设为此构建设置的值。

### Supports Game Controller User Interaction

**设置名称：** `INFOPLIST_KEY_GCSupportsControllerUserInteraction`

启用 `GENERATE_INFOPLIST_FILE` 时，会将 `Info.plist` 文件中 GCSupportsControllerUserInteraction 键的值设为此构建设置的值。

### Supports Game Mode

**设置名称：** `INFOPLIST_KEY_GCSupportsGameMode`

启用 `GENERATE_INFOPLIST_FILE` 时，会将 `Info.plist` 文件中 GCSupportsGameMode 键的值设为此构建设置的值。

### App Uses Non-Exempt Encryption

**设置名称：** `INFOPLIST_KEY_ITSAppUsesNonExemptEncryption`

启用 `GENERATE_INFOPLIST_FILE` 时，会将 `Info.plist` 文件中 [ITSAppUsesNonExemptEncryption](https://developer.apple.com/documentation/bundleresources/information-property-list/itsappusesnonexemptencryption) 键的值设为此构建设置的值。

### App Encryption Export Compliance Code

**设置名称：** `INFOPLIST_KEY_ITSEncryptionExportComplianceCode`

启用 `GENERATE_INFOPLIST_FILE` 时，会将 `Info.plist` 文件中 [ITSEncryptionExportComplianceCode](https://developer.apple.com/documentation/bundleresources/information-property-list/itsencryptionexportcompliancecode) 键的值设为此构建设置的值。

### Application Category

**设置名称：** `INFOPLIST_KEY_LSApplicationCategoryType`

启用 `GENERATE_INFOPLIST_FILE` 时，会将 `Info.plist` 文件中 [LSApplicationCategoryType](https://developer.apple.com/documentation/bundleresources/information-property-list/lsapplicationcategorytype) 键的值设为此构建设置的值。

### Application is Background Only

**设置名称：** `INFOPLIST_KEY_LSBackgroundOnly`

启用 `GENERATE_INFOPLIST_FILE` 时，会将 `Info.plist` 文件中 [LSBackgroundOnly](https://developer.apple.com/documentation/bundleresources/information-property-list/lsbackgroundonly) 键的值设为此构建设置的值。

### Supports Opening Documents in Place

**设置名称：** `INFOPLIST_KEY_LSSupportsOpeningDocumentsInPlace`

启用 `GENERATE_INFOPLIST_FILE` 时，会将 `Info.plist` 文件中 [LSSupportsOpeningDocumentsInPlace](https://developer.apple.com/documentation/bundleresources/information-property-list/lssupportsopeningdocumentsinplace) 键的值设为此构建设置的值。

### Application is Agent (UIElement)

**设置名称：** `INFOPLIST_KEY_LSUIElement`

启用 `GENERATE_INFOPLIST_FILE` 时，会将 `Info.plist` 文件中 [LSUIElement](https://developer.apple.com/documentation/bundleresources/information-property-list/lsuielement) 键的值设为此构建设置的值。

### Metal Capture Enabled

**设置名称：** `INFOPLIST_KEY_MetalCaptureEnabled`

启用 `GENERATE_INFOPLIST_FILE` 时，会将 `Info.plist` 文件中 MetalCaptureEnabled 键的值设为此构建设置的值。

### Privacy - NFC Scan Usage Description

**设置名称：** `INFOPLIST_KEY_NFCReaderUsageDescription`

启用 `GENERATE_INFOPLIST_FILE` 时，会将 `Info.plist` 文件中 [NFCReaderUsageDescription](https://developer.apple.com/documentation/bundleresources/information-property-list/nfcreaderusagedescription) 键的值设为此构建设置的值。

### Privacy - Accessory Tracking Usage Description

**设置名称：** `INFOPLIST_KEY_NSAccessoryTrackingUsageDescription`

启用 `GENERATE_INFOPLIST_FILE` 时，会将 `Info.plist` 文件中 [NSAccessoryTrackingUsageDescription](https://developer.apple.com/documentation/bundleresources/information-property-list/nsaccessorytrackingusagedescription) 键的值设为此构建设置的值。

### Privacy - Other Application Data Usage Description

**设置名称：** `INFOPLIST_KEY_NSAppDataUsageDescription`

启用 `GENERATE_INFOPLIST_FILE` 时，会将 `Info.plist` 文件中 [NSAppDataUsageDescription](https://developer.apple.com/documentation/bundleresources/information-property-list/nsappdatausagedescription) 键的值设为此构建设置的值。

### Privacy - AppleEvents Sending Usage Description

**设置名称：** `INFOPLIST_KEY_NSAppleEventsUsageDescription`

启用 `GENERATE_INFOPLIST_FILE` 时，会将 `Info.plist` 文件中 [NSAppleEventsUsageDescription](https://developer.apple.com/documentation/bundleresources/information-property-list/nsappleeventsusagedescription) 键的值设为此构建设置的值。

### Privacy - Media Library Usage Description

**设置名称：** `INFOPLIST_KEY_NSAppleMusicUsageDescription`

启用 `GENERATE_INFOPLIST_FILE` 时，会将 `Info.plist` 文件中 [NSAppleMusicUsageDescription](https://developer.apple.com/documentation/bundleresources/information-property-list/nsapplemusicusagedescription) 键的值设为此构建设置的值。

### Privacy - Bluetooth Always Usage Description

**设置名称：** `INFOPLIST_KEY_NSBluetoothAlwaysUsageDescription`

启用 `GENERATE_INFOPLIST_FILE` 时，会将 `Info.plist` 文件中 [NSBluetoothAlwaysUsageDescription](https://developer.apple.com/documentation/bundleresources/information-property-list/nsbluetoothalwaysusagedescription) 键的值设为此构建设置的值。

### Privacy - Bluetooth Peripheral Usage Description

**设置名称：** `INFOPLIST_KEY_NSBluetoothPeripheralUsageDescription`

启用 `GENERATE_INFOPLIST_FILE` 时，会将 `Info.plist` 文件中 [NSBluetoothPeripheralUsageDescription](https://developer.apple.com/documentation/bundleresources/information-property-list/nsbluetoothperipheralusagedescription) 键的值设为此构建设置的值。

### Privacy - Bluetooth While In Use Usage Description

**设置名称：** `INFOPLIST_KEY_NSBluetoothWhileInUseUsageDescription`

启用 `GENERATE_INFOPLIST_FILE` 时，会将 `Info.plist` 文件中 NSBluetoothWhileInUseUsageDescription 键的值设为此构建设置的值。

### Privacy - Calendars Full Access Usage Description

**设置名称：** `INFOPLIST_KEY_NSCalendarsFullAccessUsageDescription`

启用 `GENERATE_INFOPLIST_FILE` 时，会将 `Info.plist` 文件中 [NSCalendarsFullAccessUsageDescription](https://developer.apple.com/documentation/bundleresources/information-property-list/nscalendarsfullaccessusagedescription) 键的值设为此构建设置的值。

### Privacy - Calendars Usage Description

**设置名称：** `INFOPLIST_KEY_NSCalendarsUsageDescription`

启用 `GENERATE_INFOPLIST_FILE` 时，会将 `Info.plist` 文件中 [NSCalendarsUsageDescription](https://developer.apple.com/documentation/bundleresources/information-property-list/nscalendarsusagedescription) 键的值设为此构建设置的值。

### Privacy - Calendars Write Only Usage Description

**设置名称：** `INFOPLIST_KEY_NSCalendarsWriteOnlyAccessUsageDescription`

启用 `GENERATE_INFOPLIST_FILE` 时，会将 `Info.plist` 文件中 [NSCalendarsWriteOnlyAccessUsageDescription](https://developer.apple.com/documentation/bundleresources/information-property-list/nscalendarswriteonlyaccessusagedescription) 键的值设为此构建设置的值。

### Privacy - Camera Usage Description

**设置名称：** `INFOPLIST_KEY_NSCameraUsageDescription`

启用 `GENERATE_INFOPLIST_FILE` 时，会将 `Info.plist` 文件中 [NSCameraUsageDescription](https://developer.apple.com/documentation/bundleresources/information-property-list/nscamerausagedescription) 键的值设为此构建设置的值。

### Privacy - Contacts Usage Description

**设置名称：** `INFOPLIST_KEY_NSContactsUsageDescription`

启用 `GENERATE_INFOPLIST_FILE` 时，会将 `Info.plist` 文件中 [NSContactsUsageDescription](https://developer.apple.com/documentation/bundleresources/information-property-list/nscontactsusagedescription) 键的值设为此构建设置的值。

### Privacy - Critical Messaging Usage Description

**设置名称：** `INFOPLIST_KEY_NSCriticalMessagingUsageDescription`

启用 `GENERATE_INFOPLIST_FILE` 时，会将 `Info.plist` 文件中 [NSCriticalMessagingUsageDescription](https://developer.apple.com/documentation/bundleresources/information-property-list/nscriticalmessagingusagedescription) 键的值设为此构建设置的值。

### Privacy - Desktop Folder Usage Description

**设置名称：** `INFOPLIST_KEY_NSDesktopFolderUsageDescription`

启用 `GENERATE_INFOPLIST_FILE` 时，会将 `Info.plist` 文件中 [NSDesktopFolderUsageDescription](https://developer.apple.com/documentation/bundleresources/information-property-list/nsdesktopfolderusagedescription) 键的值设为此构建设置的值。

### Privacy - Documents Folder Usage Description

**设置名称：** `INFOPLIST_KEY_NSDocumentsFolderUsageDescription`

启用 `GENERATE_INFOPLIST_FILE` 时，会将 `Info.plist` 文件中 [NSDocumentsFolderUsageDescription](https://developer.apple.com/documentation/bundleresources/information-property-list/nsdocumentsfolderusagedescription) 键的值设为此构建设置的值。

### Privacy - Downloads Folder Usage Description

**设置名称：** `INFOPLIST_KEY_NSDownloadsFolderUsageDescription`

启用 `GENERATE_INFOPLIST_FILE` 时，会将 `Info.plist` 文件中 [NSDownloadsFolderUsageDescription](https://developer.apple.com/documentation/bundleresources/information-property-list/nsdownloadsfolderusagedescription) 键的值设为此构建设置的值。

### Privacy - Face ID Usage Description

**设置名称：** `INFOPLIST_KEY_NSFaceIDUsageDescription`

启用 `GENERATE_INFOPLIST_FILE` 时，会将 `Info.plist` 文件中 [NSFaceIDUsageDescription](https://developer.apple.com/documentation/bundleresources/information-property-list/nsfaceidusagedescription) 键的值设为此构建设置的值。

### Privacy - Fall Detection Usage Description

**设置名称：** `INFOPLIST_KEY_NSFallDetectionUsageDescription`

启用 `GENERATE_INFOPLIST_FILE` 时，会将 `Info.plist` 文件中 [NSFallDetectionUsageDescription](https://developer.apple.com/documentation/bundleresources/information-property-list/nsfalldetectionusagedescription) 键的值设为此构建设置的值。

### Privacy - Access to a File Provide Domain Usage Description

**设置名称：** `INFOPLIST_KEY_NSFileProviderDomainUsageDescription`

启用 `GENERATE_INFOPLIST_FILE` 时，会将 `Info.plist` 文件中 [NSFileProviderDomainUsageDescription](https://developer.apple.com/documentation/bundleresources/information-property-list/nsfileproviderdomainusagedescription) 键的值设为此构建设置的值。

### Privacy - File Provider Presence Usage Description

**设置名称：** `INFOPLIST_KEY_NSFileProviderPresenceUsageDescription`

启用 `GENERATE_INFOPLIST_FILE` 时，会将 `Info.plist` 文件中 NSFileProviderPresenceUsageDescription 键的值设为此构建设置的值。

### Privacy - Financial Data Usage Description

**设置名称：** `INFOPLIST_KEY_NSFinancialDataUsageDescription`

启用 `GENERATE_INFOPLIST_FILE` 时，会将 `Info.plist` 文件中 [NSFinancialDataUsageDescription](https://developer.apple.com/documentation/bundleresources/information-property-list/nsfinancialdatausagedescription) 键的值设为此构建设置的值。

### Privacy - Focus Status Usage Description

**设置名称：** `INFOPLIST_KEY_NSFocusStatusUsageDescription`

启用 `GENERATE_INFOPLIST_FILE` 时，会将 `Info.plist` 文件中 NSFocusStatusUsageDescription 键的值设为此构建设置的值。

### Privacy - GameKit Friend List Usage Description

**设置名称：** `INFOPLIST_KEY_NSGKFriendListUsageDescription`

启用 `GENERATE_INFOPLIST_FILE` 时，会将 `Info.plist` 文件中 [NSGKFriendListUsageDescription](https://developer.apple.com/documentation/bundleresources/information-property-list/nsgkfriendlistusagedescription) 键的值设为此构建设置的值。

### Privacy - Hands Tracking Usage Description

**设置名称：** `INFOPLIST_KEY_NSHandsTrackingUsageDescription`

启用 `GENERATE_INFOPLIST_FILE` 时，会将 `Info.plist` 文件中 [NSHandsTrackingUsageDescription](https://developer.apple.com/documentation/bundleresources/information-property-list/nshandstrackingusagedescription) 键的值设为此构建设置的值。

### Privacy - Health Records Usage Description

**设置名称：** `INFOPLIST_KEY_NSHealthClinicalHealthRecordsShareUsageDescription`

启用 `GENERATE_INFOPLIST_FILE` 时，会将 `Info.plist` 文件中 [NSHealthClinicalHealthRecordsShareUsageDescription](https://developer.apple.com/documentation/bundleresources/information-property-list/nshealthclinicalhealthrecordsshareusagedescription) 键的值设为此构建设置的值。

### Privacy - Health Share Usage Description

**设置名称：** `INFOPLIST_KEY_NSHealthShareUsageDescription`

启用 `GENERATE_INFOPLIST_FILE` 时，会将 `Info.plist` 文件中 [NSHealthShareUsageDescription](https://developer.apple.com/documentation/bundleresources/information-property-list/nshealthshareusagedescription) 键的值设为此构建设置的值。

### Privacy - Health Update Usage Description

**设置名称：** `INFOPLIST_KEY_NSHealthUpdateUsageDescription`

启用 `GENERATE_INFOPLIST_FILE` 时，会将 `Info.plist` 文件中 [NSHealthUpdateUsageDescription](https://developer.apple.com/documentation/bundleresources/information-property-list/nshealthupdateusagedescription) 键的值设为此构建设置的值。

### Privacy - HomeKit Usage Description

**设置名称：** `INFOPLIST_KEY_NSHomeKitUsageDescription`

启用 `GENERATE_INFOPLIST_FILE` 时，会将 `Info.plist` 文件中 [NSHomeKitUsageDescription](https://developer.apple.com/documentation/bundleresources/information-property-list/nshomekitusagedescription) 键的值设为此构建设置的值。

### Copyright (Human-Readable)

**设置名称：** `INFOPLIST_KEY_NSHumanReadableCopyright`

启用 `GENERATE_INFOPLIST_FILE` 时，会将 `Info.plist` 文件中 [NSHumanReadableCopyright](https://developer.apple.com/documentation/bundleresources/information-property-list/nshumanreadablecopyright) 键的值设为此构建设置的值。

### Privacy - Identity Usage Description

**设置名称：** `INFOPLIST_KEY_NSIdentityUsageDescription`

启用 `GENERATE_INFOPLIST_FILE` 时，会将 `Info.plist` 文件中 [NSIdentityUsageDescription](https://developer.apple.com/documentation/bundleresources/information-property-list/nsidentityusagedescription) 键的值设为此构建设置的值。

### Privacy - Local Network Usage Description

**设置名称：** `INFOPLIST_KEY_NSLocalNetworkUsageDescription`

启用 `GENERATE_INFOPLIST_FILE` 时，会将 `Info.plist` 文件中 [NSLocalNetworkUsageDescription](https://developer.apple.com/documentation/bundleresources/information-property-list/nslocalnetworkusagedescription) 键的值设为此构建设置的值。

### Privacy - Location Always and When In Use Usage Description

**设置名称：** `INFOPLIST_KEY_NSLocationAlwaysAndWhenInUseUsageDescription`

启用 `GENERATE_INFOPLIST_FILE` 时，会将 `Info.plist` 文件中 [NSLocationAlwaysAndWhenInUseUsageDescription](https://developer.apple.com/documentation/bundleresources/information-property-list/nslocationalwaysandwheninuseusagedescription) 键的值设为此构建设置的值。

### Privacy - Location Always Usage Description

**设置名称：** `INFOPLIST_KEY_NSLocationAlwaysUsageDescription`

启用 `GENERATE_INFOPLIST_FILE` 时，会将 `Info.plist` 文件中 [NSLocationAlwaysUsageDescription](https://developer.apple.com/documentation/bundleresources/information-property-list/nslocationalwaysusagedescription) 键的值设为此构建设置的值。

### Privacy - Location Temporary Usage Description Dictionary

**设置名称：** `INFOPLIST_KEY_NSLocationTemporaryUsageDescriptionDictionary`

启用 `GENERATE_INFOPLIST_FILE` 时，会将 `Info.plist` 文件中 [NSLocationTemporaryUsageDescriptionDictionary](https://developer.apple.com/documentation/bundleresources/information-property-list/nslocationtemporaryusagedescriptiondictionary) 键的值设为此构建设置的值。

### Privacy - Location Usage Description

**设置名称：** `INFOPLIST_KEY_NSLocationUsageDescription`

启用 `GENERATE_INFOPLIST_FILE` 时，会将 `Info.plist` 文件中 [NSLocationUsageDescription](https://developer.apple.com/documentation/bundleresources/information-property-list/nslocationusagedescription) 键的值设为此构建设置的值。

### Privacy - Location When In Use Usage Description

**设置名称：** `INFOPLIST_KEY_NSLocationWhenInUseUsageDescription`

启用 `GENERATE_INFOPLIST_FILE` 时，会将 `Info.plist` 文件中 [NSLocationWhenInUseUsageDescription](https://developer.apple.com/documentation/bundleresources/information-property-list/nslocationwheninuseusagedescription) 键的值设为此构建设置的值。

### Privacy - Main Camera Usage Description

**设置名称：** `INFOPLIST_KEY_NSMainCameraUsageDescription`

启用 `GENERATE_INFOPLIST_FILE` 时，会将 `Info.plist` 文件中 [NSMainCameraUsageDescription](https://developer.apple.com/documentation/bundleresources/information-property-list/nsmaincamerausagedescription) 键的值设为此构建设置的值。

### Main Nib File Base Name

**设置名称：** `INFOPLIST_KEY_NSMainNibFile`

启用 `GENERATE_INFOPLIST_FILE` 时，会将 `Info.plist` 文件中 [NSMainNibFile](https://developer.apple.com/documentation/bundleresources/information-property-list/nsmainnibfile) 键的值设为此构建设置的值。

### AppKit Main Storyboard File Base Name

**设置名称：** `INFOPLIST_KEY_NSMainStoryboardFile`

启用 `GENERATE_INFOPLIST_FILE` 时，会将 `Info.plist` 文件中 [NSMainStoryboardFile](https://developer.apple.com/documentation/bundleresources/information-property-list/nsmainstoryboardfile) 键的值设为此构建设置的值。

### Privacy - Microphone Usage Description

**设置名称：** `INFOPLIST_KEY_NSMicrophoneUsageDescription`

启用 `GENERATE_INFOPLIST_FILE` 时，会将 `Info.plist` 文件中 [NSMicrophoneUsageDescription](https://developer.apple.com/documentation/bundleresources/information-property-list/nsmicrophoneusagedescription) 键的值设为此构建设置的值。

### Privacy - Motion Usage Description

**设置名称：** `INFOPLIST_KEY_NSMotionUsageDescription`

启用 `GENERATE_INFOPLIST_FILE` 时，会将 `Info.plist` 文件中 [NSMotionUsageDescription](https://developer.apple.com/documentation/bundleresources/information-property-list/nsmotionusagedescription) 键的值设为此构建设置的值。

### Privacy - Nearby Interaction Allow Once Usage Description

**设置名称：** `INFOPLIST_KEY_NSNearbyInteractionAllowOnceUsageDescription`

启用 `GENERATE_INFOPLIST_FILE` 时，会将 `Info.plist` 文件中 [NSNearbyInteractionAllowOnceUsageDescription](https://developer.apple.com/documentation/bundleresources/information-property-list/nsnearbyinteractionallowonceusagedescription) 键的值设为此构建设置的值。

### Privacy - Nearby Interaction Usage Description

**设置名称：** `INFOPLIST_KEY_NSNearbyInteractionUsageDescription`

启用 `GENERATE_INFOPLIST_FILE` 时，会将 `Info.plist` 文件中 [NSNearbyInteractionUsageDescription](https://developer.apple.com/documentation/bundleresources/information-property-list/nsnearbyinteractionusagedescription) 键的值设为此构建设置的值。

### Privacy - Network Volumes Usage Description

**设置名称：** `INFOPLIST_KEY_NSNetworkVolumesUsageDescription`

启用 `GENERATE_INFOPLIST_FILE` 时，会将 `Info.plist` 文件中 [NSNetworkVolumesUsageDescription](https://developer.apple.com/documentation/bundleresources/information-property-list/nsnetworkvolumesusagedescription) 键的值设为此构建设置的值。

### Privacy - Photo Library Additions Usage Description

**设置名称：** `INFOPLIST_KEY_NSPhotoLibraryAddUsageDescription`

启用 `GENERATE_INFOPLIST_FILE` 时，会将 `Info.plist` 文件中 [NSPhotoLibraryAddUsageDescription](https://developer.apple.com/documentation/bundleresources/information-property-list/nsphotolibraryaddusagedescription) 键的值设为此构建设置的值。

### Privacy - Photo Library Usage Description

**设置名称：** `INFOPLIST_KEY_NSPhotoLibraryUsageDescription`

启用 `GENERATE_INFOPLIST_FILE` 时，会将 `Info.plist` 文件中 [NSPhotoLibraryUsageDescription](https://developer.apple.com/documentation/bundleresources/information-property-list/nsphotolibraryusagedescription) 键的值设为此构建设置的值。

### Principal Class

**设置名称：** `INFOPLIST_KEY_NSPrincipalClass`

启用 `GENERATE_INFOPLIST_FILE` 时，会将 `Info.plist` 文件中 [NSPrincipalClass](https://developer.apple.com/documentation/bundleresources/information-property-list/nsprincipalclass) 键的值设为此构建设置的值。

### Privacy - Reminders Full Access Usage Description

**设置名称：** `INFOPLIST_KEY_NSRemindersFullAccessUsageDescription`

启用 `GENERATE_INFOPLIST_FILE` 时，会将 `Info.plist` 文件中 [NSRemindersFullAccessUsageDescription](https://developer.apple.com/documentation/bundleresources/information-property-list/nsremindersfullaccessusagedescription) 键的值设为此构建设置的值。

### Privacy - Reminders Usage Description

**设置名称：** `INFOPLIST_KEY_NSRemindersUsageDescription`

启用 `GENERATE_INFOPLIST_FILE` 时，会将 `Info.plist` 文件中 [NSRemindersUsageDescription](https://developer.apple.com/documentation/bundleresources/information-property-list/nsremindersusagedescription) 键的值设为此构建设置的值。

### Privacy - Removable Volumes Usage Description

**设置名称：** `INFOPLIST_KEY_NSRemovableVolumesUsageDescription`

启用 `GENERATE_INFOPLIST_FILE` 时，会将 `Info.plist` 文件中 [NSRemovableVolumesUsageDescription](https://developer.apple.com/documentation/bundleresources/information-property-list/nsremovablevolumesusagedescription) 键的值设为此构建设置的值。

### Privacy - SensorKit Privacy Policy URL

**设置名称：** `INFOPLIST_KEY_NSSensorKitPrivacyPolicyURL`

启用 `GENERATE_INFOPLIST_FILE` 时，会将 `Info.plist` 文件中 [NSSensorKitPrivacyPolicyURL](https://developer.apple.com/documentation/bundleresources/information-property-list/nssensorkitprivacypolicyurl) 键的值设为此构建设置的值。

### Privacy - SensorKit Usage Description

**设置名称：** `INFOPLIST_KEY_NSSensorKitUsageDescription`

启用 `GENERATE_INFOPLIST_FILE` 时，会将 `Info.plist` 文件中 [NSSensorKitUsageDescription](https://developer.apple.com/documentation/bundleresources/information-property-list/nssensorkitusagedescription) 键的值设为此构建设置的值。

### Privacy - Siri Usage Description

**设置名称：** `INFOPLIST_KEY_NSSiriUsageDescription`

启用 `GENERATE_INFOPLIST_FILE` 时，会将 `Info.plist` 文件中 [NSSiriUsageDescription](https://developer.apple.com/documentation/bundleresources/information-property-list/nssiriusagedescription) 键的值设为此构建设置的值。

### Privacy - Speech Recognition Usage Description

**设置名称：** `INFOPLIST_KEY_NSSpeechRecognitionUsageDescription`

启用 `GENERATE_INFOPLIST_FILE` 时，会将 `Info.plist` 文件中 [NSSpeechRecognitionUsageDescription](https://developer.apple.com/documentation/bundleresources/information-property-list/nsspeechrecognitionusagedescription) 键的值设为此构建设置的值。

### Sticker Sharing Level

**设置名称：** `INFOPLIST_KEY_NSStickerSharingLevel`

启用 `GENERATE_INFOPLIST_FILE` 时，会将 `Info.plist` 文件中 NSStickerSharingLevel 键的值设为此构建设置的值。

### Supports Live Activities

**设置名称：** `INFOPLIST_KEY_NSSupportsLiveActivities`

启用 `GENERATE_INFOPLIST_FILE` 时，会将 `Info.plist` 文件中 [NSSupportsLiveActivities](https://developer.apple.com/documentation/bundleresources/information-property-list/nssupportsliveactivities) 键的值设为此构建设置的值。

### Supports Frequent Updates of Live Activities

**设置名称：** `INFOPLIST_KEY_NSSupportsLiveActivitiesFrequentUpdates`

启用 `GENERATE_INFOPLIST_FILE` 时，会将 `Info.plist` 文件中 [NSSupportsLiveActivitiesFrequentUpdates](https://developer.apple.com/documentation/bundleresources/information-property-list/nssupportsliveactivitiesfrequentupdates) 键的值设为此构建设置的值。

### Privacy - System Administration Usage Description

**设置名称：** `INFOPLIST_KEY_NSSystemAdministrationUsageDescription`

启用 `GENERATE_INFOPLIST_FILE` 时，会将 `Info.plist` 文件中 [NSSystemAdministrationUsageDescription](https://developer.apple.com/documentation/bundleresources/information-property-list/nssystemadministrationusagedescription) 键的值设为此构建设置的值。

### Privacy - System Extension Usage Description

**设置名称：** `INFOPLIST_KEY_NSSystemExtensionUsageDescription`

启用 `GENERATE_INFOPLIST_FILE` 时，会将 `Info.plist` 文件中 NSSystemExtensionUsageDescription 键的值设为此构建设置的值。

### Privacy - Tracking Usage Description

**设置名称：** `INFOPLIST_KEY_NSUserTrackingUsageDescription`

启用 `GENERATE_INFOPLIST_FILE` 时，会将 `Info.plist` 文件中 [NSUserTrackingUsageDescription](https://developer.apple.com/documentation/bundleresources/information-property-list/nsusertrackingusagedescription) 键的值设为此构建设置的值。

### Privacy - TV Provider Usage Description

**设置名称：** `INFOPLIST_KEY_NSVideoSubscriberAccountUsageDescription`

启用 `GENERATE_INFOPLIST_FILE` 时，会将 `Info.plist` 文件中 [NSVideoSubscriberAccountUsageDescription](https://developer.apple.com/documentation/bundleresources/information-property-list/nsvideosubscriberaccountusagedescription) 键的值设为此构建设置的值。

### Privacy - VoIP Usage Description

**设置名称：** `INFOPLIST_KEY_NSVoIPUsageDescription`

启用 `GENERATE_INFOPLIST_FILE` 时，会将 `Info.plist` 文件中 NSVoIPUsageDescription 键的值设为此构建设置的值。

### Privacy - World Sensing Usage Description

**设置名称：** `INFOPLIST_KEY_NSWorldSensingUsageDescription`

启用 `GENERATE_INFOPLIST_FILE` 时，会将 `Info.plist` 文件中 [NSWorldSensingUsageDescription](https://developer.apple.com/documentation/bundleresources/information-property-list/nsworldsensingusagedescription) 键的值设为此构建设置的值。

### Privacy - Driver Extension Usage Description

**设置名称：** `INFOPLIST_KEY_OSBundleUsageDescription`

启用 `GENERATE_INFOPLIST_FILE` 时，会将 `Info.plist` 文件中 OSBundleUsageDescription 键的值设为此构建设置的值。

### Application Scene Manifest (Generation)

**设置名称：** `INFOPLIST_KEY_UIApplicationSceneManifest_Generation`

启用 `GENERATE_INFOPLIST_FILE` 时，会将 Info.plist 文件中 [UIApplicationSceneManifest](https://developer.apple.com/documentation/bundleresources/information-property-list/uiapplicationscenemanifest) 键的值设为适用于多窗口应用程序的一个条目。

### Supports Indirect Events

**设置名称：** `INFOPLIST_KEY_UIApplicationSupportsIndirectInputEvents`

启用 `GENERATE_INFOPLIST_FILE` 时，会将 `Info.plist` 文件中 [UIApplicationSupportsIndirectInputEvents](https://developer.apple.com/documentation/bundleresources/information-property-list/uiapplicationsupportsindirectinputevents) 键的值设为此构建设置的值。

### Launch Screen (Generation)

**设置名称：** `INFOPLIST_KEY_UILaunchScreen_Generation`

启用 `GENERATE_INFOPLIST_FILE` 时，会将 Info.plist 文件中 [UILaunchScreen](https://developer.apple.com/documentation/bundleresources/information-property-list/uilaunchscreen) 键的值设为一个空字典。

### Launch Screen Interface File Base Name

**设置名称：** `INFOPLIST_KEY_UILaunchStoryboardName`

启用 `GENERATE_INFOPLIST_FILE` 时，会将 `Info.plist` 文件中 [UILaunchStoryboardName](https://developer.apple.com/documentation/bundleresources/information-property-list/uilaunchstoryboardname) 键的值设为此构建设置的值。

### UIKit Main Storyboard File Base Name

**设置名称：** `INFOPLIST_KEY_UIMainStoryboardFile`

启用 `GENERATE_INFOPLIST_FILE` 时，会将 `Info.plist` 文件中 [UIMainStoryboardFile](https://developer.apple.com/documentation/bundleresources/information-property-list/uimainstoryboardfile) 键的值设为此构建设置的值。

### Required Device Capabilities

**设置名称：** `INFOPLIST_KEY_UIRequiredDeviceCapabilities`

启用 `GENERATE_INFOPLIST_FILE` 时，会将 `Info.plist` 文件中 [UIRequiredDeviceCapabilities](https://developer.apple.com/documentation/bundleresources/information-property-list/uirequireddevicecapabilities) 键的值设为此构建设置的值。

### Requires Full Screen

**设置名称：** `INFOPLIST_KEY_UIRequiresFullScreen`

启用 `GENERATE_INFOPLIST_FILE` 时，会将 `Info.plist` 文件中 [UIRequiresFullScreen](https://developer.apple.com/documentation/bundleresources/information-property-list/uirequiresfullscreen) 键的值设为此构建设置的值。

### Status Bar Initially Hidden

**设置名称：** `INFOPLIST_KEY_UIStatusBarHidden`

启用 `GENERATE_INFOPLIST_FILE` 时，会将 `Info.plist` 文件中 [UIStatusBarHidden](https://developer.apple.com/documentation/bundleresources/information-property-list/uistatusbarhidden) 键的值设为此构建设置的值。

### Status Bar Style

**设置名称：** `INFOPLIST_KEY_UIStatusBarStyle`

启用 `GENERATE_INFOPLIST_FILE` 时，会将 `Info.plist` 文件中 [UIStatusBarStyle](https://developer.apple.com/documentation/bundleresources/information-property-list/uistatusbarstyle) 键的值设为此构建设置的值。

### Supported Interface Orientations

**设置名称：** `INFOPLIST_KEY_UISupportedInterfaceOrientations`

启用 `GENERATE_INFOPLIST_FILE` 时，会将 `Info.plist` 文件中 [UISupportedInterfaceOrientations](https://developer.apple.com/documentation/bundleresources/information-property-list/uisupportedinterfaceorientations) 键的值设为此构建设置的值。

### Supported Interface Orientations (iPad)

**设置名称：** `INFOPLIST_KEY_UISupportedInterfaceOrientations_iPad`

启用 `GENERATE_INFOPLIST_FILE` 时，会将 `Info.plist` 文件中 [UISupportedInterfaceOrientations~iPad](https://developer.apple.com/documentation/bundleresources/information-property-list/uisupportedinterfaceorientations) 键的值设为此构建设置的值。

### Supported Interface Orientations (iPhone)

**设置名称：** `INFOPLIST_KEY_UISupportedInterfaceOrientations_iPhone`

启用 `GENERATE_INFOPLIST_FILE` 时，会将 `Info.plist` 文件中 [UISupportedInterfaceOrientations~iPhone](https://developer.apple.com/documentation/bundleresources/information-property-list/uisupportedinterfaceorientations) 键的值设为此构建设置的值。

### Supports Document Browser

**设置名称：** `INFOPLIST_KEY_UISupportsDocumentBrowser`

启用 `GENERATE_INFOPLIST_FILE` 时，会将 `Info.plist` 文件中 [UISupportsDocumentBrowser](https://developer.apple.com/documentation/bundleresources/information-property-list/uisupportsdocumentbrowser) 键的值设为此构建设置的值。

### User Interface Style

**设置名称：** `INFOPLIST_KEY_UIUserInterfaceStyle`

启用 `GENERATE_INFOPLIST_FILE` 时，会将 `Info.plist` 文件中 [UIUserInterfaceStyle](https://developer.apple.com/documentation/bundleresources/information-property-list/uiuserinterfacestyle) 键的值设为此构建设置的值。

### WatchKit Companion App Bundle Identifier

**设置名称：** `INFOPLIST_KEY_WKCompanionAppBundleIdentifier`

启用 `GENERATE_INFOPLIST_FILE` 时，会将 `Info.plist` 文件中 [WKCompanionAppBundleIdentifier](https://developer.apple.com/documentation/bundleresources/information-property-list/wkcompanionappbundleidentifier) 键的值设为此构建设置的值。

### WatchKit Extension Delegate Class Name

**设置名称：** `INFOPLIST_KEY_WKExtensionDelegateClassName`

启用 `GENERATE_INFOPLIST_FILE` 时，会将 `Info.plist` 文件中 [WKExtensionDelegateClassName](https://developer.apple.com/documentation/bundleresources/information-property-list/wkextensiondelegateclassname) 键的值设为此构建设置的值。

### App Can Run Independently of Companion iPhone App

**设置名称：** `INFOPLIST_KEY_WKRunsIndependentlyOfCompanionApp`

启用 `GENERATE_INFOPLIST_FILE` 时，会将 `Info.plist` 文件中 [WKRunsIndependentlyOfCompanionApp](https://developer.apple.com/documentation/bundleresources/information-property-list/wkrunsindependentlyofcompanionapp) 键的值设为此构建设置的值。

### Supports Launch for Live Activity Attribute Types

**设置名称：** `INFOPLIST_KEY_WKSupportsLiveActivityLaunchAttributeTypes`

启用 `GENERATE_INFOPLIST_FILE` 时，会将 `Info.plist` 文件中 WKSupportsLiveActivityLaunchAttributeTypes 键的值设为此构建设置的值。

### App is Available Only on Apple Watch

**设置名称：** `INFOPLIST_KEY_WKWatchOnly`

启用 `GENERATE_INFOPLIST_FILE` 时，会将 `Info.plist` 文件中 [WKWatchOnly](https://developer.apple.com/documentation/bundleresources/information-property-list/wkwatchonly) 键的值设为此构建设置的值。

### Info.plist Other Preprocessor Flags

**设置名称：** `INFOPLIST_OTHER_PREPROCESSOR_FLAGS`

预处理 `Info.plist` 文件时，传递给 C 预处理器的其他标志。

### Info.plist Output Encoding

**设置名称：** `INFOPLIST_OUTPUT_FORMAT`

指定输出的 `Info.plist` 的输出编码。输出编码可以是 `binary` 或 `XML`。默认情况下，输出编码与输入保持一致。

### INFOPLIST_PATH

**设置名称：** `INFOPLIST_PATH`

指定该 Bundle 信息属性列表文件的路径。

### Info.plist Preprocessor Prefix File

**设置名称：** `INFOPLIST_PREFIX_HEADER`

预处理 `Info.plist` 文件时隐式包含给定的文件。给出的路径应为相对于项目的路径，或者是绝对路径。

### Preprocess Info.plist File

**设置名称：** `INFOPLIST_PREPROCESS`

使用 C 预处理器预处理 `Info.plist` 文件。

### Info.plist Preprocessor Definitions

**设置名称：** `INFOPLIST_PREPROCESSOR_DEFINITIONS`

形如 `foo` 或 `foo=bar` 的预处理器宏的空格分隔列表。这些宏会在预处理 `Info.plist` 文件时使用。

### INFOSTRINGS_PATH

**设置名称：** `INFOSTRINGS_PATH`

指定包含该 Bundle 本地化字符串文件的文件。

### Initialization Routine

**设置名称：** `INIT_ROUTINE`

这是用于初始化的例程名称。

### Enable Text-Based Stubs Inlining

**设置名称：** `INLINE_PRIVATE_FRAMEWORKS`

为基于文本的桩（Text-Based stub）启用私有框架内联。

### Perform Copy Files Phases During `installhdrs`

**设置名称：** `INSTALLHDRS_COPY_PHASE`

指定在 `installhdr` 构建中是否执行该 target 的 Copy Files 构建阶段。

### Perform Shell Script Phases During `installhdrs`

**设置名称：** `INSTALLHDRS_SCRIPT_PHASE`

指定在 `installhdr` 构建中是否执行该 target 的 Run Script 构建阶段。有关 `installhdr` 构建的详情，请参阅 `ACTION`。

### INSTALL_DIR

**设置名称：** `INSTALL_DIR`

标识开发者文件系统中放置_已安装_产品的目录。

### Install Group

**设置名称：** `INSTALL_GROUP`

已安装产品的组名或 `gid`。

### Install Permissions

**设置名称：** `INSTALL_MODE_FLAG`

用于已安装产品文件的权限。

### Install Owner

**设置名称：** `INSTALL_OWNER`

已安装产品的属主名或 `uid`。

### Installation Directory

**设置名称：** `INSTALL_PATH`

安装构建产品所使用的目录。此路径前面会加上 `DSTROOT`。

### Intent Class Generation Language

**设置名称：** `INTENTS_CODEGEN_LANGUAGE`

用于生成的 Intent 类的源代码语言。默认情况下，“Automatic”会分析你的项目以确定正确的语言。调整此设置可显式选择“Swift”或“Objective-C”。

### Building for Mac Catalyst

**设置名称：** `IS_MACCATALYST`

指示该 target 是否正在为 Mac Catalyst 构建。此构建设置旨在用于 shell 脚本和构建设置组合，应视为只读。

### Preserve Private External Symbols

**设置名称：** `KEEP_PRIVATE_EXTERNS`

激活此设置会保留私有外部符号，而不是将它们转换为静态符号。执行单目标文件预链接（single-object prelink）时也会遵循此设置。

### Launch Constraint Parent Process Plist

**设置名称：** `LAUNCH_CONSTRAINT_PARENT`

一个 plist 表示形式的路径，该 plist 表示一个需求字典（Requirements Dictionary），指示对此二进制文件父进程所需的约束。

### Launch Constraint Responsible Process Plist

**设置名称：** `LAUNCH_CONSTRAINT_RESPONSIBLE`

一个 plist 表示形式的路径，该 plist 表示一个需求字典，指示对此二进制文件的责任进程（responsible process）所需的约束。

### Launch Constraint Process Plist

**设置名称：** `LAUNCH_CONSTRAINT_SELF`

一个 plist 表示形式的路径，该 plist 表示一个需求字典，指示对此二进制文件本身所需的约束。

### Client Name

**设置名称：** `LD_CLIENT_NAME`

此设置在链接可执行文件时，通过 `-client_name` 传递该值。

### Path to Linker Dependency Info File

**设置名称：** `LD_DEPENDENCY_INFO_FILE`

此设置定义了链接器应输出其所使用的输入文件及生成文件相关信息的路径。Xcode 使用此信息进行依赖关系跟踪。将此设置的值设为空会禁止将此选项传递给链接器。

### Dynamic Library Allowable Clients

**设置名称：** `LD_DYLIB_ALLOWABLE_CLIENTS`

此设置通过为每个提供的值向链接器传递 `-allowable_client`，来限制允许链接某个 dylib 的客户端。

### Dynamic Library Install Name

**设置名称：** `LD_DYLIB_INSTALL_NAME`

在动态库中设置一个内部“安装路径”（`LC_ID_DYLIB`）。任何链接该库的客户端都会记录该路径，作为 `dyld` 应如何定位此库的方式。如果未指定此选项，则会使用 `-o` 路径。构建动态库以外的任何产品时会忽略此设置。请参阅 [Dynamic Library Programming Topics](https://developer.apple.com/library/content/documentation/DeveloperTools/Conceptual/DynamicLibraries/000-Introduction/Introduction.html)。

### Dynamic Linker Environment

**设置名称：** `LD_ENVIRONMENT`

此设置允许将 `key=value` 形式的 `dyld` 环境变量对，作为 `LC_DYLD_ENVIRONMENT` 加载命令嵌入生成的可执行文件中，以便在平台及其安全环境允许的情况下，补充该可执行文件启动时所处的环境。

### Export Symbols

**设置名称：** `LD_EXPORT_SYMBOLS`

从二进制文件中导出符号。对于没有 API 或插件、因而不需要任何符号导出的二进制文件，禁用此设置会很有用。[-no_exported_symbols]

### Write Link Map File

**设置名称：** `LD_GENERATE_MAP_FILE`

激活此设置会使链接器将一个映射文件写入磁盘，其中详细列出了输出映像中的所有符号及其地址。该映射文件的路径由 `LD_MAP_FILE_PATH` 设置定义。

### Path to Link Map File

**设置名称：** `LD_MAP_FILE_PATH`

此设置定义了在激活 `LD_GENERATE_MAP_FILE` 设置时，链接器写入的映射文件的路径。默认情况下，会为每种架构和构建变体分别写入一个文件，这些文件会生成在正在链接其产品的 target 的 Intermediates 目录中。

### Generate Position-Dependent Executable

**设置名称：** `LD_NO_PIE`

激活此设置会阻止 Xcode 构建位置无关（PIE）的主可执行文件。当针对 macOS 10.7 或更高版本时，PIE 是主可执行文件的默认设置，因此激活此设置会改变这一行为。当针对 OS X 10.6 或更早版本、或为 i386 构建时，PIE 不是默认设置，因此激活此设置不会产生任何效果。

你无法从使用 `-mdynamic-no-pic` 编译的 `.o` 文件创建 PIE。使用 PIE 意味着代码生成不那么优化，但地址随机化增加了一定的安全性。

### Quote Linker Arguments

**设置名称：** `LD_QUOTE_LINKER_ARGUMENTS_FOR_COMPILER_DRIVER`

此设置控制是否应使用 `-Xlinker` 对传给链接器的参数加引号。默认情况下，Xcode 通过调用用于构建该 target 中源文件的编译器驱动程序来调用链接器，传递 `-Xlinker` 加引号会使编译器驱动程序将这些参数原样传递给链接器（而不是尝试在驱动程序内部对它们求值）。此设置默认启用。禁用它会使 Xcode 不使用 `-Xlinker` 向链接器传递参数。如果该 target 已指示 Xcode 使用替代链接器（例如通过将 `LD` 设置为另一个链接器的路径），而该替代链接器不识别 `-Xlinker`，禁用此设置会很有用。

### Runpath Search Paths

**设置名称：** `LD_RUNPATH_SEARCH_PATHS`

这是一个路径列表，会被添加到正在创建的映像的 `runpath` 搜索路径列表中。在运行时，`dyld` 在搜索加载路径以 `@rpath/` 开头的 dylib 时会使用 `runpath`。请参阅 [Dynamic Library Programming Topics](https://developer.apple.com/library/content/documentation/DeveloperTools/Conceptual/DynamicLibraries/000-Introduction/Introduction.html)。

### Duplicate Libraries

**设置名称：** `LD_WARN_DUPLICATE_LIBRARIES`

当同一个库被多次链接时发出警告。

### Unused Dylibs

**设置名称：** `LD_WARN_UNUSED_DYLIBS`

对任何已链接但未使用的 dylib 发出警告。

### Other Lex Flags

**设置名称：** `LEXFLAGS`

传递给 `lex` 的其他标志的空格分隔列表。请务必对包含空格或特殊字符的参数（例如可能包含空格的路径名）进行反斜杠转义。如果 Xcode 尚未为某个 `lex` 标志提供界面，请使用此设置。

### Generate Case-Insensitive Scanner

**设置名称：** `LEX_CASE_INSENSITIVE_SCANNER`

启用此选项会使 `lex` 生成一个不区分大小写的扫描器。`lex` 输入模式中给出的字母大小写将被忽略，输入中的词法单元（token）匹配将不区分大小写。`yytext` 中给出的匹配文本将保留原始大小写（例如，不会被折叠）。

### Insert #line Directives

**设置名称：** `LEX_INSERT_LINE_DIRECTIVES`

启用此选项会指示 `lex` 插入 `#line` 指令，以便动作中的错误消息能正确地对应到原始的 `lex` 输入文件（如果错误是由输入文件中的代码引起）或 `lex.yy.c`（如果错误是 `lex` 自身的问题）。此选项默认启用；禁用它会向 `lex` 传递一个不插入 `#line` 指令的标志。

### Suppress Default Rule

**设置名称：** `LEX_SUPPRESS_DEFAULT_RULE`

启用此选项会抑制默认规则（即未匹配的扫描器输入会被回显到 `stdout`）。如果扫描器遇到不匹配其任何规则的输入，它会以错误中止。此选项有助于发现扫描器规则集中的漏洞。

### Suppress Warning Messages

**设置名称：** `LEX_SUPPRESS_WARNINGS`

启用此选项会使 `lex` 抑制其警告消息。

### Library Load Constraint Plist

**设置名称：** `LIBRARY_LOAD_CONSTRAINT`

一个 plist 表示形式的路径，该 plist 表示一个需求字典，指定该进程可以加载的库的期望集合。在 macOS 14 或更高版本上构建时支持。

### Library Search Paths

**设置名称：** `LIBRARY_SEARCH_PATHS`

这是一个文件夹路径列表，链接器会在其中搜索产品所使用的库。路径之间以空白分隔，因此任何包含空格的路径都需要正确加引号。

### Display Mangled Names

**设置名称：** `LINKER_DISPLAYS_MANGLED_NAMES`

激活此设置会使链接器显示 C++ 符号的重整（mangled）名称。通常不建议这样做，但开启它有助于诊断和解决 C++ 链接错误。

### Link With Standard Libraries

**设置名称：** `LINK_WITH_STANDARD_LIBRARIES`

启用此设置时，编译器驱动程序会在链接期间自动将其标准库传递给链接器使用。如果需要，可以使用此标志禁用与标准库的链接，然后可以将各个库作为 `OTHER_LDFLAGS` 传入。

### Link-Time Optimization

**设置名称：** `LLVM_LTO`

启用此设置可在链接期间跨文件边界进行优化。

- _No：_ 禁用。不使用链接时优化。
- _Monolithic Link-Time Optimization：_ 此模式对二进制文件执行整体式（monolithic）链接时优化，将所有可执行代码合并为单个单元，并运行激进的编译器优化。
- _Incremental Link-Time Optimization：_ 此模式对二进制文件执行分区式链接时优化，在编译单元之间进行内联，并对每个单元并行运行激进的编译器优化。这样可以实现快速的增量构建，且比整体式 LTO 使用更少的内存。

### Localization Export Supported

**设置名称：** `LOCALIZATION_EXPORT_SUPPORTED`

启用后，此 target/项目中的可本地化内容可以被导出。

### Localization Prefers String Catalogs

**设置名称：** `LOCALIZATION_PREFERS_STRING_CATALOGS`

启用后，本地化导出中生成的字符串表将优先使用 String Catalog 格式。

### Localized Strings in Code Comments

**设置名称：** `LOCALIZED_STRING_CODE_COMMENTS`

启用后，即使被注释掉或包裹在 `#if 0` 中，包裹在 NSLocalizedString 及类似字符串宏中的可本地化字符串也会被提取出来。

### Localized String Macro Names

**设置名称：** `LOCALIZED_STRING_MACRO_NAMES`

用于在源代码中生成本地化字符串的、类似 NSLocalizedString 的宏或函数的基础名称。即使此设置为空，也始终会考虑 NSLocalizedString 和 CFCopyLocalizedString 这两个默认基础名称。

### Localized String SwiftUI Support

**设置名称：** `LOCALIZED_STRING_SWIFTUI_SUPPORT`

启用后，本地化导出期间会提取 SwiftUI 中的字符串字面量。除非同时启用了 `SWIFT_EMIT_LOC_STRINGS`，否则这只会提取 `Text()` 初始化方法中的字符串字面量。

### Mach-O Type

**设置名称：** `MACH_O_TYPE`

此设置决定了生成的二进制文件的格式，以及在构建其他二进制文件时如何链接它。有关二进制文件类型的信息，请参阅 [Mach-O Programming Topics](https://developer.apple.com/library/content/documentation/DeveloperTools/Conceptual/MachOTopics/0-Introduction/introduction.html) 中的 [Building Mach-O Files](https://developer.apple.com/library/content/documentation/DeveloperTools/Conceptual/MachOTopics/1-Articles/building_files.html#//apple_ref/doc/uid/TP40001828-SW1)。

- _Executable：_ 可执行文件和独立二进制文件，无法被链接。[mh_execute]
- _Dynamic Library：_ 动态库在构建时链接，在需要时自动加载。[mh_dylib]
- _Bundle：_ Bundle 库在运行时被显式加载。[mh_bundle]
- _Static Library：_ 静态库在构建时链接，在执行时加载。[staticlib]
- _Relocatable Object File：_ 目标文件是在构建时链接的单模块文件。[mh_object]

### Suppress all mapc warnings

**设置名称：** `MAPC_NO_WARNINGS`

将 `.xcmappingmodel` 文件编译为 `.cdm`，且不报告警告。

### Marketing Version

**设置名称：** `MARKETING_VERSION`

此设置定义了该项目面向用户可见的版本。

启用 `GENERATE_INFOPLIST_FILE` 时，会将 `Info.plist` 文件中 [CFBundleShortVersionString](https://developer.apple.com/documentation/bundleresources/information-property-list/cfbundleshortversionstring) 键的值设为此构建设置的值。

### Alternative Distribution - Marketplaces

**设置名称：** `MARKETPLACES`

启用后，可在从 Xcode 运行时，使用一个附加的应用市场标识符列表覆盖你 App 的分发者标识符。

### Build Mergeable Library

**设置名称：** `MERGEABLE_LIBRARY`

对于动态库和框架，将此 target 的二进制文件链接为一个可合并库（mergeable library），如果依赖它的某个 target 配置为这样做，该库就可以被合并进该 target 的产品中。此 target 会在发行版构建中被链接为可合并库以便被合并，但在调试构建中会改为链接为一个普通的、用于重新导出的动态库。对于其他二进制文件类型，此设置不起作用。

有关可合并库的更多信息，请参阅 [Configuring your project to use mergeable libraries](https://developer.apple.com/documentation/xcode/configuring-your-project-to-use-mergeable-libraries)。

### Create Merged Binary

**设置名称：** `MERGED_BINARY_TYPE`

使用此设置，通过将该 target 的二进制文件与其所链接的可合并库合并，来将它们链接成一个单一的二进制文件。仅适用于可执行文件、动态库和框架。

- 设为 Automatic 时，此 target 中构建动态库或框架、且位于其 Link Binaries With Libraries 中的直接依赖项，会在发行版构建期间自动构建为可合并库并合并进此 target 的二进制文件中，或在调试构建期间被重新导出。
- 设为 Manual 时，只有显式启用了 Build Mergeable Library 的直接依赖项才会被合并或重新导出。

有关可合并库的更多信息，请参阅 [Configuring your project to use mergeable libraries](https://developer.apple.com/documentation/xcode/configuring-your-project-to-use-mergeable-libraries)。

### Module Map File

**设置名称：** `MODULEMAP_FILE`

这是相对于项目的路径，指向为编译器定义模块结构的 LLVM 模块映射文件。如果为空，当启用 `DEFINES_MODULE` 时，会为适当的产品自动生成该文件。

### Private Module Map File

**设置名称：** `MODULEMAP_PRIVATE_FILE`

这是相对于项目的路径，指向为私有头文件定义模块结构的 LLVM 模块映射文件。

### MODULES_FOLDER_PATH

**设置名称：** `MODULES_FOLDER_PATH`

指定包含该产品 Clang 模块映射和 Swift 模块内容的目录。

### MODULE_CACHE_DIR

**设置名称：** `MODULE_CACHE_DIR`

编译器存储其缓存模块的文件夹的绝对路径——此缓存是一项性能改进。

### Module Identifier

**设置名称：** `MODULE_NAME`

这是生成的桩中列出的内核模块标识符。仅在构建内核扩展时使用。

### Module Start Routine

**设置名称：** `MODULE_START`

这定义了内核模块启动例程的名称。仅在构建内核扩展时使用。

### Module Stop Routine

**设置名称：** `MODULE_STOP`

这定义了内核模块停止例程的名称。仅在构建内核扩展时使用。

### Supported Languages

**设置名称：** `MODULE_VERIFIER_SUPPORTED_LANGUAGES`

用于验证模块的语言，即框架客户端所支持的语言。允许的值为“c”、“c++”、“objective-c”、“objective-c++”

### Supported Language Dialects

**设置名称：** `MODULE_VERIFIER_SUPPORTED_LANGUAGE_STANDARDS`

用于验证模块的语言方言，即框架客户端所支持的语言方言。允许的值为“ansi”、“c89”、“gnu89”、“c99”、“gnu99”、“c11”、“gnu11”、“c17”、“gnu17”、“c23”、“gnu23”、“c++98”、“gnu++98”、“c++11”、“gnu++11”、“c++14”、“gnu++14”、“c++17”、“gnu++17”、“c++20”、“gnu++20”、“c++23”、“gnu++23”

### Module Version

**设置名称：** `MODULE_VERSION`

这是生成的桩中列出的内核模块版本。仅在构建内核扩展时使用。

### Suppress momc warnings for delete rules

**设置名称：** `MOMC_NO_DELETE_RULE_WARNINGS`

在编译 `.xcdatamodel(d)` 文件期间，抑制托管对象模型编译器（`momc`）针对删除规则发出的警告。

### Suppress momc warnings on missing inverse relationships

**设置名称：** `MOMC_NO_INVERSE_RELATIONSHIP_WARNINGS`

在编译 `.xcdatamodel(d)` 文件期间，抑制托管对象模型编译器（`momc`）针对缺失逆向关系输出的警告

### Suppress momc warnings for entities with more than 100 properties

**设置名称：** `MOMC_NO_MAX_PROPERTY_COUNT_WARNINGS`

在编译 `.xcdatamodel(d)` 文件期间，抑制托管对象模型编译器（`momc`）针对属性数超过 100 个的实体输出的警告。

### Suppress all momc warnings

**设置名称：** `MOMC_NO_WARNINGS`

在编译 `.xcdatamodel(d)` 文件期间，抑制托管对象模型编译器（`momc`）输出的警告

### Suppress momc error on transient inverse relationships

**设置名称：** `MOMC_SUPPRESS_INVERSE_TRANSIENT_ERROR`

在编译 `.xcdatamodel(d)` 文件期间，抑制托管对象模型编译器（`momc`）针对瞬态逆向关系输出的警告。此设置仅适用于在 10.5 引入该错误之前、在 10.4.x 中创建并能正常编译的模型

### Other Metal Linker Flags

**设置名称：** `MTLLINKER_FLAGS`

Metal 链接器标志的空格分隔列表

### Other Metal Compiler Flags

**设置名称：** `MTL_COMPILER_FLAGS`

编译器标志的空格分隔列表

### Produce Debugging Information

**设置名称：** `MTL_ENABLE_DEBUG_INFO`

着色器调试和性能分析需要调试信息。

### Enable Index-While-Building Functionality (Metal)

**设置名称：** `MTL_ENABLE_INDEX_STORE`

控制编译器是否应在构建时输出索引数据。

### Enable Modules (Metal)

**设置名称：** `MTL_ENABLE_MODULES`

启用模块的使用。头文件会作为语义模块导入，而非原始头文件。这可以带来更快的构建速度和项目索引速度。

- _All：_ 为所有头文件启用。
- _Standard library：_ 仅为标准库头文件启用（默认）。
- _None：_ 禁用此功能。

### Enable Fast Math

**设置名称：** `MTL_FAST_MATH`

为浮点算术启用优化，这可能违反 IEEE 754 标准，并对单精度和半精度浮点禁用高精度版本的数学函数。

### Header Search Paths

**设置名称：** `MTL_HEADER_SEARCH_PATHS`

这是一个文件夹路径列表，编译 Metal 时，编译器会在其中搜索被包含或导入的头文件。路径之间以空白分隔，因此任何包含空格的路径都需要正确加引号。[MTL_HEADER_SEARCH_PATHS, -I]

### Ignore Warnings

**设置名称：** `MTL_IGNORE_WARNINGS`

启用此选项会使所有警告都被忽略。[MTL_IGNORE_WARNINGS, -W]

### Metal Language Revision

**设置名称：** `MTL_LANGUAGE_REVISION`

确定要使用的语言修订版本。必须为此选项提供一个值。

### Single-Precision Floating Point Functions

**设置名称：** `MTL_MATH_FP32_FUNCTIONS`

控制单精度浮点的默认数学函数

### Math Mode

**设置名称：** `MTL_MATH_MODE`

控制浮点优化

### Optimization Level

**设置名称：** `MTL_OPTIMIZATION_LEVEL`

Metal 编译器的优化级别。

- _Default：_ 针对程序性能进行优化 [-O2]。此设置应用适度的优化级别，启用大多数优化。
- _Size：_ 与 default 类似，但增加了减小代码大小的额外优化 [-Os]。此设置限制会增加代码大小的优化（例如循环展开和函数内联），并启用其他针对大小的优化。在针对性能优化会导致代码非常庞大的情况下，它可以减少编译时间和编译器内存占用。

### Preprocessor Definitions

**设置名称：** `MTL_PREPROCESSOR_DEFINITIONS`

形如“foo”或“foo=bar”的预处理器宏的空格分隔列表。

### Treat Warnings as Errors

**设置名称：** `MTL_TREAT_WARNINGS_AS_ERRORS`

启用此选项会使所有警告都被当作错误处理。[MTL_TREAT_WARNINGS_AS_ERRORS, -Werror]

### NATIVE_ARCH

**设置名称：** `NATIVE_ARCH`

标识执行构建所在的架构。

### OBJECT_FILE_DIR

**设置名称：** `OBJECT_FILE_DIR`

部分标识放置变体目标文件的目录。完整的规格是使用此构建设置的各个变体计算得出的。

### Intermediate Build Files Path

**设置名称：** `OBJROOT`

构建期间放置中间文件的路径。中间文件包括生成的源文件、目标文件等。Run Script 构建阶段也可以在此处放置和访问文件。通常不会按 target 设置此路径，而是按项目或按用户设置。默认情况下，此值设为 `$(PROJECT_DIR)/build`。

### Build Active Architecture Only

**设置名称：** `ONLY_ACTIVE_ARCH`

如果启用，只会构建活动架构。使用未定义具体架构的运行目标（例如“Generic Device”运行目标）构建时，或者如果“Override Architectures”scheme 选项设为“Match Run Destination”或“Universal”，此设置将被忽略。

### On Demand Resources Initial Install Tags

**设置名称：** `ON_DEMAND_RESOURCES_INITIAL_INSTALL_TAGS`

定义一组要随你的应用程序一起下载和安装的初始按需资源（On Demand Resources）标签。

### On Demand Resources Prefetch Order

**设置名称：** `ON_DEMAND_RESOURCES_PREFETCH_ORDER`

在你的 App 安装后，此设置定义了一组应被下载的按需资源标签。这些标签会在你的应用程序初始安装之后下载，并按照列表中从前到后提供的顺序下载。

### OpenCL Architectures

**设置名称：** `OPENCL_ARCHS`

产品将为之构建的架构列表。这通常设为平台提供的一个预定义构建设置。

### Auto-vectorizer

**设置名称：** `OPENCL_AUTO_VECTORIZE_ENABLE`

为 CPU 自动向量化 `OpenCL` 内核。此设置仅对 CPU 有效。这使得编写一个可在 CPU 和 GPU 之间移植且性能良好的单一内核成为可能。

### OpenCL Compiler Version

**设置名称：** `OPENCL_COMPILER_VERSION`

该平台所支持的 `OpenCL` C 编译器版本。

### Flush denorms to zero

**设置名称：** `OPENCL_DENORMS_ARE_ZERO`

此选项控制单精度和双精度非规格化数（denormalized number）的处理方式。如果将其指定为构建选项，单精度非规格化数可能会被刷新为零；如果设备支持双精度的可选扩展，双精度非规格化数也可能被刷新为零。这旨在作为一个性能提示，如果设备支持单精度（或双精度）非规格化数，`OpenCL` 编译器可以选择不将非规格化数刷新为零。

如果设备不支持单精度非规格化数（例如 `CL_DEVICE_SINGLE_FP_CONFIG` 中未设置 `CL_FP_DENORM` 位），此选项对单精度数会被忽略。

如果设备不支持双精度、或者支持双精度但不支持双精度非规格化数（例如 `CL_DEVICE_DOUBLE_FP_CONFIG` 中未设置 `CL_FP_DENORM` 位），此选项对双精度数会被忽略。

此标志仅适用于程序内部的标量和向量单精度浮点变量及其上的计算。它不适用于图像对象的读取或写入。

### Double as single

**设置名称：** `OPENCL_DOUBLE_AS_SINGLE`

将双精度浮点表达式当作单精度浮点表达式处理。此选项仅适用于 GPU。

### Relax IEEE Compliance

**设置名称：** `OPENCL_FAST_RELAXED_MATH`

这允许为浮点算术进行优化，这可能违反 IEEE 754 标准，以及 `OpenCL` 1.1 规范中第 7.4 节（针对单精度浮点）、第 9.3.9 节（针对双精度浮点）所定义的数值合规性要求，以及第 7.5 节中的边界情况行为。

这旨在作为一项性能优化。

此选项会使预处理器宏 `__FAST_RELAXED_MATH__` 在 `OpenCL` 程序中被定义。

### Use MAD

**设置名称：** `OPENCL_MAD_ENABLE`

允许将 `a * b + c` 替换为一条 `mad` 指令。`mad` 以降低的精度计算 `a * b + c`。例如，一些 `OpenCL` 设备实现 `mad` 的方式是先截断 `a * b` 的结果，再将其与 `c` 相加。

这旨在作为一项性能优化。

### Optimization Level

**设置名称：** `OPENCL_OPTIMIZATION_LEVEL`

- _None：_ 不优化。[-O0] 使用此设置时，编译器的目标是降低编译成本，并使调试产生预期的结果。各语句相互独立：如果你在语句之间用断点停止程序，就可以为任意变量赋新值，或者将程序计数器改到该函数中的任意其他语句，并得到与源代码完全一致的预期结果。
- _Fast：_ 优化编译会花费稍多的时间，对于大型函数还会占用更多的内存。[-O, -O1] 使用此设置时，编译器会尝试在不进行任何耗费大量编译时间的优化的前提下，减小代码大小和执行时间。在 Apple 的编译器中，进行优化时默认会禁用严格别名、块重排序和块间调度。
- _Faster：_ 编译器会执行几乎所有不涉及空间-速度权衡的受支持优化。[-O2] 使用此设置时，编译器不会执行循环展开、函数内联或寄存器重命名。与 `Fast` 设置相比，此设置会同时增加编译时间和生成代码的性能。
- _Fastest：_ 开启 `Faster` 设置指定的所有优化，还会开启函数内联和寄存器重命名选项。此设置可能导致更大的二进制文件。[-O3]
- _Fastest, smallest：_ 针对大小进行优化。此设置会启用所有通常不会增加代码大小的 `Faster` 优化，还会执行旨在减小代码大小的进一步优化。[-Os]

### OpenCL Other Flags

**设置名称：** `OPENCL_OTHER_BC_FLAGS`

传递给编译器的其他标志的空格分隔列表。请务必对包含空格或特殊字符的参数（例如可能包含空格的路径名）进行反斜杠转义。如果 Xcode 尚未为某个特定的编译器标志提供界面，请使用此设置。

### OpenCL Preprocessor Macros

**设置名称：** `OPENCL_PREPROCESSOR_DEFINITIONS`

形如 `foo` 或 `foo=bar` 的预处理器宏的空格分隔列表。

### Order File

**设置名称：** `ORDER_FILE`

一个文件的路径，该文件用于改变函数和数据的布局顺序。

对于输出文件中的每个段，在该段中任何在顺序文件（order file）中指定的符号，都会被移动到该段的起始位置，并按照顺序文件中的相同顺序排列。顺序文件是每行一个符号名称的文本文件。以 `#` 开头的行是注释。符号名称前面可以选择性地加上其目标文件的叶子名称和一个冒号（例如 `foo.o:_foo`）。这对于出现在多个文件中的静态函数/数据很有用。符号名称前面还可以选择性地加上架构（例如 `ppc:_foo` 或 `ppc:foo.o:_foo`）。这使你可以拥有一个适用于多种架构的顺序文件。字面量 C 字符串可以通过在顺序文件中给字符串加引号来排序（例如 `"Hello, world\n"`）。

通常你不应该在 Debug 或 Development 配置中指定顺序文件，因为这会使已链接的二进制文件对调试器而言可读性变差。仅在 Release 或 Deployment 配置中使用它们。

### Save as Execute-Only

**设置名称：** `OSACOMPILE_EXECUTE_ONLY`

以仅可执行的形式保存输出脚本；该脚本可以运行，但无法在 Script Editor 或 Xcode 中打开。禁用此选项时，用户可以通过打开脚本查看原始脚本源代码。

### Other C Flags

**设置名称：** `OTHER_CFLAGS`

传递给 C 和 Objective-C 文件编译器的其他标志的空格分隔列表。请务必对包含空格或特殊字符的参数（例如可能包含空格的路径名）进行反斜杠转义。如果 Xcode 尚未为某个特定的 C 或 Objective-C 编译器标志提供界面，请使用此设置。

### Other Code Signing Flags

**设置名称：** `OTHER_CODE_SIGN_FLAGS`

传递给 `codesign(1)` 的其他选项列表。

### Other C++ Flags

**设置名称：** `OTHER_CPLUSPLUSFLAGS`

传递给 C++ 和 Objective-C++ 文件编译器的其他标志的空格分隔列表。请务必对包含空格或特殊字符的参数（例如可能包含空格的路径名）进行反斜杠转义。如果 Xcode 尚未为某个 C++ 或 Objective-C++ 编译器标志提供界面，请使用此设置。

### Other DocC Flags

**设置名称：** `OTHER_DOCC_FLAGS`

传递给 DocC 的其他标志列表

### Other IIG C Flags

**设置名称：** `OTHER_IIG_CFLAGS`

传递给 `iig` 所调用的 clang 的其他标志的空格分隔列表。请务必对包含空格或特殊字符的参数（例如可能包含空格的路径名）进行反斜杠转义。如果 Xcode 尚未为某个特定的 `iig` 标志提供界面，请使用此设置

### Other IIG Flags

**设置名称：** `OTHER_IIG_FLAGS`

传递给 `iig` 编译器的其他标志的空格分隔列表。请务必对包含空格或特殊字符的参数（例如可能包含空格的路径名）进行反斜杠转义。如果 Xcode 尚未为某个特定的 `iig` 标志提供界面，请使用此设置

### Other Linker Flags

**设置名称：** `OTHER_LDFLAGS`

此设置中定义的选项会传递给链接器的各次调用。

### Other Librarian Flags

**设置名称：** `OTHER_LIBTOOLFLAGS`

此设置中定义的选项会传递给归档库管理器（archive librarian，用于生成静态库）的所有调用。

### Other MiG Flags

**设置名称：** `OTHER_MIGFLAGS`

传递给 `mig` 的其他标志的空格分隔列表。请务必对包含空格或特殊字符的参数（例如可能包含空格的路径名）进行反斜杠转义。如果 Xcode 尚未为某个 `mig` 标志提供界面，请使用此设置。

### Other Module Verifier Flags

**设置名称：** `OTHER_MODULE_VERIFIER_FLAGS`

传递给 modules-verifier 工具的其他标志。

### Other OSACompile Flags

**设置名称：** `OTHER_OSACOMPILEFLAGS`

传递给 `osacompile` 的其他标志的空格分隔列表。请务必对包含空格或特殊字符的参数（例如可能包含空格的路径名）进行反斜杠转义。如果 Xcode 尚未为某个特定的 `osacompile` 标志提供界面，请使用此设置。

### Other Rez Flags

**设置名称：** `OTHER_REZFLAGS`

传递给 `Rez` 编译器的其他标志的空格分隔列表。请务必对包含空格或特殊字符的参数（例如可能包含空格的路径名）进行反斜杠转义。如果 Xcode 尚未为某个特定的 `Rez` 标志提供界面，请使用此设置。

### Other Swift Flags

**设置名称：** `OTHER_SWIFT_FLAGS`

传递给 Swift 编译器的其他标志列表。

### Other Text-Based InstallAPI Flags

**设置名称：** `OTHER_TAPI_FLAGS`

此设置中定义的选项会传递给 `Text-Based InstallAPI` 工具的各次调用。

### PACKAGE_TYPE

**设置名称：** `PACKAGE_TYPE`

统一类型标识符。标识该 target 构建的产品类型。有些产品可能由单个二进制文件或归档文件组成。其他产品可能由多个文件组成，这些文件被归组在单个目录下。这些容器目录称为 _bundle_。

### Property List Output Encoding

**设置名称：** `PLIST_FILE_OUTPUT_FORMAT`

指定属性列表文件（`.plist`）的输出编码。输出编码可以是 `binary` 或 `XML`。默认情况下，输出编码与输入保持一致。

### PLUGINS_FOLDER_PATH

**设置名称：** `PLUGINS_FOLDER_PATH`

指定包含产品插件的目录。

### Precompiled Header Uses Files From Build Directory

**设置名称：** `PRECOMPS_INCLUDE_HEADERS_FROM_BUILT_PRODUCTS_DIR`

此设置能更好地控制在项目之间共享预编译前缀头文件。默认情况下，如果构建目录位于项目目录之外，Xcode 会假定前缀头文件可能包含来自构建目录的头文件。Xcode 无法提前确定这一点，因为在需要该信息时，其他项目可能尚未构建到共享构建目录中。

如果你的前缀文件从不包含来自构建目录的文件，你可以将此设置设为 `NO`，以改善预编译头文件的共享。如果该前缀确实使用了项目目录内某个构建目录中的文件，你可以将此设置设为 `YES`，以避免可能导致构建失败的意外共享。

### Single-Object Prelink Flags

**设置名称：** `PRELINK_FLAGS`

执行单目标文件预链接时传递的其他标志。

### Prelink libraries

**设置名称：** `PRELINK_LIBS`

执行单目标文件预链接时传递的其他库。

### Private Headers Folder Path

**设置名称：** `PRIVATE_HEADERS_FOLDER_PATH`

构建期间将私有头文件复制到的位置，相对于构建产品文件夹。

### PROCESSED_INFOPLIST_PATH

**设置名称：** `PROCESSED_INFOPLIST_PATH`

应用了 C 预处理和/或变量展开之后，按架构、按变体划分的中间 Info.plist 的路径。

### Product Bundle Identifier

**设置名称：** `PRODUCT_BUNDLE_IDENTIFIER`

一个唯一标识该 Bundle 的字符串。该字符串应采用反向 DNS 格式，只能使用字母数字字符（`A-Z`、`a-z`、`0-9`）、句点（`.`）和连字符（`-`）。

启用 `GENERATE_INFOPLIST_FILE` 时，会将 `Info.plist` 文件中 [CFBundleIdentifier](https://developer.apple.com/documentation/bundleresources/information-property-list/cfbundleidentifier) 键的值设为此构建设置的值。

### PRODUCT_DEFINITION_PLIST

**设置名称：** `PRODUCT_DEFINITION_PLIST`

一个文件的路径，该文件为产品归档指定了附加要求。

### Product Module Name

**设置名称：** `PRODUCT_MODULE_NAME`

为该 target 构建的源代码模块所使用的名称，该名称会用于在实现源文件中导入该模块。必须是一个有效的标识符。

### Product Name

**设置名称：** `PRODUCT_NAME`

这是该 target 生成的产品的基础名称。

启用 `GENERATE_INFOPLIST_FILE` 时，会将 `Info.plist` 文件中 [CFBundleName](https://developer.apple.com/documentation/bundleresources/information-property-list/cfbundlename) 键的值设为此构建设置的值。

### Project Name

**设置名称：** `PROJECT_NAME`

当前项目的名称。

### PROJECT_TEMP_DIR

**设置名称：** `PROJECT_TEMP_DIR`

标识放置项目中间构建文件的目录。此目录由该项目定义的所有 target 共享。Run Script 构建阶段应在 `DERIVED_FILE_DIR` 所标识的目录中生成中间构建文件，而不是此构建设置指定的位置。

### Provisioning Profile

**设置名称：** `PROVISIONING_PROFILE_SPECIFIER`

必须包含一个描述文件名称（或 UUID）。缺失或无效的描述文件会导致构建错误。请与 [DEVELOPMENT_TEAM] 结合使用，以完整指定预配描述文件。

### Public Headers Folder Path

**设置名称：** `PUBLIC_HEADERS_FOLDER_PATH`

构建期间将公共头文件复制到的位置，相对于构建产品文件夹。

### Re-Exported Framework Names

**设置名称：** `REEXPORTED_FRAMEWORK_NAMES`

其符号应从已构建的库中重新导出的框架名称列表。

### Re-Exported Library Names

**设置名称：** `REEXPORTED_LIBRARY_NAMES`

其符号应从已构建的库中重新导出的库名称列表。

### Re-Exported Library Paths

**设置名称：** `REEXPORTED_LIBRARY_PATHS`

其符号应从已构建的库中重新导出的库路径列表。

### Strip USDZ file(s) from Reference Object

**设置名称：** `REFERENCEOBJECT_STRIP_USDZ`

编译 Reference Object 文件时，剥离任何内嵌的 USDZ 文件。

### Register App Groups

**设置名称：** `REGISTER_APP_GROUPS`

在描述文件中注册 App Group。

### REMOVE_CVS_FROM_RESOURCES

**设置名称：** `REMOVE_CVS_FROM_RESOURCES`

指定在复制 Bundle 资源时，是否从中移除 `CVS` 目录。

### REMOVE_GIT_FROM_RESOURCES

**设置名称：** `REMOVE_GIT_FROM_RESOURCES`

指定在复制 Bundle 资源时，是否从中移除 `.git` 目录。

### REMOVE_HG_FROM_RESOURCES

**设置名称：** `REMOVE_HG_FROM_RESOURCES`

指定在复制 Bundle 资源时，是否从中移除 `.hg` 目录。

### REMOVE_SVN_FROM_RESOURCES

**设置名称：** `REMOVE_SVN_FROM_RESOURCES`

指定在复制 Bundle 资源时，是否从中移除 `SVN` 目录。

### File Fork of Binary Sources

**设置名称：** `RESMERGER_SOURCES_FORK`

决定 `ResMerger` 将二进制输入文件视为数据分支（data-fork）承载还是资源分支（resource-fork）承载，或者由它自动检查每个输入文件。

### Resources Targeted Device Family

**设置名称：** `RESOURCES_TARGETED_DEVICE_FAMILY`

当资源复制需要与默认目标设备不同时，覆盖 `TARGETED_DEVICE_FAMILY`。

### RETAIN_RAW_BINARIES

**设置名称：** `RETAIN_RAW_BINARIES`

指定是否保留未剥离二进制文件的副本。

### REZ_COLLECTOR_DIR

**设置名称：** `REZ_COLLECTOR_DIR`

指定由 `ResMerger` 生成的、已收集的 Resource Manager 资源在被添加到产品之前存储的目录。

### REZ_OBJECTS_DIR

**设置名称：** `REZ_OBJECTS_DIR`

指定由 `Rez` 生成的、已编译的 Resource Manager 资源在使用 `ResMerger` 收集之前存储的目录。

### Rez Prefix File

**设置名称：** `REZ_PREFIX_FILE`

为每个已编译的 `Rez` 文件在命令行上隐式包含指定名称的文件。给出的路径应为相对于项目的路径，或者是绝对路径。

### Preprocessor Defines

**设置名称：** `REZ_PREPROCESSOR_DEFINITIONS`

编译 Resource Manager 资源时，将定义这些字符串。

### Preprocessor Undefines

**设置名称：** `REZ_PREPROCESSOR_UNDEFINITIONS`

编译 Resource Manager 资源时，将取消定义这些字符串。

### Resolve Aliases

**设置名称：** `REZ_RESOLVE_ALIASES`

允许别名不被解析或有条件地解析。默认设置是始终解析别名。

### Read-only Resource Map

**设置名称：** `REZ_RESOURCE_MAP_READ_ONLY`

启用此选项会使资源映射输出为只读。

### Rez Script Type

**设置名称：** `REZ_SCRIPT_TYPE`

启用编译 Resource Manager 资源时，对特定双字节字符文字标识符的识别。这使得字符串中的双字节字符可以作为不可分割的实体处理。默认语言为 Roman，指定的是单字节字符集。

### Rez Search Paths

**设置名称：** `REZ_SEARCH_PATHS`

这是一个路径列表，用于搜索包含 Resource Manager 资源的文件。路径之间以空白分隔，因此任何包含空格的路径都需要正确加引号。

### Show Diagnostic Output

**设置名称：** `REZ_SHOW_DEBUG_OUTPUT`

启用此选项会使编译 Resource Manager 资源时输出版本和进度信息。

### Suppress Type Redeclaration Warnings

**设置名称：** `REZ_SUPPRESS_REDECLARED_RESOURCE_TYPE_WARNINGS`

启用此选项会抑制关于重新声明资源类型的警告。

### Allow DYLD Environment Variables

**设置名称：** `RUNTIME_EXCEPTION_ALLOW_DYLD_ENVIRONMENT_VARIABLES`

一个布尔值，指示该 App 是否可能受动态链接器环境变量的影响，你可以使用这些变量向该 App 的进程注入代码。

### Allow JIT

**设置名称：** `RUNTIME_EXCEPTION_ALLOW_JIT`

一个布尔值，指示该 App 是否可以使用 MAP_JIT 标志创建可写且可执行的内存。

### Allow Unsigned Executable Memory

**设置名称：** `RUNTIME_EXCEPTION_ALLOW_UNSIGNED_EXECUTABLE_MEMORY`

一个布尔值，指示该 App 是否可以在不受 MAP_JIT 标志所施加限制的情况下创建可写且可执行的内存。

### Debugging Tool

**设置名称：** `RUNTIME_EXCEPTION_DEBUGGING_TOOL`

一个布尔值，指示该 App 是否是一个调试器，是否可以附加到其他进程或获取任务端口。

### Disable Executable Page Protection

**设置名称：** `RUNTIME_EXCEPTION_DISABLE_EXECUTABLE_PAGE_PROTECTION`

一个布尔值，指示在启动某个 App 及其执行期间，是否禁用所有代码签名保护。

### Disable Library Validation

**设置名称：** `RUNTIME_EXCEPTION_DISABLE_LIBRARY_VALIDATION`

一个布尔值，指示该 App 是否在不要求代码签名的情况下加载任意插件或框架。

### Analyze During 'Build'

**设置名称：** `RUN_CLANG_STATIC_ANALYZER`

激活此设置会使 Xcode 在每次构建期间，对符合条件的源文件运行 `Clang` 静态分析工具。

### Build Documentation During 'Build'

**设置名称：** `RUN_DOCUMENTATION_COMPILER`

作为“Build”操作的一部分，同时构建文档。

### Scan All Source Files for Includes

**设置名称：** `SCAN_ALL_SOURCE_FILES_FOR_INCLUDES`

激活此设置会使所有源文件在计算依赖关系图时都被扫描 include（例如头文件的 include），在这种情况下，如果某个被包含的文件发生变化，下次构建包含它的 target 时，包含它的文件就会被重新构建。通常只有某些类型的文件（例如 C 语言源文件）会被扫描。

如果你的项目包含使用自定义构建规则编译的、类型不常见的文件，此设置会很有用。

### SCRIPTS_FOLDER_PATH

**设置名称：** `SCRIPTS_FOLDER_PATH`

指定包含产品脚本的目录。

### Base SDK

**设置名称：** `SDKROOT`

构建期间所使用基础 SDK 的名称或路径。该产品将针对指定 SDK 内的头文件和库进行构建。此路径将被添加到所有搜索路径之前，并通过环境传递给编译器和链接器。可以在 `ADDITIONAL_SDKS` 设置中指定其他 SDK。

### Symbol Ordering Flags

**设置名称：** `SECTORDER_FLAGS`

这些标志通常用于指定段内符号排序的选项，例如传递给 `ld` 的 `-sectorder` 选项。

通常你不应该在 Debug 或 Development 配置中指定符号排序选项，因为这会使已链接的二进制文件对调试器而言可读性变差。仅在 Release 或 Deployment 配置中使用它们。

### Separately Edit Symbols

**设置名称：** `SEPARATE_SYMBOL_EDIT`

当需要编辑已链接产品的符号时，激活此设置会使编辑通过单独调用 `nmedit(1)` 进行。否则，如果可能，编辑会在链接期间进行。

### SHARED_FRAMEWORKS_FOLDER_PATH

**设置名称：** `SHARED_FRAMEWORKS_FOLDER_PATH`

指定包含产品共享框架的目录。

### Precompiled Headers Cache Path

**设置名称：** `SHARED_PRECOMPS_DIR`

构建期间放置预编译前缀头文件的路径。默认值为 `$(OBJROOT)/SharedPrecompiledHeaders`。使用一个公共位置可以让预编译头文件在多个项目之间共享。

### Skip Install

**设置名称：** `SKIP_INSTALL`

如果启用，即使部署位置处于活动状态，也不安装已构建的产品。

### Skip Mergeable Library Bundle Hook

**设置名称：** `SKIP_MERGEABLE_LIBRARY_BUNDLE_HOOK`

对于可合并库，跳过向该库的资源 Bundle 添加钩子。这将阻止 `Bundle(for:)` 返回此库的资源 Bundle。

有关可合并库的更多信息，请参阅 [Configuring your project to use mergeable libraries](https://developer.apple.com/documentation/xcode/configuring-your-project-to-use-mergeable-libraries)。

### SRCROOT

**设置名称：** `SRCROOT`

标识包含该 target 源文件的目录。

### STRINGSDATA_DIR

**设置名称：** `STRINGSDATA_DIR`

启用 SWIFT_EMIT_LOC_STRINGS 时，写入 .stringsdata 文件的位置。

### STRINGSDATA_ROOT

**设置名称：** `STRINGSDATA_ROOT`

为本地化导出时，遍历并收集 .stringsdata 文件的位置。

### Adjust Strings File Names for Info.plist

**设置名称：** `STRINGS_FILE_INFOPLIST_RENAME`

如果启用，会将基础名称与该 target 的 Info.plist 文件相匹配的 .strings 文件，在构建产品中重命名为 InfoPlist.strings。

### Strings File Output Encoding

**设置名称：** `STRINGS_FILE_OUTPUT_ENCODING`

指定用于 Strings 文件的输出编码——默认是 UTF-16。该值可以是 `NSStringEncoding`（例如 `NSString` 所识别的某个数值），也可以是 `CFString` 所理解的 IANA 字符集名称。建议源文件采用 UTF-8 编码（这是标准 strings 文件的默认编码），Xcode 会自动将其处理为输出编码。如果文件无法转换为指定的编码，处理将会失败。

### Generate String Catalog Symbols

**设置名称：** `STRING_CATALOG_GENERATE_SYMBOLS`

启用后，会为 String Catalog 中手动管理的字符串生成符号。

### Additional Strip Flags

**设置名称：** `STRIPFLAGS`

剥离该构建已链接产品时传递的其他标志。

### Strip Linked Product

**设置名称：** `STRIP_INSTALLED_PRODUCT`

如果启用，在执行部署后处理时，该构建的已链接产品会被剥离符号。

### Remove Text Metadata From PNG Files

**设置名称：** `STRIP_PNG_TEXT`

PNG 文件中以文本块形式存在的元数据会被移除，以减小其磁盘占用。

### Strip Style

**设置名称：** `STRIP_STYLE`

对该构建的已链接产品执行的符号剥离级别。默认值由该 target 的产品类型定义。

- _All Symbols：_ 彻底剥离二进制文件，移除符号表和重定位信息。[all, -s]
- _Non-Global Symbols：_ 剥离非全局符号，但保留外部符号。[non-global, -x]
- _Debugging Symbols：_ 剥离调试符号，但保留局部和全局符号。[debugging, -S]

### Strip Swift Symbols

**设置名称：** `STRIP_SWIFT_SYMBOLS`

调整由 STRIP_STYLE 设置指定的符号剥离级别，使该构建的已链接产品被剥离时，所有 Swift 符号都会被移除。

### Supported Platforms

**设置名称：** `SUPPORTED_PLATFORMS`

可以使用基础 SDK 的受支持平台列表。如果该产品可以使用不同的 SDK 针对多个平台构建，会使用此设置。

### Supports Mac Catalyst

**设置名称：** `SUPPORTS_MACCATALYST`

支持为 Mac Catalyst 构建此 target。

### Show Mac (Designed for iPhone & iPad) Destination

**设置名称：** `SUPPORTS_MAC_DESIGNED_FOR_IPHONE_IPAD`

显示 Mac（为 iPhone 设计）和 Mac（为 iPad 设计）运行目标。

### Supports Text-Based InstallAPI

**设置名称：** `SUPPORTS_TEXT_BASED_API`

启用以表明该 target 支持 `Text-Based InstallAPI`，这将使其在 `install` 构建期间生成。

### Show Apple Vision (Designed for iPhone & iPad) Destination

**设置名称：** `SUPPORTS_XR_DESIGNED_FOR_IPHONE_IPAD`

显示 Apple Vision（为 iPhone 设计）和 Apple Vision（为 iPad 设计）运行目标。

### Active Compilation Conditions

**设置名称：** `SWIFT_ACTIVE_COMPILATION_CONDITIONS`

要为条件编译表达式启用的编译条件列表。

### Approachable Concurrency

**设置名称：** `SWIFT_APPROACHABLE_CONCURRENCY`

启用一系列即将推出的特性，旨在为 Swift 并发提供一条更易上手的路径：DisableOutwardActorInference、GlobalActorIsolatedTypesUsability、InferIsolatedConformances、InferSendableFromCaptures 和 NonisolatedNonsendingByDefault。

### Bridging Header is Internal to the Module

**设置名称：** `SWIFT_BRIDGING_HEADER_IS_INTERNAL`

当存在桥接头文件时，此设置指示该桥接头文件的内容是否应被当作来自内部 import 那样导入。当桥接头文件与被导入到其他模块中的 Swift 模块一起使用时，这是必要的。

### Compilation Mode

**设置名称：** `SWIFT_COMPILATION_MODE`

此设置控制模块中 Swift 文件被重新构建的方式。

- _Incremental_： 只重新构建模块中已过期的 Swift 源文件，按需运行多个编译器进程。
- _Whole Module_： 始终在单个编译器进程中重新构建模块中的所有 Swift 源文件。

### Default Actor Isolation

**设置名称：** `SWIFT_DEFAULT_ACTOR_ISOLATION`

控制未注解代码的默认 Actor 隔离。设为“MainActor”时，默认会推断出 `@MainActor` 隔离，以缓解顺序代码中的假阳性数据争用安全错误。

### Disable Safety Checks

**设置名称：** `SWIFT_DISABLE_SAFETY_CHECKS`

优化时禁用运行时安全检查。

### Const value emission protocol list

**设置名称：** `SWIFT_EMIT_CONST_VALUE_PROTOCOLS`

一个协议名称列表，Swift 编译器将为其一致性输出编译期已知的值。

### Use Compiler to Extract Swift Strings

**设置名称：** `SWIFT_EMIT_LOC_STRINGS`

启用后，本地化导出期间将使用 Swift 编译器提取 Swift 字符串字面量以及插值 `LocalizedStringKey` 和 `LocalizationKey` 类型。

### Bare Slash Regex Literals

**设置名称：** `SWIFT_ENABLE_BARE_SLASH_REGEX`

启用正则表达式的正斜杠语法（`/.../`）。在 Swift 6 语言模式下始终启用此功能。

### Emit Swift const values

**设置名称：** `SWIFT_ENABLE_EMIT_CONST_VALUES`

从 Swift 编译器输出提取出的编译期已知值（-emit-const-values）

### Explicitly Built Modules

**设置名称：** `SWIFT_ENABLE_EXPLICIT_MODULES`

通过构建系统调度的显式任务，协调主模块模块化依赖项的构建。

### Exclusive Access to Memory

**设置名称：** `SWIFT_ENFORCE_EXCLUSIVE_ACCESS`

在运行时强制执行独占访问。

### Module Import Paths

**设置名称：** `SWIFT_INCLUDE_PATHS`

Swift 编译器用于搜索附加 Swift 模块的路径列表。

### Install Swift Module

**设置名称：** `SWIFT_INSTALL_MODULE`

对于框架，安装 Swift 模块，以便使用该框架的 Swift 代码可以访问它。

### Install Generated Header

**设置名称：** `SWIFT_INSTALL_OBJC_HEADER`

对于框架，将描述桥接 Swift 类型的 C++/Objective-C 生成头文件安装到 `PUBLIC_HEADERS_FOLDER_PATH` 中，以便使用该框架的 Objective-C 或 C++ 代码可以访问它们。默认值为 `YES`。

### Link Frameworks and Libraries Automatically

**设置名称：** `SWIFT_MODULES_AUTOLINK`

自动链接通过 `import` 引用的框架和库。

### Bridging Header

**设置名称：** `SWIFT_OBJC_BRIDGING_HEADER`

定义要在 Swift 中暴露的 C 接口的头文件路径。

### Generated Header Name

**设置名称：** `SWIFT_OBJC_INTERFACE_HEADER_NAME`

用于 Swift 编译器生成的头文件的名称，该头文件供 Objective-C 或 C++ 中的 `#import` 语句使用。

### C++ and Objective-C Interoperability

**设置名称：** `SWIFT_OBJC_INTEROP_MODE`

确定 Swift 除了能与 Objective-C 互操作外，是否还能与 C++ 互操作。

### Optimization Level

**设置名称：** `SWIFT_OPTIMIZATION_LEVEL`

- _None：_ 不进行任何优化地编译。[-Onone]
- _Optimize for Speed：_ [-O]
- _Optimize for Size：_ [-Osize]
- _Whole Module Optimization：_ [-O -whole-module-optimization]

### Package Access Identifier

**设置名称：** `SWIFT_PACKAGE_NAME`

一个标识符，允许将具有 package 访问修饰符的符号访问权限的模块分组。

### Precompile Bridging Header

**设置名称：** `SWIFT_PRECOMPILE_BRIDGING_HEADER`

如果使用了 Objective-C 桥接头文件，为其生成一个预编译头文件，以缩短总体构建时间。

### Reflection Metadata Level

**设置名称：** `SWIFT_REFLECTION_METADATA_LEVEL`

此设置控制 Swift 编译器输出的反射元数据级别。

- _All：_ 关于 Swift 结构体和类的存储属性、Swift 枚举 case 及其名称的类型信息，会被输出到二进制文件中，供 Memory Graph Debugger 进行反射和分析。
- _Without Names：_ 只有关于存储属性和 case 的类型信息会被输出到二进制文件中，其名称会被省略。[-disable-reflection-names]
- _None：_ 不会向二进制文件中输出任何反射元数据。在 Memory Graph Debugger 中检测涉及 Swift 类型的内存问题的准确性将会降低，Swift 代码中的反射可能无法发现类型的子项，例如属性和枚举 case。[-disable-reflection-metadata]

### Skip Automatically Linking All Frameworks

**设置名称：** `SWIFT_SKIP_AUTOLINKING_ALL_FRAMEWORKS`

启用后，不会自动链接任何通过 `import` 引用的框架。

### Skip Automatically Linking Frameworks

**设置名称：** `SWIFT_SKIP_AUTOLINKING_FRAMEWORKS`

一个框架名称列表，当这些框架通过 `import` 引用时不应被自动链接。

### Skip Automatically Linking Libraries

**设置名称：** `SWIFT_SKIP_AUTOLINKING_LIBRARIES`

一个库名称列表，当这些库通过 `import` 引用时不应被自动链接。

### Strict Concurrency Checking

**设置名称：** `SWIFT_STRICT_CONCURRENCY`

启用严格并发检查，为可能的数据争用生成警告。在 Swift 6 语言模式下，此设置始终为“complete”，并生成错误而非警告。

### Strict Memory Safety

**设置名称：** `SWIFT_STRICT_MEMORY_SAFETY`

启用严格内存安全检查。这会为每处未通过 `unsafe` 或 `@unsafe` 确认的不安全语言构造或 API 的使用生成警告。

### Suppress Warnings

**设置名称：** `SWIFT_SUPPRESS_WARNINGS`

不发出任何警告。

### System Module Import Paths

**设置名称：** `SWIFT_SYSTEM_INCLUDE_PATHS`

Swift 编译器用于搜索附加系统 Swift 模块的路径列表。系统模块中发现的警告不会被发出。

### Treat Warnings as Errors

**设置名称：** `SWIFT_TREAT_WARNINGS_AS_ERRORS`

将所有警告当作错误处理。

### Concise Magic File

**设置名称：** `SWIFT_UPCOMING_FEATURE_CONCISE_MAGIC_FILE`

将 #file 更改为求值为形如 `<module-name>/<file-name>` 的字符串字面量，现有行为则保留在新的 #filePath 中。在 Swift 6 语言模式下始终启用此功能。

### Deprecate Application Main

**设置名称：** `SWIFT_UPCOMING_FEATURE_DEPRECATE_APPLICATION_MAIN`

使任何对 `@UIApplicationMain` 或 `@NSApplicationMain` 的使用产生警告（请改用 `@main`）。在 Swift 6 语言模式下始终启用此功能，且产生的是错误而非警告。

### Disable Outward Actor Isolation Inference

**设置名称：** `SWIFT_UPCOMING_FEATURE_DISABLE_OUTWARD_ACTOR_ISOLATION`

移除属性包装器上推断出的 Actor 隔离推断。在 Swift 6 语言模式下始终启用此功能。

### Dynamic Actor Isolation

**设置名称：** `SWIFT_UPCOMING_FEATURE_DYNAMIC_ACTOR_ISOLATION`

为同步隔离函数启用运行时 Actor 隔离检查。在 Swift 6 语言模式下始终启用此功能。

### Require Existential any

**设置名称：** `SWIFT_UPCOMING_FEATURE_EXISTENTIAL_ANY`

将既存类型更改为要求使用 `any` 关键字显式注解。

### Forward Trailing Closures

**设置名称：** `SWIFT_UPCOMING_FEATURE_FORWARD_TRAILING_CLOSURES`

更新尾随闭包的求值方式，使参数按正向而非反向匹配。在 Swift 6 语言模式下始终启用此功能。

### Global-Actor-Isolated Types Usability

**设置名称：** `SWIFT_UPCOMING_FEATURE_GLOBAL_ACTOR_ISOLATED_TYPES_USABILITY`

为全局 Actor 隔离类型启用新的并发检查规则。在 Swift 6 语言模式下始终启用此功能。

### Isolated Global Variables

**设置名称：** `SWIFT_UPCOMING_FEATURE_GLOBAL_CONCURRENCY`

为既未隔离到全局 Actor、又不是同时满足不可变和 Sendable 的全局变量添加警告。在 Swift 6 语言模式下始终启用此功能，且产生的是错误而非警告。

### Implicitly Opened Existentials

**设置名称：** `SWIFT_UPCOMING_FEATURE_IMPLICIT_OPEN_EXISTENTIALS`

在需要泛型的地方启用传入既存类型。在 Swift 6 语言模式下始终启用此功能。

### Import Objective-C Forward Declarations

**设置名称：** `SWIFT_UPCOMING_FEATURE_IMPORT_OBJC_FORWARD_DECLS`

合成占位类型，以表示前向声明的 Objective-C 接口和协议。在 Swift 6 语言模式下始终启用此功能。

### Infer Isolated Conformances

**设置名称：** `SWIFT_UPCOMING_FEATURE_INFER_ISOLATED_CONFORMANCES`

推断全局 Actor 隔离类型的一致性隔离到同一个 Actor，除非显式将隔离指定为 `nonisolated`。

### Infer Sendable for Methods and Key Path Literals

**设置名称：** `SWIFT_UPCOMING_FEATURE_INFER_SENDABLE_FROM_CAPTURES`

为部分应用和未应用的方法添加可发送性（sendability）推断，并允许指定某个键路径字面量是否为 Sendable。在 Swift 6 语言模式下始终启用此功能。

### Default Internal Imports

**设置名称：** `SWIFT_UPCOMING_FEATURE_INTERNAL_IMPORTS_BY_DEFAULT`

将模块 import 的默认可访问性从 `public` 切换为 `internal`。

### Isolated Default Values

**设置名称：** `SWIFT_UPCOMING_FEATURE_ISOLATED_DEFAULT_VALUES`

为默认值添加 Actor 隔离，使其与所在的函数或存储属性保持一致。在 Swift 6 语言模式下始终启用此功能。

### Member Import Visibility

**设置名称：** `SWIFT_UPCOMING_FEATURE_MEMBER_IMPORT_VISIBILITY`

要求必须直接导入某个模块，其成员声明才可被访问。

### Nonfrozen Enum Exhaustivity

**设置名称：** `SWIFT_UPCOMING_FEATURE_NONFROZEN_ENUM_EXHAUSTIVITY`

在对非冻结枚举进行 switch、且没有 `@unknown default` case 时启用错误。在 Swift 6 语言模式下始终启用此功能。

### nonisolated(nonsending) By Default

**设置名称：** `SWIFT_UPCOMING_FEATURE_NONISOLATED_NONSENDING_BY_DEFAULT`

默认在调用者的 Actor 上运行 nonisolated 异步函数，除非该函数被显式标记为 `@concurrent`。

### Region Based Isolation

**设置名称：** `SWIFT_UPCOMING_FEATURE_REGION_BASED_ISOLATION`

在没有并发访问可能性的情况下，启用跨隔离边界传递非 Sendable 值。在 Swift 6 语言模式下始终启用此功能。

### Swift Language Version

**设置名称：** `SWIFT_VERSION`

用于编译该 target Swift 代码的语言版本。

### Diagnostic Groups Treated as Errors

**设置名称：** `SWIFT_WARNINGS_AS_ERRORS_GROUPS`

指定应被当作错误处理的诊断组（格式：“”）

### Diagnostic Groups Remain Warnings

**设置名称：** `SWIFT_WARNINGS_AS_WARNINGS_GROUPS`

指定应保持为警告的诊断组（格式：“”）

### Module name

**设置名称：** `SYMBOL_GRAPH_EXTRACTOR_MODULE_NAME`

要提取的主模块的名称。

### Output directory

**设置名称：** `SYMBOL_GRAPH_EXTRACTOR_OUTPUT_DIR`

符号图 JSON 输出目录。

### Build Products Path

**设置名称：** `SYMROOT`

执行构建时放置所有产品的路径。通常不会按 target 设置此路径，而是按项目或按用户设置。默认情况下，此值设为 `$(PROJECT_DIR)/build`。

### System Framework Search Paths

**设置名称：** `SYSTEM_FRAMEWORK_SEARCH_PATHS`

这是一个文件夹路径列表，这些文件夹中包含系统框架，编译 C、Objective-C、C++ 或 Objective-C++ 时，编译器会在其中搜索被包含或导入的头文件，链接器也会在其中搜索产品所使用的框架。顺序从高优先级到低优先级。路径之间以空白分隔，因此任何包含空格的路径都需要正确加引号。此设置与“Framework Search Paths”非常相似，区别在于这些搜索路径传递给编译器的方式，会抑制在系统搜索路径中找到的头文件所产生的大多数警告。如果编译器不支持系统框架搜索路径这一概念，这些搜索路径会被追加到“Framework Search Paths”中定义的任何现有框架搜索路径之后。

### System Header Search Paths

**设置名称：** `SYSTEM_HEADER_SEARCH_PATHS`

这是一个文件夹路径列表，编译 C、Objective-C、C++ 或 Objective-C++ 时，编译器会在其中搜索被包含或导入的系统头文件。顺序从高优先级到低优先级。路径之间以空白分隔，因此任何包含空格的路径都需要正确加引号。此设置与“Header Search Paths”非常相似，区别在于头文件传递给编译器的方式，会抑制在系统搜索路径中找到的头文件所产生的大多数警告。如果编译器不支持系统头文件搜索路径这一概念，这些搜索路径会被追加到“Header Search Paths”中定义的任何现有头文件搜索路径之后。

### Text-Based InstallAPI Demangle Symbols

**设置名称：** `TAPI_DEMANGLE`

构建 `Text-Based InstallAPI` 时显示反重整（demangle）后的符号。

### Enable Text-Based InstallAPI for Project Headers

**设置名称：** `TAPI_ENABLE_PROJECT_HEADERS`

构建 `Text-Based InstallAPI` 时包含项目级头文件。

### Exclude Private Header Paths

**设置名称：** `TAPI_EXCLUDE_PRIVATE_HEADERS`

构建 `Text-Based InstallAPI` 时，从该 target 中移除私有级头文件。

### Exclude Project Header Paths

**设置名称：** `TAPI_EXCLUDE_PROJECT_HEADERS`

构建 `Text-Based InstallAPI` 时，从该 target 中移除项目级头文件。

### Exclude Public Header Paths

**设置名称：** `TAPI_EXCLUDE_PUBLIC_HEADERS`

构建 `Text-Based InstallAPI` 时，从该 target 中移除公共级头文件。

### Extra Private Header Paths

**设置名称：** `TAPI_EXTRA_PRIVATE_HEADERS`

构建 `Text-Based InstallAPI` 时，添加来自其他 target 的私有级头文件。

### Extra Project Header Paths

**设置名称：** `TAPI_EXTRA_PROJECT_HEADERS`

构建 `Text-Based InstallAPI` 时，添加来自其他 target 的项目级头文件。

### Extra Public Header Paths

**设置名称：** `TAPI_EXTRA_PUBLIC_HEADERS`

构建 `Text-Based InstallAPI` 时，添加来自其他 target 的公共级头文件。

### Text-Based InstallAPI Language Mode

**设置名称：** `TAPI_LANGUAGE`

构建 `Text-Based InstallAPI` 时选择语言模式。

### Text-Based InstallAPI Language Dialect

**设置名称：** `TAPI_LANGUAGE_STANDARD`

构建 `Text-Based InstallAPI` 时选择语言方言。

### Text-Based InstallAPI Verification Mode

**设置名称：** `TAPI_VERIFY_MODE`

构建 `Text-Based InstallAPI` 时选择要报告的警告和错误级别。

### Targeted Device Families

**设置名称：** `TARGETED_DEVICE_FAMILY`

一个逗号分隔的整数列表，对应此 target 所支持的设备系列。

构建系统使用此信息为它添加到该 target `Info.plist` 文件中的 `UIDeviceFamily` 键设置正确的值。不适用于当前平台的值会被自动移除。这也驱动传给 actool 的 `--target-device` 标志，该标志决定了目录编译期间所选用的界面习惯（idiom）。

可能的值包括：

- **1**：iPhone、iPod touch
- **2**：iPad、使用“Scaled to Match iPad”界面的 Mac Catalyst
- **3**：Apple TV
- **4**：Apple Watch
- **6**：使用“Optimize for Mac”界面的 Mac Catalyst
- **7**：Apple Vision

### TARGET_BUILD_DIR

**设置名称：** `TARGET_BUILD_DIR`

标识包含产品文件（不含中间构建文件）的目录层级结构的根。对定义该 target 的产品文件进行操作的 Run Script 构建阶段应使用此构建设置的值，而对其他 target 的产品文件进行操作的 Run Script 构建阶段则应改用 `BUILT_PRODUCTS_DIR`。

### Target Name

**设置名称：** `TARGET_NAME`

当前 target 的名称。

### TARGET_TEMP_DIR

**设置名称：** `TARGET_TEMP_DIR`

标识包含该 target 中间构建文件的目录。Run Script 构建阶段应将中间文件放置在 `DERIVED_FILE_DIR` 所指示的位置，而不是此构建设置所标识的目录。

### Test Host

**设置名称：** `TEST_HOST`

测试包被注入其中的可执行文件的路径。仅在测试某个应用程序或其他可执行文件时指定此设置。

### Treat missing baselines as test failures

**设置名称：** `TREAT_MISSING_BASELINES_AS_TEST_FAILURES`

运行通过 `XCTestCase` 测量性能的测试时，将缺失的基线报告为测试失败。

### Treat Missing Script Phase Outputs as Errors

**设置名称：** `TREAT_MISSING_SCRIPT_PHASE_OUTPUTS_AS_ERRORS`

启用此选项会使因缺少输出的脚本阶段而导致的增量构建性能问题警告被当作错误处理。

### Unexported Symbols File

**设置名称：** `UNEXPORTED_SYMBOLS_FILE`

一个相对于项目的路径，指向一个列出不要导出符号的文件。有关导出符号的详情，请参阅 `ld -exported_symbols_list`。

### UNLOCALIZED_RESOURCES_FOLDER_PATH

**设置名称：** `UNLOCALIZED_RESOURCES_FOLDER_PATH`

指定包含产品未本地化资源的目录。

### User Header Search Paths

**设置名称：** `USER_HEADER_SEARCH_PATHS`

这是一个文件夹路径列表，编译 C、Objective-C、C++ 或 Objective-C++ 时，编译器会在其中搜索被包含或导入的用户头文件（那些用引号列出的头文件）。路径之间以空白分隔，因此任何包含空格的路径都需要正确加引号。有关此设置如何使用的更多详情，请参阅 `ALWAYS_SEARCH_USER_PATHS`。如果编译器不支持用户头文件这一概念，这些搜索路径会被添加到 `HEADER_SEARCH_PATHS` 中定义的任何现有头文件搜索路径之前。

### Use Header Maps

**设置名称：** `USE_HEADERMAP`

启用 _Header Map_（头文件映射）的使用，它为编译器提供从文本头文件名称到其位置的映射，绕过编译器正常的头文件搜索路径机制。这使得源代码可以包含来自文件系统中不同位置的头文件，而无需更新头文件搜索路径构建设置。

### Validate Built Product

**设置名称：** `VALIDATE_PRODUCT`

如果启用，作为构建过程的一部分，对产品执行验证检查。

### VERBOSE_PBXCP

**设置名称：** `VERBOSE_PBXCP`

指定该 target 的 Copy Files 构建阶段在复制文件时是否生成附加信息。

### Versioning System

**设置名称：** `VERSIONING_SYSTEM`

选择用于为生成文件加盖版本戳的流程。

- _None：_ 不使用版本控制系统。
- _Apple Generic：_ 使用当前项目版本设置。[apple-generic]
- _Apple Generic (Hidden Symbols)：_ 使用当前项目版本设置，并采用隐藏可见性的符号。[apple-generic-hidden]

### Versioning Username

**设置名称：** `VERSION_INFO_BUILDER`

这定义了要包含在生成的 Apple Generic Versioning 桩中的、对执行构建用户的引用。默认值为 `USER` 环境变量的值。

### Generated Versioning Variables

**设置名称：** `VERSION_INFO_EXPORT_DECL`

这为生成的 Apple Generic Versioning 桩中的版本信息符号声明定义了一个前缀字符串。例如，可以用它为版本符号声明添加一个可选的 `export` 关键字。这个设置很少需要改动。

### Generated Versioning Source Filename

**设置名称：** `VERSION_INFO_FILE`

用于为 Apple Generic Versioning 生成、并编译进你产品中的源文件指定一个名称。默认情况下，此值设为 `$(PRODUCT_NAME)_vers.c`。

### Versioning Name Prefix

**设置名称：** `VERSION_INFO_PREFIX`

用作生成的版本控制源文件中版本信息符号名称的前缀。如果你为导出的符号加了前缀，你可能会希望将此设置为相同的前缀。

### Versioning Name Suffix

**设置名称：** `VERSION_INFO_SUFFIX`

用作生成的版本控制源文件中版本信息符号名称的后缀。这个设置很少使用。

### Other Warning Flags

**设置名称：** `WARNING_CFLAGS`

传递给编译器的其他警告标志的空格分隔列表。如果 Xcode 尚未为某个特定的编译器警告标志提供界面，请使用此设置。

### Wrapper Extension

**设置名称：** `WRAPPER_EXTENSION`

用于产品包装器的扩展名，其默认值基于产品类型确定。

### WRAPPER_NAME

**设置名称：** `WRAPPER_NAME`

指定产品 Bundle 的文件名，包括相应的扩展名。

### WRAPPER_SUFFIX

**设置名称：** `WRAPPER_SUFFIX`

指定产品 Bundle 名称的后缀，包括将扩展名与 Bundle 名称其余部分分隔开的字符。

### Other Yacc Flags

**设置名称：** `YACCFLAGS`

传递给 `yacc` 的其他标志的空格分隔列表。请务必对包含空格或特殊字符的参数（例如可能包含空格的路径名）进行反斜杠转义。如果 Xcode 尚未为某个 `yacc` 标志提供界面，请使用此设置。

### Generated File Stem

**设置名称：** `YACC_GENERATED_FILE_STEM`

用于 `yacc` 生成文件的文件主干（stem）。根据此设置的值，这些文件将被命名为 `<stem>.tab.c` 和 `<stem>.tab.h`。Standard（`y`）选项会使同一 target 中的所有 `yacc` 源文件生成相同的输出文件，因此不建议在包含多个 `yacc` 源文件的 target 中使用。

### Generate Debugging Directives

**设置名称：** `YACC_GENERATE_DEBUGGING_DIRECTIVES`

启用此选项会改变 `yacc` 生成的预处理器指令，使调试语句被纳入已编译的代码中。

### Insert #line Directives

**设置名称：** `YACC_INSERT_LINE_DIRECTIVES`

启用此选项会使 `yacc` 在生成的代码中插入 `#line` 指令。`#line` 指令使 C 编译器能够将生成代码中的错误与用户的原始代码关联起来。如果禁用此选项，用户在源文件中指定的 `#line` 指令仍会被保留。

## 另请参阅

### Build settings

- [Configuring the build settings of a target](configuring-the-build-settings-of-a-target.md) — 指定用于编译、链接并从 target 生成产品的选项，并识别从项目或系统继承的设置。
- [Adding a build configuration file to your project](adding-a-build-configuration-file-to-your-project.md) — 以纯文本文件的形式指定你项目的构建设置，并为调试构建和发行版构建提供不同的设置。
- [Identifying and addressing framework module issues](identifying-and-addressing-framework-module-issues.md) — 使用模块验证器检测并修复框架模块中的常见问题。
- [Understanding build product layout changes in Xcode](understanding-build-product-layout-changes.md)
