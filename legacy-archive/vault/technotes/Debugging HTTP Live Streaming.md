---
title: Debugging HTTP Live Streaming
apple_id: DTS40017666
resource_type: Technical Note
platform: tvOS|iOS|macOS
topic: Audio, Video, & Visual Effects
technology: AVFoundation
published: '2017-08-25'
source_url: https://developer.apple.com/library/archive/technotes/tn2436/_index.html
archived_at: '2026-07-26T19:54:15.345790Z'
---
> 导航：[总目录](../README.md) · [technotes](../_indexes/technotes.md)



Technical Note TN2436

# Debugging HTTP Live Streaming

This document is intended for AVFoundation clients and content owners that are debugging issues when playing HTTP live streaming (HLS) content. For AVFoundation clients, this document provides an overview of the various types of errors that can be encountered during the playback of HLS content as well as an overview of the various facilities for applications to be notified of errors that occur during the playback process from the AVPlayer. For contents owners, this document provides useful information about verifying HLS content against the HTTP Live Streaming Authoring Specification for Apple Devices. This document also provides links to helpful resources and tools available for AVFoundation clients and content owners to use during debugging as well as best practices that lead to better playback experience.

[Debugging HTTP Live Streaming](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgnbqgaytonrwgywugsbrfvcekqsvi5dustshl5efivcql5gesvsfl5jviusfifgustsh)[Types of Errors Encountered During Playback](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgnbqgaytonrwgywugsbrfvcekqsvi5dustshl5efivcql5gesvsfl5jviusfifgustshfvkfsucfknpu6rs7ivjfet2sknpuktsdj5ku4vcfkjcuix2ekvjestshl5ieyqkzijaugsy)[Discovering Errors](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgnbqgaytonrwgywugsbrfvcekqsvi5dustshl5efivcql5gesvsfl5jviusfifgustshfvcesu2dj5lekusjjzdv6rkskjhveuy)[Verifying Content](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgnbqgaytonrwgywugsbrfvcekqsvi5dustshl5efivcql5gesvsfl5jviusfifgustshfvlekusjizmustshl5bu6tsuivhfi)[Helpful Resources](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgnbqgaytonrwgywugsbrfvcekqsvi5dustshl5efivcql5gesvsfl5jviusfifgustshfveektcqizkuyx2sivju6vksincvg)[Document Revision History](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgnbqgaytonrwgywvezlwnfzws33ojbuxg5dpoj4s2rdpnz2ey2lonncwyzlnmvxhiskel4yq)

## Debugging HTTP Live Streaming

HTTP Live Streaming (HLS) reliably delivers media content across a variety of network and bandwidth conditions. This document discusses best practices for handling errors during playback of HLS content with AVFoundation.

### Types of Errors Encountered During Playback

