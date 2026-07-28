---
title: 在包中嵌入非标准代码结构
framework: xcode
symbol_kind: article
role: article
role_heading: Article
platforms: []
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/xcode/embedding-nonstandard-code-structures-in-a-bundle
source_url: 'https://developer.apple.com/documentation/xcode/embedding-nonstandard-code-structures-in-a-bundle'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/xcode/embedding-nonstandard-code-structures-in-a-bundle.json'
content_hash: 'sha256:edeb4c32557db35c'
translated: true
---

> 导航：[技术](../technologies.md) · [Xcode](../xcode.md) · [包与框架](bundles-and-frameworks.md)

# 在包中嵌入非标准代码结构

<sub>文章</sub>

使用以非标准方式构建的代码，同时避免代码签名与分发问题。

## 概述

所有 App——以及 Mac 上许多非 App 的软件产品，如插件——都以包（bundle）结构打包。在创建包时，请将内容放置在正确的位置。将内容放置在非标准位置可能导致代码签名与分发问题。详情请见[将内容放入包中](../bundleresources/placing-content-in-a-bundle.md)。

在某些情况下，你需要处理非标准代码结构，即其结构与你目标平台的标准包结构不匹配的代码。例如，你可能正在构建一个 Mac App，并想在其中嵌入一个开源语言运行时。如果该运行时的磁盘布局不遵循[将内容放入包中](../bundleresources/placing-content-in-a-bundle.md)的规则，你就会面临代码签名与分发问题的风险。

解决这一难题的最佳方案是重新构建代码，使其与你目标平台的包结构相匹配。但这并非总是可行：

- 这需要你对代码的构建系统有深入了解。如果你尚不熟悉，可能会花费大量时间来获取这些知识。
- 这仅在产品是开源的情况下才有效。

幸运的是，还有另一种方法。本文档将通过一个示例，逐步向你展示如何在不重新构建所有代码的情况下，将非标准代码结构嵌入到你的包中。虽然示例针对 Mac，但其基本技术适用于所有 Apple 平台。

> [!important] 重要
> 这只是一个示例。你所使用的代码，其结构很可能与本例不同。请根据你的具体情况，调整此处展示的技术。

### 分离只读与可读写内容

包是一个只读结构。除 Mac 外，所有 Apple 平台都在运行时强制执行此要求。例如，在 iOS 上，任何在运行时修改你的 App 包的尝试都会失败并报错。Mac 可能会也可能不会在运行时强制执行此要求，这取决于上下文，但修改你的 App 包是不受支持的，因为这会破坏 App 代码签名的密封性。

起源于其他平台的代码结构并不总是与此要求兼容。例如，Python 运行时会与原始 Python 源文件在同一目录下写入字节码文件。假设你有一个名为 `WaffleVarnish.py` 的文件，运行时可能会在该目录中写入一个名为 `WaffleVarnish.pyc`（或 `WaffleVarnish.pyo`）的文件。这会导致两个问题：

- 如果平台阻止此写入，你将错失这些字节码文件带来的性能优势。
- 如果平台未阻止此写入，该写入会破坏 App 代码签名的密封性。

如果你使用的代码以这种方式工作，请设法分离其只读内容（可安全放入包中）和可读写内容（不能放入包中）。具体细节取决于所讨论的代码，但这通常涉及设置一个指向可写位置（例如在资源库（Library）目录中）的命令行参数或环境变量。

### 调查动态库链接

想象一下，你正在构建一个用于给华夫饼上光的 Mac App，并希望使用出色的开源 libWaffleVarnish 代码。其构建系统输出的目录结构如下：

```
libWaffleVarnish/
  bin/
    wafflevarnish
  etc/
    wafflevarnish.config
  lib/
    libVarnish.dylib
    libWaffle.dylib
```

`wafflevarnish` 工具依赖于这两个动态库。`libVarnish.dylib` 库依赖于 `libWaffle.dylib`。`wafflevarnish` 工具还会读取 `wafflevarnish.config` 配置文件。

好消息是，libWaffleVarnish 的结构使其易于重定位。`wafflevarnish` 工具通过一个指向 `lib` 目录的可执行文件相对路径来设置 rpath 上下文：

```
% otool -l libWaffleVarnish/bin/wafflevarnish | grep -B 1 -A 2 LC_RPATH 
Load command 15
          cmd LC_RPATH
      cmdsize 40
         path @executable_path/../lib …
```

