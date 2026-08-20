---
title: 'AVAutoWait: Using AVFoundation to play HTTP assets with minimal stalls'
apple_id: TP40017477
resource_type: Sample Code
platform: iOS
topic: null
technology: AVFoundation
published: '2016-09-13'
source_url: https://developer.apple.com/library/archive/samplecode/AVAutoWait/Listings/AVAutoWait_MediaSelectionTableViewController_swift.html
archived_at: '2026-07-18T03:00:00.617141Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [AVAutoWait: Using AVFoundation to play HTTP assets with minimal stalls](AVAutoWait-%20Using%20AVFoundation%20to%20play%20HTTP%20assets%20with%20minimal%20stalls.md)


[Next](AVAutoWait-PlaybackDetailsViewController.swift.md)[Previous](AVAutoWait-PlaybackViewController.swift.md)

# AVAutoWait/MediaSelectionTableViewController.swift

```swift
/*
    Copyright (C) 2016 Apple Inc. All Rights Reserved.
    See LICENSE.txt for this sample’s licensing information

    Abstract:
    Main view controller where user interaction begins. Allows the user to select a media item from a table view.
*/
import UIKit

/// Table view controller that manages our available media items. All user action starts here.
class MediaSelectionTableViewController: UITableViewController {
    // MARK: Types

    private struct MediaItem {
        let name: String
        let url: URL
    }

    // MARK: Properties
    private let mediaItems = [
        MediaItem(name: "In the Woods",
                  url: URL(string: "http://devimages.apple.com.edgekey.net/samplecode/avfoundationMedia/AVFoundationQueuePlayer_Progressive.mov")!),

        // Add your own media items here.
    ]

    // MARK: UITableViewDataSource

    override func numberOfSections(in tableView: UITableView) -> Int {
        return 1
    }

    override func tableView(_ tableView: UITableView, numberOfRowsInSection section: Int) -> Int {
        return mediaItems.count
    }

    override func tableView(_ tableView: UITableView, cellForRowAt indexPath: IndexPath) -> UITableViewCell {
        let cell = tableView.dequeueReusableCell(withIdentifier: "Media", for: indexPath)
        cell.textLabel?.text = mediaItems[indexPath.row].name

        return cell
    }

    // MARK: UIViewController

    override func prepare(for segue: UIStoryboardSegue, sender: AnyObject?) {
        if segue.identifier == "ShowMedia", let mediaVC = segue.destination as? MediaViewController, let itemIndex = tableView.indexPathForSelectedRow?.row {

            // Set the selected URL on the destionation view controller.
            mediaVC.mediaURL = self.mediaItems[itemIndex].url
        }
    }
}
```

[Next](AVAutoWait-PlaybackDetailsViewController.swift.md)[Previous](AVAutoWait-PlaybackViewController.swift.md)