When an [AVPlayer](https://developer.apple.com/documentation/avfoundation/avplayer) encounters an error during playback, the type of error typically falls into one of the following categories:

- Network Errors:

  All the 4XX and 5XX errors that are sent from the server as well as TCP/IP and DNS errors.

  With regards to 4XX and 5XX errors, it is important to make sure that when your server encounters these errors that it sends an error that AVFoundation expects. This ensures that AVFoundation handles these errors in such a way that alternate playback options such as backup sources or lower bitrate variants are used if they are available and playback can continue smoothly.

  For more information about how your server should be handling and returning errors see the following video:

  - [WWDC 2017 - Session 514: Error Handling Best Practices for HTTP Live Streaming](https://developer.apple.com/videos/play/wwdc2017/514/)
- Timeout Errors:

  When resources such as the master playlist, media playlists, media files and content keys are requested there are timeouts defined. A failure to get a response within this timeout will cause timeout errors.
- Format Errors:

  Format errors occur when an incorrect format is used for the playlist, key or session data. If you are encountering this class of error, see the "Verifying Content" section below.
- Live Playlist Update Errors:

  In the case of a live stream, playlists need to be updated according to the published target duration and failure to update in time will result in a live playlist update error.

### Discovering Errors

The AVFoundation framework provide several facilities for applications to be notified of errors that occur during the playback process from the [AVPlayer](https://developer.apple.com/documentation/avfoundation/avplayer).

#### Getting Notified When Errors Occur

To be notified of when an error occurs, the AVFoundation client or app should register for Key-Value Observing (KVO) on the [AVPlayer.status](https://developer.apple.com/documentation/avfoundation/avplayer/1388096-status) and [AVPlayer.currentItem.status](https://developer.apple.com/documentation/avfoundation/avplayeritem/1389493-status) properties. If an error occurs at any point during the playback process, the values of these properties will change to [AVPlayerStatus.failed](https://developer.apple.com/documentation/avfoundation/avplayerstatus) and [AVPlayerItemStatus.failed](https://developer.apple.com/documentation/avfoundation/avplayeritemstatus) respectively. For the exact error that caused the status to change to `.failed`, look at [AVPlayerItem.error](https://developer.apple.com/documentation/avfoundation/avplayeritem/1389185-error).

__Listing 1__  Getting notified when errors occur.

```swift
func beginPlayback () {
    let hlsAsset = AVURLAsset(url: assetURL)
    let playerItem = AVPlayerItem(asset: hlsAsset)
    player = AVPlayer(playerItem: playerItem)

    let playerObserver = player.observe(\AVPlayer.status, options: [.new, .initial]) { (player, _) in
                if player.status == .failed {
                    guard let error = player.currentItem?.error else { return }

                    // Handle error accordingly.
                }
    }

    let playerItemObserver = playerItem.observe(\AVPlayerItem.status, options: [.new, .initial]) { (item, _) in
                if item.status == .failed {
                    guard let error = item.error else { return }

                    // Handle error accordingly.
                }
    }
}
```

__Important:__ The User-info dictionary of [AVPlayerItem.error](https://developer.apple.com/documentation/avfoundation/avplayeritem/1389185-error) contains the underlying error, this can be nested if more than one error is causing the failure.

It is important to note that the [AVPlayerItem.status](https://developer.apple.com/documentation/avfoundation/avplayeritem/1389493-status) property will only change to `.failed` after:

- There are no viable alternate variants to use to continue playback.
- [AVPlayer](https://developer.apple.com/documentation/avfoundation/avplayer) has played out its current buffer.

#### Getting Notified When AVPlayerItem Failed To Play To Completion

Your application can also observe the [AVPlayerItemFailedToPlayToEndTimeNotification](https://developer.apple.com/documentation/foundation/nsnotification.name/1388007-avplayeritemfailedtoplaytoendtim) to be notified if the [AVPlayerItem](https://developer.apple.com/documentation/avfoundation/avplayeritem) did not play to completion. The `userInfo` dictionary of this notification contains the error that describes the problem that was encountered and can be retrieved using the [AVPlayerItemFailedToPlayToEndTimeErrorKey](https://developer.apple.com/documentation/avfoundation/avplayeritemfailedtoplaytoendtimeerrorkey) key.

__Listing 2__  Getting notified when AVPlayerItem failed to play to completion.

```
...
// Listen to notification
NotificationCenter.default.addObserver(self,
                                        selector:#selector(failedToPlayToEndTime:),
                                        name: .AVPlayerItemFailedToPlayToEndTimeNotification,
                                        object: player.currentItem)
...
```

__Listing 3__  Responding to AVPlayerItemFailedToPlayToEndTimeNotification.

```swift
func failedToPlayToEndTime(notification: Notification) {
    guard let userInfo = notification.userInfo, let error = userInfo[AVPlayerItemFailedToPlayToEndTimeErrorKey] as? Error else {
        return
    }

    // Handle Error accordingly.
}
```

#### Getting Detailed Error Logs

If your application needs to know all the error events that happened during the playback session for analytics or debugging then it should call [AVPlayerItem.errorLog()](https://developer.apple.com/documentation/avfoundation/avplayeritem/1387573-errorlog) which will return an instance of [AVPlayerItemErrorLog](https://developer.apple.com/documentation/avfoundation/avplayeritemerrorlog) if errors were encountered during playback.

[AVPlayerItemErrorLog](https://developer.apple.com/documentation/avfoundation/avplayeritemerrorlog) includes an array containing [AVPlayerItemErrorLogEvent](https://developer.apple.com/documentation/avfoundation/avplayeritemerrorlogevent) objects that represent the chronological sequence of events contained in the error log.

To be notified when a new entry has been added to the error log, add an observer for the [AVPlayerItemNewErrorLogEntryNotification](https://developer.apple.com/documentation/foundation/nsnotification.name/1388450-avplayeritemnewerrorlogentry).

__Listing 4__  Getting detailed error logs.

```
...
// Listen to notification
NotificationCenter.default.addObserver(self,
                                        selector:#selector(newErrorLogEntry),
                                        name: .AVPlayerItemNewErrorLogEntry,
                                        object: player.currentItem)
...
```

__Listing 5__  Responding to new error log entries.

```swift
func newErrorLogEntry() {
    guard let errorLog = player.currentItem.errorLog() else {
        return
    }

    for event in errorLog.events {
        // Handle error events accordingly.
    }

}
```

### Verifying Content

If you are encountering format errors during playback, it is important to test the validity of any playlist streams using the Media Stream Validator tool, `mediastreamvalidator`. This tool verifies that the index file and media segments conform to the [HTTP Live Streaming Authoring Specification for Apple Devices](https://developer.apple.com/library/content/documentation/General/Reference/HLSAuthoringSpec/Requirements.html#//apple_ref/doc/uid/TP40016596-CH2-SW1). It performs several checks to ensure reliable streaming. If any errors or problems are found, a detailed diagnostic report is displayed. It is important to address the issues that the `mediastreamvalidator` finds to ensure that the AVFoundation framework handles your content in an expected way.

__Important:__ The validator does not do low-level bitstream checks, you should be using third-party tools if you think you may have issues with your encoders.

The Authoring Specification is Apple's advice for authoring HLS content. This is different from the HTTP Live Streaming Internet-Draft which includes only absolutely necessary requirements. The Authoring Specification, on the other hand, includes requirements that are specific to Apple's players, as well as things that, while not absolutely required, are part of best practice.

iOS or Mac Developer Program members can download the latest version of the Media Stream Validator from the Apple Developer Connection website. To download, go to [Apple Developer Downloads](https://developer.apple.com/download/more/), in the search field type "HTTP Live Streaming Tools", download and install the 'HTTP Live Streaming Tools'.

Instructions for using the tools can be found in the man pages for each tool. For example, launch the Terminal app and type `man mediastreamvalidator` to see these.

Once you run the `mediastreamvalidator` against your stream, you can run the `hlsreport.py` tool which is included as part of the 'HTTP Live Streaming Tools' package. What this tool does is take the JSON output of `mediastreamvalidator` and generates an HTML page with the contents of the report.

__Important:__ When running the `mediastreamvalidator`, you should always run the `hlsreport.py` tool as it can surface information from the JSON that is not immediately apparent in the raw JSON output of the `mediastreamvalidator` tool.

The document [Media Stream Validator Tool Results Explained](https://developer.apple.com/library/content/technotes/tn2235/_index.html) discusses any error message that may be returned from the Media Stream Validator tool.

You may also find the following resources useful in verifying that your HLS content is authored in a way that is supported by Apple devices:

- [WWDC 2016 - Session 510: Validating HTTP Live Streams](https://developer.apple.com/videos/play/wwdc2016/510/)
- [HLS Authoring Specification for Apple Devices](https://developer.apple.com/library/content/documentation/General/Reference/HLSAuthoringSpec/Requirements.html#//apple_ref/doc/uid/TP40016596-CH2-SW1)

### Helpful Resources

- General information regarding HLS on supported Apple devices and platforms:
- - [HTTP Live Streaming (HLS) - Apple Developer](https://developer.apple.com/streaming/)
  - [AV Foundation - Apple Developer](https://developer.apple.com/av-foundation/)
- Information regarding authoring HLS content for devices and platforms:
- - [HLS Authoring Specification for Apple Devices](https://developer.apple.com/library/content/documentation/General/Reference/HLSAuthoringSpec/index.html#//apple_ref/doc/uid/TP40016596-CH4-SW1)
  - [WWDC 2016 - Session 510: Validating HTTP Live Streams](https://developer.apple.com/videos/play/wwdc2016/510/)
  - [WWDC 2017 - Session 515: HLS Authoring Update](https://developer.apple.com/videos/play/wwdc2017/515/)
- Information regarding error handling on the server side and with AVFoundation on supported Apple devices and platforms:
- - [WWDC 2017 - Session 514: Error Handling Best Practices for HTTP Live Streaming](https://developer.apple.com/videos/play/wwdc2017/514/)
[Back to Top](#)

---

#### Document Revision History

| __Date__ | __Notes__ |
| 2017-08-25 | Fixed URLs referenced in this document. |
| 2017-08-04 | New document that how to debug issues related to HTTP Live Streaming. |