并且 `wafflevarnish` 和 `libVarnish.dylib` 都使用 rpath 相对引用来引用其动态库依赖：

```
% otool -L "libWaffleVarnish/bin/wafflevarnish"
…
    @rpath/libVarnish.dylib …
    @rpath/libWaffle.dylib …
    …
% otool -L "libWaffleVarnish/lib/libVarnish.dylib"
…
    @rpath/libVarnish.dylib …
    @rpath/libWaffle.dylib …
    …
% otool -L "libWaffleVarnish/lib/libWaffle.dylib"
…
    @rpath/libWaffle.dylib …
    …
```

关于 rpath 机制的更多信息，请参阅 `dyld` 手册页。如果你不熟悉阅读手册页，请参阅[阅读 UNIX 手册页](../os/reading-unix-manual-pages.md)。

通过这种设置，可以轻松地将该工具及其库以最小的改动放入你的包中。如果你使用的代码就是以这种方式构建的，请跳转至[在包内正确位置放置内容](embedding-nonstandard-code-structures-in-a-bundle.md#Place-content-in-the-correct-location-within-the-bundle)。

### 采用 rpath 相对引用

并非所有非标准结构的代码都像 libWaffleVarnish 那样易于调整。例如，libRubPat 的构建系统使用绝对路径来表达其依赖：

```
% otool -L "libRubPat/bin/rubpat"
…
    /usr/local/libRubPat/lib/libPat.dylib …
    /usr/local/libRubPat/lib/libRub.dylib …
    …
% otool -L "libRubPat/lib/libPat.dylib"
…
    /usr/local/libRubPat/lib/libPat.dylib …
    /usr/local/libRubPat/lib/libRub.dylib …
    …
% otool -L "libRubPat/lib/libRub.dylib"
…
    /usr/local/libRubPat/lib/libRub.dylib …
    …
```

该工具及其关联的动态库仅在安装于 `/usr/local/libRubPat` 时才能工作，因此你无法按原样将此代码嵌入到你的包中。

> [!note] 注意
> 完全基于 rpath 相对路径的 libWaffleVarnish，与完全基于绝对路径的 libRubPat，并非仅有的两种可能。许多非标准代码结构混合使用了绝对路径、相对路径、可执行文件相对路径（`@executable_path`）、加载器相对路径（`@loader_path`）和 rpath 相对路径（`@rpath`）。解决这个问题可能颇具挑战性。

解决此问题的最佳方法是更新代码的构建系统以使用 rpath 相对引用。然而，对于 libRubPat 来说这是不可能的，因为该库并非开源。要将 libRubPat 嵌入你的包中，可以使用 `install_name_tool` 来更改嵌入在其代码项中的路径。首先，移除所有代码签名：

```
% codesign --remove-signature "libRubPat/lib/libRub.dylib"
% codesign --remove-signature "libRubPat/lib/libPat.dylib"
% codesign --remove-signature "libRubPat/bin/rubpat"
```

使用 `install_name_tool` 更改代码会破坏其代码签名的密封性，`install_name_tool` 也会对此发出警告。作为分发过程的一部分，你将会重新签署这些代码，因此不如直接处理未签名的代码，以避免大量警告。

现在，将每个库的动态库标识符更改为 rpath 相对形式：

```
% install_name_tool -id "@rpath/libRub.dylib" "libRubPat/lib/libRub.dylib"
% install_name_tool -id "@rpath/libPat.dylib" "libRubPat/lib/libPat.dylib"
```

这控制了库向系统其余部分标识自身的方式。

接下来，更改每个动态库依赖以使其匹配：

```
% install_name_tool -change "/usr/local/libRubPat/lib/libRub.dylib" "@rpath/libWaffle.dylib" "libRubPat/lib/libPat.dylib"
% install_name_tool -change "/usr/local/libRubPat/lib/libRub.dylib" "@rpath/libWaffle.dylib" "libRubPat/bin/rubpat"
% install_name_tool -change "/usr/local/libRubPat/lib/libPat.dylib" "@rpath/libVarnish.dylib" "libRubPat/bin/rubpat"
```

最后，为该工具添加一个可执行文件相对路径的 rpath：

```
% install_name_tool -add_rpath "@executable_path/../lib" "libRubPat/bin/rubpat"
```

要确认你已修复所有依赖，可像处理 libWaffleVarnish 时一样运行 `otool`：

```
% otool -l libRubPat/bin/rubpat | grep -B 1 -A 2 LC_RPATH 
Load command 17
          cmd LC_RPATH
      cmdsize 40
         path @executable_path/../lib (offset 12)

% otool -L "libRubPat/bin/rubpat"
…
    @rpath/libPat.dylib …
    @rpath/libRub.dylib …
    …
% otool -L "libRubPat/lib/libPat.dylib"
…
    @rpath/libPat.dylib …
    @rpath/libRub.dylib …
    …
% otool -L "libRubPat/lib/libRub.dylib"
…
    @rpath/libRub.dylib …
    …
```

最终结果是一个所有动态库依赖都是 rpath 相对形式，且工具自身的 rpath 条目为可执行文件相对形式的代码结构。无论该结构在磁盘上位于何处，此结构都能正常工作，这使得将其嵌入到你的包中变得可行。

### 在包内正确位置放置内容

一旦你确认代码使用了 rpath 相对路径，就可以将其嵌入到你的包中了。设想你正在构建一个名为 MacWaffleVarnish 的 App。[将内容放入包中](../bundleresources/placing-content-in-a-bundle.md)中的规则要求使用以下结构：

```
MacWaffleVarnish.app/
  Contents/
    Info.plist
    MacOS/
      MacWaffleVarnish
      wafflevarnish
    Frameworks/
      libVarnish.dylib
      libWaffle.dylib
    Resources/
      … other resources …
      libWaffleVarnish/
        etc/
          wafflevarnish.config
```

动态库位于 `Contents/Frameworks` 中，工具在 `Contents/MacOS` 中，配置文件在 `Contents/Resources` 中。

要实现此目的，请使用 `install_name_tool` 调整 `wafflevarnish` 工具中的 rpath 条目，使其指向 Frameworks 目录而非 lib 目录：

```
% install_name_tool -rpath "@executable_path/../lib" "@executable_path/../Frameworks" "wafflevarnish"
```

这就是你需要做的一切。libWaffleVarnish 中对 rpath 相对引用的使用，使得更改其代码结构以匹配平台约定变得容易。

### 对棘手的边界情况使用符号链接

这里还有最后一个陷阱。如果你运行 `wafflevarnish` 工具，你会看到这个错误：

```
% MacWaffleVarnish.app/Contents/MacOS/wafflevarnish
MacWaffleVarnish.app/Contents/MacOS/../etc/wafflevarnish.config: No such file or directory
…
```

它试图通过一个相对于可执行文件的路径来访问 `wafflevarnish.config`，但因为你移动了文件，该配置文件在该相对路径下已不再可用。在许多情况下，工具会提供通过命令行参数或环境变量来设置其配置路径的方法。如果没有，可通过符号链接（symlink）来解决此问题：

```
MacWaffleVarnish.app/
  Contents/
    …
    MacOS/
      …
      wafflevarnish
    …
    Resources/
      …
      libWaffleVarnish/
        bin/
          wafflevarnish -> ../../MacOS/wafflevarnish
        etc/
          wafflevarnish.config
```

现在，如果你通过符号链接运行 `wafflevarnish` 工具，它就能找到配置文件，一切正常：

```
% MacWaffleVarnish.app/Contents/Resources/libWaffleVarnish/bin/wafflevarnish
configuration:
  finish: gloss
…
```

符号链接是一种处理棘手边界情况的强大技术。例如，如果代码通过一个指向无法存放代码位置的相对路径动态加载插件，可在该位置创建一个符号链接，指向代码实际存放的位置。

你还可以使用符号链接来减少必须使用 `install_name_tool` 重写的动态库依赖的数量。设想你正在处理一个拥有大量库间依赖的巨大代码结构。与其重写所有这些依赖，不如将整个代码结构一并嵌入，然后将每个代码项移动到包内适当的位置，同时在其原位置留下一个符号链接。

然而，在大多数情况下，重写所有内容以使用 rpath 相对引用会更简单、也更好。

## 另请参阅

### 包

- [将内容放入包中](../bundleresources/placing-content-in-a-bundle.md) — 根据包内容的类型，将其放置在正确的位置。
- [管理 App 的信息属性列表值](../bundleresources/managing-your-app-s-information-property-list.md) — 使用 Xcode 自定义 App 的信息属性列表值。
- [编辑属性列表文件](editing-property-list-files.md) — 在结构化文件中添加、移除和更改键与值。
