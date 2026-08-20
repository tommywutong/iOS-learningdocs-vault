---
title: 'Emerge Tools 博客 | 符号化 SwiftUI（及任意 Apple 框架），第 2 部分'
source: Emerge Tools Blog
source_key: emergetools
source_url: 'https://www.emergetools.com/blog/posts/symbolicating-swiftui-and-any-apple-framework-part-2'
original_language: en
published: ''
status: frozen
license: All rights reserved（页脚明示）→ 严格私有
archived_at: 2026-07-27
content_hash: 'sha256:15d8fbc254b01f0e'
translated: true
---

> 原文：[Emerge Tools Blog | Symbolicating SwiftUI (and any Apple Framework), Part 2](https://www.emergetools.com/blog/posts/symbolicating-swiftui-and-any-apple-framework-part-2)　·　Emerge Tools Blog

# 符号化 SwiftUI（及任意 Apple 框架），第 2 部分

2023 年 12 月 12 日

[Itay Brenner](https://twitter.com/itaybre)

iOSSwift 开源

![符号化 SwiftUI（及任意 Apple 框架），第 2 部分](https://www.emergetools.com/_next/image?url=%2F_next%2Fstatic%2Fmedia%2Fbanner.f04ea2e8.png&w=3840&q=100&dpl=dpl_9GUvYRYkSXVcp9398feaiSHuz7SE)

在[第 1 部分](https://www.emergetools.com/blog/posts/symbolicating-swiftui-and-any-apple-framework)中，我们探索了如何对 SwiftUI 这样的框架进行符号化——这类框架因为不提供符号（symbols）而在崩溃报告中难以调试。现在是把那些工作派上用场的时候了。我们的目标是提供一种方式来实现：

- 符号化（symbolicate）崩溃报告
- 高效提取任何框架的符号
- 追踪已发现的符号

由于这些框架的符号化显然应该由各个开发者自己负责🙃，我们需要一种可扩展的、社区驱动的方式来实现任意框架的符号化。带着这个想法，我们很兴奋地推出我们的开源 [**ETSymbolication**](https://github.com/EmergeTools/ETSymbolication) 仓库和 Emerge Tools 的 [**symbolicator**](https://www.emergetools.com/symbolicate)。

⭐️

[**ETSymbolication**](https://github.com/EmergeTools/ETSymbolication) 是一个开源仓库，用于为私有框架生成和发现符号，并允许任何人贡献代码来生成符号。

![ETSymbolication 仓库中可用的符号](https://www.emergetools.com/_next/image?url=%2Fimages%2Fblogs%2Fblog19%2Favailable-symbols.png&w=1920&q=75&dpl=dpl_9GUvYRYkSXVcp9398feaiSHuz7SE)

ETSymbolication 仓库中可用的符号

⭐️

Emerge Tools [**symbolicator**](https://www.emergetools.com/symbolicate) 是一个免费工具，它使用该开源仓库中的符号来符号化任何崩溃报告。

![Emerge Tools Symbolicator 截图](https://www.emergetools.com/_next/image?url=%2Fimages%2Fblogs%2Fblog19%2Fsymbolicate.gif&w=1920&q=75&dpl=dpl_9GUvYRYkSXVcp9398feaiSHuz7SE)

Emerge Tools Symbolicator

这篇博客的第 2 部分首先聚焦于 ETSymbolication 的设计与实现——如何生成和提取符号。接着，我们会讲解我们是如何构建 symbolicator 的，以及你也能自己打造一个。下面是我们要涵盖的内容：

- [生成崩溃报告](#generating-crash-reports)
- [下载崩溃报告](#downloading-crash-reports)
- [理解崩溃报告](#understanding-crash-reports)
- [解析崩溃报告](#parsing-crash-reports)
- [创建 symbolicator](#creating-a-symbolicator)

## [生成崩溃报告](https://www.emergetools.com/blog/posts/symbolicating-swiftui-and-any-apple-framework-part-2#generating-crash-reports)

如果你还记得第 1 部分，挖掘符号来源于人为制造崩溃。崩溃必须快速且可追踪。有什么比做一个 App 更好的办法呢！

我们需要一个直观的 UI 来在合适的位置触发崩溃。为此，我们只需要一个框架选择器（Framework selector）和两个步进器（steppers）：Threads（线程数）和 Offset（偏移量）。

![Firebase 示例崩溃](https://www.emergetools.com/_next/image?url=%2Fimages%2Fblogs%2Fblog19%2Fcrasher-app.jpeg&w=640&q=75&dpl=dpl_9GUvYRYkSXVcp9398feaiSHuz7SE)

- **Threads**：每个线程能够提取 550 个符号。你使用的线程越多，所需的崩溃次数就越少。请记住，使用过多线程可能会拖慢 Apple 的崩溃报告服务——稍后我们需要用它来下载崩溃报告。
- **Offset**：我们需要多次崩溃来提取所有符号。offset（偏移量）参数指示要开始的内存地址。如果我们将一个二进制的所有符号列表按照每次崩溃的符号数量（线程数 * 550）进行分割，offset 就是我们要开始处理的数组中的位置。基于上一次崩溃，偏移量会自动设置。

要使用[这个 App](https://github.com/EmergeTools/ETSymbolication/tree/main/ETSymbolicationApp)，将它上传到 TestFlight 然后开始制造崩溃。一旦该框架的所有符号都被收集完毕，App 会通知你。

![Firebase 示例崩溃](https://www.emergetools.com/_next/image?url=%2Fimages%2Fblogs%2Fblog19%2Fno-more-symbols.png&w=640&q=75&dpl=dpl_9GUvYRYkSXVcp9398feaiSHuz7SE)

重要的是要记住，每个设备和操作系统的组合，对于给定的库可能有不同的起始地址，因此崩溃报告可能不同。在为某个框架生成符号时，必须在同一台设备上收集所有崩溃报告。

## [下载崩溃报告](https://www.emergetools.com/blog/posts/symbolicating-swiftui-and-any-apple-framework-part-2#downloading-crash-reports)

在必要的崩溃发生后，我们需要前往 [AppStore Connect](https://appstoreconnect.apple.com/apps) 的 "Crashes" 部分，路径为 App →（你的 App）→ TestFlight。

![Firebase 示例崩溃](https://www.emergetools.com/_next/image?url=%2Fimages%2Fblogs%2Fblog19%2Fcrash-feedback.png&w=1200&q=75&dpl=dpl_9GUvYRYkSXVcp9398feaiSHuz7SE)

当 Apple 完成了某个崩溃的符号化后，将鼠标悬停在崩溃条目上会出现一个 "Open in Xcode" 按钮。不要点击这个按钮，而是点击崩溃条目，在那里你会找到一个下载该崩溃报告的按钮。每个崩溃都需要重复这个过程。

![Firebase 示例崩溃](https://www.emergetools.com/_next/image?url=%2Fimages%2Fblogs%2Fblog19%2Fcrash-details.png&w=1920&q=75&dpl=dpl_9GUvYRYkSXVcp9398feaiSHuz7SE)

解压下载的文件，并将所有 `*.crash` 文件放入一个新文件夹中。

## [理解崩溃报告](https://www.emergetools.com/blog/posts/symbolicating-swiftui-and-any-apple-framework-part-2#understanding-crash-reports)

现在我们已经将所有的崩溃报告保存在电脑上，下一步是提取并解读它们包含的信息。如果你想复习一下如何阅读这些报告，可以观看 WWDC 2021 的讲座 ["Symbolication: Beyond the basics"](https://developer.apple.com/videos/play/wwdc2021/10211/) 和 Apple 关于崩溃报告的[文档](https://developer.apple.com/documentation/xcode/examining-the-fields-in-a-crash-report)。

下面是我们将要参考的一份示例崩溃报告：

```plaintext
Thread 14:
0   libsystem_kernel.dylib        	0x00000001de2849d8 __semwait_signal + 8
1   libsystem_c.dylib             	0x000000019f6240fc nanosleep + 220 (nanosleep.c:104)
2   Foundation                    	0x0000000196d95c18 +[NSThread sleepForTimeInterval:] + 160 (NSThread.m:527)
3   ETSymbolicationApp            	0x0000000102b02858 -[EMGThread modifyFrameAndWait] + 316 (EMGThread.m:84)
4   ETSymbolicationApp            	0x0000000102b0270c -[EMGThread main] + 52 (EMGThread.m:33)
5   SwiftUI                       	0x000000019b373dd2 -[BaseDateProvider _updateFrequency] + 2 (BaseDateProvider.m:177)
6   SwiftUI                       	0x000000019b373dda -[BaseDateProvider _timeFormatByRemovingWhitespaceAroundDesignatorOfTimeFormat:designatorExists:] + 2 (BaseDateProvider.m:182)
...
Binary Images:
      0x102afc000 -         0x102b07fff ETSymbolicationApp arm64  <60ae09cb96de37c4a0cad4230beb1453> /private/var/containers/Bundle/Application/73270493-A800-446E-B306-49F3E89A169B/ETSymbolicationApp.app/ETSymbolicationApp
...
      0x19b366000 -         0x19d241fff SwiftUI arm64e  <7bbaf70522f73edc9a764c8c1730188c> /System/Library/Frameworks/SwiftUI.framework/SwiftUI
```

像 `0x000000019b373dd2` 这样的内存地址是由 `symbol address` 和 `load address` 组合而成的。

```plaintext
0x000000019b373dd2 = symbol address + load address
```

`load address` 来自两个组成部分：`slide` 和 `linker address`。

```plaintext
load address = slide + linker address
```

崩溃报告和地址可能会让人望而生畏，所以在继续之前，让我们退一步来理解我们正在做的事情。第 1 部分表明，Apple 的崩溃报告包含其框架的符号。我们还知道，对于一个设备和操作系统的组合，符号在磁盘上的地址是相同的。我们想要从 Apple 获取所有可能的崩溃（针对一个设备 x 操作系统组合），然后将内存地址映射到符号名称。为此，我们需要可靠地计算内存地址，从而能够符号化崩溃报告。

把这一部分想象成我们在做代数。我们知道地址是如何计算的公式。现在，我们需要求解我们的变量。

首先，让我们找到 `linker address`，它是在编译时定义的，并且可以在二进制文件中找到，因此很容易获取。我们需要：

- 设备的 `.ipsw` 文件，你可以从 [https://www.ipsw.me](https://www.ipsw.me) 下载
- [ipsw CLI](https://github.com/blacktop/ipsw) 工具，它让我们可以从 .ipsw 文件中提取框架

  ```shell
  brew install blacktop/tap/ipsw
  ```
- DyldExtractor，用于从 ipsw 中提取共享缓存（shared cache）

  ```shell
  python3 -m pip install dyldextractor
  ```
- `otool`

安装 ipsw 后，我们的第一步是提取共享缓存：

```shell
ipsw extract --dyld PATH_TO_IPSW
```

现在，我们可以使用 DyldExtractor 提取特定的框架二进制文件：

```shell
dyldex -e /System/Library/Frameworks/YOUR_FRAMEWORK.framework/YOUR_FRAMEWORK ./PATH_TO_EXTRACTED_IPSW/dyld_shared_cache_arm64e
```

这个过程将我们的框架二进制文件从共享缓存中分离出来。下一步是使用 `otool` 来确定 `linker address`。为此，我们检查加载命令（load commands），并在输出中专门查找 `segname __TEXT` 字段。

```shell
otool -l binaries/System/Library/Frameworks/SwiftUI.framework/SwiftUI | grep LC_SEGMENT -A8

Output:
cmd LC_SEGMENT_64
cmdsize 2152
segname __TEXT
vmaddr 0x000000018b99e000
vmsize 0x0000000001edc000
fileoff 0
filesize 32358400
maxprot 0x00000005
initprot 0x00000005
```

`vmaddr` 字段代表了 `linker address`，在这个例子中是 `0x000000018b99e000`。当我们在构建 symbolicator 时，也会用到 `linker address` 和 `OS version`。

收集了所有必需的变量后，我们现在可以计算符号的磁盘地址（disk address）。公式如下：

```plaintext
0x000000019b373dd2 = symbol address + load address
```

`load address` 是崩溃报告底部显示的第一个地址：

```plaintext
Binary Images:
...
      0x19b366000 -    0x19d241fff SwiftUI arm64e  <7bbaf70522f73edc9a764c8c1730188c> /System/Library/Frameworks/SwiftUI.framework/SwiftUI
```

有了 `linker address` 和 `load address`，我们现在可以计算 slide：

```plaintext
slide = load address - linker address = 0x000000019b366000 - 0x000000018b99e000
slide = 0x00000000F9C8000
```

最后，我们可以使用 slide 值来计算符号的磁盘地址：

```plaintext
symbol address = 0x000000019b373dd2 - slide
symbol address = 0x000000019b373dd2 - 0x00000000F9C8000
symbol address = 0x000000018b9abdd2
```

这个计算出的值，代表符号在磁盘上的地址，对于同一个操作系统和设备组合的每一份崩溃报告都是恒定的。这意味着，为了找到每次崩溃的符号，我们只需要为我们的特定报告确定 slide 值。

## [解析崩溃报告](https://www.emergetools.com/blog/posts/symbolicating-swiftui-and-any-apple-framework-part-2#parsing-crash-reports)

在理论基础打好之后，以下是我们需要编码实现的内容：

1. **读取每个崩溃报告**
2. **查找并验证操作系统版本的一致性**：确保所有崩溃报告来自同一个操作系统版本。一致性对于准确性至关重要。
3. **识别 load address**：在每份报告中，找到与 SwiftUI 框架关联的 load address。
4. **计算 slide**：使用 linker address 和 load address 计算每份崩溃报告的 slide 值。
5. **确定符号的地址**：从崩溃报告中报告的符号地址中减去 slide 值。
6. **处理 +2 常量**：记得处理我们在第一篇博客中添加的 +2 常量值。这个调整确保地址落在符号开始之后。

**读取崩溃报告**

```swift
guard let streamReader = StreamReader(path: crash) else {
fatalError("Failed to open the file (crash).")
}
defer {
streamReader.close()
}
```

**验证操作系统一致性**

```swift
var version: String? = nil
while let line = streamReader.nextLine() {
let regex = /OS Version:( )+(iPhone OS|iOS) (d{2}).(d)(.d)? ((?<version>[da-zA-Z]+))/
if let match = line.firstMatch(of: regex) {
  version = String(describing: match.version)
  break
}
}
guard let versionFound = version else {
fatalError("Could not find OS version in (crash).")
}
// 我们应该确保对于每个崩溃报告，这个 versionFound 都是相同的
```

**识别 load address**

我们需要 "Binary Images" 部分来进行 slide 计算，因此我们暂时存储内存地址和符号名称，包括 slide：

```swift
private enum CrashResult {
case nothing
case symbol(UInt64, Substring)
case parsingDone
}
var tmpCrashSymbols: [UInt64: Substring] = [:]
whileLoop: while let line = streamReader.nextLine() {
switch parseCrashForSymbols(line, library) {
case .parsingDone:
  break whileLoop  // Stop while
case .symbol(let address, let symbol):
  tmpCrashSymbols[address] = symbol
case .nothing:
  break
}
}
static private func parseCrashForSymbols(_ line: String, _ library: String) -> CrashResult {
let regex = /d+s+(?<library>[a-zA-Z0-9]+)s+	?0x(?<address>[a-fA-F0-9]{16})s+(?<method>.+)/
if let match = line.firstMatch(of: regex),
  match.library == library,
  let addressAsInt = UInt64(match.address, radix: 16)
{
  return .symbol(addressAsInt, match.method)
}
if line == "Binary Images:" {
  return .parsingDone
}
return .nothing
}
```

这种方法允许我们遍历崩溃报告中的所有行，只选择性地存储那些与我们的目标库相关的行。例如，像这样的一行：

```swift
172 SwiftUI    0x000000019b37d892 initializeBufferWithCopyOfBuffer for CapsuleSlider + 2 (<compiler-generated>:0)
```

将返回元组 `(6899095698, "initializeBufferWithCopyOfBuffer for CapsuleSlider + 2 (<compiler-generated>:0")`。然后将此数据存储在临时字典 `tmpCrashSymbols` 中。

**计算 slide**

```swift
var loadAddress: UInt64? = nil
while let line = streamReader.nextLine() {
if let address = parseCrashForLoadAddress(line, library) {
  loadAddress = address
  break
}
}

guard let loadAddress = loadAddress else {
fatalError("Could not find \(library) load address in \(crash).")
}

static private func parseCrashForLoadAddress(_ line: String, _ library: String) -> UInt64? {
let loadRegex = /\s+0x(?<memoryAddress>[a-fA-F0-9]{9})\s-\s+0x[a-fA-F0-9]{9}\s(?<library>[a-zA-Z0-9]+)/

if let match = line.firstMatch(of: loadRegex),
  match.library == library
{
  return UInt64(match.memoryAddress, radix: 16)
}
return nil
}
```

找到 `load address` 后，我们现在可以精确地计算 `slide`。这个计算使我们能够修正内存地址：

```swift
var symbolsMap: [UInt64: String] = [:]

let slide = loadAddress - linkerAddress;

for (address, symbol) in tmpCrashSymbols {
let (fixedAddress, fixedSymbol) = fixSymbols(address, symbol, slide)
symbolsMap[fixedAddress] = symbol
}

static let plusRegex = / + (?<symbol*length>d+)/
static private func fixSymbols(* address: UInt64, _ symbol: Substring, _ slide: UInt64) -> (
UInt64, String
) {
var fixedAddress = address - slide
var fixedSymbol = symbol

// 符号文件的格式为 NEXT_SYMBOL_ADDR: symbol_name + symbol_length
if let match = fixedSymbol.firstMatch(of: plusRegex) {
  fixedAddress -= UInt64(match.symbol_length) ?? 0
  fixedSymbol.replaceSubrange(match.range, with: "")
}

return (fixedAddress, String(fixedSymbol))
}
```

处理完每份崩溃报告后，生成的符号映射表就可以保存了。为了简化，ETSymbolication 将[清理后的符号](https://github.com/EmergeTools/ETSymbolication/blob/main/ETSymbolicationApp/ETSymbolicationBuilder/Logic/ResultWriter.swift)输出为 CSV 文件，然后可以轻松地存储在数据库中，并供我们的 symbolicator 引用。如果你计划处理更大规模的崩溃分析，可能需要一个更健壮的存储格式。

![ETSymbolication 中的 CSV 文件](https://www.emergetools.com/_next/image?url=%2Fimages%2Fblogs%2Fblog19%2Fcsv-files.png&w=828&q=75&dpl=dpl_9GUvYRYkSXVcp9398feaiSHuz7SE)

ETSymbolication 中的 CSV 文件

在 ETSymbolication 中，文件夹代表一个设备，比如上图中的 iPhone SE 2nd gen。每个文件对应一个特定的操作系统版本，并且可以包含多个框架的符号。支持的符号完整列表在[这里](https://github.com/EmergeTools/ETSymbolication/?tab=readme-ov-file#supported-symbols)。

## [创建 symbolicator](https://www.emergetools.com/blog/posts/symbolicating-swiftui-and-any-apple-framework-part-2#creating-a-symbolicator)

到目前为止，我们已经完成了如何在框架中查找符号、利用崩溃提取符号，以及解读崩溃报告以构建符号数据库。

本篇博客的最后部分将聚焦于我们是如何构建 Emerge Tools symbolicator 的，内容包括：

- 接收崩溃报告
- 为每个库查找 slide
- 修正堆栈跟踪的内存地址
- 从我们的数据库中查找符号

我们可以使用之前相同的代码来查找设备和操作系统版本。为了找到 `load address`，我们暂时跳过堆栈跟踪，留待稍后处理。

```swift
static let linkerAddresses: [String: UInt64] = [
"20F66": 0x000000018a8bf000,
]

var loadAddress: UInt64 = 0
while let line = streamReader.nextLine() {
let loadRegex = /s+0x(?<memoryAddress>[a-fA-F0-9]{9})s-s+0x[a-fA-F0-9]{9}s(?<library>[a-zA-Z0-9]+)/
if let match = line.firstMatch(of: loadRegex),
  match.library == library,
  let addressAsInt = UInt64(match.memoryAddress, radix: 16)
{
  loadAddress = addressAsInt
  streamReader.reset() // reset stream to start reading from the first line
  break;
}
}
guard let loadAddressFound = loadAddress else {
fatalError("Could not find load address for (library).")
}
let slide = loadAddress - linkerAddresses[version]
```

计算得到 `slide` 后，我们可以遍历堆栈跟踪，替换任何缺失的库符号。

```swift
let symbolicator = try Symbolicator(version: version)
while let line = streamReader.nextLine() && loadAddress == 0 {
let regex = /(?<line>(\d+)\s+(?<library>[a-zA-Z0-9]+)( )+0x(?<address>[\da-f]{0,16})) (?<method>.*)/
if let match = line.firstMatch(of: regex),
  match.library == library,
  let address = UInt64(match.address, radix: 16),
  let symbolicateMethod = symbolicator.getSymbolNameForAddress(library, address - slide)
{
  print("(match.line) (symbolicateMethod)")
} else {
  print(line)
}
}
```

`Symbolicator` 类将所有特定操作系统版本的符号加载到内存中，从而实现快速搜索。

```swift
class SwiftUISymbolicator {
let version: String
private var addressesToSymbols: [String: [UInt64: String]] = [:]

init(version: String) throws {
  self.version = version
  loadAddresses()
}

private func loadAddresses() {
  let symbolsPath = "~/Symbols/symbols_\(versionFound).csv"

  guard let streamReader = StreamReader(path: swiftUISymbolsPath) else {
    fatalError("Failed to open the file \(swiftUISymbolsPath).")
  }
  defer {
    streamReader.close()
  }
  while let line = streamReader.nextLine() {
    let regex = /\/(?<library>[a-zA-Z0-9]+),\[0x(?<startAddress>[a-fA-F0-9]{16}),0x[a-fA-F0-9]{16}\),(?<symbol>.+),/
    if let match = line.firstMatch(of: regex),
      let address = UInt64(match.startAddress, radix: 16)
    {
      let library = match.library
      let symbol = match.symbol
      if addressesToSymbols[library] == nil {
        addressesToSymbols[library] = [:]
      }
      addressesToSymbols[library][address] = symbol
    }
  }
}
}
```

`getSymbolNameForAddress` 将内存地址映射到它们对应的符号名称。

```swift
private var sortedAddresses: [String: [UInt64]] = [:]

func getSymbolNameForAddress(_ library: string, _ address: UInt64) -> String? {
// 确保地址已排序，以防 CSV 文件有问题
var librarySortedAddresses = sortedAddresses[library]
if librarySortedAddresses == nil {
  librarySortedAddresses = addressesToSymbols[library]!.keys.sorted()
  sortedAddresses[library] = librarySortedAddresses
}
let symbol = findLargestLowerItem(librarySortedAddresses, address)!
return addressesToSymbols[library]![symbol]
}
```

如果面试准备告诉我们什么，那就是我们希望一切已排序，这样我们就可以使用二分查找（binary search）。

```swift
private func findLargestLowerItem(_ array: [UInt64], _ value: UInt64) -> UInt64? {
var left = 0
var right = array.count - 1
var result: UInt64?

while left <= right {
  let mid = (left + right) / 2
  let midValue = array[mid]

  if midValue < value {
    result = midValue
    left = mid + 1
  } else {
    right = mid - 1
  }
}
return result
}
```

## [总结](https://www.emergetools.com/blog/posts/symbolicating-swiftui-and-any-apple-framework-part-2#conclusion)

![Emerge Tools Symbolicator 运行中](https://www.emergetools.com/_next/image?url=%2Fimages%2Fblogs%2Fblog19%2Fsymbolicate.gif&w=1920&q=75&dpl=dpl_9GUvYRYkSXVcp9398feaiSHuz7SE)

Emerge Tools Symbolicator 运行中

就这样，我们有了一个 symbolicator！感谢你陪伴我们完成这次关于 Swift 符号化的深度探索！我们被第一篇博文的反馈所震撼，并且非常兴奋能将这项工作开源。如果你有兴趣贡献，所有信息都在 [ETSymbolication 仓库](https://github.com/EmergeTools/ETSymbolication)中。如果你有一些崩溃想要追查到底，那就[尽情符号化吧！](https://www.emergetools.com/symbolicate)
