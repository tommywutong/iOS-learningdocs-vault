---
title: 资源编程指南
apple_id: 10000051i
resource_type: Guide
platform: watchOS|tvOS|iOS|macOS
topic: Data Management
technology: null
published: '2016-03-21'
source_url: https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/LoadingResources/Strings/Strings.html
archived_at: '2026-07-15T07:16:32.555473Z'
---
> 导航：[总目录](../../../README.md) · [文档](../../../_indexes/documentation.md) · [资源编程指南](About%20Resources.md)


[下一页](Image%2C%20Sound%2C%20and%20Video%20Resources.md)[上一页](Nib%20Files.md)

# 字符串资源

本地化（localization）过程中很重要的一环，是把应用程序显示的所有文本字符串都本地化。就其性质而言，位于 [nib 文件](https://developer.apple.com/library/archive/documentation/General/Conceptual/DevPedia-CocoaCore/NibFile.html#//apple_ref/doc/uid/TP40008195-CH34)中的字符串可以随 nib 文件的其余内容一起顺理成章地完成本地化。然而，嵌入在代码中的字符串必须先提取出来，本地化之后再重新插回代码中。为了简化这个过程——同时也让代码更易于维护——OS X 和 iOS 提供了所需的基础设施，把字符串从代码中分离出来，放进便于本地化的资源文件里。

包含可本地化字符串的资源文件被称为 _strings_ 文件，因为它们的文件扩展名是 `.strings`。你可以根据需要手动或以编程方式创建 strings 文件。标准的 strings 文件格式由一个或多个键值对以及可选的注释组成。一对键值中的键和值都是用双引号括起来、并以等号分隔的文本字符串。（你也可以对 strings 文件使用属性列表格式。这种情况下，顶层节点是一个字典，该字典的每个键值对就是一个字符串条目。）

清单 2-1 展示了一个简单的 strings 文件，其中包含用于默认语言的未本地化条目。当你需要显示某个字符串时，把等号左边的字符串传给某个可用的字符串加载例程。你拿回的是与之匹配的值字符串，其中包含最适合当前用户的文本译文。对于开发语言，通常键和值使用相同的字符串，但这并不是必须的。

__清单 2-1__  一个简单的 strings 文件

```
/* Insert Element 菜单项 */
"Insert Element" = "Insert Element";
/* 用于未知错误类型的错误字符串。 */
"ErrorString_1" = "An unknown error occurred.";
```

一个典型的应用程序针对每种本地化至少有一个 strings 文件，也就是在 [bundle](https://developer.apple.com/library/archive/documentation/General/Conceptual/DevPedia-CocoaCore/Bundle.html#//apple_ref/doc/uid/TP40008195-CH4) 的每个 `.lproj` 子目录中各有一个 strings 文件。默认 strings 文件的名称是 `Localizable.strings`，但你可以用任何你喜欢的文件名来创建 strings 文件。关于创建 strings 文件的更深入讨论，请参阅[创建字符串资源文件](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgeydambqga2tc2jninedmlktk42q)。

字符串资源（无论本地化与否）的加载最终依赖于 OS X 和 iOS 中的 bundle 与国际化支持。关于 bundle 的信息，请参阅 _[Bundle Programming Guide](../../Core%20Foundation/Bundle%20Programming%20Guide/Introduction.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgeydambqgezdg2i)_。关于国际化和本地化的更多信息，请参阅 _[Internationalization and Localization Guide](../../Mac%20OSX/Internationalization%20and%20Localization%20Guide/About%20Internationalization%20and%20Localization.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgeydambqge3tc2i)_。

虽然你可以手动创建 strings 文件，但很少有必要这么做。如果你用合适的字符串加载宏来编写代码，就可以使用 `genstrings` 命令行工具提取这些字符串，并为你创建出 strings 文件。

以下各节介绍如何组织你的源文件，以便于使用 `genstrings` 工具。关于该工具的详细信息，请参阅 `genstrings` 手册页。

在本地化应用程序界面时，并不是把应用程序用到的每个字符串都本地化才合适。翻译是一项成本高昂的工作，翻译那些用户永远看不到的字符串是在浪费时间和金钱。不会显示给用户的字符串，例如应用程序内部使用的通知名称，就不需要翻译。请看下面的例子：

```c
if (CFStringHasPrefix(value, CFSTR("-")) {    CFArrayAppendValue(myArray, value);};
```

在这个例子中，字符串“`-`”只在内部使用，用户永远看不到；因此它不需要放进 strings 文件。

下面的代码展示了另一个用户看不到的字符串的例子。字符串 `"%d %d %s"` 不需要本地化，因为用户永远看不到它，它也不会影响用户看到的任何内容。

```c
matches = sscanf(s, "%d %d %s", &first, &last, &other);
```

由于 nib 文件是单独本地化的，你不需要把已经位于 nib 文件内部的字符串包含进来。不过，你应该本地化的字符串包括以下这些：

- 以编程方式添加到窗口、面板、视图或控件上并随后显示给用户的字符串。这也包括你传给标准例程的字符串，比如那些用于显示警告框的例程。
- 以编程方式添加的菜单项标题字符串。例如，如果你为“撤销”菜单项使用了自定义字符串，这些字符串就应该放在 strings 文件中。
- 显示给用户的错误消息。
- 显示给用户的任何样板文字。
- 应用程序的信息属性列表（`Info.plist`）文件中的某些字符串；参阅 _[Runtime Configuration Guidelines](../../Mac%20OSX/Runtime%20Configuration%20Guidelines/Introduction.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgeydambqge3ta2i)_。
- 新建文件名和文档名。

Foundation 和 Core Foundation [框架](https://developer.apple.com/library/archive/documentation/General/Conceptual/DevPedia-CocoaCore/Framework.html#//apple_ref/doc/uid/TP40008195-CH56)定义了以下宏，让从 strings 文件加载字符串变得更简单：

- Core Foundation 宏：

  - [CFCopyLocalizedString](https://developer.apple.com/documentation/corefoundation/cfcopylocalizedstring)
  - [CFCopyLocalizedStringFromTable](https://developer.apple.com/documentation/corefoundation/cfcopylocalizedstringfromtable)
  - [CFCopyLocalizedStringFromTableInBundle](https://developer.apple.com/documentation/corefoundation/cfcopylocalizedstringfromtableinbundle)
  - [CFCopyLocalizedStringWithDefaultValue](https://developer.apple.com/documentation/corefoundation/cfcopylocalizedstringwithdefaultvalue)
- Foundation 宏：

  - [NSLocalizedString](https://developer.apple.com/documentation/foundation/nslocalizedstring)
  - [NSLocalizedStringFromTable](https://developer.apple.com/documentation/foundation/nslocalizedstringfromtable)
  - [NSLocalizedStringFromTableInBundle](https://developer.apple.com/documentation/foundation/nslocalizedstringfromtableinbundle)
  - [NSLocalizedStringWithDefaultValue](https://developer.apple.com/documentation/foundation/nslocalizedstringwithdefaultvalue)

你在源代码中使用这些宏，从应用程序的某个 strings 文件加载字符串。这些宏在检索实际字符串值时会考虑用户当前的语言偏好。此外，`genstrings` 工具会搜索这些宏，并利用其中包含的信息为你的应用程序构建出最初的一组 strings 文件。

关于如何使用这些宏的更多信息，请参阅[在代码中加载字符串资源](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgiydambqgaydkljzg4ydkni)。

在开发过程中的某个阶段，你需要创建代码所需的 strings 文件。如果你是用 Core Foundation 和 Foundation 的宏编写代码的，创建 strings 文件最简单的方式就是使用 `genstrings` 命令行工具。你可以用这个工具生成一组新的 strings 文件，或者根据源代码更新一组已有的文件。

使用 `genstrings` 工具时，你通常至少要提供两个参数：

- 一组源文件
- 一个可选的输出目录

`genstrings` 工具可以解析扩展名为 `.c`、`.m` 或 `.java` 的 C、[Objective-C](https://developer.apple.com/library/archive/documentation/General/Conceptual/DevPedia-CocoaCore/ObjectiveC.html#//apple_ref/doc/uid/TP40008195-CH43) 和 Java 代码文件。虽然并非严格必需，但建议指定输出目录，`genstrings` 会把生成的 strings 文件放到那里。多数情况下，你会希望指定包含开发语言工程资源的那个目录。

下面的例子展示了运行 `genstrings` 工具的一条简单命令。这条命令让工具解析当前目录下的所有 Objective-C 源文件，并把生成的 strings 文件放进 `en.lproj` 子目录，该子目录必须事先存在。

```bash
genstrings -o en.lproj *.m
```

第一次运行 `genstrings` 工具时，它会为你创建一组新的 strings 文件。后续运行则会用源代码中当前找到的字符串条目替换这些 strings 文件的内容。对于后续运行，最好在运行 `genstrings` 之前先保存一份当前 strings 文件的副本。这样你就可以对新旧版本做 diff，确定工程中新增了（或改动了）哪些字符串。接着你可以用这些信息去更新那些已经本地化过的 strings 文件版本，而不必替换掉它们再重新本地化一遍。

在同一个 strings 文件中，每个键必须唯一。所幸 `genstrings` 工具足够聪明，会合并它找到的重复条目。当它发现某个键字符串在同一个 strings 文件中被使用了多次时，会把各个条目的注释合并成一条注释字符串，并生成一个警告。（你可以用 `-q` 选项抑制重复条目警告。）如果相同的键字符串被赋给了不同 strings 文件中的字符串，则不会生成警告。

关于使用 `genstrings` 工具的更多信息，请参阅 `genstrings` 手册页。

虽然 `genstrings` 工具是创建 strings 文件最方便的方式，但你也可以手动创建它们。要手动创建 strings 文件，请在 TextEdit（或你偏好的文本编辑应用）中新建一个文件，并以 Unicode UTF-8 编码保存。（保存文件时，TextEdit 通常会默认选择合适的编码。要强制使用特定编码，你必须在应用程序偏好设置中修改保存选项。）该文件的内容由一组键值对以及描述每个键值对用途的可选注释组成。键字符串和值字符串以等号分隔，整个条目必须以分号字符结尾。按照惯例，注释用 C 风格的注释定界符（`/*` 和 `*/`）括起来，并紧放在它所描述的条目之前。

清单 2-2 展示了 strings 文件的基本格式。这个例子中的条目取自 TextEdit 应用程序 `Localizable.strings` 文件的英文版本。每个等号左边的字符串代表键，右边的字符串代表值。开发应用程序时的一个常见惯例是：让键名等于应用开发所用语言中的那个值。因此，由于 TextEdit 是用英语开发的，`Localizable.strings` 文件的英文版本中键和值是一致的。

__清单 2-2__  为英语本地化的字符串

```
/* 把当前文档转换为纯文本的菜单项 */
"Make Plain Text" = "Make Plain Text";
/* 把当前文档转换为富文本的菜单项 */
"Make Rich Text" = "Make Rich Text";
```

清单 2-3 展示了这些相同条目的德语译文。这些条目同样位于一个名为 `Localizable.strings` 的文件中，只不过这个版本的文件位于 TextEdit 应用程序的德语工程目录下。注意键仍然是英文的，但赋给这些键的值是德文的。这是因为键字符串永远不会被最终用户看到，它们供代码用来检索对应的值字符串——本例中值字符串是德文的。

__清单 2-3__  为德语本地化的字符串

```
/* 把当前文档转换为纯文本的菜单项 */
"Make Plain Text" = "In reinen Text umwandeln";
/* 把当前文档转换为富文本的菜单项 */
"Make Rich Text" = "In formatierten Text umwandeln";
```


基于 AppKit 的应用程序可以利用内置支持来检测哪些字符串不需要本地化，以及哪些字符串需要本地化却尚未本地化。要使用这项内置支持，可以在运行应用时设置用户默认项（user default）或添加启动参数。用一个布尔值来指明该用户默认项应当启用还是禁用。可用的用户默认项如下：

- `NSShowNonLocalizableStrings` 用户默认项用于识别不可本地化的字符串。这些字符串会以大写形式记录到 shell 中。这个选项偶尔会产生一些误报，但总体上仍然很有用。
- `NSShowNonLocalizedStrings` 用户默认项用于找出那些本应被本地化、却在应用程序现有 strings 文件中找不到的字符串。你可以用这个用户默认项来发现本地化过期的问题。

例如，要对 TextEdit 应用程序使用 `NSShowNonLocalizedStrings` 用户默认项，请在“终端”中输入以下内容：

```bash
/Applications/TextEdit.app/Contents/MacOS/TextEdit -NSShowNonLocalizedStrings YES
```


Core Foundation 和 Foundation 框架提供了一些宏，用于检索存放在 strings 文件中的本地化和未本地化字符串。虽然这些宏的主要用途是在运行时加载字符串，但它们还有第二个用途：充当标记，供 `genstrings` 工具定位应用程序的字符串资源。正是这第二个用途解释了为什么许多宏允许你指定的信息，远多于加载一个字符串通常所需的信息。`genstrings` 工具会用你提供的信息自动创建或更新应用程序的 strings 文件。表 2-1 列出了你可以为这些例程指定的信息类型，并说明 `genstrings` 工具如何使用这些信息。

__表 2-1__  字符串加载例程中常见的参数

| 参数 | 说明 |
| --- | --- |
| Key | 用于查找对应值的字符串。该字符串不得包含扩展 ASCII 字符集中的任何字符，其中包括带重音符号的 ASCII 字符变体。如果你希望初始的值字符串包含扩展 ASCII 字符，请使用允许你指定默认值参数的例程。（关于扩展 ASCII 字符集的信息，请参阅对应的 [Wikipedia 条目](http://en.wikipedia.org/wiki/Extended_ASCII)。） |
| Table name | 指定键所在的 strings 文件的名称。`genstrings` 工具会把这个参数解读为该字符串应被放入的 strings 文件的名称。如果没有提供表名，字符串会被放进默认的 `Localizable.strings` 文件。（为该参数指定值时，只写文件名，不带 `.strings` 扩展名。）  表名以 `.nocache` 结尾的 `.strings` 文件——例如 `ErrorNames.nocache.strings`——其内容不会被 [NSBundle](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSBundle/Description.html#//apple_ref/occ/cl/NSBundle) 缓存。 |
| Default value | 与给定键关联的默认值。如果没有指定默认值，`genstrings` 工具会用键字符串作为初始值。默认值字符串可以包含扩展 ASCII 字符。 |
| Comment | 随字符串一起包含的翻译注释。你可以用注释向翻译团队提示某个字符串的用途。`genstrings` 工具会把这些注释放进 strings 文件，用 C 风格的注释定界符（`/*` 和 `*/`）括起来，并紧放在关联条目的上方。 |
| Bundle | 与包含 strings 文件的 bundle 对应的 [NSBundle](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSBundle/Description.html#//apple_ref/occ/cl/NSBundle) 对象或 [CFBundleRef](https://developer.apple.com/documentation/corefoundation/cfbundle) 类型。你可以用它从应用程序主 bundle 以外的 bundle 加载字符串。例如，你可能用它从[框架](https://developer.apple.com/library/archive/documentation/General/Conceptual/DevPedia-CocoaCore/Framework.html#//apple_ref/doc/uid/TP40008195-CH56)或插件中加载本地化字符串。 |

当你从 strings 文件请求一个字符串时，返回的字符串取决于可用的本地化（如果有的话）。Cocoa 和 Core Foundation 的宏利用内置的 [bundle](https://developer.apple.com/library/archive/documentation/General/Conceptual/DevPedia-CocoaCore/Bundle.html#//apple_ref/doc/uid/TP40008195-CH4) 国际化支持，检索其本地化与用户当前语言偏好相匹配的字符串。只要你的本地化资源文件放在了合适的特定语言的工程目录中，用这些宏加载字符串就会自动得到合适的字符串。如果找不到合适的本地化字符串资源，bundle 的加载代码会自动改用合适的未本地化字符串。

关于国际化的总体信息以及如何创建特定语言的工程目录，请参阅 _[Internationalization and Localization Guide](../../Mac%20OSX/Internationalization%20and%20Localization%20Guide/About%20Internationalization%20and%20Localization.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgeydambqge3tc2i)_。关于 bundle 结构以及资源文件如何从 bundle 目录中被选取的信息，请参阅 _[Bundle Programming Guide](../../Core%20Foundation/Bundle%20Programming%20Guide/Introduction.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgeydambqgezdg2i)_。

Core Foundation 框架定义了一个函数和若干宏，用于从应用程序 bundle 加载本地化字符串。[CFBundleCopyLocalizedString](https://developer.apple.com/documentation/corefoundation/1537103-cfbundlecopylocalizedstring) 函数提供了检索字符串的基础实现。不过，建议你改用以下这些宏：

- [CFCopyLocalizedString](https://developer.apple.com/documentation/corefoundation/cfcopylocalizedstring)`(key, comment)`
- [CFCopyLocalizedStringFromTable](https://developer.apple.com/documentation/corefoundation/cfcopylocalizedstringfromtable)`(key, tableName, comment)`
- [CFCopyLocalizedStringFromTableInBundle](https://developer.apple.com/documentation/corefoundation/cfcopylocalizedstringfromtableinbundle)`(key, tableName, bundle, comment)`
- [CFCopyLocalizedStringWithDefaultValue](https://developer.apple.com/documentation/corefoundation/cfcopylocalizedstringwithdefaultvalue)`(key, tableName, bundle, value, comment)`

有好几个理由说明应该使用这些宏而不是 `CFBundleCopyLocalizedString` 函数。第一，对于某些常见场景，宏用起来更简单。第二，宏让你可以为字符串条目关联一条注释字符串。第三，`genstrings` 工具能识别这些宏，却无法识别 `CFBundleCopyLocalizedString` 函数。

关于上述宏的语法信息，请参阅 _[CFBundle Reference](https://developer.apple.com/documentation/corefoundation/cfbundle-s0a)_。

Foundation 框架定义了一个方法和若干宏，用于加载字符串资源。`NSBundle` 类的 [localizedStringForKey:value:table:](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSBundle/Description.html#//apple_ref/occ/instm/NSBundle/localizedStringForKey:value:table:) 方法从当前 bundle 中的 strings 文件加载指定的字符串资源。Cocoa 还定义了以下用于获取本地化字符串的宏：

- [NSLocalizedString](https://developer.apple.com/documentation/foundation/nslocalizedstring)`(key, comment)`
- [NSLocalizedStringFromTable](https://developer.apple.com/documentation/foundation/nslocalizedstringfromtable)`(key, tableName, comment)`
- [NSLocalizedStringFromTableInBundle](https://developer.apple.com/documentation/foundation/nslocalizedstringfromtableinbundle)`(key, tableName, bundle, comment)`
- [NSLocalizedStringWithDefaultValue](https://developer.apple.com/documentation/foundation/nslocalizedstringwithdefaultvalue)`(key, tableName, bundle, value, comment)`

和 Core Foundation 的情况一样，Apple 建议你使用 Cocoa 提供的便捷宏来加载字符串。这些宏的主要优势在于它们能被 `genstrings` 工具解析，用来创建应用程序的 strings 文件。它们用起来也更简单，并且让你可以为每个条目关联翻译注释。

关于上述宏的语法信息，请参阅 _Foundation Functions Reference_。_[NSBundle Class Reference](https://developer.apple.com/documentation/foundation/nsbundle)_ 中还定义了其他用于加载字符串的方法。

下面的例子演示了使用 Foundation 和 Core Foundation 宏检索字符串的基本方法。每个例子都假设当前 bundle 包含一个名为 `Custom.strings` 的 strings 文件，并且它已被翻译成法语。这个译文文件包含以下字符串：

```
/* A comment */
"Yes" = "Oui";
"The same text in English" = "Le même texte en anglais";
```

使用 Foundation 框架，你可以用 [NSLocalizedStringFromTable](https://developer.apple.com/documentation/foundation/nslocalizedstringfromtable) 宏获取“`Yes`”这个字符串的值，如下例所示：

```objc
NSString* theString;
theString = NSLocalizedStringFromTable (@"Yes", @"Custom", @"A comment");
```

使用 Core Foundation 框架，你可以用 [CFCopyLocalizedStringFromTable](https://developer.apple.com/documentation/corefoundation/cfcopylocalizedstringfromtable) 宏获取相同的字符串，如本例所示：

```c
CFStringRef theString;
theString = CFCopyLocalizedStringFromTable(CFSTR("Yes"), CFSTR("Custom"), "A comment");
```

在这两个例子中，代码都指定了要检索的键，也就是字符串“Yes”。它们还指定了在哪个 strings 文件（或表）中查找该键，本例中是 `Custom.strings` 文件。在检索字符串的过程中，注释字符串会被忽略。

以下各节提供了一些处理 strings 文件和字符串资源的额外提示。

`genstrings` 工具默认会搜索 Core Foundation 和 Foundation 的字符串宏。它用这些宏中的信息在工程的 strings 文件中创建字符串条目。你也可以指示 `genstrings` 在代码中查找自定义的字符串加载函数，并在标准宏之外一并使用这些函数。你可能会用自定义函数包装内置的字符串加载例程并执行一些额外处理，也可能用自己的自定义模型取代默认的字符串处理行为。

如果你想让 `genstrings` 配合自己的自定义函数使用，这些函数必须遵循 Foundation 宏所用的命名和格式约定。你的函数参数必须与对应宏的参数完全一致。调用 genstrings 时，你要指定 `-s` 选项，后面跟上与 [NSLocalizedString](https://developer.apple.com/documentation/foundation/nslocalizedstring) 宏相对应的那个函数的名称。你的其他函数名应当在这个基名之上构建。例如，如果你指定的函数名是 `MyStringFunction`，那么其他函数名就应该是 `MyStringFunctionFromTable`、`MyStringFunctionFromTableInBundle` 和 `MyStringFunctionWithDefaultValue`。`genstrings` 工具会查找这些函数，并用它们来构建对应的 strings 文件。

对于某些字符串，你可能不希望（或无法）把整个字符串都编码进一个字符串资源，因为字符串的某些部分可能在运行时发生变化。例如，如果一个字符串包含用户文档的名称，你就需要能够动态地把该文档名插入到字符串中。创建字符串资源时，你可以使用在 Foundation 和 Core Foundation 框架中处理字符串替换时通常会用的任何格式化字符。清单 2-4 展示了几个使用基本格式化字符的字符串资源：

__清单 2-4__  带格式化字符的字符串

```
"Windows must have at least %d columns and %d rows." =
"Les fenêtres doivent être composes au minimum de %d colonnes et %d lignes.";
"File %@ not found." = "Le fichier %@ n’existe pas.";
```

要用实际值替换格式化字符，你需要使用 `NSString` 的 [stringWithFormat:](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSStringClassCluster/Description.html#//apple_ref/occ/clm/NSString/stringWithFormat:) 方法或 [CFStringCreateWithFormat](https://developer.apple.com/documentation/corefoundation/1563243-cfstringcreatewithformat) 函数，把字符串资源当作格式字符串。Foundation 和 Core Foundation 支持 `printf` 语句中使用的大多数标准格式化字符。此外，你还可以使用前例中展示的 `%@` 说明符，插入与任意 Objective-C 对象关联的描述性文本。完整的说明符列表参见 _[String Programming Guide](../String%20Programming%20Guide/Introduction%20to%20String%20Programming%20Guide.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgeydambqgaztk2i)_ 中的 [Formatting String Objects](https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/Strings/Articles/FormatStrings.html#//apple_ref/doc/uid/20000943)。

翻译过程中经常出现的一个问题是：为了适应源语言和目标语言之间的差异，译者可能需要在译文字符串中重新排列参数的顺序。如果一个字符串包含多个参数，译者可以在格式化字符之间插入形如 _n_`$` 的特殊标记（其中 _n_ 指定原始参数的位置）。这些标记让译者可以重新排列原字符串中出现的参数。下面的例子展示了一个字符串，它的两个参数在译文字符串中调换了顺序：

```
/* 某项操作失败时在警告对话框中显示的消息 */
"%@ Error! %@ failed!" = "%2$@ blah blah, %1$@ blah!";
```


就像在 C 语言中一样，某些字符必须加上反斜杠前缀，才能包含到字符串里。这些字符包括双引号、反斜杠本身，以及诸如换行（`\n`）和回车（`\r`）之类的特殊控制字符。

```
"File \"%@\" cannot be opened" = " ... ";
"Type \"OK\" when done" = " ... ";
```

你可以在值字符串中包含任意 Unicode 字符，方法是写 `\U`，后面紧跟最多四个十六进制数字。这四个数字表示所需 Unicode 字符的编码；例如，空格字符用十六进制的 20 表示，因此作为 Unicode 字符指定时就写作 `\U0020`。如果某个字符串必须包含由于某些原因无法直接输入的 Unicode 字符，这个选项就很有用。使用这个选项时，你还必须给 `genstrings` 传入 `-u` 选项，这样生成的 strings 文件中的十六进制数字才能被正确解释。`genstrings` 工具默认假定你的字符串是低位 ASCII，只有指定了 `-u` 选项才会解释反斜杠序列。

如果你在测试中遇到问题，发现用于检索字符串的函数和宏总是返回键本身（而不是翻译后的值），请对你的 strings 文件运行 `/usr/bin/plutil` 工具。strings 文件本质上就是一个以特殊方式格式化的属性列表文件。用 `-lint` 选项运行 `plutil` 可以揭示出隐藏字符或其他导致字符串无法被正确检索的错误。

[下一页](Image%2C%20Sound%2C%20and%20Video%20Resources.md)[上一页](Nib%20Files.md)

