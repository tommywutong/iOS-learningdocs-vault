---
title: iOS 13
source: NSHipster (Mattt)
source_key: nshipster
source_url: 'https://nshipster.com/ios-13/'
original_language: en
published: 2019-09-23
status: active
license: CC BY-NC（页脚明示）→ 可非商业再分发，须署名
archived_at: 2026-07-27
content_hash: 'sha256:3daa7532ced1bf4e'
translated: false
---

> 原文：[iOS 13](https://nshipster.com/ios-13/)　·　NSHipster (Mattt)

# [iOS 13](https://nshipster.com/ios-13/)

Written by  [Mattt](https://nshipster.com/authors/mattt/)  September 23^rd, 2019

Apple announced a lot at WWDC this year. During the conference and the days that followed, a lot of us walked around in a daze, attempting to recover from have our minds _“hashtag-mindblown’d”_ (#🤯). But now a few months later, after everything announced has launched _([well, almost everything](https://appleinsider.com/articles/19/09/16/what-apple-is-holding-back-for-ios-131))_ those very same keynote announcements now elicit far different reactions:

Dark Mode?

😎 [Already covered it](https://nshipster.com/dark-mode/).

SwiftUI?

🙄 [Give it another year or two](https://nshipster.com/wwdc-2019/).

Augmented Reality?

🥱 [Wake us up when Apple announces AR glasses.](http://appleinsider.com/articles/17/01/09/rumor-apple-working-with-carl-zeiss-on-ar-glasses-to-debut-in-2018)

Although the lion’s share of attention has been showered on the aforementioned features, not nearly enough coverage has been given to the rest of iOS 13 — and that’s a shame, because this release is among the most exciting in terms of new functionality and satisfying in terms of improving existing functionality.

So to mark last week’s release of iOS 13, we’re taking a look at some obscure (largely undocumented) APIs that you can now use in your apps. We’ve scavenged the best bits out of the [iOS 13 Release Notes](https://developer.apple.com/documentation/ios_ipados_release_notes/ios_13_release_notes) [API diffs](http://codeworkshop.net/objc-diff/sdkdiffs/ios/13.0/), and now present them to you.

Here are some of our favorite things you can do starting in iOS 13:

---

## Generate Rich Representations of URLs

New in iOS 13, the [LinkPresentation framework](https://developer.apple.com/documentation/LinkPresentation) provides a convenient, built-in way to replicate the rich previews of URLs you see in Messages. If your app has any kind of chat or messaging functionality, you’ll definitely want to check this out.

Rich previews of URLs have a rich history going at least as far back as the early ’00s, with the spread of [Microformats](http://microformats.org) by semantic web pioneers, and early precursors to Digg and Reddit using [khtml2png](https://github.com/xsuchy/khtml2png) to generate thumbnail images of web pages. Fast forward to 2010, with the rise of social media and user-generated content, when Facebook created the [OpenGraph protocol](https://ogp.me) to allow web publishers to customize how their pages looked when posted on the Newsfeed.

These days, most websites reliably have OpenGraph `<meta>` tags on their site that provide a summary of their content for social networks, search engines, and anywhere else that links are trafficked. For example, here’s what you would see if you did “View Source” for this very webpage:

```
<meta property="og:site_name" content="NSHipster" />
<meta property="og:image" content="https://nshipster.com/logo.png" />
<meta property="og:type" content="article" />
<meta property="og:title" content="iOS 13" />
<meta property="og:url" content="https://nshipster.com/ios-13/" />
<meta property="og:description" content="To mark last week's release of iOS 13, we're taking a look at some obscure (largely undocumented) APIs that you can now use in your apps." />
```

If you wanted to consume this information in your app, you can now use the LinkPresentation framework’s `LPMetadataProvider` class to fetch the metadata and optionally construct a representation:

```
import LinkPresentation

let metadataProvider = LPMetadataProvider()
let url = URL(string: "https://nshipster.com/ios-13/")!

metadataProvider.startFetchingMetadata(for: url) { [weak self] metadata, error in
    guard let metadata = metadata else { return }

    let linkView = LPLinkView(metadata: metadata)
    self?.view.addSubview(linkView)
}
```

After setting appropriate constraints (and perhaps a call to `sizeToFit()`), you’ll get the following, which the user can tap to preview the linked webpage:

![iOS 13 Link View](https://nshipster.com/assets/ios-13-link-view--light-945c7ca785dafd897f6c7e5ed8a3a66cc867e3bb69d6eb38380f2ca517029ee0e1d28972f6f394cfc32ba2687006a36ece8e4cc5f551d535cfd514c37d32367a.png)

Alternatively, if you already have the metadata in-app, or otherwise can’t or don’t want to fetch remotely, you can construct an `LPLinkMetadata` directly:

```
let metadata = LPLinkMetadata()
metadata.url = url
metadata.title = "iOS 13"
metadata.iconProvider = …

let linkView = LPLinkView(metadata: metadata)
```

## Perform On-Device Speech Recognition

[`SFSpeechRecognizer`](https://developer.apple.com/documentation/speech/sfspeechrecognizer) gets a major upgrade in iOS 13 — most notably for its added support for on-device speech recognition.

Previously, transcription required an internet connection and was restricted to a maximum of 1-minute duration with daily limits for requests. But now, you can do speech recognition completely on-device and offline, with no limitations. The only caveats are that offline transcription isn’t as good as what you’d get with a server connection, and is only available for certain languages.

To determine whether offline transcription is available for the user’s locale, check the `SFSpeechRecognizer` property [`supportsOnDeviceRecognition`](https://developer.apple.com/documentation/speech/sfspeechrecognizer/3152604-supportsondevicerecognition). At the time of publication, the list of supported languages are as follows:

English United States (`en-US`) Canada (`en-CA`) Great Britain (`en-GB`) India (`en-IN`) Spanish United States (`es-US`) Mexico (`es-MX`) Spain (`es-ES`) Italian Italy (`it-IT`) Portuguese Brazil (`pt-BR`) Russian Russia (`ru-RU`) Turkish Turkey (`tr-TR`) Chinese Mandarin (`zh-cmn`) Cantonese (`zh-yue`)

But that’s not all for speech recognition in iOS 13! `SFSpeechRecognizer` now provides information including speaking rate and average pause duration, as well as voice analytics features like jitter (variations in pitch) and shimmer (variations in amplitude).

```
import Speech

guard SFSpeechRecognizer.authorizationStatus() == .authorized,
    let recognizer = SFSpeechRecognizer()
else {
    fatalError()
}

let url: URL = …
let request = SFSpeechURLRecognitionRequest(url: url)

recognizer.recognitionTask(with: request) { (result, error) in
    guard let result = result else { return }

    for segment in result.bestTranscription.segments {
        guard let voiceAnalytics = segment.voiceAnalytics else { continue }

        let pitch = voiceAnalytics.pitch.acousticFeatureValuePerFrame
        let voicing = voiceAnalytics.voicing.acousticFeatureValuePerFrame
        let jitter = voiceAnalytics.jitter.acousticFeatureValuePerFrame
        let shimmer = voiceAnalytics.shimmer.acousticFeatureValuePerFrame
    }
}
```

Information about pitch and voicing and other features could be used by your app (perhaps [in coordination with CoreML](https://developer.apple.com/documentation/createml/mlsoundclassifier)) to differentiate between speakers or determine subtext from a speaker’s inflection.

## Send and Receive Web Socket Messages

Speaking of the Foundation URL Loading System, we now have native support for something that’s been at the top of our wish list for many years: web sockets.

Thanks to the new [`URLSessionWebSocketTask`](https://developer.apple.com/documentation/foundation/urlsessionwebsockettask) class in iOS 13, you can now incorporate real-time communications in your app as easily and reliably as sending HTTP requests — all without any third-party library or framework:

```
let url = URL(string: "wss://…")!
let webSocketTask = URLSession.shared.webSocketTask(with: url)
webSocketTask.resume()

// Send one message
let message: URLSessionWebSocketTask.Message = .string("Hello, world!")
webSocketTask.send(message) { error in
    …
}

// Receive one message
webSocketTask.receive { result in
    guard case let .success(message) = result else { return }
    …
}

// Eventually...
webSocketTask.cancel(with: .goingAway, reason: nil)
```

For years now, networking has been probably the fastest-moving part of the whole Apple technology stack. Each WWDC, there’s so much to talk about that that they routinely have to break their content across two separate sessions. 2019 was no exception, and we highly recommend that you take some time to check out this year’s “Advances in Networking” sessions ([Part 1](https://developer.apple.com/videos/play/wwdc2019/712/), [Part 2](https://developer.apple.com/videos/play/wwdc2019/713)).

## Do More With Maps

MapKit is another part of Apple SDKs that’s consistently had a strong showing at WWDC year after year. And it’s often the small touches that make the most impact in our day-to-day.

For instance, the new [`MKMapView.CameraBoundary`](https://developer.apple.com/documentation/mapkit/mkmapview/cameraboundary) API in iOS 13 makes it much easier to constrain a map’s viewport to a particular region without locking it down completely.

```
let region = MKCoordinateRegion(center: mapView.center,
                                        latitudinalMeters: 1000,
                                        longitudinalMeters: 1000)
mapView.cameraBoundary = MKMapView.CameraBoundary(coordinateRegion: region)
```

And with the new [`MKPointOfInterestFilter`](https://developer.apple.com/documentation/mapkit/mkpointofinterestfilter) API, you can now customize the appearance of map views to show only certain kinds of points of interest _(whereas previously it was an [all-or-nothing](https://developer.apple.com/documentation/mapkit/mkmapview/1452102-showspointsofinterest) proposition)_.

```
let filter = MKPointOfInterestFilter(including: [.cafe])
mapView.pointOfInterestFilter = filter // only show cafés
```

Finally, with [`MKGeoJSONDecoder`](https://developer.apple.com/documentation/mapkit/mkgeojsondecoder), we now have a built-in way to pull in [GeoJSON](https://geojson.org) shapes from web services and other data sources.

```
let decoder = MKGeoJSONDecoder()

if let url = URL(string: "…"),
    let data = try? Data(contentsOfURL: url),
    let geoJSONObjects = try? decoder.decode(data) {

    for case let overlay as MKOverlay in geoJSONObjects {
        mapView.addOverlay(overlay)
    }
}
```

## Keep Promises in JavaScript

If you enjoyed our article about [JavaScriptCore](https://nshipster.com/javascriptcore/), you’d be thrilled to know that `JSValue` objects [now natively support promises](https://developer.apple.com/documentation/javascriptcore/jsvalue/3335012-init).

For the uninitiated: in JavaScript, a [`Promise`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise) is an object that represents the eventual completion (or rejection) of an asynchronous operation and its resulting value. Promises are a mainstay of modern JS development — perhaps most notably within the [`fetch`](https://developer.mozilla.org/en-US/docs/Web/API/Fetch_API) API.

Another addition to JavaScriptCore in iOS 13 is support for [symbols](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Symbol) (no, not [those symbols](https://developer.apple.com/design/human-interface-guidelines/sf-symbols/)). For more information about [`init(newSymbolFromDescription:in:)`](https://developer.apple.com/documentation/javascriptcore/jsvalue/3042804-init), ~~refer to the docs~~ just guess how to use it.

## Respond to Objective-C Associated Objects (?)

On a lark, we decided to see if there was anything new in Objective-C this year and were surprised to find out about [objc_setHook_setAssociatedObject](https://developer.apple.com/documentation/objectivec/objc_hook_setassociatedobject?language=objc). Again, we don’t have much to go on except the declaration, but it looks like you can now configure a block to execute when an [associated object](https://nshipster.com/associated-objects/) is set. For anyone still deep in the guts of the Objective-C runtime, this sounds like it could be handy.

## Tame Activity Items (?)

On the subject of missing docs: [`UIActivityItemsConfiguration`](https://developer.apple.com/documentation/uikit/uiactivityitemsconfiguration) _seems_ like a compelling option for managing actions in the new iOS 13 share sheets, but we don’t really know where to start…

![iOS 13 Share Actions](https://nshipster.com/assets/ios-13-share-actions-e6d29c2be2d47a7eb901772745888015a3e84e43f87fedef150e38a5f4bd19d970f12f0d6635573b0389f63b86f15408f81d65938c42daa0babc743d864f9055.png)

Shame that we don’t have the information we need to take advantage of this yet.

## Format Lists and Relative Times

As discussed in [a previous article](https://nshipster.com/formatter/), iOS 13 brings two new formatters to Foundation: [`ListFormatter`](https://developer.apple.com/documentation/foundation/listformatter) and [`RelativeDateTimeFormatter`](https://developer.apple.com/documentation/foundation/relativedatetimeformatter).

Not to harp on about this, but both of them are _still_ undocumented, so if you want to learn more, we’d recommend checking out that article from July. Or, if you’re in a rush here’s a quick example demonstrating how to use both of them together:

```
import Foundation

let relativeDateTimeFormatter = RelativeDateTimeFormatter()
relativeDateTimeFormatter.dateTimeStyle = .named

let listFormatter = ListFormatter()
listFormatter.string(from: [
    relativeDateTimeFormatter.localizedString(from: DateComponents(day: -1)),
    relativeDateTimeFormatter.localizedString(from: DateComponents(day: 0)),
    relativeDateTimeFormatter.localizedString(from: DateComponents(day: 1))
]) // "yesterday, today, and tomorrow"
```

## Track the Progress of Enqueued Operations

Starting in iOS 13, `OperationQueue` now has a [`progress`](https://developer.apple.com/documentation/foundation/operationqueue/3172535-progress) property.

Granted, [`(NS)Progress`](https://developer.apple.com/documentation/foundation/progress) objects aren’t the most straightforward or convenient things to work with (we’ve been meaning to write an article about them at some point), but they have a complete and well-considered API, and even have some convenient slots in app frameworks.

For example, check out how easy it is to wire up a `UIProgressView` to display the live-updating progress of an operation queue by way of its [`observedProgress` property](https://developer.apple.com/documentation/uikit/uiprogressview/1619840-observedprogress):

```
import UIKit

fileprivate class DownloadOperation: Operation { … }

class ViewController: UIViewController {
    private let operationQueue = {
        let queue = OperationQueue()
        queue.maxConcurrentOperationCount = 1
    }()

    @IBOutlet private var progressView: UIProgressView!

    @IBAction private func startDownloading(_ sender: Any) {
        operationQueue.cancelAllOperations()
        progressView.observedProgress = operationQueue.progress

        for url in […] {
            let operation = DownloadOperation(url: url)
            operationQueue.addOperation(operation)
        }
    }
}
```

It’s also worth mentioning a few other APIs coming to in 13, like [`schedule(after:interval:tolerance:options:_:)`](https://developer.apple.com/documentation/foundation/operationqueue/3329364-schedule), which clues `OperationQueue` into the new [Combine framework](https://developer.apple.com/documentation/combine) in a nice way, and [`addBarrierBlock(_:)`](https://developer.apple.com/documentation/foundation/operationqueue/3172534-addbarrierblock), which presumably works like [Dispatch barrier blocks](https://developer.apple.com/documentation/dispatch/1452917-dispatch_barrier_sync?language=objc) (though without documentation, it’s anyone’s guess).

## Manage Background Tasks with Ease

One of the things that often differentiates category-defining apps from their competitors is their use of background tasks to make sure the app is fully synced and updated for the next time it enters the foreground.

iOS 7 was the first release to provide [an official API for scheduling background tasks](https://developer.apple.com/documentation/uikit/uiapplication/1623051-beginbackgroundtask) _(though developers had employed various creative approaches prior to this)_. But in the intervening years, multiple factors — from an increase in iOS app capabilities and complexity to growing emphasis in performance, efficiency, and privacy for apps — have created a need for a more comprehensive solution.

That solution came to iOS 13 by way of the new [BackgroundTasks framework](https://developer.apple.com/documentation/backgroundtasks?language=objc).

As described in this year’s WWDC session [“Advances in App Background Execution”](https://developer.apple.com/videos/play/wwdc2019/707), the framework distinguishes between two broad classes of background tasks:

- app refresh tasks: short-lived tasks that keep an app up-to-date throughout the day
- background processing tasks: long-lived tasks for performing deferrable maintenance tasks

The WWDC session and the accompanying sample code project do a great job of explaining how to incorporate both of these into your app. But if you want the quick gist of it, here’s a small example of an app that schedules periodic refreshes from a web server:

```
import UIKit
import BackgroundTasks

fileprivate let backgroundTaskIdentifier = "com.nshipster.example.task.refresh"

@UIApplicationMain
class AppDelegate: UIResponder, UIApplicationDelegate {
    var window: UIWindow?

    lazy var backgroundURLSession = {
        let configuration = URLSessionConfiguration.background(withIdentifier: "com.nshipster.url-session.background")
        configuration.discretionary = true
        configuration.timeoutIntervalForRequest = 30

        return URLSession(configuration: configuration, delegate: …, delegateQueue: …)
    }

    func application(_ application: UIApplication, didFinishLaunchingWithOptions launchOptions: [UIApplication.LaunchOptionsKey: Any]?) -> Bool {
       …

        BGTaskScheduler.shared.register(forTaskWithIdentifier: backgroundTaskIdentifier, using: nil) { task in
            self.handleAppRefresh(task: task as! BGAppRefreshTask)
        }

        return true
    }

    func applicationDidEnterBackground(_ application: UIApplication) {
        scheduleAppRefresh()
    }

    func scheduleAppRefresh() {
        let request = BGAppRefreshTaskRequest(identifier: backgroundTaskIdentifier)
        request.earliestBeginDate = Date(timeIntervalSinceNow: 60 * 10)

        do {
            try BGTaskScheduler.shared.submit(request)
        } catch {
            print("Couldn't schedule app refresh: \(error)")
        }
    }

    func handleAppRefresh(task: BGAppRefreshTask) {
        scheduleAppRefresh()

        let url: URL = …
        var dataTask = backgroundURLSession.dataTask(with: url) { (data, response, error) in
            …
            let success = (200..<300).contains(response?.statusCode)
            task.setTaskCompleted(success: success)
        }

        task.expirationHandler = {
            dataTask.cancel()
        }

        dataTask.resume()
    }

    …
}
```

## Annotate Text Content Types for Better Accessibility

You know how frustrating it is to hear some people read out URLs? (_“eɪʧ ti ti pi ˈkoʊlən slæʃ slæʃ ˈdʌbəlju ˈdʌbəlju ˈdʌbəlju dɑt”…_) That’s what it can be like when [VoiceOver](https://www.apple.com/accessibility/iphone/vision/) tries to read something without knowing more about _what_ it’s reading.

iOS 13 promises to improve the situation considerably with the new [`accessibilityTextualContext`](https://developer.apple.com/documentation/objectivec/nsobject/3075456-accessibilitytextualcontext) property and [`UIAccessibilityTextAttributeContext`](https://developer.apple.com/documentation/uikit/uiaccessibilitytextattributecontext) `NSAttributedString` attribute key. Whenever possible, be sure to annotate views and attributed strings with the constant that best describes the kind of text being displayed:

- `UIAccessibilityTextualContextConsole`
- `UIAccessibilityTextualContextFileSystem`
- `UIAccessibilityTextualContextMessaging`
- `UIAccessibilityTextualContextNarrative`
- `UIAccessibilityTextualContextSourceCode`
- `UIAccessibilityTextualContextSpreadsheet`
- `UIAccessibilityTextualContextWordProcessing`

## Remove Implicitly Unwrapped Optionals from View Controllers Initialized from Storyboards

SwiftUI may have signaled the eventual end of Storyboards, but that doesn’t mean that things aren’t and won’t continue to get better until if / when that day comes.

One of the most irritating anti-patterns for Swift purists when working on iOS projects with Storyboards has been view controller initialization. Due to an impedance mismatch between Interface Builder’s “prepare for segues” approach and Swift’s object initialization rules, we frequently had to choose between making all of our properties non-private, variable, and (implicitly unwrapped) optionals, or foregoing Storyboards entirely.

Xcode 11 and iOS 13 allow these paradigms to reconcile their differences by way of the new `@IBSegueAction` attribute and some new `UIStoryboard` class methods:

First, the `@IBSegueAction` attribute can be applied view controller method declarations to designate itself as the API responsible for creating a segue’s destination view controller _(i.e. the `destinationViewController` property of the `segue` parameter in the `prepare(for:sender:)` method)_.

```
@IBSegueAction
func makeProfileViewController(coder: NSCoder, sender: Any?, segueIdentifier: String?) -> ProfileViewController? {
    ProfileViewController(
        coder: coder,
        name: self.selectedName,
        avatarImageURL: self.selectedAvatarImageURL
    )
}
```

Second, the `UIStoryboard` class methods [`instantiateInitialViewController(creator:)`](https://developer.apple.com/documentation/uikit/uistoryboard/3213988-instantiateinitialviewcontroller) and [`instantiateViewController(identifier:creator:)`](https://developer.apple.com/documentation/uikit/uistoryboard/3213989-instantiateviewcontroller`) offer a convenient block-based customization point for instantiating a Storyboard’s view controllers.

```
import UIKit

struct Person { … }

class ProfileViewController: UIViewController {
    let name: String
    let avatarImageURL: URL?

    init?(coder: NSCoder, name: String, avatarImageURL: URL?) {
        self.name = name
        self.avatarImageURL = avatarImageURL

        super.init(coder: coder)
    }

    required init?(coder: NSCoder) {
        fatalError("init(coder:) has not been implemented")
    }
}

let storyboard = UIStoryboard(name: "ProfileViewController", bundle: nil)
storyboard.instantiateInitialViewController(creator: { decoder in
    ProfileViewController(
        coder: decoder,
        name: "Johnny Appleseed",
        avatarImageURL: nil
    )
})
```

Together with the new [UIKit Scene](https://developer.apple.com/documentation/uikit/app_and_environment/scenes) APIs, iOS 13 gives us a lot to work with as we wait for SwiftUI to mature and stabilize.

---

That does it for our round-up of iOS 13 features that you may have missed. But rest assured — we’re planning to cover many more new APIs in future NSHipster articles.

If there’s anything we missed that you’d like for us to cover, please [@ us on Twitter](https://twitter.com/nshipster)!
