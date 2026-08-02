---
title: 'TalkingToTheLiveView: Sending messages to a Swift Playground live view and
  saving data to its key-value store'
apple_id: TP40017380
resource_type: Sample Code
platform: iOS
topic: Swift
technology: null
published: '2016-09-13'
source_url: https://developer.apple.com/library/archive/samplecode/TalkingToTheLiveView/Introduction/Intro.html
archived_at: '2026-07-27T06:57:10.612300Z'
---
> 导航：[总目录](../README.md) · [samplecode](../_indexes/samplecode.md)



# TalkingToTheLiveView: Sending messages to a Swift Playground live view and saving data to its key-value store

|  |  |
| --- | --- |
| __Last Revision:__ | Version 1.0, 2016-09-13 First release |
| __Build Requirements:__ | Xcode 8.0 or later; iOS 10.0 SDK or later |
| __Runtime Requirements:__ | iOS 10.0 or later; Swift Playgrounds on iPad |

This Playground Book demonstrates how to talk to the always-on live view process from the main process running the code in the editor.

Examples include:
\* Using the PlaygroundSupport framework
\* Encoding/decoding structs to and from PlaygroundValue cases
\* Talking to the PlaygroundRemoteLiveViewProxy to send messages between the always-on live view process and the main process
\* Using the PlaygroundKeyValueStore to remember things for the next time you open the document
