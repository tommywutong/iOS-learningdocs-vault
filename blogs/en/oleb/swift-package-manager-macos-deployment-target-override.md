---
title: Swift Package Manager macOS deployment target override
source: Ole Begemann
source_key: oleb
source_url: 'https://oleb.net/blog/2017/04/swift-3-1-package-manager-deployment-target/'
original_language: en
published: ''
status: active
license: 未声明 → 仅私有归档
archived_at: 2026-07-27
content_hash: 'sha256:fd28951cdc78033a'
translated: false
---

> 原文：[Swift Package Manager macOS deployment target override](https://oleb.net/blog/2017/04/swift-3-1-package-manager-deployment-target/)　·　Ole Begemann

# Swift Package Manager macOS deployment target override

Swift 3.1 fixes a bug in the [Swift Package Manager](https://swift.org/package-manager/) that prevented overriding the macOS deployment target.

When you run `swift build` on macOS, the package manager currently (as of Swift 3.0 and 3.1) hardcodes the deployment target to macOS 10.10.^[1](#fn:check-deployment-target) In Swift 3.0 it was impossible to override this due to [a bug](https://bugs.swift.org/browse/SR-2535) in the order arguments were evaluated.

Because of this, you could not easily^[2](#fn:available) compile code that required newer APIs. As an example, consider a very simple package with just a few lines of code in a single source file. The program uses the new [units and measurements types](https://oleb.net/blog/2016/07/measurements-and-units/) introduced in macOS 10.12 to convert a value from _km/h_ to _m/s_:

```
// main.swift
import Foundation

let kph = Measurement(value: 100,
    unit: UnitSpeed.kilometersPerHour)
let mps = kph.converted(to: .metersPerSecond)
print("\(kph) is \(mps)")
```

Building this with `swift build` on macOS (with Swift 3.0 or 3.1) produces an error because the API is not available on macOS 10.10:

```
$ swift build
Compile Swift Module 'Units' (1 sources)
main.swift:3:11: error: 'Measurement' is only available on OS X 10.12 or newer
let kph = Measurement(value: 100,
          ^
main.swift:3:11: note: add 'if #available' version check
let kph = Measurement(value: 100,
          ^
...
<unknown>:0: error: build had 1 command failures
error: exit(1): /Applications/Xcode.app/Contents/Developer/Toolchains/XcodeDefault.xctoolchain/usr/bin/swift-build-tool -f .build/debug.yaml
```

In Swift 3.1 you can override the deployment target on the command line like this:

```
$ swift build -Xswiftc "-target" \
    -Xswiftc "x86_64-apple-macosx10.12"
Compile Swift Module 'Units' (1 sources)
Linking ./.build/debug/Units
```

And now you can run the executable:

```
$ .build/debug/Units
100.0 km/h is 27.7778 m/s
```

# Conclusion

Aside from the deployment target, another common use case for custom build settings is to pass a `DEBUG` flag to the compiler so that you can use `#if DEBUG`/`#endif` blocks in your code — the package manager doesn’t do this automatically in debug builds. You can do it with `swift build -Xswiftc "-D" -Xswiftc "DEBUG"`.

This is still far from ideal — you have to pass the command line arguments manually every time you invoke `swift build` or `swift test` — but at least it’s possible.

The ability to specify custom build settings in the package manifest is part of the [Swift 4 roadmap](https://forums.swift.org/t/swift-4-package-manager-roadmap/4955) for the package manager. My guess is we’ll see a [Swift Evolution proposal](https://www.swift.org/swift-evolution/) for this soon.

1. You an verify this by adding this code snippet to your `main.swift` file and then building and running the package:

  ```
  #if os(macOS)
      print("macOS deployment target:", __MAC_OS_X_VERSION_MIN_REQUIRED)
  #endif
  ```

  If run on macOS, this will print:

  ```
  macOS deployment target: 101000
  ```

  [↩︎](#fnref:check-deployment-target)
2. You’d have to wrap all code that depended on the newer APIs in `if #available(macOS 10.12, iOS 10.0, tvOS 10.0, watchOS 3.0, *) { ... }` (or similar) blocks. [↩︎](#fnref:available)
