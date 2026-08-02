---
title: 'MusicMotion: Adding Motion Awareness to a Music App'
apple_id: TP40016160
resource_type: Sample Code
platform: iOS
topic: null
technology: CoreMotion
published: '2016-09-28'
source_url: https://developer.apple.com/library/archive/samplecode/MusicMotion/Listings/MusicMotion_SongViewController_swift.html
archived_at: '2026-07-18T03:16:33.032184Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [MusicMotion: Adding Motion Awareness to a Music App](MusicMotion-%20Adding%20Motion%20Awareness%20to%20a%20Music%20App.md)


[Next](MusicMotion-Song.swift.md)[Previous](MusicMotion-MotionManager.swift.md)

# MusicMotion/SongViewController.swift

```swift
/*
Copyright (C) 2016 Apple Inc. All Rights Reserved.
See LICENSE.txt for this sample’s licensing information

Abstract:
This class manages the presentation of the queued songs and updates when the users context changes.
*/

import UIKit

class SongViewController: UIViewController, UITableViewDataSource, UITableViewDelegate, SongManagerDelegate {
    // MARK: Properties

    static let textCellIdentifier = "SongCell"

    @IBOutlet weak var songTableView: UITableView!
    @IBOutlet weak var albumView: UIImageView!

    let motionManager = MotionManager()
    let songManager = SongManager()
    var cachedSongQueue = [Song]()

    // MARK: View Controller

    override func viewDidLoad() {
        super.viewDidLoad()

        setNeedsStatusBarAppearanceUpdate()

        motionManager.delegate = songManager

        /*
            This is currently needed to allow the Motion Activity Access dialog
            to appear in front of the app, instead of behind it.
        */
        DispatchQueue.main.async {
            self.motionManager.startMonitoring()
        }

        songManager.delegate = self

        // Save the inital queue to present to the user.
        cachedSongQueue = songManager.songQueue

        updateAlbumViewWithSong(nil)

        selectFirstRow()
    }

    func updateAlbumViewWithSong(_ song: Song?) {
        // If no song is passed in, just use the first song in the queue.
        guard let song = song ?? cachedSongQueue.first else { return }

        albumView.image = song.albumImage
    }

    func selectFirstRow() {
        let rowToSelect = IndexPath(row: 0, section: 0)

        songTableView.selectRow(at: rowToSelect, animated: false, scrollPosition: .none)

        tableView(songTableView, didSelectRowAt: rowToSelect)
    }

    // MARK: UITableViewDataSource

    func tableView(_ tableView: UITableView, numberOfRowsInSection section: Int) -> Int {
        return cachedSongQueue.count
    }

    func tableView(_ tableView: UITableView, cellForRowAt indexPath: IndexPath) -> UITableViewCell {
        let cell = tableView.dequeueReusableCell(withIdentifier: SongViewController.textCellIdentifier, for: indexPath)

        let song = cachedSongQueue[indexPath.row]

        cell.textLabel!.text = song.artist
        cell.detailTextLabel!.text = song.title

        return cell
    }

    func tableView(_ tableView: UITableView, titleForHeaderInSection section: Int) -> String? {
        // Create the header based on the intensity. For example "Low Intensity Music".
        return songManager.contextDescription
    }

    // MARK: UITableViewDelegate

    func tableView(_ tableView: UITableView, didSelectRowAt indexPath: IndexPath) {
        let song = cachedSongQueue[indexPath.row]

        updateAlbumViewWithSong(song)
    }

    // MARK: SongManagerDelegate

    func didUpdateSongQueue(_ manager: SongManager) {
        let indexSet = IndexSet(integer: 0)

        // Cache the songs to avoid modifications to the data outside the view controller.
        cachedSongQueue = manager.songQueue

        DispatchQueue.main.async {
            self.songTableView.reloadSections(indexSet, with: .fade)

            self.updateAlbumViewWithSong(nil)

            self.selectFirstRow()
        }
    }

    func didEncounterAuthorizationError(_ manager: SongManager) {
        let title = NSLocalizedString("Motion Activity Not Authorized", comment: "")

        let message = NSLocalizedString("To enable Motion features, please allow access to Motion & Fitness in Settings under Privacy.", comment: "")

        let alert = UIAlertController(title: title, message: message, preferredStyle: .alert)

        let cancelAction = UIAlertAction(title: "Cancel", style: .cancel, handler: nil)
        alert.addAction(cancelAction)

        let openSettingsAction = UIAlertAction(title: "Open Settings", style: .default) { _ in
            // Open the Settings app.
            let url = URL(string: UIApplicationOpenSettingsURLString)!

            UIApplication.shared.openURL(url)
        }

        alert.addAction(openSettingsAction)

        DispatchQueue.main.async {
            self.present(alert, animated: true, completion:nil)
        }
    }
}
```

[Next](MusicMotion-Song.swift.md)[Previous](MusicMotion-MotionManager.swift.md)

