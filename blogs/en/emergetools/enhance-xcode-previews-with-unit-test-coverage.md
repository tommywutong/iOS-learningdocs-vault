---
title: Enhance Xcode Previews with Unit Test Coverage
source: Emerge Tools Blog
source_key: emergetools
source_url: 'https://www.emergetools.com/blog/posts/unit-test-xcode-previews'
original_language: en
published: ''
status: frozen
license: All rights reserved（页脚明示）→ 严格私有
archived_at: 2026-07-27
content_hash: 'sha256:a872c3f0d1d30cb2'
translated: false
---

> 原文：[Enhance Xcode Previews with Unit Test Coverage](https://www.emergetools.com/blog/posts/unit-test-xcode-previews)　·　Emerge Tools Blog

# Enhance Xcode Previews with Unit Test Coverage

December 5, 2024 by

[Noah Martin](https://twitter.com/sond813)

iOSSnapshot Testing

![Enhance Xcode Previews with Unit Test Coverage](https://www.emergetools.com/_next/image?url=%2F_next%2Fstatic%2Fmedia%2Fcover.0eec28d8.jpg&w=3840&q=100&dpl=dpl_9GUvYRYkSXVcp9398feaiSHuz7SE)

This year Xcode previews got a big upgrade with the new execution engine in Xcode 16. Apple has been giving us many new preview related features such as UIKit support in `#Preview` macros, `@Previewable` to manage state, and `PreviewModifier` to reuse data. These make adopting previews easier and increase the popularity of [preview driven development](https://emergetools.com/blog/posts/preview-driven-development?utm_medium=blog&utm_source=emerge-tools&utm_campaign=blog-post).

However, previews can be prone to unexpected breaks. For example, say someone on your team adds a property to a view that uses `@EnvironmentObject`. If they forget to update every callsite to set the environment, the app will crash. Any preview that uses the view without an environment will also crash when Xcode tries to render the preview. This problem is even tricker because Xcode doesn’t have a built-in way to test that previews will not crash without manually testing each one - this would take an impossibly long time. Some companies like [Doordash](https://careersatdoordash.com/blog/how-to-speed-up-swiftui-development-and-testing-using-previewsnapshots/?utm_medium=blog&utm_source=emerge-tools&utm_campaign=blog-post) and [Handshake](https://joinhandshake.com/blog/our-team/effortless-ios-snapshot-testing-using-emerge-tools/?utm_medium=blog&utm_source=emerge-tools&utm_campaign=blog-post) have written about how they use previews for their snapshot tests - one technique to catch failing previews. In this post, we’ll look at an even simpler way - writing a unit test that does a layout pass of all previews using Emerge's open-source [SnapshotPreviews](https://github.com/EmergeTools/SnapshotPreviews?utm_medium=blog&utm_source=emerge-tools&utm_campaign=blog-post) Swift Package.

# An example

Consider these two views in different files:

```swift
// Title.swift
struct Title: View {
  let title: String
  
  var body: some View {
    Text(title)
      .font(.largeTitle)
  }
}

#Preview {
  Title(title: "Title")
}

// TitleSubtitle.swift
struct TitleSubtitle: View {
  let title: String
  let subtitle: String

  var body: some View {
    HStack {
      Title(title: title)
      Text(subtitle)
    }
  }
}

#Preview {
  TitleSubtitle(title: "Title", subtitle: "subtitle")
}
```

Now a change is made to add an environment object theme in `Title`

```swift
final class Theme: ObservableObject {
    @Published var textColor: Color = .gray
}

struct Title: View {
  @EnvironmentObject var theme: Theme
  let title: String

    var body: some View {
    Text(title)
      .font(.largeTitle)
      .foregroundStyle(theme.textColor)
  }
}

#Preview {
  Title(title: "Title")
    .environmentObject(Theme()) // crashes without this!
}
```

This is correct for the preview in `Title.swift`, but causes a crash in `TitleSubtitle.swift`! It would be easily fixed if you knew the previews that eventually use a `Title`, but in a large codebase, this could be in a file you’ve never even seen before.

## [Adding tests](https://www.emergetools.com/blog/posts/unit-test-xcode-previews#adding-tests)

Instead of manually testing each preview, you can write a unit test that automatically runs every preview in your app or framework. Just link the [SnapshotPreviews](https://github.com/EmergeTools/SnapshotPreviews?utm_medium=blog&utm_source=emerge-tools&utm_campaign=blog-post) package _to your test target_ and copy the following code:

```swift
import SnapshottingTests

// This is an XCTestCase you can run in Xcode
final class MyPreviewTest: PreviewLayoutTest { }
```

Test functions will be automatically added for every preview in the app. You can easily view the results in Xcode or automate it to run as part of CI using Fastlane or `xcodebuild`.

A successful result will look like this:

![Test result](https://www.emergetools.com/_next/image?url=%2Fimages%2Fblogs%2Fblog30%2FtestOutput.png&w=1920&q=75&dpl=dpl_9GUvYRYkSXVcp9398feaiSHuz7SE)

and the previous example will result in a crash with a stacktrace pinpointing the problem:

![Crash result](https://www.emergetools.com/_next/image?url=%2Fimages%2Fblogs%2Fblog30%2FcrashOutput.png&w=1920&q=75&dpl=dpl_9GUvYRYkSXVcp9398feaiSHuz7SE)

## [How it works](https://www.emergetools.com/blog/posts/unit-test-xcode-previews#how-it-works)

This works by reading the Swift type metadata in the app binary to find all protocol conformance records to `PreviewProvider`. The conforming type is dynamically initialized and called to get the SwiftUI View for each provider. Then, the view is decomposed into each preview using [VariadicView](https://www.emergetools.com/blog/posts/how-to-use-variadic-view?utm_medium=blog&utm_source=emerge-tools&utm_campaign=blog-post).

A new test function is added to the test class for each discovered preview thanks, to the dynamic nature of the Objective-C runtime. Since this is automatic, you don’t have to write any code, just add the new previews to your app and they are tested!

## [Concluding thoughts](https://www.emergetools.com/blog/posts/unit-test-xcode-previews#concluding-thoughts)

Writing tests always seems like the worst part of testing, and this is an easy way to get a lot of test coverage without having to write any tests! Typically, unit tests don’t include view related code, so this is also a great way to increase the code coverage percentage beyond the usual unit tests. Lastly, although the example we looked at in this post is not a bug in the production app, it still would waste developer time if it was not caught with a test because anyone using the affected previews would have to wait for a fix. Catching these issues pre-merge is a great way to speed up preview driven development!
