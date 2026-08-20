---
title: Accessing Audio Files in Asset Catalogs
apple_id: DTS40016671
resource_type: QA
platform: tvOS|iOS|macOS
topic: Audio, Video, & Visual Effects
technology: AVFoundation
published: '2016-10-31'
source_url: https://developer.apple.com/library/archive/qa/qa1913/_index.html
archived_at: '2026-07-18T02:36:08.152720Z'
---
> 导航：[总目录](../../README.md) · [qa](../../_indexes/qa.md)



Technical Q&A QA1913

# Accessing Audio Files in Asset Catalogs

## Q:  How do I add and access audio files stored in asset catalogs?

A: Asset catalogs allow you to manage your app resources. They can include files such as icons, images, audio and video files, and watch complications. See [Xcode Help > Work with Assets > Asset Catalogs](http://help.apple.com/xcode/mac/8.0/#/dev10510b1f7) for more information about asset catalogs.

Asset catalogs use data sets to create and manage audio files. See [Xcode Help > Work with Assets > Asset Catalogs > Create a data set](http://help.apple.com/xcode/mac/8.0/#/dev10510b1f7) for more information on how to use them to add your audio files as shown in Figure 1.

__Figure 1__  Sound data asset that contains an audio file.

!!

The [NSDataAsset](https://developer.apple.com/reference/uikit/nsdataasset) class allows you to access an object from a data set stored in an asset catalog. Create and initialize an instance of `NSDataAsset` with your data set's name, then use its [data](https://developer.apple.com/reference/uikit/nsdataasset/1403437-data) property to access your audio file in the asset catalog as shown in Listing 1.

__Listing 1__  Accessing and playing an audio file stored in the Sound data set

```swift
import AVFoundation

var player: AVAudioPlayer?

 @IBAction func play(_ sender: UIButton){
    // Fetch the Sound data set.
    if let asset = NSDataAsset(name:"Sound"){

       do {
             // Use NSDataAsset's data property to access the audio file stored in Sound.
              player = try AVAudioPlayer(data:asset.data, fileTypeHint:"caf")
             // Play the above sound file.
             player?.play()
       } catch let error as NSError {
             print(error.localizedDescription)
       }
    }
 }
```


---

#### Document Revision History

| __Date__ | __Notes__ |
| 2016-10-31 | Fixed typo in code listing. Updated for Xcode 8. |
| 2015-12-26 | New document that describes how to add and access audio files stored in asset catalogs. |

