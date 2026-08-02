---
title: QTKit Capture - Disabling specific audio channels when recording
apple_id: DTS40008045
resource_type: QA
platform: macOS
topic: Audio, Video, & Visual Effects
technology: QTKit
published: '2008-10-13'
source_url: https://developer.apple.com/library/archive/qa/qa1617/_index.html
archived_at: '2026-07-18T02:32:47.020353Z'
---
> 导航：[总目录](../README.md) · [qa](../_indexes/qa.md)



Technical Q&A QA1617

# QTKit Capture - Disabling specific audio channels when recording

## Q:  How can I disable specific audio channels when recording?

A: How can I disable specific audio channels when recording?

Use the `QTCaptureConnectionEnabledAudioChannelsAttribute` attribute, an `NSIndexSet` value that specifies which audio channels should be sent through the connection.

To use the attribute, run the session (start capturing data) and then observe when the format description of the connection changes. Applications can be notified of changes to a connection’s format by registering to receive the `QTCaptureConnectionFormatDescriptionDidChangeNotification` notification as shown in Listing 1.

__Listing 1__  Registering for the `QTCaptureConnectionFormatDescriptionDidChangeNotification` notification.

```
 // Register for changes to a connection's format   [[NSNotificationCenter defaultCenter] addObserver:self      selector:@selector(connectionFormatDidChange:)      name:QTCaptureConnectionFormatDescriptionDidChangeNotification      object:nil];
```

Once this change notification fires, you should first check if the attribute is writable, and then use it to enable the desired audio channels on the connection.

__Listing 2__  Using the `QTCaptureConnectionEnabledAudioChannelsAttribute` attribute to enable audio channels on the connection.

```
 // This method called when the connection format changes   - (void)connectionFormatDidChange:(NSNotification *)notification   {     // You may now use the QTCaptureConnectionEnabledAudioChannelsAttribute     // attribute to enable audio channels for the connection     [self enableAudioChannelsForConnection:[self myAudioCaptureConnection]];   }    // Specify the audio channels that should be used on the connection   -(void) enableAudioChannelsForConnection:(QTCaptureConnection *)captureConnection   {     // Make sure attribute is writeable before we use it     if ([captureConnection attributeIsReadOnly:       QTCaptureConnectionEnabledAudioChannelsAttribute] == NO)     {       NSRange channelIndexes;       channelIndexes.location = 0;       channelIndexes.length = 2;       NSIndexSet *channelIndexSet =          [NSIndexSet indexSetWithIndexesInRange:channelIndexes];        // Example: enable audio channels 1,2 (only) for the connection       [captureConnection setAttribute:channelIndexSet          forKey:QTCaptureConnectionEnabledAudioChannelsAttribute];     }   }
```


[Technical Q&A QA1607 QTKit Capture - Disabling Audio Or Video When Capturing From a Muxed Device](https://developer.apple.com/qa/qa2008/qa1607.html)

---

#### Document Revision History

| __Date__ | __Notes__ |
| 2008-10-13 | New document that describes how to disable specific audio channels when recording using QTKit Capture. |

