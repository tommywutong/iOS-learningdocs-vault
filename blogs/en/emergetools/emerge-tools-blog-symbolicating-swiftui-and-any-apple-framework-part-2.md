---
title: 'Emerge Tools Blog | Symbolicating SwiftUI (and any Apple Framework), Part 2'
source: Emerge Tools Blog
source_key: emergetools
source_url: 'https://www.emergetools.com/blog/posts/symbolicating-swiftui-and-any-apple-framework-part-2'
original_language: en
published: ''
status: frozen
license: All rights reserved（页脚明示）→ 严格私有
archived_at: 2026-07-27
content_hash: 'sha256:15d8fbc254b01f0e'
translated: false
---

> 原文：[Emerge Tools Blog | Symbolicating SwiftUI (and any Apple Framework), Part 2](https://www.emergetools.com/blog/posts/symbolicating-swiftui-and-any-apple-framework-part-2)　·　Emerge Tools Blog

# Symbolicating SwiftUI (and any Apple Framework), Part 2

December 12, 2023 by

[Itay Brenner](https://twitter.com/itaybre)

iOSSwiftOpen Source

![Symbolicating SwiftUI (and any Apple Framework), Part 2](https://www.emergetools.com/_next/image?url=%2F_next%2Fstatic%2Fmedia%2Fbanner.f04ea2e8.png&w=3840&q=100&dpl=dpl_9GUvYRYkSXVcp9398feaiSHuz7SE)

In [Part 1](https://www.emergetools.com/blog/posts/symbolicating-swiftui-and-any-apple-framework), we explored how you can symbolicate frameworks like SwiftUI, which are difficult to debug in crash reports because they don’t provide symbols. Now it's time to put that work to good use. Our goal is to provide a way to:

- Symbolicate crash reports
- Efficiently exfiltrate symbols for any framework
- Keep track of symbols that have already been discovered

Since the symbolication of these frameworks should clearly be on the onus of individual developers 🙃 we need a scalable, community-driven way to symbolicate any framework. With that in mind, we’re excited to unveil our open-source [**ETSymbolication**](https://github.com/EmergeTools/ETSymbolication) repo and the Emerge Tools’ [**symbolicator**](https://www.emergetools.com/symbolicate).

⭐️

[**ETSymbolication**](https://github.com/EmergeTools/ETSymbolication) is an open-source repo to generate and discover symbols for private frameworks and let anyone contribute to generating symbols.

![Available symbols, found in the ETSymbolication repo](https://www.emergetools.com/_next/image?url=%2Fimages%2Fblogs%2Fblog19%2Favailable-symbols.png&w=1920&q=75&dpl=dpl_9GUvYRYkSXVcp9398feaiSHuz7SE)

Available symbols, found in the ETSymbolication repo

⭐️

The Emerge Tools [**symbolicator**](https://www.emergetools.com/symbolicate) is a free tool that uses symbols in the open-source repo to symbolicate any crash report.

![Screenshot of Emerge Tools Symbolicator](https://www.emergetools.com/_next/image?url=%2Fimages%2Fblogs%2Fblog19%2Fsymbolicate.gif&w=1920&q=75&dpl=dpl_9GUvYRYkSXVcp9398feaiSHuz7SE)

Emerge Tools Symbolicator

Part 2 of this blog first focuses on the design and implementation of ETSymbolication — how to generate and extract symbols. Then, we walk through how we built our symbolicator and how you could build one too. Here's a look at what we'll cover:

- [Generating crash reports](#generating-crash-reports)
- [Downloading crash reports](#downloading-crash-reports)
- [Understanding crash reports](#understanding-crash-reports)
- [Parsing crash reports](#parsing-crash-reports)
- [Creating a symbolicator](#creating-a-symbolicator)

## [Generating crash reports](https://www.emergetools.com/blog/posts/symbolicating-swiftui-and-any-apple-framework-part-2#generating-crash-reports)

If you remember from Part I, excavating symbols comes from manufacturing crashes. Crashing should be fast and trackable. What better way to do that than making an app!

We need a straightforward UI to initiate crashes at the appropriate points. To do so, we only need a Framework selector and 2 steppers: Threads and Offset.

![Firebase example crash](https://www.emergetools.com/_next/image?url=%2Fimages%2Fblogs%2Fblog19%2Fcrasher-app.jpeg&w=640&q=75&dpl=dpl_9GUvYRYkSXVcp9398feaiSHuz7SE)

- **Threads**: Each thread is capable of extracting 550 symbols. The more threads you use, the fewer crashes you need. Keep in mind that using too many threads may slow Apple's crash reporting service, which we’ll need later to download the crashes.
- **Offset**: We need multiple crashes to extract all symbols. The offset parameter indicates the memory address to start at. If we split a binary's full list of symbols by the number of symbols per crash (threads * 550), the offset is the position in the array we will start working from. Offsets are set automatically based on the previous crash.

To use [the app](https://github.com/EmergeTools/ETSymbolication/tree/main/ETSymbolicationApp), upload it to TestFlight and start crashing. The app will alert you once all symbols have been collected for the framework.

![Firebase example crash](https://www.emergetools.com/_next/image?url=%2Fimages%2Fblogs%2Fblog19%2Fno-more-symbols.png&w=640&q=75&dpl=dpl_9GUvYRYkSXVcp9398feaiSHuz7SE)

It's important to remember that each device and OS pairing may have a different starting address for a given library, so crash reports can differ. When generating symbols for a framework, it's essential to collect all crashes on the same device.

## [Downloading crash reports](https://www.emergetools.com/blog/posts/symbolicating-swiftui-and-any-apple-framework-part-2#downloading-crash-reports)

After the necessary crashing, we need to go to the [AppStore Connect](https://appstoreconnect.apple.com/apps) Crashes section inside App → (Your App) → TestFlight.

![Firebase example crash](https://www.emergetools.com/_next/image?url=%2Fimages%2Fblogs%2Fblog19%2Fcrash-feedback.png&w=1200&q=75&dpl=dpl_9GUvYRYkSXVcp9398feaiSHuz7SE)

When Apple has completed the symbolication of a crash, an 'Open in Xcode' button will appear as you hover over the crash entry. Instead of clicking this button, click on the crash entry, where you will find a button to download the crash. This process needs to be repeated for each crash.

![Firebase example crash](https://www.emergetools.com/_next/image?url=%2Fimages%2Fblogs%2Fblog19%2Fcrash-details.png&w=1920&q=75&dpl=dpl_9GUvYRYkSXVcp9398feaiSHuz7SE)

Unzip the downloaded files and place the *.crash files inside a new folder.

## [Understanding crash reports](https://www.emergetools.com/blog/posts/symbolicating-swiftui-and-any-apple-framework-part-2#understanding-crash-reports)

Now that we have all the crash reports on our computer, our next step is to extract and interpret the information they contain. If you’d like to brush up on how to read these reports, you can check out the WWDC 2021 session, ["Symbolication: Beyond the basics"](https://developer.apple.com/videos/play/wwdc2021/10211/) and Apple’s [documentation](https://developer.apple.com/documentation/xcode/examining-the-fields-in-a-crash-report) on crash reports.

Here’s a sample crash report that we'll be referring to:

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

A memory address like `0x000000019b373dd2` combines the `symbol address` and the `load address`.

```plaintext
0x000000019b373dd2 = symbol address + load address
```

The `load address` is derived from two components: the `slide` and the `linker address`.

```plaintext
load address = slide + linker address
```

Crash reports and addresses can be scary, so before going any further, let’s take a step back to frame what we are doing. Part 1 showed that Apple’s crash reports have symbols for their frameworks. We also know that a symbol’s address on disk is the same across a device and OS pairing. We want to get all the possible crashes (for a device x OS pair) from Apple and then map the memory address to the symbol name. To do this, we need to reliably calculate a memory address, allowing us to symbolicate crash reports.

Think of this part like we’re doing Algebra. We know the equations for how addresses are calculated. Now, we need to solve for our variables.

First, let’s find the `linker address`, which is defined at the time of compilation and can be found within the binary, making it easy to get. We'll need:

- The device `.ipsw`, which you can download it from [https://www.ipsw.me](https://www.ipsw.me)
- [ipsw CLI](https://github.com/blacktop/ipsw) tool, which lets us extract the framework from .ipsw

  ```shell
  brew install blacktop/tap/ipsw
  ```
- DyldExtractor to extract the ipsw shared cache

  ```shell
  python3 -m pip install dyldextractor
  ```
- `otool`

After installing ipsw, our first step is to extract the shared cache:

```shell
ipsw extract --dyld PATH_TO_IPSW
```

Now, we can extract the specific framework binary using DyldExtractor:

```shell
dyldex -e /System/Library/Frameworks/YOUR_FRAMEWORK.framework/YOUR_FRAMEWORK ./PATH_TO_EXTRACTED_IPSW/dyld_shared_cache_arm64e
```

This process isolates our framework binary from the shared cache. The next step involves using `otool` to determine the `linker address`. For this, we inspect the load commands and specifically look for the `segname __TEXT` field in the output.

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

The `vmaddr` field represents the `linker address`, which, in this example, is `0x000000018b99e000`. The `linker address` and `OS version` will also be used when we're making our symbolicator.

Having gathered all required variables, we can now calculate the disk address for the symbol. This formula is:

```plaintext
0x000000019b373dd2 = symbol address + load address
```

The `load address` is the first address at the bottom of the crash report:

```plaintext
Binary Images:
...
      0x19b366000 -    0x19d241fff SwiftUI arm64e  <7bbaf70522f73edc9a764c8c1730188c> /System/Library/Frameworks/SwiftUI.framework/SwiftUI
```

With the `linker address` and `load address`, we can now calculate the slide:

```plaintext
slide = load address - linker address = 0x000000019b366000 - 0x000000018b99e000
slide = 0x00000000F9C8000
```

And finally, we can use the slide value to calculate the symbol’s disk address:

```plaintext
symbol address = 0x000000019b373dd2 - slide
symbol address = 0x000000019b373dd2 - 0x00000000F9C8000
symbol address = 0x000000018b9abdd2
```

This calculated value, representing the symbol's address on the disk, remains constant across every crash report for the same OS and device combination. This means that to find the symbol for each crash, we only need to determine the slide value for our particular report.

## [Parsing the crash reports](https://www.emergetools.com/blog/posts/symbolicating-swiftui-and-any-apple-framework-part-2#parsing-crash-reports)

With the theoretical groundwork laid out, here’s what we need to code:

1. **Read Each Crash Report**
2. **Find and Verify OS Version Consistency**: Ensure all crash reports are from the same OS version. Consistency is crucial for accuracy.
3. **Identify the Load Address**: In each report, locate the load address associated with the SwiftUI framework.
4. **Calculate the Slide**: Use the linker address and load address to calculate the slide value for each crash report.
5. **Determine the Symbol's Address**: Subtract the slide value from the reported symbol address in the crash report.
6. **Adjust for the +2 Constant**: Remember to account for the +2 constant value we added in our first blog post. This adjustment ensures that the address falls after the start of the symbol.

**Reading the crash report**

```swift
guard let streamReader = StreamReader(path: crash) else {
fatalError("Failed to open the file (crash).")
}
defer {
streamReader.close()
}
```

**Verifying OS Consistency**

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
// We should make sure this versionFound is the same for each crash report
```

**Identifying load address**

We need the 'Binary Images' section for our slide calculation, so we will temporarily store the memory addresses and symbol names, including the slides:

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

This approach allows us to iterate over all lines in the crash report, selectively storing only the relevant ones for our target library. For example, a line like:

```swift
172 SwiftUI    0x000000019b37d892 initializeBufferWithCopyOfBuffer for CapsuleSlider + 2 (<compiler-generated>:0)
```

Will return the tuple `(6899095698, "initializeBufferWithCopyOfBuffer for CapsuleSlider + 2 (<compiler-generated>:0")`. This data is then stored in a temporary dictionary `tmpCrashSymbols`.

**Calculating the slide**

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

Having located the `load address`, we can now accurately calculate the `slide`. This calculation allows us to correct the memory addresses:

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

// Symbols file have format NEXT_SYMBOL_ADDR: symbol_name + symbol_length
if let match = fixedSymbol.firstMatch(of: plusRegex) {
  fixedAddress -= UInt64(match.symbol_length) ?? 0
  fixedSymbol.replaceSubrange(match.range, with: "")
}

return (fixedAddress, String(fixedSymbol))
}
```

Once we have processed each crash report, the resulting symbols map is ready to be saved. For simplicity, ETSymbolication outputs [cleaned symbols](https://github.com/EmergeTools/ETSymbolication/blob/main/ETSymbolicationApp/ETSymbolicationBuilder/Logic/ResultWriter.swift) as a CSV, which are then easily stored in a database and referenced for our symbolicator. A more robust storage format may be necessary if you're planning to handle crash analysis on a larger scale.

![CSV files in ETSymbolication](https://www.emergetools.com/_next/image?url=%2Fimages%2Fblogs%2Fblog19%2Fcsv-files.png&w=828&q=75&dpl=dpl_9GUvYRYkSXVcp9398feaiSHuz7SE)

CSV files in ETSymbolication

In ETSymbolication, folders represent a device, like an iPhone SE 2nd gen in the example above. Each file corresponds to a specific OS version and can have symbols for multiple frameworks. A full list of supported symbols is available [here](https://github.com/EmergeTools/ETSymbolication/?tab=readme-ov-file#supported-symbols).

## [Creating a symbolicator](https://www.emergetools.com/blog/posts/symbolicating-swiftui-and-any-apple-framework-part-2#creating-a-symbolicator)

To this point, we’ve gone through how to find symbols within a framework, extract them using crashes, and interpret the crashes to build a database of symbols.

This final part of the post will focus on how we built the Emerge Tools symbolicator, covering:

- Intaking a crash report
- Finding the slide for each library
- Fixing the memory address of the stacktrace
- Looking up the symbols from our DB

We can use the same code we used previously to find the device and OS version. To find the `load address`, we temporarily bypass the stacktrace for later processing.

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

With the `slide` calculated, we can iterate over the stacktrace, replacing any missing symbols for our library.

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

The `Symbolicator` class loads all symbols for the specific OS version into memory, enabling quick searches.

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

`getSymbolNameForAddress` maps memory addresses to their corresponding symbol names.

```swift
private var sortedAddresses: [String: [UInt64]] = [:]

func getSymbolNameForAddress(_ library: string, _ address: UInt64) -> String? {
// Lets make sure addresses are sorted, just in case the CSV had an issue
var librarySortedAddresses = sortedAddresses[library]
if librarySortedAddresses == nil {
  librarySortedAddresses = addressesToSymbols[library]!.keys.sorted()
  sortedAddresses[library] = librarySortedAddresses
}
let symbol = findLargestLowerItem(librarySortedAddresses, address)!
return addressesToSymbols[library]![symbol]
}
```

If interview prep tells us anything, it’s that we want to have everything sorted so we can use a binary search.

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

## [Wrapping Up](https://www.emergetools.com/blog/posts/symbolicating-swiftui-and-any-apple-framework-part-2#conclusion)

![Emerge Tools Symbolicator in action](https://www.emergetools.com/_next/image?url=%2Fimages%2Fblogs%2Fblog19%2Fsymbolicate.gif&w=1920&q=75&dpl=dpl_9GUvYRYkSXVcp9398feaiSHuz7SE)

Emerge Tools Symbolicator in action

And with that, we have a symbolicator! Thank you for joining on this deep dive through Swift symbolication! We were floored by the reaction from the first post and are incredibly excited to make this work open-sourced. If you're interested in contributing, all information is in the [ETSymbolication repo](https://github.com/EmergeTools/ETSymbolication). If you have crashes you'd like to get to the bottom of, then [happy symbolicating!](https://www.emergetools.com/symbolicate)
