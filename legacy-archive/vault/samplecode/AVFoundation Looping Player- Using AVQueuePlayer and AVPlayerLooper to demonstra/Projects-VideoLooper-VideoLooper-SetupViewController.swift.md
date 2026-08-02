---
title: 'AVFoundation Looping Player: Using AVQueuePlayer and AVPlayerLooper to demonstrate
  loop playback'
apple_id: TP40014695
resource_type: Sample Code
platform: iOS|macOS
topic: Audio, Video, & Visual Effects
technology: AVFoundation
published: '2016-09-13'
source_url: https://developer.apple.com/library/archive/samplecode/avloopplayer/Listings/Projects_VideoLooper_VideoLooper_SetupViewController_swift.html
archived_at: '2026-07-18T03:28:58.185767Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [AVFoundation Looping Player: Using AVQueuePlayer and AVPlayerLooper to demonstrate loop playback](AVFoundation%20Looping%20Player-%20Using%20AVQueuePlayer%20and%20AVPlayerLooper%20to%20demonstra.md)


[Next](Projects-VideoLooper-VideoLooper-LooperViewController.swift.md)[Previous](Projects-VideoLooper-VideoLooper-QueuePlayerLooper.swift.md)

# Projects/VideoLooper/VideoLooper/SetupViewController.swift

```swift
/*
    Copyright (C) 2016 Apple Inc. All Rights Reserved.
    See LICENSE.txt for this sample’s licensing information

    Abstract:
    View to allow the user to configure the video looping playback and select the method to perform the looping.
*/

import UIKit

class SetupViewController: UIViewController, UIPickerViewDelegate, UIPickerViewDataSource {
    // MARK: SegueHandlerType

    enum SegueIdentifier: String {
        case queuePlayerLooper = "QueuePlayerLooper"

        case playerLooper = "PlayerLooper"
    }

    // MARK: Properties

    var mediaFileList = [String]()

    var mediaURLList = [URL]()

    var loopOptionStringList = [String]()

    var loopOptionValueList = [Int]()

    var selectedMediaFileIndex = 0

    var selectedLoopOptionIndex = 0

    // MARK: Interface Builder outlets

    @IBOutlet weak var filePicker: UIPickerView!

    @IBOutlet weak var loopCountPicker: UIPickerView!

    // MARK: UIViewController

    override func viewDidLoad() {
        super.viewDidLoad()

        mediaFileList = ["Sweep", "BipBop"]

        mediaURLList = [URL(fileURLWithPath:Bundle.main.path(forResource: "maskOff", ofType: "mov")!),
                        URL(fileURLWithPath:Bundle.main.path(forResource: "ChoppedBipBop", ofType: "m4v")!)]

        loopOptionStringList = ["Infinite", "2", "3", "5", "7", "10"]
        loopOptionValueList = [-1, 2, 3, 5, 7, 10]

        filePicker.dataSource = self
        filePicker.delegate = self
        loopCountPicker.dataSource = self
        loopCountPicker.delegate = self
    }

    override func prepare(for segue: UIStoryboardSegue, sender: Any?) {
        guard let looperViewController = segue.destination as? LooperViewController,
            let identifier = segue.identifier,
            let segueIdentifier = SegueIdentifier(rawValue: identifier)
        else {
            return
        }


        let videoURL = mediaURLList[selectedMediaFileIndex]
        let loopCount = loopOptionValueList[selectedLoopOptionIndex]

        switch segueIdentifier {
            case .queuePlayerLooper:
                looperViewController.looper = QueuePlayerLooper(videoURL: videoURL, loopCount: loopCount)

            case .playerLooper:
                looperViewController.looper = PlayerLooper(videoURL: videoURL, loopCount: loopCount)
        }
    }

    // MARK: UIPickerViewDataSource

    func numberOfComponents(in pickerView: UIPickerView) -> Int {
        return 1
    }

    func pickerView(_ pickerView: UIPickerView, numberOfRowsInComponent component: Int) -> Int {
        switch pickerView {
            case filePicker:
                return mediaFileList.count

            case loopCountPicker:
                return loopOptionStringList.count

            default:
                return 0
        }
    }

    func pickerView(_ pickerView: UIPickerView, titleForRow row: Int, forComponent component: Int) -> String? {
        switch pickerView {
            case filePicker:
                return mediaFileList[row]

            case loopCountPicker:
                return loopOptionStringList[row]

            default:
                return nil
        }
    }


    // MARK: UIPickerViewDelegate

    func pickerView(_ pickerView: UIPickerView, didSelectRow row: Int, inComponent component: Int) {
        switch pickerView {
            case filePicker:
                selectedMediaFileIndex = row

            case loopCountPicker:
                selectedLoopOptionIndex = row

            default:
                fatalError("Picker selected unknown row \(row) in component \(component)")
        }
    }
}
```

[Next](Projects-VideoLooper-VideoLooper-LooperViewController.swift.md)[Previous](Projects-VideoLooper-VideoLooper-QueuePlayerLooper.swift.md)

